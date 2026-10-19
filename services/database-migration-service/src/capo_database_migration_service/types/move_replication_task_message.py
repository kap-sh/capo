"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MoveReplicationTaskMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class MoveReplicationTaskMessage(TypedDict, closed=True):
    replication_task_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the task that you want to move.</p>"""
    target_replication_instance_arn: (
        "capo_database_migration_service.types.string.String"
    )
    """<p>The ARN of the replication instance where you want to move the task to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MoveReplicationTaskMessage) -> dict:
    out: dict = {}
    out["ReplicationTaskArn"] = value["replication_task_arn"]
    out["TargetReplicationInstanceArn"] = value["target_replication_instance_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MoveReplicationTaskMessage:
    out: MoveReplicationTaskMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationTaskArn") is not None:
        out["replication_task_arn"] = data["ReplicationTaskArn"]
    else:
        out["replication_task_arn"] = ""
    if data.get("TargetReplicationInstanceArn") is not None:
        out["target_replication_instance_arn"] = data["TargetReplicationInstanceArn"]
    else:
        out["target_replication_instance_arn"] = ""
    return out
