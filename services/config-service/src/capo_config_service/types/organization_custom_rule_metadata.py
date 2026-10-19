"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationCustomRuleMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.maximum_execution_frequency
    import capo_config_service.types.organization_config_rule_trigger_types
    import capo_config_service.types.resource_types_scope
    import capo_config_service.types.string_with_char_limit128
    import capo_config_service.types.string_with_char_limit256
    import capo_config_service.types.string_with_char_limit256_min0
    import capo_config_service.types.string_with_char_limit768
    import capo_config_service.types.string_with_char_limit1024


class OrganizationCustomRuleMetadata(TypedDict, closed=True):
    description: NotRequired[
        "capo_config_service.types.string_with_char_limit256_min0.StringWithCharLimit256Min0"
    ]
    """<p>The description that you provide for your organization Config rule.</p>"""
    lambda_function_arn: (
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    )
    """<p>The lambda function ARN.</p>"""
    organization_config_rule_trigger_types: "capo_config_service.types.organization_config_rule_trigger_types.OrganizationConfigRuleTriggerTypes"
    """<p>The type of notification that triggers Config to run an evaluation for a rule. You can specify the following notification types:</p> <ul> <li> <p> <code>ConfigurationItemChangeNotification</code> - Triggers an evaluation when Config delivers a configuration item as a result of a resource change.</p> </li> <li> <p> <code>OversizedConfigurationItemChangeNotification</code> - Triggers an evaluation when Config delivers an oversized configuration item. Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.</p> </li> <li> <p> <code>ScheduledNotification</code> - Triggers a periodic evaluation at the frequency specified for <code>MaximumExecutionFrequency</code>.</p> </li> </ul>"""
    input_parameters: NotRequired[
        "capo_config_service.types.string_with_char_limit1024.StringWithCharLimit1024"
    ]
    """<p>A string, in JSON format, that is passed to your organization Config rule Lambda function.</p>"""
    maximum_execution_frequency: NotRequired[
        "capo_config_service.types.maximum_execution_frequency.MaximumExecutionFrequency"
    ]
    """<p>The maximum frequency with which Config runs evaluations for a rule. Your custom rule is triggered when Config delivers the configuration snapshot. For more information, see <a>ConfigSnapshotDeliveryProperties</a>.</p> <note> <p>By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the <code>MaximumExecutionFrequency</code> parameter.</p> </note>"""
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
    """<p>One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values. </p>"""
    tag_value_scope: NotRequired[
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationCustomRuleMetadata) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    out["LambdaFunctionArn"] = value["lambda_function_arn"]
    import capo_config_service.types.organization_config_rule_trigger_types

    out["OrganizationConfigRuleTriggerTypes"] = (
        capo_config_service.types.organization_config_rule_trigger_types.serialize_aws_json_1_1(
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
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationCustomRuleMetadata:
    out: OrganizationCustomRuleMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LambdaFunctionArn") is not None:
        out["lambda_function_arn"] = data["LambdaFunctionArn"]
    else:
        out["lambda_function_arn"] = ""
    if data.get("OrganizationConfigRuleTriggerTypes") is not None:
        import capo_config_service.types.organization_config_rule_trigger_types

        out["organization_config_rule_trigger_types"] = (
            capo_config_service.types.organization_config_rule_trigger_types.deserialize_aws_json_1_1(
                data["OrganizationConfigRuleTriggerTypes"]
            )
        )
    else:
        out["organization_config_rule_trigger_types"] = []
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
    return out
