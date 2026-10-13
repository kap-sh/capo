"""Generated from Smithy shape ``com.amazonaws.qconnect#ListAIAgentVersionsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.ai_agent_version_summaries_list
    import capo_qconnect.types.next_token


class ListAIAgentVersionsResponse(TypedDict, closed=True):
    ai_agent_version_summaries: "capo_qconnect.types.ai_agent_version_summaries_list.AIAgentVersionSummariesList"
    """<p>The summaries of AI Agent versions.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAIAgentVersionsResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.ai_agent_version_summaries_list

    out["aiAgentVersionSummaries"] = (
        capo_qconnect.types.ai_agent_version_summaries_list.serialize_json(
            value["ai_agent_version_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAIAgentVersionsResponse:
    out: ListAIAgentVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("aiAgentVersionSummaries") is not None:
        import capo_qconnect.types.ai_agent_version_summaries_list

        out["ai_agent_version_summaries"] = (
            capo_qconnect.types.ai_agent_version_summaries_list.deserialize_json(
                data["aiAgentVersionSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAIAgentVersionsResponse.ai_agent_version_summaries required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListAIAgentVersionsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ai_agent_version_summaries" in value:
        import capo_qconnect.types.ai_agent_version_summaries_list

        out["ai_agent_version_summaries"] = (
            capo_qconnect.types.ai_agent_version_summaries_list.redact_sensitive(
                value["ai_agent_version_summaries"]
            )
        )
    return out
