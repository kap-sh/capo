"""Generated from Smithy shape ``com.amazonaws.elasticache#NodeGroupConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.allowed_node_group_id
    import capo_elasticache.types.availability_zones_list
    import capo_elasticache.types.integer_optional
    import capo_elasticache.types.outpost_arns_list
    import capo_elasticache.types.string


class NodeGroupConfiguration(TypedDict, closed=True):
    node_group_id: NotRequired[
        "capo_elasticache.types.allowed_node_group_id.AllowedNodeGroupId"
    ]
    """<p>Either the ElastiCache supplied 4-digit id or a user supplied id for the node group these configuration values apply to.</p>"""
    slots: NotRequired["capo_elasticache.types.string.String"]
    """<p>A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to 16,383. The string is in the format <code>startkey-endkey</code>.</p> <p>Example: <code>"0-3999"</code> </p>"""
    replica_count: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of read replica nodes in this node group (shard).</p>"""
    primary_availability_zone: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Availability Zone where the primary node of this node group (shard) is launched.</p>"""
    replica_availability_zones: NotRequired[
        "capo_elasticache.types.availability_zones_list.AvailabilityZonesList"
    ]
    """<p>A list of Availability Zones to be used for the read replicas. The number of Availability Zones in this list must match the value of <code>ReplicaCount</code> or <code>ReplicasPerNodeGroup</code> if not specified.</p>"""
    primary_outpost_arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The outpost ARN of the primary node.</p>"""
    replica_outpost_arns: NotRequired[
        "capo_elasticache.types.outpost_arns_list.OutpostArnsList"
    ]
    """<p>The outpost ARN of the node replicas.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeGroupConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "node_group_id" in value:
        pairs.append((f"{key_prefix}NodeGroupId", str(value["node_group_id"])))
    if "slots" in value:
        pairs.append((f"{key_prefix}Slots", str(value["slots"])))
    if "replica_count" in value:
        pairs.append((f"{key_prefix}ReplicaCount", str(value["replica_count"])))
    if "primary_availability_zone" in value:
        pairs.append(
            (
                f"{key_prefix}PrimaryAvailabilityZone",
                str(value["primary_availability_zone"]),
            )
        )
    if "replica_availability_zones" in value:
        import capo_elasticache.types.availability_zones_list

        capo_elasticache.types.availability_zones_list.serialize_query(
            value["replica_availability_zones"],
            pairs,
            f"{key_prefix}ReplicaAvailabilityZones",
        )
    if "primary_outpost_arn" in value:
        pairs.append(
            (f"{key_prefix}PrimaryOutpostArn", str(value["primary_outpost_arn"]))
        )
    if "replica_outpost_arns" in value:
        import capo_elasticache.types.outpost_arns_list

        capo_elasticache.types.outpost_arns_list.serialize_query(
            value["replica_outpost_arns"], pairs, f"{key_prefix}ReplicaOutpostArns"
        )


def deserialize_query(el: Element) -> NodeGroupConfiguration:
    out: NodeGroupConfiguration = {}  # type: ignore[typeddict-item]
    child_node_group_id = el.find("NodeGroupId")
    if child_node_group_id is not None:
        out["node_group_id"] = str(child_node_group_id.text or "")
    child_slots = el.find("Slots")
    if child_slots is not None:
        out["slots"] = str(child_slots.text or "")
    child_replica_count = el.find("ReplicaCount")
    if child_replica_count is not None:
        out["replica_count"] = int(child_replica_count.text or "")
    child_primary_availability_zone = el.find("PrimaryAvailabilityZone")
    if child_primary_availability_zone is not None:
        out["primary_availability_zone"] = str(
            child_primary_availability_zone.text or ""
        )
    child_replica_availability_zones = el.find("ReplicaAvailabilityZones")
    if child_replica_availability_zones is not None:
        import capo_elasticache.types.availability_zones_list

        out["replica_availability_zones"] = (
            capo_elasticache.types.availability_zones_list.deserialize_query(
                child_replica_availability_zones
            )
        )
    child_primary_outpost_arn = el.find("PrimaryOutpostArn")
    if child_primary_outpost_arn is not None:
        out["primary_outpost_arn"] = str(child_primary_outpost_arn.text or "")
    child_replica_outpost_arns = el.find("ReplicaOutpostArns")
    if child_replica_outpost_arns is not None:
        import capo_elasticache.types.outpost_arns_list

        out["replica_outpost_arns"] = (
            capo_elasticache.types.outpost_arns_list.deserialize_query(
                child_replica_outpost_arns
            )
        )
    return out
