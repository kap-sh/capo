"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateReplicationConfigMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.compute_config
    import capo_database_migration_service.types.migration_type_value
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.tag_list


class CreateReplicationConfigMessage(TypedDict, closed=True):
    replication_config_identifier: "capo_database_migration_service.types.string.String"
    """<p>A unique identifier that you want to use to create a <code>ReplicationConfigArn</code> that is returned as part of the output from this action. You can then pass this output <code>ReplicationConfigArn</code> as the value of the <code>ReplicationConfigArn</code> option for other actions to identify both DMS Serverless replications and replication configurations that you want those actions to operate on. For some actions, you can also use either this unique identifier or a corresponding ARN in action filters to identify the specific replication and replication configuration to operate on.</p>"""
    source_endpoint_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the source endpoint for this DMS Serverless replication configuration.</p>"""
    target_endpoint_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the target endpoint for this DMS serverless replication configuration.</p>"""
    compute_config: "capo_database_migration_service.types.compute_config.ComputeConfig"
    """<p>Configuration parameters for provisioning an DMS Serverless replication.</p>"""
    replication_type: (
        "capo_database_migration_service.types.migration_type_value.MigrationTypeValue"
    )
    """<p>The type of DMS Serverless replication to provision using this replication configuration.</p> <p>Possible values:</p> <ul> <li> <p> <code>"full-load"</code> </p> </li> <li> <p> <code>"cdc"</code> </p> </li> <li> <p> <code>"full-load-and-cdc"</code> </p> </li> </ul>"""
    table_mappings: "capo_database_migration_service.types.string.String"
    """<p>JSON table mappings for DMS Serverless replications that are provisioned using this replication configuration. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.html"> Specifying table selection and transformations rules using JSON</a>.</p>"""
    replication_settings: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Optional JSON settings for DMS Serverless replications that are provisioned using this replication configuration. For example, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.ChangeProcessingTuning.html"> Change processing tuning settings</a>.</p>"""
    supplemental_settings: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Optional JSON settings for specifying supplemental data. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html"> Specifying supplemental data for task settings</a>.</p>"""
    resource_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Optional unique value or name that you set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.FineGrainedAccess"> Fine-grained access control using resource names and tags</a>.</p>"""
    tags: NotRequired["capo_database_migration_service.types.tag_list.TagList"]
    """<p>One or more optional tags associated with resources used by the DMS Serverless replication. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tagging.html"> Tagging resources in Database Migration Service</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateReplicationConfigMessage) -> dict:
    out: dict = {}
    out["ReplicationConfigIdentifier"] = value["replication_config_identifier"]
    out["SourceEndpointArn"] = value["source_endpoint_arn"]
    out["TargetEndpointArn"] = value["target_endpoint_arn"]
    import capo_database_migration_service.types.compute_config

    out["ComputeConfig"] = (
        capo_database_migration_service.types.compute_config.serialize_aws_json_1_1(
            value["compute_config"]
        )
    )
    import capo_database_migration_service.types.migration_type_value

    out["ReplicationType"] = (
        capo_database_migration_service.types.migration_type_value.serialize_aws_json_1_1(
            value["replication_type"]
        )
    )
    out["TableMappings"] = value["table_mappings"]
    if "replication_settings" in value:
        out["ReplicationSettings"] = value["replication_settings"]
    if "supplemental_settings" in value:
        out["SupplementalSettings"] = value["supplemental_settings"]
    if "resource_identifier" in value:
        out["ResourceIdentifier"] = value["resource_identifier"]
    if "tags" in value:
        import capo_database_migration_service.types.tag_list

        out["Tags"] = (
            capo_database_migration_service.types.tag_list.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateReplicationConfigMessage:
    out: CreateReplicationConfigMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationConfigIdentifier") is not None:
        out["replication_config_identifier"] = data["ReplicationConfigIdentifier"]
    else:
        raise DeserializationError(
            "CreateReplicationConfigMessage.replication_config_identifier required"
        )
    if data.get("SourceEndpointArn") is not None:
        out["source_endpoint_arn"] = data["SourceEndpointArn"]
    else:
        raise DeserializationError(
            "CreateReplicationConfigMessage.source_endpoint_arn required"
        )
    if data.get("TargetEndpointArn") is not None:
        out["target_endpoint_arn"] = data["TargetEndpointArn"]
    else:
        raise DeserializationError(
            "CreateReplicationConfigMessage.target_endpoint_arn required"
        )
    if data.get("ComputeConfig") is not None:
        import capo_database_migration_service.types.compute_config

        out["compute_config"] = (
            capo_database_migration_service.types.compute_config.deserialize_aws_json_1_1(
                data["ComputeConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateReplicationConfigMessage.compute_config required"
        )
    if data.get("ReplicationType") is not None:
        import capo_database_migration_service.types.migration_type_value

        out["replication_type"] = (
            capo_database_migration_service.types.migration_type_value.deserialize_aws_json_1_1(
                data["ReplicationType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateReplicationConfigMessage.replication_type required"
        )
    if data.get("TableMappings") is not None:
        out["table_mappings"] = data["TableMappings"]
    else:
        raise DeserializationError(
            "CreateReplicationConfigMessage.table_mappings required"
        )
    if data.get("ReplicationSettings") is not None:
        out["replication_settings"] = data["ReplicationSettings"]
    if data.get("SupplementalSettings") is not None:
        out["supplemental_settings"] = data["SupplementalSettings"]
    if data.get("ResourceIdentifier") is not None:
        out["resource_identifier"] = data["ResourceIdentifier"]
    if data.get("Tags") is not None:
        import capo_database_migration_service.types.tag_list

        out["tags"] = (
            capo_database_migration_service.types.tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    return out
