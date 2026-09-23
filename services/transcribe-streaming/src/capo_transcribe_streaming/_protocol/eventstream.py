"""Shared Amazon eventstream binary-format runtime.

Hand-written, not regenerated. Provides framing, header encoding, and
checksum validation for Smithy event-stream messages.
"""

from __future__ import annotations

import datetime
import uuid
import zlib
from collections.abc import AsyncIterator, Callable, Iterator
from dataclasses import dataclass, field
from typing import TypeVar, Union

HeaderValue = Union[bool, int, bytes, str, datetime.datetime, uuid.UUID]
T = TypeVar("T")


# Header type constants from the Amazon eventstream specification.
_TRUE_HEADER = 0x00
_FALSE_HEADER = 0x01
_BYTE_HEADER = 0x02
_SHORT_HEADER = 0x03
_INTEGER_HEADER = 0x04
_LONG_HEADER = 0x05
_BYTE_ARRAY_HEADER = 0x06
_STRING_HEADER = 0x07
_TIMESTAMP_HEADER = 0x08
_UUID_HEADER = 0x09


def _encode_header_value(value: HeaderValue) -> bytes:
    if isinstance(value, bool):
        return bytes([_TRUE_HEADER if value else _FALSE_HEADER])
    if isinstance(value, int):
        if -128 <= value <= 127:
            return bytes([_BYTE_HEADER]) + value.to_bytes(1, "big", signed=True)
        if -32768 <= value <= 32767:
            return bytes([_SHORT_HEADER]) + value.to_bytes(2, "big", signed=True)
        if -2147483648 <= value <= 2147483647:
            return bytes([_INTEGER_HEADER]) + value.to_bytes(4, "big", signed=True)
        # Fall through to signed 64-bit.
        return bytes([_LONG_HEADER]) + value.to_bytes(8, "big", signed=True)
    if isinstance(value, bytes):
        return bytes([_BYTE_ARRAY_HEADER]) + len(value).to_bytes(2, "big") + value
    if isinstance(value, str):
        encoded = value.encode("utf-8")
        return bytes([_STRING_HEADER]) + len(encoded).to_bytes(2, "big") + encoded
    if isinstance(value, datetime.datetime):
        millis = int(value.timestamp() * 1000)
        return bytes([_TIMESTAMP_HEADER]) + millis.to_bytes(8, "big", signed=True)
    if isinstance(value, uuid.UUID):
        return bytes([_UUID_HEADER]) + value.bytes
    raise TypeError(f"unsupported eventstream header value: {value!r}")


def _decode_header_value(
    type_byte: int, data: bytes | bytearray, pos: int
) -> tuple[HeaderValue, int]:
    if type_byte == _TRUE_HEADER:
        return True, pos
    if type_byte == _FALSE_HEADER:
        return False, pos
    if type_byte == _BYTE_HEADER:
        return int.from_bytes(data[pos : pos + 1], "big", signed=True), pos + 1
    if type_byte == _SHORT_HEADER:
        return int.from_bytes(data[pos : pos + 2], "big", signed=True), pos + 2
    if type_byte == _INTEGER_HEADER:
        return int.from_bytes(data[pos : pos + 4], "big", signed=True), pos + 4
    if type_byte == _LONG_HEADER:
        return int.from_bytes(data[pos : pos + 8], "big", signed=True), pos + 8
    if type_byte == _BYTE_ARRAY_HEADER:
        length = int.from_bytes(data[pos : pos + 2], "big")
        pos += 2
        return bytes(data[pos : pos + length]), pos + length
    if type_byte == _STRING_HEADER:
        length = int.from_bytes(data[pos : pos + 2], "big")
        pos += 2
        return data[pos : pos + length].decode("utf-8"), pos + length
    if type_byte == _TIMESTAMP_HEADER:
        millis = int.from_bytes(data[pos : pos + 8], "big", signed=True)
        return (
            datetime.datetime.fromtimestamp(millis / 1000, tz=datetime.timezone.utc),
            pos + 8,
        )
    if type_byte == _UUID_HEADER:
        return uuid.UUID(bytes=bytes(data[pos : pos + 16])), pos + 16
    raise ValueError(f"unsupported eventstream header type: {type_byte:#x}")


def _encode_headers(headers: dict[str, HeaderValue]) -> bytes:
    parts: list[bytes] = []
    for name, value in headers.items():
        name_bytes = name.encode("utf-8")
        if len(name_bytes) > 255:
            raise ValueError(f"eventstream header name too long: {name!r}")
        parts.append(bytes([len(name_bytes)]) + name_bytes)
        parts.append(_encode_header_value(value))
    return b"".join(parts)


def _decode_headers(data: bytes | bytearray) -> dict[str, HeaderValue]:
    pos = 0
    headers: dict[str, HeaderValue] = {}
    while pos < len(data):
        name_len = data[pos]
        pos += 1
        name = data[pos : pos + name_len].decode("utf-8")
        pos += name_len
        type_byte = data[pos]
        pos += 1
        value, pos = _decode_header_value(type_byte, data, pos)
        headers[name] = value
    return headers


@dataclass
class Message:
    """A single Amazon eventstream message."""

    headers: dict[str, HeaderValue] = field(default_factory=dict)
    payload: bytes = b""

    def encode(self) -> bytes:
        """Serialize this message into eventstream framing bytes."""
        headers_bytes = _encode_headers(self.headers)
        headers_length = len(headers_bytes)
        payload = self.payload
        # total_length covers the whole frame, trailing message CRC included.
        total_length = 12 + headers_length + len(payload) + 4

        prelude = total_length.to_bytes(4, "big") + headers_length.to_bytes(4, "big")
        prelude_crc = zlib.crc32(prelude).to_bytes(4, "big")
        message_body = prelude + prelude_crc + headers_bytes + payload
        message_crc = zlib.crc32(message_body).to_bytes(4, "big")
        return message_body + message_crc


@dataclass
class MessageDecoder:
    """Stateful decoder that turns byte chunks into :class:`Message` objects.

    ``feed`` may emit zero, one, or many messages for each chunk. Partial
    frames are buffered until the next chunk completes them.
    """

    _buffer: bytearray = field(default_factory=bytearray, init=False)

    def feed(self, data: bytes) -> Iterator[Message]:
        """Append ``data`` to the internal buffer and yield any full messages."""
        self._buffer.extend(data)
        while True:
            if len(self._buffer) < 12:
                return

            total_length = int.from_bytes(self._buffer[:4], "big")
            headers_length = int.from_bytes(self._buffer[4:8], "big")
            prelude = bytes(self._buffer[:8])
            prelude_crc = int.from_bytes(self._buffer[8:12], "big")

            # total_length covers the whole frame: 12-byte prelude, headers,
            # payload, and the trailing 4-byte message CRC.
            if total_length < 16 + headers_length:
                raise ValueError(
                    f"invalid eventstream message: total_length={total_length} "
                    f"is smaller than minimum {16 + headers_length}"
                )

            if len(self._buffer) < total_length:
                return

            computed_prelude_crc = zlib.crc32(prelude) & 0xFFFFFFFF
            if computed_prelude_crc != prelude_crc:
                raise ValueError("eventstream prelude checksum mismatch")

            payload_end = total_length - 4
            message_bytes = bytes(self._buffer[:payload_end])
            message_crc = int.from_bytes(self._buffer[payload_end:total_length], "big")
            computed_message_crc = zlib.crc32(message_bytes) & 0xFFFFFFFF
            if computed_message_crc != message_crc:
                raise ValueError("eventstream message checksum mismatch")

            headers = _decode_headers(self._buffer[12 : 12 + headers_length])
            payload = bytes(self._buffer[12 + headers_length : payload_end])
            del self._buffer[:total_length]
            yield Message(headers=headers, payload=payload)


def raw_stream_to_events(
    raw_stream: Iterator[bytes], decoder: MessageDecoder, deser: Callable[[Message], T]
) -> Iterator[T]:
    """Map a raw byte iterator into deserialized event objects."""
    for chunk in raw_stream:
        for message in decoder.feed(chunk):
            yield deser(message)


async def async_raw_stream_to_events(
    raw_stream: AsyncIterator[bytes],
    decoder: MessageDecoder,
    deser: Callable[[Message], T],
) -> AsyncIterator[T]:
    """Map an async raw byte iterator into deserialized event objects."""
    async for chunk in raw_stream:
        for message in decoder.feed(chunk):
            yield deser(message)


def read_messages(
    raw_stream: Iterator[bytes], decoder: MessageDecoder
) -> Iterator[Message]:
    """Yield :class:`Message` objects framed out of a raw byte iterator.

    Used by RPC event streams (e.g. awsJson) where the first message may be an
    initial-response that must be pulled off before consuming the events.
    """
    for chunk in raw_stream:
        yield from decoder.feed(chunk)


async def async_read_messages(
    raw_stream: AsyncIterator[bytes], decoder: MessageDecoder
) -> AsyncIterator[Message]:
    """Async variant of :func:`read_messages`."""
    async for chunk in raw_stream:
        for message in decoder.feed(chunk):
            yield message


__all__ = [
    "HeaderValue",
    "Message",
    "MessageDecoder",
    "async_raw_stream_to_events",
    "async_read_messages",
    "raw_stream_to_events",
    "read_messages",
]
