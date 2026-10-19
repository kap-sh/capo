"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#KeywordInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.keyword
    import capo_pinpoint_sms_voice_v2.types.keyword_action
    import capo_pinpoint_sms_voice_v2.types.keyword_message


class KeywordInformation(TypedDict, closed=True):
    keyword: "capo_pinpoint_sms_voice_v2.types.keyword.Keyword"
    """<p>The keyword as a string.</p>"""
    keyword_message: "capo_pinpoint_sms_voice_v2.types.keyword_message.KeywordMessage"
    """<p>A custom message that can be used with the keyword.</p>"""
    keyword_action: "capo_pinpoint_sms_voice_v2.types.keyword_action.KeywordAction"
    """<p>The action to perform for the keyword.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeywordInformation) -> dict:
    out: dict = {}
    out["Keyword"] = value["keyword"]
    out["KeywordMessage"] = value["keyword_message"]
    out["KeywordAction"] = value["keyword_action"]
    return out


def deserialize_aws_json_1_0(data: dict) -> KeywordInformation:
    out: KeywordInformation = {}  # type: ignore[typeddict-item]
    if data.get("Keyword") is not None:
        out["keyword"] = data["Keyword"]
    else:
        out["keyword"] = ""
    if data.get("KeywordMessage") is not None:
        out["keyword_message"] = data["KeywordMessage"]
    else:
        out["keyword_message"] = ""
    if data.get("KeywordAction") is not None:
        out["keyword_action"] = data["KeywordAction"]
    else:
        out["keyword_action"] = ""
    return out
