"""HTTP caching of S3 downloads through zapros' ``CacheMiddleware`` (hishel).

A repeat download must go out as a conditional request (``If-None-Match``)
and come back as a bodiless ``304``, with the body served from the cache; a
changed object must be transferred again. See the Caching section of the
README for the user-facing recipe these tests pin down.
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from pathlib import Path
from typing import cast

import pytest
from capo_s3 import AsyncS3Client, S3Client
from hishel import AsyncSqliteStorage, CacheOptions, SpecificationPolicy, SyncSqliteStorage
from zapros import (
    AsyncBaseHandler,
    AsyncBaseMiddleware,
    AsyncStdNetworkHandler,
    BaseHandler,
    BaseMiddleware,
    CacheMiddleware,
    Request,
    Response,
    StdNetworkHandler,
)

from tests.conftest import aread_body, make_async_s3_client, make_s3_client, needs_threads, read_body

# hishel's async sqlite storage runs on worker threads (anysqlite)
pytestmark = needs_threads

KEY = "big.bin"
DATA = b"capo " * 1000
NEW_DATA = b"CAPO " * 2000

# (method, sent If-None-Match, status) of every request that reached the network
WireEntry = tuple[str, bool, int]


class Wire(AsyncBaseMiddleware, BaseMiddleware):
    """Records what actually goes over the wire, below the cache."""

    def __init__(self, next_handler: AsyncBaseHandler | BaseHandler, log: list[WireEntry]) -> None:
        self.next = cast(BaseHandler, next_handler)
        self.async_next = cast(AsyncBaseHandler, next_handler)
        self._log = log

    def _record(self, request: Request, response: Response) -> None:
        if KEY in str(request.url):  # skip credential-provider traffic on AWS
            self._log.append((request.method, "if-none-match" in request.headers, response.status))

    async def ahandle(self, request: Request) -> Response:
        response = await self.async_next.ahandle(request)
        self._record(request, response)
        return response

    def handle(self, request: Request) -> Response:
        response = self.next.handle(request)
        self._record(request, response)
        return response


def make_cached_s3(backend: str, db: Path, log: list[WireEntry], *, private: bool = True) -> S3Client:
    """A client whose downloads go through a cache persisted in ``db``.

    ``private`` selects the policy the README recommends; the default (shared)
    policy refuses to store responses to requests carrying ``Authorization``.
    """
    cache = CacheMiddleware(
        Wire(StdNetworkHandler(), log),
        policy=SpecificationPolicy(CacheOptions(shared=False)) if private else None,
        storage=SyncSqliteStorage(database_path=db),
    )
    return make_s3_client(backend, http_handler=cache)


def make_cached_async_s3(backend: str, db: Path, log: list[WireEntry], *, private: bool = True) -> AsyncS3Client:
    """Async twin of :func:`make_cached_s3`."""
    cache = CacheMiddleware(
        Wire(AsyncStdNetworkHandler(), log),
        policy=SpecificationPolicy(CacheOptions(shared=False)) if private else None,
        storage=AsyncSqliteStorage(database_path=db),
    )
    return make_async_s3_client(backend, http_handler=cache)


@pytest.fixture
def cache_db(tmp_path: Path) -> Path:
    return tmp_path / "s3-cache.db"


@pytest.fixture
def wire_log() -> list[WireEntry]:
    return []


@pytest.fixture
def cached_s3(s3_backend: str, cache_db: Path, wire_log: list[WireEntry]) -> Iterator[S3Client]:
    with make_cached_s3(s3_backend, cache_db, wire_log) as client:
        yield client


@pytest.fixture
async def cached_async_s3(s3_backend: str, cache_db: Path, wire_log: list[WireEntry]) -> AsyncIterator[AsyncS3Client]:
    async with make_cached_async_s3(s3_backend, cache_db, wire_log) as client:
        yield client


class TestAsyncCaching:  # unasync: generate
    async def test_repeat_download_is_revalidated_not_transferred(
        self, cached_async_s3: AsyncS3Client, bucket: str, wire_log: list[WireEntry]
    ):
        await cached_async_s3.put_object(bucket, KEY, body=DATA, cache_control="no-cache")
        wire_log.clear()

        assert await aread_body(cached_async_s3.get_object(bucket, KEY)) == DATA
        assert await aread_body(cached_async_s3.get_object(bucket, KEY)) == DATA

        assert wire_log == [("GET", False, 200), ("GET", True, 304)]

    async def test_changed_object_is_downloaded_again(
        self, cached_async_s3: AsyncS3Client, bucket: str, wire_log: list[WireEntry]
    ):
        await cached_async_s3.put_object(bucket, KEY, body=DATA, cache_control="no-cache")
        assert await aread_body(cached_async_s3.get_object(bucket, KEY)) == DATA

        await cached_async_s3.put_object(bucket, KEY, body=NEW_DATA, cache_control="no-cache")
        wire_log.clear()

        assert await aread_body(cached_async_s3.get_object(bucket, KEY)) == NEW_DATA
        assert wire_log == [("GET", True, 200)]  # the stale ETag was offered and rejected

    async def test_cache_survives_client_restart(
        self, s3_backend: str, bucket: str, cache_db: Path, wire_log: list[WireEntry]
    ):
        async with make_cached_async_s3(s3_backend, cache_db, wire_log) as first:
            await first.put_object(bucket, KEY, body=DATA, cache_control="no-cache")
            assert await aread_body(first.get_object(bucket, KEY)) == DATA
        wire_log.clear()

        async with make_cached_async_s3(s3_backend, cache_db, wire_log) as second:
            assert await aread_body(second.get_object(bucket, KEY)) == DATA
        assert wire_log == [("GET", True, 304)]

    async def test_default_shared_policy_does_not_store(
        self, s3_backend: str, bucket: str, cache_db: Path, wire_log: list[WireEntry]
    ):
        # Why the README insists on CacheOptions(shared=False): signed requests
        # carry Authorization, which a shared cache must not store (RFC 9111 §3.5).
        async with make_cached_async_s3(s3_backend, cache_db, wire_log, private=False) as client:
            await client.put_object(bucket, KEY, body=DATA, cache_control="no-cache")
            wire_log.clear()
            assert await aread_body(client.get_object(bucket, KEY)) == DATA
            assert await aread_body(client.get_object(bucket, KEY)) == DATA
        assert wire_log == [("GET", False, 200), ("GET", False, 200)]

class TestCaching:  # unasync: generated
    def test_repeat_download_is_revalidated_not_transferred(
        self, cached_s3: S3Client, bucket: str, wire_log: list[WireEntry]
    ):
        cached_s3.put_object(bucket, KEY, body=DATA, cache_control="no-cache")
        wire_log.clear()

        assert read_body(cached_s3.get_object(bucket, KEY)) == DATA
        assert read_body(cached_s3.get_object(bucket, KEY)) == DATA

        assert wire_log == [("GET", False, 200), ("GET", True, 304)]

    def test_changed_object_is_downloaded_again(
        self, cached_s3: S3Client, bucket: str, wire_log: list[WireEntry]
    ):
        cached_s3.put_object(bucket, KEY, body=DATA, cache_control="no-cache")
        assert read_body(cached_s3.get_object(bucket, KEY)) == DATA

        cached_s3.put_object(bucket, KEY, body=NEW_DATA, cache_control="no-cache")
        wire_log.clear()

        assert read_body(cached_s3.get_object(bucket, KEY)) == NEW_DATA
        assert wire_log == [("GET", True, 200)]  # the stale ETag was offered and rejected

    def test_cache_survives_client_restart(
        self, s3_backend: str, bucket: str, cache_db: Path, wire_log: list[WireEntry]
    ):
        with make_cached_s3(s3_backend, cache_db, wire_log) as first:
            first.put_object(bucket, KEY, body=DATA, cache_control="no-cache")
            assert read_body(first.get_object(bucket, KEY)) == DATA
        wire_log.clear()

        with make_cached_s3(s3_backend, cache_db, wire_log) as second:
            assert read_body(second.get_object(bucket, KEY)) == DATA
        assert wire_log == [("GET", True, 304)]

    def test_default_shared_policy_does_not_store(
        self, s3_backend: str, bucket: str, cache_db: Path, wire_log: list[WireEntry]
    ):
        # Why the README insists on CacheOptions(shared=False): signed requests
        # carry Authorization, which a shared cache must not store (RFC 9111 §3.5).
        with make_cached_s3(s3_backend, cache_db, wire_log, private=False) as client:
            client.put_object(bucket, KEY, body=DATA, cache_control="no-cache")
            wire_log.clear()
            assert read_body(client.get_object(bucket, KEY)) == DATA
            assert read_body(client.get_object(bucket, KEY)) == DATA
        assert wire_log == [("GET", False, 200), ("GET", False, 200)]
