"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsReplyAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.rcs_postback_data
    import capo_pinpoint_sms_voice_v2.types.rcs_suggested_action_text


class RcsReplyAction(TypedDict, closed=True):
    text: "capo_pinpoint_sms_voice_v2.types.rcs_suggested_action_text.RcsSuggestedActionText"
    """<p>The display text of the suggested reply. Maximum 25 characters.</p>"""
    postback_data: "capo_pinpoint_sms_voice_v2.types.rcs_postback_data.RcsPostbackData"
    """<p>The postback data sent to your webhook when the user taps this reply. Maximum 2048 characters.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsReplyAction) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    out["PostbackData"] = value["postback_data"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RcsReplyAction:
    out: RcsReplyAction = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        out["text"] = ""
    if data.get("PostbackData") is not None:
        out["postback_data"] = data["PostbackData"]
    else:
        out["postback_data"] = ""
    return out
