"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name


class ActionDefinition(TypedDict, closed=True):
    action_definition_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the action definition.</p>"""
    action_name: "capo_iotsitewise.types.name.Name"
    """<p>The name of the action definition.</p>"""
    action_type: "capo_iotsitewise.types.name.Name"
    """<p>The type of the action definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionDefinition) -> dict:
    out: dict = {}
    out["actionDefinitionId"] = value["action_definition_id"]
    out["actionName"] = value["action_name"]
    out["actionType"] = value["action_type"]
    return out


def deserialize_json(data: dict) -> ActionDefinition:
    out: ActionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("actionDefinitionId") is not None:
        out["action_definition_id"] = data["actionDefinitionId"]
    else:
        out["action_definition_id"] = ""
    if data.get("actionName") is not None:
        out["action_name"] = data["actionName"]
    else:
        out["action_name"] = ""
    if data.get("actionType") is not None:
        out["action_type"] = data["actionType"]
    else:
        out["action_type"] = ""
    return out
