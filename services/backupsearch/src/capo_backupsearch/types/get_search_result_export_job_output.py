"""Generated from Smithy shape ``com.amazonaws.backupsearch#GetSearchResultExportJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_backupsearch.types.export_job_arn
    import capo_backupsearch.types.export_job_status
    import capo_backupsearch.types.export_specification
    import capo_backupsearch.types.generic_id
    import capo_backupsearch.types.search_job_arn


class GetSearchResultExportJobOutput(TypedDict, closed=True):
    export_job_identifier: "capo_backupsearch.types.generic_id.GenericId"
    """<p>This is the unique string that identifies the specified export job.</p>"""
    export_job_arn: NotRequired["capo_backupsearch.types.export_job_arn.ExportJobArn"]
    """<p>The unique Amazon Resource Name (ARN) that uniquely identifies the export job.</p>"""
    status: NotRequired["capo_backupsearch.types.export_job_status.ExportJobStatus"]
    """<p>This is the current status of the export job.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The date and time that an export job was created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    completion_time: NotRequired["datetime.datetime"]
    """<p>The date and time that an export job completed, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    status_message: NotRequired["str"]
    """<p>A status message is a string that is returned for search job with a status of <code>FAILED</code>, along with steps to remedy and retry the operation.</p>"""
    export_specification: NotRequired[
        "capo_backupsearch.types.export_specification.ExportSpecification"
    ]
    """<p>The export specification consists of the destination S3 bucket to which the search results were exported, along with the destination prefix.</p>"""
    search_job_arn: NotRequired["capo_backupsearch.types.search_job_arn.SearchJobArn"]
    """<p>The unique string that identifies the Amazon Resource Name (ARN) of the specified search job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSearchResultExportJobOutput) -> dict:
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
    if "export_specification" in value:
        import capo_backupsearch.types.export_specification

        out["ExportSpecification"] = (
            capo_backupsearch.types.export_specification.serialize_json(
                value["export_specification"]
            )
        )
    if "search_job_arn" in value:
        out["SearchJobArn"] = value["search_job_arn"]
    return out


def deserialize_json(data: dict) -> GetSearchResultExportJobOutput:
    out: GetSearchResultExportJobOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("ExportSpecification") is not None:
        import capo_backupsearch.types.export_specification

        out["export_specification"] = (
            capo_backupsearch.types.export_specification.deserialize_json(
                data["ExportSpecification"]
            )
        )
    if data.get("SearchJobArn") is not None:
        out["search_job_arn"] = data["SearchJobArn"]
    return out
