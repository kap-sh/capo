"""Generated from Smithy shape ``com.amazonaws.ssm#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.deletion_mode
    import capo_ssm.types.policy_hash
    import capo_ssm.types.policy_id
    import capo_ssm.types.resource_arn_string


class DeleteResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_ssm.types.resource_arn_string.ResourceArnString"
    """<p>Amazon Resource Name (ARN) of the resource to which the policies are attached.</p>"""
    policy_id: "capo_ssm.types.policy_id.PolicyId"
    """<p>The policy ID.</p>"""
    policy_hash: "capo_ssm.types.policy_hash.PolicyHash"
    """<p>ID of the current policy version. The hash helps to prevent multiple calls from attempting to overwrite a policy.</p>"""
    deletion_mode: NotRequired["capo_ssm.types.deletion_mode.DeletionMode"]
    """<p>Specifies the intended outcome of the operation. Applies only to the <code>Document</code> resource type. The operation ignores this parameter for other resource types. Optional. Defaults to <code>RemoveSharing</code>.</p> <ul> <li> <p> <code>RemoveSharing</code> – Deletes the resource policy and removes sharing of the document.</p> </li> <li> <p> <code>RollbackMigration</code> – Reverts the document to Custom sharing, preserving existing consumer access, instead of removing the policy.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["PolicyId"] = value["policy_id"]
    out["PolicyHash"] = value["policy_hash"]
    if "deletion_mode" in value:
        import capo_ssm.types.deletion_mode

        out["DeletionMode"] = capo_ssm.types.deletion_mode.serialize_aws_json_1_1(
            value["deletion_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("DeleteResourcePolicyRequest.resource_arn required")
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    else:
        raise DeserializationError("DeleteResourcePolicyRequest.policy_id required")
    if data.get("PolicyHash") is not None:
        out["policy_hash"] = data["PolicyHash"]
    else:
        raise DeserializationError("DeleteResourcePolicyRequest.policy_hash required")
    if data.get("DeletionMode") is not None:
        import capo_ssm.types.deletion_mode

        out["deletion_mode"] = capo_ssm.types.deletion_mode.deserialize_aws_json_1_1(
            data["DeletionMode"]
        )
    return out
