"""Generated from Smithy shape ``com.amazonaws.pi#CreatePerformanceAnalysisReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.analysis_report_id


class CreatePerformanceAnalysisReportResponse(TypedDict, closed=True):
    analysis_report_id: NotRequired["capo_pi.types.analysis_report_id.AnalysisReportId"]
    """<p>A unique identifier for the created analysis report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePerformanceAnalysisReportResponse) -> dict:
    out: dict = {}
    if "analysis_report_id" in value:
        out["AnalysisReportId"] = value["analysis_report_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePerformanceAnalysisReportResponse:
    out: CreatePerformanceAnalysisReportResponse = {}  # type: ignore[typeddict-item]
    if data.get("AnalysisReportId") is not None:
        out["analysis_report_id"] = data["AnalysisReportId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreatePerformanceAnalysisReportResponse) -> dict:
    out: dict = {}
    if "analysis_report_id" in value:
        out["AnalysisReportId"] = value["analysis_report_id"]
    return out


def deserialize_cbor(data: dict) -> CreatePerformanceAnalysisReportResponse:
    out: CreatePerformanceAnalysisReportResponse = {}  # type: ignore[typeddict-item]
    if data.get("AnalysisReportId") is not None:
        out["analysis_report_id"] = data["AnalysisReportId"]
    return out
