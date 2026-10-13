"""Generated from Smithy shape ``com.amazonaws.pi#AnalysisReport``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_pi.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pi.types.analysis_report_id
    import capo_pi.types.analysis_status
    import capo_pi.types.identifier_string
    import capo_pi.types.insight_list
    import capo_pi.types.iso_timestamp
    import capo_pi.types.service_type


class AnalysisReport(TypedDict, closed=True):
    analysis_report_id: "capo_pi.types.analysis_report_id.AnalysisReportId"
    """<p>The name of the analysis report.</p>"""
    identifier: NotRequired["capo_pi.types.identifier_string.IdentifierString"]
    """<p>The unique identifier of the analysis report.</p>"""
    service_type: NotRequired["capo_pi.types.service_type.ServiceType"]
    """<p>List the tags for the Amazon Web Services service for which Performance Insights returns metrics. Valid values are as follows:</p> <ul> <li> <p> <code>RDS</code> </p> </li> <li> <p> <code>DOCDB</code> </p> </li> </ul>"""
    create_time: NotRequired["capo_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The time you created the analysis report.</p>"""
    start_time: NotRequired["capo_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The analysis start time in the report.</p>"""
    end_time: NotRequired["capo_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The analysis end time in the report.</p>"""
    status: NotRequired["capo_pi.types.analysis_status.AnalysisStatus"]
    """<p>The status of the created analysis report.</p>"""
    insights: NotRequired["capo_pi.types.insight_list.InsightList"]
    """<p>The list of identified insights in the analysis report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalysisReport) -> dict:
    out: dict = {}
    out["AnalysisReportId"] = value["analysis_report_id"]
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "service_type" in value:
        import capo_pi.types.service_type

        out["ServiceType"] = capo_pi.types.service_type.serialize_aws_json_1_1(
            value["service_type"]
        )
    if "create_time" in value:
        import capo_pi.types.iso_timestamp

        out["CreateTime"] = capo_pi.types.iso_timestamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "start_time" in value:
        import capo_pi.types.iso_timestamp

        out["StartTime"] = capo_pi.types.iso_timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_pi.types.iso_timestamp

        out["EndTime"] = capo_pi.types.iso_timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "status" in value:
        import capo_pi.types.analysis_status

        out["Status"] = capo_pi.types.analysis_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "insights" in value:
        import capo_pi.types.insight_list

        out["Insights"] = capo_pi.types.insight_list.serialize_aws_json_1_1(
            value["insights"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalysisReport:
    out: AnalysisReport = {}  # type: ignore[typeddict-item]
    if data.get("AnalysisReportId") is not None:
        out["analysis_report_id"] = data["AnalysisReportId"]
    else:
        raise DeserializationError("AnalysisReport.analysis_report_id required")
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    if data.get("ServiceType") is not None:
        import capo_pi.types.service_type

        out["service_type"] = capo_pi.types.service_type.deserialize_aws_json_1_1(
            data["ServiceType"]
        )
    if data.get("CreateTime") is not None:
        import capo_pi.types.iso_timestamp

        out["create_time"] = capo_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["CreateTime"]
        )
    if data.get("StartTime") is not None:
        import capo_pi.types.iso_timestamp

        out["start_time"] = capo_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_pi.types.iso_timestamp

        out["end_time"] = capo_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("Status") is not None:
        import capo_pi.types.analysis_status

        out["status"] = capo_pi.types.analysis_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("Insights") is not None:
        import capo_pi.types.insight_list

        out["insights"] = capo_pi.types.insight_list.deserialize_aws_json_1_1(
            data["Insights"]
        )
    return out


def redact_sensitive(value: AnalysisReport) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "insights" in value:
        import capo_pi.types.insight_list

        out["insights"] = capo_pi.types.insight_list.redact_sensitive(value["insights"])
    return out
