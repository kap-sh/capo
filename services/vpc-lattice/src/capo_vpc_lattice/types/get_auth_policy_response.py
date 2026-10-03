"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetAuthPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.auth_policy_state
    import capo_vpc_lattice.types.auth_policy_string
    import capo_vpc_lattice.types.timestamp


class GetAuthPolicyResponse(TypedDict, closed=True):
    policy: NotRequired["capo_vpc_lattice.types.auth_policy_string.AuthPolicyString"]
    """<p>The auth policy.</p>"""
    state: NotRequired["capo_vpc_lattice.types.auth_policy_state.AuthPolicyState"]
    """<p>The state of the auth policy. The auth policy is only active when the auth type is set to <code>AWS_IAM</code>. If you provide a policy, then authentication and authorization decisions are made based on this policy and the client's IAM policy. If the auth type is <code>NONE</code>, then any auth policy that you provide remains inactive. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html#create-service-network">Create a service network</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>"""
    created_at: NotRequired["capo_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the auth policy was created, in ISO-8601 format.</p>"""
    last_updated_at: NotRequired["capo_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the auth policy was last updated, in ISO-8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAuthPolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        out["policy"] = value["policy"]
    if "state" in value:
        out["state"] = value["state"]
    if "created_at" in value:
        import capo_vpc_lattice.types.timestamp

        out["createdAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_vpc_lattice.types.timestamp

        out["lastUpdatedAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetAuthPolicyResponse:
    out: GetAuthPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    if data.get("state") is not None:
        out["state"] = data["state"]
    if data.get("createdAt") is not None:
        import capo_vpc_lattice.types.timestamp

        out["created_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("lastUpdatedAt") is not None:
        import capo_vpc_lattice.types.timestamp

        out["last_updated_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    return out
