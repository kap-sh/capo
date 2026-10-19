"""Generated from Smithy shape ``com.amazonaws.connect#ListEvaluationFormAIVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_ai_version_summary_list
    import capo_connect.types.next_token


class ListEvaluationFormAIVersionsResponse(TypedDict, closed=True):
    ai_version_summaries: "capo_connect.types.evaluation_form_ai_version_summary_list.EvaluationFormAIVersionSummaryList"
    """<p>The list of AI version summaries.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEvaluationFormAIVersionsResponse) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_ai_version_summary_list

    out["AIVersionSummaries"] = (
        capo_connect.types.evaluation_form_ai_version_summary_list.serialize_json(
            value["ai_version_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEvaluationFormAIVersionsResponse:
    out: ListEvaluationFormAIVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AIVersionSummaries") is not None:
        import capo_connect.types.evaluation_form_ai_version_summary_list

        out["ai_version_summaries"] = (
            capo_connect.types.evaluation_form_ai_version_summary_list.deserialize_json(
                data["AIVersionSummaries"]
            )
        )
    else:
        out["ai_version_summaries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
