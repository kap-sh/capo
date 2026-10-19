"""Generated from Smithy shape ``com.amazonaws.qconnect#ListAIPromptsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_prompt_summary_list
    import capo_qconnect.types.next_token


class ListAIPromptsResponse(TypedDict, closed=True):
    ai_prompt_summaries: (
        "capo_qconnect.types.ai_prompt_summary_list.AIPromptSummaryList"
    )
    """<p>The summaries of the AI Prompts.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAIPromptsResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.ai_prompt_summary_list

    out["aiPromptSummaries"] = (
        capo_qconnect.types.ai_prompt_summary_list.serialize_json(
            value["ai_prompt_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAIPromptsResponse:
    out: ListAIPromptsResponse = {}  # type: ignore[typeddict-item]
    if data.get("aiPromptSummaries") is not None:
        import capo_qconnect.types.ai_prompt_summary_list

        out["ai_prompt_summaries"] = (
            capo_qconnect.types.ai_prompt_summary_list.deserialize_json(
                data["aiPromptSummaries"]
            )
        )
    else:
        out["ai_prompt_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
