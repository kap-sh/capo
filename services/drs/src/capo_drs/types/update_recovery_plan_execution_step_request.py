"""Generated from Smithy shape ``com.amazonaws.drs#UpdateRecoveryPlanExecutionStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_execution_step_status
    import capo_drs.types.recovery_plan_servers
    import capo_drs.types.strict_drsarn
    import capo_drs.types.wait_duration_minutes


class UpdateRecoveryPlanExecutionStepRequest(TypedDict, closed=True):
    recovery_plan_execution_step_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the execution step to update.</p>"""
    status: NotRequired[
        "capo_drs.types.recovery_plan_execution_step_status.RecoveryPlanExecutionStepStatus"
    ]
    """Only SKIPPED is accepted. Step must be in NOT_STARTED or FAILED status."""
    servers: NotRequired["capo_drs.types.recovery_plan_servers.RecoveryPlanServers"]
    """Full replacement of the server list. Only allowed when the step is in NOT_STARTED status (Server type steps only)."""
    wait_duration_minutes: NotRequired[
        "capo_drs.types.wait_duration_minutes.WaitDurationMinutes"
    ]
    """Updated wait duration. Only allowed when the step is in NOT_STARTED status (Wait type steps only)."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecoveryPlanExecutionStepRequest) -> dict:
    out: dict = {}
    out["recoveryPlanExecutionStepArn"] = value["recovery_plan_execution_step_arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "servers" in value:
        import capo_drs.types.recovery_plan_servers

        out["servers"] = capo_drs.types.recovery_plan_servers.serialize_json(
            value["servers"]
        )
    if "wait_duration_minutes" in value:
        out["waitDurationMinutes"] = value["wait_duration_minutes"]
    return out


def deserialize_json(data: dict) -> UpdateRecoveryPlanExecutionStepRequest:
    out: UpdateRecoveryPlanExecutionStepRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanExecutionStepArn") is not None:
        out["recovery_plan_execution_step_arn"] = data["recoveryPlanExecutionStepArn"]
    else:
        out["recovery_plan_execution_step_arn"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("servers") is not None:
        import capo_drs.types.recovery_plan_servers

        out["servers"] = capo_drs.types.recovery_plan_servers.deserialize_json(
            data["servers"]
        )
    if data.get("waitDurationMinutes") is not None:
        out["wait_duration_minutes"] = data["waitDurationMinutes"]
    return out
