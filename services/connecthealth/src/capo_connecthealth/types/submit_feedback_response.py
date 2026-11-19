"""Generated from Smithy shape ``com.amazonaws.connecthealth#SubmitFeedbackResponse``."""

from typing_extensions import TypedDict


class SubmitFeedbackResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: SubmitFeedbackResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SubmitFeedbackResponse:
    out: SubmitFeedbackResponse = {}  # type: ignore[typeddict-item]
    return out
