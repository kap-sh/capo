"""Generated from Smithy shape ``com.amazonaws.ssmincidents#DeleteResourcePolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.policy_id


class DeleteResourcePolicyInput(TypedDict, closed=True):
    resource_arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource you're deleting the policy from.</p>"""
    policy_id: "capo_ssm_incidents.types.policy_id.PolicyId"
    """<p>The ID of the resource policy you're deleting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePolicyInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["policyId"] = value["policy_id"]
    return out


def deserialize_json(data: dict) -> DeleteResourcePolicyInput:
    out: DeleteResourcePolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("policyId") is not None:
        out["policy_id"] = data["policyId"]
    else:
        out["policy_id"] = ""
    return out
