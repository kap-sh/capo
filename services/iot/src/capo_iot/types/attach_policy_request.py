"""Generated from Smithy shape ``com.amazonaws.iot#AttachPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.policy_name
    import capo_iot.types.policy_target


class AttachPolicyRequest(TypedDict, closed=True):
    policy_name: "capo_iot.types.policy_name.PolicyName"
    """<p>The name of the policy to attach.</p>"""
    target: "capo_iot.types.policy_target.PolicyTarget"
    """<p>The <a href="https://docs.aws.amazon.com/iot/latest/developerguide/security-iam.html">identity</a> to which the policy is attached. For example, a thing group or a certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachPolicyRequest) -> dict:
    out: dict = {}
    out["target"] = value["target"]
    return out


def deserialize_json(data: dict) -> AttachPolicyRequest:
    out: AttachPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("target") is not None:
        out["target"] = data["target"]
    else:
        raise DeserializationError("AttachPolicyRequest.target required")
    return out
