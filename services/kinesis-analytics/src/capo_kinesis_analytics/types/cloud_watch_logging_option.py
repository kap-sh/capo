"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#CloudWatchLoggingOption``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.log_stream_arn
    import capo_kinesis_analytics.types.role_arn


class CloudWatchLoggingOption(TypedDict, closed=True):
    log_stream_arn: "capo_kinesis_analytics.types.log_stream_arn.LogStreamARN"
    """<p>ARN of the CloudWatch log to receive application messages.</p>"""
    role_arn: "capo_kinesis_analytics.types.role_arn.RoleARN"
    """<p>IAM ARN of the role to use to send application messages. Note: To write application messages to CloudWatch, the IAM role that is used must have the <code>PutLogEvents</code> policy action enabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLoggingOption) -> dict:
    out: dict = {}
    out["LogStreamARN"] = value["log_stream_arn"]
    out["RoleARN"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchLoggingOption:
    out: CloudWatchLoggingOption = {}  # type: ignore[typeddict-item]
    if data.get("LogStreamARN") is not None:
        out["log_stream_arn"] = data["LogStreamARN"]
    else:
        out["log_stream_arn"] = ""
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    else:
        out["role_arn"] = ""
    return out
