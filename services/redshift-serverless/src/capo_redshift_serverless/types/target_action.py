"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#TargetAction``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError, SerializationError
from capo_redshift_serverless.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_redshift_serverless.types.create_snapshot_schedule_action_parameters


class _TargetAction_createSnapshot(TypedDict, closed=True):
    createSnapshot: "capo_redshift_serverless.types.create_snapshot_schedule_action_parameters.CreateSnapshotScheduleActionParameters"


TargetAction: TypeAlias = _TargetAction_createSnapshot | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetAction) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TargetAction: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "createSnapshot" in value:
        import capo_redshift_serverless.types.create_snapshot_schedule_action_parameters

        return {
            "createSnapshot": capo_redshift_serverless.types.create_snapshot_schedule_action_parameters.serialize_aws_json_1_1(
                value["createSnapshot"]
            )
        }
    else:
        raise SerializationError("TargetAction: no variant present")


def deserialize_aws_json_1_1(data: dict) -> TargetAction:
    if data.get("createSnapshot") is not None:
        import capo_redshift_serverless.types.create_snapshot_schedule_action_parameters

        return {
            "createSnapshot": capo_redshift_serverless.types.create_snapshot_schedule_action_parameters.deserialize_aws_json_1_1(
                data["createSnapshot"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TargetAction: no recognized variant key")
