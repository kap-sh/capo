"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AssociatedPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.policy_arn


class AssociatedPolicy(TypedDict, closed=True):
    policy_arn: "capo_network_security_manager.types.policy_arn.PolicyArn"
    """<p>The ARN of the associated policy, including its version qualifier when a specific published version is pinned (for example, <code>...:policy:abc123:3</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedPolicy) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    return out


def deserialize_json(data: dict) -> AssociatedPolicy:
    out: AssociatedPolicy = {}  # type: ignore[typeddict-item]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError("AssociatedPolicy.policy_arn required")
    return out
