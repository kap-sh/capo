"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ReleaseSenderIdRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.iso_country_code
    import capo_pinpoint_sms_voice_v2.types.sender_id_or_arn


class ReleaseSenderIdRequest(TypedDict, closed=True):
    sender_id: "capo_pinpoint_sms_voice_v2.types.sender_id_or_arn.SenderIdOrArn"
    """<p>The sender ID to release.</p>"""
    iso_country_code: "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReleaseSenderIdRequest) -> dict:
    out: dict = {}
    out["SenderId"] = value["sender_id"]
    out["IsoCountryCode"] = value["iso_country_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ReleaseSenderIdRequest:
    out: ReleaseSenderIdRequest = {}  # type: ignore[typeddict-item]
    if data.get("SenderId") is not None:
        out["sender_id"] = data["SenderId"]
    else:
        out["sender_id"] = ""
    if data.get("IsoCountryCode") is not None:
        out["iso_country_code"] = data["IsoCountryCode"]
    else:
        out["iso_country_code"] = ""
    return out
