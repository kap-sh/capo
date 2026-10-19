"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateExportTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.export_destination_bucket
    import capo_cloudwatch_logs.types.export_destination_prefix
    import capo_cloudwatch_logs.types.export_task_name
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.log_stream_name
    import capo_cloudwatch_logs.types.timestamp

CreateExportTaskRequest = TypedDict(
    "CreateExportTaskRequest",
    {
        "task_name": NotRequired[
            "capo_cloudwatch_logs.types.export_task_name.ExportTaskName"
        ],
        "log_group_name": "capo_cloudwatch_logs.types.log_group_name.LogGroupName",
        "log_stream_name_prefix": NotRequired[
            "capo_cloudwatch_logs.types.log_stream_name.LogStreamName"
        ],
        "from": "capo_cloudwatch_logs.types.timestamp.Timestamp",
        "to": "capo_cloudwatch_logs.types.timestamp.Timestamp",
        "destination": "capo_cloudwatch_logs.types.export_destination_bucket.ExportDestinationBucket",
        "destination_prefix": NotRequired[
            "capo_cloudwatch_logs.types.export_destination_prefix.ExportDestinationPrefix"
        ],
    },
    closed=True,
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExportTaskRequest) -> dict:
    out: dict = {}
    if "task_name" in value:
        out["taskName"] = value["task_name"]
    out["logGroupName"] = value["log_group_name"]
    if "log_stream_name_prefix" in value:
        out["logStreamNamePrefix"] = value["log_stream_name_prefix"]
    out["from"] = value["from"]
    out["to"] = value["to"]
    out["destination"] = value["destination"]
    if "destination_prefix" in value:
        out["destinationPrefix"] = value["destination_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExportTaskRequest:
    out: CreateExportTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("taskName") is not None:
        out["task_name"] = data["taskName"]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    else:
        out["log_group_name"] = ""
    if data.get("logStreamNamePrefix") is not None:
        out["log_stream_name_prefix"] = data["logStreamNamePrefix"]
    if data.get("from") is not None:
        out["from"] = data["from"]
    else:
        out["from"] = 0
    if data.get("to") is not None:
        out["to"] = data["to"]
    else:
        out["to"] = 0
    if data.get("destination") is not None:
        out["destination"] = data["destination"]
    else:
        out["destination"] = ""
    if data.get("destinationPrefix") is not None:
        out["destination_prefix"] = data["destinationPrefix"]
    return out
