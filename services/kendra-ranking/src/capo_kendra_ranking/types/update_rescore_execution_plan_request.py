"""Generated from Smithy shape ``com.amazonaws.kendraranking#UpdateRescoreExecutionPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra_ranking.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra_ranking.types.capacity_units_configuration
    import capo_kendra_ranking.types.description
    import capo_kendra_ranking.types.rescore_execution_plan_id
    import capo_kendra_ranking.types.rescore_execution_plan_name


class UpdateRescoreExecutionPlanRequest(TypedDict, closed=True):
    id: "capo_kendra_ranking.types.rescore_execution_plan_id.RescoreExecutionPlanId"
    """<p>The identifier of the rescore execution plan that you want to update.</p>"""
    name: NotRequired[
        "capo_kendra_ranking.types.rescore_execution_plan_name.RescoreExecutionPlanName"
    ]
    """<p>A new name for the rescore execution plan.</p>"""
    description: NotRequired["capo_kendra_ranking.types.description.Description"]
    """<p>A new description for the rescore execution plan.</p>"""
    capacity_units: NotRequired[
        "capo_kendra_ranking.types.capacity_units_configuration.CapacityUnitsConfiguration"
    ]
    """<p>You can set additional capacity units to meet the needs of your rescore execution plan. You are given a single capacity unit by default. If you want to use the default capacity, you don't set additional capacity units. For more information on the default capacity and additional capacity units, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html">Adjusting capacity</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRescoreExecutionPlanRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "capacity_units" in value:
        import capo_kendra_ranking.types.capacity_units_configuration

        out["CapacityUnits"] = (
            capo_kendra_ranking.types.capacity_units_configuration.serialize_aws_json_1_0(
                value["capacity_units"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateRescoreExecutionPlanRequest:
    out: UpdateRescoreExecutionPlanRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdateRescoreExecutionPlanRequest.id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CapacityUnits") is not None:
        import capo_kendra_ranking.types.capacity_units_configuration

        out["capacity_units"] = (
            capo_kendra_ranking.types.capacity_units_configuration.deserialize_aws_json_1_0(
                data["CapacityUnits"]
            )
        )
    return out
