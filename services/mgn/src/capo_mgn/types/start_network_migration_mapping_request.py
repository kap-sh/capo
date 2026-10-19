"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.network_migration_execution_id
    import capo_mgn.types.security_group_mapping_strategy


class StartNetworkMigrationMappingRequest(TypedDict, closed=True):
    network_migration_execution_id: (
        "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    )
    """<p>The unique identifier of the network migration execution.</p>"""
    network_migration_definition_id: (
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition.</p>"""
    security_group_mapping_strategy: NotRequired[
        "capo_mgn.types.security_group_mapping_strategy.SecurityGroupMappingStrategy"
    ]
    """<p>The security group mapping strategy to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationMappingRequest) -> dict:
    out: dict = {}
    out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "security_group_mapping_strategy" in value:
        out["securityGroupMappingStrategy"] = value["security_group_mapping_strategy"]
    return out


def deserialize_json(data: dict) -> StartNetworkMigrationMappingRequest:
    out: StartNetworkMigrationMappingRequest = {}  # type: ignore[typeddict-item]
    if data.get("networkMigrationExecutionID") is not None:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    else:
        out["network_migration_execution_id"] = ""
    if data.get("networkMigrationDefinitionID") is not None:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        out["network_migration_definition_id"] = ""
    if data.get("securityGroupMappingStrategy") is not None:
        out["security_group_mapping_strategy"] = data["securityGroupMappingStrategy"]
    return out
