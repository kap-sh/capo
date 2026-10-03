"""Generated from Smithy shape ``com.amazonaws.organizations#Organization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.account_arn
    import capo_organizations.types.account_id
    import capo_organizations.types.email
    import capo_organizations.types.organization_arn
    import capo_organizations.types.organization_feature_set
    import capo_organizations.types.organization_id
    import capo_organizations.types.policy_types


class Organization(TypedDict, closed=True):
    id: NotRequired["capo_organizations.types.organization_id.OrganizationId"]
    """<p>The unique identifier (ID) of an organization.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for an organization ID string requires "o-" followed by from 10 to 32 lowercase letters or digits.</p>"""
    arn: NotRequired["capo_organizations.types.organization_arn.OrganizationArn"]
    """<p>The Amazon Resource Name (ARN) of an organization.</p> <p>For more information about ARNs in Organizations, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies">ARN Formats Supported by Organizations</a> in the <i>Amazon Web Services Service Authorization Reference</i>.</p>"""
    feature_set: NotRequired[
        "capo_organizations.types.organization_feature_set.OrganizationFeatureSet"
    ]
    """<p>Specifies the functionality that currently is available to the organization. If set to "ALL", then all features are enabled and policies can be applied to accounts in the organization. If set to "CONSOLIDATED_BILLING", then only consolidated billing functionality is available. For more information, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">Enabling all features in your organization</a> in the <i>Organizations User Guide</i>.</p>"""
    master_account_arn: NotRequired["capo_organizations.types.account_arn.AccountArn"]
    """<p>The Amazon Resource Name (ARN) of the account that is designated as the management account for the organization.</p> <p>For more information about ARNs in Organizations, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies">ARN Formats Supported by Organizations</a> in the <i>Amazon Web Services Service Authorization Reference</i>.</p>"""
    master_account_id: NotRequired["capo_organizations.types.account_id.AccountId"]
    """<p>The unique identifier (ID) of the management account of an organization.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for an account ID string requires exactly 12 digits.</p>"""
    master_account_email: NotRequired["capo_organizations.types.email.Email"]
    """<p>The email address that is associated with the Amazon Web Services account that is designated as the management account for the organization.</p>"""
    available_policy_types: NotRequired[
        "capo_organizations.types.policy_types.PolicyTypes"
    ]
    """<important> <p>Do not use. This field is deprecated and doesn't provide complete information about the policies in your organization.</p> </important> <p>To determine the policies that are enabled and available for use in your organization, use the <a>ListRoots</a> operation instead.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Organization) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "feature_set" in value:
        import capo_organizations.types.organization_feature_set

        out["FeatureSet"] = (
            capo_organizations.types.organization_feature_set.serialize_aws_json_1_1(
                value["feature_set"]
            )
        )
    if "master_account_arn" in value:
        out["MasterAccountArn"] = value["master_account_arn"]
    if "master_account_id" in value:
        out["MasterAccountId"] = value["master_account_id"]
    if "master_account_email" in value:
        out["MasterAccountEmail"] = value["master_account_email"]
    if "available_policy_types" in value:
        import capo_organizations.types.policy_types

        out["AvailablePolicyTypes"] = (
            capo_organizations.types.policy_types.serialize_aws_json_1_1(
                value["available_policy_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Organization:
    out: Organization = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("FeatureSet") is not None:
        import capo_organizations.types.organization_feature_set

        out["feature_set"] = (
            capo_organizations.types.organization_feature_set.deserialize_aws_json_1_1(
                data["FeatureSet"]
            )
        )
    if data.get("MasterAccountArn") is not None:
        out["master_account_arn"] = data["MasterAccountArn"]
    if data.get("MasterAccountId") is not None:
        out["master_account_id"] = data["MasterAccountId"]
    if data.get("MasterAccountEmail") is not None:
        out["master_account_email"] = data["MasterAccountEmail"]
    if data.get("AvailablePolicyTypes") is not None:
        import capo_organizations.types.policy_types

        out["available_policy_types"] = (
            capo_organizations.types.policy_types.deserialize_aws_json_1_1(
                data["AvailablePolicyTypes"]
            )
        )
    return out
