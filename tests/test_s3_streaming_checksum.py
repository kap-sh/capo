"""Streaming uploads with a trailing checksum against MinIO, RustFS (free) and AWS (paid).

A body without a known digest up front (iterator, async generator, ``Body``)
goes out in ``aws-chunked`` framing with the checksum in the trailer. Every
test here sends one for real and lets the server validate it: a wrong trailer
is rejected, so a matching response checksum proves the SDK hashed the right
bytes. ``ry`` generates the sync twins.
"""

from __future__ import annotations

import base64
import hashlib
import os
from pathlib import Path

import pytest
from capo_s3 import AsyncS3Client, Body, S3Client
from capo_s3._checksums import TrailingChecksumStream
from capo_s3.errors import NotFound, ServiceError
from capo_s3.types.checksum_algorithm import ChecksumAlgorithm

from tests.conftest import aread_body, astream, crc32_b64, parts_of, read_body, stream

DATA = os.urandom(300 * 1024 + 17)  # several 64 KiB frames plus a ragged tail
PART = os.urandom(5 * 1024 * 1024 + 3)  # smallest legal non-final multipart part
CHECKSUM_ALGORITHMS: list[ChecksumAlgorithm] = ["CRC32", "CRC32C", "SHA1", "SHA256", "CRC64NVME"]
RESPONSE_FIELD = {
    "CRC32": "checksum_crc32",
    "CRC32C": "checksum_crc32_c",
    "SHA1": "checksum_sha1",
    "SHA256": "checksum_sha256",
    "CRC64NVME": "checksum_crc64_nvme",
}


def expected_checksum(algorithm: str, data: bytes) -> str | None:
    """Digest computed without the SDK, or ``None`` where the stdlib has no implementation.

    CRC32C and CRC64NVME are then covered by the server alone: it rejects a
    trailer that does not match the bytes it received.
    """
    if algorithm == "CRC32":
        return crc32_b64(data)
    if algorithm == "SHA1":
        return base64.b64encode(hashlib.sha1(data).digest()).decode()
    if algorithm == "SHA256":
        return base64.b64encode(hashlib.sha256(data).digest()).decode()
    return None


class TestAsyncStreamingChecksum:  # unasync: generate
    @pytest.mark.parametrize("algorithm", CHECKSUM_ALGORITHMS)
    async def test_iterator_upload(self, async_s3: AsyncS3Client, bucket: str, algorithm: ChecksumAlgorithm):
        out = await async_s3.put_object(
            bucket,
            "iter.bin",
            body=astream(parts_of(DATA)),
            content_length=len(DATA),
            checksum_algorithm=algorithm,
        )
        field = RESPONSE_FIELD[algorithm]
        assert out.get(field)
        if expected_checksum(algorithm, DATA) is not None:
            assert out.get(field) == expected_checksum(algorithm, DATA)
        async with async_s3.get_object(bucket, "iter.bin", checksum_mode="ENABLED") as obj:
            assert obj.get(field) == out.get(field)
            assert b"".join([chunk async for chunk in obj["body"]]) == DATA

    async def test_body_from_path_is_reusable(self, async_s3: AsyncS3Client, bucket: str, tmp_path: Path):
        path = tmp_path / "data.bin"
        path.write_bytes(DATA)
        body = Body.async_from_path(path)

        out = await async_s3.put_object(bucket, "path.bin", body=body, checksum_algorithm="CRC32")
        assert out.get("checksum_crc32") == crc32_b64(DATA)
        assert body.stream is None, "Body left open after the upload"
        assert await aread_body(async_s3.get_object(bucket, "path.bin")) == DATA

        # The same Body again with another algorithm: a fresh stream and a fresh hasher.
        out = await async_s3.put_object(bucket, "path2.bin", body=body, checksum_algorithm="SHA256")
        assert out.get("checksum_sha256") == expected_checksum("SHA256", DATA)

    async def test_empty_iterator(self, async_s3: AsyncS3Client, bucket: str):
        out = await async_s3.put_object(
            bucket,
            "empty.bin",
            body=astream([]),
            content_length=0,
            checksum_algorithm="CRC32",
        )
        assert out.get("checksum_crc32") == crc32_b64(b"")
        assert await aread_body(async_s3.get_object(bucket, "empty.bin")) == b""

    async def test_empty_chunks_are_skipped(self, async_s3: AsyncS3Client, bucket: str):
        # An empty chunk must not become a "0" frame, which would end the body early.
        sparse = [b"", b"", DATA[:10000], b"", DATA[10000:70000], b"", b"", DATA[70000:], b"", b""]
        out = await async_s3.put_object(
            bucket,
            "sparse.bin",
            body=astream(sparse),
            content_length=len(DATA),
            checksum_algorithm="CRC32C",
        )
        assert out.get("checksum_crc32_c")
        assert await aread_body(async_s3.get_object(bucket, "sparse.bin")) == DATA

        out = await async_s3.put_object(
            bucket,
            "all-empty.bin",
            body=astream([b"", b"", b""]),
            content_length=0,
            checksum_algorithm="SHA256",
        )
        assert out.get("checksum_sha256") == expected_checksum("SHA256", b"")

    async def test_small_chunks(
        self,
        async_s3: AsyncS3Client,
        bucket: str,
        s3_backend: str,
        request: pytest.FixtureRequest,
    ):
        if s3_backend == "aws":
            request.applymarker(
                pytest.mark.xfail(
                    strict=True,
                    raises=ServiceError,
                    reason="each yielded chunk becomes one aws-chunked frame and AWS rejects frames under 8 KiB "
                    "(InvalidChunkSizeError); the SDK does not coalesce small chunks",
                )
            )
        out = await async_s3.put_object(
            bucket,
            "small.bin",
            body=astream(parts_of(DATA, size=1024)),
            content_length=len(DATA),
            checksum_algorithm="CRC32",
        )
        assert out.get("checksum_crc32") == crc32_b64(DATA)
        assert await aread_body(async_s3.get_object(bucket, "small.bin")) == DATA

    async def test_tampered_trailer_is_rejected(
        self,
        async_s3: AsyncS3Client,
        bucket: str,
        monkeypatch: pytest.MonkeyPatch,
    ):
        # Send a wrong checksum in the trailer to prove the server really validates it.
        def bad_trailer(self: TrailingChecksumStream) -> bytes:
            self._done = True
            return f"0\r\n{self.header}:AAAAAA==\r\n\r\n".encode()

        monkeypatch.setattr(TrailingChecksumStream, "_trailer", bad_trailer)
        with pytest.raises(ServiceError):
            await async_s3.put_object(
                bucket,
                "tampered.bin",
                body=astream(parts_of(DATA)),
                content_length=len(DATA),
                checksum_algorithm="CRC32",
            )
        monkeypatch.undo()
        with pytest.raises(NotFound):
            await async_s3.head_object(bucket, "tampered.bin")

    async def test_multipart_with_streamed_parts(self, async_s3: AsyncS3Client, bucket: str):
        upload_id = (await async_s3.create_multipart_upload(bucket, "mpu.bin", checksum_algorithm="CRC32"))["upload_id"]
        p1 = await async_s3.upload_part(
            bucket,
            "mpu.bin",
            part_number=1,
            upload_id=upload_id,
            body=astream(parts_of(PART)),
            content_length=len(PART),
            checksum_algorithm="CRC32",
        )
        assert p1.get("checksum_crc32") == crc32_b64(PART)
        p2 = await async_s3.upload_part(
            bucket,
            "mpu.bin",
            part_number=2,
            upload_id=upload_id,
            body=astream(parts_of(DATA)),
            content_length=len(DATA),
            checksum_algorithm="CRC32",
        )
        assert p2.get("checksum_crc32") == crc32_b64(DATA)
        await async_s3.complete_multipart_upload(
            bucket,
            "mpu.bin",
            upload_id=upload_id,
            multipart_upload={
                "parts": [
                    {"part_number": 1, "e_tag": p1["e_tag"], "checksum_crc32": p1["checksum_crc32"]},
                    {"part_number": 2, "e_tag": p2["e_tag"], "checksum_crc32": p2["checksum_crc32"]},
                ]
            },
        )
        assert await aread_body(async_s3.get_object(bucket, "mpu.bin")) == PART + DATA


class TestStreamingChecksum:  # unasync: generated
    @pytest.mark.parametrize("algorithm", CHECKSUM_ALGORITHMS)
    def test_iterator_upload(self, s3: S3Client, bucket: str, algorithm: ChecksumAlgorithm):
        out = s3.put_object(
            bucket,
            "iter.bin",
            body=stream(parts_of(DATA)),
            content_length=len(DATA),
            checksum_algorithm=algorithm,
        )
        field = RESPONSE_FIELD[algorithm]
        assert out.get(field)
        if expected_checksum(algorithm, DATA) is not None:
            assert out.get(field) == expected_checksum(algorithm, DATA)
        with s3.get_object(bucket, "iter.bin", checksum_mode="ENABLED") as obj:
            assert obj.get(field) == out.get(field)
            assert b"".join([chunk for chunk in obj["body"]]) == DATA

    def test_body_from_path_is_reusable(self, s3: S3Client, bucket: str, tmp_path: Path):
        path = tmp_path / "data.bin"
        path.write_bytes(DATA)
        body = Body.from_path(path)

        out = s3.put_object(bucket, "path.bin", body=body, checksum_algorithm="CRC32")
        assert out.get("checksum_crc32") == crc32_b64(DATA)
        assert body.stream is None, "Body left open after the upload"
        assert read_body(s3.get_object(bucket, "path.bin")) == DATA

        # The same Body again with another algorithm: a fresh stream and a fresh hasher.
        out = s3.put_object(bucket, "path2.bin", body=body, checksum_algorithm="SHA256")
        assert out.get("checksum_sha256") == expected_checksum("SHA256", DATA)

    def test_empty_iterator(self, s3: S3Client, bucket: str):
        out = s3.put_object(
            bucket,
            "empty.bin",
            body=stream([]),
            content_length=0,
            checksum_algorithm="CRC32",
        )
        assert out.get("checksum_crc32") == crc32_b64(b"")
        assert read_body(s3.get_object(bucket, "empty.bin")) == b""

    def test_empty_chunks_are_skipped(self, s3: S3Client, bucket: str):
        # An empty chunk must not become a "0" frame, which would end the body early.
        sparse = [b"", b"", DATA[:10000], b"", DATA[10000:70000], b"", b"", DATA[70000:], b"", b""]
        out = s3.put_object(
            bucket,
            "sparse.bin",
            body=stream(sparse),
            content_length=len(DATA),
            checksum_algorithm="CRC32C",
        )
        assert out.get("checksum_crc32_c")
        assert read_body(s3.get_object(bucket, "sparse.bin")) == DATA

        out = s3.put_object(
            bucket,
            "all-empty.bin",
            body=stream([b"", b"", b""]),
            content_length=0,
            checksum_algorithm="SHA256",
        )
        assert out.get("checksum_sha256") == expected_checksum("SHA256", b"")

    def test_small_chunks(
        self,
        s3: S3Client,
        bucket: str,
        s3_backend: str,
        request: pytest.FixtureRequest,
    ):
        if s3_backend == "aws":
            request.applymarker(
                pytest.mark.xfail(
                    strict=True,
                    raises=ServiceError,
                    reason="each yielded chunk becomes one aws-chunked frame and AWS rejects frames under 8 KiB "
                    "(InvalidChunkSizeError); the SDK does not coalesce small chunks",
                )
            )
        out = s3.put_object(
            bucket,
            "small.bin",
            body=stream(parts_of(DATA, size=1024)),
            content_length=len(DATA),
            checksum_algorithm="CRC32",
        )
        assert out.get("checksum_crc32") == crc32_b64(DATA)
        assert read_body(s3.get_object(bucket, "small.bin")) == DATA

    def test_tampered_trailer_is_rejected(
        self,
        s3: S3Client,
        bucket: str,
        monkeypatch: pytest.MonkeyPatch,
    ):
        # Send a wrong checksum in the trailer to prove the server really validates it.
        def bad_trailer(self: TrailingChecksumStream) -> bytes:
            self._done = True
            return f"0\r\n{self.header}:AAAAAA==\r\n\r\n".encode()

        monkeypatch.setattr(TrailingChecksumStream, "_trailer", bad_trailer)
        with pytest.raises(ServiceError):
            s3.put_object(
                bucket,
                "tampered.bin",
                body=stream(parts_of(DATA)),
                content_length=len(DATA),
                checksum_algorithm="CRC32",
            )
        monkeypatch.undo()
        with pytest.raises(NotFound):
            s3.head_object(bucket, "tampered.bin")

    def test_multipart_with_streamed_parts(self, s3: S3Client, bucket: str):
        upload_id = (s3.create_multipart_upload(bucket, "mpu.bin", checksum_algorithm="CRC32"))["upload_id"]
        p1 = s3.upload_part(
            bucket,
            "mpu.bin",
            part_number=1,
            upload_id=upload_id,
            body=stream(parts_of(PART)),
            content_length=len(PART),
            checksum_algorithm="CRC32",
        )
        assert p1.get("checksum_crc32") == crc32_b64(PART)
        p2 = s3.upload_part(
            bucket,
            "mpu.bin",
            part_number=2,
            upload_id=upload_id,
            body=stream(parts_of(DATA)),
            content_length=len(DATA),
            checksum_algorithm="CRC32",
        )
        assert p2.get("checksum_crc32") == crc32_b64(DATA)
        s3.complete_multipart_upload(
            bucket,
            "mpu.bin",
            upload_id=upload_id,
            multipart_upload={
                "parts": [
                    {"part_number": 1, "e_tag": p1["e_tag"], "checksum_crc32": p1["checksum_crc32"]},
                    {"part_number": 2, "e_tag": p2["e_tag"], "checksum_crc32": p2["checksum_crc32"]},
                ]
            },
        )
        assert read_body(s3.get_object(bucket, "mpu.bin")) == PART + DATA
