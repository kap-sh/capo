"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.cloud_hsm_arn
    import capo_cloudhsm_v2.types.resource_policy


class PutResourcePolicyResponse(TypedDict, closed=True):
    resource_arn: NotRequired["capo_cloudhsm_v2.types.cloud_hsm_arn.CloudHsmArn"]
    """<p>Amazon Resource Name (ARN) of the resource to which a policy is attached.</p>"""
    policy: NotRequired["capo_cloudhsm_v2.types.resource_policy.ResourcePolicy"]
    """<p>The policy attached to a resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_cbor(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    return out
