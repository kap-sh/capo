"""Generated from Smithy shape ``com.amazonaws.artifact#PutComplianceInquiryFeedbackResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.timestamp_attribute


class PutComplianceInquiryFeedbackResponse(TypedDict, closed=True):
    submitted_at: "capo_artifact.types.timestamp_attribute.TimestampAttribute"
    """<p>The timestamp when the feedback was submitted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutComplianceInquiryFeedbackResponse) -> dict:
    out: dict = {}
    import capo_artifact.types.timestamp_attribute

    out["submittedAt"] = capo_artifact.types.timestamp_attribute.serialize_json(
        value["submitted_at"]
    )
    return out


def deserialize_json(data: dict) -> PutComplianceInquiryFeedbackResponse:
    out: PutComplianceInquiryFeedbackResponse = {}  # type: ignore[typeddict-item]
    if data.get("submittedAt") is not None:
        import capo_artifact.types.timestamp_attribute

        out["submitted_at"] = capo_artifact.types.timestamp_attribute.deserialize_json(
            data["submittedAt"]
        )
    else:
        import datetime

        out["submitted_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
