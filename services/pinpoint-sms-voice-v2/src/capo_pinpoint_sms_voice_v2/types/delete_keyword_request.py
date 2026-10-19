"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteKeywordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.keyword
    import capo_pinpoint_sms_voice_v2.types.phone_or_pool_id_or_arn


class DeleteKeywordRequest(TypedDict, closed=True):
    origination_identity: (
        "capo_pinpoint_sms_voice_v2.types.phone_or_pool_id_or_arn.PhoneOrPoolIdOrArn"
    )
    """<p>The origination identity to use such as a PhoneNumberId, PhoneNumberArn, PoolId or PoolArn. You can use <a>DescribePhoneNumbers</a> to find the values for PhoneNumberId and PhoneNumberArn and <a>DescribePools</a> to find the values of PoolId and PoolArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    keyword: "capo_pinpoint_sms_voice_v2.types.keyword.Keyword"
    """<p>The keyword to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteKeywordRequest) -> dict:
    out: dict = {}
    out["OriginationIdentity"] = value["origination_identity"]
    out["Keyword"] = value["keyword"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteKeywordRequest:
    out: DeleteKeywordRequest = {}  # type: ignore[typeddict-item]
    if data.get("OriginationIdentity") is not None:
        out["origination_identity"] = data["OriginationIdentity"]
    else:
        out["origination_identity"] = ""
    if data.get("Keyword") is not None:
        out["keyword"] = data["Keyword"]
    else:
        out["keyword"] = ""
    return out
