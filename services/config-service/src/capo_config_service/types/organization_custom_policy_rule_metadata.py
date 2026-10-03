"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationCustomPolicyRuleMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.debug_log_delivery_accounts
    import capo_config_service.types.maximum_execution_frequency
    import capo_config_service.types.organization_config_rule_trigger_type_no_s_ns
    import capo_config_service.types.policy_runtime
    import capo_config_service.types.policy_text
    import capo_config_service.types.resource_types_scope
    import capo_config_service.types.string_with_char_limit128
    import capo_config_service.types.string_with_char_limit256
    import capo_config_service.types.string_with_char_limit256_min0
    import capo_config_service.types.string_with_char_limit768
    import capo_config_service.types.string_with_char_limit1024


class OrganizationCustomPolicyRuleMetadata(TypedDict, closed=True):
    description: NotRequired[
        "capo_config_service.types.string_with_char_limit256_min0.StringWithCharLimit256Min0"
    ]
    """<p>The description that you provide for your organization Config Custom Policy rule.</p>"""
    organization_config_rule_trigger_types: NotRequired[
        "capo_config_service.types.organization_config_rule_trigger_type_no_s_ns.OrganizationConfigRuleTriggerTypeNoSNs"
    ]
    """<p>The type of notification that initiates Config to run an evaluation for a rule. For Config Custom Policy rules, Config supports change-initiated notification types:</p> <ul> <li> <p> <code>ConfigurationItemChangeNotification</code> - Initiates an evaluation when Config delivers a configuration item as a result of a resource change.</p> </li> <li> <p> <code>OversizedConfigurationItemChangeNotification</code> - Initiates an evaluation when Config delivers an oversized configuration item. Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.</p> </li> </ul>"""
    input_parameters: NotRequired[
        "capo_config_service.types.string_with_char_limit1024.StringWithCharLimit1024"
    ]
    """<p>A string, in JSON format, that is passed to your organization Config Custom Policy rule.</p>"""
    maximum_execution_frequency: NotRequired[
        "capo_config_service.types.maximum_execution_frequency.MaximumExecutionFrequency"
    ]
    """<p>The maximum frequency with which Config runs evaluations for a rule. Your Config Custom Policy rule is triggered when Config delivers the configuration snapshot. For more information, see <a>ConfigSnapshotDeliveryProperties</a>.</p>"""
    resource_types_scope: NotRequired[
        "capo_config_service.types.resource_types_scope.ResourceTypesScope"
    ]
    """<p>The type of the Amazon Web Services resource that was evaluated.</p>"""
    resource_id_scope: NotRequired[
        "capo_config_service.types.string_with_char_limit768.StringWithCharLimit768"
    ]
    """<p>The ID of the Amazon Web Services resource that was evaluated.</p>"""
    tag_key_scope: NotRequired[
        "capo_config_service.types.string_with_char_limit128.StringWithCharLimit128"
    ]
    """<p>One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.</p>"""
    tag_value_scope: NotRequired[
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).</p>"""
    policy_runtime: "capo_config_service.types.policy_runtime.PolicyRuntime"
    """<p>The runtime system for your organization Config Custom Policy rules. Guard is a policy-as-code language that allows you to write policies that are enforced by Config Custom Policy rules. For more information about Guard, see the <a href="https://github.com/aws-cloudformation/cloudformation-guard">Guard GitHub Repository</a>.</p>"""
    policy_text: "capo_config_service.types.policy_text.PolicyText"
    """<p>The policy definition containing the logic for your organization Config Custom Policy rule.</p>"""
    debug_log_delivery_accounts: NotRequired[
        "capo_config_service.types.debug_log_delivery_accounts.DebugLogDeliveryAccounts"
    ]
    """<p>A list of accounts that you can enable debug logging for your organization Config Custom Policy rule. List is null when debug logging is enabled for all accounts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationCustomPolicyRuleMetadata) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "organization_config_rule_trigger_types" in value:
        import capo_config_service.types.organization_config_rule_trigger_type_no_s_ns

        out["OrganizationConfigRuleTriggerTypes"] = (
            capo_config_service.types.organization_config_rule_trigger_type_no_s_ns.serialize_aws_json_1_1(
                value["organization_config_rule_trigger_types"]
            )
        )
    if "input_parameters" in value:
        out["InputParameters"] = value["input_parameters"]
    if "maximum_execution_frequency" in value:
        import capo_config_service.types.maximum_execution_frequency

        out["MaximumExecutionFrequency"] = (
            capo_config_service.types.maximum_execution_frequency.serialize_aws_json_1_1(
                value["maximum_execution_frequency"]
            )
        )
    if "resource_types_scope" in value:
        import capo_config_service.types.resource_types_scope

        out["ResourceTypesScope"] = (
            capo_config_service.types.resource_types_scope.serialize_aws_json_1_1(
                value["resource_types_scope"]
            )
        )
    if "resource_id_scope" in value:
        out["ResourceIdScope"] = value["resource_id_scope"]
    if "tag_key_scope" in value:
        out["TagKeyScope"] = value["tag_key_scope"]
    if "tag_value_scope" in value:
        out["TagValueScope"] = value["tag_value_scope"]
    out["PolicyRuntime"] = value["policy_runtime"]
    out["PolicyText"] = value["policy_text"]
    if "debug_log_delivery_accounts" in value:
        import capo_config_service.types.debug_log_delivery_accounts

        out["DebugLogDeliveryAccounts"] = (
            capo_config_service.types.debug_log_delivery_accounts.serialize_aws_json_1_1(
                value["debug_log_delivery_accounts"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationCustomPolicyRuleMetadata:
    out: OrganizationCustomPolicyRuleMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("OrganizationConfigRuleTriggerTypes") is not None:
        import capo_config_service.types.organization_config_rule_trigger_type_no_s_ns

        out["organization_config_rule_trigger_types"] = (
            capo_config_service.types.organization_config_rule_trigger_type_no_s_ns.deserialize_aws_json_1_1(
                data["OrganizationConfigRuleTriggerTypes"]
            )
        )
    if data.get("InputParameters") is not None:
        out["input_parameters"] = data["InputParameters"]
    if data.get("MaximumExecutionFrequency") is not None:
        import capo_config_service.types.maximum_execution_frequency

        out["maximum_execution_frequency"] = (
            capo_config_service.types.maximum_execution_frequency.deserialize_aws_json_1_1(
                data["MaximumExecutionFrequency"]
            )
        )
    if data.get("ResourceTypesScope") is not None:
        import capo_config_service.types.resource_types_scope

        out["resource_types_scope"] = (
            capo_config_service.types.resource_types_scope.deserialize_aws_json_1_1(
                data["ResourceTypesScope"]
            )
        )
    if data.get("ResourceIdScope") is not None:
        out["resource_id_scope"] = data["ResourceIdScope"]
    if data.get("TagKeyScope") is not None:
        out["tag_key_scope"] = data["TagKeyScope"]
    if data.get("TagValueScope") is not None:
        out["tag_value_scope"] = data["TagValueScope"]
    if data.get("PolicyRuntime") is not None:
        out["policy_runtime"] = data["PolicyRuntime"]
    else:
        raise DeserializationError(
            "OrganizationCustomPolicyRuleMetadata.policy_runtime required"
        )
    if data.get("PolicyText") is not None:
        out["policy_text"] = data["PolicyText"]
    else:
        raise DeserializationError(
            "OrganizationCustomPolicyRuleMetadata.policy_text required"
        )
    if data.get("DebugLogDeliveryAccounts") is not None:
        import capo_config_service.types.debug_log_delivery_accounts

        out["debug_log_delivery_accounts"] = (
            capo_config_service.types.debug_log_delivery_accounts.deserialize_aws_json_1_1(
                data["DebugLogDeliveryAccounts"]
            )
        )
    return out
