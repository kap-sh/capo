"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#GetPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.policy_identifier


class GetPolicyInput(TypedDict, closed=True):
    policy_identifier: (
        "capo_network_security_manager.types.policy_identifier.PolicyIdentifier"
    )
    """<p>The identifier of the policy. This is the policy's Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPolicyInput:
    out: GetPolicyInput = {}  # type: ignore[typeddict-item]
    return out
