"""Generated from Smithy shape ``com.amazonaws.elasticache#ConfigureShard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.allowed_node_group_id
    import capo_elasticache.types.integer
    import capo_elasticache.types.preferred_availability_zone_list
    import capo_elasticache.types.preferred_outpost_arn_list


class ConfigureShard(TypedDict, closed=True):
    node_group_id: NotRequired[
        "capo_elasticache.types.allowed_node_group_id.AllowedNodeGroupId"
    ]
    """<p>The 4-digit id for the node group you are configuring. For Valkey or Redis OSS (cluster mode disabled) replication groups, the node group id is always 0001. To find a Valkey or Redis OSS (cluster mode enabled)'s node group's (shard's) id, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/shard-find-id.html">Finding a Shard's Id</a>.</p>"""
    new_replica_count: NotRequired["capo_elasticache.types.integer.Integer"]
    """<p>The number of replicas you want in this node group at the end of this operation. The maximum value for <code>NewReplicaCount</code> is 5. The minimum value depends upon the type of Valkey or Redis OSS replication group you are working with.</p> <p>The minimum number of replicas in a shard or replication group is:</p> <ul> <li> <p>Valkey or Redis OSS (cluster mode disabled)</p> <ul> <li> <p>If Multi-AZ: 1</p> </li> <li> <p>If Multi-AZ: 0</p> </li> </ul> </li> <li> <p>Valkey or Redis OSS (cluster mode enabled): 0 (though you will not be able to failover to a replica if your primary node fails)</p> </li> </ul>"""
    preferred_availability_zones: NotRequired[
        "capo_elasticache.types.preferred_availability_zone_list.PreferredAvailabilityZoneList"
    ]
    """<p>A list of <code>PreferredAvailabilityZone</code> strings that specify which availability zones the replication group's nodes are to be in. The nummber of <code>PreferredAvailabilityZone</code> values must equal the value of <code>NewReplicaCount</code> plus 1 to account for the primary node. If this member of <code>ReplicaConfiguration</code> is omitted, ElastiCache selects the availability zone for each of the replicas.</p>"""
    preferred_outpost_arns: NotRequired[
        "capo_elasticache.types.preferred_outpost_arn_list.PreferredOutpostArnList"
    ]
    """<p>The outpost ARNs in which the cache cluster is created.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ConfigureShard, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "node_group_id" in value:
        pairs.append((f"{key_prefix}NodeGroupId", str(value["node_group_id"])))
    if "new_replica_count" in value:
        pairs.append((f"{key_prefix}NewReplicaCount", str(value["new_replica_count"])))
    if "preferred_availability_zones" in value:
        import capo_elasticache.types.preferred_availability_zone_list

        capo_elasticache.types.preferred_availability_zone_list.serialize_query(
            value["preferred_availability_zones"],
            pairs,
            f"{key_prefix}PreferredAvailabilityZones",
        )
    if "preferred_outpost_arns" in value:
        import capo_elasticache.types.preferred_outpost_arn_list

        capo_elasticache.types.preferred_outpost_arn_list.serialize_query(
            value["preferred_outpost_arns"], pairs, f"{key_prefix}PreferredOutpostArns"
        )


def deserialize_query(el: Element) -> ConfigureShard:
    out: ConfigureShard = {}  # type: ignore[typeddict-item]
    child_node_group_id = el.find("NodeGroupId")
    if child_node_group_id is not None:
        out["node_group_id"] = str(child_node_group_id.text or "")
    child_new_replica_count = el.find("NewReplicaCount")
    if child_new_replica_count is not None:
        out["new_replica_count"] = int(child_new_replica_count.text or "")
    child_preferred_availability_zones = el.find("PreferredAvailabilityZones")
    if child_preferred_availability_zones is not None:
        import capo_elasticache.types.preferred_availability_zone_list

        out["preferred_availability_zones"] = (
            capo_elasticache.types.preferred_availability_zone_list.deserialize_query(
                child_preferred_availability_zones
            )
        )
    child_preferred_outpost_arns = el.find("PreferredOutpostArns")
    if child_preferred_outpost_arns is not None:
        import capo_elasticache.types.preferred_outpost_arn_list

        out["preferred_outpost_arns"] = (
            capo_elasticache.types.preferred_outpost_arn_list.deserialize_query(
                child_preferred_outpost_arns
            )
        )
    return out
