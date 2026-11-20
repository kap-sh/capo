"""Generated from Smithy shape ``com.amazonaws.connectscheduling#CancelTimeOffResponse``."""

from typing_extensions import TypedDict


class CancelTimeOffResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelTimeOffResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelTimeOffResponse:
    out: CancelTimeOffResponse = {}  # type: ignore[typeddict-item]
    return out
