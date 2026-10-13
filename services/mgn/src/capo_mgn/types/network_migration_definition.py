"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationDefinition``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mgn.types.arn
    import capo_mgn.types.cidr_mappings_list
    import capo_mgn.types.network_migration_definition_description
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.network_migration_definition_name
    import capo_mgn.types.scope_tags_map
    import capo_mgn.types.source_configuration_list
    import capo_mgn.types.tags_map
    import capo_mgn.types.target_deployment
    import capo_mgn.types.target_network
    import capo_mgn.types.target_s3_configuration
    import capo_mgn.types.vpc_provisioning_strategy


class NetworkMigrationDefinition(TypedDict, closed=True):
    arn: NotRequired["capo_mgn.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the network migration definition.</p>"""
    network_migration_definition_id: NotRequired[
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    ]
    """<p>The unique identifier of the network migration definition.</p>"""
    name: NotRequired[
        "capo_mgn.types.network_migration_definition_name.NetworkMigrationDefinitionName"
    ]
    """<p>The name of the network migration definition.</p>"""
    description: NotRequired[
        "capo_mgn.types.network_migration_definition_description.NetworkMigrationDefinitionDescription"
    ]
    """<p>A description of the network migration definition.</p>"""
    source_configurations: NotRequired[
        "capo_mgn.types.source_configuration_list.SourceConfigurationList"
    ]
    """<p>A list of source configurations for the network migration.</p>"""
    target_s3_configuration: NotRequired[
        "capo_mgn.types.target_s3_configuration.TargetS3Configuration"
    ]
    """<p>The S3 configuration for storing the target network artifacts.</p>"""
    target_network: NotRequired["capo_mgn.types.target_network.TargetNetwork"]
    """<p>The target network configuration including topology and CIDR ranges.</p>"""
    target_deployment: NotRequired["capo_mgn.types.target_deployment.TargetDeployment"]
    """<p>The target deployment configuration for the migrated network.</p>"""
    vpc_provisioning_strategy: NotRequired[
        "capo_mgn.types.vpc_provisioning_strategy.VpcProvisioningStrategy"
    ]
    """<p>Indicates whether the migration creates new target VPCs or uses existing ones. <code>CREATE_NEW</code> provisions new target VPCs; <code>USE_EXISTING</code> migrates into existing VPCs in the target account.</p>"""
    cidr_mappings: NotRequired["capo_mgn.types.cidr_mappings_list.CidrMappingsList"]
    """<p>A list of CIDR mappings that map original source CIDR ranges to updated target CIDR ranges. CIDR mappings apply only when <code>vpcProvisioningStrategy</code> is set to <code>USE_EXISTING</code>.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the network migration definition was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the network migration definition was last updated.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Tags assigned to the network migration definition.</p>"""
    scope_tags: NotRequired["capo_mgn.types.scope_tags_map.ScopeTagsMap"]
    """<p>Scope tags for the network migration definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationDefinition) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "network_migration_definition_id" in value:
        out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "source_configurations" in value:
        import capo_mgn.types.source_configuration_list

        out["sourceConfigurations"] = (
            capo_mgn.types.source_configuration_list.serialize_json(
                value["source_configurations"]
            )
        )
    if "target_s3_configuration" in value:
        import capo_mgn.types.target_s3_configuration

        out["targetS3Configuration"] = (
            capo_mgn.types.target_s3_configuration.serialize_json(
                value["target_s3_configuration"]
            )
        )
    if "target_network" in value:
        import capo_mgn.types.target_network

        out["targetNetwork"] = capo_mgn.types.target_network.serialize_json(
            value["target_network"]
        )
    if "target_deployment" in value:
        out["targetDeployment"] = value["target_deployment"]
    if "vpc_provisioning_strategy" in value:
        out["vpcProvisioningStrategy"] = value["vpc_provisioning_strategy"]
    if "cidr_mappings" in value:
        import capo_mgn.types.cidr_mappings_list

        out["cidrMappings"] = capo_mgn.types.cidr_mappings_list.serialize_json(
            value["cidr_mappings"]
        )
    if "created_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["createdAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["updatedAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    if "scope_tags" in value:
        import capo_mgn.types.scope_tags_map

        out["scopeTags"] = capo_mgn.types.scope_tags_map.serialize_json(
            value["scope_tags"]
        )
    return out


def deserialize_json(data: dict) -> NetworkMigrationDefinition:
    out: NetworkMigrationDefinition = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("networkMigrationDefinitionID") is not None:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("sourceConfigurations") is not None:
        import capo_mgn.types.source_configuration_list

        out["source_configurations"] = (
            capo_mgn.types.source_configuration_list.deserialize_json(
                data["sourceConfigurations"]
            )
        )
    if data.get("targetS3Configuration") is not None:
        import capo_mgn.types.target_s3_configuration

        out["target_s3_configuration"] = (
            capo_mgn.types.target_s3_configuration.deserialize_json(
                data["targetS3Configuration"]
            )
        )
    if data.get("targetNetwork") is not None:
        import capo_mgn.types.target_network

        out["target_network"] = capo_mgn.types.target_network.deserialize_json(
            data["targetNetwork"]
        )
    if data.get("targetDeployment") is not None:
        out["target_deployment"] = data["targetDeployment"]
    if data.get("vpcProvisioningStrategy") is not None:
        out["vpc_provisioning_strategy"] = data["vpcProvisioningStrategy"]
    if data.get("cidrMappings") is not None:
        import capo_mgn.types.cidr_mappings_list

        out["cidr_mappings"] = capo_mgn.types.cidr_mappings_list.deserialize_json(
            data["cidrMappings"]
        )
    if data.get("createdAt") is not None:
        import capo_mgn.types._prelude.timestamp

        out["created_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_mgn.types._prelude.timestamp

        out["updated_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if data.get("tags") is not None:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    if data.get("scopeTags") is not None:
        import capo_mgn.types.scope_tags_map

        out["scope_tags"] = capo_mgn.types.scope_tags_map.deserialize_json(
            data["scopeTags"]
        )
    return out


def redact_sensitive(value: NetworkMigrationDefinition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    if "scope_tags" in value:
        out["scope_tags"] = "*** Sensitive Data Redacted ***"
    return out
