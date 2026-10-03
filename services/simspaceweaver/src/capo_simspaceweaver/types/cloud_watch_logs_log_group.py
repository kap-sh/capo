"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#CloudWatchLogsLogGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_simspaceweaver.types.log_group_arn


class CloudWatchLogsLogGroup(TypedDict, closed=True):
    log_group_arn: NotRequired["capo_simspaceweaver.types.log_group_arn.LogGroupArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log group for the simulation. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>. For more information about log groups, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html">Working with log groups and log streams</a> in the <i>Amazon CloudWatch Logs User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogsLogGroup) -> dict:
    out: dict = {}
    if "log_group_arn" in value:
        out["LogGroupArn"] = value["log_group_arn"]
    return out


def deserialize_json(data: dict) -> CloudWatchLogsLogGroup:
    out: CloudWatchLogsLogGroup = {}  # type: ignore[typeddict-item]
    if data.get("LogGroupArn") is not None:
        out["log_group_arn"] = data["LogGroupArn"]
    return out
