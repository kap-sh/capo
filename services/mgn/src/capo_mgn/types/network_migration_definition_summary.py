"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationDefinitionSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.arn
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.network_migration_definition_name
    import capo_mgn.types.scope_tags_map
    import capo_mgn.types.source_environment
    import capo_mgn.types.tags_map


class NetworkMigrationDefinitionSummary(TypedDict, closed=True):
    network_migration_definition_id: NotRequired[
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    ]
    """<p>The unique identifier of the network migration definition.</p>"""
    name: NotRequired[
        "capo_mgn.types.network_migration_definition_name.NetworkMigrationDefinitionName"
    ]
    """<p>The name of the network migration definition.</p>"""
    source_environment: NotRequired[
        "capo_mgn.types.source_environment.SourceEnvironment"
    ]
    """<p>The source environment configuration.</p>"""
    arn: NotRequired["capo_mgn.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the network migration definition.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Tags assigned to the network migration definition.</p>"""
    scope_tags: NotRequired["capo_mgn.types.scope_tags_map.ScopeTagsMap"]
    """<p>Scope tags for the network migration definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationDefinitionSummary) -> dict:
    out: dict = {}
    if "network_migration_definition_id" in value:
        out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "source_environment" in value:
        out["sourceEnvironment"] = value["source_environment"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    if "scope_tags" in value:
        import capo_mgn.types.scope_tags_map

        out["scopeTags"] = capo_mgn.types.scope_tags_map.serialize_json(
            value["scope_tags"]
        )
    return out


def deserialize_json(data: dict) -> NetworkMigrationDefinitionSummary:
    out: NetworkMigrationDefinitionSummary = {}  # type: ignore[typeddict-item]
    if data.get("networkMigrationDefinitionID") is not None:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("sourceEnvironment") is not None:
        out["source_environment"] = data["sourceEnvironment"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("tags") is not None:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    if data.get("scopeTags") is not None:
        import capo_mgn.types.scope_tags_map

        out["scope_tags"] = capo_mgn.types.scope_tags_map.deserialize_json(
            data["scopeTags"]
        )
    return out


def redact_sensitive(value: NetworkMigrationDefinitionSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    if "scope_tags" in value:
        out["scope_tags"] = "*** Sensitive Data Redacted ***"
    return out
