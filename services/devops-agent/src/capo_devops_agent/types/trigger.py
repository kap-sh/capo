"""Generated from Smithy shape ``com.amazonaws.devopsagent#Trigger``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.resource_id
    import capo_devops_agent.types.trigger_action
    import capo_devops_agent.types.trigger_condition
    import capo_devops_agent.types.trigger_status
    import capo_devops_agent.types.trigger_type


class Trigger(TypedDict, closed=True):
    trigger_id: "capo_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier for this Trigger</p>"""
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The agent space this Trigger belongs to</p>"""
    type: "capo_devops_agent.types.trigger_type.TriggerType"
    """<p>How this Trigger fires</p>"""
    condition: "capo_devops_agent.types.trigger_condition.TriggerCondition"
    """<p>The condition that fires this Trigger</p>"""
    action: "capo_devops_agent.types.trigger_action.TriggerAction"
    """<p>The action this Trigger performs when it fires</p>"""
    status: "capo_devops_agent.types.trigger_status.TriggerStatus"
    """<p>The status of this Trigger</p>"""
    created_at: "datetime.datetime"
    """<p>Timestamp when this Trigger was created</p>"""
    updated_at: "datetime.datetime"
    """<p>Timestamp when this Trigger was last updated</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Trigger) -> dict:
    out: dict = {}
    out["triggerId"] = value["trigger_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    out["type"] = value["type"]
    import capo_devops_agent.types.trigger_condition

    out["condition"] = capo_devops_agent.types.trigger_condition.serialize_json(
        value["condition"]
    )
    out["action"] = value["action"]
    out["status"] = value["status"]
    import capo_devops_agent.types._prelude.timestamp

    out["createdAt"] = capo_devops_agent.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_devops_agent.types._prelude.timestamp

    out["updatedAt"] = capo_devops_agent.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> Trigger:
    out: Trigger = {}  # type: ignore[typeddict-item]
    if data.get("triggerId") is not None:
        out["trigger_id"] = data["triggerId"]
    else:
        out["trigger_id"] = ""
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("condition") is not None:
        import capo_devops_agent.types.trigger_condition

        out["condition"] = capo_devops_agent.types.trigger_condition.deserialize_json(
            data["condition"]
        )
    else:
        out["condition"] = {"$unknown": {"name": ""}}
    if data.get("action") is not None:
        out["action"] = data["action"]
    else:
        out["action"] = None
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("createdAt") is not None:
        import capo_devops_agent.types._prelude.timestamp

        out["created_at"] = capo_devops_agent.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_devops_agent.types._prelude.timestamp

        out["updated_at"] = capo_devops_agent.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
