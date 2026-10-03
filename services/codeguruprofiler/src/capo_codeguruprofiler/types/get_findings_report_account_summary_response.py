"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#GetFindingsReportAccountSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.findings_report_summaries
    import capo_codeguruprofiler.types.pagination_token


class GetFindingsReportAccountSummaryResponse(TypedDict, closed=True):
    report_summaries: (
        "capo_codeguruprofiler.types.findings_report_summaries.FindingsReportSummaries"
    )
    """<p>The return list of <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_FindingsReportSummary.html"> <code>FindingsReportSummary</code> </a> objects taht contain summaries of analysis results for all profiling groups in your AWS account.</p>"""
    next_token: NotRequired[
        "capo_codeguruprofiler.types.pagination_token.PaginationToken"
    ]
    """<p>The <code>nextToken</code> value to include in a future <code>GetFindingsReportAccountSummary</code> request. When the results of a <code>GetFindingsReportAccountSummary</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsReportAccountSummaryResponse) -> dict:
    out: dict = {}
    import capo_codeguruprofiler.types.findings_report_summaries

    out["reportSummaries"] = (
        capo_codeguruprofiler.types.findings_report_summaries.serialize_json(
            value["report_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetFindingsReportAccountSummaryResponse:
    out: GetFindingsReportAccountSummaryResponse = {}  # type: ignore[typeddict-item]
    if data.get("reportSummaries") is not None:
        import capo_codeguruprofiler.types.findings_report_summaries

        out["report_summaries"] = (
            capo_codeguruprofiler.types.findings_report_summaries.deserialize_json(
                data["reportSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "GetFindingsReportAccountSummaryResponse.report_summaries required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
