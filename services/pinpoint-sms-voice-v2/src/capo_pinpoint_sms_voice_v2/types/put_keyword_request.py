"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PutKeywordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.keyword
    import capo_pinpoint_sms_voice_v2.types.keyword_action
    import capo_pinpoint_sms_voice_v2.types.keyword_message
    import capo_pinpoint_sms_voice_v2.types.phone_or_pool_id_or_arn


class PutKeywordRequest(TypedDict, closed=True):
    origination_identity: (
        "capo_pinpoint_sms_voice_v2.types.phone_or_pool_id_or_arn.PhoneOrPoolIdOrArn"
    )
    """<p>The origination identity to use such as a PhoneNumberId, PhoneNumberArn, SenderId or SenderIdArn. You can use <a>DescribePhoneNumbers</a> get the values for PhoneNumberId and PhoneNumberArn while <a>DescribeSenderIds</a> can be used to get the values for SenderId and SenderIdArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    keyword: "capo_pinpoint_sms_voice_v2.types.keyword.Keyword"
    """<p>The new keyword to add.</p>"""
    keyword_message: "capo_pinpoint_sms_voice_v2.types.keyword_message.KeywordMessage"
    """<p>The message associated with the keyword.</p>"""
    keyword_action: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.keyword_action.KeywordAction"
    ]
    """<p>The action to perform for the new keyword when it is received.</p> <ul> <li> <p>AUTOMATIC_RESPONSE: A message is sent to the recipient.</p> </li> <li> <p>OPT_OUT: Keeps the recipient from receiving future messages.</p> </li> <li> <p>OPT_IN: The recipient wants to receive future messages.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutKeywordRequest) -> dict:
    out: dict = {}
    out["OriginationIdentity"] = value["origination_identity"]
    out["Keyword"] = value["keyword"]
    out["KeywordMessage"] = value["keyword_message"]
    if "keyword_action" in value:
        out["KeywordAction"] = value["keyword_action"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutKeywordRequest:
    out: PutKeywordRequest = {}  # type: ignore[typeddict-item]
    if data.get("OriginationIdentity") is not None:
        out["origination_identity"] = data["OriginationIdentity"]
    else:
        out["origination_identity"] = ""
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
    return out
