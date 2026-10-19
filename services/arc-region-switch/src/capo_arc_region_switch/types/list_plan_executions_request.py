"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ListPlanExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_region_switch.types.execution_state
    import capo_arc_region_switch.types.list_executions_max_results
    import capo_arc_region_switch.types.plan_arn


class ListPlanExecutionsRequest(TypedDict, closed=True):
    plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The ARN for the plan.</p>"""
    max_results: NotRequired[
        "capo_arc_region_switch.types.list_executions_max_results.ListExecutionsMaxResults"
    ]
    """<p>The number of objects that you want to return with this call.</p>"""
    next_token: NotRequired["str"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""
    state: NotRequired["capo_arc_region_switch.types.execution_state.ExecutionState"]
    """<p>The state of the plan execution. For example, the plan execution might be In Progress.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPlanExecutionsRequest) -> dict:
    out: dict = {}
    out["planArn"] = value["plan_arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "state" in value:
        import capo_arc_region_switch.types.execution_state

        out["state"] = (
            capo_arc_region_switch.types.execution_state.serialize_aws_json_1_0(
                value["state"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPlanExecutionsRequest:
    out: ListPlanExecutionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("planArn") is not None:
        out["plan_arn"] = data["planArn"]
    else:
        raise DeserializationError("ListPlanExecutionsRequest.plan_arn required")
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("state") is not None:
        import capo_arc_region_switch.types.execution_state

        out["state"] = (
            capo_arc_region_switch.types.execution_state.deserialize_aws_json_1_0(
                data["state"]
            )
        )
    return out
