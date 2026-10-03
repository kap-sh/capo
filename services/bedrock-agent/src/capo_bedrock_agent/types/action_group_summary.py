"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ActionGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.action_group_state
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.name


class ActionGroupSummary(TypedDict, closed=True):
    action_group_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the action group.</p>"""
    action_group_name: "capo_bedrock_agent.types.name.Name"
    """<p>The name of the action group.</p>"""
    action_group_state: "capo_bedrock_agent.types.action_group_state.ActionGroupState"
    """<p>Specifies whether the action group is available for the agent to invoke or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>The description of the action group.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the action group was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionGroupSummary) -> dict:
    out: dict = {}
    out["actionGroupId"] = value["action_group_id"]
    out["actionGroupName"] = value["action_group_name"]
    import capo_bedrock_agent.types.action_group_state

    out["actionGroupState"] = (
        capo_bedrock_agent.types.action_group_state.serialize_json(
            value["action_group_state"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agent.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> ActionGroupSummary:
    out: ActionGroupSummary = {}  # type: ignore[typeddict-item]
    if data.get("actionGroupId") is not None:
        out["action_group_id"] = data["actionGroupId"]
    else:
        raise DeserializationError("ActionGroupSummary.action_group_id required")
    if data.get("actionGroupName") is not None:
        out["action_group_name"] = data["actionGroupName"]
    else:
        raise DeserializationError("ActionGroupSummary.action_group_name required")
    if data.get("actionGroupState") is not None:
        import capo_bedrock_agent.types.action_group_state

        out["action_group_state"] = (
            capo_bedrock_agent.types.action_group_state.deserialize_json(
                data["actionGroupState"]
            )
        )
    else:
        raise DeserializationError("ActionGroupSummary.action_group_state required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("updatedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["updated_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("ActionGroupSummary.updated_at required")
    return out
