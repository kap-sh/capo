"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AnalysisReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.analysis_report_id
    import capo_network_firewall.types.enabled_analysis_type
    import capo_network_firewall.types.report_time
    import capo_network_firewall.types.status


class AnalysisReport(TypedDict, closed=True):
    analysis_report_id: NotRequired[
        "capo_network_firewall.types.analysis_report_id.AnalysisReportId"
    ]
    """<p>The unique ID of the query that ran when you requested an analysis report. </p>"""
    analysis_type: NotRequired[
        "capo_network_firewall.types.enabled_analysis_type.EnabledAnalysisType"
    ]
    """<p>The type of traffic that will be used to generate a report. </p>"""
    report_time: NotRequired["capo_network_firewall.types.report_time.ReportTime"]
    """<p>The date and time the analysis report was ran. </p>"""
    status: NotRequired["capo_network_firewall.types.status.Status"]
    """<p>The status of the analysis report you specify. Statuses include <code>RUNNING</code>, <code>COMPLETED</code>, or <code>FAILED</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnalysisReport) -> dict:
    out: dict = {}
    if "analysis_report_id" in value:
        out["AnalysisReportId"] = value["analysis_report_id"]
    if "analysis_type" in value:
        import capo_network_firewall.types.enabled_analysis_type

        out["AnalysisType"] = (
            capo_network_firewall.types.enabled_analysis_type.serialize_aws_json_1_0(
                value["analysis_type"]
            )
        )
    if "report_time" in value:
        import capo_network_firewall.types.report_time

        out["ReportTime"] = (
            capo_network_firewall.types.report_time.serialize_aws_json_1_0(
                value["report_time"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AnalysisReport:
    out: AnalysisReport = {}  # type: ignore[typeddict-item]
    if data.get("AnalysisReportId") is not None:
        out["analysis_report_id"] = data["AnalysisReportId"]
    if data.get("AnalysisType") is not None:
        import capo_network_firewall.types.enabled_analysis_type

        out["analysis_type"] = (
            capo_network_firewall.types.enabled_analysis_type.deserialize_aws_json_1_0(
                data["AnalysisType"]
            )
        )
    if data.get("ReportTime") is not None:
        import capo_network_firewall.types.report_time

        out["report_time"] = (
            capo_network_firewall.types.report_time.deserialize_aws_json_1_0(
                data["ReportTime"]
            )
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AnalysisReport) -> dict:
    out: dict = {}
    if "analysis_report_id" in value:
        out["AnalysisReportId"] = value["analysis_report_id"]
    if "analysis_type" in value:
        import capo_network_firewall.types.enabled_analysis_type

        out["AnalysisType"] = (
            capo_network_firewall.types.enabled_analysis_type.serialize_cbor(
                value["analysis_type"]
            )
        )
    if "report_time" in value:
        import capo_network_firewall.types.report_time

        out["ReportTime"] = capo_network_firewall.types.report_time.serialize_cbor(
            value["report_time"]
        )
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_cbor(data: dict) -> AnalysisReport:
    out: AnalysisReport = {}  # type: ignore[typeddict-item]
    if data.get("AnalysisReportId") is not None:
        out["analysis_report_id"] = data["AnalysisReportId"]
    if data.get("AnalysisType") is not None:
        import capo_network_firewall.types.enabled_analysis_type

        out["analysis_type"] = (
            capo_network_firewall.types.enabled_analysis_type.deserialize_cbor(
                data["AnalysisType"]
            )
        )
    if data.get("ReportTime") is not None:
        import capo_network_firewall.types.report_time

        out["report_time"] = capo_network_firewall.types.report_time.deserialize_cbor(
            data["ReportTime"]
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    return out
