from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any

import pytest
from capo_s3.errors import ServiceError
from capo_s3.transfer import TransferConfig, TransferManager

MIB = 1024 * 1024


class StubClient:
    """Enough of S3Client for the transfer manager to drive."""

    def __init__(
        self, *, object_body: bytes = b"", e_tag: str | None = '"etag"'
    ) -> None:
        self.calls: list[tuple[str, dict[str, Any]]] = []
        self.uploaded: dict[int, bytes] = {}
        self.object_body = object_body
        self.e_tag = e_tag
        self.fail_parts: dict[int, int] = {}
        self._failures: dict[int, int] = {}

    def _record(self, name: str, **kwargs: Any) -> None:
        self.calls.append((name, kwargs))

    def names(self) -> list[str]:
        return [name for name, _ in self.calls]

    def kwargs_for(self, name: str) -> list[dict[str, Any]]:
        return [kw for called, kw in self.calls if called == name]

    def put_object(self, bucket: str, key: str, **kwargs: Any) -> dict[str, Any]:
        self._record("put_object", bucket=bucket, key=key, **kwargs)
        self.uploaded[0] = bytes(kwargs.get("body") or b"")
        return {"e_tag": self.e_tag}

    def create_multipart_upload(
        self, bucket: str, key: str, **kwargs: Any
    ) -> dict[str, Any]:
        self._record("create_multipart_upload", bucket=bucket, key=key, **kwargs)
        return {"upload_id": "upload-1"}

    def upload_part(
        self, bucket: str, key: str, part_number: int, upload_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        self._record(
            "upload_part",
            bucket=bucket,
            key=key,
            part_number=part_number,
            upload_id=upload_id,
            **kwargs,
        )
        remaining = self._failures.get(part_number, self.fail_parts.get(part_number, 0))
        if remaining:
            self._failures[part_number] = remaining - 1
            raise ServiceError(
                "server", is_throttling_error=False, is_retryable=True, code="Slow"
            )
        self.uploaded[part_number] = bytes(kwargs["body"])
        return {"e_tag": f'"etag-{part_number}"'}

    def complete_multipart_upload(
        self, bucket: str, key: str, upload_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        self._record(
            "complete_multipart_upload",
            bucket=bucket,
            key=key,
            upload_id=upload_id,
            **kwargs,
        )
        return {"e_tag": self.e_tag}

    def abort_multipart_upload(
        self, bucket: str, key: str, upload_id: str
    ) -> dict[str, Any]:
        self._record(
            "abort_multipart_upload", bucket=bucket, key=key, upload_id=upload_id
        )
        return {}

    def head_object(self, bucket: str, key: str, **kwargs: Any) -> dict[str, Any]:
        self._record("head_object", bucket=bucket, key=key, **kwargs)
        return {"content_length": len(self.object_body), "e_tag": self.e_tag}

    @contextmanager
    def get_object(
        self, bucket: str, key: str, **kwargs: Any
    ) -> Iterator[dict[str, Any]]:
        self._record("get_object", bucket=bucket, key=key, **kwargs)
        body = self.object_body
        if (rng := kwargs.get("range")) is not None:
            first, _, last = rng.removeprefix("bytes=").partition("-")
            body = body[int(first) : int(last) + 1]
        yield {"body": iter([body])}


@pytest.fixture
def config() -> TransferConfig:
    return TransferConfig(
        multipart_threshold=10 * MIB, multipart_chunksize=5 * MIB, max_concurrency=4
    )


def write(tmp_path: Path, size: int) -> Path:
    path = tmp_path / "source.bin"
    path.write_bytes(bytes(range(256)) * (size // 256) + b"\x00" * (size % 256))
    return path


class TestUpload:
    def test_small_file_uses_a_single_put(self, tmp_path: Path, config: TransferConfig):
        client = StubClient()
        source = write(tmp_path, 1 * MIB)

        TransferManager(client, config).upload_file(source, "bucket", "key")

        assert client.names() == ["put_object"]
        assert client.uploaded[0] == source.read_bytes()

    def test_large_file_uses_multipart(self, tmp_path: Path, config: TransferConfig):
        client = StubClient()
        source = write(tmp_path, 12 * MIB)

        TransferManager(client, config).upload_file(source, "bucket", "key")

        assert client.names()[0] == "create_multipart_upload"
        assert client.names()[-1] == "complete_multipart_upload"
        assert sorted(client.uploaded) == [1, 2, 3]
        assert (
            b"".join(client.uploaded[n] for n in sorted(client.uploaded))
            == source.read_bytes()
        )

    def test_parts_are_completed_in_order(self, tmp_path: Path, config: TransferConfig):
        """Workers finish out of order; the parts list must not."""
        client = StubClient()
        TransferManager(client, config).upload_file(
            write(tmp_path, 12 * MIB), "bucket", "key"
        )

        parts = client.kwargs_for("complete_multipart_upload")[0]["multipart_upload"][
            "parts"
        ]
        assert [p["part_number"] for p in parts] == [1, 2, 3]
        assert [p["e_tag"] for p in parts] == ['"etag-1"', '"etag-2"', '"etag-3"']

    def test_object_metadata_goes_to_create_not_to_parts(
        self, tmp_path: Path, config: TransferConfig
    ):
        client = StubClient()

        TransferManager(client, config).upload_file(
            write(tmp_path, 12 * MIB),
            "bucket",
            "key",
            extra_args={
                "content_type": "video/mp4",
                "sse_customer_algorithm": "AES256",
            },
        )

        created = client.kwargs_for("create_multipart_upload")[0]
        assert created["content_type"] == "video/mp4"
        for part in client.kwargs_for("upload_part"):
            assert "content_type" not in part
            assert part["sse_customer_algorithm"] == "AES256"

    def test_pipeline_retry_is_disabled_on_parts(
        self, tmp_path: Path, config: TransferConfig
    ):
        """A replayed request would send a spent body; parts retry above the client."""
        client = StubClient()
        TransferManager(client, config).upload_file(
            write(tmp_path, 12 * MIB), "bucket", "key"
        )

        for part in client.kwargs_for("upload_part"):
            assert part["config_overrides"] == {"retry_max_attempts": 1}

    def test_a_retried_part_sends_its_body_again(
        self, tmp_path: Path, config: TransferConfig
    ):
        client = StubClient()
        client.fail_parts = {2: 1}
        source = write(tmp_path, 12 * MIB)

        TransferManager(client, config).upload_file(source, "bucket", "key")

        assert len(client.kwargs_for("upload_part")) == 4  # 3 parts, one retried
        assert (
            b"".join(client.uploaded[n] for n in sorted(client.uploaded))
            == source.read_bytes()
        )

    def test_failure_aborts_the_upload(self, tmp_path: Path, config: TransferConfig):
        client = StubClient()
        client.fail_parts = {2: 99}  # exhausts max_attempts

        with pytest.raises(ServiceError):
            TransferManager(client, config).upload_file(
                write(tmp_path, 12 * MIB), "bucket", "key"
            )

        assert "abort_multipart_upload" in client.names()
        assert "complete_multipart_upload" not in client.names()

    def test_progress_totals_the_object(self, tmp_path: Path, config: TransferConfig):
        client = StubClient()
        seen: list[int] = []
        source = write(tmp_path, 12 * MIB)

        TransferManager(client, config).upload_file(
            source, "bucket", "key", progress=seen.append
        )

        assert sum(seen) == source.stat().st_size

    def test_fileobj_never_yields_a_short_middle_part(
        self, tmp_path: Path, config: TransferConfig
    ):
        """Only the final part may fall below S3's 5 MiB floor."""
        client = StubClient()
        source = write(tmp_path, 27 * MIB)

        with source.open("rb") as fh:
            TransferManager(client, config).upload_fileobj(fh, "bucket", "key")

        sizes = [len(client.uploaded[n]) for n in sorted(client.uploaded)]
        assert all(size == 5 * MIB for size in sizes[:-1]), sizes
        assert (
            b"".join(client.uploaded[n] for n in sorted(client.uploaded))
            == source.read_bytes()
        )

    def test_small_fileobj_uses_a_single_put(
        self, tmp_path: Path, config: TransferConfig
    ):
        client = StubClient()
        source = write(tmp_path, 1 * MIB)

        with source.open("rb") as fh:
            TransferManager(client, config).upload_fileobj(fh, "bucket", "key")

        assert client.names() == ["put_object"]


class TestDownload:
    def test_small_object_downloads_in_one_request(
        self, tmp_path: Path, config: TransferConfig
    ):
        body = bytes(range(256)) * (4 * 1024)
        client = StubClient(object_body=body)
        target = tmp_path / "out.bin"

        TransferManager(client, config).download_file("bucket", "key", target)

        assert client.names() == ["head_object", "get_object"]
        assert target.read_bytes() == body

    def test_large_object_downloads_in_ranges(
        self, tmp_path: Path, config: TransferConfig
    ):
        body = bytes(range(256)) * (12 * MIB // 256)
        client = StubClient(object_body=body)
        target = tmp_path / "out.bin"

        TransferManager(client, config).download_file("bucket", "key", target)

        ranges = [kw["range"] for kw in client.kwargs_for("get_object")]
        assert sorted(ranges) == sorted(
            [
                f"bytes=0-{5 * MIB - 1}",
                f"bytes={5 * MIB}-{10 * MIB - 1}",
                f"bytes={10 * MIB}-{12 * MIB - 1}",
            ]
        )
        assert target.read_bytes() == body

    def test_every_range_pins_the_etag(self, tmp_path: Path, config: TransferConfig):
        """Otherwise a concurrent overwrite splices two versions into one file."""
        client = StubClient(object_body=bytes(range(256)) * (12 * MIB // 256))

        TransferManager(client, config).download_file(
            "bucket", "key", tmp_path / "out.bin"
        )

        gets = client.kwargs_for("get_object")
        assert len(gets) == 3
        assert all(kw["if_match"] == '"etag"' for kw in gets)

    def test_download_fileobj_is_sequential(
        self, tmp_path: Path, config: TransferConfig
    ):
        body = bytes(range(256)) * (12 * MIB // 256)
        client = StubClient(object_body=body)
        target = tmp_path / "out.bin"

        with target.open("wb") as fh:
            TransferManager(client, config).download_fileobj("bucket", "key", fh)

        assert client.names() == ["get_object"]
        assert "range" not in client.kwargs_for("get_object")[0]
        assert target.read_bytes() == body
