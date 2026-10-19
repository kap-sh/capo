"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#CloudWatchLoggingOptionUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.id
    import capo_kinesis_analytics.types.log_stream_arn
    import capo_kinesis_analytics.types.role_arn


class CloudWatchLoggingOptionUpdate(TypedDict, closed=True):
    cloud_watch_logging_option_id: "capo_kinesis_analytics.types.id.Id"
    """<p>ID of the CloudWatch logging option to update</p>"""
    log_stream_arn_update: NotRequired[
        "capo_kinesis_analytics.types.log_stream_arn.LogStreamARN"
    ]
    """<p>ARN of the CloudWatch log to receive application messages.</p>"""
    role_arn_update: NotRequired["capo_kinesis_analytics.types.role_arn.RoleARN"]
    """<p>IAM ARN of the role to use to send application messages. Note: To write application messages to CloudWatch, the IAM role used must have the <code>PutLogEvents</code> policy action enabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLoggingOptionUpdate) -> dict:
    out: dict = {}
    out["CloudWatchLoggingOptionId"] = value["cloud_watch_logging_option_id"]
    if "log_stream_arn_update" in value:
        out["LogStreamARNUpdate"] = value["log_stream_arn_update"]
    if "role_arn_update" in value:
        out["RoleARNUpdate"] = value["role_arn_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchLoggingOptionUpdate:
    out: CloudWatchLoggingOptionUpdate = {}  # type: ignore[typeddict-item]
    if data.get("CloudWatchLoggingOptionId") is not None:
        out["cloud_watch_logging_option_id"] = data["CloudWatchLoggingOptionId"]
    else:
        out["cloud_watch_logging_option_id"] = ""
    if data.get("LogStreamARNUpdate") is not None:
        out["log_stream_arn_update"] = data["LogStreamARNUpdate"]
    if data.get("RoleARNUpdate") is not None:
        out["role_arn_update"] = data["RoleARNUpdate"]
    return out
