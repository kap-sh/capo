"""Generated from Smithy shape ``com.amazonaws.kendraranking#DescribeRescoreExecutionPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra_ranking.types.rescore_execution_plan_id


class DescribeRescoreExecutionPlanRequest(TypedDict, closed=True):
    id: "capo_kendra_ranking.types.rescore_execution_plan_id.RescoreExecutionPlanId"
    """<p>The identifier of the rescore execution plan that you want to get information on.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRescoreExecutionPlanRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRescoreExecutionPlanRequest:
    out: DescribeRescoreExecutionPlanRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    return out
