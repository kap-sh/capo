"""rpcv2Cbor runtime: the CBOR codec and error parsing."""

from __future__ import annotations

import datetime
from typing import Any

import cbor2
from zapros import Response

PROTOCOL = "rpc-v2-cbor"


def dumps(value: object) -> bytes:
    """Encode a serialized shape.

    A datetime goes out as a tag 1 epoch timestamp, the only timestamp
    form the protocol has; a naive one is taken as UTC.
    """
    return cbor2.dumps(
        value, datetime_as_timestamp=True, timezone=datetime.timezone.utc
    )


def loads(data: bytes) -> Any:
    """Decode a response body. Tag 1 timestamps come back as aware UTC datetimes."""
    return cbor2.loads(data)


def parse_error(response: Response) -> tuple[dict, str | None, str | None]:
    """Return ``(data, code, message)`` from an rpcv2Cbor error response.

    ``code`` is the shape name out of the ``__type`` body field, which
    holds the error's absolute shape ID. The ``X-Amzn-Errortype`` header
    and the ``code`` body field are not consulted.

    A response without the ``smithy-protocol: rpc-v2-cbor`` header, or
    whose body is not a CBOR map, is malformed: nothing in it is
    interpreted and ``code`` is ``None``, which leaves the caller with
    the status code alone.
    """
    if response.headers.get("smithy-protocol") != PROTOCOL:
        return {}, None, f"response is missing the smithy-protocol: {PROTOCOL} header"
    try:
        data = loads(response.read())
    except cbor2.CBORDecodeError:
        data = None
    if not isinstance(data, dict):
        return {}, None, "response body is not a CBOR map"
    type_ = data.get("__type")
    code = type_.rsplit("#", 1)[-1] if isinstance(type_, str) else None
    message = data.get("message") or data.get("Message")
    return data, code, message


__all__ = ["PROTOCOL", "dumps", "loads", "parse_error"]
