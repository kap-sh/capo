"""Generated from Smithy shape ``com.amazonaws.vpclattice#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.policy_string
    import capo_vpc_lattice.types.resource_arn


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_vpc_lattice.types.resource_arn.ResourceArn"
    """<p>The ID or ARN of the service network or service for which the policy is created.</p>"""
    policy: "capo_vpc_lattice.types.policy_string.PolicyString"
    """<p>An IAM policy. The policy string in JSON must not contain newlines or blank lines.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    return out
