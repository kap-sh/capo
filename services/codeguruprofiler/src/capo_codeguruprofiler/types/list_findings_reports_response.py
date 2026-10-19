"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ListFindingsReportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.findings_report_summaries
    import capo_codeguruprofiler.types.pagination_token


class ListFindingsReportsResponse(TypedDict, closed=True):
    findings_report_summaries: (
        "capo_codeguruprofiler.types.findings_report_summaries.FindingsReportSummaries"
    )
    """<p>The list of analysis results summaries.</p>"""
    next_token: NotRequired[
        "capo_codeguruprofiler.types.pagination_token.PaginationToken"
    ]
    """<p>The <code>nextToken</code> value to include in a future <code>ListFindingsReports</code> request. When the results of a <code>ListFindingsReports</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsReportsResponse) -> dict:
    out: dict = {}
    import capo_codeguruprofiler.types.findings_report_summaries

    out["findingsReportSummaries"] = (
        capo_codeguruprofiler.types.findings_report_summaries.serialize_json(
            value["findings_report_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFindingsReportsResponse:
    out: ListFindingsReportsResponse = {}  # type: ignore[typeddict-item]
    if data.get("findingsReportSummaries") is not None:
        import capo_codeguruprofiler.types.findings_report_summaries

        out["findings_report_summaries"] = (
            capo_codeguruprofiler.types.findings_report_summaries.deserialize_json(
                data["findingsReportSummaries"]
            )
        )
    else:
        out["findings_report_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
