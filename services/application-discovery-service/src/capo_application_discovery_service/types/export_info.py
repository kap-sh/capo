"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ExportInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.boolean
    import capo_application_discovery_service.types.configurations_download_url
    import capo_application_discovery_service.types.configurations_export_id
    import capo_application_discovery_service.types.export_request_time
    import capo_application_discovery_service.types.export_status
    import capo_application_discovery_service.types.export_status_message
    import capo_application_discovery_service.types.time_stamp


class ExportInfo(TypedDict, closed=True):
    export_id: "capo_application_discovery_service.types.configurations_export_id.ConfigurationsExportId"
    """<p>A unique identifier used to query an export.</p>"""
    export_status: "capo_application_discovery_service.types.export_status.ExportStatus"
    """<p>The status of the data export job.</p>"""
    status_message: "capo_application_discovery_service.types.export_status_message.ExportStatusMessage"
    """<p>A status message provided for API callers.</p>"""
    configurations_download_url: NotRequired[
        "capo_application_discovery_service.types.configurations_download_url.ConfigurationsDownloadUrl"
    ]
    """<p>A URL for an Amazon S3 bucket where you can review the exported data. The URL is displayed only if the export succeeded.</p>"""
    export_request_time: (
        "capo_application_discovery_service.types.export_request_time.ExportRequestTime"
    )
    """<p>The time that the data export was initiated.</p>"""
    is_truncated: "capo_application_discovery_service.types.boolean.Boolean"
    """<p>If true, the export of agent information exceeded the size limit for a single export and the exported data is incomplete for the requested time range. To address this, select a smaller time range for the export by using <code>startDate</code> and <code>endDate</code>.</p>"""
    requested_start_time: NotRequired[
        "capo_application_discovery_service.types.time_stamp.TimeStamp"
    ]
    """<p>The value of <code>startTime</code> parameter in the <code>StartExportTask</code> request. If no <code>startTime</code> was requested, this result does not appear in <code>ExportInfo</code>.</p>"""
    requested_end_time: NotRequired[
        "capo_application_discovery_service.types.time_stamp.TimeStamp"
    ]
    """<p>The <code>endTime</code> used in the <code>StartExportTask</code> request. If no <code>endTime</code> was requested, this result does not appear in <code>ExportInfo</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportInfo) -> dict:
    out: dict = {}
    out["exportId"] = value["export_id"]
    import capo_application_discovery_service.types.export_status

    out["exportStatus"] = (
        capo_application_discovery_service.types.export_status.serialize_aws_json_1_1(
            value["export_status"]
        )
    )
    out["statusMessage"] = value["status_message"]
    if "configurations_download_url" in value:
        out["configurationsDownloadUrl"] = value["configurations_download_url"]
    import capo_application_discovery_service.types.export_request_time

    out["exportRequestTime"] = (
        capo_application_discovery_service.types.export_request_time.serialize_aws_json_1_1(
            value["export_request_time"]
        )
    )
    out["isTruncated"] = value.get("is_truncated", False)
    if "requested_start_time" in value:
        import capo_application_discovery_service.types.time_stamp

        out["requestedStartTime"] = (
            capo_application_discovery_service.types.time_stamp.serialize_aws_json_1_1(
                value["requested_start_time"]
            )
        )
    if "requested_end_time" in value:
        import capo_application_discovery_service.types.time_stamp

        out["requestedEndTime"] = (
            capo_application_discovery_service.types.time_stamp.serialize_aws_json_1_1(
                value["requested_end_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportInfo:
    out: ExportInfo = {}  # type: ignore[typeddict-item]
    if data.get("exportId") is not None:
        out["export_id"] = data["exportId"]
    else:
        out["export_id"] = ""
    if data.get("exportStatus") is not None:
        import capo_application_discovery_service.types.export_status

        out["export_status"] = (
            capo_application_discovery_service.types.export_status.deserialize_aws_json_1_1(
                data["exportStatus"]
            )
        )
    else:
        import typing

        out["export_status"] = typing.cast(
            "capo_application_discovery_service.types.export_status.ExportStatus", ""
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    else:
        out["status_message"] = ""
    if data.get("configurationsDownloadUrl") is not None:
        out["configurations_download_url"] = data["configurationsDownloadUrl"]
    if data.get("exportRequestTime") is not None:
        import capo_application_discovery_service.types.export_request_time

        out["export_request_time"] = (
            capo_application_discovery_service.types.export_request_time.deserialize_aws_json_1_1(
                data["exportRequestTime"]
            )
        )
    else:
        import datetime

        out["export_request_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("isTruncated") is not None:
        out["is_truncated"] = data["isTruncated"]
    else:
        out["is_truncated"] = False
    if data.get("requestedStartTime") is not None:
        import capo_application_discovery_service.types.time_stamp

        out["requested_start_time"] = (
            capo_application_discovery_service.types.time_stamp.deserialize_aws_json_1_1(
                data["requestedStartTime"]
            )
        )
    if data.get("requestedEndTime") is not None:
        import capo_application_discovery_service.types.time_stamp

        out["requested_end_time"] = (
            capo_application_discovery_service.types.time_stamp.deserialize_aws_json_1_1(
                data["requestedEndTime"]
            )
        )
    return out
