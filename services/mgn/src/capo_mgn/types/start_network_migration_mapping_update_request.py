"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationMappingUpdateRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.network_migration_execution_id
    import capo_mgn.types.start_network_migration_mapping_update_constructs
    import capo_mgn.types.start_network_migration_mapping_update_segments


class StartNetworkMigrationMappingUpdateRequest(TypedDict, closed=True):
    network_migration_execution_id: (
        "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    )
    """<p>The unique identifier of the network migration execution.</p>"""
    network_migration_definition_id: (
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition.</p>"""
    constructs: NotRequired[
        "capo_mgn.types.start_network_migration_mapping_update_constructs.StartNetworkMigrationMappingUpdateConstructs"
    ]
    """<p>A list of construct updates to apply.</p>"""
    segments: NotRequired[
        "capo_mgn.types.start_network_migration_mapping_update_segments.StartNetworkMigrationMappingUpdateSegments"
    ]
    """<p>A list of segment updates to apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationMappingUpdateRequest) -> dict:
    out: dict = {}
    out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "constructs" in value:
        import capo_mgn.types.start_network_migration_mapping_update_constructs

        out["constructs"] = (
            capo_mgn.types.start_network_migration_mapping_update_constructs.serialize_json(
                value["constructs"]
            )
        )
    if "segments" in value:
        import capo_mgn.types.start_network_migration_mapping_update_segments

        out["segments"] = (
            capo_mgn.types.start_network_migration_mapping_update_segments.serialize_json(
                value["segments"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartNetworkMigrationMappingUpdateRequest:
    out: StartNetworkMigrationMappingUpdateRequest = {}  # type: ignore[typeddict-item]
    if data.get("networkMigrationExecutionID") is not None:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    else:
        out["network_migration_execution_id"] = ""
    if data.get("networkMigrationDefinitionID") is not None:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        out["network_migration_definition_id"] = ""
    if data.get("constructs") is not None:
        import capo_mgn.types.start_network_migration_mapping_update_constructs

        out["constructs"] = (
            capo_mgn.types.start_network_migration_mapping_update_constructs.deserialize_json(
                data["constructs"]
            )
        )
    if data.get("segments") is not None:
        import capo_mgn.types.start_network_migration_mapping_update_segments

        out["segments"] = (
            capo_mgn.types.start_network_migration_mapping_update_segments.deserialize_json(
                data["segments"]
            )
        )
    return out


def redact_sensitive(
    value: StartNetworkMigrationMappingUpdateRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "segments" in value:
        import capo_mgn.types.start_network_migration_mapping_update_segments

        out["segments"] = (
            capo_mgn.types.start_network_migration_mapping_update_segments.redact_sensitive(
                value["segments"]
            )
        )
    return out
