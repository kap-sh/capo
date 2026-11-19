"""Generated from Smithy shape ``com.amazonaws.pi#AnalysisReportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.analysis_status
    import capo_pi.types.iso_timestamp
    import capo_pi.types.string
    import capo_pi.types.tag_list


class AnalysisReportSummary(TypedDict, closed=True):
    analysis_report_id: NotRequired["capo_pi.types.string.String"]
    """<p>The name of the analysis report.</p>"""
    create_time: NotRequired["capo_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The time you created the analysis report.</p>"""
    start_time: NotRequired["capo_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The start time of the analysis in the report.</p>"""
    end_time: NotRequired["capo_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The end time of the analysis in the report.</p>"""
    status: NotRequired["capo_pi.types.analysis_status.AnalysisStatus"]
    """<p>The status of the analysis report.</p>"""
    tags: NotRequired["capo_pi.types.tag_list.TagList"]
    """<p>List of all the tags added to the analysis report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalysisReportSummary) -> dict:
    out: dict = {}
    if "analysis_report_id" in value:
        out["AnalysisReportId"] = value["analysis_report_id"]
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
    if "tags" in value:
        import capo_pi.types.tag_list

        out["Tags"] = capo_pi.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalysisReportSummary:
    out: AnalysisReportSummary = {}  # type: ignore[typeddict-item]
    if data.get("AnalysisReportId") is not None:
        out["analysis_report_id"] = data["AnalysisReportId"]
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
    if data.get("Tags") is not None:
        import capo_pi.types.tag_list

        out["tags"] = capo_pi.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AnalysisReportSummary) -> dict:
    out: dict = {}
    if "analysis_report_id" in value:
        out["AnalysisReportId"] = value["analysis_report_id"]
    if "create_time" in value:
        import capo_pi.types.iso_timestamp

        out["CreateTime"] = capo_pi.types.iso_timestamp.serialize_cbor(
            value["create_time"]
        )
    if "start_time" in value:
        import capo_pi.types.iso_timestamp

        out["StartTime"] = capo_pi.types.iso_timestamp.serialize_cbor(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_pi.types.iso_timestamp

        out["EndTime"] = capo_pi.types.iso_timestamp.serialize_cbor(value["end_time"])
    if "status" in value:
        import capo_pi.types.analysis_status

        out["Status"] = capo_pi.types.analysis_status.serialize_cbor(value["status"])
    if "tags" in value:
        import capo_pi.types.tag_list

        out["Tags"] = capo_pi.types.tag_list.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> AnalysisReportSummary:
    out: AnalysisReportSummary = {}  # type: ignore[typeddict-item]
    if data.get("AnalysisReportId") is not None:
        out["analysis_report_id"] = data["AnalysisReportId"]
    if data.get("CreateTime") is not None:
        import capo_pi.types.iso_timestamp

        out["create_time"] = capo_pi.types.iso_timestamp.deserialize_cbor(
            data["CreateTime"]
        )
    if data.get("StartTime") is not None:
        import capo_pi.types.iso_timestamp

        out["start_time"] = capo_pi.types.iso_timestamp.deserialize_cbor(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_pi.types.iso_timestamp

        out["end_time"] = capo_pi.types.iso_timestamp.deserialize_cbor(data["EndTime"])
    if data.get("Status") is not None:
        import capo_pi.types.analysis_status

        out["status"] = capo_pi.types.analysis_status.deserialize_cbor(data["Status"])
    if data.get("Tags") is not None:
        import capo_pi.types.tag_list

        out["tags"] = capo_pi.types.tag_list.deserialize_cbor(data["Tags"])
    return out
