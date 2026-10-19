"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#PutResourcePolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.resource_arn
    import capo_payment_cryptography.types.resource_policy


class PutResourcePolicyInput(TypedDict, closed=True):
    resource_arn: "capo_payment_cryptography.types.resource_arn.ResourceArn"
    """<p>The <code>KeyARN</code> of the key to attach the resource-based policy to.</p>"""
    policy: "capo_payment_cryptography.types.resource_policy.ResourcePolicy"
    """<p>The resource-based policy to attach to the key, in JSON format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutResourcePolicyInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutResourcePolicyInput:
    out: PutResourcePolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        out["policy"] = ""
    return out
