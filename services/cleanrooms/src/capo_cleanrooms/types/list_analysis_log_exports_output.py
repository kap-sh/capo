"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListAnalysisLogExportsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_log_export_summary_list
    import capo_cleanrooms.types.pagination_token


class ListAnalysisLogExportsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    analysis_log_exports: "capo_cleanrooms.types.analysis_log_export_summary_list.AnalysisLogExportSummaryList"
    """<p>A list of analysis log exports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnalysisLogExportsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanrooms.types.analysis_log_export_summary_list

    out["analysisLogExports"] = (
        capo_cleanrooms.types.analysis_log_export_summary_list.serialize_json(
            value["analysis_log_exports"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListAnalysisLogExportsOutput:
    out: ListAnalysisLogExportsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("analysisLogExports") is not None:
        import capo_cleanrooms.types.analysis_log_export_summary_list

        out["analysis_log_exports"] = (
            capo_cleanrooms.types.analysis_log_export_summary_list.deserialize_json(
                data["analysisLogExports"]
            )
        )
    else:
        out["analysis_log_exports"] = []
    return out
