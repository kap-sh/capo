"""Generated from Smithy shape ``com.amazonaws.sesv2#GetExportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.export_data_source
    import capo_sesv2.types.export_destination
    import capo_sesv2.types.export_source_type
    import capo_sesv2.types.export_statistics
    import capo_sesv2.types.failure_info
    import capo_sesv2.types.job_id
    import capo_sesv2.types.job_status
    import capo_sesv2.types.timestamp


class GetExportJobResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_sesv2.types.job_id.JobId"]
    """<p>The export job ID.</p>"""
    export_source_type: NotRequired[
        "capo_sesv2.types.export_source_type.ExportSourceType"
    ]
    """<p>The type of source of the export job.</p>"""
    job_status: NotRequired["capo_sesv2.types.job_status.JobStatus"]
    """<p>The status of the export job.</p>"""
    export_destination: NotRequired[
        "capo_sesv2.types.export_destination.ExportDestination"
    ]
    """<p>The destination of the export job. When <code>JobStatus</code> is <code>COMPLETED</code>, this object includes <code>S3Url</code>, a pre-signed URL that you use to download the export file.</p>"""
    export_data_source: NotRequired[
        "capo_sesv2.types.export_data_source.ExportDataSource"
    ]
    """<p>The data source of the export job.</p>"""
    created_timestamp: NotRequired["capo_sesv2.types.timestamp.Timestamp"]
    """<p>The timestamp of when the export job was created.</p>"""
    completed_timestamp: NotRequired["capo_sesv2.types.timestamp.Timestamp"]
    """<p>The timestamp of when the export job was completed.</p>"""
    failure_info: NotRequired["capo_sesv2.types.failure_info.FailureInfo"]
    """<p>The failure details about an export job.</p>"""
    statistics: NotRequired["capo_sesv2.types.export_statistics.ExportStatistics"]
    """<p>The statistics about the export job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExportJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "export_source_type" in value:
        import capo_sesv2.types.export_source_type

        out["ExportSourceType"] = capo_sesv2.types.export_source_type.serialize_json(
            value["export_source_type"]
        )
    if "job_status" in value:
        import capo_sesv2.types.job_status

        out["JobStatus"] = capo_sesv2.types.job_status.serialize_json(
            value["job_status"]
        )
    if "export_destination" in value:
        import capo_sesv2.types.export_destination

        out["ExportDestination"] = capo_sesv2.types.export_destination.serialize_json(
            value["export_destination"]
        )
    if "export_data_source" in value:
        import capo_sesv2.types.export_data_source

        out["ExportDataSource"] = capo_sesv2.types.export_data_source.serialize_json(
            value["export_data_source"]
        )
    if "created_timestamp" in value:
        import capo_sesv2.types.timestamp

        out["CreatedTimestamp"] = capo_sesv2.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "completed_timestamp" in value:
        import capo_sesv2.types.timestamp

        out["CompletedTimestamp"] = capo_sesv2.types.timestamp.serialize_json(
            value["completed_timestamp"]
        )
    if "failure_info" in value:
        import capo_sesv2.types.failure_info

        out["FailureInfo"] = capo_sesv2.types.failure_info.serialize_json(
            value["failure_info"]
        )
    if "statistics" in value:
        import capo_sesv2.types.export_statistics

        out["Statistics"] = capo_sesv2.types.export_statistics.serialize_json(
            value["statistics"]
        )
    return out


def deserialize_json(data: dict) -> GetExportJobResponse:
    out: GetExportJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("ExportSourceType") is not None:
        import capo_sesv2.types.export_source_type

        out["export_source_type"] = (
            capo_sesv2.types.export_source_type.deserialize_json(
                data["ExportSourceType"]
            )
        )
    if data.get("JobStatus") is not None:
        import capo_sesv2.types.job_status

        out["job_status"] = capo_sesv2.types.job_status.deserialize_json(
            data["JobStatus"]
        )
    if data.get("ExportDestination") is not None:
        import capo_sesv2.types.export_destination

        out["export_destination"] = (
            capo_sesv2.types.export_destination.deserialize_json(
                data["ExportDestination"]
            )
        )
    if data.get("ExportDataSource") is not None:
        import capo_sesv2.types.export_data_source

        out["export_data_source"] = (
            capo_sesv2.types.export_data_source.deserialize_json(
                data["ExportDataSource"]
            )
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_sesv2.types.timestamp

        out["created_timestamp"] = capo_sesv2.types.timestamp.deserialize_json(
            data["CreatedTimestamp"]
        )
    if data.get("CompletedTimestamp") is not None:
        import capo_sesv2.types.timestamp

        out["completed_timestamp"] = capo_sesv2.types.timestamp.deserialize_json(
            data["CompletedTimestamp"]
        )
    if data.get("FailureInfo") is not None:
        import capo_sesv2.types.failure_info

        out["failure_info"] = capo_sesv2.types.failure_info.deserialize_json(
            data["FailureInfo"]
        )
    if data.get("Statistics") is not None:
        import capo_sesv2.types.export_statistics

        out["statistics"] = capo_sesv2.types.export_statistics.deserialize_json(
            data["Statistics"]
        )
    return out
