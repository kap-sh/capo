"""Generated from Smithy shape ``com.amazonaws.elasticache#CompleteMigrationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.boolean
    import capo_elasticache.types.string


class CompleteMigrationMessage(TypedDict, closed=True):
    replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ID of the replication group to which data is being migrated.</p>"""
    serverless_cache_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the serverless cache to which data is being migrated.</p>"""
    force: NotRequired["capo_elasticache.types.boolean.Boolean"]
    """<p>Forces the migration to stop without ensuring that data is in sync. It is recommended to use this option only to abort the migration and not recommended when application wants to continue migration to ElastiCache.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CompleteMigrationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "replication_group_id" in value:
        pairs.append(
            (f"{key_prefix}ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "serverless_cache_name" in value:
        pairs.append(
            (f"{key_prefix}ServerlessCacheName", str(value["serverless_cache_name"]))
        )
    if "force" in value:
        pairs.append((f"{key_prefix}Force", "true" if value["force"] else "false"))


def deserialize_query(el: Element) -> CompleteMigrationMessage:
    out: CompleteMigrationMessage = {}  # type: ignore[typeddict-item]
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_serverless_cache_name = el.find("ServerlessCacheName")
    if child_serverless_cache_name is not None:
        out["serverless_cache_name"] = str(child_serverless_cache_name.text or "")
    child_force = el.find("Force")
    if child_force is not None:
        out["force"] = (child_force.text or "").lower() == "true"
    return out
