"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#LogDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_simspaceweaver.types.cloud_watch_logs_log_group


class LogDestination(TypedDict, closed=True):
    cloud_watch_logs_log_group: NotRequired[
        "capo_simspaceweaver.types.cloud_watch_logs_log_group.CloudWatchLogsLogGroup"
    ]
    """<p>An Amazon CloudWatch Logs log group that stores simulation log data. For more information about log groups, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html">Working with log groups and log streams</a> in the <i>Amazon CloudWatch Logs User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogDestination) -> dict:
    out: dict = {}
    if "cloud_watch_logs_log_group" in value:
        import capo_simspaceweaver.types.cloud_watch_logs_log_group

        out["CloudWatchLogsLogGroup"] = (
            capo_simspaceweaver.types.cloud_watch_logs_log_group.serialize_json(
                value["cloud_watch_logs_log_group"]
            )
        )
    return out


def deserialize_json(data: dict) -> LogDestination:
    out: LogDestination = {}  # type: ignore[typeddict-item]
    if data.get("CloudWatchLogsLogGroup") is not None:
        import capo_simspaceweaver.types.cloud_watch_logs_log_group

        out["cloud_watch_logs_log_group"] = (
            capo_simspaceweaver.types.cloud_watch_logs_log_group.deserialize_json(
                data["CloudWatchLogsLogGroup"]
            )
        )
    return out
