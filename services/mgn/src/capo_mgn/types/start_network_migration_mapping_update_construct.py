"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationMappingUpdateConstruct``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.construct_id
    import capo_mgn.types.network_migration_mapper_segment_construct_type
    import capo_mgn.types.operation_union
    import capo_mgn.types.segment_id


class StartNetworkMigrationMappingUpdateConstruct(TypedDict, closed=True):
    segment_id: "capo_mgn.types.segment_id.SegmentID"
    """<p>The ID of the segment containing the construct.</p>"""
    construct_id: "capo_mgn.types.construct_id.ConstructID"
    """<p>The ID of the construct to update.</p>"""
    construct_type: "capo_mgn.types.network_migration_mapper_segment_construct_type.NetworkMigrationMapperSegmentConstructType"
    """<p>The type of the construct.</p>"""
    operation: NotRequired["capo_mgn.types.operation_union.OperationUnion"]
    """<p>The operation to perform on the construct.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationMappingUpdateConstruct) -> dict:
    out: dict = {}
    out["segmentID"] = value["segment_id"]
    out["constructID"] = value["construct_id"]
    out["constructType"] = value["construct_type"]
    if "operation" in value:
        import capo_mgn.types.operation_union

        out["operation"] = capo_mgn.types.operation_union.serialize_json(
            value["operation"]
        )
    return out


def deserialize_json(data: dict) -> StartNetworkMigrationMappingUpdateConstruct:
    out: StartNetworkMigrationMappingUpdateConstruct = {}  # type: ignore[typeddict-item]
    if data.get("segmentID") is not None:
        out["segment_id"] = data["segmentID"]
    else:
        out["segment_id"] = ""
    if data.get("constructID") is not None:
        out["construct_id"] = data["constructID"]
    else:
        out["construct_id"] = ""
    if data.get("constructType") is not None:
        out["construct_type"] = data["constructType"]
    else:
        out["construct_type"] = ""
    if data.get("operation") is not None:
        import capo_mgn.types.operation_union

        out["operation"] = capo_mgn.types.operation_union.deserialize_json(
            data["operation"]
        )
    return out
