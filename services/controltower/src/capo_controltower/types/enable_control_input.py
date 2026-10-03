"""Generated from Smithy shape ``com.amazonaws.controltower#EnableControlInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import capo_controltower.types.control_identifier
    import capo_controltower.types.enabled_control_parameters
    import capo_controltower.types.tag_map
    import capo_controltower.types.target_identifier


class EnableControlInput(TypedDict, closed=True):
    control_identifier: "capo_controltower.types.control_identifier.ControlIdentifier"
    """<p>The ARN of the control. Only <b>Strongly recommended</b> and <b>Elective</b> controls are permitted, with the exception of the <b>Region deny</b> control. For information on how to find the <code>controlIdentifier</code>, see <a href="https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html">the overview page</a>.</p>"""
    target_identifier: "capo_controltower.types.target_identifier.TargetIdentifier"
    """<p>The ARN of the organizational unit. For information on how to find the <code>targetIdentifier</code>, see <a href="https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html">the overview page</a>.</p>"""
    tags: NotRequired["capo_controltower.types.tag_map.TagMap"]
    """<p>Tags to be applied to the <code>EnabledControl</code> resource.</p>"""
    parameters: NotRequired[
        "capo_controltower.types.enabled_control_parameters.EnabledControlParameters"
    ]
    """<p>A list of input parameter values, which are specified to configure the control when you enable it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableControlInput) -> dict:
    out: dict = {}
    out["controlIdentifier"] = value["control_identifier"]
    out["targetIdentifier"] = value["target_identifier"]
    if "tags" in value:
        import capo_controltower.types.tag_map

        out["tags"] = capo_controltower.types.tag_map.serialize_json(value["tags"])
    if "parameters" in value:
        import capo_controltower.types.enabled_control_parameters

        out["parameters"] = (
            capo_controltower.types.enabled_control_parameters.serialize_json(
                value["parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnableControlInput:
    out: EnableControlInput = {}  # type: ignore[typeddict-item]
    if data.get("controlIdentifier") is not None:
        out["control_identifier"] = data["controlIdentifier"]
    else:
        raise DeserializationError("EnableControlInput.control_identifier required")
    if data.get("targetIdentifier") is not None:
        out["target_identifier"] = data["targetIdentifier"]
    else:
        raise DeserializationError("EnableControlInput.target_identifier required")
    if data.get("tags") is not None:
        import capo_controltower.types.tag_map

        out["tags"] = capo_controltower.types.tag_map.deserialize_json(data["tags"])
    if data.get("parameters") is not None:
        import capo_controltower.types.enabled_control_parameters

        out["parameters"] = (
            capo_controltower.types.enabled_control_parameters.deserialize_json(
                data["parameters"]
            )
        )
    return out
