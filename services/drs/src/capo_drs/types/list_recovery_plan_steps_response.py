"""Generated from Smithy shape ``com.amazonaws.drs#ListRecoveryPlanStepsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.pagination_token
    import capo_drs.types.recovery_plan_step_list


class ListRecoveryPlanStepsResponse(TypedDict, closed=True):
    recovery_plan_steps: "capo_drs.types.recovery_plan_step_list.RecoveryPlanStepList"
    """<p>The list of Recovery Plan steps.</p>"""
    next_token: NotRequired["capo_drs.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecoveryPlanStepsResponse) -> dict:
    out: dict = {}
    import capo_drs.types.recovery_plan_step_list

    out["recoveryPlanSteps"] = capo_drs.types.recovery_plan_step_list.serialize_json(
        value["recovery_plan_steps"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecoveryPlanStepsResponse:
    out: ListRecoveryPlanStepsResponse = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanSteps") is not None:
        import capo_drs.types.recovery_plan_step_list

        out["recovery_plan_steps"] = (
            capo_drs.types.recovery_plan_step_list.deserialize_json(
                data["recoveryPlanSteps"]
            )
        )
    else:
        out["recovery_plan_steps"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
