"""Generated from Smithy shape ``com.amazonaws.qconnect#ListAIAgentsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_agent_summary_list
    import capo_qconnect.types.next_token


class ListAIAgentsResponse(TypedDict, closed=True):
    ai_agent_summaries: "capo_qconnect.types.ai_agent_summary_list.AIAgentSummaryList"
    """<p>The summaries of AI Agents.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAIAgentsResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.ai_agent_summary_list

    out["aiAgentSummaries"] = capo_qconnect.types.ai_agent_summary_list.serialize_json(
        value["ai_agent_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAIAgentsResponse:
    out: ListAIAgentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("aiAgentSummaries") is not None:
        import capo_qconnect.types.ai_agent_summary_list

        out["ai_agent_summaries"] = (
            capo_qconnect.types.ai_agent_summary_list.deserialize_json(
                data["aiAgentSummaries"]
            )
        )
    else:
        out["ai_agent_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListAIAgentsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ai_agent_summaries" in value:
        import capo_qconnect.types.ai_agent_summary_list

        out["ai_agent_summaries"] = (
            capo_qconnect.types.ai_agent_summary_list.redact_sensitive(
                value["ai_agent_summaries"]
            )
        )
    return out
