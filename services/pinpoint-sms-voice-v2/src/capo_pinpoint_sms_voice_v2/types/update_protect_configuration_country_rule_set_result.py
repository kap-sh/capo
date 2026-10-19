"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#UpdateProtectConfigurationCountryRuleSetResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.number_capability
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_arn
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id


class UpdateProtectConfigurationCountryRuleSetResult(TypedDict, closed=True):
    protect_configuration_arn: "capo_pinpoint_sms_voice_v2.types.protect_configuration_arn.ProtectConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the protect configuration.</p>"""
    protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id.ProtectConfigurationId"
    """<p>The unique identifier for the protect configuration.</p>"""
    number_capability: (
        "capo_pinpoint_sms_voice_v2.types.number_capability.NumberCapability"
    )
    """<p>The number capability that was updated</p>"""
    country_rule_set: "capo_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set.ProtectConfigurationCountryRuleSet"
    """<p>An array of ProtectConfigurationCountryRuleSetInformation containing the rules for the NumberCapability.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: UpdateProtectConfigurationCountryRuleSetResult,
) -> dict:
    out: dict = {}
    out["ProtectConfigurationArn"] = value["protect_configuration_arn"]
    out["ProtectConfigurationId"] = value["protect_configuration_id"]
    out["NumberCapability"] = value["number_capability"]
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set

    out["CountryRuleSet"] = (
        capo_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set.serialize_aws_json_1_0(
            value["country_rule_set"]
        )
    )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> UpdateProtectConfigurationCountryRuleSetResult:
    out: UpdateProtectConfigurationCountryRuleSetResult = {}  # type: ignore[typeddict-item]
    if data.get("ProtectConfigurationArn") is not None:
        out["protect_configuration_arn"] = data["ProtectConfigurationArn"]
    else:
        out["protect_configuration_arn"] = ""
    if data.get("ProtectConfigurationId") is not None:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    else:
        out["protect_configuration_id"] = ""
    if data.get("NumberCapability") is not None:
        out["number_capability"] = data["NumberCapability"]
    else:
        out["number_capability"] = ""
    if data.get("CountryRuleSet") is not None:
        import capo_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set

        out["country_rule_set"] = (
            capo_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set.deserialize_aws_json_1_0(
                data["CountryRuleSet"]
            )
        )
    else:
        out["country_rule_set"] = {}
    return out
