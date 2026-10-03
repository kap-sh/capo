"""Generated from Smithy shape ``com.amazonaws.elasticache#UpdateAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.cache_node_update_status_list
    import capo_elasticache.types.node_group_update_status_list
    import capo_elasticache.types.service_update_severity
    import capo_elasticache.types.service_update_status
    import capo_elasticache.types.service_update_type
    import capo_elasticache.types.sla_met
    import capo_elasticache.types.string
    import capo_elasticache.types.t_stamp
    import capo_elasticache.types.update_action_status


class UpdateAction(TypedDict, closed=True):
    replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ID of the replication group</p>"""
    cache_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ID of the cache cluster</p>"""
    service_update_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The unique ID of the service update</p>"""
    service_update_release_date: NotRequired["capo_elasticache.types.t_stamp.TStamp"]
    """<p>The date the update is first available</p>"""
    service_update_severity: NotRequired[
        "capo_elasticache.types.service_update_severity.ServiceUpdateSeverity"
    ]
    """<p>The severity of the service update</p>"""
    service_update_status: NotRequired[
        "capo_elasticache.types.service_update_status.ServiceUpdateStatus"
    ]
    """<p>The status of the service update</p>"""
    service_update_recommended_apply_by_date: NotRequired[
        "capo_elasticache.types.t_stamp.TStamp"
    ]
    """<p>The recommended date to apply the service update to ensure compliance. For information on compliance, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/elasticache-compliance.html#elasticache-compliance-self-service">Self-Service Security Updates for Compliance</a>.</p>"""
    service_update_type: NotRequired[
        "capo_elasticache.types.service_update_type.ServiceUpdateType"
    ]
    """<p>Reflects the nature of the service update </p>"""
    update_action_available_date: NotRequired["capo_elasticache.types.t_stamp.TStamp"]
    """<p>The date that the service update is available to a replication group</p>"""
    update_action_status: NotRequired[
        "capo_elasticache.types.update_action_status.UpdateActionStatus"
    ]
    """<p>The status of the update action</p>"""
    nodes_updated: NotRequired["capo_elasticache.types.string.String"]
    """<p>The progress of the service update on the replication group</p>"""
    update_action_status_modified_date: NotRequired[
        "capo_elasticache.types.t_stamp.TStamp"
    ]
    """<p>The date when the UpdateActionStatus was last modified</p>"""
    sla_met: NotRequired["capo_elasticache.types.sla_met.SlaMet"]
    """<p>If yes, all nodes in the replication group have been updated by the recommended apply-by date. If no, at least one node in the replication group have not been updated by the recommended apply-by date. If N/A, the replication group was created after the recommended apply-by date.</p>"""
    node_group_update_status: NotRequired[
        "capo_elasticache.types.node_group_update_status_list.NodeGroupUpdateStatusList"
    ]
    """<p>The status of the service update on the node group</p>"""
    cache_node_update_status: NotRequired[
        "capo_elasticache.types.cache_node_update_status_list.CacheNodeUpdateStatusList"
    ]
    """<p>The status of the service update on the cache node</p>"""
    estimated_update_time: NotRequired["capo_elasticache.types.string.String"]
    """<p>The estimated length of time for the update to complete</p>"""
    engine: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Elasticache engine to which the update applies. Either Valkey, Redis OSS or Memcached.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "replication_group_id" in value:
        pairs.append(
            (f"{key_prefix}ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "cache_cluster_id" in value:
        pairs.append((f"{key_prefix}CacheClusterId", str(value["cache_cluster_id"])))
    if "service_update_name" in value:
        pairs.append(
            (f"{key_prefix}ServiceUpdateName", str(value["service_update_name"]))
        )
    if "service_update_release_date" in value:
        import capo_elasticache.types.t_stamp

        capo_elasticache.types.t_stamp.serialize_query(
            value["service_update_release_date"],
            pairs,
            f"{key_prefix}ServiceUpdateReleaseDate",
        )
    if "service_update_severity" in value:
        import capo_elasticache.types.service_update_severity

        capo_elasticache.types.service_update_severity.serialize_query(
            value["service_update_severity"],
            pairs,
            f"{key_prefix}ServiceUpdateSeverity",
        )
    if "service_update_status" in value:
        import capo_elasticache.types.service_update_status

        capo_elasticache.types.service_update_status.serialize_query(
            value["service_update_status"], pairs, f"{key_prefix}ServiceUpdateStatus"
        )
    if "service_update_recommended_apply_by_date" in value:
        import capo_elasticache.types.t_stamp

        capo_elasticache.types.t_stamp.serialize_query(
            value["service_update_recommended_apply_by_date"],
            pairs,
            f"{key_prefix}ServiceUpdateRecommendedApplyByDate",
        )
    if "service_update_type" in value:
        import capo_elasticache.types.service_update_type

        capo_elasticache.types.service_update_type.serialize_query(
            value["service_update_type"], pairs, f"{key_prefix}ServiceUpdateType"
        )
    if "update_action_available_date" in value:
        import capo_elasticache.types.t_stamp

        capo_elasticache.types.t_stamp.serialize_query(
            value["update_action_available_date"],
            pairs,
            f"{key_prefix}UpdateActionAvailableDate",
        )
    if "update_action_status" in value:
        import capo_elasticache.types.update_action_status

        capo_elasticache.types.update_action_status.serialize_query(
            value["update_action_status"], pairs, f"{key_prefix}UpdateActionStatus"
        )
    if "nodes_updated" in value:
        pairs.append((f"{key_prefix}NodesUpdated", str(value["nodes_updated"])))
    if "update_action_status_modified_date" in value:
        import capo_elasticache.types.t_stamp

        capo_elasticache.types.t_stamp.serialize_query(
            value["update_action_status_modified_date"],
            pairs,
            f"{key_prefix}UpdateActionStatusModifiedDate",
        )
    if "sla_met" in value:
        import capo_elasticache.types.sla_met

        capo_elasticache.types.sla_met.serialize_query(
            value["sla_met"], pairs, f"{key_prefix}SlaMet"
        )
    if "node_group_update_status" in value:
        import capo_elasticache.types.node_group_update_status_list

        capo_elasticache.types.node_group_update_status_list.serialize_query(
            value["node_group_update_status"],
            pairs,
            f"{key_prefix}NodeGroupUpdateStatus",
        )
    if "cache_node_update_status" in value:
        import capo_elasticache.types.cache_node_update_status_list

        capo_elasticache.types.cache_node_update_status_list.serialize_query(
            value["cache_node_update_status"],
            pairs,
            f"{key_prefix}CacheNodeUpdateStatus",
        )
    if "estimated_update_time" in value:
        pairs.append(
            (f"{key_prefix}EstimatedUpdateTime", str(value["estimated_update_time"]))
        )
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))


def deserialize_query(el: Element) -> UpdateAction:
    out: UpdateAction = {}  # type: ignore[typeddict-item]
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_cache_cluster_id = el.find("CacheClusterId")
    if child_cache_cluster_id is not None:
        out["cache_cluster_id"] = str(child_cache_cluster_id.text or "")
    child_service_update_name = el.find("ServiceUpdateName")
    if child_service_update_name is not None:
        out["service_update_name"] = str(child_service_update_name.text or "")
    child_service_update_release_date = el.find("ServiceUpdateReleaseDate")
    if child_service_update_release_date is not None:
        import capo_elasticache.types.t_stamp

        out["service_update_release_date"] = (
            capo_elasticache.types.t_stamp.deserialize_query(
                child_service_update_release_date
            )
        )
    child_service_update_severity = el.find("ServiceUpdateSeverity")
    if child_service_update_severity is not None:
        import capo_elasticache.types.service_update_severity

        out["service_update_severity"] = (
            capo_elasticache.types.service_update_severity.deserialize_query(
                child_service_update_severity
            )
        )
    child_service_update_status = el.find("ServiceUpdateStatus")
    if child_service_update_status is not None:
        import capo_elasticache.types.service_update_status

        out["service_update_status"] = (
            capo_elasticache.types.service_update_status.deserialize_query(
                child_service_update_status
            )
        )
    child_service_update_recommended_apply_by_date = el.find(
        "ServiceUpdateRecommendedApplyByDate"
    )
    if child_service_update_recommended_apply_by_date is not None:
        import capo_elasticache.types.t_stamp

        out["service_update_recommended_apply_by_date"] = (
            capo_elasticache.types.t_stamp.deserialize_query(
                child_service_update_recommended_apply_by_date
            )
        )
    child_service_update_type = el.find("ServiceUpdateType")
    if child_service_update_type is not None:
        import capo_elasticache.types.service_update_type

        out["service_update_type"] = (
            capo_elasticache.types.service_update_type.deserialize_query(
                child_service_update_type
            )
        )
    child_update_action_available_date = el.find("UpdateActionAvailableDate")
    if child_update_action_available_date is not None:
        import capo_elasticache.types.t_stamp

        out["update_action_available_date"] = (
            capo_elasticache.types.t_stamp.deserialize_query(
                child_update_action_available_date
            )
        )
    child_update_action_status = el.find("UpdateActionStatus")
    if child_update_action_status is not None:
        import capo_elasticache.types.update_action_status

        out["update_action_status"] = (
            capo_elasticache.types.update_action_status.deserialize_query(
                child_update_action_status
            )
        )
    child_nodes_updated = el.find("NodesUpdated")
    if child_nodes_updated is not None:
        out["nodes_updated"] = str(child_nodes_updated.text or "")
    child_update_action_status_modified_date = el.find("UpdateActionStatusModifiedDate")
    if child_update_action_status_modified_date is not None:
        import capo_elasticache.types.t_stamp

        out["update_action_status_modified_date"] = (
            capo_elasticache.types.t_stamp.deserialize_query(
                child_update_action_status_modified_date
            )
        )
    child_sla_met = el.find("SlaMet")
    if child_sla_met is not None:
        import capo_elasticache.types.sla_met

        out["sla_met"] = capo_elasticache.types.sla_met.deserialize_query(child_sla_met)
    child_node_group_update_status = el.find("NodeGroupUpdateStatus")
    if child_node_group_update_status is not None:
        import capo_elasticache.types.node_group_update_status_list

        out["node_group_update_status"] = (
            capo_elasticache.types.node_group_update_status_list.deserialize_query(
                child_node_group_update_status
            )
        )
    child_cache_node_update_status = el.find("CacheNodeUpdateStatus")
    if child_cache_node_update_status is not None:
        import capo_elasticache.types.cache_node_update_status_list

        out["cache_node_update_status"] = (
            capo_elasticache.types.cache_node_update_status_list.deserialize_query(
                child_cache_node_update_status
            )
        )
    child_estimated_update_time = el.find("EstimatedUpdateTime")
    if child_estimated_update_time is not None:
        out["estimated_update_time"] = str(child_estimated_update_time.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    return out
