"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.component_parameter_name
    import capo_imagebuilder.types.component_parameter_value_list


class ComponentParameter(TypedDict, closed=True):
    name: "capo_imagebuilder.types.component_parameter_name.ComponentParameterName"
    """<p>The name of the component parameter to set.</p>"""
    value: "capo_imagebuilder.types.component_parameter_value_list.ComponentParameterValueList"
    """<p>Sets the value for the named component parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentParameter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_imagebuilder.types.component_parameter_value_list

    out["value"] = (
        capo_imagebuilder.types.component_parameter_value_list.serialize_json(
            value["value"]
        )
    )
    return out


def deserialize_json(data: dict) -> ComponentParameter:
    out: ComponentParameter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("value") is not None:
        import capo_imagebuilder.types.component_parameter_value_list

        out["value"] = (
            capo_imagebuilder.types.component_parameter_value_list.deserialize_json(
                data["value"]
            )
        )
    else:
        out["value"] = []
    return out
