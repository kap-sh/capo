"""Generated from Smithy shape ``com.amazonaws.mgn#GetNetworkMigrationMapperSegmentConstructRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.construct_id
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.network_migration_execution_id
    import capo_mgn.types.segment_id


class GetNetworkMigrationMapperSegmentConstructRequest(TypedDict, closed=True):
    network_migration_definition_id: (
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition.</p>"""
    network_migration_execution_id: (
        "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    )
    """<p>The unique identifier of the network migration execution.</p>"""
    segment_id: "capo_mgn.types.segment_id.SegmentID"
    """<p>The unique identifier of the mapper segment.</p>"""
    construct_id: "capo_mgn.types.construct_id.ConstructID"
    """<p>The unique identifier of the construct within the segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkMigrationMapperSegmentConstructRequest) -> dict:
    out: dict = {}
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    out["segmentID"] = value["segment_id"]
    out["constructID"] = value["construct_id"]
    return out


def deserialize_json(data: dict) -> GetNetworkMigrationMapperSegmentConstructRequest:
    out: GetNetworkMigrationMapperSegmentConstructRequest = {}  # type: ignore[typeddict-item]
    if data.get("networkMigrationDefinitionID") is not None:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        out["network_migration_definition_id"] = ""
    if data.get("networkMigrationExecutionID") is not None:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    else:
        out["network_migration_execution_id"] = ""
    if data.get("segmentID") is not None:
        out["segment_id"] = data["segmentID"]
    else:
        out["segment_id"] = ""
    if data.get("constructID") is not None:
        out["construct_id"] = data["constructID"]
    else:
        out["construct_id"] = ""
    return out
