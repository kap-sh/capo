"""Generated from Smithy shape ``com.amazonaws.elasticache#StartMigrationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.boolean_optional
    import capo_elasticache.types.customer_node_endpoint_list
    import capo_elasticache.types.string


class StartMigrationMessage(TypedDict, closed=True):
    serverless_cache_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the serverless cache to which data is being migrated.</p>"""
    replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ID of the replication group to which data should be migrated.</p>"""
    customer_node_endpoint_list: NotRequired[
        "capo_elasticache.types.customer_node_endpoint_list.CustomerNodeEndpointList"
    ]
    """<p>The list of endpoints from which to migrate data. For Valkey or Redis OSS (cluster mode disabled), the list should have only one element. For serverless cache migrations, ElastiCache uses the endpoint that you provided in <code>PrepareMigration</code>.</p>"""
    auto_cutover: NotRequired["capo_elasticache.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether ElastiCache automatically attempts to complete the migration after data sync is established.</p>"""
    clear_target_cache_data: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether ElastiCache deletes existing data in the serverless cache before migration begins. After <code>StopMigration</code>, <code>StartMigration</code> requires this option to restart the data sync.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StartMigrationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "serverless_cache_name" in value:
        pairs.append(
            (f"{key_prefix}ServerlessCacheName", str(value["serverless_cache_name"]))
        )
    if "replication_group_id" in value:
        pairs.append(
            (f"{key_prefix}ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "customer_node_endpoint_list" in value:
        import capo_elasticache.types.customer_node_endpoint_list

        capo_elasticache.types.customer_node_endpoint_list.serialize_query(
            value["customer_node_endpoint_list"],
            pairs,
            f"{key_prefix}CustomerNodeEndpointList",
        )
    if "auto_cutover" in value:
        pairs.append(
            (f"{key_prefix}AutoCutover", "true" if value["auto_cutover"] else "false")
        )
    if "clear_target_cache_data" in value:
        pairs.append(
            (
                f"{key_prefix}ClearTargetCacheData",
                "true" if value["clear_target_cache_data"] else "false",
            )
        )


def deserialize_query(el: Element) -> StartMigrationMessage:
    out: StartMigrationMessage = {}  # type: ignore[typeddict-item]
    child_serverless_cache_name = el.find("ServerlessCacheName")
    if child_serverless_cache_name is not None:
        out["serverless_cache_name"] = str(child_serverless_cache_name.text or "")
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_customer_node_endpoint_list = el.find("CustomerNodeEndpointList")
    if child_customer_node_endpoint_list is not None:
        import capo_elasticache.types.customer_node_endpoint_list

        out["customer_node_endpoint_list"] = (
            capo_elasticache.types.customer_node_endpoint_list.deserialize_query(
                child_customer_node_endpoint_list
            )
        )
    child_auto_cutover = el.find("AutoCutover")
    if child_auto_cutover is not None:
        out["auto_cutover"] = (child_auto_cutover.text or "").lower() == "true"
    child_clear_target_cache_data = el.find("ClearTargetCacheData")
    if child_clear_target_cache_data is not None:
        out["clear_target_cache_data"] = (
            child_clear_target_cache_data.text or ""
        ).lower() == "true"
    return out
