"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#VerifyDestinationNumberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.verification_code
    import capo_pinpoint_sms_voice_v2.types.verified_destination_number_id_or_arn


class VerifyDestinationNumberRequest(TypedDict, closed=True):
    verified_destination_number_id: "capo_pinpoint_sms_voice_v2.types.verified_destination_number_id_or_arn.VerifiedDestinationNumberIdOrArn"
    """<p>The unique identifier for the verififed destination phone number.</p>"""
    verification_code: (
        "capo_pinpoint_sms_voice_v2.types.verification_code.VerificationCode"
    )
    """<p>The verification code that was received by the verified destination phone number.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VerifyDestinationNumberRequest) -> dict:
    out: dict = {}
    out["VerifiedDestinationNumberId"] = value["verified_destination_number_id"]
    out["VerificationCode"] = value["verification_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VerifyDestinationNumberRequest:
    out: VerifyDestinationNumberRequest = {}  # type: ignore[typeddict-item]
    if data.get("VerifiedDestinationNumberId") is not None:
        out["verified_destination_number_id"] = data["VerifiedDestinationNumberId"]
    else:
        out["verified_destination_number_id"] = ""
    if data.get("VerificationCode") is not None:
        out["verification_code"] = data["VerificationCode"]
    else:
        out["verification_code"] = ""
    return out
