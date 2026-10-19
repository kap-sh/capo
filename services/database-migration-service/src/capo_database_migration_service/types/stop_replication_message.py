"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StopReplicationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class StopReplicationMessage(TypedDict, closed=True):
    replication_config_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name of the replication to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopReplicationMessage) -> dict:
    out: dict = {}
    out["ReplicationConfigArn"] = value["replication_config_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopReplicationMessage:
    out: StopReplicationMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationConfigArn") is not None:
        out["replication_config_arn"] = data["ReplicationConfigArn"]
    else:
        out["replication_config_arn"] = ""
    return out
