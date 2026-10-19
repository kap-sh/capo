"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanStep``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.iso8601_datetime_string
    import capo_drs.types.recovery_plan_step_configuration
    import capo_drs.types.recovery_plan_step_name
    import capo_drs.types.recovery_plan_step_order
    import capo_drs.types.strict_drsarn


class RecoveryPlanStep(TypedDict, closed=True):
    recovery_plan_step_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the Recovery Plan step.</p>"""
    step_order: "capo_drs.types.recovery_plan_step_order.RecoveryPlanStepOrder"
    step_name: "capo_drs.types.recovery_plan_step_name.RecoveryPlanStepName"
    configuration: (
        "capo_drs.types.recovery_plan_step_configuration.RecoveryPlanStepConfiguration"
    )
    created_at: "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    """<p>The timestamp when the step was created.</p>"""
    updated_at: "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    """<p>The timestamp when the step was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlanStep) -> dict:
    out: dict = {}
    out["recoveryPlanStepArn"] = value["recovery_plan_step_arn"]
    out["stepOrder"] = value["step_order"]
    out["stepName"] = value["step_name"]
    import capo_drs.types.recovery_plan_step_configuration

    out["configuration"] = (
        capo_drs.types.recovery_plan_step_configuration.serialize_json(
            value["configuration"]
        )
    )
    out["createdAt"] = value["created_at"]
    out["updatedAt"] = value["updated_at"]
    return out


def deserialize_json(data: dict) -> RecoveryPlanStep:
    out: RecoveryPlanStep = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanStepArn") is not None:
        out["recovery_plan_step_arn"] = data["recoveryPlanStepArn"]
    else:
        out["recovery_plan_step_arn"] = ""
    if data.get("stepOrder") is not None:
        out["step_order"] = data["stepOrder"]
    else:
        out["step_order"] = 0
    if data.get("stepName") is not None:
        out["step_name"] = data["stepName"]
    else:
        out["step_name"] = ""
    if data.get("configuration") is not None:
        import capo_drs.types.recovery_plan_step_configuration

        out["configuration"] = (
            capo_drs.types.recovery_plan_step_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        import capo_drs.types._unknown

        out["configuration"] = capo_drs.types._unknown.UnknownUnionMember("")
    if data.get("createdAt") is not None:
        out["created_at"] = data["createdAt"]
    else:
        out["created_at"] = ""
    if data.get("updatedAt") is not None:
        out["updated_at"] = data["updatedAt"]
    else:
        out["updated_at"] = ""
    return out
