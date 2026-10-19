"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateNetworkMigrationMapperSegmentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.network_migration_execution_id
    import capo_mgn.types.scope_tags_map
    import capo_mgn.types.segment_id


class UpdateNetworkMigrationMapperSegmentRequest(TypedDict, closed=True):
    network_migration_definition_id: (
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition.</p>"""
    network_migration_execution_id: (
        "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    )
    """<p>The unique identifier of the network migration execution.</p>"""
    segment_id: "capo_mgn.types.segment_id.SegmentID"
    """<p>The unique identifier of the segment to update.</p>"""
    scope_tags: NotRequired["capo_mgn.types.scope_tags_map.ScopeTagsMap"]
    """<p>The updated scope tags for the segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNetworkMigrationMapperSegmentRequest) -> dict:
    out: dict = {}
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    out["segmentID"] = value["segment_id"]
    if "scope_tags" in value:
        import capo_mgn.types.scope_tags_map

        out["scopeTags"] = capo_mgn.types.scope_tags_map.serialize_json(
            value["scope_tags"]
        )
    return out


def deserialize_json(data: dict) -> UpdateNetworkMigrationMapperSegmentRequest:
    out: UpdateNetworkMigrationMapperSegmentRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("scopeTags") is not None:
        import capo_mgn.types.scope_tags_map

        out["scope_tags"] = capo_mgn.types.scope_tags_map.deserialize_json(
            data["scopeTags"]
        )
    return out


def redact_sensitive(
    value: UpdateNetworkMigrationMapperSegmentRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "scope_tags" in value:
        out["scope_tags"] = "*** Sensitive Data Redacted ***"
    return out
