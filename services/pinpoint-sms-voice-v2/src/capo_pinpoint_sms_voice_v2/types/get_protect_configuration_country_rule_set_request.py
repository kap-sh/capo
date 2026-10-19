"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#GetProtectConfigurationCountryRuleSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.number_capability
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn


class GetProtectConfigurationCountryRuleSetRequest(TypedDict, closed=True):
    protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
    """<p>The unique identifier for the protect configuration.</p>"""
    number_capability: (
        "capo_pinpoint_sms_voice_v2.types.number_capability.NumberCapability"
    )
    """<p>The capability type to return the CountryRuleSet for. Valid values are <code>SMS</code>, <code>VOICE</code>, or <code>MMS</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetProtectConfigurationCountryRuleSetRequest) -> dict:
    out: dict = {}
    out["ProtectConfigurationId"] = value["protect_configuration_id"]
    out["NumberCapability"] = value["number_capability"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> GetProtectConfigurationCountryRuleSetRequest:
    out: GetProtectConfigurationCountryRuleSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProtectConfigurationId") is not None:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    else:
        out["protect_configuration_id"] = ""
    if data.get("NumberCapability") is not None:
        out["number_capability"] = data["NumberCapability"]
    else:
        out["number_capability"] = ""
    return out
