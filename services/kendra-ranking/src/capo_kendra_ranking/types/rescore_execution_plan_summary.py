"""Generated from Smithy shape ``com.amazonaws.kendraranking#RescoreExecutionPlanSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra_ranking.types.rescore_execution_plan_id
    import capo_kendra_ranking.types.rescore_execution_plan_name
    import capo_kendra_ranking.types.rescore_execution_plan_status
    import capo_kendra_ranking.types.timestamp


class RescoreExecutionPlanSummary(TypedDict, closed=True):
    name: NotRequired[
        "capo_kendra_ranking.types.rescore_execution_plan_name.RescoreExecutionPlanName"
    ]
    """<p>The name of the rescore execution plan.</p>"""
    id: NotRequired[
        "capo_kendra_ranking.types.rescore_execution_plan_id.RescoreExecutionPlanId"
    ]
    """<p>The identifier of the rescore execution plan.</p>"""
    created_at: NotRequired["capo_kendra_ranking.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the rescore execution plan was created.</p>"""
    updated_at: NotRequired["capo_kendra_ranking.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the rescore execution plan was last updated.</p>"""
    status: NotRequired[
        "capo_kendra_ranking.types.rescore_execution_plan_status.RescoreExecutionPlanStatus"
    ]
    """<p>The current status of the rescore execution plan. When the value is <code>ACTIVE</code>, the rescore execution plan is ready for use.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RescoreExecutionPlanSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
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
    return out


def deserialize_aws_json_1_0(data: dict) -> RescoreExecutionPlanSummary:
    out: RescoreExecutionPlanSummary = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
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
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RescoreExecutionPlanSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "created_at" in value:
        import capo_kendra_ranking.types.timestamp

        out["CreatedAt"] = capo_kendra_ranking.types.timestamp.serialize_cbor(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_kendra_ranking.types.timestamp

        out["UpdatedAt"] = capo_kendra_ranking.types.timestamp.serialize_cbor(
            value["updated_at"]
        )
    if "status" in value:
        import capo_kendra_ranking.types.rescore_execution_plan_status

        out["Status"] = (
            capo_kendra_ranking.types.rescore_execution_plan_status.serialize_cbor(
                value["status"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RescoreExecutionPlanSummary:
    out: RescoreExecutionPlanSummary = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("CreatedAt") is not None:
        import capo_kendra_ranking.types.timestamp

        out["created_at"] = capo_kendra_ranking.types.timestamp.deserialize_cbor(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_kendra_ranking.types.timestamp

        out["updated_at"] = capo_kendra_ranking.types.timestamp.deserialize_cbor(
            data["UpdatedAt"]
        )
    if data.get("Status") is not None:
        import capo_kendra_ranking.types.rescore_execution_plan_status

        out["status"] = (
            capo_kendra_ranking.types.rescore_execution_plan_status.deserialize_cbor(
                data["Status"]
            )
        )
    return out
