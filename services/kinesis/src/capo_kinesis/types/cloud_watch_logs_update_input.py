"""Generated from Smithy shape ``com.amazonaws.kinesis#CloudWatchLogsUpdateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.boolean_object
    import capo_kinesis.types.cloud_watch_log_group_name
    import capo_kinesis.types.cloud_watch_log_stream_name


class CloudWatchLogsUpdateInput(TypedDict, closed=True):
    enabled: "capo_kinesis.types.boolean_object.BooleanObject"
    """<p>Specifies whether logging to Amazon CloudWatch Logs is enabled.</p>"""
    log_group_name: NotRequired[
        "capo_kinesis.types.cloud_watch_log_group_name.CloudWatchLogGroupName"
    ]
    """<p>The name of the Amazon CloudWatch Logs log group.</p>"""
    log_stream_name: NotRequired[
        "capo_kinesis.types.cloud_watch_log_stream_name.CloudWatchLogStreamName"
    ]
    """<p>The name of the Amazon CloudWatch Logs log stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLogsUpdateInput) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    if "log_group_name" in value:
        out["LogGroupName"] = value["log_group_name"]
    if "log_stream_name" in value:
        out["LogStreamName"] = value["log_stream_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchLogsUpdateInput:
    out: CloudWatchLogsUpdateInput = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if data.get("LogGroupName") is not None:
        out["log_group_name"] = data["LogGroupName"]
    if data.get("LogStreamName") is not None:
        out["log_stream_name"] = data["LogStreamName"]
    return out
