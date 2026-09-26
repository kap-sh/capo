import os
import threading
import time
from collections.abc import Callable, Iterator
from concurrent.futures import Future, ThreadPoolExecutor
from contextlib import suppress
from dataclasses import dataclass
from functools import partial
from pathlib import Path
from typing import Any, BinaryIO, TypeVar

from capo_s3._services._pipeline import _is_retryable, _retry_delay
from capo_s3._services.s3 import S3Client, S3ClientConfig
from capo_s3.types.completed_part import CompletedPart

from ._config import (
    MAX_PARTS,
    DownloadExtraArgs,
    TransferConfig,
    UploadExtraArgs,
    split_upload_args,
)

T = TypeVar("T")

Progress = Callable[[int], None]
"""Called with the number of bytes transferred since the previous call."""

# Parts carry their own retry loop, so the pipeline's must be off. Leaving both on is not merely redundant: the pipeline
# retries by replaying the same request, and a streaming body is a one-shot iterator, so its second attempt sends
# nothing at all. Rebuilding the body per attempt is the only correct way, and that has to happen above the client call.
_NO_PIPELINE_RETRY: S3ClientConfig = {"retry_max_attempts": 1}


@dataclass(frozen=True, slots=True)
class _Upload:
    """The identity of one multipart upload, constant for all of its parts."""

    bucket: str
    key: str
    upload_id: str
    part_args: dict[str, Any]


@dataclass(frozen=True, slots=True)
class _Download:
    """The identity of one download, constant for all of its ranges."""

    fd: int
    bucket: str
    key: str
    e_tag: str | None
    extra: dict[str, Any]


@dataclass(frozen=True, slots=True)
class _Download:
    """The identity of one download, constant for all of its ranges."""

    fd: int
    bucket: str
    key: str
    e_tag: str | None
    extra: dict[str, Any]


class _Reporter:
    """Serialises progress callbacks; workers call it concurrently."""

    def __init__(self, progress: Progress | None) -> None:
        self._progress = progress
        self._lock = threading.Lock()

    def __call__(self, transferred: int) -> None:
        if self._progress is None:
            return
        with self._lock:
            self._progress(transferred)


def _pread_exact(fd: int, length: int, offset: int) -> bytes:
    """Guard against short reads."""
    out = bytearray()
    while len(out) < length:
        chunk = os.pread(fd, length - len(out), offset + len(out))
        if not chunk:
            break
        out += chunk
    return bytes(out)


def _read_exact(fileobj: BinaryIO, length: int) -> bytes:
    """Guard against short reads, as :func:`_pread_exact` does, where there is no position to read from."""
    out = bytearray()
    while len(out) < length:
        chunk = fileobj.read(length - len(out))
        if not chunk:
            break
        out += chunk
    return bytes(out)


class TransferManager:
    """Whole-file transfers built on the generated operations.

    Args:
        client: An open client. Its lifetime stays with whoever opened it; this manager never closes it.
        config: Thresholds and concurrency. Defaults to :class:`TransferConfig`.

    Examples:
        Upload a large file with a raised threshold::

            >>> with S3Client(region="us-east-1") as client:
            ...     tm = TransferManager(client, TransferConfig(multipart_threshold=25 * 1024 * 1024))
            ...     tm.upload_file("large_video.mp4", "my-bucket", "videos/large_video.mp4")
    """

    def __init__(self, client: S3Client, config: TransferConfig | None = None) -> None:
        self._client = client
        self._config = config or TransferConfig()

    def upload_file(
        self,
        filename: str | os.PathLike[str],
        bucket: str,
        key: str,
        *,
        extra_args: UploadExtraArgs | None = None,
        progress: Progress | None = None,
    ) -> None:
        """Preferred over :meth:`upload_fileobj` for anything large.

        A path can be read by position, so each worker pulls its own slice straight from disk: no part waits in
        memory for its turn, and a failed attempt just reads the same bytes again.
        """
        report = _Reporter(progress)
        with Path(filename).open("rb") as source:
            fd = source.fileno()
            size = os.fstat(fd).st_size
            if not self._config.is_multipart(size):
                body = _pread_exact(fd, size, 0)
                self._put_object(bucket, key, body, extra_args)
                report(len(body))
                return
            sources = (
                (number, partial(_pread_exact, fd, length, offset))
                for number, (offset, length) in enumerate(
                    self._config.part_ranges(size), start=1
                )
            )
            self._upload_multipart(bucket, key, sources, extra_args, report)

    def upload_fileobj(
        self,
        fileobj: BinaryIO,
        bucket: str,
        key: str,
        *,
        extra_args: UploadExtraArgs | None = None,
        progress: Progress | None = None,
    ) -> None:
        """For sources that are not a path on disk -- an open file, a socket, anything readable.

        Such a source has no size to ask for and may not be rewindable, so the first ``multipart_threshold`` bytes
        are read up front purely to find out whether one request will do. Parts are then read one at a time and
        uploaded concurrently, which caps how much sits in memory at ``max_concurrency`` parts.
        """
        report = _Reporter(progress)
        head = _read_exact(fileobj, self._config.multipart_threshold)
        if len(head) < self._config.multipart_threshold:
            self._put_object(bucket, key, head, extra_args)
            report(len(head))
            return
        self._upload_multipart(
            bucket, key, self._stream_parts(fileobj, head), extra_args, report
        )

    def _stream_parts(
        self, fileobj: BinaryIO, head: bytes
    ) -> Iterator[tuple[int, Callable[[], bytes]]]:
        """Cut a stream into parts S3 will accept.

        Bytes are buffered and released a full chunk at a time. Splitting each read wherever it happened to end
        would sooner or later produce a short part in the middle of the upload, and S3 rejects any part below
        MIN_PART_SIZE except the last one.

        Each part is handed back as a callable over bytes still in memory, so a failed attempt can be replayed
        byte-for-byte.
        """
        chunk = self._config.multipart_chunksize
        buffer = bytearray(head)
        number = 0
        eof = False
        while True:
            if len(buffer) < chunk and not eof:
                wanted = chunk - len(buffer)
                more = _read_exact(fileobj, wanted)
                buffer += more
                eof = len(more) < wanted
            if not buffer:
                return
            part = bytes(buffer[:chunk])
            del buffer[:chunk]
            number += 1
            if number > MAX_PARTS:
                raise ValueError(
                    f"stream needs more than {MAX_PARTS} parts at a {chunk}-byte chunk size; raise multipart_chunksize"
                )
            # ``data=part`` binds this part now. A bare ``lambda: part`` would read whatever the loop
            # rebinds it to next, which a worker calling the loader later would see instead.
            yield number, lambda data=part: data

    def _put_object(
        self,
        bucket: str,
        key: str,
        body: bytes,
        extra_args: UploadExtraArgs | None,
    ) -> None:
        def attempt() -> None:
            self._client.put_object(
                bucket,
                key,
                config_overrides=_NO_PIPELINE_RETRY,
                body=body,
                content_length=len(body),
                **(extra_args or {}),
            )

        self._retrying(attempt)

    def _upload_multipart(
        self,
        bucket: str,
        key: str,
        sources: Iterator[tuple[int, Callable[[], bytes]]],
        extra_args: UploadExtraArgs | None,
        report: _Reporter,
    ) -> None:
        create_args, part_args = split_upload_args(extra_args)
        created = self._client.create_multipart_upload(bucket, key, **create_args)
        upload = _Upload(bucket, key, created["upload_id"], part_args)
        try:
            with ThreadPoolExecutor(max_workers=self._config.max_concurrency) as pool:
                # Bounds how far the producer reads ahead of the uploads, which is what keeps peak memory at
                # concurrency * chunksize.
                slots = threading.Semaphore(self._config.max_concurrency)
                futures: list[Future[CompletedPart]] = []
                for number, load in sources:
                    slots.acquire()
                    futures.append(
                        pool.submit(
                            self._upload_part, upload, number, load, report, slots
                        )
                    )
                # Submission order is part order, so the results need no sorting.
                parts = [future.result() for future in futures]
            self._client.complete_multipart_upload(
                upload.bucket,
                upload.key,
                upload.upload_id,
                multipart_upload={"parts": parts},
            )
        except BaseException:
            # BaseException, not Exception: Ctrl-C and SystemExit have to abort too. An upload left open keeps its
            # parts in the bucket and keeps billing for them until a lifecycle rule notices. The abort is suppressed
            # and we re-raise immediately, so the interrupt still propagates on time.
            self._abort(upload)
            raise

    def _upload_part(
        self,
        upload: _Upload,
        number: int,
        load: Callable[[], bytes],
        report: _Reporter,
        slots: threading.Semaphore,
    ) -> CompletedPart:
        try:

            def attempt() -> tuple[str, int]:
                body = load()  # rebuilt per attempt, never a spent iterator
                output = self._client.upload_part(
                    upload.bucket,
                    upload.key,
                    number,
                    upload.upload_id,
                    config_overrides=_NO_PIPELINE_RETRY,
                    body=body,
                    content_length=len(body),
                    **upload.part_args,
                )
                e_tag = output.get("e_tag")
                if e_tag is None:
                    raise ValueError(
                        f"S3 returned no ETag for part {number}; cannot complete the upload"
                    )
                return e_tag, len(body)

            e_tag, size = self._retrying(attempt)
            report(size)
            return CompletedPart(part_number=number, e_tag=e_tag)
        finally:
            slots.release()

    def _abort(self, upload: _Upload) -> None:
        """Best-effort cleanup: never mask the failure that got us here."""
        with suppress(Exception):
            self._client.abort_multipart_upload(
                upload.bucket, upload.key, upload.upload_id
            )

    def download_file(
        self,
        bucket: str,
        key: str,
        filename: str | os.PathLike[str],
        *,
        extra_args: DownloadExtraArgs | None = None,
        progress: Progress | None = None,
    ) -> None:
        """Preferred over :meth:`download_fileobj` for anything large.

        A path can be written by position, so parts are free to arrive in any order and the download runs
        concurrently.
        """
        report = _Reporter(progress)
        extra: dict[str, Any] = dict(extra_args) if extra_args else {}
        head = self._client.head_object(bucket, key, **extra)
        size = head.get("content_length") or 0
        # buffering=0 so the file object holds nothing of its own: every write below is positional.
        with Path(filename).open("wb", buffering=0) as sink:
            download = _Download(sink.fileno(), bucket, key, head.get("e_tag"), extra)
            if not self._config.is_multipart(size):
                self._download_whole(download, report)
                return
            self._download_ranges(download, size, report)

    def download_fileobj(
        self,
        bucket: str,
        key: str,
        fileobj: BinaryIO,
        *,
        extra_args: DownloadExtraArgs | None = None,
        progress: Progress | None = None,
    ) -> None:
        """For destinations that are not a path on disk -- an open file, a socket, anything writable.

        One request however big the object is: such a destination has a single write position, so parts arriving out
        of order would have to be held in memory until their turn came. :meth:`download_file` has no such limit.
        """
        report = _Reporter(progress)
        extra: dict[str, Any] = dict(extra_args) if extra_args else {}

        def attempt() -> None:
            with self._client.get_object(
                bucket, key, config_overrides=_NO_PIPELINE_RETRY, **extra
            ) as output:
                for chunk in output.get("body") or ():
                    fileobj.write(chunk)
                    report(len(chunk))

        self._retrying(attempt)

    def _download_whole(self, download: _Download, report: _Reporter) -> None:
        def attempt() -> None:
            offset = 0
            with self._client.get_object(
                download.bucket,
                download.key,
                config_overrides=_NO_PIPELINE_RETRY,
                **download.extra,
            ) as output:
                for chunk in output.get("body") or ():
                    os.pwrite(download.fd, chunk, offset)
                    offset += len(chunk)
                    report(len(chunk))

        self._retrying(attempt)

    def _download_ranges(
        self, download: _Download, size: int, report: _Reporter
    ) -> None:
        with ThreadPoolExecutor(max_workers=self._config.max_concurrency) as pool:
            futures = [
                pool.submit(self._download_range, download, offset, length, report)
                for offset, length in self._config.part_ranges(size)
            ]
            for future in futures:
                future.result()

    def _download_range(
        self, download: _Download, offset: int, length: int, report: _Reporter
    ) -> None:
        def attempt() -> None:
            # if_match pins every range to the object we sized with head_object. Without it an overwrite
            # mid-download stitches bytes from two versions into a file that is corrupt but raises nothing.
            written = 0
            with self._client.get_object(
                download.bucket,
                download.key,
                config_overrides=_NO_PIPELINE_RETRY,
                range=f"bytes={offset}-{offset + length - 1}",
                **({"if_match": download.e_tag} if download.e_tag else {}),
                **download.extra,
            ) as output:
                for chunk in output.get("body") or ():
                    # Positional, so a replayed attempt overwrites rather than appending whatever the failed one
                    # managed to write.
                    os.pwrite(download.fd, chunk, offset + written)
                    written += len(chunk)
            report(written)

        self._retrying(attempt)

    def _retrying(self, attempt: Callable[[], T]) -> T:
        last = self._config.max_attempts
        for number in range(1, last + 1):
            try:
                return attempt()
            except Exception as exc:
                # Re-raising on the final attempt keeps the original traceback and leaves the loop with no
                # fall-through to guard -- an ``assert`` here would vanish under ``python -O``.
                if not _is_retryable(exc) or number == last:
                    raise
                time.sleep(
                    _retry_delay(number, getattr(exc, "is_throttling_error", False))
                )
        raise RuntimeError("unreachable: max_attempts is validated to be at least 1")
