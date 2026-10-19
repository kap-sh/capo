"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ImportBatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.batch_id
    import capo_cloudwatch_logs.types.error_message
    import capo_cloudwatch_logs.types.import_status


class ImportBatch(TypedDict, closed=True):
    batch_id: "capo_cloudwatch_logs.types.batch_id.BatchId"
    """<p>The unique identifier of the import batch.</p>"""
    status: "capo_cloudwatch_logs.types.import_status.ImportStatus"
    """<p>The current status of the import batch. Valid values are IN_PROGRESS, CANCELLED, COMPLETED and FAILED.</p>"""
    error_message: NotRequired["capo_cloudwatch_logs.types.error_message.ErrorMessage"]
    """<p>The error message if the batch failed to import. Only present when status is FAILED.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportBatch) -> dict:
    out: dict = {}
    out["batchId"] = value["batch_id"]
    import capo_cloudwatch_logs.types.import_status

    out["status"] = capo_cloudwatch_logs.types.import_status.serialize_aws_json_1_1(
        value["status"]
    )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportBatch:
    out: ImportBatch = {}  # type: ignore[typeddict-item]
    if data.get("batchId") is not None:
        out["batch_id"] = data["batchId"]
    else:
        out["batch_id"] = ""
    if data.get("status") is not None:
        import capo_cloudwatch_logs.types.import_status

        out["status"] = (
            capo_cloudwatch_logs.types.import_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cloudwatch_logs.types.import_status.ImportStatus", ""
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
