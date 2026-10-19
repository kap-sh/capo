"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteAgentAliasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_alias_id
    import capo_bedrock_agent.types.agent_alias_status
    import capo_bedrock_agent.types.id


class DeleteAgentAliasResponse(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent that the alias belongs to.</p>"""
    agent_alias_id: "capo_bedrock_agent.types.agent_alias_id.AgentAliasId"
    """<p>The unique identifier of the alias that was deleted.</p>"""
    agent_alias_status: "capo_bedrock_agent.types.agent_alias_status.AgentAliasStatus"
    """<p>The status of the alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentAliasResponse) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["agentAliasId"] = value["agent_alias_id"]
    import capo_bedrock_agent.types.agent_alias_status

    out["agentAliasStatus"] = (
        capo_bedrock_agent.types.agent_alias_status.serialize_json(
            value["agent_alias_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteAgentAliasResponse:
    out: DeleteAgentAliasResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentId") is not None:
        out["agent_id"] = data["agentId"]
    else:
        out["agent_id"] = ""
    if data.get("agentAliasId") is not None:
        out["agent_alias_id"] = data["agentAliasId"]
    else:
        out["agent_alias_id"] = ""
    if data.get("agentAliasStatus") is not None:
        import capo_bedrock_agent.types.agent_alias_status

        out["agent_alias_status"] = (
            capo_bedrock_agent.types.agent_alias_status.deserialize_json(
                data["agentAliasStatus"]
            )
        )
    else:
        import typing

        out["agent_alias_status"] = typing.cast(
            "capo_bedrock_agent.types.agent_alias_status.AgentAliasStatus", ""
        )
    return out
