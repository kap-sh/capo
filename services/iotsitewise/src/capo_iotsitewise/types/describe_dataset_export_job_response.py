"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeDatasetExportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_iotsitewise.types.dataset_export_job_id
    import capo_iotsitewise.types.dataset_export_job_status
    import capo_iotsitewise.types.export_error_report_location
    import capo_iotsitewise.types.processing_input
    import capo_iotsitewise.types.s3_uri
    import capo_iotsitewise.types.workspace_name


class DescribeDatasetExportJobResponse(TypedDict, closed=True):
    job_id: "capo_iotsitewise.types.dataset_export_job_id.DatasetExportJobId"
    """<p>The unique identifier for the dataset export job.</p>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace that contains the dataset export job.</p>"""
    status: "capo_iotsitewise.types.dataset_export_job_status.DatasetExportJobStatus"
    """<p>The current status of the dataset export job.</p>"""
    started_at: "datetime.datetime"
    """<p>The timestamp when the job started processing.</p>"""
    completed_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the job completed, or null if the job is still running.</p>"""
    destination_s3_uri: "capo_iotsitewise.types.s3_uri.S3Uri"
    """<p>The S3 URI where output clips are written.</p>"""
    error_report_location: (
        "capo_iotsitewise.types.export_error_report_location.ExportErrorReportLocation"
    )
    """<p>The location where the error report will be written on failure.</p>"""
    input: "capo_iotsitewise.types.processing_input.ProcessingInput"
    """<p>The processing input that was provided in the CreateDatasetExportJob request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDatasetExportJobResponse) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["workspaceName"] = value["workspace_name"]
    import capo_iotsitewise.types.dataset_export_job_status

    out["status"] = capo_iotsitewise.types.dataset_export_job_status.serialize_json(
        value["status"]
    )
    import capo_iotsitewise.types._prelude.timestamp

    out["startedAt"] = capo_iotsitewise.types._prelude.timestamp.serialize_json(
        value["started_at"]
    )
    if "completed_at" in value:
        import capo_iotsitewise.types._prelude.timestamp

        out["completedAt"] = capo_iotsitewise.types._prelude.timestamp.serialize_json(
            value["completed_at"]
        )
    out["destinationS3Uri"] = value["destination_s3_uri"]
    import capo_iotsitewise.types.export_error_report_location

    out["errorReportLocation"] = (
        capo_iotsitewise.types.export_error_report_location.serialize_json(
            value["error_report_location"]
        )
    )
    import capo_iotsitewise.types.processing_input

    out["input"] = capo_iotsitewise.types.processing_input.serialize_json(
        value["input"]
    )
    return out


def deserialize_json(data: dict) -> DescribeDatasetExportJobResponse:
    out: DescribeDatasetExportJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    else:
        out["workspace_name"] = ""
    if data.get("status") is not None:
        import capo_iotsitewise.types.dataset_export_job_status

        out["status"] = (
            capo_iotsitewise.types.dataset_export_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_iotsitewise.types.dataset_export_job_status.DatasetExportJobStatus",
            "",
        )
    if data.get("startedAt") is not None:
        import capo_iotsitewise.types._prelude.timestamp

        out["started_at"] = capo_iotsitewise.types._prelude.timestamp.deserialize_json(
            data["startedAt"]
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("completedAt") is not None:
        import capo_iotsitewise.types._prelude.timestamp

        out["completed_at"] = (
            capo_iotsitewise.types._prelude.timestamp.deserialize_json(
                data["completedAt"]
            )
        )
    if data.get("destinationS3Uri") is not None:
        out["destination_s3_uri"] = data["destinationS3Uri"]
    else:
        out["destination_s3_uri"] = ""
    if data.get("errorReportLocation") is not None:
        import capo_iotsitewise.types.export_error_report_location

        out["error_report_location"] = (
            capo_iotsitewise.types.export_error_report_location.deserialize_json(
                data["errorReportLocation"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeDatasetExportJobResponse.error_report_location required"
        )
    if data.get("input") is not None:
        import capo_iotsitewise.types.processing_input

        out["input"] = capo_iotsitewise.types.processing_input.deserialize_json(
            data["input"]
        )
    else:
        import capo_iotsitewise.types._unknown

        out["input"] = capo_iotsitewise.types._unknown.UnknownUnionMember("")
    return out
