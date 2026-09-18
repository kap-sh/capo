from __future__ import annotations

import base64
import hashlib
import zlib
from collections.abc import AsyncIterator, Iterator
from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Callable,
    ClassVar,
    Literal,
    Mapping,
    Protocol,
    Sequence,
    Union,
    cast,
)

from zapros import (
    AsyncBaseHandler,
    AsyncBaseMiddleware,
    AsyncClosableStream,
    BaseHandler,
    BaseMiddleware,
    ClosableStream,
    Request,
    Response,
)

from capo_s3.errors import ChecksumMismatch, ChecksumUnavailable

if TYPE_CHECKING:
    import google_crc32c
else:
    try:
        import google_crc32c
    except ImportError:
        google_crc32c = None

if TYPE_CHECKING:
    import xxhash
else:
    try:
        import xxhash
    except ImportError:
        xxhash = None

ChecksumAlgorithm = Literal[
    "CRC64NVME",
    "CRC32C",
    "CRC32",
    "XXHASH3",
    "XXHASH128",
    "XXHASH64",
    "MD5",
    "SHA1",
    "SHA256",
    "SHA512",
]

Buffer = Union[bytes, bytearray, memoryview]


class Hasher(Protocol):
    """Anything with ``update()`` and ``digest()``: hashlib, xxhash, the CRCs below."""

    def update(self, data: Buffer, /) -> None: ...

    def digest(self) -> bytes: ...


def _b64(hasher: Hasher) -> str:
    return base64.b64encode(hasher.digest()).decode("ascii")


_CRC32C_POLY = 0x82F63B78  # Castagnoli, reflected
_CRC64NVME_POLY = 0x9A6C9329AC4BC9B5  # NVMe / Rocksoft, reflected


def _crc_table(poly_reflected: int) -> list[int]:
    table = []
    for i in range(256):
        crc = i
        for _ in range(8):
            crc = (crc >> 1) ^ (poly_reflected if crc & 1 else 0)
        table.append(crc)
    return table


class _CrcHasher:
    """Reflected CRC with all-ones init and final-xor.

    The running value is the finalised CRC, which is also what zlib and
    google-crc32c take and return, so an accelerated ``update`` drops in.
    """

    width: ClassVar[int]
    _table: ClassVar[list[int]]

    def __init__(self) -> None:
        self._value = 0

    def update(self, data: Buffer, /) -> None:
        mask = (1 << self.width) - 1
        crc = self._value ^ mask
        for byte in bytes(data):
            crc = self._table[(crc ^ byte) & 0xFF] ^ (crc >> 8)
        self._value = crc ^ mask

    def value(self) -> int:
        return self._value

    def digest(self) -> bytes:
        return self._value.to_bytes(self.width // 8, "big")


class Crc32Hasher(_CrcHasher):
    """CRC-32/ISO-HDLC, 4 bytes."""

    width = 32

    def update(self, data: Buffer, /) -> None:
        self._value = zlib.crc32(data, self._value)


class Crc32cHasher(_CrcHasher):
    """CRC-32C/Castagnoli, 4 bytes. Accelerated by google-crc32c when installed."""

    width = 32
    _table = _crc_table(_CRC32C_POLY)

    def update(self, data: Buffer, /) -> None:
        if google_crc32c is None:
            super().update(data)
        else:
            self._value = google_crc32c.extend(self._value, data)


class Crc64NvmeHasher(_CrcHasher):
    """CRC-64/NVME, 8 bytes."""

    width = 64
    _table = _crc_table(_CRC64NVME_POLY)


@dataclass(frozen=True)
class Algorithm:
    name: ChecksumAlgorithm
    available: bool
    factory: Callable[[], Hasher]

    @property
    def header(self) -> str:
        return f"x-amz-checksum-{self.name.lower()}"


def _xx_factory(attr: str, name: str) -> Callable[[], Hasher]:
    def factory() -> Hasher:
        if xxhash is None:
            raise ChecksumUnavailable(f"{name} requires: pip install xxhash")
        return cast(Hasher, getattr(xxhash, attr)())

    return factory


# Iteration order is the response-validation preference, cheapest first. Every
# algorithm is listed whether or not its package is installed: recognising a
# header is what lets us knowingly skip one we cannot compute.
ALGORITHMS: dict[ChecksumAlgorithm, Algorithm] = {
    spec.name: spec
    for spec in (
        Algorithm("CRC64NVME", True, Crc64NvmeHasher),
        Algorithm("CRC32C", True, Crc32cHasher),
        Algorithm("CRC32", True, Crc32Hasher),
        Algorithm("XXHASH3", xxhash is not None, _xx_factory("xxh3_64", "XXHASH3")),
        Algorithm(
            "XXHASH128", xxhash is not None, _xx_factory("xxh3_128", "XXHASH128")
        ),
        Algorithm("XXHASH64", xxhash is not None, _xx_factory("xxh64", "XXHASH64")),
        Algorithm("MD5", True, hashlib.md5),
        Algorithm("SHA1", True, hashlib.sha1),
        Algorithm("SHA256", True, hashlib.sha256),
        Algorithm("SHA512", True, hashlib.sha512),
    )
}

LEGACY_MD5_HEADER = "Content-MD5"
SDK_ALGORITHM_HEADER = "x-amz-sdk-checksum-algorithm"
TRAILER_HEADER = "x-amz-trailer"
DECODED_LENGTH_HEADER = "x-amz-decoded-content-length"
STREAMING_UNSIGNED_PAYLOAD_TRAILER = "STREAMING-UNSIGNED-PAYLOAD-TRAILER"
_FLEXIBLE_HEADERS: frozenset[str] = frozenset(
    spec.header for spec in ALGORITHMS.values()
)
_STRIPPED_HEADERS: frozenset[str] = _FLEXIBLE_HEADERS | {
    SDK_ALGORITHM_HEADER,
    LEGACY_MD5_HEADER.lower(),
}
DEFAULT_REQUEST_ALGORITHM: ChecksumAlgorithm = "CRC32"


def strip_checksum_headers(request: Request) -> Request:
    """Drop every header that binds a request to a body, in place.

    For presigning: the URL is handed to someone else, who supplies the body,
    and presigning signs whatever headers it finds -- so any checksum left here
    is one the holder of the URL must reproduce exactly. That covers
    Content-MD5 as much as the x-amz-checksum-* family, and
    x-amz-sdk-checksum-algorithm goes too, since the service rejects that
    header without a matching value.
    """
    for name in [key for key in request.headers if key.lower() in _STRIPPED_HEADERS]:
        del request.headers[name]
    return request


def compute(algorithm: ChecksumAlgorithm, data: Buffer) -> str:
    """The base64 checksum of an in-memory body. The name is case-insensitive."""
    spec = ALGORITHMS.get(cast(ChecksumAlgorithm, algorithm.upper()))
    if spec is None:
        raise ValueError(f"unsupported checksum algorithm: {algorithm}")
    hasher = spec.factory()
    hasher.update(data)
    return _b64(hasher)


def _request_algorithm(algorithm: ChecksumAlgorithm | None) -> ChecksumAlgorithm:
    """The algorithm to checksum a request with: the caller's, else the default."""
    name = cast(ChecksumAlgorithm, (algorithm or DEFAULT_REQUEST_ALGORITHM).upper())
    if name not in ALGORITHMS:
        raise ValueError(f"unsupported checksum algorithm: {algorithm}")
    return name


def set_request_checksum(
    headers: dict[str, str], body: object, algorithm: ChecksumAlgorithm | None
) -> bool:
    """Set ``x-amz-checksum-<algorithm>`` for a buffered request body.

    ``algorithm`` is what the caller passed for the operation's
    requestAlgorithmMember; None means nobody asked and the default applies.

    Returns True once the request carries its checksum -- computed here, or
    already supplied by hand (an ``x-amz-checksum-*`` header, or ``Content-MD5``
    when no algorithm was requested). Returns False when a checksum is wanted
    but the body is a stream, which cannot be hashed up front: the caller then
    sends it as a trailer through :func:`trailing_checksum` instead.
    """
    present = {key.lower() for key in headers}
    if present & _FLEXIBLE_HEADERS:  # a hand-supplied checksum wins
        return True
    # Content-MD5 covers integrity, but does not stand in for a requested algorithm.
    if algorithm is None and LEGACY_MD5_HEADER.lower() in present:
        return True
    name = _request_algorithm(algorithm)
    if body is None:  # an absent payload is an empty one
        body = b""
    if not isinstance(body, (bytes, bytearray, memoryview)):
        return False
    headers[ALGORITHMS[name].header] = compute(name, cast(Buffer, body))
    return True


class TrailingChecksumStream(AsyncIterator[bytes], Iterator[bytes]):
    """A streaming request body in ``aws-chunked`` framing, hashed on its way out.

    Each chunk goes out as ``<hex size>\r\n<data>\r\n``; once the source is
    exhausted, one last item carries the completion chunk and the trailer,
    ``0\r\nx-amz-checksum-<algorithm>:<base64>\r\n\r\n``. The framing is part of
    the entity, not the transfer coding: the service parses it *after* the HTTP
    layer has undone ``Transfer-Encoding: chunked``, so a trailer in the HTTP
    trailer section never reaches it.

    Empty chunks are skipped -- ``0\r\n`` is the completion chunk, so one in the
    middle would end the body early. Whichever of ``__next__`` / ``__anext__``
    the transport drives is the one the wrapped stream supports.
    """

    def __init__(
        self,
        stream: Iterator[bytes] | AsyncIterator[bytes],
        algorithm: ChecksumAlgorithm,
    ) -> None:
        self.stream = stream
        self.algorithm = algorithm
        self.hasher = ALGORITHMS[algorithm].factory()
        self._done = False

    @property
    def header(self) -> str:
        return ALGORITHMS[self.algorithm].header

    def _frame(self, chunk: bytes) -> bytes:
        self.hasher.update(chunk)
        return f"{len(chunk):x}\r\n".encode("ascii") + chunk + b"\r\n"

    def _trailer(self) -> bytes:
        self._done = True
        return f"0\r\n{self.header}:{_b64(self.hasher)}\r\n\r\n".encode("ascii")

    def __next__(self) -> bytes:
        if self._done:
            raise StopIteration
        stream = cast(Iterator[bytes], self.stream)
        try:
            while True:
                chunk = next(stream)
                if chunk:
                    return self._frame(chunk)
        except StopIteration:
            return self._trailer()

    async def __anext__(self) -> bytes:
        if self._done:
            raise StopAsyncIteration
        stream = cast(AsyncIterator[bytes], self.stream)
        try:
            while True:
                chunk = await stream.__anext__()
                if chunk:
                    return self._frame(chunk)
        except StopAsyncIteration:
            return self._trailer()


def trailing_checksum(
    headers: dict[str, str],
    body: Iterator[bytes] | AsyncIterator[bytes],
    algorithm: ChecksumAlgorithm | None,
) -> TrailingChecksumStream:
    """Send a streaming body's checksum as an ``aws-chunked`` trailer.

    The wire format is what S3 documents for unsigned trailing checksums: the
    body in ``aws-chunked`` framing with ``x-amz-checksum-*`` in its trailer
    chunk, announced by ``x-amz-trailer``,
    ``x-amz-content-sha256: STREAMING-UNSIGNED-PAYLOAD-TRAILER`` and
    ``Content-Encoding: aws-chunked``. ``Content-Length`` gives way to
    ``x-amz-decoded-content-length`` -- the framed length is not known up
    front, so the transport sends the body with ``Transfer-Encoding: chunked``
    on top, as the AWS SDKs do.

    Returns the framed stream to send as the body.
    """
    stream = TrailingChecksumStream(body, _request_algorithm(algorithm))
    for key in list(headers):
        if key.lower() == "content-length":
            headers[DECODED_LENGTH_HEADER] = headers.pop(key)
        elif key.lower() == "content-encoding":
            headers[key] = f"aws-chunked, {headers[key]}"
    headers.setdefault("Content-Encoding", "aws-chunked")
    headers[TRAILER_HEADER] = stream.header
    headers["x-amz-content-sha256"] = STREAMING_UNSIGNED_PAYLOAD_TRAILER
    return stream


def is_composite(value: str) -> bool:
    """Whether a value is a multipart checksum, which S3 writes ``<base64>-<parts>``.

    Reproducing one needs the part boundaries, which the response does not carry.
    """
    _, dash, count = value.rpartition("-")
    return bool(dash and count.isdigit())


def _expected_checksum(
    response_algorithms: Sequence[ChecksumAlgorithm],
    headers: Mapping[str, str],
) -> tuple[ChecksumAlgorithm, str] | None:
    """The algorithm to validate with and the value the service sent, or None.

    None means nothing here is verifiable -- unrecognised, not installed, or
    composite -- which is skipped rather than failed.
    """
    allowed = {name.upper() for name in response_algorithms}
    present = {key.lower(): value for key, value in headers.items()}
    for name, spec in ALGORITHMS.items():
        if name not in allowed or not spec.available:
            continue
        value = present.get(spec.header)
        if value is not None and not is_composite(value):
            return name, value
    return None


class ChecksumStream(AsyncClosableStream, ClosableStream):
    """The response body, hashed on its way to the caller.

    Reads ``iter_raw`` because the service checksums the bytes it sent, not the
    content-decoded ones. Whichever of ``__next__`` / ``__anext__`` the response
    is driven by picks the matching underlying stream.
    """

    def __init__(
        self, response: Response, algorithm: ChecksumAlgorithm, expected: str
    ) -> None:
        self.response = response
        self.algorithm = algorithm
        self.expected = expected
        self.hasher = ALGORITHMS[algorithm].factory()
        self.sync_raw_stream = response.iter_raw()
        self.async_raw_stream = response.async_iter_raw()

    def verify(self) -> None:
        actual = _b64(self.hasher)
        if actual != self.expected:
            raise ChecksumMismatch(self.algorithm, self.expected, actual)

    def __next__(self) -> bytes:
        try:
            chunk = next(self.sync_raw_stream)
        except StopIteration:
            self.verify()
            raise
        self.hasher.update(chunk)
        return chunk

    async def __anext__(self) -> bytes:
        try:
            chunk = await self.async_raw_stream.__anext__()
        except StopAsyncIteration:
            self.verify()
            raise
        self.hasher.update(chunk)
        return chunk

    def close(self) -> None:
        self.response.close()

    async def aclose(self) -> None:
        await self.response.aclose()


class ChecksumMiddleware(BaseMiddleware, AsyncBaseMiddleware):
    """Validate response bodies against the checksum header the service sent.

    The operation's responseAlgorithms arrive in ``context["checksum_algorithms"]``.
    """

    def __init__(self, next_handler: BaseHandler | AsyncBaseHandler) -> None:
        self.next = cast(BaseHandler, next_handler)
        self.async_next = cast(AsyncBaseHandler, next_handler)

    def handle(self, request: Request) -> Response:
        return _validating(request, self.next.handle(request))

    async def ahandle(self, request: Request) -> Response:
        return _validating(request, await self.async_next.ahandle(request))


def _validating(request: Request, response: Response) -> Response:
    """``response`` with a checksum-verifying body, or unchanged if none applies."""
    # A ranged GET is answered with the whole object's checksum over a slice of
    # its body. partNumber is unaffected: that returns the part's own checksum.
    if "range" in request.headers:
        return response
    algorithms = cast(
        "Sequence[ChecksumAlgorithm]", request.context.get("checksum_algorithms", ())
    )
    found = _expected_checksum(algorithms, response.headers)
    if found is None:
        return response
    algorithm, expected = found
    return Response(
        response.status,
        response.headers,
        content=ChecksumStream(response, algorithm, expected),
        context=response.context,
        request=response.request,
    )
