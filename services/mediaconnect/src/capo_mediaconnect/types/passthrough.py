"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Passthrough``."""

from typing_extensions import TypedDict


class Passthrough(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: Passthrough) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> Passthrough:
    out: Passthrough = {}  # type: ignore[typeddict-item]
    return out
