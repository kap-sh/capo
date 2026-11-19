"""Generated from Smithy shape ``com.amazonaws.ssm#TargetsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.integer


class TargetsSummary(TypedDict, closed=True):
    total_count: "capo_ssm.types.integer.Integer"
    """<p>The total number of targets in the rate control execution.</p>"""
    started_count: "capo_ssm.types.integer.Integer"
    """<p>The number of child executions that started.</p>"""
    completed_count: "capo_ssm.types.integer.Integer"
    """<p>The number of child executions that finished, whether they succeeded or failed.</p>"""
    successful_count: "capo_ssm.types.integer.Integer"
    """<p>The number of child executions that succeeded.</p>"""
    failed_count: "capo_ssm.types.integer.Integer"
    """<p>The number of child executions that failed, timed out, or were canceled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetsSummary) -> dict:
    out: dict = {}
    out["TotalCount"] = value.get("total_count", 0)
    out["StartedCount"] = value.get("started_count", 0)
    out["CompletedCount"] = value.get("completed_count", 0)
    out["SuccessfulCount"] = value.get("successful_count", 0)
    out["FailedCount"] = value.get("failed_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetsSummary:
    out: TargetsSummary = {}  # type: ignore[typeddict-item]
    if data.get("TotalCount") is not None:
        out["total_count"] = data["TotalCount"]
    else:
        out["total_count"] = 0
    if data.get("StartedCount") is not None:
        out["started_count"] = data["StartedCount"]
    else:
        out["started_count"] = 0
    if data.get("CompletedCount") is not None:
        out["completed_count"] = data["CompletedCount"]
    else:
        out["completed_count"] = 0
    if data.get("SuccessfulCount") is not None:
        out["successful_count"] = data["SuccessfulCount"]
    else:
        out["successful_count"] = 0
    if data.get("FailedCount") is not None:
        out["failed_count"] = data["FailedCount"]
    else:
        out["failed_count"] = 0
    return out
