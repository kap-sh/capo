"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CloudWatchLoggingOption``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.log_stream_arn


class CloudWatchLoggingOption(TypedDict, closed=True):
    log_stream_arn: "capo_kinesis_analytics_v2.types.log_stream_arn.LogStreamARN"
    """<p>The ARN of the CloudWatch log to receive application messages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLoggingOption) -> dict:
    out: dict = {}
    out["LogStreamARN"] = value["log_stream_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchLoggingOption:
    out: CloudWatchLoggingOption = {}  # type: ignore[typeddict-item]
    if data.get("LogStreamARN") is not None:
        out["log_stream_arn"] = data["LogStreamARN"]
    else:
        out["log_stream_arn"] = ""
    return out
