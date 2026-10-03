"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ElasticsearchClusterConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.boolean
    import capo_elasticsearch_service.types.cold_storage_options
    import capo_elasticsearch_service.types.es_partition_instance_type
    import capo_elasticsearch_service.types.es_warm_partition_instance_type
    import capo_elasticsearch_service.types.integer_class
    import capo_elasticsearch_service.types.zone_awareness_config


class ElasticsearchClusterConfig(TypedDict, closed=True):
    instance_type: NotRequired[
        "capo_elasticsearch_service.types.es_partition_instance_type.ESPartitionInstanceType"
    ]
    """<p>The instance type for an Elasticsearch cluster. UltraWarm instance types are not supported for data instances.</p>"""
    instance_count: NotRequired[
        "capo_elasticsearch_service.types.integer_class.IntegerClass"
    ]
    """<p>The number of instances in the specified domain cluster.</p>"""
    dedicated_master_enabled: NotRequired[
        "capo_elasticsearch_service.types.boolean.Boolean"
    ]
    """<p>A boolean value to indicate whether a dedicated master node is enabled. See <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes" target="_blank">About Dedicated Master Nodes</a> for more information.</p>"""
    zone_awareness_enabled: NotRequired[
        "capo_elasticsearch_service.types.boolean.Boolean"
    ]
    """<p>A boolean value to indicate whether zone awareness is enabled. See <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness" target="_blank">About Zone Awareness</a> for more information.</p>"""
    zone_awareness_config: NotRequired[
        "capo_elasticsearch_service.types.zone_awareness_config.ZoneAwarenessConfig"
    ]
    """<p>Specifies the zone awareness configuration for a domain when zone awareness is enabled.</p>"""
    dedicated_master_type: NotRequired[
        "capo_elasticsearch_service.types.es_partition_instance_type.ESPartitionInstanceType"
    ]
    """<p>The instance type for a dedicated master node.</p>"""
    dedicated_master_count: NotRequired[
        "capo_elasticsearch_service.types.integer_class.IntegerClass"
    ]
    """<p>Total number of dedicated master nodes, active and on standby, for the cluster.</p>"""
    warm_enabled: NotRequired["capo_elasticsearch_service.types.boolean.Boolean"]
    """<p>True to enable warm storage.</p>"""
    warm_type: NotRequired[
        "capo_elasticsearch_service.types.es_warm_partition_instance_type.ESWarmPartitionInstanceType"
    ]
    """<p>The instance type for the Elasticsearch cluster's warm nodes.</p>"""
    warm_count: NotRequired[
        "capo_elasticsearch_service.types.integer_class.IntegerClass"
    ]
    """<p>The number of warm nodes in the cluster.</p>"""
    cold_storage_options: NotRequired[
        "capo_elasticsearch_service.types.cold_storage_options.ColdStorageOptions"
    ]
    """<p>Specifies the <code>ColdStorageOptions</code> config for Elasticsearch Domain</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ElasticsearchClusterConfig) -> dict:
    out: dict = {}
    if "instance_type" in value:
        import capo_elasticsearch_service.types.es_partition_instance_type

        out["InstanceType"] = (
            capo_elasticsearch_service.types.es_partition_instance_type.serialize_json(
                value["instance_type"]
            )
        )
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "dedicated_master_enabled" in value:
        out["DedicatedMasterEnabled"] = value["dedicated_master_enabled"]
    if "zone_awareness_enabled" in value:
        out["ZoneAwarenessEnabled"] = value["zone_awareness_enabled"]
    if "zone_awareness_config" in value:
        import capo_elasticsearch_service.types.zone_awareness_config

        out["ZoneAwarenessConfig"] = (
            capo_elasticsearch_service.types.zone_awareness_config.serialize_json(
                value["zone_awareness_config"]
            )
        )
    if "dedicated_master_type" in value:
        import capo_elasticsearch_service.types.es_partition_instance_type

        out["DedicatedMasterType"] = (
            capo_elasticsearch_service.types.es_partition_instance_type.serialize_json(
                value["dedicated_master_type"]
            )
        )
    if "dedicated_master_count" in value:
        out["DedicatedMasterCount"] = value["dedicated_master_count"]
    if "warm_enabled" in value:
        out["WarmEnabled"] = value["warm_enabled"]
    if "warm_type" in value:
        import capo_elasticsearch_service.types.es_warm_partition_instance_type

        out["WarmType"] = (
            capo_elasticsearch_service.types.es_warm_partition_instance_type.serialize_json(
                value["warm_type"]
            )
        )
    if "warm_count" in value:
        out["WarmCount"] = value["warm_count"]
    if "cold_storage_options" in value:
        import capo_elasticsearch_service.types.cold_storage_options

        out["ColdStorageOptions"] = (
            capo_elasticsearch_service.types.cold_storage_options.serialize_json(
                value["cold_storage_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> ElasticsearchClusterConfig:
    out: ElasticsearchClusterConfig = {}  # type: ignore[typeddict-item]
    if data.get("InstanceType") is not None:
        import capo_elasticsearch_service.types.es_partition_instance_type

        out["instance_type"] = (
            capo_elasticsearch_service.types.es_partition_instance_type.deserialize_json(
                data["InstanceType"]
            )
        )
    if data.get("InstanceCount") is not None:
        out["instance_count"] = data["InstanceCount"]
    if data.get("DedicatedMasterEnabled") is not None:
        out["dedicated_master_enabled"] = data["DedicatedMasterEnabled"]
    if data.get("ZoneAwarenessEnabled") is not None:
        out["zone_awareness_enabled"] = data["ZoneAwarenessEnabled"]
    if data.get("ZoneAwarenessConfig") is not None:
        import capo_elasticsearch_service.types.zone_awareness_config

        out["zone_awareness_config"] = (
            capo_elasticsearch_service.types.zone_awareness_config.deserialize_json(
                data["ZoneAwarenessConfig"]
            )
        )
    if data.get("DedicatedMasterType") is not None:
        import capo_elasticsearch_service.types.es_partition_instance_type

        out["dedicated_master_type"] = (
            capo_elasticsearch_service.types.es_partition_instance_type.deserialize_json(
                data["DedicatedMasterType"]
            )
        )
    if data.get("DedicatedMasterCount") is not None:
        out["dedicated_master_count"] = data["DedicatedMasterCount"]
    if data.get("WarmEnabled") is not None:
        out["warm_enabled"] = data["WarmEnabled"]
    if data.get("WarmType") is not None:
        import capo_elasticsearch_service.types.es_warm_partition_instance_type

        out["warm_type"] = (
            capo_elasticsearch_service.types.es_warm_partition_instance_type.deserialize_json(
                data["WarmType"]
            )
        )
    if data.get("WarmCount") is not None:
        out["warm_count"] = data["WarmCount"]
    if data.get("ColdStorageOptions") is not None:
        import capo_elasticsearch_service.types.cold_storage_options

        out["cold_storage_options"] = (
            capo_elasticsearch_service.types.cold_storage_options.deserialize_json(
                data["ColdStorageOptions"]
            )
        )
    return out
