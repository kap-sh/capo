"""Generated from Smithy shape ``com.amazonaws.kendraranking#DescribeRescoreExecutionPlanResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra_ranking.types.capacity_units_configuration
    import capo_kendra_ranking.types.description
    import capo_kendra_ranking.types.error_message
    import capo_kendra_ranking.types.rescore_execution_plan_arn
    import capo_kendra_ranking.types.rescore_execution_plan_id
    import capo_kendra_ranking.types.rescore_execution_plan_name
    import capo_kendra_ranking.types.rescore_execution_plan_status
    import capo_kendra_ranking.types.timestamp


class DescribeRescoreExecutionPlanResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_kendra_ranking.types.rescore_execution_plan_id.RescoreExecutionPlanId"
    ]
    """<p>The identifier of the rescore execution plan.</p>"""
    arn: NotRequired[
        "capo_kendra_ranking.types.rescore_execution_plan_arn.RescoreExecutionPlanArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the rescore execution plan.</p>"""
    name: NotRequired[
        "capo_kendra_ranking.types.rescore_execution_plan_name.RescoreExecutionPlanName"
    ]
    """<p>The name for the rescore execution plan.</p>"""
    description: NotRequired["capo_kendra_ranking.types.description.Description"]
    """<p>The description for the rescore execution plan.</p>"""
    capacity_units: NotRequired[
        "capo_kendra_ranking.types.capacity_units_configuration.CapacityUnitsConfiguration"
    ]
    """<p>The capacity units set for the rescore execution plan. A capacity of zero indicates that the rescore execution plan is using the default capacity. For more information on the default capacity and additional capacity units, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html">Adjusting capacity</a>.</p>"""
    created_at: NotRequired["capo_kendra_ranking.types.timestamp.Timestamp"]
    """<p>The Unix timestamp of when the rescore execution plan was created.</p>"""
    updated_at: NotRequired["capo_kendra_ranking.types.timestamp.Timestamp"]
    """<p>The Unix timestamp of when the rescore execution plan was last updated.</p>"""
    status: NotRequired[
        "capo_kendra_ranking.types.rescore_execution_plan_status.RescoreExecutionPlanStatus"
    ]
    """<p>The current status of the rescore execution plan. When the value is <code>ACTIVE</code>, the rescore execution plan is ready for use. If the <code>Status</code> field value is <code>FAILED</code>, the <code>ErrorMessage</code> field contains a message that explains why.</p>"""
    error_message: NotRequired["capo_kendra_ranking.types.error_message.ErrorMessage"]
    """<p>When the <code>Status</code> field value is <code>FAILED</code>, the <code>ErrorMessage</code> field contains a message that explains why.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRescoreExecutionPlanResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
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
    if "created_at" in value:
        import capo_kendra_ranking.types.timestamp

        out["CreatedAt"] = capo_kendra_ranking.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_kendra_ranking.types.timestamp

        out["UpdatedAt"] = capo_kendra_ranking.types.timestamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    if "status" in value:
        import capo_kendra_ranking.types.rescore_execution_plan_status

        out["Status"] = (
            capo_kendra_ranking.types.rescore_execution_plan_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRescoreExecutionPlanResponse:
    out: DescribeRescoreExecutionPlanResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
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
    if data.get("CreatedAt") is not None:
        import capo_kendra_ranking.types.timestamp

        out["created_at"] = (
            capo_kendra_ranking.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_kendra_ranking.types.timestamp

        out["updated_at"] = (
            capo_kendra_ranking.types.timestamp.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    if data.get("Status") is not None:
        import capo_kendra_ranking.types.rescore_execution_plan_status

        out["status"] = (
            capo_kendra_ranking.types.rescore_execution_plan_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
