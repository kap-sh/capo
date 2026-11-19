"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationMappingUpdateSegment``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.scope_tags_map
    import capo_mgn.types.segment_id
    import capo_mgn.types.segment_logical_id
    import capo_mgn.types.segment_operation


class StartNetworkMigrationMappingUpdateSegment(TypedDict, closed=True):
    segment_id: NotRequired["capo_mgn.types.segment_id.SegmentID"]
    """<p>The ID of the segment to update.</p>"""
    segment_logical_id: NotRequired[
        "capo_mgn.types.segment_logical_id.SegmentLogicalID"
    ]
    """<p>An identifier that you choose for a segment created by this request. You can use it in other constructs in the same request to refer to the new segment.</p>"""
    operation: NotRequired["capo_mgn.types.segment_operation.SegmentOperation"]
    """<p>The operation to perform on the segment.</p>"""
    target_account: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>The updated target AWS account for the segment.</p>"""
    scope_tags: NotRequired["capo_mgn.types.scope_tags_map.ScopeTagsMap"]
    """<p>The updated scope tags for the segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationMappingUpdateSegment) -> dict:
    out: dict = {}
    if "segment_id" in value:
        out["segmentID"] = value["segment_id"]
    if "segment_logical_id" in value:
        out["segmentLogicalID"] = value["segment_logical_id"]
    if "operation" in value:
        import capo_mgn.types.segment_operation

        out["operation"] = capo_mgn.types.segment_operation.serialize_json(
            value["operation"]
        )
    if "target_account" in value:
        out["targetAccount"] = value["target_account"]
    if "scope_tags" in value:
        import capo_mgn.types.scope_tags_map

        out["scopeTags"] = capo_mgn.types.scope_tags_map.serialize_json(
            value["scope_tags"]
        )
    return out


def deserialize_json(data: dict) -> StartNetworkMigrationMappingUpdateSegment:
    out: StartNetworkMigrationMappingUpdateSegment = {}  # type: ignore[typeddict-item]
    if data.get("segmentID") is not None:
        out["segment_id"] = data["segmentID"]
    if data.get("segmentLogicalID") is not None:
        out["segment_logical_id"] = data["segmentLogicalID"]
    if data.get("operation") is not None:
        import capo_mgn.types.segment_operation

        out["operation"] = capo_mgn.types.segment_operation.deserialize_json(
            data["operation"]
        )
    if data.get("targetAccount") is not None:
        out["target_account"] = data["targetAccount"]
    if data.get("scopeTags") is not None:
        import capo_mgn.types.scope_tags_map

        out["scope_tags"] = capo_mgn.types.scope_tags_map.deserialize_json(
            data["scopeTags"]
        )
    return out


def redact_sensitive(
    value: StartNetworkMigrationMappingUpdateSegment,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "operation" in value:
        import capo_mgn.types.segment_operation

        out["operation"] = capo_mgn.types.segment_operation.redact_sensitive(
            value["operation"]
        )
    if "scope_tags" in value:
        out["scope_tags"] = "*** Sensitive Data Redacted ***"
    return out
