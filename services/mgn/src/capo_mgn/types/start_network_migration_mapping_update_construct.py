"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationMappingUpdateConstruct``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.construct_id
    import capo_mgn.types.construct_logical_id
    import capo_mgn.types.logical_id
    import capo_mgn.types.network_migration_mapper_segment_construct_type
    import capo_mgn.types.operation_union
    import capo_mgn.types.segment_id


class StartNetworkMigrationMappingUpdateConstruct(TypedDict, closed=True):
    segment_id: NotRequired["capo_mgn.types.segment_id.SegmentID"]
    """<p>The ID of the segment containing the construct.</p>"""
    segment_logical_id: NotRequired["capo_mgn.types.logical_id.LogicalID"]
    """<p>The identifier of a segment created in the same request that this construct belongs to. Use it instead of <code>segmentID</code> for a new segment.</p>"""
    construct_id: NotRequired["capo_mgn.types.construct_id.ConstructID"]
    """<p>The ID of the construct to update.</p>"""
    construct_type: "capo_mgn.types.network_migration_mapper_segment_construct_type.NetworkMigrationMapperSegmentConstructType"
    """<p>The type of the construct.</p>"""
    construct_logical_id: NotRequired[
        "capo_mgn.types.construct_logical_id.ConstructLogicalID"
    ]
    """<p>The logical identifier for a construct created by a create operation; other operations identify the construct by constructID. Other entries in the same request can reference the new construct as {"Ref": "&lt;constructLogicalID&gt;"}.</p>"""
    operation: NotRequired["capo_mgn.types.operation_union.OperationUnion"]
    """<p>The operation to perform on the construct.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationMappingUpdateConstruct) -> dict:
    out: dict = {}
    if "segment_id" in value:
        out["segmentID"] = value["segment_id"]
    if "segment_logical_id" in value:
        out["segmentLogicalID"] = value["segment_logical_id"]
    if "construct_id" in value:
        out["constructID"] = value["construct_id"]
    out["constructType"] = value["construct_type"]
    if "construct_logical_id" in value:
        out["constructLogicalID"] = value["construct_logical_id"]
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
    if data.get("segmentLogicalID") is not None:
        out["segment_logical_id"] = data["segmentLogicalID"]
    if data.get("constructID") is not None:
        out["construct_id"] = data["constructID"]
    if data.get("constructType") is not None:
        out["construct_type"] = data["constructType"]
    else:
        out["construct_type"] = ""
    if data.get("constructLogicalID") is not None:
        out["construct_logical_id"] = data["constructLogicalID"]
    if data.get("operation") is not None:
        import capo_mgn.types.operation_union

        out["operation"] = capo_mgn.types.operation_union.deserialize_json(
            data["operation"]
        )
    return out
