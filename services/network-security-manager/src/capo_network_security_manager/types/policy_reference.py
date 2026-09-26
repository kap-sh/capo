"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#PolicyReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.policy_identifier


class PolicyReference(TypedDict, closed=True):
    policy_identifier: (
        "capo_network_security_manager.types.policy_identifier.PolicyIdentifier"
    )
    """<p>The identifier of the policy. This is the policy's Amazon Resource Name (ARN), optionally version-qualified to pin a specific published version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyReference) -> dict:
    out: dict = {}
    out["policyIdentifier"] = value["policy_identifier"]
    return out


def deserialize_json(data: dict) -> PolicyReference:
    out: PolicyReference = {}  # type: ignore[typeddict-item]
    if data.get("policyIdentifier") is not None:
        out["policy_identifier"] = data["policyIdentifier"]
    else:
        raise DeserializationError("PolicyReference.policy_identifier required")
    return out
