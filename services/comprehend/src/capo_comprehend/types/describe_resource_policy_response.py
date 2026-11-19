"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.policy
    import capo_comprehend.types.policy_revision_id
    import capo_comprehend.types.timestamp


class DescribeResourcePolicyResponse(TypedDict, closed=True):
    resource_policy: NotRequired["capo_comprehend.types.policy.Policy"]
    """<p>The JSON body of the resource-based policy.</p>"""
    creation_time: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>The time at which the policy was created.</p>"""
    last_modified_time: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>The time at which the policy was last modified.</p>"""
    policy_revision_id: NotRequired[
        "capo_comprehend.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>The revision ID of the policy. Each time you modify a policy, Amazon Comprehend assigns a new revision ID, and it deletes the prior version of the policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_policy" in value:
        out["ResourcePolicy"] = value["resource_policy"]
    if "creation_time" in value:
        import capo_comprehend.types.timestamp

        out["CreationTime"] = capo_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_comprehend.types.timestamp

        out["LastModifiedTime"] = (
            capo_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeResourcePolicyResponse:
    out: DescribeResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourcePolicy") is not None:
        out["resource_policy"] = data["ResourcePolicy"]
    if data.get("CreationTime") is not None:
        import capo_comprehend.types.timestamp

        out["creation_time"] = capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_comprehend.types.timestamp

        out["last_modified_time"] = (
            capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("PolicyRevisionId") is not None:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_policy" in value:
        out["ResourcePolicy"] = value["resource_policy"]
    if "creation_time" in value:
        import capo_comprehend.types.timestamp

        out["CreationTime"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_comprehend.types.timestamp

        out["LastModifiedTime"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["last_modified_time"]
        )
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    return out


def deserialize_cbor(data: dict) -> DescribeResourcePolicyResponse:
    out: DescribeResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourcePolicy") is not None:
        out["resource_policy"] = data["ResourcePolicy"]
    if data.get("CreationTime") is not None:
        import capo_comprehend.types.timestamp

        out["creation_time"] = capo_comprehend.types.timestamp.deserialize_cbor(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_comprehend.types.timestamp

        out["last_modified_time"] = capo_comprehend.types.timestamp.deserialize_cbor(
            data["LastModifiedTime"]
        )
    if data.get("PolicyRevisionId") is not None:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    return out
