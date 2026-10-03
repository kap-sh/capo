"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheSubnetGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.network_type_list
    import capo_elasticache.types.string
    import capo_elasticache.types.subnet_list


class CacheSubnetGroup(TypedDict, closed=True):
    cache_subnet_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache subnet group.</p>"""
    cache_subnet_group_description: NotRequired["capo_elasticache.types.string.String"]
    """<p>The description of the cache subnet group.</p>"""
    vpc_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.</p>"""
    subnets: NotRequired["capo_elasticache.types.subnet_list.SubnetList"]
    """<p>A list of subnets associated with the cache subnet group.</p>"""
    arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ARN (Amazon Resource Name) of the cache subnet group.</p>"""
    supported_network_types: NotRequired[
        "capo_elasticache.types.network_type_list.NetworkTypeList"
    ]
    """<p>Either <code>ipv4</code> | <code>ipv6</code> | <code>dual_stack</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheSubnetGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cache_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}CacheSubnetGroupName", str(value["cache_subnet_group_name"]))
        )
    if "cache_subnet_group_description" in value:
        pairs.append(
            (
                f"{key_prefix}CacheSubnetGroupDescription",
                str(value["cache_subnet_group_description"]),
            )
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "subnets" in value:
        import capo_elasticache.types.subnet_list

        capo_elasticache.types.subnet_list.serialize_query(
            value["subnets"], pairs, f"{key_prefix}Subnets"
        )
    if "arn" in value:
        pairs.append((f"{key_prefix}ARN", str(value["arn"])))
    if "supported_network_types" in value:
        import capo_elasticache.types.network_type_list

        capo_elasticache.types.network_type_list.serialize_query(
            value["supported_network_types"],
            pairs,
            f"{key_prefix}SupportedNetworkTypes",
        )


def deserialize_query(el: Element) -> CacheSubnetGroup:
    out: CacheSubnetGroup = {}  # type: ignore[typeddict-item]
    child_cache_subnet_group_name = el.find("CacheSubnetGroupName")
    if child_cache_subnet_group_name is not None:
        out["cache_subnet_group_name"] = str(child_cache_subnet_group_name.text or "")
    child_cache_subnet_group_description = el.find("CacheSubnetGroupDescription")
    if child_cache_subnet_group_description is not None:
        out["cache_subnet_group_description"] = str(
            child_cache_subnet_group_description.text or ""
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_subnets = el.find("Subnets")
    if child_subnets is not None:
        import capo_elasticache.types.subnet_list

        out["subnets"] = capo_elasticache.types.subnet_list.deserialize_query(
            child_subnets
        )
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_supported_network_types = el.find("SupportedNetworkTypes")
    if child_supported_network_types is not None:
        import capo_elasticache.types.network_type_list

        out["supported_network_types"] = (
            capo_elasticache.types.network_type_list.deserialize_query(
                child_supported_network_types
            )
        )
    return out
