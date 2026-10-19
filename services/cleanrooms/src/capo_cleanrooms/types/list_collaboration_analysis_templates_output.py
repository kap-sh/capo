"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListCollaborationAnalysisTemplatesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_analysis_template_summary_list
    import capo_cleanrooms.types.pagination_token


class ListCollaborationAnalysisTemplatesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    collaboration_analysis_template_summaries: "capo_cleanrooms.types.collaboration_analysis_template_summary_list.CollaborationAnalysisTemplateSummaryList"
    """<p>The metadata of the analysis template within a collaboration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationAnalysisTemplatesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanrooms.types.collaboration_analysis_template_summary_list

    out["collaborationAnalysisTemplateSummaries"] = (
        capo_cleanrooms.types.collaboration_analysis_template_summary_list.serialize_json(
            value["collaboration_analysis_template_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListCollaborationAnalysisTemplatesOutput:
    out: ListCollaborationAnalysisTemplatesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("collaborationAnalysisTemplateSummaries") is not None:
        import capo_cleanrooms.types.collaboration_analysis_template_summary_list

        out["collaboration_analysis_template_summaries"] = (
            capo_cleanrooms.types.collaboration_analysis_template_summary_list.deserialize_json(
                data["collaborationAnalysisTemplateSummaries"]
            )
        )
    else:
        out["collaboration_analysis_template_summaries"] = []
    return out
