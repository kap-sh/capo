"""Generated from Smithy shape ``com.amazonaws.qconnect#ListAIPromptVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_prompt_version_summaries_list
    import capo_qconnect.types.next_token


class ListAIPromptVersionsResponse(TypedDict, closed=True):
    ai_prompt_version_summaries: "capo_qconnect.types.ai_prompt_version_summaries_list.AIPromptVersionSummariesList"
    """<p>The summaries of the AI Prompt versions.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAIPromptVersionsResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.ai_prompt_version_summaries_list

    out["aiPromptVersionSummaries"] = (
        capo_qconnect.types.ai_prompt_version_summaries_list.serialize_json(
            value["ai_prompt_version_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAIPromptVersionsResponse:
    out: ListAIPromptVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("aiPromptVersionSummaries") is not None:
        import capo_qconnect.types.ai_prompt_version_summaries_list

        out["ai_prompt_version_summaries"] = (
            capo_qconnect.types.ai_prompt_version_summaries_list.deserialize_json(
                data["aiPromptVersionSummaries"]
            )
        )
    else:
        out["ai_prompt_version_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
