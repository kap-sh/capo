"""Generated from Smithy shape ``com.amazonaws.iot#CloudwatchLogsAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.batch_mode
    import capo_iot.types.log_group_name


class CloudwatchLogsAction(TypedDict, closed=True):
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The IAM role that allows access to the CloudWatch log.</p>"""
    log_group_name: "capo_iot.types.log_group_name.LogGroupName"
    """<p>The CloudWatch log group to which the action sends data.</p>"""
    batch_mode: NotRequired["capo_iot.types.batch_mode.BatchMode"]
    """<p>Indicates whether batches of log records will be extracted and uploaded into CloudWatch. Values include <code>true</code> or <code>false</code> <i>(default)</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudwatchLogsAction) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["logGroupName"] = value["log_group_name"]
    if "batch_mode" in value:
        out["batchMode"] = value["batch_mode"]
    return out


def deserialize_json(data: dict) -> CloudwatchLogsAction:
    out: CloudwatchLogsAction = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    else:
        out["log_group_name"] = ""
    if data.get("batchMode") is not None:
        out["batch_mode"] = data["batchMode"]
    return out
