"""Generated from Smithy shape ``com.amazonaws.ssm#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.policy
    import capo_ssm.types.policy_hash
    import capo_ssm.types.policy_id
    import capo_ssm.types.resource_arn_string


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_ssm.types.resource_arn_string.ResourceArnString"
    """<p>Amazon Resource Name (ARN) of the resource to which you want to attach a policy.</p>"""
    policy: "capo_ssm.types.policy.Policy"
    """<p>A policy you want to associate with a resource.</p>"""
    policy_id: NotRequired["capo_ssm.types.policy_id.PolicyId"]
    """<p>The policy ID.</p>"""
    policy_hash: NotRequired["capo_ssm.types.policy_hash.PolicyHash"]
    """<p>ID of the current policy version. The hash helps to prevent a situation where multiple users attempt to overwrite a policy. You must provide this hash when updating or deleting a policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["Policy"] = value["policy"]
    if "policy_id" in value:
        out["PolicyId"] = value["policy_id"]
    if "policy_hash" in value:
        out["PolicyHash"] = value["policy_hash"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        out["policy"] = ""
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    if data.get("PolicyHash") is not None:
        out["policy_hash"] = data["PolicyHash"]
    return out
