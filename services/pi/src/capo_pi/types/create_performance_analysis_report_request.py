"""Generated from Smithy shape ``com.amazonaws.pi#CreatePerformanceAnalysisReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.identifier_string
    import capo_pi.types.iso_timestamp
    import capo_pi.types.service_type
    import capo_pi.types.tag_list


class CreatePerformanceAnalysisReportRequest(TypedDict, closed=True):
    service_type: "capo_pi.types.service_type.ServiceType"
    """<p>The Amazon Web Services service for which Performance Insights will return metrics. Valid value is <code>RDS</code>.</p>"""
    identifier: "capo_pi.types.identifier_string.IdentifierString"
    """<p>An immutable, Amazon Web Services Region-unique identifier for a data source. Performance Insights gathers metrics from this data source.</p> <p>To use an Amazon RDS instance as a data source, you specify its <code>DbiResourceId</code> value. For example, specify <code>db-ADECBTYHKTSAUMUZQYPDS2GW4A</code>.</p>"""
    start_time: "capo_pi.types.iso_timestamp.ISOTimestamp"
    """<p>The start time defined for the analysis report.</p>"""
    end_time: NotRequired["capo_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The end time defined for the analysis report.</p>"""
    tags: NotRequired["capo_pi.types.tag_list.TagList"]
    """<p>The metadata assigned to the analysis report consisting of a key-value pair.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePerformanceAnalysisReportRequest) -> dict:
    out: dict = {}
    import capo_pi.types.service_type

    out["ServiceType"] = capo_pi.types.service_type.serialize_aws_json_1_1(
        value["service_type"]
    )
    out["Identifier"] = value["identifier"]
    import capo_pi.types.iso_timestamp

    out["StartTime"] = capo_pi.types.iso_timestamp.serialize_aws_json_1_1(
        value["start_time"]
    )
    if "end_time" in value:
        import capo_pi.types.iso_timestamp

        out["EndTime"] = capo_pi.types.iso_timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "tags" in value:
        import capo_pi.types.tag_list

        out["Tags"] = capo_pi.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePerformanceAnalysisReportRequest:
    out: CreatePerformanceAnalysisReportRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceType") is not None:
        import capo_pi.types.service_type

        out["service_type"] = capo_pi.types.service_type.deserialize_aws_json_1_1(
            data["ServiceType"]
        )
    else:
        import typing

        out["service_type"] = typing.cast("capo_pi.types.service_type.ServiceType", "")
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("StartTime") is not None:
        import capo_pi.types.iso_timestamp

        out["start_time"] = capo_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndTime") is not None:
        import capo_pi.types.iso_timestamp

        out["end_time"] = capo_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("Tags") is not None:
        import capo_pi.types.tag_list

        out["tags"] = capo_pi.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
