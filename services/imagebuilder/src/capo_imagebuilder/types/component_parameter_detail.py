"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentParameterDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.component_parameter_description
    import capo_imagebuilder.types.component_parameter_name
    import capo_imagebuilder.types.component_parameter_type
    import capo_imagebuilder.types.component_parameter_value_list


class ComponentParameterDetail(TypedDict, closed=True):
    name: "capo_imagebuilder.types.component_parameter_name.ComponentParameterName"
    """<p>The name of this input parameter.</p>"""
    type: "capo_imagebuilder.types.component_parameter_type.ComponentParameterType"
    """<p>The type of input this parameter provides. The currently supported value is "string".</p>"""
    default_value: NotRequired[
        "capo_imagebuilder.types.component_parameter_value_list.ComponentParameterValueList"
    ]
    """<p>The default value of this parameter if no input is provided.</p>"""
    description: NotRequired[
        "capo_imagebuilder.types.component_parameter_description.ComponentParameterDescription"
    ]
    """<p>Describes this parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentParameterDetail) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    if "default_value" in value:
        import capo_imagebuilder.types.component_parameter_value_list

        out["defaultValue"] = (
            capo_imagebuilder.types.component_parameter_value_list.serialize_json(
                value["default_value"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ComponentParameterDetail:
    out: ComponentParameterDetail = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ComponentParameterDetail.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("ComponentParameterDetail.type required")
    if data.get("defaultValue") is not None:
        import capo_imagebuilder.types.component_parameter_value_list

        out["default_value"] = (
            capo_imagebuilder.types.component_parameter_value_list.deserialize_json(
                data["defaultValue"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
