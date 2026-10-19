"""Generated from Smithy shape ``com.amazonaws.kendraranking#DeleteRescoreExecutionPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra_ranking.types.rescore_execution_plan_id


class DeleteRescoreExecutionPlanRequest(TypedDict, closed=True):
    id: "capo_kendra_ranking.types.rescore_execution_plan_id.RescoreExecutionPlanId"
    """<p>The identifier of the rescore execution plan that you want to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRescoreExecutionPlanRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRescoreExecutionPlanRequest:
    out: DeleteRescoreExecutionPlanRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    return out
