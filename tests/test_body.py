"""``Body`` replay on retry, and file handling.

A retry can only re-send a body it can reopen, so these tests put a zapros
``MockMiddleware`` between the client and the real network handler: the first
attempts are answered with a 500 by one-shot mocks, the retry passes through,
and the object is read back from the backend byte for byte.
"""

from __future__ import annotations

import fcntl
import gc
import os
from collections.abc import AsyncIterator, Iterator
from contextlib import asynccontextmanager, contextmanager
from pathlib import Path

import pytest
from capo_s3 import AsyncS3Client, Body, S3Client
from capo_s3.errors import NotFound, ServiceError
from zapros import AsyncStdNetworkHandler, Response, StdNetworkHandler, ZaprosError
from zapros.mock import Mock, MockMiddleware, MockRouter

from tests.conftest import (
    aread_body,
    astream,
    make_async_s3_client,
    make_s3_client,
    parts_of,
    read_body,
    stream,
    unique_name,
)

DATA = os.urandom(4 * 1024 * 1024)

ERROR_XML = (
    b'<?xml version="1.0" encoding="UTF-8"?>'
    b"<Error><Code>InternalError</Code><Message>injected by tests</Message><RequestId>0</RequestId></Error>"
)


def fail_next(router: MockRouter, n: int) -> None:
    """Answer the next ``n`` requests with a retryable 500; later ones pass through.

    Each mock is ``once()``, so ``router.verify()`` asserts every fault was hit.
    """
    for _ in range(n):
        response = Response(500, headers={"Content-Type": "application/xml"}, content=ERROR_XML)
        router.add(Mock().respond(response).once())


@pytest.fixture
def data_file(tmp_path: Path) -> Path:
    path = tmp_path / "data.bin"
    path.write_bytes(DATA)
    return path.resolve()


@pytest.fixture
def router() -> MockRouter:
    return MockRouter()


@pytest.fixture
def faulty_s3(s3_backend: str, router: MockRouter) -> Iterator[S3Client]:
    middleware = MockMiddleware(router, next_handler=StdNetworkHandler())
    with make_s3_client(s3_backend, http_handler=middleware) as client:
        yield client


@pytest.fixture
async def faulty_async_s3(s3_backend: str, router: MockRouter) -> AsyncIterator[AsyncS3Client]:
    middleware = MockMiddleware(router, next_handler=AsyncStdNetworkHandler())
    async with make_async_s3_client(s3_backend, http_handler=middleware) as client:
        yield client


def is_open(path: Path) -> bool:
    """Whether this process holds a file descriptor on ``path``."""
    getpath = getattr(fcntl, "F_GETPATH", None)  # macOS; Linux resolves /proc/self/fd instead
    for fd in os.listdir("/dev/fd"):
        try:
            if getpath is not None:
                opened = fcntl.fcntl(int(fd), getpath, bytes(1024)).rstrip(b"\0").decode()
            else:
                opened = os.readlink(f"/proc/self/fd/{fd}")
        except OSError:
            continue
        if opened == str(path):
            return True
    return False


class TestAsyncBodyReplay:  # unasync: generate
    async def test_body_is_replayed_after_500(
        self,
        faulty_async_s3: AsyncS3Client,
        async_s3: AsyncS3Client,
        router: MockRouter,
        bucket: str,
        data_file: Path,
    ):
        fail_next(router, 2)
        await faulty_async_s3.put_object(bucket, "replay.bin", body=Body.async_from_path(data_file))
        router.verify()
        assert await aread_body(async_s3.get_object(bucket, "replay.bin")) == DATA

    async def test_gives_up_after_max_attempts(
        self,
        faulty_async_s3: AsyncS3Client,
        async_s3: AsyncS3Client,
        router: MockRouter,
        bucket: str,
        data_file: Path,
    ):
        fail_next(router, 3)
        body = Body.async_from_path(data_file)
        with pytest.raises(ServiceError):
            await faulty_async_s3.put_object(bucket, "never.bin", body=body)
        router.verify()
        assert body.stream is None
        assert not is_open(data_file)
        with pytest.raises(NotFound):
            await async_s3.head_object(bucket, "never.bin")

    async def test_bytes_body_is_replayed(
        self,
        faulty_async_s3: AsyncS3Client,
        async_s3: AsyncS3Client,
        router: MockRouter,
        bucket: str,
    ):
        fail_next(router, 1)
        await faulty_async_s3.put_object(bucket, "bytes.bin", body=DATA)
        router.verify()
        assert await aread_body(async_s3.get_object(bucket, "bytes.bin")) == DATA

    async def test_one_shot_iterator_is_not_retried(
        self,
        faulty_async_s3: AsyncS3Client,
        async_s3: AsyncS3Client,
        router: MockRouter,
        bucket: str,
    ):
        fail_next(router, 1)
        with pytest.raises(ServiceError):
            await faulty_async_s3.put_object(
                bucket,
                "once.bin",
                body=astream(parts_of(DATA)),
                content_length=len(DATA),
            )
        router.verify()
        with pytest.raises(NotFound):
            await async_s3.head_object(bucket, "once.bin")

    async def test_upload_part_body_is_replayed(
        self,
        faulty_async_s3: AsyncS3Client,
        async_s3: AsyncS3Client,
        router: MockRouter,
        bucket: str,
        data_file: Path,
    ):
        upload_id = (await async_s3.create_multipart_upload(bucket, "mpu.bin"))["upload_id"]
        fail_next(router, 1)
        part = await faulty_async_s3.upload_part(
            bucket,
            "mpu.bin",
            part_number=1,
            upload_id=upload_id,
            body=Body.async_from_path(data_file),
        )
        router.verify()
        await async_s3.complete_multipart_upload(
            bucket,
            "mpu.bin",
            upload_id=upload_id,
            multipart_upload={"parts": [{"part_number": 1, "e_tag": part["e_tag"]}]},
        )
        assert await aread_body(async_s3.get_object(bucket, "mpu.bin")) == DATA

    async def test_opener_is_entered_once_per_attempt(
        self,
        faulty_async_s3: AsyncS3Client,
        router: MockRouter,
        bucket: str,
    ):
        state = {"enter": 0, "exit": 0}

        @asynccontextmanager
        async def opener() -> AsyncIterator[tuple[AsyncIterator[bytes], int]]:
            state["enter"] += 1
            try:
                yield astream(parts_of(DATA)), len(DATA)
            finally:
                state["exit"] += 1

        fail_next(router, 2)
        await faulty_async_s3.put_object(bucket, "opener.bin", body=Body(opener))
        assert state == {"enter": 3, "exit": 3}

        state = {"enter": 0, "exit": 0}
        with pytest.raises((ServiceError, ZaprosError)):  # either way one attempt, see TestAsyncEarlyResponse
            await faulty_async_s3.put_object(unique_name("no-such-bucket"), "k", body=Body(opener))
        assert state == {"enter": 1, "exit": 1}

    async def test_opener_that_cannot_reopen_stops_the_retries(
        self,
        faulty_async_s3: AsyncS3Client,
        async_s3: AsyncS3Client,
        router: MockRouter,
        bucket: str,
    ):
        opens = 0

        @asynccontextmanager
        async def opener() -> AsyncIterator[tuple[AsyncIterator[bytes], int] | None]:
            nonlocal opens
            opens += 1
            yield (astream(parts_of(DATA)), len(DATA)) if opens == 1 else None

        fail_next(router, 1)
        with pytest.raises(ServiceError):
            await faulty_async_s3.put_object(bucket, "k", body=Body(opener))
        router.verify()
        with pytest.raises(NotFound):
            await async_s3.head_object(bucket, "k")


class TestBodyReplay:  # unasync: generated
    def test_body_is_replayed_after_500(
        self,
        faulty_s3: S3Client,
        s3: S3Client,
        router: MockRouter,
        bucket: str,
        data_file: Path,
    ):
        fail_next(router, 2)
        faulty_s3.put_object(bucket, "replay.bin", body=Body.from_path(data_file))
        router.verify()
        assert read_body(s3.get_object(bucket, "replay.bin")) == DATA

    def test_gives_up_after_max_attempts(
        self,
        faulty_s3: S3Client,
        s3: S3Client,
        router: MockRouter,
        bucket: str,
        data_file: Path,
    ):
        fail_next(router, 3)
        body = Body.from_path(data_file)
        with pytest.raises(ServiceError):
            faulty_s3.put_object(bucket, "never.bin", body=body)
        router.verify()
        assert body.stream is None
        assert not is_open(data_file)
        with pytest.raises(NotFound):
            s3.head_object(bucket, "never.bin")

    def test_bytes_body_is_replayed(
        self,
        faulty_s3: S3Client,
        s3: S3Client,
        router: MockRouter,
        bucket: str,
    ):
        fail_next(router, 1)
        faulty_s3.put_object(bucket, "bytes.bin", body=DATA)
        router.verify()
        assert read_body(s3.get_object(bucket, "bytes.bin")) == DATA

    def test_one_shot_iterator_is_not_retried(
        self,
        faulty_s3: S3Client,
        s3: S3Client,
        router: MockRouter,
        bucket: str,
    ):
        fail_next(router, 1)
        with pytest.raises(ServiceError):
            faulty_s3.put_object(
                bucket,
                "once.bin",
                body=stream(parts_of(DATA)),
                content_length=len(DATA),
            )
        router.verify()
        with pytest.raises(NotFound):
            s3.head_object(bucket, "once.bin")

    def test_upload_part_body_is_replayed(
        self,
        faulty_s3: S3Client,
        s3: S3Client,
        router: MockRouter,
        bucket: str,
        data_file: Path,
    ):
        upload_id = (s3.create_multipart_upload(bucket, "mpu.bin"))["upload_id"]
        fail_next(router, 1)
        part = faulty_s3.upload_part(
            bucket,
            "mpu.bin",
            part_number=1,
            upload_id=upload_id,
            body=Body.from_path(data_file),
        )
        router.verify()
        s3.complete_multipart_upload(
            bucket,
            "mpu.bin",
            upload_id=upload_id,
            multipart_upload={"parts": [{"part_number": 1, "e_tag": part["e_tag"]}]},
        )
        assert read_body(s3.get_object(bucket, "mpu.bin")) == DATA

    def test_opener_is_entered_once_per_attempt(
        self,
        faulty_s3: S3Client,
        router: MockRouter,
        bucket: str,
    ):
        state = {"enter": 0, "exit": 0}

        @contextmanager
        def opener() -> Iterator[tuple[Iterator[bytes], int]]:
            state["enter"] += 1
            try:
                yield stream(parts_of(DATA)), len(DATA)
            finally:
                state["exit"] += 1

        fail_next(router, 2)
        faulty_s3.put_object(bucket, "opener.bin", body=Body(opener))
        assert state == {"enter": 3, "exit": 3}

        state = {"enter": 0, "exit": 0}
        with pytest.raises((ServiceError, ZaprosError)):  # either way one attempt, see TestEarlyResponse
            faulty_s3.put_object(unique_name("no-such-bucket"), "k", body=Body(opener))
        assert state == {"enter": 1, "exit": 1}

    def test_opener_that_cannot_reopen_stops_the_retries(
        self,
        faulty_s3: S3Client,
        s3: S3Client,
        router: MockRouter,
        bucket: str,
    ):
        opens = 0

        @contextmanager
        def opener() -> Iterator[tuple[Iterator[bytes], int] | None]:
            nonlocal opens
            opens += 1
            yield (stream(parts_of(DATA)), len(DATA)) if opens == 1 else None

        fail_next(router, 1)
        with pytest.raises(ServiceError):
            faulty_s3.put_object(bucket, "k", body=Body(opener))
        router.verify()
        with pytest.raises(NotFound):
            s3.head_object(bucket, "k")


class TestAsyncEarlyResponse:  # unasync: generate
    async def test_error_response_during_upload_is_reported(
        self,
        async_s3: AsyncS3Client,
        s3_backend: str,
        request: pytest.FixtureRequest,
    ):
        # The server can answer before the whole body arrived; the client should
        # still deliver that answer rather than the failure of its own write.
        if s3_backend == "minio":
            request.applymarker(
                pytest.mark.xfail(
                    strict=True,
                    raises=ZaprosError,
                    reason="MinIO answers 404 and closes the socket before the 4 MiB body is written; "
                    "the write failure is raised instead of the service error",
                )
            )
        with pytest.raises(ServiceError) as info:
            await async_s3.put_object(unique_name("no-such-bucket"), "k", body=DATA)
        assert info.value.code == "NoSuchBucket"


class TestEarlyResponse:  # unasync: generated
    def test_error_response_during_upload_is_reported(
        self,
        s3: S3Client,
        s3_backend: str,
        request: pytest.FixtureRequest,
    ):
        # The server can answer before the whole body arrived; the client should
        # still deliver that answer rather than the failure of its own write.
        if s3_backend == "minio":
            request.applymarker(
                pytest.mark.xfail(
                    strict=True,
                    raises=ZaprosError,
                    reason="MinIO answers 404 and closes the socket before the 4 MiB body is written; "
                    "the write failure is raised instead of the service error",
                )
            )
        with pytest.raises(ServiceError) as info:
            s3.put_object(unique_name("no-such-bucket"), "k", body=DATA)
        assert info.value.code == "NoSuchBucket"


class TestAsyncBodyFiles:  # unasync: generate
    async def test_file_is_closed_after_every_call(self, async_s3: AsyncS3Client, bucket: str, data_file: Path):
        # With the collector off, only deterministic closing keeps the descriptor count at zero.
        gc.disable()
        try:
            body = Body.async_from_path(data_file)
            for i in range(3):
                await async_s3.put_object(bucket, f"ok-{i}.bin", body=Body.async_from_path(data_file))
                assert not is_open(data_file)
                await async_s3.put_object(bucket, f"reuse-{i}.bin", body=body)
                assert body.stream is None
                assert not is_open(data_file)
                with pytest.raises((ServiceError, ZaprosError)):  # see TestAsyncEarlyResponse
                    await async_s3.put_object(unique_name("no-such-bucket"), "k", body=Body.async_from_path(data_file))
                assert not is_open(data_file)
        finally:
            gc.enable()
        assert await aread_body(async_s3.get_object(bucket, "reuse-2.bin")) == DATA

    async def test_from_path_roundtrip(self, async_s3: AsyncS3Client, bucket: str, data_file: Path):
        body = Body.async_from_path(data_file)
        await async_s3.put_object(bucket, "a.bin", body=body)
        await async_s3.put_object(bucket, "b.bin", body=body)
        assert await aread_body(async_s3.get_object(bucket, "a.bin")) == DATA
        assert await aread_body(async_s3.get_object(bucket, "b.bin")) == DATA


class TestBodyFiles:  # unasync: generated
    def test_file_is_closed_after_every_call(self, s3: S3Client, bucket: str, data_file: Path):
        # With the collector off, only deterministic closing keeps the descriptor count at zero.
        gc.disable()
        try:
            body = Body.from_path(data_file)
            for i in range(3):
                s3.put_object(bucket, f"ok-{i}.bin", body=Body.from_path(data_file))
                assert not is_open(data_file)
                s3.put_object(bucket, f"reuse-{i}.bin", body=body)
                assert body.stream is None
                assert not is_open(data_file)
                with pytest.raises((ServiceError, ZaprosError)):  # see TestEarlyResponse
                    s3.put_object(unique_name("no-such-bucket"), "k", body=Body.from_path(data_file))
                assert not is_open(data_file)
        finally:
            gc.enable()
        assert read_body(s3.get_object(bucket, "reuse-2.bin")) == DATA

    def test_from_path_roundtrip(self, s3: S3Client, bucket: str, data_file: Path):
        body = Body.from_path(data_file)
        s3.put_object(bucket, "a.bin", body=body)
        s3.put_object(bucket, "b.bin", body=body)
        assert read_body(s3.get_object(bucket, "a.bin")) == DATA
        assert read_body(s3.get_object(bucket, "b.bin")) == DATA
