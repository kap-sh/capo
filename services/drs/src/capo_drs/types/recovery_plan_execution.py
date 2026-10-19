"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanExecution``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.error_detail
    import capo_drs.types.iso8601_datetime_string
    import capo_drs.types.recovery_plan_execution_mode
    import capo_drs.types.recovery_plan_execution_status
    import capo_drs.types.strict_drsarn
    import capo_drs.types.tags_map


class RecoveryPlanExecution(TypedDict, closed=True):
    recovery_plan_execution_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the Recovery Plan execution.</p>"""
    recovery_plan_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the Recovery Plan being executed.</p>"""
    mode: "capo_drs.types.recovery_plan_execution_mode.RecoveryPlanExecutionMode"
    """<p>The execution mode.</p>"""
    status: "capo_drs.types.recovery_plan_execution_status.RecoveryPlanExecutionStatus"
    """<p>The execution status.</p>"""
    started_at: "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    """<p>The timestamp when the execution started.</p>"""
    completed_at: NotRequired[
        "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>The timestamp when the execution completed.</p>"""
    error_detail: NotRequired["capo_drs.types.error_detail.ErrorDetail"]
    """<p>Error details if the execution failed.</p>"""
    tags: NotRequired["capo_drs.types.tags_map.TagsMap"]
    """<p>The tags associated with the Recovery Plan execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlanExecution) -> dict:
    out: dict = {}
    out["recoveryPlanExecutionArn"] = value["recovery_plan_execution_arn"]
    out["recoveryPlanArn"] = value["recovery_plan_arn"]
    out["mode"] = value["mode"]
    out["status"] = value["status"]
    out["startedAt"] = value["started_at"]
    if "completed_at" in value:
        out["completedAt"] = value["completed_at"]
    if "error_detail" in value:
        import capo_drs.types.error_detail

        out["errorDetail"] = capo_drs.types.error_detail.serialize_json(
            value["error_detail"]
        )
    if "tags" in value:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RecoveryPlanExecution:
    out: RecoveryPlanExecution = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanExecutionArn") is not None:
        out["recovery_plan_execution_arn"] = data["recoveryPlanExecutionArn"]
    else:
        out["recovery_plan_execution_arn"] = ""
    if data.get("recoveryPlanArn") is not None:
        out["recovery_plan_arn"] = data["recoveryPlanArn"]
    else:
        out["recovery_plan_arn"] = ""
    if data.get("mode") is not None:
        out["mode"] = data["mode"]
    else:
        out["mode"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("startedAt") is not None:
        out["started_at"] = data["startedAt"]
    else:
        out["started_at"] = ""
    if data.get("completedAt") is not None:
        out["completed_at"] = data["completedAt"]
    if data.get("errorDetail") is not None:
        import capo_drs.types.error_detail

        out["error_detail"] = capo_drs.types.error_detail.deserialize_json(
            data["errorDetail"]
        )
    if data.get("tags") is not None:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: RecoveryPlanExecution) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
