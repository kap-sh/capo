"""Generated from Smithy shape ``com.amazonaws.mgn#SegmentUpdateOperation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.scope_tags_map
    import capo_mgn.types.segment_description
    import capo_mgn.types.segment_name


class SegmentUpdateOperation(TypedDict, closed=True):
    name: NotRequired["capo_mgn.types.segment_name.SegmentName"]
    """<p>The updated name for the segment.</p>"""
    description: NotRequired["capo_mgn.types.segment_description.SegmentDescription"]
    """<p>The updated description for the segment.</p>"""
    target_account: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>The updated target AWS account for the segment.</p>"""
    scope_tags: NotRequired["capo_mgn.types.scope_tags_map.ScopeTagsMap"]
    """<p>The updated scope tags for the segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentUpdateOperation) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "target_account" in value:
        out["targetAccount"] = value["target_account"]
    if "scope_tags" in value:
        import capo_mgn.types.scope_tags_map

        out["scopeTags"] = capo_mgn.types.scope_tags_map.serialize_json(
            value["scope_tags"]
        )
    return out


def deserialize_json(data: dict) -> SegmentUpdateOperation:
    out: SegmentUpdateOperation = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("targetAccount") is not None:
        out["target_account"] = data["targetAccount"]
    if data.get("scopeTags") is not None:
        import capo_mgn.types.scope_tags_map

        out["scope_tags"] = capo_mgn.types.scope_tags_map.deserialize_json(
            data["scopeTags"]
        )
    return out


def redact_sensitive(value: SegmentUpdateOperation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "scope_tags" in value:
        out["scope_tags"] = "*** Sensitive Data Redacted ***"
    return out
