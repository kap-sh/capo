"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#CreateLoadBalancerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.customer_owned_ipv4_pool
    import capo_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum
    import capo_elastic_load_balancing_v2.types.ip_address_type
    import capo_elastic_load_balancing_v2.types.ipam_pools
    import capo_elastic_load_balancing_v2.types.load_balancer_name
    import capo_elastic_load_balancing_v2.types.load_balancer_scheme_enum
    import capo_elastic_load_balancing_v2.types.load_balancer_type_enum
    import capo_elastic_load_balancing_v2.types.security_groups
    import capo_elastic_load_balancing_v2.types.subnet_mappings
    import capo_elastic_load_balancing_v2.types.subnets
    import capo_elastic_load_balancing_v2.types.tag_list


class CreateLoadBalancerInput(TypedDict, closed=True):
    name: NotRequired[
        "capo_elastic_load_balancing_v2.types.load_balancer_name.LoadBalancerName"
    ]
    """<p>The name of the load balancer.</p> <p>This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, must not begin or end with a hyphen, and must not begin with "internal-".</p>"""
    subnets: NotRequired["capo_elastic_load_balancing_v2.types.subnets.Subnets"]
    """<p>The IDs of the subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings, but not both. To specify an Elastic IP address, specify subnet mappings instead of subnets.</p> <p>[Application Load Balancers] You must specify subnets from at least two Availability Zones.</p> <p>[Application Load Balancers on Outposts] You must specify one Outpost subnet.</p> <p>[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.</p> <p>[Network Load Balancers and Gateway Load Balancers] You can specify subnets from one or more Availability Zones.</p>"""
    subnet_mappings: NotRequired[
        "capo_elastic_load_balancing_v2.types.subnet_mappings.SubnetMappings"
    ]
    """<p>The IDs of the subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings, but not both.</p> <p>[Application Load Balancers] You must specify subnets from at least two Availability Zones. You can't specify Elastic IP addresses for your subnets.</p> <p>[Application Load Balancers on Outposts] You must specify one Outpost subnet.</p> <p>[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.</p> <p>[Network Load Balancers] You can specify subnets from one or more Availability Zones. You can specify one Elastic IP address per subnet if you need static IP addresses for your internet-facing load balancer. For internal load balancers, you can specify one private IP address per subnet from the IPv4 range of the subnet. For internet-facing load balancer, you can specify one IPv6 address per subnet.</p> <p>[Gateway Load Balancers] You can specify subnets from one or more Availability Zones. You can't specify Elastic IP addresses for your subnets.</p>"""
    security_groups: NotRequired[
        "capo_elastic_load_balancing_v2.types.security_groups.SecurityGroups"
    ]
    """<p>[Application Load Balancers and Network Load Balancers] The IDs of the security groups for the load balancer.</p>"""
    scheme: NotRequired[
        "capo_elastic_load_balancing_v2.types.load_balancer_scheme_enum.LoadBalancerSchemeEnum"
    ]
    """<p>The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the internet.</p> <p>The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can route requests only from clients with access to the VPC for the load balancer.</p> <p>The default is an Internet-facing load balancer.</p> <p>You can't specify a scheme for a Gateway Load Balancer.</p>"""
    tags: NotRequired["capo_elastic_load_balancing_v2.types.tag_list.TagList"]
    """<p>The tags to assign to the load balancer.</p>"""
    type: NotRequired[
        "capo_elastic_load_balancing_v2.types.load_balancer_type_enum.LoadBalancerTypeEnum"
    ]
    """<p>The type of load balancer. The default is <code>application</code>.</p>"""
    ip_address_type: NotRequired[
        "capo_elastic_load_balancing_v2.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type. Internal load balancers must use <code>ipv4</code>.</p> <p>[Application Load Balancers] The possible values are <code>ipv4</code> (IPv4 addresses), <code>dualstack</code> (IPv4 and IPv6 addresses), and <code>dualstack-without-public-ipv4</code> (public IPv6 addresses and private IPv4 and IPv6 addresses).</p> <p>[Network Load Balancers and Gateway Load Balancers] The possible values are <code>ipv4</code> (IPv4 addresses) and <code>dualstack</code> (IPv4 and IPv6 addresses).</p>"""
    customer_owned_ipv4_pool: NotRequired[
        "capo_elastic_load_balancing_v2.types.customer_owned_ipv4_pool.CustomerOwnedIpv4Pool"
    ]
    """<p>[Application Load Balancers on Outposts] The ID of the customer-owned address pool (CoIP pool).</p>"""
    enable_prefix_for_ipv6_source_nat: NotRequired[
        "capo_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum.EnablePrefixForIpv6SourceNatEnum"
    ]
    """<p>[Network Load Balancers with UDP listeners] Indicates whether to use an IPv6 prefix from each subnet for source NAT. The IP address type must be <code>dualstack</code>. The default value is <code>off</code>.</p>"""
    ipam_pools: NotRequired["capo_elastic_load_balancing_v2.types.ipam_pools.IpamPools"]
    """<p>[Application Load Balancers] The IPAM pools to use with the load balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateLoadBalancerInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "subnets" in value:
        import capo_elastic_load_balancing_v2.types.subnets

        capo_elastic_load_balancing_v2.types.subnets.serialize_query(
            value["subnets"], pairs, f"{key_prefix}Subnets"
        )
    if "subnet_mappings" in value:
        import capo_elastic_load_balancing_v2.types.subnet_mappings

        capo_elastic_load_balancing_v2.types.subnet_mappings.serialize_query(
            value["subnet_mappings"], pairs, f"{key_prefix}SubnetMappings"
        )
    if "security_groups" in value:
        import capo_elastic_load_balancing_v2.types.security_groups

        capo_elastic_load_balancing_v2.types.security_groups.serialize_query(
            value["security_groups"], pairs, f"{key_prefix}SecurityGroups"
        )
    if "scheme" in value:
        import capo_elastic_load_balancing_v2.types.load_balancer_scheme_enum

        capo_elastic_load_balancing_v2.types.load_balancer_scheme_enum.serialize_query(
            value["scheme"], pairs, f"{key_prefix}Scheme"
        )
    if "tags" in value:
        import capo_elastic_load_balancing_v2.types.tag_list

        capo_elastic_load_balancing_v2.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "type" in value:
        import capo_elastic_load_balancing_v2.types.load_balancer_type_enum

        capo_elastic_load_balancing_v2.types.load_balancer_type_enum.serialize_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "ip_address_type" in value:
        import capo_elastic_load_balancing_v2.types.ip_address_type

        capo_elastic_load_balancing_v2.types.ip_address_type.serialize_query(
            value["ip_address_type"], pairs, f"{key_prefix}IpAddressType"
        )
    if "customer_owned_ipv4_pool" in value:
        pairs.append(
            (
                f"{key_prefix}CustomerOwnedIpv4Pool",
                str(value["customer_owned_ipv4_pool"]),
            )
        )
    if "enable_prefix_for_ipv6_source_nat" in value:
        import capo_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum

        capo_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum.serialize_query(
            value["enable_prefix_for_ipv6_source_nat"],
            pairs,
            f"{key_prefix}EnablePrefixForIpv6SourceNat",
        )
    if "ipam_pools" in value:
        import capo_elastic_load_balancing_v2.types.ipam_pools

        capo_elastic_load_balancing_v2.types.ipam_pools.serialize_query(
            value["ipam_pools"], pairs, f"{key_prefix}IpamPools"
        )


def deserialize_query(el: Element) -> CreateLoadBalancerInput:
    out: CreateLoadBalancerInput = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_subnets = el.find("Subnets")
    if child_subnets is not None:
        import capo_elastic_load_balancing_v2.types.subnets

        out["subnets"] = capo_elastic_load_balancing_v2.types.subnets.deserialize_query(
            child_subnets
        )
    child_subnet_mappings = el.find("SubnetMappings")
    if child_subnet_mappings is not None:
        import capo_elastic_load_balancing_v2.types.subnet_mappings

        out["subnet_mappings"] = (
            capo_elastic_load_balancing_v2.types.subnet_mappings.deserialize_query(
                child_subnet_mappings
            )
        )
    child_security_groups = el.find("SecurityGroups")
    if child_security_groups is not None:
        import capo_elastic_load_balancing_v2.types.security_groups

        out["security_groups"] = (
            capo_elastic_load_balancing_v2.types.security_groups.deserialize_query(
                child_security_groups
            )
        )
    child_scheme = el.find("Scheme")
    if child_scheme is not None:
        import capo_elastic_load_balancing_v2.types.load_balancer_scheme_enum

        out["scheme"] = (
            capo_elastic_load_balancing_v2.types.load_balancer_scheme_enum.deserialize_query(
                child_scheme
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elastic_load_balancing_v2.types.tag_list

        out["tags"] = capo_elastic_load_balancing_v2.types.tag_list.deserialize_query(
            child_tags
        )
    child_type = el.find("Type")
    if child_type is not None:
        import capo_elastic_load_balancing_v2.types.load_balancer_type_enum

        out["type"] = (
            capo_elastic_load_balancing_v2.types.load_balancer_type_enum.deserialize_query(
                child_type
            )
        )
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import capo_elastic_load_balancing_v2.types.ip_address_type

        out["ip_address_type"] = (
            capo_elastic_load_balancing_v2.types.ip_address_type.deserialize_query(
                child_ip_address_type
            )
        )
    child_customer_owned_ipv4_pool = el.find("CustomerOwnedIpv4Pool")
    if child_customer_owned_ipv4_pool is not None:
        out["customer_owned_ipv4_pool"] = str(child_customer_owned_ipv4_pool.text or "")
    child_enable_prefix_for_ipv6_source_nat = el.find("EnablePrefixForIpv6SourceNat")
    if child_enable_prefix_for_ipv6_source_nat is not None:
        import capo_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum

        out["enable_prefix_for_ipv6_source_nat"] = (
            capo_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum.deserialize_query(
                child_enable_prefix_for_ipv6_source_nat
            )
        )
    child_ipam_pools = el.find("IpamPools")
    if child_ipam_pools is not None:
        import capo_elastic_load_balancing_v2.types.ipam_pools

        out["ipam_pools"] = (
            capo_elastic_load_balancing_v2.types.ipam_pools.deserialize_query(
                child_ipam_pools
            )
        )
    return out
