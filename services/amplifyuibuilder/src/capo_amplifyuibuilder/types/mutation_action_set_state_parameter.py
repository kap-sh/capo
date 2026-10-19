"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#MutationActionSetStateParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.component_property


class MutationActionSetStateParameter(TypedDict, closed=True):
    component_name: "str"
    """<p>The name of the component that is being modified.</p>"""
    property: "str"
    """<p>The name of the component property to apply the state configuration to.</p>"""
    set: "capo_amplifyuibuilder.types.component_property.ComponentProperty"
    """<p>The state configuration to assign to the property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MutationActionSetStateParameter) -> dict:
    out: dict = {}
    out["componentName"] = value["component_name"]
    out["property"] = value["property"]
    import capo_amplifyuibuilder.types.component_property

    out["set"] = capo_amplifyuibuilder.types.component_property.serialize_json(
        value["set"]
    )
    return out


def deserialize_json(data: dict) -> MutationActionSetStateParameter:
    out: MutationActionSetStateParameter = {}  # type: ignore[typeddict-item]
    if data.get("componentName") is not None:
        out["component_name"] = data["componentName"]
    else:
        out["component_name"] = ""
    if data.get("property") is not None:
        out["property"] = data["property"]
    else:
        out["property"] = ""
    if data.get("set") is not None:
        import capo_amplifyuibuilder.types.component_property

        out["set"] = capo_amplifyuibuilder.types.component_property.deserialize_json(
            data["set"]
        )
    else:
        raise DeserializationError("MutationActionSetStateParameter.set required")
    return out
