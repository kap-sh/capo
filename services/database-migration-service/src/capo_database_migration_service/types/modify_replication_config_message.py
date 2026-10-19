"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyReplicationConfigMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.compute_config
    import capo_database_migration_service.types.migration_type_value
    import capo_database_migration_service.types.string


class ModifyReplicationConfigMessage(TypedDict, closed=True):
    replication_config_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name of the replication to modify.</p>"""
    replication_config_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The new replication config to apply to the replication.</p>"""
    replication_type: NotRequired[
        "capo_database_migration_service.types.migration_type_value.MigrationTypeValue"
    ]
    """<p>The type of replication.</p>"""
    table_mappings: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Table mappings specified in the replication.</p>"""
    replication_settings: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The settings for the replication.</p>"""
    supplemental_settings: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Additional settings for the replication.</p>"""
    compute_config: NotRequired[
        "capo_database_migration_service.types.compute_config.ComputeConfig"
    ]
    """<p>Configuration parameters for provisioning an DMS Serverless replication.</p>"""
    source_endpoint_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the source endpoint for this DMS serverless replication configuration.</p>"""
    target_endpoint_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the target endpoint for this DMS serverless replication configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyReplicationConfigMessage) -> dict:
    out: dict = {}
    out["ReplicationConfigArn"] = value["replication_config_arn"]
    if "replication_config_identifier" in value:
        out["ReplicationConfigIdentifier"] = value["replication_config_identifier"]
    if "replication_type" in value:
        import capo_database_migration_service.types.migration_type_value

        out["ReplicationType"] = (
            capo_database_migration_service.types.migration_type_value.serialize_aws_json_1_1(
                value["replication_type"]
            )
        )
    if "table_mappings" in value:
        out["TableMappings"] = value["table_mappings"]
    if "replication_settings" in value:
        out["ReplicationSettings"] = value["replication_settings"]
    if "supplemental_settings" in value:
        out["SupplementalSettings"] = value["supplemental_settings"]
    if "compute_config" in value:
        import capo_database_migration_service.types.compute_config

        out["ComputeConfig"] = (
            capo_database_migration_service.types.compute_config.serialize_aws_json_1_1(
                value["compute_config"]
            )
        )
    if "source_endpoint_arn" in value:
        out["SourceEndpointArn"] = value["source_endpoint_arn"]
    if "target_endpoint_arn" in value:
        out["TargetEndpointArn"] = value["target_endpoint_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyReplicationConfigMessage:
    out: ModifyReplicationConfigMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationConfigArn") is not None:
        out["replication_config_arn"] = data["ReplicationConfigArn"]
    else:
        out["replication_config_arn"] = ""
    if data.get("ReplicationConfigIdentifier") is not None:
        out["replication_config_identifier"] = data["ReplicationConfigIdentifier"]
    if data.get("ReplicationType") is not None:
        import capo_database_migration_service.types.migration_type_value

        out["replication_type"] = (
            capo_database_migration_service.types.migration_type_value.deserialize_aws_json_1_1(
                data["ReplicationType"]
            )
        )
    if data.get("TableMappings") is not None:
        out["table_mappings"] = data["TableMappings"]
    if data.get("ReplicationSettings") is not None:
        out["replication_settings"] = data["ReplicationSettings"]
    if data.get("SupplementalSettings") is not None:
        out["supplemental_settings"] = data["SupplementalSettings"]
    if data.get("ComputeConfig") is not None:
        import capo_database_migration_service.types.compute_config

        out["compute_config"] = (
            capo_database_migration_service.types.compute_config.deserialize_aws_json_1_1(
                data["ComputeConfig"]
            )
        )
    if data.get("SourceEndpointArn") is not None:
        out["source_endpoint_arn"] = data["SourceEndpointArn"]
    if data.get("TargetEndpointArn") is not None:
        out["target_endpoint_arn"] = data["TargetEndpointArn"]
    return out
