"""Shared request-binding serialization runtime.

Hand-written, not regenerated. Text encodings for values bound to HTTP
labels, query parameters, and headers by the generated operations.
"""

from __future__ import annotations

import base64
import datetime
from email.utils import format_datetime


def as_utc(value: datetime.datetime) -> datetime.datetime:
    """Normalize to an aware UTC datetime; naive values are taken as UTC."""
    if value.tzinfo is None:
        return value.replace(tzinfo=datetime.timezone.utc)
    return value.astimezone(datetime.timezone.utc)


def fmt_date_time(value: datetime.datetime) -> str:
    """RFC 3339 with a ``Z`` designator, e.g. ``2015-01-25T08:00:00Z``."""
    return as_utc(value).isoformat().replace("+00:00", "Z")


def fmt_http_date(value: datetime.datetime) -> str:
    """IMF-fixdate, e.g. ``Sun, 25 Jan 2015 08:00:00 GMT``."""
    return format_datetime(as_utc(value), usegmt=True)


def fmt_epoch_seconds(value: datetime.datetime) -> str:
    """Seconds since the epoch; whole seconds carry no ``.0`` suffix."""
    ts = as_utc(value).timestamp()
    return str(int(ts)) if ts == int(ts) else str(ts)


def b64(value: bytes) -> str:
    return base64.b64encode(value).decode("ascii")


__all__ = [
    "as_utc",
    "b64",
    "fmt_date_time",
    "fmt_epoch_seconds",
    "fmt_http_date",
]
