"""Generated from Smithy shape ``com.amazonaws.drs#UpdateRecoveryPlanStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_step_configuration
    import capo_drs.types.recovery_plan_step_name
    import capo_drs.types.strict_drsarn


class UpdateRecoveryPlanStepRequest(TypedDict, closed=True):
    recovery_plan_step_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the Recovery Plan step to update.</p>"""
    step_name: NotRequired[
        "capo_drs.types.recovery_plan_step_name.RecoveryPlanStepName"
    ]
    configuration: NotRequired[
        "capo_drs.types.recovery_plan_step_configuration.RecoveryPlanStepConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecoveryPlanStepRequest) -> dict:
    out: dict = {}
    out["recoveryPlanStepArn"] = value["recovery_plan_step_arn"]
    if "step_name" in value:
        out["stepName"] = value["step_name"]
    if "configuration" in value:
        import capo_drs.types.recovery_plan_step_configuration

        out["configuration"] = (
            capo_drs.types.recovery_plan_step_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRecoveryPlanStepRequest:
    out: UpdateRecoveryPlanStepRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanStepArn") is not None:
        out["recovery_plan_step_arn"] = data["recoveryPlanStepArn"]
    else:
        out["recovery_plan_step_arn"] = ""
    if data.get("stepName") is not None:
        out["step_name"] = data["stepName"]
    if data.get("configuration") is not None:
        import capo_drs.types.recovery_plan_step_configuration

        out["configuration"] = (
            capo_drs.types.recovery_plan_step_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out
