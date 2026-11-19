"""Generated from Smithy shape ``com.amazonaws.lambda#PauseDurableExecutionResponse``."""

from typing_extensions import TypedDict


class PauseDurableExecutionResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PauseDurableExecutionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PauseDurableExecutionResponse:
    out: PauseDurableExecutionResponse = {}  # type: ignore[typeddict-item]
    return out
