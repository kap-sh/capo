"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#UpdateComponentTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_type_id
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.state
    import capo_iottwinmaker.types.twin_maker_arn


class UpdateComponentTypeResponse(TypedDict, closed=True):
    workspace_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the component type.</p>"""
    arn: "capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The ARN of the component type.</p>"""
    component_type_id: "capo_iottwinmaker.types.component_type_id.ComponentTypeId"
    """<p>The ID of the component type.</p>"""
    state: "capo_iottwinmaker.types.state.State"
    """<p>The current state of the component type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateComponentTypeResponse) -> dict:
    out: dict = {}
    out["workspaceId"] = value["workspace_id"]
    out["arn"] = value["arn"]
    out["componentTypeId"] = value["component_type_id"]
    out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> UpdateComponentTypeResponse:
    out: UpdateComponentTypeResponse = {}  # type: ignore[typeddict-item]
    if data.get("workspaceId") is not None:
        out["workspace_id"] = data["workspaceId"]
    else:
        out["workspace_id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("componentTypeId") is not None:
        out["component_type_id"] = data["componentTypeId"]
    else:
        out["component_type_id"] = ""
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        out["state"] = ""
    return out
