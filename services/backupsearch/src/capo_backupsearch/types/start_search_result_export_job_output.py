"""Generated from Smithy shape ``com.amazonaws.backupsearch#StartSearchResultExportJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backupsearch.types.export_job_arn
    import capo_backupsearch.types.generic_id


class StartSearchResultExportJobOutput(TypedDict, closed=True):
    export_job_arn: NotRequired["capo_backupsearch.types.export_job_arn.ExportJobArn"]
    """<p>This is the unique ARN (Amazon Resource Name) that belongs to the new export job.</p>"""
    export_job_identifier: "capo_backupsearch.types.generic_id.GenericId"
    """<p>This is the unique identifier that specifies the new export job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSearchResultExportJobOutput) -> dict:
    out: dict = {}
    if "export_job_arn" in value:
        out["ExportJobArn"] = value["export_job_arn"]
    out["ExportJobIdentifier"] = value["export_job_identifier"]
    return out


def deserialize_json(data: dict) -> StartSearchResultExportJobOutput:
    out: StartSearchResultExportJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("ExportJobArn") is not None:
        out["export_job_arn"] = data["ExportJobArn"]
    if data.get("ExportJobIdentifier") is not None:
        out["export_job_identifier"] = data["ExportJobIdentifier"]
    else:
        out["export_job_identifier"] = ""
    return out
