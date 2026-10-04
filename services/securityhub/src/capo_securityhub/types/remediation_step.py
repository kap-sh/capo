"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class RemediationStep(TypedDict, closed=True):
    phase: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The phase of the remediation plan that this step belongs to (for example, <code>FIX</code>).</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A description of what the step does.</p>"""
    service: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Which service this step is performed in.</p>"""
    action: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The action to be taken for this step.</p>"""
    logic: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The logic behind the existence of this step.</p>"""
    inverse: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The inverse of the step, to be used if the step needs to be rolled back.</p>"""
    verify_after: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The action to take after the step to verify its success.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationStep) -> dict:
    out: dict = {}
    if "phase" in value:
        out["Phase"] = value["phase"]
    if "description" in value:
        out["Description"] = value["description"]
    if "service" in value:
        out["Service"] = value["service"]
    if "action" in value:
        out["Action"] = value["action"]
    if "logic" in value:
        out["Logic"] = value["logic"]
    if "inverse" in value:
        out["Inverse"] = value["inverse"]
    if "verify_after" in value:
        out["VerifyAfter"] = value["verify_after"]
    return out


def deserialize_json(data: dict) -> RemediationStep:
    out: RemediationStep = {}  # type: ignore[typeddict-item]
    if data.get("Phase") is not None:
        out["phase"] = data["Phase"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Service") is not None:
        out["service"] = data["Service"]
    if data.get("Action") is not None:
        out["action"] = data["Action"]
    if data.get("Logic") is not None:
        out["logic"] = data["Logic"]
    if data.get("Inverse") is not None:
        out["inverse"] = data["Inverse"]
    if data.get("VerifyAfter") is not None:
        out["verify_after"] = data["VerifyAfter"]
    return out
