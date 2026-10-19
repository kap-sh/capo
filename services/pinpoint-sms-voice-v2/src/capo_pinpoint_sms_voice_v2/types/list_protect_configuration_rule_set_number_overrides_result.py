"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ListProtectConfigurationRuleSetNumberOverridesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_arn
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override_list


class ListProtectConfigurationRuleSetNumberOverridesResult(TypedDict, closed=True):
    protect_configuration_arn: "capo_pinpoint_sms_voice_v2.types.protect_configuration_arn.ProtectConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the protect configuration.</p>"""
    protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id.ProtectConfigurationId"
    """<p>The unique identifier for the protect configuration.</p>"""
    rule_set_number_overrides: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override_list.ProtectConfigurationRuleSetNumberOverrideList"
    ]
    """<p>An array of RuleSetNumberOverrides objects.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ListProtectConfigurationRuleSetNumberOverridesResult,
) -> dict:
    out: dict = {}
    out["ProtectConfigurationArn"] = value["protect_configuration_arn"]
    out["ProtectConfigurationId"] = value["protect_configuration_id"]
    if "rule_set_number_overrides" in value:
        import capo_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override_list

        out["RuleSetNumberOverrides"] = (
            capo_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override_list.serialize_aws_json_1_0(
                value["rule_set_number_overrides"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListProtectConfigurationRuleSetNumberOverridesResult:
    out: ListProtectConfigurationRuleSetNumberOverridesResult = {}  # type: ignore[typeddict-item]
    if data.get("ProtectConfigurationArn") is not None:
        out["protect_configuration_arn"] = data["ProtectConfigurationArn"]
    else:
        out["protect_configuration_arn"] = ""
    if data.get("ProtectConfigurationId") is not None:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    else:
        out["protect_configuration_id"] = ""
    if data.get("RuleSetNumberOverrides") is not None:
        import capo_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override_list

        out["rule_set_number_overrides"] = (
            capo_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override_list.deserialize_aws_json_1_0(
                data["RuleSetNumberOverrides"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
