"""Generated from Smithy shape ``com.amazonaws.drs#ListRecoveryPlanExecutionStepsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.pagination_token
    import capo_drs.types.recovery_plan_execution_step_summary_list


class ListRecoveryPlanExecutionStepsResponse(TypedDict, closed=True):
    recovery_plan_execution_steps: "capo_drs.types.recovery_plan_execution_step_summary_list.RecoveryPlanExecutionStepSummaryList"
    """<p>The list of execution steps.</p>"""
    next_token: NotRequired["capo_drs.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecoveryPlanExecutionStepsResponse) -> dict:
    out: dict = {}
    import capo_drs.types.recovery_plan_execution_step_summary_list

    out["recoveryPlanExecutionSteps"] = (
        capo_drs.types.recovery_plan_execution_step_summary_list.serialize_json(
            value["recovery_plan_execution_steps"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecoveryPlanExecutionStepsResponse:
    out: ListRecoveryPlanExecutionStepsResponse = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanExecutionSteps") is not None:
        import capo_drs.types.recovery_plan_execution_step_summary_list

        out["recovery_plan_execution_steps"] = (
            capo_drs.types.recovery_plan_execution_step_summary_list.deserialize_json(
                data["recoveryPlanExecutionSteps"]
            )
        )
    else:
        out["recovery_plan_execution_steps"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
