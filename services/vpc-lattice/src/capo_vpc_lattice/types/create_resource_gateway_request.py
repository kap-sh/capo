"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateResourceGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.ipv4_addresses_per_eni
    import capo_vpc_lattice.types.resource_config_dns_resolution
    import capo_vpc_lattice.types.resource_gateway_ip_address_type
    import capo_vpc_lattice.types.resource_gateway_name
    import capo_vpc_lattice.types.security_group_list
    import capo_vpc_lattice.types.subnet_list
    import capo_vpc_lattice.types.tag_map
    import capo_vpc_lattice.types.vpc_id


class CreateResourceGatewayRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_vpc_lattice.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>"""
    name: "capo_vpc_lattice.types.resource_gateway_name.ResourceGatewayName"
    """<p>The name of the resource gateway.</p>"""
    vpc_identifier: NotRequired["capo_vpc_lattice.types.vpc_id.VpcId"]
    """<p>The ID of the VPC for the resource gateway.</p>"""
    subnet_ids: NotRequired["capo_vpc_lattice.types.subnet_list.SubnetList"]
    """<p>The IDs of the VPC subnets in which to create the resource gateway.</p>"""
    security_group_ids: NotRequired[
        "capo_vpc_lattice.types.security_group_list.SecurityGroupList"
    ]
    """<p>The IDs of the security groups to apply to the resource gateway. The security groups must be in the same VPC.</p>"""
    ip_address_type: NotRequired[
        "capo_vpc_lattice.types.resource_gateway_ip_address_type.ResourceGatewayIpAddressType"
    ]
    """<p>A resource gateway can have IPv4, IPv6 or dualstack addresses. The IP address type of a resource gateway must be compatible with the subnets of the resource gateway and the IP address type of the resource, as described here: </p> <ul> <li> <p> <b>IPv4</b>Assign IPv4 addresses to your resource gateway network interfaces. This option is supported only if all selected subnets have IPv4 address ranges, and the resource also has an IPv4 address.</p> </li> <li> <p> <b>IPv6</b>Assign IPv6 addresses to your resource gateway network interfaces. This option is supported only if all selected subnets are IPv6 only subnets, and the resource also has an IPv6 address.</p> </li> <li> <p> <b>Dualstack</b>Assign both IPv4 and IPv6 addresses to your resource gateway network interfaces. This option is supported only if all selected subnets have both IPv4 and IPv6 address ranges, and the resource either has an IPv4 or IPv6 address.</p> </li> </ul> <p>The IP address type of the resource gateway is independent of the IP address type of the client or the VPC endpoint through which the resource is accessed.</p>"""
    ipv4_addresses_per_eni: NotRequired[
        "capo_vpc_lattice.types.ipv4_addresses_per_eni.Ipv4AddressesPerEni"
    ]
    """<p>The number of IPv4 addresses in each ENI for the resource gateway.</p>"""
    resource_config_dns_resolution: NotRequired[
        "capo_vpc_lattice.types.resource_config_dns_resolution.ResourceConfigDnsResolution"
    ]
    """<p>Indicates how DNS is resolved for resource configurations associated with this resource gateway. This value is set when you create the resource gateway and can't be changed afterward. The default is <code>PUBLIC</code>.</p> <ul> <li> <p> <code>IN_VPC</code> - DNS resolution occurs privately within the resource gateway's VPC. DNS queries for resources behind this resource gateway resolve using the DNS resolvers defined in the VPC's DHCP option sets. Use this when your resource domain names are hosted in private Route 53 hosted zones or on-premises DNS servers reachable from the VPC. A CIDR resource configuration requires a resource gateway that uses <code>IN_VPC</code>, and an <code>IN_VPC</code> resource gateway can't be used for ARN resource configurations, so a single resource gateway can't serve both ARN and CIDR resource configurations.</p> </li> <li> <p> <code>PUBLIC</code> - DNS resolution occurs against public DNS resolvers. DNS queries for resources behind this resource gateway resolve using standard public DNS. Use this when your resource domain names are publicly resolvable.</p> </li> </ul>"""
    tags: NotRequired["capo_vpc_lattice.types.tag_map.TagMap"]
    """<p>The tags for the resource gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResourceGatewayRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    if "vpc_identifier" in value:
        out["vpcIdentifier"] = value["vpc_identifier"]
    if "subnet_ids" in value:
        import capo_vpc_lattice.types.subnet_list

        out["subnetIds"] = capo_vpc_lattice.types.subnet_list.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_vpc_lattice.types.security_group_list

        out["securityGroupIds"] = (
            capo_vpc_lattice.types.security_group_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "ip_address_type" in value:
        out["ipAddressType"] = value["ip_address_type"]
    if "ipv4_addresses_per_eni" in value:
        out["ipv4AddressesPerEni"] = value["ipv4_addresses_per_eni"]
    if "resource_config_dns_resolution" in value:
        out["resourceConfigDnsResolution"] = value["resource_config_dns_resolution"]
    if "tags" in value:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateResourceGatewayRequest:
    out: CreateResourceGatewayRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("vpcIdentifier") is not None:
        out["vpc_identifier"] = data["vpcIdentifier"]
    if data.get("subnetIds") is not None:
        import capo_vpc_lattice.types.subnet_list

        out["subnet_ids"] = capo_vpc_lattice.types.subnet_list.deserialize_json(
            data["subnetIds"]
        )
    if data.get("securityGroupIds") is not None:
        import capo_vpc_lattice.types.security_group_list

        out["security_group_ids"] = (
            capo_vpc_lattice.types.security_group_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if data.get("ipAddressType") is not None:
        out["ip_address_type"] = data["ipAddressType"]
    if data.get("ipv4AddressesPerEni") is not None:
        out["ipv4_addresses_per_eni"] = data["ipv4AddressesPerEni"]
    if data.get("resourceConfigDnsResolution") is not None:
        out["resource_config_dns_resolution"] = data["resourceConfigDnsResolution"]
    if data.get("tags") is not None:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    return out
