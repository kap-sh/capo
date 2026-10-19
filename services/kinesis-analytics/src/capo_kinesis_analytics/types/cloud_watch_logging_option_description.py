"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#CloudWatchLoggingOptionDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.id
    import capo_kinesis_analytics.types.log_stream_arn
    import capo_kinesis_analytics.types.role_arn


class CloudWatchLoggingOptionDescription(TypedDict, closed=True):
    cloud_watch_logging_option_id: NotRequired["capo_kinesis_analytics.types.id.Id"]
    """<p>ID of the CloudWatch logging option description.</p>"""
    log_stream_arn: "capo_kinesis_analytics.types.log_stream_arn.LogStreamARN"
    """<p>ARN of the CloudWatch log to receive application messages.</p>"""
    role_arn: "capo_kinesis_analytics.types.role_arn.RoleARN"
    """<p>IAM ARN of the role to use to send application messages. Note: To write application messages to CloudWatch, the IAM role used must have the <code>PutLogEvents</code> policy action enabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLoggingOptionDescription) -> dict:
    out: dict = {}
    if "cloud_watch_logging_option_id" in value:
        out["CloudWatchLoggingOptionId"] = value["cloud_watch_logging_option_id"]
    out["LogStreamARN"] = value["log_stream_arn"]
    out["RoleARN"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchLoggingOptionDescription:
    out: CloudWatchLoggingOptionDescription = {}  # type: ignore[typeddict-item]
    if data.get("CloudWatchLoggingOptionId") is not None:
        out["cloud_watch_logging_option_id"] = data["CloudWatchLoggingOptionId"]
    if data.get("LogStreamARN") is not None:
        out["log_stream_arn"] = data["LogStreamARN"]
    else:
        out["log_stream_arn"] = ""
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    else:
        out["role_arn"] = ""
    return out
