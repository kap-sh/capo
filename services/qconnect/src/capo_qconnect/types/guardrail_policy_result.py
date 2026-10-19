"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_action
    import capo_qconnect.types.guardrail_policy_type
    import capo_qconnect.types.non_empty_string


class GuardrailPolicyResult(TypedDict, closed=True):
    policy_type: "capo_qconnect.types.guardrail_policy_type.GuardrailPolicyType"
    """<p>The type of guardrail policy that was evaluated.</p>"""
    action: "capo_qconnect.types.guardrail_action.GuardrailAction"
    """<p>Outcome of this specific policy.</p>"""
    details: NotRequired["capo_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>Policy-specific detail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailPolicyResult) -> dict:
    out: dict = {}
    out["policyType"] = value["policy_type"]
    out["action"] = value["action"]
    if "details" in value:
        out["details"] = value["details"]
    return out


def deserialize_json(data: dict) -> GuardrailPolicyResult:
    out: GuardrailPolicyResult = {}  # type: ignore[typeddict-item]
    if data.get("policyType") is not None:
        out["policy_type"] = data["policyType"]
    else:
        out["policy_type"] = ""
    if data.get("action") is not None:
        out["action"] = data["action"]
    else:
        out["action"] = ""
    if data.get("details") is not None:
        out["details"] = data["details"]
    return out
