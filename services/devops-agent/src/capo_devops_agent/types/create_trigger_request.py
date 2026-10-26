"""Generated from Smithy shape ``com.amazonaws.devopsagent#CreateTriggerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_identifier
    import capo_devops_agent.types.trigger_action
    import capo_devops_agent.types.trigger_condition
    import capo_devops_agent.types.trigger_status
    import capo_devops_agent.types.trigger_type


class CreateTriggerRequest(TypedDict, closed=True):
    agent_space_id: (
        "capo_devops_agent.types.agent_space_identifier.AgentSpaceIdentifier"
    )
    """<p>The unique identifier for the agent space where the Trigger will be created</p>"""
    type: "capo_devops_agent.types.trigger_type.TriggerType"
    """<p>How the new Trigger fires</p>"""
    condition: "capo_devops_agent.types.trigger_condition.TriggerCondition"
    """<p>The condition that fires the new Trigger</p>"""
    action: "capo_devops_agent.types.trigger_action.TriggerAction"
    """<p>The action the new Trigger performs when it fires</p>"""
    status: NotRequired["capo_devops_agent.types.trigger_status.TriggerStatus"]
    """<p>The initial status of the Trigger</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier used for idempotent Trigger creation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTriggerRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    import capo_devops_agent.types.trigger_condition

    out["condition"] = capo_devops_agent.types.trigger_condition.serialize_json(
        value["condition"]
    )
    out["action"] = value["action"]
    if "status" in value:
        out["status"] = value["status"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateTriggerRequest:
    out: CreateTriggerRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
