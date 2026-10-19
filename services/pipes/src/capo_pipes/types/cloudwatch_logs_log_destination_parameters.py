"""Generated from Smithy shape ``com.amazonaws.pipes#CloudwatchLogsLogDestinationParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.cloudwatch_log_group_arn


class CloudwatchLogsLogDestinationParameters(TypedDict, closed=True):
    log_group_arn: "capo_pipes.types.cloudwatch_log_group_arn.CloudwatchLogGroupArn"
    """<p>The Amazon Web Services Resource Name (ARN) for the CloudWatch log group to which EventBridge sends the log records.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudwatchLogsLogDestinationParameters) -> dict:
    out: dict = {}
    out["LogGroupArn"] = value["log_group_arn"]
    return out


def deserialize_json(data: dict) -> CloudwatchLogsLogDestinationParameters:
    out: CloudwatchLogsLogDestinationParameters = {}  # type: ignore[typeddict-item]
    if data.get("LogGroupArn") is not None:
        out["log_group_arn"] = data["LogGroupArn"]
    else:
        out["log_group_arn"] = ""
    return out
