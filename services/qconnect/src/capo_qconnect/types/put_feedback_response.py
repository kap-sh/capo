"""Generated from Smithy shape ``com.amazonaws.qconnect#PutFeedbackResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.content_feedback_data
    import capo_qconnect.types.target_type
    import capo_qconnect.types.uuid
    import capo_qconnect.types.uuid_or_arn


class PutFeedbackResponse(TypedDict, closed=True):
    assistant_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the Amazon Q in Connect assistant.</p>"""
    assistant_arn: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.</p>"""
    target_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the feedback target.</p>"""
    target_type: "capo_qconnect.types.target_type.TargetType"
    """<p>The type of the feedback target.</p>"""
    content_feedback: "capo_qconnect.types.content_feedback_data.ContentFeedbackData"
    """<p>Information about the feedback provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutFeedbackResponse) -> dict:
    out: dict = {}
    out["assistantId"] = value["assistant_id"]
    out["assistantArn"] = value["assistant_arn"]
    out["targetId"] = value["target_id"]
    out["targetType"] = value["target_type"]
    import capo_qconnect.types.content_feedback_data

    out["contentFeedback"] = capo_qconnect.types.content_feedback_data.serialize_json(
        value["content_feedback"]
    )
    return out


def deserialize_json(data: dict) -> PutFeedbackResponse:
    out: PutFeedbackResponse = {}  # type: ignore[typeddict-item]
    if data.get("assistantId") is not None:
        out["assistant_id"] = data["assistantId"]
    else:
        out["assistant_id"] = ""
    if data.get("assistantArn") is not None:
        out["assistant_arn"] = data["assistantArn"]
    else:
        out["assistant_arn"] = ""
    if data.get("targetId") is not None:
        out["target_id"] = data["targetId"]
    else:
        out["target_id"] = ""
    if data.get("targetType") is not None:
        out["target_type"] = data["targetType"]
    else:
        out["target_type"] = ""
    if data.get("contentFeedback") is not None:
        import capo_qconnect.types.content_feedback_data

        out["content_feedback"] = (
            capo_qconnect.types.content_feedback_data.deserialize_json(
                data["contentFeedback"]
            )
        )
    else:
        import capo_qconnect.types._unknown

        out["content_feedback"] = capo_qconnect.types._unknown.UnknownUnionMember("")
    return out
