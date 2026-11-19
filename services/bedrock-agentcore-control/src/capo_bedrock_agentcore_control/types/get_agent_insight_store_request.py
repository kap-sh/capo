"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetAgentInsightStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_insight_store_id


class GetAgentInsightStoreRequest(TypedDict, closed=True):
    agent_insight_store_id: "capo_bedrock_agentcore_control.types.agent_insight_store_id.AgentInsightStoreId"
    """<p>Specifies the unique identifier of the Agent Insight Store to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentInsightStoreRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentInsightStoreRequest:
    out: GetAgentInsightStoreRequest = {}  # type: ignore[typeddict-item]
    return out
