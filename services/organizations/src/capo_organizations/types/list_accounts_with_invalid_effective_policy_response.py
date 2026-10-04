"""Generated from Smithy shape ``com.amazonaws.organizations#ListAccountsWithInvalidEffectivePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.accounts
    import capo_organizations.types.effective_policy_type
    import capo_organizations.types.next_token


class ListAccountsWithInvalidEffectivePolicyResponse(TypedDict, closed=True):
    accounts: NotRequired["capo_organizations.types.accounts.Accounts"]
    """<p>The accounts in the organization which have an invalid effective policy for the specified policy type.</p>"""
    policy_type: NotRequired[
        "capo_organizations.types.effective_policy_type.EffectivePolicyType"
    ]
    """<p>The specified policy type. One of the following values:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html">DECLARATIVE_POLICY_EC2</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html">BACKUP_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html">TAG_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_chatbot.html">CHATBOT_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html">AISERVICES_OPT_OUT_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_security_hub.html">SECURITYHUB_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_upgrade_rollout.html">UPGRADE_ROLLOUT_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inspector.html">INSPECTOR_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_bedrock.html">BEDROCK_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_s3.html">S3_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_network_security_director.html">NETWORK_SECURITY_DIRECTOR_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_guardduty.html">GUARDDUTY_POLICY</a> </p> </li> </ul>"""
    next_token: NotRequired["capo_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListAccountsWithInvalidEffectivePolicyResponse,
) -> dict:
    out: dict = {}
    if "accounts" in value:
        import capo_organizations.types.accounts

        out["Accounts"] = capo_organizations.types.accounts.serialize_aws_json_1_1(
            value["accounts"]
        )
    if "policy_type" in value:
        import capo_organizations.types.effective_policy_type

        out["PolicyType"] = (
            capo_organizations.types.effective_policy_type.serialize_aws_json_1_1(
                value["policy_type"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListAccountsWithInvalidEffectivePolicyResponse:
    out: ListAccountsWithInvalidEffectivePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("Accounts") is not None:
        import capo_organizations.types.accounts

        out["accounts"] = capo_organizations.types.accounts.deserialize_aws_json_1_1(
            data["Accounts"]
        )
    if data.get("PolicyType") is not None:
        import capo_organizations.types.effective_policy_type

        out["policy_type"] = (
            capo_organizations.types.effective_policy_type.deserialize_aws_json_1_1(
                data["PolicyType"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
