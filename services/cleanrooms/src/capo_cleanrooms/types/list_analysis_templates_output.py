"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListAnalysisTemplatesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_template_summary_list
    import capo_cleanrooms.types.pagination_token


class ListAnalysisTemplatesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    analysis_template_summaries: "capo_cleanrooms.types.analysis_template_summary_list.AnalysisTemplateSummaryList"
    """<p>Lists analysis template metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnalysisTemplatesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanrooms.types.analysis_template_summary_list

    out["analysisTemplateSummaries"] = (
        capo_cleanrooms.types.analysis_template_summary_list.serialize_json(
            value["analysis_template_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListAnalysisTemplatesOutput:
    out: ListAnalysisTemplatesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("analysisTemplateSummaries") is not None:
        import capo_cleanrooms.types.analysis_template_summary_list

        out["analysis_template_summaries"] = (
            capo_cleanrooms.types.analysis_template_summary_list.deserialize_json(
                data["analysisTemplateSummaries"]
            )
        )
    else:
        out["analysis_template_summaries"] = []
    return out
