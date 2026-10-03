"""Generated from Smithy shape ``com.amazonaws.codebuild#CloudWatchLogsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codebuild.types.logs_config_status_type
    import capo_codebuild.types.string


class CloudWatchLogsConfig(TypedDict, closed=True):
    status: "capo_codebuild.types.logs_config_status_type.LogsConfigStatusType"
    """<p>The current status of the logs in CloudWatch Logs for a build project. Valid values are:</p> <ul> <li> <p> <code>ENABLED</code>: CloudWatch Logs are enabled for this build project.</p> </li> <li> <p> <code>DISABLED</code>: CloudWatch Logs are not enabled for this build project.</p> </li> </ul>"""
    group_name: NotRequired["capo_codebuild.types.string.String"]
    """<p> The group name of the logs in CloudWatch Logs. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html">Working with Log Groups and Log Streams</a>. </p>"""
    stream_name: NotRequired["capo_codebuild.types.string.String"]
    """<p> The prefix of the stream name of the CloudWatch Logs. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html">Working with Log Groups and Log Streams</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLogsConfig) -> dict:
    out: dict = {}
    import capo_codebuild.types.logs_config_status_type

    out["status"] = capo_codebuild.types.logs_config_status_type.serialize_aws_json_1_1(
        value["status"]
    )
    if "group_name" in value:
        out["groupName"] = value["group_name"]
    if "stream_name" in value:
        out["streamName"] = value["stream_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchLogsConfig:
    out: CloudWatchLogsConfig = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_codebuild.types.logs_config_status_type

        out["status"] = (
            capo_codebuild.types.logs_config_status_type.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CloudWatchLogsConfig.status required")
    if data.get("groupName") is not None:
        out["group_name"] = data["groupName"]
    if data.get("streamName") is not None:
        out["stream_name"] = data["streamName"]
    return out
