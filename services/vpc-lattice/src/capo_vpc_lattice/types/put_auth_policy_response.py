"""Generated from Smithy shape ``com.amazonaws.vpclattice#PutAuthPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.auth_policy_state
    import capo_vpc_lattice.types.auth_policy_string


class PutAuthPolicyResponse(TypedDict, closed=True):
    policy: NotRequired["capo_vpc_lattice.types.auth_policy_string.AuthPolicyString"]
    """<p>The auth policy. The policy string in JSON must not contain newlines or blank lines.</p>"""
    state: NotRequired["capo_vpc_lattice.types.auth_policy_state.AuthPolicyState"]
    """<p>The state of the auth policy. The auth policy is only active when the auth type is set to <code>AWS_IAM</code>. If you provide a policy, then authentication and authorization decisions are made based on this policy and the client's IAM policy. If the Auth type is <code>NONE</code>, then, any auth policy that you provide remains inactive. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html#create-service-network">Create a service network</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAuthPolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        out["policy"] = value["policy"]
    if "state" in value:
        out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> PutAuthPolicyResponse:
    out: PutAuthPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    if data.get("state") is not None:
        out["state"] = data["state"]
    return out
