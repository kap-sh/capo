"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.log_group_class
    import capo_cloudwatch_logs.types.log_group_name


class LogGroupSummary(TypedDict, closed=True):
    log_group_name: NotRequired[
        "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    ]
    """<p>The name of the log group.</p>"""
    log_group_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the log group.</p>"""
    log_group_class: NotRequired[
        "capo_cloudwatch_logs.types.log_group_class.LogGroupClass"
    ]
    """<p>The log group class for this log group. For details about the features supported by each log group class, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html">Log classes</a> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogGroupSummary) -> dict:
    out: dict = {}
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    if "log_group_arn" in value:
        out["logGroupArn"] = value["log_group_arn"]
    if "log_group_class" in value:
        import capo_cloudwatch_logs.types.log_group_class

        out["logGroupClass"] = (
            capo_cloudwatch_logs.types.log_group_class.serialize_aws_json_1_1(
                value["log_group_class"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LogGroupSummary:
    out: LogGroupSummary = {}  # type: ignore[typeddict-item]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    if data.get("logGroupArn") is not None:
        out["log_group_arn"] = data["logGroupArn"]
    if data.get("logGroupClass") is not None:
        import capo_cloudwatch_logs.types.log_group_class

        out["log_group_class"] = (
            capo_cloudwatch_logs.types.log_group_class.deserialize_aws_json_1_1(
                data["logGroupClass"]
            )
        )
    return out
