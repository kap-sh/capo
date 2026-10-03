"""Generated from Smithy shape ``com.amazonaws.sfn#LogDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.cloud_watch_logs_log_group


class LogDestination(TypedDict, closed=True):
    cloud_watch_logs_log_group: NotRequired[
        "capo_sfn.types.cloud_watch_logs_log_group.CloudWatchLogsLogGroup"
    ]
    """<p>An object describing a CloudWatch log group. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html">AWS::Logs::LogGroup</a> in the CloudFormation User Guide.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LogDestination) -> dict:
    out: dict = {}
    if "cloud_watch_logs_log_group" in value:
        import capo_sfn.types.cloud_watch_logs_log_group

        out["cloudWatchLogsLogGroup"] = (
            capo_sfn.types.cloud_watch_logs_log_group.serialize_aws_json_1_0(
                value["cloud_watch_logs_log_group"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LogDestination:
    out: LogDestination = {}  # type: ignore[typeddict-item]
    if data.get("cloudWatchLogsLogGroup") is not None:
        import capo_sfn.types.cloud_watch_logs_log_group

        out["cloud_watch_logs_log_group"] = (
            capo_sfn.types.cloud_watch_logs_log_group.deserialize_aws_json_1_0(
                data["cloudWatchLogsLogGroup"]
            )
        )
    return out
