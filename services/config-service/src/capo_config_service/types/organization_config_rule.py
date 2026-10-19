"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConfigRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.date
    import capo_config_service.types.excluded_accounts
    import capo_config_service.types.organization_config_rule_name
    import capo_config_service.types.organization_custom_policy_rule_metadata_no_policy
    import capo_config_service.types.organization_custom_rule_metadata
    import capo_config_service.types.organization_managed_rule_metadata
    import capo_config_service.types.string_with_char_limit256


class OrganizationConfigRule(TypedDict, closed=True):
    organization_config_rule_name: "capo_config_service.types.organization_config_rule_name.OrganizationConfigRuleName"
    """<p>The name that you assign to organization Config rule.</p>"""
    organization_config_rule_arn: (
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    )
    """<p>Amazon Resource Name (ARN) of organization Config rule.</p>"""
    organization_managed_rule_metadata: NotRequired[
        "capo_config_service.types.organization_managed_rule_metadata.OrganizationManagedRuleMetadata"
    ]
    """<p>An <code>OrganizationManagedRuleMetadata</code> object.</p>"""
    organization_custom_rule_metadata: NotRequired[
        "capo_config_service.types.organization_custom_rule_metadata.OrganizationCustomRuleMetadata"
    ]
    """<p>An <code>OrganizationCustomRuleMetadata</code> object.</p>"""
    excluded_accounts: NotRequired[
        "capo_config_service.types.excluded_accounts.ExcludedAccounts"
    ]
    """<p>A comma-separated list of accounts excluded from organization Config rule.</p>"""
    last_update_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The timestamp of the last update.</p>"""
    organization_custom_policy_rule_metadata: NotRequired[
        "capo_config_service.types.organization_custom_policy_rule_metadata_no_policy.OrganizationCustomPolicyRuleMetadataNoPolicy"
    ]
    """<p>An object that specifies metadata for your organization's Config Custom Policy rule. The metadata includes the runtime system in use, which accounts have debug logging enabled, and other custom rule metadata, such as resource type, resource ID of Amazon Web Services resource, and organization trigger types that initiate Config to evaluate Amazon Web Services resources against a rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConfigRule) -> dict:
    out: dict = {}
    out["OrganizationConfigRuleName"] = value["organization_config_rule_name"]
    out["OrganizationConfigRuleArn"] = value["organization_config_rule_arn"]
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
    if "last_update_time" in value:
        import capo_config_service.types.date

        out["LastUpdateTime"] = capo_config_service.types.date.serialize_aws_json_1_1(
            value["last_update_time"]
        )
    if "organization_custom_policy_rule_metadata" in value:
        import capo_config_service.types.organization_custom_policy_rule_metadata_no_policy

        out["OrganizationCustomPolicyRuleMetadata"] = (
            capo_config_service.types.organization_custom_policy_rule_metadata_no_policy.serialize_aws_json_1_1(
                value["organization_custom_policy_rule_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationConfigRule:
    out: OrganizationConfigRule = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationConfigRuleName") is not None:
        out["organization_config_rule_name"] = data["OrganizationConfigRuleName"]
    else:
        out["organization_config_rule_name"] = ""
    if data.get("OrganizationConfigRuleArn") is not None:
        out["organization_config_rule_arn"] = data["OrganizationConfigRuleArn"]
    else:
        out["organization_config_rule_arn"] = ""
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
    if data.get("LastUpdateTime") is not None:
        import capo_config_service.types.date

        out["last_update_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["LastUpdateTime"]
            )
        )
    if data.get("OrganizationCustomPolicyRuleMetadata") is not None:
        import capo_config_service.types.organization_custom_policy_rule_metadata_no_policy

        out["organization_custom_policy_rule_metadata"] = (
            capo_config_service.types.organization_custom_policy_rule_metadata_no_policy.deserialize_aws_json_1_1(
                data["OrganizationCustomPolicyRuleMetadata"]
            )
        )
    return out
