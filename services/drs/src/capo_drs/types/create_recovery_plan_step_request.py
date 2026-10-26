"""Generated from Smithy shape ``com.amazonaws.drs#CreateRecoveryPlanStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.client_idempotency_token
    import capo_drs.types.recovery_plan_step_configuration
    import capo_drs.types.recovery_plan_step_name
    import capo_drs.types.recovery_plan_step_order
    import capo_drs.types.strict_drsarn


class CreateRecoveryPlanStepRequest(TypedDict, closed=True):
    recovery_plan_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the Recovery Plan to add the step to.</p>"""
    step_name: "capo_drs.types.recovery_plan_step_name.RecoveryPlanStepName"
    step_order: NotRequired[
        "capo_drs.types.recovery_plan_step_order.RecoveryPlanStepOrder"
    ]
    configuration: (
        "capo_drs.types.recovery_plan_step_configuration.RecoveryPlanStepConfiguration"
    )
    client_token: NotRequired[
        "capo_drs.types.client_idempotency_token.ClientIdempotencyToken"
    ]
    """<p>A unique string provided to ensure request idempotency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecoveryPlanStepRequest) -> dict:
    out: dict = {}
    out["recoveryPlanArn"] = value["recovery_plan_arn"]
    out["stepName"] = value["step_name"]
    if "step_order" in value:
        out["stepOrder"] = value["step_order"]
    import capo_drs.types.recovery_plan_step_configuration

    out["configuration"] = (
        capo_drs.types.recovery_plan_step_configuration.serialize_json(
            value["configuration"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateRecoveryPlanStepRequest:
    out: CreateRecoveryPlanStepRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanArn") is not None:
        out["recovery_plan_arn"] = data["recoveryPlanArn"]
    else:
        out["recovery_plan_arn"] = ""
    if data.get("stepName") is not None:
        out["step_name"] = data["stepName"]
    else:
        out["step_name"] = ""
    if data.get("stepOrder") is not None:
        out["step_order"] = data["stepOrder"]
    if data.get("configuration") is not None:
        import capo_drs.types.recovery_plan_step_configuration

        out["configuration"] = (
            capo_drs.types.recovery_plan_step_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        out["configuration"] = {"$unknown": {"name": ""}}
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
