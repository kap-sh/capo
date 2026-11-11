"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogGroupImpact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.retention_value
    import capo_cloudwatch_logs.types.stored_bytes


class LogGroupImpact(TypedDict, closed=True):
    log_group_name: NotRequired[
        "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    ]
    """<p>The name of the log group.</p>"""
    current_retention: NotRequired[
        "capo_cloudwatch_logs.types.retention_value.RetentionValue"
    ]
    """<p>The current effective retention period of the log group, in days. A value of <code>NEVER_EXPIRE</code> indicates that log events in the log group never expire.</p>"""
    proposed_retention: NotRequired[
        "capo_cloudwatch_logs.types.retention_value.RetentionValue"
    ]
    """<p>The effective retention period of the log group, in days, after the change. A value of <code>NEVER_EXPIRE</code> indicates that log events in the log group would never expire.</p>"""
    stored_bytes: NotRequired["capo_cloudwatch_logs.types.stored_bytes.StoredBytes"]
    """<p>The number of bytes stored in the log group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogGroupImpact) -> dict:
    out: dict = {}
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    if "current_retention" in value:
        out["currentRetention"] = value["current_retention"]
    if "proposed_retention" in value:
        out["proposedRetention"] = value["proposed_retention"]
    if "stored_bytes" in value:
        out["storedBytes"] = value["stored_bytes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LogGroupImpact:
    out: LogGroupImpact = {}  # type: ignore[typeddict-item]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    if data.get("currentRetention") is not None:
        out["current_retention"] = data["currentRetention"]
    if data.get("proposedRetention") is not None:
        out["proposed_retention"] = data["proposedRetention"]
    if data.get("storedBytes") is not None:
        out["stored_bytes"] = data["storedBytes"]
    return out
