"""Generated from Smithy shape ``com.amazonaws.elasticache#Subnet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.availability_zone
    import capo_elasticache.types.network_type_list
    import capo_elasticache.types.string
    import capo_elasticache.types.subnet_outpost


class Subnet(TypedDict, closed=True):
    subnet_identifier: NotRequired["capo_elasticache.types.string.String"]
    """<p>The unique identifier for the subnet.</p>"""
    subnet_availability_zone: NotRequired[
        "capo_elasticache.types.availability_zone.AvailabilityZone"
    ]
    """<p>The Availability Zone associated with the subnet.</p>"""
    subnet_outpost: NotRequired["capo_elasticache.types.subnet_outpost.SubnetOutpost"]
    """<p>The outpost ARN of the subnet.</p>"""
    supported_network_types: NotRequired[
        "capo_elasticache.types.network_type_list.NetworkTypeList"
    ]
    """<p>Either <code>ipv4</code> | <code>ipv6</code> | <code>dual_stack</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Subnet, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "subnet_identifier" in value:
        pairs.append((f"{key_prefix}SubnetIdentifier", str(value["subnet_identifier"])))
    if "subnet_availability_zone" in value:
        import capo_elasticache.types.availability_zone

        capo_elasticache.types.availability_zone.serialize_query(
            value["subnet_availability_zone"],
            pairs,
            f"{key_prefix}SubnetAvailabilityZone",
        )
    if "subnet_outpost" in value:
        import capo_elasticache.types.subnet_outpost

        capo_elasticache.types.subnet_outpost.serialize_query(
            value["subnet_outpost"], pairs, f"{key_prefix}SubnetOutpost"
        )
    if "supported_network_types" in value:
        import capo_elasticache.types.network_type_list

        capo_elasticache.types.network_type_list.serialize_query(
            value["supported_network_types"],
            pairs,
            f"{key_prefix}SupportedNetworkTypes",
        )


def deserialize_query(el: Element) -> Subnet:
    out: Subnet = {}  # type: ignore[typeddict-item]
    child_subnet_identifier = el.find("SubnetIdentifier")
    if child_subnet_identifier is not None:
        out["subnet_identifier"] = str(child_subnet_identifier.text or "")
    child_subnet_availability_zone = el.find("SubnetAvailabilityZone")
    if child_subnet_availability_zone is not None:
        import capo_elasticache.types.availability_zone

        out["subnet_availability_zone"] = (
            capo_elasticache.types.availability_zone.deserialize_query(
                child_subnet_availability_zone
            )
        )
    child_subnet_outpost = el.find("SubnetOutpost")
    if child_subnet_outpost is not None:
        import capo_elasticache.types.subnet_outpost

        out["subnet_outpost"] = capo_elasticache.types.subnet_outpost.deserialize_query(
            child_subnet_outpost
        )
    child_supported_network_types = el.find("SupportedNetworkTypes")
    if child_supported_network_types is not None:
        import capo_elasticache.types.network_type_list

        out["supported_network_types"] = (
            capo_elasticache.types.network_type_list.deserialize_query(
                child_supported_network_types
            )
        )
    return out
