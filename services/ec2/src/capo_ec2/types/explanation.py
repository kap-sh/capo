"""Generated from Smithy shape ``com.amazonaws.ec2#Explanation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.analysis_acl_rule
    import capo_ec2.types.analysis_component
    import capo_ec2.types.analysis_component_list
    import capo_ec2.types.analysis_load_balancer_listener
    import capo_ec2.types.analysis_load_balancer_target
    import capo_ec2.types.analysis_route_table_route
    import capo_ec2.types.analysis_security_group_rule
    import capo_ec2.types.analysis_transit_gateway_policy_table_entry
    import capo_ec2.types.component_account
    import capo_ec2.types.component_region
    import capo_ec2.types.firewall_stateful_rule
    import capo_ec2.types.firewall_stateless_rule
    import capo_ec2.types.ip_address
    import capo_ec2.types.ip_address_list
    import capo_ec2.types.port
    import capo_ec2.types.port_range_list
    import capo_ec2.types.resource_arn
    import capo_ec2.types.string
    import capo_ec2.types.string_list
    import capo_ec2.types.transit_gateway_route_table_route
    import capo_ec2.types.value_string_list


class Explanation(TypedDict, closed=True):
    acl: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The network ACL.</p>"""
    acl_rule: NotRequired["capo_ec2.types.analysis_acl_rule.AnalysisAclRule"]
    """<p>The network ACL rule.</p>"""
    address: NotRequired["capo_ec2.types.ip_address.IpAddress"]
    """<p>The IPv4 address, in CIDR notation.</p>"""
    addresses: NotRequired["capo_ec2.types.ip_address_list.IpAddressList"]
    """<p>The IPv4 addresses, in CIDR notation.</p>"""
    attached_to: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The resource to which the component is attached.</p>"""
    availability_zones: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The Availability Zones.</p>"""
    availability_zone_ids: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The IDs of the Availability Zones.</p>"""
    cidrs: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The CIDR ranges.</p>"""
    component: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The component.</p>"""
    customer_gateway: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The customer gateway.</p>"""
    destination: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The destination.</p>"""
    destination_vpc: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The destination VPC.</p>"""
    direction: NotRequired["capo_ec2.types.string.String"]
    """<p>The direction. The following are the possible values:</p> <ul> <li> <p>egress</p> </li> <li> <p>ingress</p> </li> </ul>"""
    explanation_code: NotRequired["capo_ec2.types.string.String"]
    """<p>The explanation code.</p>"""
    ingress_route_table: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The route table.</p>"""
    internet_gateway: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The internet gateway.</p>"""
    load_balancer_arn: NotRequired["capo_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    classic_load_balancer_listener: NotRequired[
        "capo_ec2.types.analysis_load_balancer_listener.AnalysisLoadBalancerListener"
    ]
    """<p>The listener for a Classic Load Balancer.</p>"""
    load_balancer_listener_port: NotRequired["capo_ec2.types.port.Port"]
    """<p>The listener port of the load balancer.</p>"""
    load_balancer_target: NotRequired[
        "capo_ec2.types.analysis_load_balancer_target.AnalysisLoadBalancerTarget"
    ]
    """<p>The target.</p>"""
    load_balancer_target_group: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The target group.</p>"""
    load_balancer_target_groups: NotRequired[
        "capo_ec2.types.analysis_component_list.AnalysisComponentList"
    ]
    """<p>The target groups.</p>"""
    load_balancer_target_port: NotRequired["capo_ec2.types.port.Port"]
    """<p>The target port.</p>"""
    elastic_load_balancer_listener: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The load balancer listener.</p>"""
    missing_component: NotRequired["capo_ec2.types.string.String"]
    """<p>The missing component.</p>"""
    nat_gateway: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The NAT gateway.</p>"""
    network_interface: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The network interface.</p>"""
    packet_field: NotRequired["capo_ec2.types.string.String"]
    """<p>The packet field.</p>"""
    vpc_peering_connection: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The VPC peering connection.</p>"""
    port: NotRequired["capo_ec2.types.port.Port"]
    """<p>The port.</p>"""
    port_ranges: NotRequired["capo_ec2.types.port_range_list.PortRangeList"]
    """<p>The port ranges.</p>"""
    prefix_list: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The prefix list.</p>"""
    protocols: NotRequired["capo_ec2.types.string_list.StringList"]
    """<p>The protocols.</p>"""
    route_table_route: NotRequired[
        "capo_ec2.types.analysis_route_table_route.AnalysisRouteTableRoute"
    ]
    """<p>The route table route.</p>"""
    route_table: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The route table.</p>"""
    security_group: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The security group.</p>"""
    security_group_rule: NotRequired[
        "capo_ec2.types.analysis_security_group_rule.AnalysisSecurityGroupRule"
    ]
    """<p>The security group rule.</p>"""
    security_groups: NotRequired[
        "capo_ec2.types.analysis_component_list.AnalysisComponentList"
    ]
    """<p>The security groups.</p>"""
    source_vpc: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The source VPC.</p>"""
    state: NotRequired["capo_ec2.types.string.String"]
    """<p>The state.</p>"""
    subnet: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The subnet.</p>"""
    subnet_route_table: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The route table for the subnet.</p>"""
    vpc: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The component VPC.</p>"""
    vpc_endpoint: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The VPC endpoint.</p>"""
    vpn_connection: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The VPN connection.</p>"""
    vpn_gateway: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The VPN gateway.</p>"""
    transit_gateway: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The transit gateway.</p>"""
    transit_gateway_route_table: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The transit gateway route table.</p>"""
    transit_gateway_route_table_route: NotRequired[
        "capo_ec2.types.transit_gateway_route_table_route.TransitGatewayRouteTableRoute"
    ]
    """<p>The transit gateway route table route.</p>"""
    transit_gateway_policy_table: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The transit gateway policy table.</p>"""
    transit_gateway_policy_table_entry: NotRequired[
        "capo_ec2.types.analysis_transit_gateway_policy_table_entry.AnalysisTransitGatewayPolicyTableEntry"
    ]
    """<p>The transit gateway policy table entry.</p>"""
    transit_gateway_attachment: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The transit gateway attachment.</p>"""
    component_account: NotRequired["capo_ec2.types.component_account.ComponentAccount"]
    """<p>The Amazon Web Services account for the component.</p>"""
    component_region: NotRequired["capo_ec2.types.component_region.ComponentRegion"]
    """<p>The Region for the component.</p>"""
    firewall_stateless_rule: NotRequired[
        "capo_ec2.types.firewall_stateless_rule.FirewallStatelessRule"
    ]
    """<p>The Network Firewall stateless rule.</p>"""
    firewall_stateful_rule: NotRequired[
        "capo_ec2.types.firewall_stateful_rule.FirewallStatefulRule"
    ]
    """<p>The Network Firewall stateful rule.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Explanation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "acl" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["acl"], pairs, f"{key_prefix}Acl"
        )
    if "acl_rule" in value:
        import capo_ec2.types.analysis_acl_rule

        capo_ec2.types.analysis_acl_rule.serialize_ec2_query(
            value["acl_rule"], pairs, f"{key_prefix}AclRule"
        )
    if "address" in value:
        pairs.append((f"{key_prefix}Address", str(value["address"])))
    if "addresses" in value:
        import capo_ec2.types.ip_address_list

        capo_ec2.types.ip_address_list.serialize_ec2_query(
            value["addresses"], pairs, f"{key_prefix}AddressSet"
        )
    if "attached_to" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["attached_to"], pairs, f"{key_prefix}AttachedTo"
        )
    if "availability_zones" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZoneSet"
        )
    if "availability_zone_ids" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["availability_zone_ids"], pairs, f"{key_prefix}AvailabilityZoneIdSet"
        )
    if "cidrs" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["cidrs"], pairs, f"{key_prefix}CidrSet"
        )
    if "component" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["component"], pairs, f"{key_prefix}Component"
        )
    if "customer_gateway" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["customer_gateway"], pairs, f"{key_prefix}CustomerGateway"
        )
    if "destination" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["destination"], pairs, f"{key_prefix}Destination"
        )
    if "destination_vpc" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["destination_vpc"], pairs, f"{key_prefix}DestinationVpc"
        )
    if "direction" in value:
        pairs.append((f"{key_prefix}Direction", str(value["direction"])))
    if "explanation_code" in value:
        pairs.append((f"{key_prefix}ExplanationCode", str(value["explanation_code"])))
    if "ingress_route_table" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["ingress_route_table"], pairs, f"{key_prefix}IngressRouteTable"
        )
    if "internet_gateway" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["internet_gateway"], pairs, f"{key_prefix}InternetGateway"
        )
    if "load_balancer_arn" in value:
        pairs.append((f"{key_prefix}LoadBalancerArn", str(value["load_balancer_arn"])))
    if "classic_load_balancer_listener" in value:
        import capo_ec2.types.analysis_load_balancer_listener

        capo_ec2.types.analysis_load_balancer_listener.serialize_ec2_query(
            value["classic_load_balancer_listener"],
            pairs,
            f"{key_prefix}ClassicLoadBalancerListener",
        )
    if "load_balancer_listener_port" in value:
        pairs.append(
            (
                f"{key_prefix}LoadBalancerListenerPort",
                str(value["load_balancer_listener_port"]),
            )
        )
    if "load_balancer_target" in value:
        import capo_ec2.types.analysis_load_balancer_target

        capo_ec2.types.analysis_load_balancer_target.serialize_ec2_query(
            value["load_balancer_target"], pairs, f"{key_prefix}LoadBalancerTarget"
        )
    if "load_balancer_target_group" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["load_balancer_target_group"],
            pairs,
            f"{key_prefix}LoadBalancerTargetGroup",
        )
    if "load_balancer_target_groups" in value:
        import capo_ec2.types.analysis_component_list

        capo_ec2.types.analysis_component_list.serialize_ec2_query(
            value["load_balancer_target_groups"],
            pairs,
            f"{key_prefix}LoadBalancerTargetGroupSet",
        )
    if "load_balancer_target_port" in value:
        pairs.append(
            (
                f"{key_prefix}LoadBalancerTargetPort",
                str(value["load_balancer_target_port"]),
            )
        )
    if "elastic_load_balancer_listener" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["elastic_load_balancer_listener"],
            pairs,
            f"{key_prefix}ElasticLoadBalancerListener",
        )
    if "missing_component" in value:
        pairs.append((f"{key_prefix}MissingComponent", str(value["missing_component"])))
    if "nat_gateway" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["nat_gateway"], pairs, f"{key_prefix}NatGateway"
        )
    if "network_interface" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["network_interface"], pairs, f"{key_prefix}NetworkInterface"
        )
    if "packet_field" in value:
        pairs.append((f"{key_prefix}PacketField", str(value["packet_field"])))
    if "vpc_peering_connection" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["vpc_peering_connection"], pairs, f"{key_prefix}VpcPeeringConnection"
        )
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "port_ranges" in value:
        import capo_ec2.types.port_range_list

        capo_ec2.types.port_range_list.serialize_ec2_query(
            value["port_ranges"], pairs, f"{key_prefix}PortRangeSet"
        )
    if "prefix_list" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["prefix_list"], pairs, f"{key_prefix}PrefixList"
        )
    if "protocols" in value:
        import capo_ec2.types.string_list

        capo_ec2.types.string_list.serialize_ec2_query(
            value["protocols"], pairs, f"{key_prefix}ProtocolSet"
        )
    if "route_table_route" in value:
        import capo_ec2.types.analysis_route_table_route

        capo_ec2.types.analysis_route_table_route.serialize_ec2_query(
            value["route_table_route"], pairs, f"{key_prefix}RouteTableRoute"
        )
    if "route_table" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["route_table"], pairs, f"{key_prefix}RouteTable"
        )
    if "security_group" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["security_group"], pairs, f"{key_prefix}SecurityGroup"
        )
    if "security_group_rule" in value:
        import capo_ec2.types.analysis_security_group_rule

        capo_ec2.types.analysis_security_group_rule.serialize_ec2_query(
            value["security_group_rule"], pairs, f"{key_prefix}SecurityGroupRule"
        )
    if "security_groups" in value:
        import capo_ec2.types.analysis_component_list

        capo_ec2.types.analysis_component_list.serialize_ec2_query(
            value["security_groups"], pairs, f"{key_prefix}SecurityGroupSet"
        )
    if "source_vpc" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["source_vpc"], pairs, f"{key_prefix}SourceVpc"
        )
    if "state" in value:
        pairs.append((f"{key_prefix}State", str(value["state"])))
    if "subnet" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["subnet"], pairs, f"{key_prefix}Subnet"
        )
    if "subnet_route_table" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["subnet_route_table"], pairs, f"{key_prefix}SubnetRouteTable"
        )
    if "vpc" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["vpc"], pairs, f"{key_prefix}Vpc"
        )
    if "vpc_endpoint" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["vpc_endpoint"], pairs, f"{key_prefix}VpcEndpoint"
        )
    if "vpn_connection" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["vpn_connection"], pairs, f"{key_prefix}VpnConnection"
        )
    if "vpn_gateway" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["vpn_gateway"], pairs, f"{key_prefix}VpnGateway"
        )
    if "transit_gateway" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["transit_gateway"], pairs, f"{key_prefix}TransitGateway"
        )
    if "transit_gateway_route_table" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["transit_gateway_route_table"],
            pairs,
            f"{key_prefix}TransitGatewayRouteTable",
        )
    if "transit_gateway_route_table_route" in value:
        import capo_ec2.types.transit_gateway_route_table_route

        capo_ec2.types.transit_gateway_route_table_route.serialize_ec2_query(
            value["transit_gateway_route_table_route"],
            pairs,
            f"{key_prefix}TransitGatewayRouteTableRoute",
        )
    if "transit_gateway_policy_table" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["transit_gateway_policy_table"],
            pairs,
            f"{key_prefix}TransitGatewayPolicyTable",
        )
    if "transit_gateway_policy_table_entry" in value:
        import capo_ec2.types.analysis_transit_gateway_policy_table_entry

        capo_ec2.types.analysis_transit_gateway_policy_table_entry.serialize_ec2_query(
            value["transit_gateway_policy_table_entry"],
            pairs,
            f"{key_prefix}TransitGatewayPolicyTableEntry",
        )
    if "transit_gateway_attachment" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["transit_gateway_attachment"],
            pairs,
            f"{key_prefix}TransitGatewayAttachment",
        )
    if "component_account" in value:
        pairs.append((f"{key_prefix}ComponentAccount", str(value["component_account"])))
    if "component_region" in value:
        pairs.append((f"{key_prefix}ComponentRegion", str(value["component_region"])))
    if "firewall_stateless_rule" in value:
        import capo_ec2.types.firewall_stateless_rule

        capo_ec2.types.firewall_stateless_rule.serialize_ec2_query(
            value["firewall_stateless_rule"],
            pairs,
            f"{key_prefix}FirewallStatelessRule",
        )
    if "firewall_stateful_rule" in value:
        import capo_ec2.types.firewall_stateful_rule

        capo_ec2.types.firewall_stateful_rule.serialize_ec2_query(
            value["firewall_stateful_rule"], pairs, f"{key_prefix}FirewallStatefulRule"
        )


def deserialize_ec2_query(el: Element) -> Explanation:
    out: Explanation = {}  # type: ignore[typeddict-item]
    child_acl = el.find("acl")
    if child_acl is not None:
        import capo_ec2.types.analysis_component

        out["acl"] = capo_ec2.types.analysis_component.deserialize_ec2_query(child_acl)
    child_acl_rule = el.find("aclRule")
    if child_acl_rule is not None:
        import capo_ec2.types.analysis_acl_rule

        out["acl_rule"] = capo_ec2.types.analysis_acl_rule.deserialize_ec2_query(
            child_acl_rule
        )
    child_address = el.find("address")
    if child_address is not None:
        out["address"] = str(child_address.text or "")
    child_addresses = el.find("addressSet")
    if child_addresses is not None:
        import capo_ec2.types.ip_address_list

        out["addresses"] = capo_ec2.types.ip_address_list.deserialize_ec2_query(
            child_addresses
        )
    child_attached_to = el.find("attachedTo")
    if child_attached_to is not None:
        import capo_ec2.types.analysis_component

        out["attached_to"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_attached_to
        )
    child_availability_zones = el.find("availabilityZoneSet")
    if child_availability_zones is not None:
        import capo_ec2.types.value_string_list

        out["availability_zones"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                child_availability_zones
            )
        )
    child_availability_zone_ids = el.find("availabilityZoneIdSet")
    if child_availability_zone_ids is not None:
        import capo_ec2.types.value_string_list

        out["availability_zone_ids"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                child_availability_zone_ids
            )
        )
    child_cidrs = el.find("cidrSet")
    if child_cidrs is not None:
        import capo_ec2.types.value_string_list

        out["cidrs"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            child_cidrs
        )
    child_component = el.find("component")
    if child_component is not None:
        import capo_ec2.types.analysis_component

        out["component"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_component
        )
    child_customer_gateway = el.find("customerGateway")
    if child_customer_gateway is not None:
        import capo_ec2.types.analysis_component

        out["customer_gateway"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_customer_gateway
            )
        )
    child_destination = el.find("destination")
    if child_destination is not None:
        import capo_ec2.types.analysis_component

        out["destination"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_destination
        )
    child_destination_vpc = el.find("destinationVpc")
    if child_destination_vpc is not None:
        import capo_ec2.types.analysis_component

        out["destination_vpc"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_destination_vpc
            )
        )
    child_direction = el.find("direction")
    if child_direction is not None:
        out["direction"] = str(child_direction.text or "")
    child_explanation_code = el.find("explanationCode")
    if child_explanation_code is not None:
        out["explanation_code"] = str(child_explanation_code.text or "")
    child_ingress_route_table = el.find("ingressRouteTable")
    if child_ingress_route_table is not None:
        import capo_ec2.types.analysis_component

        out["ingress_route_table"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_ingress_route_table
            )
        )
    child_internet_gateway = el.find("internetGateway")
    if child_internet_gateway is not None:
        import capo_ec2.types.analysis_component

        out["internet_gateway"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_internet_gateway
            )
        )
    child_load_balancer_arn = el.find("loadBalancerArn")
    if child_load_balancer_arn is not None:
        out["load_balancer_arn"] = str(child_load_balancer_arn.text or "")
    child_classic_load_balancer_listener = el.find("classicLoadBalancerListener")
    if child_classic_load_balancer_listener is not None:
        import capo_ec2.types.analysis_load_balancer_listener

        out["classic_load_balancer_listener"] = (
            capo_ec2.types.analysis_load_balancer_listener.deserialize_ec2_query(
                child_classic_load_balancer_listener
            )
        )
    child_load_balancer_listener_port = el.find("loadBalancerListenerPort")
    if child_load_balancer_listener_port is not None:
        out["load_balancer_listener_port"] = int(
            child_load_balancer_listener_port.text or ""
        )
    child_load_balancer_target = el.find("loadBalancerTarget")
    if child_load_balancer_target is not None:
        import capo_ec2.types.analysis_load_balancer_target

        out["load_balancer_target"] = (
            capo_ec2.types.analysis_load_balancer_target.deserialize_ec2_query(
                child_load_balancer_target
            )
        )
    child_load_balancer_target_group = el.find("loadBalancerTargetGroup")
    if child_load_balancer_target_group is not None:
        import capo_ec2.types.analysis_component

        out["load_balancer_target_group"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_load_balancer_target_group
            )
        )
    child_load_balancer_target_groups = el.find("loadBalancerTargetGroupSet")
    if child_load_balancer_target_groups is not None:
        import capo_ec2.types.analysis_component_list

        out["load_balancer_target_groups"] = (
            capo_ec2.types.analysis_component_list.deserialize_ec2_query(
                child_load_balancer_target_groups
            )
        )
    child_load_balancer_target_port = el.find("loadBalancerTargetPort")
    if child_load_balancer_target_port is not None:
        out["load_balancer_target_port"] = int(
            child_load_balancer_target_port.text or ""
        )
    child_elastic_load_balancer_listener = el.find("elasticLoadBalancerListener")
    if child_elastic_load_balancer_listener is not None:
        import capo_ec2.types.analysis_component

        out["elastic_load_balancer_listener"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_elastic_load_balancer_listener
            )
        )
    child_missing_component = el.find("missingComponent")
    if child_missing_component is not None:
        out["missing_component"] = str(child_missing_component.text or "")
    child_nat_gateway = el.find("natGateway")
    if child_nat_gateway is not None:
        import capo_ec2.types.analysis_component

        out["nat_gateway"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_nat_gateway
        )
    child_network_interface = el.find("networkInterface")
    if child_network_interface is not None:
        import capo_ec2.types.analysis_component

        out["network_interface"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_network_interface
            )
        )
    child_packet_field = el.find("packetField")
    if child_packet_field is not None:
        out["packet_field"] = str(child_packet_field.text or "")
    child_vpc_peering_connection = el.find("vpcPeeringConnection")
    if child_vpc_peering_connection is not None:
        import capo_ec2.types.analysis_component

        out["vpc_peering_connection"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_vpc_peering_connection
            )
        )
    child_port = el.find("port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_port_ranges = el.find("portRangeSet")
    if child_port_ranges is not None:
        import capo_ec2.types.port_range_list

        out["port_ranges"] = capo_ec2.types.port_range_list.deserialize_ec2_query(
            child_port_ranges
        )
    child_prefix_list = el.find("prefixList")
    if child_prefix_list is not None:
        import capo_ec2.types.analysis_component

        out["prefix_list"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_prefix_list
        )
    child_protocols = el.find("protocolSet")
    if child_protocols is not None:
        import capo_ec2.types.string_list

        out["protocols"] = capo_ec2.types.string_list.deserialize_ec2_query(
            child_protocols
        )
    child_route_table_route = el.find("routeTableRoute")
    if child_route_table_route is not None:
        import capo_ec2.types.analysis_route_table_route

        out["route_table_route"] = (
            capo_ec2.types.analysis_route_table_route.deserialize_ec2_query(
                child_route_table_route
            )
        )
    child_route_table = el.find("routeTable")
    if child_route_table is not None:
        import capo_ec2.types.analysis_component

        out["route_table"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_route_table
        )
    child_security_group = el.find("securityGroup")
    if child_security_group is not None:
        import capo_ec2.types.analysis_component

        out["security_group"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_security_group
        )
    child_security_group_rule = el.find("securityGroupRule")
    if child_security_group_rule is not None:
        import capo_ec2.types.analysis_security_group_rule

        out["security_group_rule"] = (
            capo_ec2.types.analysis_security_group_rule.deserialize_ec2_query(
                child_security_group_rule
            )
        )
    child_security_groups = el.find("securityGroupSet")
    if child_security_groups is not None:
        import capo_ec2.types.analysis_component_list

        out["security_groups"] = (
            capo_ec2.types.analysis_component_list.deserialize_ec2_query(
                child_security_groups
            )
        )
    child_source_vpc = el.find("sourceVpc")
    if child_source_vpc is not None:
        import capo_ec2.types.analysis_component

        out["source_vpc"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_source_vpc
        )
    child_state = el.find("state")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_subnet = el.find("subnet")
    if child_subnet is not None:
        import capo_ec2.types.analysis_component

        out["subnet"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_subnet
        )
    child_subnet_route_table = el.find("subnetRouteTable")
    if child_subnet_route_table is not None:
        import capo_ec2.types.analysis_component

        out["subnet_route_table"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_subnet_route_table
            )
        )
    child_vpc = el.find("vpc")
    if child_vpc is not None:
        import capo_ec2.types.analysis_component

        out["vpc"] = capo_ec2.types.analysis_component.deserialize_ec2_query(child_vpc)
    child_vpc_endpoint = el.find("vpcEndpoint")
    if child_vpc_endpoint is not None:
        import capo_ec2.types.analysis_component

        out["vpc_endpoint"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_vpc_endpoint
        )
    child_vpn_connection = el.find("vpnConnection")
    if child_vpn_connection is not None:
        import capo_ec2.types.analysis_component

        out["vpn_connection"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_vpn_connection
        )
    child_vpn_gateway = el.find("vpnGateway")
    if child_vpn_gateway is not None:
        import capo_ec2.types.analysis_component

        out["vpn_gateway"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_vpn_gateway
        )
    child_transit_gateway = el.find("transitGateway")
    if child_transit_gateway is not None:
        import capo_ec2.types.analysis_component

        out["transit_gateway"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_transit_gateway
            )
        )
    child_transit_gateway_route_table = el.find("transitGatewayRouteTable")
    if child_transit_gateway_route_table is not None:
        import capo_ec2.types.analysis_component

        out["transit_gateway_route_table"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_transit_gateway_route_table
            )
        )
    child_transit_gateway_route_table_route = el.find("transitGatewayRouteTableRoute")
    if child_transit_gateway_route_table_route is not None:
        import capo_ec2.types.transit_gateway_route_table_route

        out["transit_gateway_route_table_route"] = (
            capo_ec2.types.transit_gateway_route_table_route.deserialize_ec2_query(
                child_transit_gateway_route_table_route
            )
        )
    child_transit_gateway_policy_table = el.find("transitGatewayPolicyTable")
    if child_transit_gateway_policy_table is not None:
        import capo_ec2.types.analysis_component

        out["transit_gateway_policy_table"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_transit_gateway_policy_table
            )
        )
    child_transit_gateway_policy_table_entry = el.find("transitGatewayPolicyTableEntry")
    if child_transit_gateway_policy_table_entry is not None:
        import capo_ec2.types.analysis_transit_gateway_policy_table_entry

        out["transit_gateway_policy_table_entry"] = (
            capo_ec2.types.analysis_transit_gateway_policy_table_entry.deserialize_ec2_query(
                child_transit_gateway_policy_table_entry
            )
        )
    child_transit_gateway_attachment = el.find("transitGatewayAttachment")
    if child_transit_gateway_attachment is not None:
        import capo_ec2.types.analysis_component

        out["transit_gateway_attachment"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_transit_gateway_attachment
            )
        )
    child_component_account = el.find("componentAccount")
    if child_component_account is not None:
        out["component_account"] = str(child_component_account.text or "")
    child_component_region = el.find("componentRegion")
    if child_component_region is not None:
        out["component_region"] = str(child_component_region.text or "")
    child_firewall_stateless_rule = el.find("firewallStatelessRule")
    if child_firewall_stateless_rule is not None:
        import capo_ec2.types.firewall_stateless_rule

        out["firewall_stateless_rule"] = (
            capo_ec2.types.firewall_stateless_rule.deserialize_ec2_query(
                child_firewall_stateless_rule
            )
        )
    child_firewall_stateful_rule = el.find("firewallStatefulRule")
    if child_firewall_stateful_rule is not None:
        import capo_ec2.types.firewall_stateful_rule

        out["firewall_stateful_rule"] = (
            capo_ec2.types.firewall_stateful_rule.deserialize_ec2_query(
                child_firewall_stateful_rule
            )
        )
    return out
