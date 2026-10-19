"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteReplicationSubnetGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class DeleteReplicationSubnetGroupMessage(TypedDict, closed=True):
    replication_subnet_group_identifier: (
        "capo_database_migration_service.types.string.String"
    )
    """<p>The subnet group name of the replication instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteReplicationSubnetGroupMessage) -> dict:
    out: dict = {}
    out["ReplicationSubnetGroupIdentifier"] = value[
        "replication_subnet_group_identifier"
    ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteReplicationSubnetGroupMessage:
    out: DeleteReplicationSubnetGroupMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationSubnetGroupIdentifier") is not None:
        out["replication_subnet_group_identifier"] = data[
            "ReplicationSubnetGroupIdentifier"
        ]
    else:
        out["replication_subnet_group_identifier"] = ""
    return out
