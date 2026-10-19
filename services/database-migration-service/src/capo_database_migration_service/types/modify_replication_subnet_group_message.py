"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyReplicationSubnetGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.subnet_identifier_list


class ModifyReplicationSubnetGroupMessage(TypedDict, closed=True):
    replication_subnet_group_identifier: (
        "capo_database_migration_service.types.string.String"
    )
    """<p>The name of the replication instance subnet group.</p>"""
    replication_subnet_group_description: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>A description for the replication instance subnet group.</p>"""
    subnet_ids: "capo_database_migration_service.types.subnet_identifier_list.SubnetIdentifierList"
    """<p>A list of subnet IDs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyReplicationSubnetGroupMessage) -> dict:
    out: dict = {}
    out["ReplicationSubnetGroupIdentifier"] = value[
        "replication_subnet_group_identifier"
    ]
    if "replication_subnet_group_description" in value:
        out["ReplicationSubnetGroupDescription"] = value[
            "replication_subnet_group_description"
        ]
    import capo_database_migration_service.types.subnet_identifier_list

    out["SubnetIds"] = (
        capo_database_migration_service.types.subnet_identifier_list.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyReplicationSubnetGroupMessage:
    out: ModifyReplicationSubnetGroupMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationSubnetGroupIdentifier") is not None:
        out["replication_subnet_group_identifier"] = data[
            "ReplicationSubnetGroupIdentifier"
        ]
    else:
        out["replication_subnet_group_identifier"] = ""
    if data.get("ReplicationSubnetGroupDescription") is not None:
        out["replication_subnet_group_description"] = data[
            "ReplicationSubnetGroupDescription"
        ]
    if data.get("SubnetIds") is not None:
        import capo_database_migration_service.types.subnet_identifier_list

        out["subnet_ids"] = (
            capo_database_migration_service.types.subnet_identifier_list.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    else:
        out["subnet_ids"] = []
    return out
