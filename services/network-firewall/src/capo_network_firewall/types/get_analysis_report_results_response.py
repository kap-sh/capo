"""Generated from Smithy shape ``com.amazonaws.networkfirewall#GetAnalysisReportResultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.analysis_report_next_token
    import capo_network_firewall.types.analysis_report_results
    import capo_network_firewall.types.enabled_analysis_type
    import capo_network_firewall.types.end_time
    import capo_network_firewall.types.report_time
    import capo_network_firewall.types.start_time
    import capo_network_firewall.types.status


class GetAnalysisReportResultsResponse(TypedDict, closed=True):
    status: NotRequired["capo_network_firewall.types.status.Status"]
    """<p>The status of the analysis report you specify. Statuses include <code>RUNNING</code>, <code>COMPLETED</code>, or <code>FAILED</code>.</p>"""
    start_time: NotRequired["capo_network_firewall.types.start_time.StartTime"]
    """<p> The date and time within the last 30 days from which to start retrieving analysis data, in UTC format (for example, <code>YYYY-MM-DDTHH:MM:SSZ</code>. </p>"""
    end_time: NotRequired["capo_network_firewall.types.end_time.EndTime"]
    """<p>The date and time, up to the current date, from which to stop retrieving analysis data, in UTC format (for example, <code>YYYY-MM-DDTHH:MM:SSZ</code>). </p>"""
    report_time: NotRequired["capo_network_firewall.types.report_time.ReportTime"]
    """<p>The date and time the analysis report was ran. </p>"""
    analysis_type: NotRequired[
        "capo_network_firewall.types.enabled_analysis_type.EnabledAnalysisType"
    ]
    """<p>The type of traffic that will be used to generate a report. </p>"""
    next_token: NotRequired[
        "capo_network_firewall.types.analysis_report_next_token.AnalysisReportNextToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""
    analysis_report_results: NotRequired[
        "capo_network_firewall.types.analysis_report_results.AnalysisReportResults"
    ]
    """<p>Retrieves the results of a traffic analysis report.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAnalysisReportResultsResponse) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    if "start_time" in value:
        import capo_network_firewall.types.start_time

        out["StartTime"] = (
            capo_network_firewall.types.start_time.serialize_aws_json_1_0(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import capo_network_firewall.types.end_time

        out["EndTime"] = capo_network_firewall.types.end_time.serialize_aws_json_1_0(
            value["end_time"]
        )
    if "report_time" in value:
        import capo_network_firewall.types.report_time

        out["ReportTime"] = (
            capo_network_firewall.types.report_time.serialize_aws_json_1_0(
                value["report_time"]
            )
        )
    if "analysis_type" in value:
        import capo_network_firewall.types.enabled_analysis_type

        out["AnalysisType"] = (
            capo_network_firewall.types.enabled_analysis_type.serialize_aws_json_1_0(
                value["analysis_type"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "analysis_report_results" in value:
        import capo_network_firewall.types.analysis_report_results

        out["AnalysisReportResults"] = (
            capo_network_firewall.types.analysis_report_results.serialize_aws_json_1_0(
                value["analysis_report_results"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAnalysisReportResultsResponse:
    out: GetAnalysisReportResultsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("StartTime") is not None:
        import capo_network_firewall.types.start_time

        out["start_time"] = (
            capo_network_firewall.types.start_time.deserialize_aws_json_1_0(
                data["StartTime"]
            )
        )
    if data.get("EndTime") is not None:
        import capo_network_firewall.types.end_time

        out["end_time"] = capo_network_firewall.types.end_time.deserialize_aws_json_1_0(
            data["EndTime"]
        )
    if data.get("ReportTime") is not None:
        import capo_network_firewall.types.report_time

        out["report_time"] = (
            capo_network_firewall.types.report_time.deserialize_aws_json_1_0(
                data["ReportTime"]
            )
        )
    if data.get("AnalysisType") is not None:
        import capo_network_firewall.types.enabled_analysis_type

        out["analysis_type"] = (
            capo_network_firewall.types.enabled_analysis_type.deserialize_aws_json_1_0(
                data["AnalysisType"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("AnalysisReportResults") is not None:
        import capo_network_firewall.types.analysis_report_results

        out["analysis_report_results"] = (
            capo_network_firewall.types.analysis_report_results.deserialize_aws_json_1_0(
                data["AnalysisReportResults"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAnalysisReportResultsResponse) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    if "start_time" in value:
        import capo_network_firewall.types.start_time

        out["StartTime"] = capo_network_firewall.types.start_time.serialize_cbor(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_network_firewall.types.end_time

        out["EndTime"] = capo_network_firewall.types.end_time.serialize_cbor(
            value["end_time"]
        )
    if "report_time" in value:
        import capo_network_firewall.types.report_time

        out["ReportTime"] = capo_network_firewall.types.report_time.serialize_cbor(
            value["report_time"]
        )
    if "analysis_type" in value:
        import capo_network_firewall.types.enabled_analysis_type

        out["AnalysisType"] = (
            capo_network_firewall.types.enabled_analysis_type.serialize_cbor(
                value["analysis_type"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "analysis_report_results" in value:
        import capo_network_firewall.types.analysis_report_results

        out["AnalysisReportResults"] = (
            capo_network_firewall.types.analysis_report_results.serialize_cbor(
                value["analysis_report_results"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetAnalysisReportResultsResponse:
    out: GetAnalysisReportResultsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("StartTime") is not None:
        import capo_network_firewall.types.start_time

        out["start_time"] = capo_network_firewall.types.start_time.deserialize_cbor(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_network_firewall.types.end_time

        out["end_time"] = capo_network_firewall.types.end_time.deserialize_cbor(
            data["EndTime"]
        )
    if data.get("ReportTime") is not None:
        import capo_network_firewall.types.report_time

        out["report_time"] = capo_network_firewall.types.report_time.deserialize_cbor(
            data["ReportTime"]
        )
    if data.get("AnalysisType") is not None:
        import capo_network_firewall.types.enabled_analysis_type

        out["analysis_type"] = (
            capo_network_firewall.types.enabled_analysis_type.deserialize_cbor(
                data["AnalysisType"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("AnalysisReportResults") is not None:
        import capo_network_firewall.types.analysis_report_results

        out["analysis_report_results"] = (
            capo_network_firewall.types.analysis_report_results.deserialize_cbor(
                data["AnalysisReportResults"]
            )
        )
    return out
