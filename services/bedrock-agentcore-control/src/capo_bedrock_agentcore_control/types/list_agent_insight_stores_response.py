"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListAgentInsightStoresResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_insight_store_summary_list


class ListAgentInsightStoresResponse(TypedDict, closed=True):
    agent_insight_stores: "capo_bedrock_agentcore_control.types.agent_insight_store_summary_list.AgentInsightStoreSummaryList"
    """<p>The Agent Insight Store summaries.</p>"""
    next_token: NotRequired["str"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentInsightStoresResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.agent_insight_store_summary_list

    out["agentInsightStores"] = (
        capo_bedrock_agentcore_control.types.agent_insight_store_summary_list.serialize_json(
            value["agent_insight_stores"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentInsightStoresResponse:
    out: ListAgentInsightStoresResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentInsightStores") is not None:
        import capo_bedrock_agentcore_control.types.agent_insight_store_summary_list

        out["agent_insight_stores"] = (
            capo_bedrock_agentcore_control.types.agent_insight_store_summary_list.deserialize_json(
                data["agentInsightStores"]
            )
        )
    else:
        out["agent_insight_stores"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
