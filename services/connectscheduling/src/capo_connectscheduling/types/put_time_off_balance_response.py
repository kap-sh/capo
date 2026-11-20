"""Generated from Smithy shape ``com.amazonaws.connectscheduling#PutTimeOffBalanceResponse``."""

from typing_extensions import TypedDict


class PutTimeOffBalanceResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutTimeOffBalanceResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutTimeOffBalanceResponse:
    out: PutTimeOffBalanceResponse = {}  # type: ignore[typeddict-item]
    return out
