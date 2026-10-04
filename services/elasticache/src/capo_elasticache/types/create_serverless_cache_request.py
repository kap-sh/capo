"""Generated from Smithy shape ``com.amazonaws.elasticache#CreateServerlessCacheRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.cache_usage_limits
    import capo_elasticache.types.connection_type
    import capo_elasticache.types.integer_optional
    import capo_elasticache.types.network_type
    import capo_elasticache.types.security_group_ids_list
    import capo_elasticache.types.snapshot_arns_list
    import capo_elasticache.types.string
    import capo_elasticache.types.subnet_ids_list
    import capo_elasticache.types.tag_list


class CreateServerlessCacheRequest(TypedDict, closed=True):
    serverless_cache_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>User-provided identifier for the serverless cache. This parameter is stored as a lowercase string.</p>"""
    description: NotRequired["capo_elasticache.types.string.String"]
    """<p>User-provided description for the serverless cache. The default is NULL, i.e. if no description is provided then an empty string will be returned. The maximum length is 255 characters. </p>"""
    engine: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache engine to be used for creating the serverless cache.</p>"""
    major_engine_version: NotRequired["capo_elasticache.types.string.String"]
    """<p>The version of the cache engine that will be used to create the serverless cache.</p>"""
    cache_usage_limits: NotRequired[
        "capo_elasticache.types.cache_usage_limits.CacheUsageLimits"
    ]
    """<p>Sets the cache usage limits for storage and ElastiCache Processing Units for the cache.</p>"""
    kms_key_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>ARN of the customer managed key for encrypting the data at rest. If no KMS key is provided, a default service key is used.</p>"""
    security_group_ids: NotRequired[
        "capo_elasticache.types.security_group_ids_list.SecurityGroupIdsList"
    ]
    """<p>A list of the one or more VPC security groups to be associated with the serverless cache. The security group will authorize traffic access for the VPC end-point (private-link). If no other information is given this will be the VPC’s Default Security Group that is associated with the cluster VPC end-point.</p>"""
    snapshot_arns_to_restore: NotRequired[
        "capo_elasticache.types.snapshot_arns_list.SnapshotArnsList"
    ]
    """<p>The ARN(s) of the snapshot that the new serverless cache will be created from. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    tags: NotRequired["capo_elasticache.types.tag_list.TagList"]
    """<p>The list of tags (key, value) pairs to be added to the serverless cache resource. Default is NULL.</p>"""
    user_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The identifier of the UserGroup to be associated with the serverless cache. Available for Valkey and Redis OSS only. Default is NULL.</p>"""
    subnet_ids: NotRequired["capo_elasticache.types.subnet_ids_list.SubnetIdsList"]
    """<p>A list of the identifiers of the subnets where the VPC endpoint for the serverless cache will be deployed. All the subnetIds must belong to the same VPC.</p>"""
    snapshot_retention_limit: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which ElastiCache retains automatic snapshots before deleting them. Available for Valkey, Redis OSS and Serverless Memcached only. The maximum value allowed is 35 days.</p>"""
    daily_snapshot_time: NotRequired["capo_elasticache.types.string.String"]
    """<p>The daily time that snapshots will be created from the new serverless cache. By default this number is populated with 0, i.e. no snapshots will be created on an automatic daily basis. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    network_type: NotRequired["capo_elasticache.types.network_type.NetworkType"]
    """<p>The IP protocol version used by the serverless cache. Must be either <code>ipv4</code> | <code>ipv6</code> | <code>dual_stack</code>. <code>ipv6</code> is only supported with IPv6-only subnets. If not specified, defaults to <code>ipv4</code>, unless all provided subnets are IPv6-only, in which case it defaults to <code>ipv6</code>. </p>"""
    connection_type: NotRequired[
        "capo_elasticache.types.connection_type.ConnectionType"
    ]
    """<p>The connection type for the serverless cache. Must be either <code>vpc</code> | <code>public</code>. Use <code>vpc</code> to access the cache through a VPC endpoint, or <code>public</code> to access the cache over the internet. If not specified, defaults to <code>vpc</code>. This value cannot be changed after the serverless cache is created. Setting this to <code>public</code> requires Valkey 9 or above.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateServerlessCacheRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "serverless_cache_name" in value:
        pairs.append(
            (f"{key_prefix}ServerlessCacheName", str(value["serverless_cache_name"]))
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "major_engine_version" in value:
        pairs.append(
            (f"{key_prefix}MajorEngineVersion", str(value["major_engine_version"]))
        )
    if "cache_usage_limits" in value:
        import capo_elasticache.types.cache_usage_limits

        capo_elasticache.types.cache_usage_limits.serialize_query(
            value["cache_usage_limits"], pairs, f"{key_prefix}CacheUsageLimits"
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "security_group_ids" in value:
        import capo_elasticache.types.security_group_ids_list

        capo_elasticache.types.security_group_ids_list.serialize_query(
            value["security_group_ids"], pairs, f"{key_prefix}SecurityGroupIds"
        )
    if "snapshot_arns_to_restore" in value:
        import capo_elasticache.types.snapshot_arns_list

        capo_elasticache.types.snapshot_arns_list.serialize_query(
            value["snapshot_arns_to_restore"],
            pairs,
            f"{key_prefix}SnapshotArnsToRestore",
        )
    if "tags" in value:
        import capo_elasticache.types.tag_list

        capo_elasticache.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "user_group_id" in value:
        pairs.append((f"{key_prefix}UserGroupId", str(value["user_group_id"])))
    if "subnet_ids" in value:
        import capo_elasticache.types.subnet_ids_list

        capo_elasticache.types.subnet_ids_list.serialize_query(
            value["subnet_ids"], pairs, f"{key_prefix}SubnetIds"
        )
    if "snapshot_retention_limit" in value:
        pairs.append(
            (
                f"{key_prefix}SnapshotRetentionLimit",
                str(value["snapshot_retention_limit"]),
            )
        )
    if "daily_snapshot_time" in value:
        pairs.append(
            (f"{key_prefix}DailySnapshotTime", str(value["daily_snapshot_time"]))
        )
    if "network_type" in value:
        import capo_elasticache.types.network_type

        capo_elasticache.types.network_type.serialize_query(
            value["network_type"], pairs, f"{key_prefix}NetworkType"
        )
    if "connection_type" in value:
        import capo_elasticache.types.connection_type

        capo_elasticache.types.connection_type.serialize_query(
            value["connection_type"], pairs, f"{key_prefix}ConnectionType"
        )


def deserialize_query(el: Element) -> CreateServerlessCacheRequest:
    out: CreateServerlessCacheRequest = {}  # type: ignore[typeddict-item]
    child_serverless_cache_name = el.find("ServerlessCacheName")
    if child_serverless_cache_name is not None:
        out["serverless_cache_name"] = str(child_serverless_cache_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_major_engine_version = el.find("MajorEngineVersion")
    if child_major_engine_version is not None:
        out["major_engine_version"] = str(child_major_engine_version.text or "")
    child_cache_usage_limits = el.find("CacheUsageLimits")
    if child_cache_usage_limits is not None:
        import capo_elasticache.types.cache_usage_limits

        out["cache_usage_limits"] = (
            capo_elasticache.types.cache_usage_limits.deserialize_query(
                child_cache_usage_limits
            )
        )
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_security_group_ids = el.find("SecurityGroupIds")
    if child_security_group_ids is not None:
        import capo_elasticache.types.security_group_ids_list

        out["security_group_ids"] = (
            capo_elasticache.types.security_group_ids_list.deserialize_query(
                child_security_group_ids
            )
        )
    child_snapshot_arns_to_restore = el.find("SnapshotArnsToRestore")
    if child_snapshot_arns_to_restore is not None:
        import capo_elasticache.types.snapshot_arns_list

        out["snapshot_arns_to_restore"] = (
            capo_elasticache.types.snapshot_arns_list.deserialize_query(
                child_snapshot_arns_to_restore
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elasticache.types.tag_list

        out["tags"] = capo_elasticache.types.tag_list.deserialize_query(child_tags)
    child_user_group_id = el.find("UserGroupId")
    if child_user_group_id is not None:
        out["user_group_id"] = str(child_user_group_id.text or "")
    child_subnet_ids = el.find("SubnetIds")
    if child_subnet_ids is not None:
        import capo_elasticache.types.subnet_ids_list

        out["subnet_ids"] = capo_elasticache.types.subnet_ids_list.deserialize_query(
            child_subnet_ids
        )
    child_snapshot_retention_limit = el.find("SnapshotRetentionLimit")
    if child_snapshot_retention_limit is not None:
        out["snapshot_retention_limit"] = int(child_snapshot_retention_limit.text or "")
    child_daily_snapshot_time = el.find("DailySnapshotTime")
    if child_daily_snapshot_time is not None:
        out["daily_snapshot_time"] = str(child_daily_snapshot_time.text or "")
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        import capo_elasticache.types.network_type

        out["network_type"] = capo_elasticache.types.network_type.deserialize_query(
            child_network_type
        )
    child_connection_type = el.find("ConnectionType")
    if child_connection_type is not None:
        import capo_elasticache.types.connection_type

        out["connection_type"] = (
            capo_elasticache.types.connection_type.deserialize_query(
                child_connection_type
            )
        )
    return out
