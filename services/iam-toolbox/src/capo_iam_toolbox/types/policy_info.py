"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#PolicyInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iam_toolbox.types.attached_to_list
    import capo_iam_toolbox.types.policy_type


class PolicyInfo(TypedDict, closed=True):
    type: NotRequired["capo_iam_toolbox.types.policy_type.PolicyType"]
    """<p>The type of policy. Valid values:</p> <ul> <li> <p> <code>IDENTITY_BASED_POLICY</code> - An identity-based policy attached to an IAM user, group, or role.</p> </li> <li> <p> <code>PERMISSIONS_BOUNDARY</code> - A permissions boundary for an IAM entity.</p> </li> <li> <p> <code>RESOURCE_BASED_POLICY</code> - A resource-based policy attached to a resource.</p> </li> <li> <p> <code>RESOURCE_CONTROL_POLICY</code> - A resource control policy (RCP) in AWS Organizations.</p> </li> <li> <p> <code>SERVICE_CONTROL_POLICY</code> - A service control policy (SCP) in AWS Organizations.</p> </li> <li> <p> <code>SESSION_POLICY</code> - A session policy passed during role assumption or federation.</p> </li> <li> <p> <code>VPC_ENDPOINT_POLICY</code> - A VPC endpoint policy.</p> </li> </ul>"""
    inline: NotRequired["bool"]
    """<p>Specifies whether this is an inline policy (<code>true</code>) or a managed policy (<code>false</code>).</p>"""
    uri: NotRequired["str"]
    """<p>A URI that identifies the policy. Use this URI to cross-reference the policy with the matching policies in each evaluation. The value depends on the policy type:</p> <ul> <li> <p>For managed policies, this is the policy ARN.</p> </li> <li> <p>For inline policies, which have no ARN, this is an opaque identifier.</p> </li> </ul>"""
    attached_to: NotRequired["capo_iam_toolbox.types.attached_to_list.AttachedToList"]
    """<p>The entities that the policy is attached to. For identity, session, and resource-based policies, this is typically a single entity. For organization control policies (SCPs and RCPs), it can be multiple entities at different levels of the organization hierarchy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyInfo) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_iam_toolbox.types.policy_type

        out["type"] = capo_iam_toolbox.types.policy_type.serialize_json(value["type"])
    if "inline" in value:
        out["inline"] = value["inline"]
    if "uri" in value:
        out["uri"] = value["uri"]
    if "attached_to" in value:
        import capo_iam_toolbox.types.attached_to_list

        out["attachedTo"] = capo_iam_toolbox.types.attached_to_list.serialize_json(
            value["attached_to"]
        )
    return out


def deserialize_json(data: dict) -> PolicyInfo:
    out: PolicyInfo = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_iam_toolbox.types.policy_type

        out["type"] = capo_iam_toolbox.types.policy_type.deserialize_json(data["type"])
    if data.get("inline") is not None:
        out["inline"] = data["inline"]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    if data.get("attachedTo") is not None:
        import capo_iam_toolbox.types.attached_to_list

        out["attached_to"] = capo_iam_toolbox.types.attached_to_list.deserialize_json(
            data["attachedTo"]
        )
    return out
