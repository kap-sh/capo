"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AgentInsightSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.agent_insight_summary

AgentInsightSummaryList: TypeAlias = list[
    "capo_bedrock_agentcore.types.agent_insight_summary.AgentInsightSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentInsightSummaryList) -> list:
    import capo_bedrock_agentcore.types.agent_insight_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.agent_insight_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AgentInsightSummaryList:
    import capo_bedrock_agentcore.types.agent_insight_summary

    out: AgentInsightSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.agent_insight_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: AgentInsightSummaryList) -> list[Any]:
    import capo_bedrock_agentcore.types.agent_insight_summary

    return [
        capo_bedrock_agentcore.types.agent_insight_summary.redact_sensitive(item)
        for item in value
    ]
