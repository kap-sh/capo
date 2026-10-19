"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PutMessageFeedbackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.message_feedback_status
    import capo_pinpoint_sms_voice_v2.types.message_id


class PutMessageFeedbackRequest(TypedDict, closed=True):
    message_id: "capo_pinpoint_sms_voice_v2.types.message_id.MessageId"
    """<p>The unique identifier for the message.</p>"""
    message_feedback_status: (
        "capo_pinpoint_sms_voice_v2.types.message_feedback_status.MessageFeedbackStatus"
    )
    """<p>Set the message feedback to be either <code>RECEIVED</code> or <code>FAILED</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutMessageFeedbackRequest) -> dict:
    out: dict = {}
    out["MessageId"] = value["message_id"]
    out["MessageFeedbackStatus"] = value["message_feedback_status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutMessageFeedbackRequest:
    out: PutMessageFeedbackRequest = {}  # type: ignore[typeddict-item]
    if data.get("MessageId") is not None:
        out["message_id"] = data["MessageId"]
    else:
        out["message_id"] = ""
    if data.get("MessageFeedbackStatus") is not None:
        out["message_feedback_status"] = data["MessageFeedbackStatus"]
    else:
        out["message_feedback_status"] = ""
    return out
