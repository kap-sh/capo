"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.component_name
    import capo_amplifyuibuilder.types.component_type
    import capo_amplifyuibuilder.types.uuid


class ComponentSummary(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID of the Amplify app associated with the component.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is a part of the Amplify app.</p>"""
    id: "capo_amplifyuibuilder.types.uuid.Uuid"
    """<p>The unique ID of the component.</p>"""
    name: "capo_amplifyuibuilder.types.component_name.ComponentName"
    """<p>The name of the component.</p>"""
    component_type: "capo_amplifyuibuilder.types.component_type.ComponentType"
    """<p>The component type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentSummary) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["environmentName"] = value["environment_name"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["componentType"] = value["component_type"]
    return out


def deserialize_json(data: dict) -> ComponentSummary:
    out: ComponentSummary = {}  # type: ignore[typeddict-item]
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    else:
        out["app_id"] = ""
    if data.get("environmentName") is not None:
        out["environment_name"] = data["environmentName"]
    else:
        out["environment_name"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("componentType") is not None:
        out["component_type"] = data["componentType"]
    else:
        out["component_type"] = ""
    return out
