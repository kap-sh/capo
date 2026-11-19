"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListAgentInsightsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.agent_insight_summary_list
    import capo_bedrock_agentcore.types.next_token


class ListAgentInsightsResponse(TypedDict, closed=True):
    agent_insights: "capo_bedrock_agentcore.types.agent_insight_summary_list.AgentInsightSummaryList"
    """<p>The Agent Insight summaries.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore.types.next_token.NextToken"]
    """<p>A token to use to retrieve the next page of results. This value is present only when additional results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentInsightsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.agent_insight_summary_list

    out["agentInsights"] = (
        capo_bedrock_agentcore.types.agent_insight_summary_list.serialize_json(
            value["agent_insights"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentInsightsResponse:
    out: ListAgentInsightsResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentInsights") is not None:
        import capo_bedrock_agentcore.types.agent_insight_summary_list

        out["agent_insights"] = (
            capo_bedrock_agentcore.types.agent_insight_summary_list.deserialize_json(
                data["agentInsights"]
            )
        )
    else:
        out["agent_insights"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListAgentInsightsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "agent_insights" in value:
        import capo_bedrock_agentcore.types.agent_insight_summary_list

        out["agent_insights"] = (
            capo_bedrock_agentcore.types.agent_insight_summary_list.redact_sensitive(
                value["agent_insights"]
            )
        )
    return out
