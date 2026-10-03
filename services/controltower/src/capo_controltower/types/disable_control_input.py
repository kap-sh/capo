"""Generated from Smithy shape ``com.amazonaws.controltower#DisableControlInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.arn
    import capo_controltower.types.control_identifier
    import capo_controltower.types.target_identifier


class DisableControlInput(TypedDict, closed=True):
    control_identifier: NotRequired[
        "capo_controltower.types.control_identifier.ControlIdentifier"
    ]
    """<p>The ARN of the control. Only <b>Strongly recommended</b> and <b>Elective</b> controls are permitted, with the exception of the <b>Region deny</b> control. For information on how to find the <code>controlIdentifier</code>, see <a href="https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html">the overview page</a>.</p>"""
    target_identifier: NotRequired[
        "capo_controltower.types.target_identifier.TargetIdentifier"
    ]
    """<p>The ARN of the organizational unit. For information on how to find the <code>targetIdentifier</code>, see <a href="https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html">the overview page</a>.</p>"""
    enabled_control_identifier: NotRequired["capo_controltower.types.arn.Arn"]
    """<p>The ARN of the enabled control to be disabled, which uniquely identifies the control instance on the target organizational unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableControlInput) -> dict:
    out: dict = {}
    if "control_identifier" in value:
        out["controlIdentifier"] = value["control_identifier"]
    if "target_identifier" in value:
        out["targetIdentifier"] = value["target_identifier"]
    if "enabled_control_identifier" in value:
        out["enabledControlIdentifier"] = value["enabled_control_identifier"]
    return out


def deserialize_json(data: dict) -> DisableControlInput:
    out: DisableControlInput = {}  # type: ignore[typeddict-item]
    if data.get("controlIdentifier") is not None:
        out["control_identifier"] = data["controlIdentifier"]
    if data.get("targetIdentifier") is not None:
        out["target_identifier"] = data["targetIdentifier"]
    if data.get("enabledControlIdentifier") is not None:
        out["enabled_control_identifier"] = data["enabledControlIdentifier"]
    return out
