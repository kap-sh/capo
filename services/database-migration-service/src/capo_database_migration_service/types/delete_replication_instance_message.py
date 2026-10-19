"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteReplicationInstanceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class DeleteReplicationInstanceMessage(TypedDict, closed=True):
    replication_instance_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the replication instance to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteReplicationInstanceMessage) -> dict:
    out: dict = {}
    out["ReplicationInstanceArn"] = value["replication_instance_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteReplicationInstanceMessage:
    out: DeleteReplicationInstanceMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationInstanceArn") is not None:
        out["replication_instance_arn"] = data["ReplicationInstanceArn"]
    else:
        out["replication_instance_arn"] = ""
    return out
