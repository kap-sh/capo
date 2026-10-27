"""Generated from Smithy shape ``com.amazonaws.medialive#AutoFilterSettings``."""

from typing_extensions import TypedDict


class AutoFilterSettings(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: AutoFilterSettings) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AutoFilterSettings:
    out: AutoFilterSettings = {}  # type: ignore[typeddict-item]
    return out
