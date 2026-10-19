"""Generated from Smithy shape ``com.amazonaws.rekognition#FeedbackItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.feedback_code
    import capo_rekognition.types.feedback_message


class FeedbackItem(TypedDict, closed=True):
    code: "capo_rekognition.types.feedback_code.FeedbackCode"
    """<p>A code identifying the condition that was detected during the Face Liveness session.</p>"""
    message: "capo_rekognition.types.feedback_message.FeedbackMessage"
    """<p>A human-readable description of the detected condition, suitable for displaying to an end user before they retry a Face Liveness check. Use <code>Code</code> rather than this message for programmatic decisions, because the message text can change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeedbackItem) -> dict:
    out: dict = {}
    import capo_rekognition.types.feedback_code

    out["Code"] = capo_rekognition.types.feedback_code.serialize_aws_json_1_1(
        value["code"]
    )
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FeedbackItem:
    out: FeedbackItem = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        import capo_rekognition.types.feedback_code

        out["code"] = capo_rekognition.types.feedback_code.deserialize_aws_json_1_1(
            data["Code"]
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_rekognition.types.feedback_code.FeedbackCode", ""
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out
