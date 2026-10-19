"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptAgentResource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_alias_arn


class PromptAgentResource(TypedDict, closed=True):
    agent_identifier: "capo_bedrock_agent.types.agent_alias_arn.AgentAliasArn"
    """<p>The ARN of the agent with which to use the prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptAgentResource) -> dict:
    out: dict = {}
    out["agentIdentifier"] = value["agent_identifier"]
    return out


def deserialize_json(data: dict) -> PromptAgentResource:
    out: PromptAgentResource = {}  # type: ignore[typeddict-item]
    if data.get("agentIdentifier") is not None:
        out["agent_identifier"] = data["agentIdentifier"]
    else:
        out["agent_identifier"] = ""
    return out
