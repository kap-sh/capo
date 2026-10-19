"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteAgentVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_status
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.numerical_version


class DeleteAgentVersionResponse(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent that the version belongs to.</p>"""
    agent_version: "capo_bedrock_agent.types.numerical_version.NumericalVersion"
    """<p>The version that was deleted.</p>"""
    agent_status: "capo_bedrock_agent.types.agent_status.AgentStatus"
    """<p>The status of the agent version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentVersionResponse) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["agentVersion"] = value["agent_version"]
    import capo_bedrock_agent.types.agent_status

    out["agentStatus"] = capo_bedrock_agent.types.agent_status.serialize_json(
        value["agent_status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteAgentVersionResponse:
    out: DeleteAgentVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentId") is not None:
        out["agent_id"] = data["agentId"]
    else:
        out["agent_id"] = ""
    if data.get("agentVersion") is not None:
        out["agent_version"] = data["agentVersion"]
    else:
        out["agent_version"] = ""
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
    return out
