"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PrepareAgentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_status
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.version


class PrepareAgentResponse(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent for which the <code>DRAFT</code> version was created.</p>"""
    agent_status: "capo_bedrock_agent.types.agent_status.AgentStatus"
    """<p>The status of the <code>DRAFT</code> version and whether it is ready for use.</p>"""
    agent_version: "capo_bedrock_agent.types.version.Version"
    """<p>The version of the agent.</p>"""
    prepared_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the <code>DRAFT</code> version of the agent was last prepared.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrepareAgentResponse) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    import capo_bedrock_agent.types.agent_status

    out["agentStatus"] = capo_bedrock_agent.types.agent_status.serialize_json(
        value["agent_status"]
    )
    out["agentVersion"] = value["agent_version"]
    import capo_bedrock_agent.types.date_timestamp

    out["preparedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["prepared_at"]
    )
    return out


def deserialize_json(data: dict) -> PrepareAgentResponse:
    out: PrepareAgentResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentId") is not None:
        out["agent_id"] = data["agentId"]
    else:
        out["agent_id"] = ""
    if data.get("agentStatus") is not None:
        import capo_bedrock_agent.types.agent_status

        out["agent_status"] = capo_bedrock_agent.types.agent_status.deserialize_json(
            data["agentStatus"]
        )
    else:
        import typing

        out["agent_status"] = typing.cast(
            "capo_bedrock_agent.types.agent_status.AgentStatus", ""
        )
    if data.get("agentVersion") is not None:
        out["agent_version"] = data["agentVersion"]
    else:
        out["agent_version"] = ""
    if data.get("preparedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["prepared_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["preparedAt"]
        )
    else:
        import datetime

        out["prepared_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
