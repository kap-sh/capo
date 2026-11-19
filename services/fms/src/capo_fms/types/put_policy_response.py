"""Generated from Smithy shape ``com.amazonaws.fms#PutPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.policy
    import capo_fms.types.resource_arn


class PutPolicyResponse(TypedDict, closed=True):
    policy: NotRequired["capo_fms.types.policy.Policy"]
    """<p>The details of the Firewall Manager policy.</p>"""
    policy_arn: NotRequired["capo_fms.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        import capo_fms.types.policy

        out["Policy"] = capo_fms.types.policy.serialize_aws_json_1_1(value["policy"])
    if "policy_arn" in value:
        out["PolicyArn"] = value["policy_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutPolicyResponse:
    out: PutPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        import capo_fms.types.policy

        out["policy"] = capo_fms.types.policy.deserialize_aws_json_1_1(data["Policy"])
    if data.get("PolicyArn") is not None:
        out["policy_arn"] = data["PolicyArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutPolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        import capo_fms.types.policy

        out["Policy"] = capo_fms.types.policy.serialize_cbor(value["policy"])
    if "policy_arn" in value:
        out["PolicyArn"] = value["policy_arn"]
    return out


def deserialize_cbor(data: dict) -> PutPolicyResponse:
    out: PutPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        import capo_fms.types.policy

        out["policy"] = capo_fms.types.policy.deserialize_cbor(data["Policy"])
    if data.get("PolicyArn") is not None:
        out["policy_arn"] = data["PolicyArn"]
    return out
