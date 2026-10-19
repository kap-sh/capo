"""Generated from Smithy shape ``com.amazonaws.backupsearch#ExportJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_backupsearch.types.export_job_arn
    import capo_backupsearch.types.export_job_status
    import capo_backupsearch.types.generic_id
    import capo_backupsearch.types.search_job_arn


class ExportJobSummary(TypedDict, closed=True):
    export_job_identifier: "capo_backupsearch.types.generic_id.GenericId"
    """<p>This is the unique string that identifies a specific export job.</p>"""
    export_job_arn: NotRequired["capo_backupsearch.types.export_job_arn.ExportJobArn"]
    """<p>This is the unique ARN (Amazon Resource Name) that belongs to the new export job.</p>"""
    status: NotRequired["capo_backupsearch.types.export_job_status.ExportJobStatus"]
    """<p>The status of the export job is one of the following:</p> <p> <code>CREATED</code>; <code>RUNNING</code>; <code>FAILED</code>; or <code>COMPLETED</code>.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>This is a timestamp of the time the export job was created.</p>"""
    completion_time: NotRequired["datetime.datetime"]
    """<p>This is a timestamp of the time the export job compeleted.</p>"""
    status_message: NotRequired["str"]
    """<p>A status message is a string that is returned for an export job.</p> <p>A status message is included for any status other than <code>COMPLETED</code> without issues.</p>"""
    search_job_arn: NotRequired["capo_backupsearch.types.search_job_arn.SearchJobArn"]
    """<p>The unique string that identifies the Amazon Resource Name (ARN) of the specified search job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportJobSummary) -> dict:
    out: dict = {}
    out["ExportJobIdentifier"] = value["export_job_identifier"]
    if "export_job_arn" in value:
        out["ExportJobArn"] = value["export_job_arn"]
    if "status" in value:
        import capo_backupsearch.types.export_job_status

        out["Status"] = capo_backupsearch.types.export_job_status.serialize_json(
            value["status"]
        )
    if "creation_time" in value:
        import capo_backupsearch.types._prelude.timestamp

        out["CreationTime"] = capo_backupsearch.types._prelude.timestamp.serialize_json(
            value["creation_time"]
        )
    if "completion_time" in value:
        import capo_backupsearch.types._prelude.timestamp

        out["CompletionTime"] = (
            capo_backupsearch.types._prelude.timestamp.serialize_json(
                value["completion_time"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "search_job_arn" in value:
        out["SearchJobArn"] = value["search_job_arn"]
    return out


def deserialize_json(data: dict) -> ExportJobSummary:
    out: ExportJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("ExportJobIdentifier") is not None:
        out["export_job_identifier"] = data["ExportJobIdentifier"]
    else:
        out["export_job_identifier"] = ""
    if data.get("ExportJobArn") is not None:
        out["export_job_arn"] = data["ExportJobArn"]
    if data.get("Status") is not None:
        import capo_backupsearch.types.export_job_status

        out["status"] = capo_backupsearch.types.export_job_status.deserialize_json(
            data["Status"]
        )
    if data.get("CreationTime") is not None:
        import capo_backupsearch.types._prelude.timestamp

        out["creation_time"] = (
            capo_backupsearch.types._prelude.timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    if data.get("CompletionTime") is not None:
        import capo_backupsearch.types._prelude.timestamp

        out["completion_time"] = (
            capo_backupsearch.types._prelude.timestamp.deserialize_json(
                data["CompletionTime"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("SearchJobArn") is not None:
        out["search_job_arn"] = data["SearchJobArn"]
    return out
