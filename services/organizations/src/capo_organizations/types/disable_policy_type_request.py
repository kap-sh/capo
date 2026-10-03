"""Generated from Smithy shape ``com.amazonaws.organizations#DisablePolicyTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.policy_type
    import capo_organizations.types.root_id


class DisablePolicyTypeRequest(TypedDict, closed=True):
    root_id: "capo_organizations.types.root_id.RootId"
    """<p>ID for the root in which you want to disable a policy type. You can get the ID from the <a>ListRoots</a> operation.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for a root ID string requires "r-" followed by from 4 to 32 lowercase letters or digits.</p>"""
    policy_type: "capo_organizations.types.policy_type.PolicyType"
    """<p>The policy type that you want to disable in this root. You can specify one of the following values:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html">SERVICE_CONTROL_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html">RESOURCE_CONTROL_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html">DECLARATIVE_POLICY_EC2</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html">BACKUP_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html">TAG_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_chatbot.html">CHATBOT_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html">AISERVICES_OPT_OUT_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_security_hub.html">SECURITYHUB_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_upgrade_rollout.html">UPGRADE_ROLLOUT_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inspector.html">INSPECTOR_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_bedrock.html">BEDROCK_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_s3.html">S3_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_network_security_director.html">NETWORK_SECURITY_DIRECTOR_POLICY</a> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisablePolicyTypeRequest) -> dict:
    out: dict = {}
    out["RootId"] = value["root_id"]
    import capo_organizations.types.policy_type

    out["PolicyType"] = capo_organizations.types.policy_type.serialize_aws_json_1_1(
        value["policy_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisablePolicyTypeRequest:
    out: DisablePolicyTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("RootId") is not None:
        out["root_id"] = data["RootId"]
    else:
        raise DeserializationError("DisablePolicyTypeRequest.root_id required")
    if data.get("PolicyType") is not None:
        import capo_organizations.types.policy_type

        out["policy_type"] = (
            capo_organizations.types.policy_type.deserialize_aws_json_1_1(
                data["PolicyType"]
            )
        )
    else:
        raise DeserializationError("DisablePolicyTypeRequest.policy_type required")
    return out
