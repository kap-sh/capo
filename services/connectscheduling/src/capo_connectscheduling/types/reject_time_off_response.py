"""Generated from Smithy shape ``com.amazonaws.connectscheduling#RejectTimeOffResponse``."""

from typing_extensions import TypedDict


class RejectTimeOffResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: RejectTimeOffResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RejectTimeOffResponse:
    out: RejectTimeOffResponse = {}  # type: ignore[typeddict-item]
    return out
