"""Generated from Smithy shape ``com.amazonaws.organizations#DescribeEffectivePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.effective_policy_type
    import capo_organizations.types.policy_target_id


class DescribeEffectivePolicyRequest(TypedDict, closed=True):
    policy_type: "capo_organizations.types.effective_policy_type.EffectivePolicyType"
    """<p>The type of policy that you want information about. You can specify one of the following values:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html">DECLARATIVE_POLICY_EC2</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html">BACKUP_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html">TAG_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_chatbot.html">CHATBOT_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html">AISERVICES_OPT_OUT_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_security_hub.html">SECURITYHUB_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_upgrade_rollout.html">UPGRADE_ROLLOUT_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inspector.html">INSPECTOR_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_bedrock.html">BEDROCK_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_s3.html">S3_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_network_security_director.html">NETWORK_SECURITY_DIRECTOR_POLICY</a> </p> </li> </ul>"""
    target_id: NotRequired["capo_organizations.types.policy_target_id.PolicyTargetId"]
    """<p>When you're signed in as the management account, specify the ID of the account that you want details about. Specifying an organization root or organizational unit (OU) as the target is not supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEffectivePolicyRequest) -> dict:
    out: dict = {}
    import capo_organizations.types.effective_policy_type

    out["PolicyType"] = (
        capo_organizations.types.effective_policy_type.serialize_aws_json_1_1(
            value["policy_type"]
        )
    )
    if "target_id" in value:
        out["TargetId"] = value["target_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEffectivePolicyRequest:
    out: DescribeEffectivePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("PolicyType") is not None:
        import capo_organizations.types.effective_policy_type

        out["policy_type"] = (
            capo_organizations.types.effective_policy_type.deserialize_aws_json_1_1(
                data["PolicyType"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeEffectivePolicyRequest.policy_type required"
        )
    if data.get("TargetId") is not None:
        out["target_id"] = data["TargetId"]
    return out
