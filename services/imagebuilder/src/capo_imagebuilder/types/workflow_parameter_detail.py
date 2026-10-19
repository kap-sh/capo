"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowParameterDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.workflow_parameter_description
    import capo_imagebuilder.types.workflow_parameter_name
    import capo_imagebuilder.types.workflow_parameter_type
    import capo_imagebuilder.types.workflow_parameter_value_list


class WorkflowParameterDetail(TypedDict, closed=True):
    name: "capo_imagebuilder.types.workflow_parameter_name.WorkflowParameterName"
    """<p>The name of this input parameter.</p>"""
    type: "capo_imagebuilder.types.workflow_parameter_type.WorkflowParameterType"
    """<p>The type of input this parameter provides. Supported values are <code>string</code>, <code>integer</code>, <code>boolean</code>, and <code>stringList</code>.</p>"""
    default_value: NotRequired[
        "capo_imagebuilder.types.workflow_parameter_value_list.WorkflowParameterValueList"
    ]
    """<p>The default value of this parameter if no input is provided.</p>"""
    description: NotRequired[
        "capo_imagebuilder.types.workflow_parameter_description.WorkflowParameterDescription"
    ]
    """<p>Describes this parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowParameterDetail) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    if "default_value" in value:
        import capo_imagebuilder.types.workflow_parameter_value_list

        out["defaultValue"] = (
            capo_imagebuilder.types.workflow_parameter_value_list.serialize_json(
                value["default_value"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> WorkflowParameterDetail:
    out: WorkflowParameterDetail = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("defaultValue") is not None:
        import capo_imagebuilder.types.workflow_parameter_value_list

        out["default_value"] = (
            capo_imagebuilder.types.workflow_parameter_value_list.deserialize_json(
                data["defaultValue"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
