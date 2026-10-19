"""Generated from Smithy shape ``com.amazonaws.drs#ListRecoveryPlanExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.pagination_token
    import capo_drs.types.recovery_plan_execution_summary_list


class ListRecoveryPlanExecutionsResponse(TypedDict, closed=True):
    recovery_plan_executions: "capo_drs.types.recovery_plan_execution_summary_list.RecoveryPlanExecutionSummaryList"
    """<p>The list of Recovery Plan executions.</p>"""
    next_token: NotRequired["capo_drs.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecoveryPlanExecutionsResponse) -> dict:
    out: dict = {}
    import capo_drs.types.recovery_plan_execution_summary_list

    out["recoveryPlanExecutions"] = (
        capo_drs.types.recovery_plan_execution_summary_list.serialize_json(
            value["recovery_plan_executions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecoveryPlanExecutionsResponse:
    out: ListRecoveryPlanExecutionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanExecutions") is not None:
        import capo_drs.types.recovery_plan_execution_summary_list

        out["recovery_plan_executions"] = (
            capo_drs.types.recovery_plan_execution_summary_list.deserialize_json(
                data["recoveryPlanExecutions"]
            )
        )
    else:
        out["recovery_plan_executions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
