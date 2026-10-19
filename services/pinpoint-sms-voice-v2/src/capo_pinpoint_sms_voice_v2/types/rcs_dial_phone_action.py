"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsDialPhoneAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.phone_number
    import capo_pinpoint_sms_voice_v2.types.rcs_postback_data
    import capo_pinpoint_sms_voice_v2.types.rcs_suggested_action_text


class RcsDialPhoneAction(TypedDict, closed=True):
    text: "capo_pinpoint_sms_voice_v2.types.rcs_suggested_action_text.RcsSuggestedActionText"
    """<p>The display text of the action. Maximum 25 characters.</p>"""
    postback_data: "capo_pinpoint_sms_voice_v2.types.rcs_postback_data.RcsPostbackData"
    """<p>The postback data sent to your webhook when the user taps this action. Maximum 2048 characters.</p>"""
    phone_number: "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    """<p>The phone number to dial in E.164 format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsDialPhoneAction) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    out["PostbackData"] = value["postback_data"]
    out["PhoneNumber"] = value["phone_number"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RcsDialPhoneAction:
    out: RcsDialPhoneAction = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        out["text"] = ""
    if data.get("PostbackData") is not None:
        out["postback_data"] = data["PostbackData"]
    else:
        out["postback_data"] = ""
    if data.get("PhoneNumber") is not None:
        out["phone_number"] = data["PhoneNumber"]
    else:
        out["phone_number"] = ""
    return out
