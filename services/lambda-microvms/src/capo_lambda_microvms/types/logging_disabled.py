"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#LoggingDisabled``."""

from typing_extensions import TypedDict


class LoggingDisabled(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: LoggingDisabled) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> LoggingDisabled:
    out: LoggingDisabled = {}  # type: ignore[typeddict-item]
    return out
