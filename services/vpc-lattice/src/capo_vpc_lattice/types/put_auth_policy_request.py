"""Generated from Smithy shape ``com.amazonaws.vpclattice#PutAuthPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.auth_policy_string
    import capo_vpc_lattice.types.resource_identifier


class PutAuthPolicyRequest(TypedDict, closed=True):
    resource_identifier: "capo_vpc_lattice.types.resource_identifier.ResourceIdentifier"
    """<p>The ID or ARN of the service network or service for which the policy is created.</p>"""
    policy: "capo_vpc_lattice.types.auth_policy_string.AuthPolicyString"
    """<p>The auth policy. The policy string in JSON must not contain newlines or blank lines.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAuthPolicyRequest) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutAuthPolicyRequest:
    out: PutAuthPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    return out
