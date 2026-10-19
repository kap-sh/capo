"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CancelExportTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.export_task_id


class CancelExportTaskRequest(TypedDict, closed=True):
    task_id: "capo_cloudwatch_logs.types.export_task_id.ExportTaskId"
    """<p>The ID of the export task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelExportTaskRequest) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelExportTaskRequest:
    out: CancelExportTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    else:
        out["task_id"] = ""
    return out
