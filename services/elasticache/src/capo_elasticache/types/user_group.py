"""Generated from Smithy shape ``com.amazonaws.elasticache#UserGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.engine_type
    import capo_elasticache.types.string
    import capo_elasticache.types.ug_replication_group_id_list
    import capo_elasticache.types.ug_serverless_cache_id_list
    import capo_elasticache.types.user_group_pending_changes
    import capo_elasticache.types.user_id_list


class UserGroup(TypedDict, closed=True):
    user_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ID of the user group.</p>"""
    status: NotRequired["capo_elasticache.types.string.String"]
    """<p>Indicates user group status. Can be "creating", "active", "modifying", "deleting".</p>"""
    engine: NotRequired["capo_elasticache.types.engine_type.EngineType"]
    """<p>The options are valkey or redis.</p>"""
    user_ids: NotRequired["capo_elasticache.types.user_id_list.UserIdList"]
    """<p>The list of user IDs that belong to the user group.</p>"""
    minimum_engine_version: NotRequired["capo_elasticache.types.string.String"]
    """<p>The minimum engine version required, which is Redis OSS 6.0</p>"""
    pending_changes: NotRequired[
        "capo_elasticache.types.user_group_pending_changes.UserGroupPendingChanges"
    ]
    """<p>A list of updates being applied to the user group.</p>"""
    replication_groups: NotRequired[
        "capo_elasticache.types.ug_replication_group_id_list.UGReplicationGroupIdList"
    ]
    """<p>A list of replication groups that the user group can access.</p>"""
    serverless_caches: NotRequired[
        "capo_elasticache.types.ug_serverless_cache_id_list.UGServerlessCacheIdList"
    ]
    """<p>Indicates which serverless caches the specified user group is associated with. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the user group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UserGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "user_group_id" in value:
        pairs.append((f"{key_prefix}UserGroupId", str(value["user_group_id"])))
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "user_ids" in value:
        import capo_elasticache.types.user_id_list

        capo_elasticache.types.user_id_list.serialize_query(
            value["user_ids"], pairs, f"{key_prefix}UserIds"
        )
    if "minimum_engine_version" in value:
        pairs.append(
            (f"{key_prefix}MinimumEngineVersion", str(value["minimum_engine_version"]))
        )
    if "pending_changes" in value:
        import capo_elasticache.types.user_group_pending_changes

        capo_elasticache.types.user_group_pending_changes.serialize_query(
            value["pending_changes"], pairs, f"{key_prefix}PendingChanges"
        )
    if "replication_groups" in value:
        import capo_elasticache.types.ug_replication_group_id_list

        capo_elasticache.types.ug_replication_group_id_list.serialize_query(
            value["replication_groups"], pairs, f"{key_prefix}ReplicationGroups"
        )
    if "serverless_caches" in value:
        import capo_elasticache.types.ug_serverless_cache_id_list

        capo_elasticache.types.ug_serverless_cache_id_list.serialize_query(
            value["serverless_caches"], pairs, f"{key_prefix}ServerlessCaches"
        )
    if "arn" in value:
        pairs.append((f"{key_prefix}ARN", str(value["arn"])))


def deserialize_query(el: Element) -> UserGroup:
    out: UserGroup = {}  # type: ignore[typeddict-item]
    child_user_group_id = el.find("UserGroupId")
    if child_user_group_id is not None:
        out["user_group_id"] = str(child_user_group_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_user_ids = el.find("UserIds")
    if child_user_ids is not None:
        import capo_elasticache.types.user_id_list

        out["user_ids"] = capo_elasticache.types.user_id_list.deserialize_query(
            child_user_ids
        )
    child_minimum_engine_version = el.find("MinimumEngineVersion")
    if child_minimum_engine_version is not None:
        out["minimum_engine_version"] = str(child_minimum_engine_version.text or "")
    child_pending_changes = el.find("PendingChanges")
    if child_pending_changes is not None:
        import capo_elasticache.types.user_group_pending_changes

        out["pending_changes"] = (
            capo_elasticache.types.user_group_pending_changes.deserialize_query(
                child_pending_changes
            )
        )
    child_replication_groups = el.find("ReplicationGroups")
    if child_replication_groups is not None:
        import capo_elasticache.types.ug_replication_group_id_list

        out["replication_groups"] = (
            capo_elasticache.types.ug_replication_group_id_list.deserialize_query(
                child_replication_groups
            )
        )
    child_serverless_caches = el.find("ServerlessCaches")
    if child_serverless_caches is not None:
        import capo_elasticache.types.ug_serverless_cache_id_list

        out["serverless_caches"] = (
            capo_elasticache.types.ug_serverless_cache_id_list.deserialize_query(
                child_serverless_caches
            )
        )
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out
