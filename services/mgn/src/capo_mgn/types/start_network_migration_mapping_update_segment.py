"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationMappingUpdateSegment``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.scope_tags_map
    import capo_mgn.types.segment_id


class StartNetworkMigrationMappingUpdateSegment(TypedDict, closed=True):
    segment_id: "capo_mgn.types.segment_id.SegmentID"
    """<p>The ID of the segment to update.</p>"""
    target_account: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>The updated target AWS account for the segment.</p>"""
    scope_tags: NotRequired["capo_mgn.types.scope_tags_map.ScopeTagsMap"]
    """<p>The updated scope tags for the segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationMappingUpdateSegment) -> dict:
    out: dict = {}
    out["segmentID"] = value["segment_id"]
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
    else:
        out["segment_id"] = ""
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
    if "scope_tags" in value:
        out["scope_tags"] = "*** Sensitive Data Redacted ***"
    return out
