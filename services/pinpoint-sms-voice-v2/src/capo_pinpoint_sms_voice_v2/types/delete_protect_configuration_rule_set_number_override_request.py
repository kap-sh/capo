"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteProtectConfigurationRuleSetNumberOverrideRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.phone_number
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn


class DeleteProtectConfigurationRuleSetNumberOverrideRequest(TypedDict, closed=True):
    protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
    """<p>The unique identifier for the protect configuration.</p>"""
    destination_phone_number: (
        "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    )
    """<p>The destination phone number in E.164 format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: DeleteProtectConfigurationRuleSetNumberOverrideRequest,
) -> dict:
    out: dict = {}
    out["ProtectConfigurationId"] = value["protect_configuration_id"]
    out["DestinationPhoneNumber"] = value["destination_phone_number"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> DeleteProtectConfigurationRuleSetNumberOverrideRequest:
    out: DeleteProtectConfigurationRuleSetNumberOverrideRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProtectConfigurationId") is not None:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    else:
        out["protect_configuration_id"] = ""
    if data.get("DestinationPhoneNumber") is not None:
        out["destination_phone_number"] = data["DestinationPhoneNumber"]
    else:
        out["destination_phone_number"] = ""
    return out
