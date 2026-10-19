"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanExecutionStepSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.error_detail
    import capo_drs.types.recovery_plan_execution_step_configuration
    import capo_drs.types.recovery_plan_execution_step_status
    import capo_drs.types.recovery_plan_step_name
    import capo_drs.types.recovery_plan_step_order
    import capo_drs.types.strict_drsarn


class RecoveryPlanExecutionStepSummary(TypedDict, closed=True):
    recovery_plan_execution_step_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the execution step.</p>"""
    step_name: "capo_drs.types.recovery_plan_step_name.RecoveryPlanStepName"
    step_index: "capo_drs.types.recovery_plan_step_order.RecoveryPlanStepOrder"
    status: "capo_drs.types.recovery_plan_execution_step_status.RecoveryPlanExecutionStepStatus"
    """<p>The status of the execution step.</p>"""
    configuration: "capo_drs.types.recovery_plan_execution_step_configuration.RecoveryPlanExecutionStepConfiguration"
    error_detail: NotRequired["capo_drs.types.error_detail.ErrorDetail"]
    """<p>Error details if the step failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlanExecutionStepSummary) -> dict:
    out: dict = {}
    out["recoveryPlanExecutionStepArn"] = value["recovery_plan_execution_step_arn"]
    out["stepName"] = value["step_name"]
    out["stepIndex"] = value["step_index"]
    out["status"] = value["status"]
    import capo_drs.types.recovery_plan_execution_step_configuration

    out["configuration"] = (
        capo_drs.types.recovery_plan_execution_step_configuration.serialize_json(
            value["configuration"]
        )
    )
    if "error_detail" in value:
        import capo_drs.types.error_detail

        out["errorDetail"] = capo_drs.types.error_detail.serialize_json(
            value["error_detail"]
        )
    return out


def deserialize_json(data: dict) -> RecoveryPlanExecutionStepSummary:
    out: RecoveryPlanExecutionStepSummary = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanExecutionStepArn") is not None:
        out["recovery_plan_execution_step_arn"] = data["recoveryPlanExecutionStepArn"]
    else:
        out["recovery_plan_execution_step_arn"] = ""
    if data.get("stepName") is not None:
        out["step_name"] = data["stepName"]
    else:
        out["step_name"] = ""
    if data.get("stepIndex") is not None:
        out["step_index"] = data["stepIndex"]
    else:
        out["step_index"] = 0
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("configuration") is not None:
        import capo_drs.types.recovery_plan_execution_step_configuration

        out["configuration"] = (
            capo_drs.types.recovery_plan_execution_step_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        import capo_drs.types._unknown

        out["configuration"] = capo_drs.types._unknown.UnknownUnionMember("")
    if data.get("errorDetail") is not None:
        import capo_drs.types.error_detail

        out["error_detail"] = capo_drs.types.error_detail.deserialize_json(
            data["errorDetail"]
        )
    return out
