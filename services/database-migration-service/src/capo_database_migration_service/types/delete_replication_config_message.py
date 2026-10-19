"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteReplicationConfigMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class DeleteReplicationConfigMessage(TypedDict, closed=True):
    replication_config_arn: "capo_database_migration_service.types.string.String"
    """<p>The replication config to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteReplicationConfigMessage) -> dict:
    out: dict = {}
    out["ReplicationConfigArn"] = value["replication_config_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteReplicationConfigMessage:
    out: DeleteReplicationConfigMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationConfigArn") is not None:
        out["replication_config_arn"] = data["ReplicationConfigArn"]
    else:
        out["replication_config_arn"] = ""
    return out
