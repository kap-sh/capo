"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_controlcatalog.types.control_parameter_requirement


class ControlParameter(TypedDict, closed=True):
    name: "str"
    """<p>The parameter name. This name is the parameter <code>key</code> when you call <a href="https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableControl.html"> <code>EnableControl</code> </a> or <a href="https://docs.aws.amazon.com/controltower/latest/APIReference/API_UpdateEnabledControl.html"> <code>UpdateEnabledControl</code> </a>.</p>"""
    requirement: NotRequired[
        "capo_controlcatalog.types.control_parameter_requirement.ControlParameterRequirement"
    ]
    """<p>Indicates whether the parameter is required or optional when you enable the control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlParameter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "requirement" in value:
        import capo_controlcatalog.types.control_parameter_requirement

        out["Requirement"] = (
            capo_controlcatalog.types.control_parameter_requirement.serialize_json(
                value["requirement"]
            )
        )
    return out


def deserialize_json(data: dict) -> ControlParameter:
    out: ControlParameter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ControlParameter.name required")
    if data.get("Requirement") is not None:
        import capo_controlcatalog.types.control_parameter_requirement

        out["requirement"] = (
            capo_controlcatalog.types.control_parameter_requirement.deserialize_json(
                data["Requirement"]
            )
        )
    return out
