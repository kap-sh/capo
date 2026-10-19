"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CloudWatchLoggingOptionUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.id
    import capo_kinesis_analytics_v2.types.log_stream_arn


class CloudWatchLoggingOptionUpdate(TypedDict, closed=True):
    cloud_watch_logging_option_id: "capo_kinesis_analytics_v2.types.id.Id"
    """<p>The ID of the CloudWatch logging option to update</p>"""
    log_stream_arn_update: NotRequired[
        "capo_kinesis_analytics_v2.types.log_stream_arn.LogStreamARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLoggingOptionUpdate) -> dict:
    out: dict = {}
    out["CloudWatchLoggingOptionId"] = value["cloud_watch_logging_option_id"]
    if "log_stream_arn_update" in value:
        out["LogStreamARNUpdate"] = value["log_stream_arn_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchLoggingOptionUpdate:
    out: CloudWatchLoggingOptionUpdate = {}  # type: ignore[typeddict-item]
    if data.get("CloudWatchLoggingOptionId") is not None:
        out["cloud_watch_logging_option_id"] = data["CloudWatchLoggingOptionId"]
    else:
        out["cloud_watch_logging_option_id"] = ""
    if data.get("LogStreamARNUpdate") is not None:
        out["log_stream_arn_update"] = data["LogStreamARNUpdate"]
    return out
