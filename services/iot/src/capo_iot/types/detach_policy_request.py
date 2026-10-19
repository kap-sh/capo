"""Generated from Smithy shape ``com.amazonaws.iot#DetachPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.policy_name
    import capo_iot.types.policy_target


class DetachPolicyRequest(TypedDict, closed=True):
    policy_name: "capo_iot.types.policy_name.PolicyName"
    """<p>The policy to detach.</p>"""
    target: "capo_iot.types.policy_target.PolicyTarget"
    """<p>The target from which the policy will be detached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetachPolicyRequest) -> dict:
    out: dict = {}
    out["target"] = value["target"]
    return out


def deserialize_json(data: dict) -> DetachPolicyRequest:
    out: DetachPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("target") is not None:
        out["target"] = data["target"]
    else:
        out["target"] = ""
    return out
