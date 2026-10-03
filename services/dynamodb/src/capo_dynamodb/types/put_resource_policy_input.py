"""Generated from Smithy shape ``com.amazonaws.dynamodb#PutResourcePolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.confirm_remove_self_resource_access
    import capo_dynamodb.types.policy_revision_id
    import capo_dynamodb.types.resource_arn_string
    import capo_dynamodb.types.resource_policy


class PutResourcePolicyInput(TypedDict, closed=True):
    resource_arn: "capo_dynamodb.types.resource_arn_string.ResourceArnString"
    """<p>The Amazon Resource Name (ARN) of the DynamoDB resource to which the policy will be attached. The resources you can specify include tables and streams.</p> <p>You can control index permissions using the base table's policy. To specify the same permission level for your table and its indexes, you can provide both the table and index Amazon Resource Name (ARN)s in the <code>Resource</code> field of a given <code>Statement</code> in your policy document. Alternatively, to specify different permissions for your table, indexes, or both, you can define multiple <code>Statement</code> fields in your policy document.</p>"""
    policy: "capo_dynamodb.types.resource_policy.ResourcePolicy"
    """<p>An Amazon Web Services resource-based policy document in JSON format.</p> <ul> <li> <p>The maximum size supported for a resource-based policy document is 20 KB. DynamoDB counts whitespaces when calculating the size of a policy against this limit.</p> </li> <li> <p>Within a resource-based policy, if the action for a DynamoDB service-linked role (SLR) to replicate data for a global table is denied, adding or deleting a replica will fail with an error.</p> </li> </ul> <p>For a full list of all considerations that apply while attaching a resource-based policy, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-considerations.html">Resource-based policy considerations</a>.</p>"""
    expected_revision_id: NotRequired[
        "capo_dynamodb.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>A string value that you can use to conditionally update your policy. You can provide the revision ID of your existing policy to make mutating requests against that policy.</p> <note> <p>When you provide an expected revision ID, if the revision ID of the existing policy on the resource doesn't match or if there's no policy attached to the resource, your request will be rejected with a <code>PolicyNotFoundException</code>.</p> </note> <p>To conditionally attach a policy when no policy exists for the resource, specify <code>NO_POLICY</code> for the revision ID.</p>"""
    confirm_remove_self_resource_access: "capo_dynamodb.types.confirm_remove_self_resource_access.ConfirmRemoveSelfResourceAccess"
    """<p>Set this parameter to <code>true</code> to confirm that you want to remove your permissions to change the policy of this resource in the future.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutResourcePolicyInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["Policy"] = value["policy"]
    if "expected_revision_id" in value:
        out["ExpectedRevisionId"] = value["expected_revision_id"]
    out["ConfirmRemoveSelfResourceAccess"] = value.get(
        "confirm_remove_self_resource_access", False
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PutResourcePolicyInput:
    out: PutResourcePolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("PutResourcePolicyInput.resource_arn required")
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutResourcePolicyInput.policy required")
    if data.get("ExpectedRevisionId") is not None:
        out["expected_revision_id"] = data["ExpectedRevisionId"]
    if data.get("ConfirmRemoveSelfResourceAccess") is not None:
        out["confirm_remove_self_resource_access"] = data[
            "ConfirmRemoveSelfResourceAccess"
        ]
    else:
        out["confirm_remove_self_resource_access"] = False
    return out
