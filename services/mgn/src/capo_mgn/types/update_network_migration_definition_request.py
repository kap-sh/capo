"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateNetworkMigrationDefinitionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.cidr_mappings_list
    import capo_mgn.types.network_migration_definition_description
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.network_migration_definition_name
    import capo_mgn.types.scope_tags_map
    import capo_mgn.types.source_configuration_list
    import capo_mgn.types.target_deployment
    import capo_mgn.types.target_network_update
    import capo_mgn.types.target_s3_configuration_update
    import capo_mgn.types.vpc_provisioning_strategy


class UpdateNetworkMigrationDefinitionRequest(TypedDict, closed=True):
    network_migration_definition_id: (
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition to update.</p>"""
    name: NotRequired[
        "capo_mgn.types.network_migration_definition_name.NetworkMigrationDefinitionName"
    ]
    """<p>The updated name of the network migration definition.</p>"""
    description: NotRequired[
        "capo_mgn.types.network_migration_definition_description.NetworkMigrationDefinitionDescription"
    ]
    """<p>The updated description of the network migration definition.</p>"""
    source_configurations: NotRequired[
        "capo_mgn.types.source_configuration_list.SourceConfigurationList"
    ]
    """<p>The updated list of source configurations.</p>"""
    target_s3_configuration: NotRequired[
        "capo_mgn.types.target_s3_configuration_update.TargetS3ConfigurationUpdate"
    ]
    """<p>The updated S3 configuration for storing the target network artifacts.</p>"""
    target_network: NotRequired[
        "capo_mgn.types.target_network_update.TargetNetworkUpdate"
    ]
    """<p>The updated target network configuration.</p>"""
    target_deployment: NotRequired["capo_mgn.types.target_deployment.TargetDeployment"]
    """<p>The updated target deployment configuration.</p>"""
    vpc_provisioning_strategy: NotRequired[
        "capo_mgn.types.vpc_provisioning_strategy.VpcProvisioningStrategy"
    ]
    """<p>Updates whether the migration creates new target VPCs or uses existing ones. Set to <code>USE_EXISTING</code> to migrate into existing VPCs in the target account, or to <code>CREATE_NEW</code> to provision new target VPCs.</p>"""
    cidr_mappings: NotRequired["capo_mgn.types.cidr_mappings_list.CidrMappingsList"]
    """<p>The updated list of CIDR mappings that map original source CIDR ranges to updated target CIDR ranges. CIDR mappings can be provided only when <code>vpcProvisioningStrategy</code> is set to <code>USE_EXISTING</code>.</p>"""
    scope_tags: NotRequired["capo_mgn.types.scope_tags_map.ScopeTagsMap"]
    """<p>The updated scope tags for the network migration definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNetworkMigrationDefinitionRequest) -> dict:
    out: dict = {}
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
        import capo_mgn.types.target_s3_configuration_update

        out["targetS3Configuration"] = (
            capo_mgn.types.target_s3_configuration_update.serialize_json(
                value["target_s3_configuration"]
            )
        )
    if "target_network" in value:
        import capo_mgn.types.target_network_update

        out["targetNetwork"] = capo_mgn.types.target_network_update.serialize_json(
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
    if "scope_tags" in value:
        import capo_mgn.types.scope_tags_map

        out["scopeTags"] = capo_mgn.types.scope_tags_map.serialize_json(
            value["scope_tags"]
        )
    return out


def deserialize_json(data: dict) -> UpdateNetworkMigrationDefinitionRequest:
    out: UpdateNetworkMigrationDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("networkMigrationDefinitionID") is not None:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        raise DeserializationError(
            "UpdateNetworkMigrationDefinitionRequest.network_migration_definition_id required"
        )
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
        import capo_mgn.types.target_s3_configuration_update

        out["target_s3_configuration"] = (
            capo_mgn.types.target_s3_configuration_update.deserialize_json(
                data["targetS3Configuration"]
            )
        )
    if data.get("targetNetwork") is not None:
        import capo_mgn.types.target_network_update

        out["target_network"] = capo_mgn.types.target_network_update.deserialize_json(
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
    if data.get("scopeTags") is not None:
        import capo_mgn.types.scope_tags_map

        out["scope_tags"] = capo_mgn.types.scope_tags_map.deserialize_json(
            data["scopeTags"]
        )
    return out


def redact_sensitive(value: UpdateNetworkMigrationDefinitionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "scope_tags" in value:
        out["scope_tags"] = "*** Sensitive Data Redacted ***"
    return out
