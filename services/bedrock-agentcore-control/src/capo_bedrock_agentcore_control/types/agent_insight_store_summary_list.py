"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentInsightStoreSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_insight_store_summary

AgentInsightStoreSummaryList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.agent_insight_store_summary.AgentInsightStoreSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentInsightStoreSummaryList) -> list:
    import capo_bedrock_agentcore_control.types.agent_insight_store_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.agent_insight_store_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgentInsightStoreSummaryList:
    import capo_bedrock_agentcore_control.types.agent_insight_store_summary

    out: AgentInsightStoreSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.agent_insight_store_summary.deserialize_json(
                item
            )
        )
    return out
