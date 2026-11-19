"""Generated from Smithy shape ``com.amazonaws.pi#ListPerformanceAnalysisReportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.analysis_report_summary_list
    import capo_pi.types.next_token


class ListPerformanceAnalysisReportsResponse(TypedDict, closed=True):
    analysis_reports: NotRequired[
        "capo_pi.types.analysis_report_summary_list.AnalysisReportSummaryList"
    ]
    """<p>List of reports including the report identifier, start and end time, creation time, and status.</p>"""
    next_token: NotRequired["capo_pi.types.next_token.NextToken"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxResults</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPerformanceAnalysisReportsResponse) -> dict:
    out: dict = {}
    if "analysis_reports" in value:
        import capo_pi.types.analysis_report_summary_list

        out["AnalysisReports"] = (
            capo_pi.types.analysis_report_summary_list.serialize_aws_json_1_1(
                value["analysis_reports"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPerformanceAnalysisReportsResponse:
    out: ListPerformanceAnalysisReportsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AnalysisReports") is not None:
        import capo_pi.types.analysis_report_summary_list

        out["analysis_reports"] = (
            capo_pi.types.analysis_report_summary_list.deserialize_aws_json_1_1(
                data["AnalysisReports"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListPerformanceAnalysisReportsResponse) -> dict:
    out: dict = {}
    if "analysis_reports" in value:
        import capo_pi.types.analysis_report_summary_list

        out["AnalysisReports"] = (
            capo_pi.types.analysis_report_summary_list.serialize_cbor(
                value["analysis_reports"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListPerformanceAnalysisReportsResponse:
    out: ListPerformanceAnalysisReportsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AnalysisReports") is not None:
        import capo_pi.types.analysis_report_summary_list

        out["analysis_reports"] = (
            capo_pi.types.analysis_report_summary_list.deserialize_cbor(
                data["AnalysisReports"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
