"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetAgentInsightRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.agent_application_name
    import capo_bedrock_agentcore.types.agent_insight_id


class GetAgentInsightRequest(TypedDict, closed=True):
    application_name: (
        "capo_bedrock_agentcore.types.agent_application_name.AgentApplicationName"
    )
    """<p>The application that the Agent Insight belongs to.</p>"""
    agent_insight_id: "capo_bedrock_agentcore.types.agent_insight_id.AgentInsightId"
    """<p>The unique identifier of the Agent Insight to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentInsightRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentInsightRequest:
    out: GetAgentInsightRequest = {}  # type: ignore[typeddict-item]
    return out
