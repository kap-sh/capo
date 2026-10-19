"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteReplicationTaskMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class DeleteReplicationTaskMessage(TypedDict, closed=True):
    replication_task_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the replication task to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteReplicationTaskMessage) -> dict:
    out: dict = {}
    out["ReplicationTaskArn"] = value["replication_task_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteReplicationTaskMessage:
    out: DeleteReplicationTaskMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationTaskArn") is not None:
        out["replication_task_arn"] = data["ReplicationTaskArn"]
    else:
        out["replication_task_arn"] = ""
    return out
