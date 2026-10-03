"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationManagedRuleMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.maximum_execution_frequency
    import capo_config_service.types.resource_types_scope
    import capo_config_service.types.string_with_char_limit128
    import capo_config_service.types.string_with_char_limit256
    import capo_config_service.types.string_with_char_limit256_min0
    import capo_config_service.types.string_with_char_limit768
    import capo_config_service.types.string_with_char_limit1024


class OrganizationManagedRuleMetadata(TypedDict, closed=True):
    description: NotRequired[
        "capo_config_service.types.string_with_char_limit256_min0.StringWithCharLimit256Min0"
    ]
    """<p>The description that you provide for your organization Config rule.</p>"""
    rule_identifier: (
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    )
    """<p>For organization config managed rules, a predefined identifier from a list. For example, <code>IAM_PASSWORD_POLICY</code> is a managed rule. To reference a managed rule, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html">Using Config managed rules</a>.</p>"""
    input_parameters: NotRequired[
        "capo_config_service.types.string_with_char_limit1024.StringWithCharLimit1024"
    ]
    """<p>A string, in JSON format, that is passed to your organization Config rule Lambda function.</p>"""
    maximum_execution_frequency: NotRequired[
        "capo_config_service.types.maximum_execution_frequency.MaximumExecutionFrequency"
    ]
    """<p>The maximum frequency with which Config runs evaluations for a rule. This is for an Config managed rule that is triggered at a periodic frequency.</p> <note> <p>By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the <code>MaximumExecutionFrequency</code> parameter.</p> </note>"""
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
    """<p>The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationManagedRuleMetadata) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    out["RuleIdentifier"] = value["rule_identifier"]
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


def deserialize_aws_json_1_1(data: dict) -> OrganizationManagedRuleMetadata:
    out: OrganizationManagedRuleMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RuleIdentifier") is not None:
        out["rule_identifier"] = data["RuleIdentifier"]
    else:
        raise DeserializationError(
            "OrganizationManagedRuleMetadata.rule_identifier required"
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
    return out
