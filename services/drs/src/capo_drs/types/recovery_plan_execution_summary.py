"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.error_detail
    import capo_drs.types.iso8601_datetime_string
    import capo_drs.types.recovery_plan_execution_mode
    import capo_drs.types.recovery_plan_execution_status
    import capo_drs.types.strict_drsarn


class RecoveryPlanExecutionSummary(TypedDict, closed=True):
    recovery_plan_execution_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the Recovery Plan execution.</p>"""
    recovery_plan_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the Recovery Plan.</p>"""
    mode: "capo_drs.types.recovery_plan_execution_mode.RecoveryPlanExecutionMode"
    """<p>The execution mode.</p>"""
    status: "capo_drs.types.recovery_plan_execution_status.RecoveryPlanExecutionStatus"
    """<p>The execution status.</p>"""
    started_at: "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    """<p>The timestamp when the execution started.</p>"""
    error_detail: NotRequired["capo_drs.types.error_detail.ErrorDetail"]
    """<p>Error details if the execution failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlanExecutionSummary) -> dict:
    out: dict = {}
    out["recoveryPlanExecutionArn"] = value["recovery_plan_execution_arn"]
    out["recoveryPlanArn"] = value["recovery_plan_arn"]
    out["mode"] = value["mode"]
    out["status"] = value["status"]
    out["startedAt"] = value["started_at"]
    if "error_detail" in value:
        import capo_drs.types.error_detail

        out["errorDetail"] = capo_drs.types.error_detail.serialize_json(
            value["error_detail"]
        )
    return out


def deserialize_json(data: dict) -> RecoveryPlanExecutionSummary:
    out: RecoveryPlanExecutionSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("errorDetail") is not None:
        import capo_drs.types.error_detail

        out["error_detail"] = capo_drs.types.error_detail.deserialize_json(
            data["errorDetail"]
        )
    return out
