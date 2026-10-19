"""Generated from Smithy shape ``com.amazonaws.configservice#PutOrganizationConfigRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.excluded_accounts
    import capo_config_service.types.organization_config_rule_name
    import capo_config_service.types.organization_custom_policy_rule_metadata
    import capo_config_service.types.organization_custom_rule_metadata
    import capo_config_service.types.organization_managed_rule_metadata
    import capo_config_service.types.tags_list


class PutOrganizationConfigRuleRequest(TypedDict, closed=True):
    organization_config_rule_name: "capo_config_service.types.organization_config_rule_name.OrganizationConfigRuleName"
    """<p>The name that you assign to an organization Config rule.</p>"""
    organization_managed_rule_metadata: NotRequired[
        "capo_config_service.types.organization_managed_rule_metadata.OrganizationManagedRuleMetadata"
    ]
    """<p>An <code>OrganizationManagedRuleMetadata</code> object. This object specifies organization managed rule metadata such as resource type and ID of Amazon Web Services resource along with the rule identifier. It also provides the frequency with which you want Config to run evaluations for the rule if the trigger type is periodic.</p>"""
    organization_custom_rule_metadata: NotRequired[
        "capo_config_service.types.organization_custom_rule_metadata.OrganizationCustomRuleMetadata"
    ]
    """<p>An <code>OrganizationCustomRuleMetadata</code> object. This object specifies organization custom rule metadata such as resource type, resource ID of Amazon Web Services resource, Lambda function ARN, and organization trigger types that trigger Config to evaluate your Amazon Web Services resources against a rule. It also provides the frequency with which you want Config to run evaluations for the rule if the trigger type is periodic.</p>"""
    excluded_accounts: NotRequired[
        "capo_config_service.types.excluded_accounts.ExcludedAccounts"
    ]
    """<p>A comma-separated list of accounts that you want to exclude from an organization Config rule.</p>"""
    organization_custom_policy_rule_metadata: NotRequired[
        "capo_config_service.types.organization_custom_policy_rule_metadata.OrganizationCustomPolicyRuleMetadata"
    ]
    """<p>An <code>OrganizationCustomPolicyRuleMetadata</code> object. This object specifies metadata for your organization's Config Custom Policy rule. The metadata includes the runtime system in use, which accounts have debug logging enabled, and other custom rule metadata, such as resource type, resource ID of Amazon Web Services resource, and organization trigger types that initiate Config to evaluate Amazon Web Services resources against a rule.</p>"""
    tags: NotRequired["capo_config_service.types.tags_list.TagsList"]
    """<p>The tags for the organization Config rule. Each tag consists of a key and an optional value, both of which you define.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutOrganizationConfigRuleRequest) -> dict:
    out: dict = {}
    out["OrganizationConfigRuleName"] = value["organization_config_rule_name"]
    if "organization_managed_rule_metadata" in value:
        import capo_config_service.types.organization_managed_rule_metadata

        out["OrganizationManagedRuleMetadata"] = (
            capo_config_service.types.organization_managed_rule_metadata.serialize_aws_json_1_1(
                value["organization_managed_rule_metadata"]
            )
        )
    if "organization_custom_rule_metadata" in value:
        import capo_config_service.types.organization_custom_rule_metadata

        out["OrganizationCustomRuleMetadata"] = (
            capo_config_service.types.organization_custom_rule_metadata.serialize_aws_json_1_1(
                value["organization_custom_rule_metadata"]
            )
        )
    if "excluded_accounts" in value:
        import capo_config_service.types.excluded_accounts

        out["ExcludedAccounts"] = (
            capo_config_service.types.excluded_accounts.serialize_aws_json_1_1(
                value["excluded_accounts"]
            )
        )
    if "organization_custom_policy_rule_metadata" in value:
        import capo_config_service.types.organization_custom_policy_rule_metadata

        out["OrganizationCustomPolicyRuleMetadata"] = (
            capo_config_service.types.organization_custom_policy_rule_metadata.serialize_aws_json_1_1(
                value["organization_custom_policy_rule_metadata"]
            )
        )
    if "tags" in value:
        import capo_config_service.types.tags_list

        out["Tags"] = capo_config_service.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutOrganizationConfigRuleRequest:
    out: PutOrganizationConfigRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationConfigRuleName") is not None:
        out["organization_config_rule_name"] = data["OrganizationConfigRuleName"]
    else:
        out["organization_config_rule_name"] = ""
    if data.get("OrganizationManagedRuleMetadata") is not None:
        import capo_config_service.types.organization_managed_rule_metadata

        out["organization_managed_rule_metadata"] = (
            capo_config_service.types.organization_managed_rule_metadata.deserialize_aws_json_1_1(
                data["OrganizationManagedRuleMetadata"]
            )
        )
    if data.get("OrganizationCustomRuleMetadata") is not None:
        import capo_config_service.types.organization_custom_rule_metadata

        out["organization_custom_rule_metadata"] = (
            capo_config_service.types.organization_custom_rule_metadata.deserialize_aws_json_1_1(
                data["OrganizationCustomRuleMetadata"]
            )
        )
    if data.get("ExcludedAccounts") is not None:
        import capo_config_service.types.excluded_accounts

        out["excluded_accounts"] = (
            capo_config_service.types.excluded_accounts.deserialize_aws_json_1_1(
                data["ExcludedAccounts"]
            )
        )
    if data.get("OrganizationCustomPolicyRuleMetadata") is not None:
        import capo_config_service.types.organization_custom_policy_rule_metadata

        out["organization_custom_policy_rule_metadata"] = (
            capo_config_service.types.organization_custom_policy_rule_metadata.deserialize_aws_json_1_1(
                data["OrganizationCustomPolicyRuleMetadata"]
            )
        )
    if data.get("Tags") is not None:
        import capo_config_service.types.tags_list

        out["tags"] = capo_config_service.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
