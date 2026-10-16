"""The transfer manager's multipart upload and download against RustFS (free) and AWS (paid).

Files go up for real in parts of the smallest size S3 accepts, then come back
by byte range and by part. The large file is checked by digest and never read
into memory whole, which the manager must not do either. ``ry`` generates the
sync twins.
"""

from __future__ import annotations

import base64
import hashlib
import os
import tracemalloc
import zlib
from pathlib import Path
from typing import Literal

import pytest
from capo_s3 import AsyncS3Client, AsyncTransferManager, S3Client, TransferManager, Transferred
from capo_s3.errors import NotFound, ServiceError
from capo_s3.types.checksum_algorithm import ChecksumAlgorithm

from tests.conftest import needs_threads

MiB = 1024 * 1024
PART = 5 * MiB  # smallest part S3 accepts before the last one
LARGE = 64 * MiB + 17  # 13 parts, the last one ragged
DOWNLOAD_TYPES: list[Literal["range", "part"]] = ["range", "part"]


def random_file(path: Path, size: int) -> Path:
    """``size`` random bytes, written a MiB at a time."""
    with path.open("wb") as f:
        for start in range(0, size, MiB):
            f.write(os.urandom(min(MiB, size - start)))
    return path


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(MiB):
            digest.update(chunk)
    return digest.hexdigest()


def composite_checksum(algorithm: str, data: bytes) -> str | None:
    """What S3 reports for ``data`` uploaded in ``PART`` sized parts: the digest of
    the part digests, then the part count.

    ``None`` for CRC64NVME, which is a digest of the whole object and has no
    stdlib implementation; S3 alone validates it.
    """
    if algorithm == "CRC32":
        digests = [zlib.crc32(data[i : i + PART]).to_bytes(4, "big") for i in range(0, len(data), PART)]
        combined = zlib.crc32(b"".join(digests)).to_bytes(4, "big")
    elif algorithm == "SHA256":
        digests = [hashlib.sha256(data[i : i + PART]).digest() for i in range(0, len(data), PART)]
        combined = hashlib.sha256(b"".join(digests)).digest()
    else:
        return None
    return f"{base64.b64encode(combined).decode()}-{len(digests)}"


@pytest.fixture(scope="module")
def large_file(tmp_path_factory: pytest.TempPathFactory) -> Path:
    return random_file(tmp_path_factory.mktemp("transfer") / "large.bin", LARGE)


@pytest.fixture
def transfer_manager(s3: S3Client) -> TransferManager:
    return TransferManager(
        s3, target_part_size_bytes=PART, multipart_upload_threshold_bytes=PART, multipart_download_type="range"
    )


@pytest.fixture
def async_transfer_manager(async_s3: AsyncS3Client) -> AsyncTransferManager:
    return AsyncTransferManager(
        async_s3, target_part_size_bytes=PART, multipart_upload_threshold_bytes=PART, multipart_download_type="range"
    )


class TestAsyncTransferManager:  # unasync: generate
    @needs_threads
    async def test_large_file_round_trips_without_being_held_in_memory(
        self, async_transfer_manager: AsyncTransferManager, bucket: str, large_file: Path, tmp_path: Path
    ):
        tracemalloc.start()
        try:
            out = await async_transfer_manager.upload(large_file, bucket, "large.bin")
            for download_type in DOWNLOAD_TYPES:
                await async_transfer_manager.download(
                    bucket,
                    "large.bin",
                    tmp_path / download_type,
                    transfer_config_overrides={"multipart_download_type": download_type},
                )
            peak = tracemalloc.get_traced_memory()[1]
        finally:
            tracemalloc.stop()

        assert out["e_tag"].endswith('-13"'), "not a 13-part multipart upload"
        for download_type in DOWNLOAD_TYPES:
            assert (tmp_path / download_type).stat().st_size == LARGE
            assert sha256_of(tmp_path / download_type) == sha256_of(large_file)
        assert peak < 4 * PART, f"{peak / MiB:.1f} MiB allocated for a {LARGE / MiB:.0f} MiB file"

    @pytest.mark.parametrize(
        ("size", "parts"),
        [
            pytest.param(PART - 1, None, id="below-threshold"),
            pytest.param(PART, [PART], id="exactly-one-part"),
            pytest.param(PART + 1, [PART, 1], id="one-byte-last-part"),
        ],
    )
    @needs_threads
    async def test_part_boundaries(
        self,
        async_transfer_manager: AsyncTransferManager,
        bucket: str,
        tmp_path: Path,
        size: int,
        parts: list[int] | None,
    ):
        source = random_file(tmp_path / "source", size)
        async with async_transfer_manager.upload_iter(source, bucket, "boundary.bin") as upload:
            events = [event async for event in upload]

        assert upload.output is not None
        if parts is None:
            # a single put_object: no upload to complete and a plain MD5 ETag
            assert upload.upload_id is None
            assert "-" not in upload.output["e_tag"]
            assert events == [Transferred(size, size, size)]
        else:
            assert upload.output["e_tag"].endswith(f'-{len(parts)}"')
            sent = [sum(parts[: i + 1]) for i in range(len(parts))]
            assert events == [Transferred(part, done, size) for part, done in zip(parts, sent)]

        for download_type in DOWNLOAD_TYPES:
            await async_transfer_manager.download(
                bucket,
                "boundary.bin",
                tmp_path / download_type,
                transfer_config_overrides={"multipart_download_type": download_type},
            )
            assert (tmp_path / download_type).read_bytes() == source.read_bytes()

    @pytest.mark.parametrize("download_type", DOWNLOAD_TYPES)
    @needs_threads
    async def test_download_iter_yields_the_object_in_order(
        self,
        async_transfer_manager: AsyncTransferManager,
        bucket: str,
        tmp_path: Path,
        download_type: Literal["range", "part"],
    ):
        data = random_file(tmp_path / "source", 2 * PART + 17).read_bytes()
        await async_transfer_manager.upload(tmp_path / "source", bucket, "ordered.bin")

        # 3 MiB ranges cut across the 5 MiB parts the object was stored in
        events = [
            event
            async for event in async_transfer_manager.download_iter(
                bucket,
                "ordered.bin",
                transfer_config_overrides={"multipart_download_type": download_type, "target_part_size_bytes": 3 * MiB},
            )
        ]

        assert b"".join(event.data for event in events) == data
        offset = 0
        for event in events:
            assert (event.offset, event.total_bytes) == (offset, len(data))
            offset += len(event.data)
            assert event.transferred_bytes == offset

    @pytest.mark.parametrize("algorithm", ["CRC32", "SHA256", "CRC64NVME"])
    @needs_threads
    async def test_multipart_upload_with_checksum(
        self,
        async_transfer_manager: AsyncTransferManager,
        bucket: str,
        tmp_path: Path,
        algorithm: ChecksumAlgorithm,
    ):
        source = random_file(tmp_path / "source", PART + 1)
        data = source.read_bytes()

        # S3 refuses to complete the upload unless every part's checksum comes back with it
        out = await async_transfer_manager.upload(source, bucket, "checksum.bin", checksum_algorithm=algorithm)

        field = {"CRC32": "checksum_crc32", "SHA256": "checksum_sha256", "CRC64NVME": "checksum_crc64_nvme"}[algorithm]
        assert out.get(field)
        if composite_checksum(algorithm, data) is not None:
            assert out.get(field) == composite_checksum(algorithm, data)
        # a range or a part carries no checksum of the whole object for the client to verify
        for download_type in DOWNLOAD_TYPES:
            await async_transfer_manager.download(
                bucket,
                "checksum.bin",
                tmp_path / download_type,
                checksum_mode="ENABLED",
                transfer_config_overrides={"multipart_download_type": download_type},
            )
            assert (tmp_path / download_type).read_bytes() == data

    @pytest.mark.parametrize(
        "download_type",
        [
            pytest.param(
                "range",
                marks=pytest.mark.xfail(
                    strict=True,
                    raises=ServiceError,
                    reason="the first request asks for bytes=0-N, which S3 answers with InvalidRange (416) "
                    "for an object without bytes; the manager does not fall back",
                ),
            ),
            "part",
        ],
    )
    @needs_threads
    async def test_empty_file(
        self,
        async_transfer_manager: AsyncTransferManager,
        bucket: str,
        tmp_path: Path,
        download_type: Literal["range", "part"],
    ):
        source = random_file(tmp_path / "source", 0)
        await async_transfer_manager.upload(source, bucket, "empty.bin")
        await async_transfer_manager.download(
            bucket,
            "empty.bin",
            tmp_path / "destination",
            transfer_config_overrides={"multipart_download_type": download_type},
        )
        assert (tmp_path / "destination").read_bytes() == b""

    @needs_threads
    async def test_failed_upload_is_aborted(
        self, async_s3: AsyncS3Client, async_transfer_manager: AsyncTransferManager, bucket: str, tmp_path: Path
    ):
        source = random_file(tmp_path / "source", PART + 1)
        with pytest.raises(RuntimeError, match="lost"):
            async with async_transfer_manager.upload_iter(source, bucket, "failed.bin") as upload:
                async for _ in upload:
                    raise RuntimeError("lost after the first part")

        assert upload.upload_id is not None
        assert upload.output is None
        # no parts left behind to be billed for, and no object
        assert (await async_s3.list_multipart_uploads(bucket)).get("uploads", []) == []
        with pytest.raises(NotFound):
            await async_s3.head_object(bucket, "failed.bin")

    @needs_threads
    async def test_upload_left_early_is_aborted(
        self, async_s3: AsyncS3Client, async_transfer_manager: AsyncTransferManager, bucket: str, tmp_path: Path
    ):
        source = random_file(tmp_path / "source", PART + 1)
        async with async_transfer_manager.upload_iter(source, bucket, "partial.bin") as upload:
            async for _ in upload:
                break

        assert upload.output is None
        assert (await async_s3.list_multipart_uploads(bucket)).get("uploads", []) == []
        with pytest.raises(NotFound):
            await async_s3.head_object(bucket, "partial.bin")

    @pytest.mark.parametrize("download_type", DOWNLOAD_TYPES)
    @needs_threads
    async def test_object_replaced_mid_download_raises(
        self,
        async_s3: AsyncS3Client,
        async_transfer_manager: AsyncTransferManager,
        bucket: str,
        tmp_path: Path,
        download_type: Literal["range", "part"],
    ):
        source = random_file(tmp_path / "source", PART + 1)
        await async_transfer_manager.upload(source, bucket, "replaced.bin")

        # the second request is pinned to the first one's ETag, so the two versions are never stitched together
        with pytest.raises(ServiceError) as info:
            async for event in async_transfer_manager.download_iter(
                bucket, "replaced.bin", transfer_config_overrides={"multipart_download_type": download_type}
            ):
                if event.offset == 0:
                    await async_s3.put_object(bucket, "replaced.bin", body=b"x" * (PART + 1))
        assert info.value.code == "PreconditionFailed"


class TestTransferManager:  # unasync: generated
    @needs_threads
    def test_large_file_round_trips_without_being_held_in_memory(
        self, transfer_manager: TransferManager, bucket: str, large_file: Path, tmp_path: Path
    ):
        tracemalloc.start()
        try:
            out = transfer_manager.upload(large_file, bucket, "large.bin")
            for download_type in DOWNLOAD_TYPES:
                transfer_manager.download(
                    bucket,
                    "large.bin",
                    tmp_path / download_type,
                    transfer_config_overrides={"multipart_download_type": download_type},
                )
            peak = tracemalloc.get_traced_memory()[1]
        finally:
            tracemalloc.stop()

        assert out["e_tag"].endswith('-13"'), "not a 13-part multipart upload"
        for download_type in DOWNLOAD_TYPES:
            assert (tmp_path / download_type).stat().st_size == LARGE
            assert sha256_of(tmp_path / download_type) == sha256_of(large_file)
        assert peak < 4 * PART, f"{peak / MiB:.1f} MiB allocated for a {LARGE / MiB:.0f} MiB file"

    @pytest.mark.parametrize(
        ("size", "parts"),
        [
            pytest.param(PART - 1, None, id="below-threshold"),
            pytest.param(PART, [PART], id="exactly-one-part"),
            pytest.param(PART + 1, [PART, 1], id="one-byte-last-part"),
        ],
    )
    @needs_threads
    def test_part_boundaries(
        self,
        transfer_manager: TransferManager,
        bucket: str,
        tmp_path: Path,
        size: int,
        parts: list[int] | None,
    ):
        source = random_file(tmp_path / "source", size)
        with transfer_manager.upload_iter(source, bucket, "boundary.bin") as upload:
            events = [event for event in upload]

        assert upload.output is not None
        if parts is None:
            # a single put_object: no upload to complete and a plain MD5 ETag
            assert upload.upload_id is None
            assert "-" not in upload.output["e_tag"]
            assert events == [Transferred(size, size, size)]
        else:
            assert upload.output["e_tag"].endswith(f'-{len(parts)}"')
            sent = [sum(parts[: i + 1]) for i in range(len(parts))]
            assert events == [Transferred(part, done, size) for part, done in zip(parts, sent)]

        for download_type in DOWNLOAD_TYPES:
            transfer_manager.download(
                bucket,
                "boundary.bin",
                tmp_path / download_type,
                transfer_config_overrides={"multipart_download_type": download_type},
            )
            assert (tmp_path / download_type).read_bytes() == source.read_bytes()

    @pytest.mark.parametrize("download_type", DOWNLOAD_TYPES)
    @needs_threads
    def test_download_iter_yields_the_object_in_order(
        self,
        transfer_manager: TransferManager,
        bucket: str,
        tmp_path: Path,
        download_type: Literal["range", "part"],
    ):
        data = random_file(tmp_path / "source", 2 * PART + 17).read_bytes()
        transfer_manager.upload(tmp_path / "source", bucket, "ordered.bin")

        # 3 MiB ranges cut across the 5 MiB parts the object was stored in
        events = [
            event
            for event in transfer_manager.download_iter(
                bucket,
                "ordered.bin",
                transfer_config_overrides={"multipart_download_type": download_type, "target_part_size_bytes": 3 * MiB},
            )
        ]

        assert b"".join(event.data for event in events) == data
        offset = 0
        for event in events:
            assert (event.offset, event.total_bytes) == (offset, len(data))
            offset += len(event.data)
            assert event.transferred_bytes == offset

    @pytest.mark.parametrize("algorithm", ["CRC32", "SHA256", "CRC64NVME"])
    @needs_threads
    def test_multipart_upload_with_checksum(
        self,
        transfer_manager: TransferManager,
        bucket: str,
        tmp_path: Path,
        algorithm: ChecksumAlgorithm,
    ):
        source = random_file(tmp_path / "source", PART + 1)
        data = source.read_bytes()

        # S3 refuses to complete the upload unless every part's checksum comes back with it
        out = transfer_manager.upload(source, bucket, "checksum.bin", checksum_algorithm=algorithm)

        field = {"CRC32": "checksum_crc32", "SHA256": "checksum_sha256", "CRC64NVME": "checksum_crc64_nvme"}[algorithm]
        assert out.get(field)
        if composite_checksum(algorithm, data) is not None:
            assert out.get(field) == composite_checksum(algorithm, data)
        # a range or a part carries no checksum of the whole object for the client to verify
        for download_type in DOWNLOAD_TYPES:
            transfer_manager.download(
                bucket,
                "checksum.bin",
                tmp_path / download_type,
                checksum_mode="ENABLED",
                transfer_config_overrides={"multipart_download_type": download_type},
            )
            assert (tmp_path / download_type).read_bytes() == data

    @pytest.mark.parametrize(
        "download_type",
        [
            pytest.param(
                "range",
                marks=pytest.mark.xfail(
                    strict=True,
                    raises=ServiceError,
                    reason="the first request asks for bytes=0-N, which S3 answers with InvalidRange (416) "
                    "for an object without bytes; the manager does not fall back",
                ),
            ),
            "part",
        ],
    )
    @needs_threads
    def test_empty_file(
        self,
        transfer_manager: TransferManager,
        bucket: str,
        tmp_path: Path,
        download_type: Literal["range", "part"],
    ):
        source = random_file(tmp_path / "source", 0)
        transfer_manager.upload(source, bucket, "empty.bin")
        transfer_manager.download(
            bucket,
            "empty.bin",
            tmp_path / "destination",
            transfer_config_overrides={"multipart_download_type": download_type},
        )
        assert (tmp_path / "destination").read_bytes() == b""

    @needs_threads
    def test_failed_upload_is_aborted(
        self, s3: S3Client, transfer_manager: TransferManager, bucket: str, tmp_path: Path
    ):
        source = random_file(tmp_path / "source", PART + 1)
        with pytest.raises(RuntimeError, match="lost"):
            with transfer_manager.upload_iter(source, bucket, "failed.bin") as upload:
                for _ in upload:
                    raise RuntimeError("lost after the first part")

        assert upload.upload_id is not None
        assert upload.output is None
        # no parts left behind to be billed for, and no object
        assert (s3.list_multipart_uploads(bucket)).get("uploads", []) == []
        with pytest.raises(NotFound):
            s3.head_object(bucket, "failed.bin")

    @needs_threads
    def test_upload_left_early_is_aborted(
        self, s3: S3Client, transfer_manager: TransferManager, bucket: str, tmp_path: Path
    ):
        source = random_file(tmp_path / "source", PART + 1)
        with transfer_manager.upload_iter(source, bucket, "partial.bin") as upload:
            for _ in upload:
                break

        assert upload.output is None
        assert (s3.list_multipart_uploads(bucket)).get("uploads", []) == []
        with pytest.raises(NotFound):
            s3.head_object(bucket, "partial.bin")

    @pytest.mark.parametrize("download_type", DOWNLOAD_TYPES)
    @needs_threads
    def test_object_replaced_mid_download_raises(
        self,
        s3: S3Client,
        transfer_manager: TransferManager,
        bucket: str,
        tmp_path: Path,
        download_type: Literal["range", "part"],
    ):
        source = random_file(tmp_path / "source", PART + 1)
        transfer_manager.upload(source, bucket, "replaced.bin")

        # the second request is pinned to the first one's ETag, so the two versions are never stitched together
        with pytest.raises(ServiceError) as info:
            for event in transfer_manager.download_iter(
                bucket, "replaced.bin", transfer_config_overrides={"multipart_download_type": download_type}
            ):
                if event.offset == 0:
                    s3.put_object(bucket, "replaced.bin", body=b"x" * (PART + 1))
        assert info.value.code == "PreconditionFailed"
