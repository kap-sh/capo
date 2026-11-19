"""Generated from Smithy shape ``com.amazonaws.lambda#ResumeDurableExecutionResponse``."""

from typing_extensions import TypedDict


class ResumeDurableExecutionResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: ResumeDurableExecutionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ResumeDurableExecutionResponse:
    out: ResumeDurableExecutionResponse = {}  # type: ignore[typeddict-item]
    return out
