"""Generated from Smithy shape ``com.amazonaws.supportauthz#TagResourceOutput``."""

from typing_extensions import TypedDict


class TagResourceOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> TagResourceOutput:
    out: TagResourceOutput = {}  # type: ignore[typeddict-item]
    return out
