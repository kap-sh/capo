"""Generated from Smithy shape ``com.amazonaws.drs#ListRecoveryPlanExecutionStepsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.list_recovery_plan_execution_steps_filter
    import capo_drs.types.max_results_type
    import capo_drs.types.pagination_token
    import capo_drs.types.strict_drsarn


class ListRecoveryPlanExecutionStepsRequest(TypedDict, closed=True):
    recovery_plan_execution_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the Recovery Plan execution.</p>"""
    filter: NotRequired[
        "capo_drs.types.list_recovery_plan_execution_steps_filter.ListRecoveryPlanExecutionStepsFilter"
    ]
    """<p>Filters for listing execution steps.</p>"""
    max_results: NotRequired["capo_drs.types.max_results_type.MaxResultsType"]
    """<p>Maximum number of results to return.</p>"""
    next_token: NotRequired["capo_drs.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecoveryPlanExecutionStepsRequest) -> dict:
    out: dict = {}
    out["recoveryPlanExecutionArn"] = value["recovery_plan_execution_arn"]
    if "filter" in value:
        import capo_drs.types.list_recovery_plan_execution_steps_filter

        out["filter"] = (
            capo_drs.types.list_recovery_plan_execution_steps_filter.serialize_json(
                value["filter"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecoveryPlanExecutionStepsRequest:
    out: ListRecoveryPlanExecutionStepsRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanExecutionArn") is not None:
        out["recovery_plan_execution_arn"] = data["recoveryPlanExecutionArn"]
    else:
        out["recovery_plan_execution_arn"] = ""
    if data.get("filter") is not None:
        import capo_drs.types.list_recovery_plan_execution_steps_filter

        out["filter"] = (
            capo_drs.types.list_recovery_plan_execution_steps_filter.deserialize_json(
                data["filter"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
