"""Generated from Smithy shape ``com.amazonaws.drs#ReorderRecoveryPlanStepsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_step_list


class ReorderRecoveryPlanStepsResponse(TypedDict, closed=True):
    recovery_plan_steps: "capo_drs.types.recovery_plan_step_list.RecoveryPlanStepList"
    """<p>The steps with updated order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReorderRecoveryPlanStepsResponse) -> dict:
    out: dict = {}
    import capo_drs.types.recovery_plan_step_list

    out["recoveryPlanSteps"] = capo_drs.types.recovery_plan_step_list.serialize_json(
        value["recovery_plan_steps"]
    )
    return out


def deserialize_json(data: dict) -> ReorderRecoveryPlanStepsResponse:
    out: ReorderRecoveryPlanStepsResponse = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanSteps") is not None:
        import capo_drs.types.recovery_plan_step_list

        out["recovery_plan_steps"] = (
            capo_drs.types.recovery_plan_step_list.deserialize_json(
                data["recoveryPlanSteps"]
            )
        )
    else:
        out["recovery_plan_steps"] = []
    return out
