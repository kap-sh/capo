"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.associated_target_network_set
    import capo_ec2.types.boolean
    import capo_ec2.types.client_connect_response_options
    import capo_ec2.types.client_login_banner_response_options
    import capo_ec2.types.client_route_enforcement_response_options
    import capo_ec2.types.client_vpn_authentication_list
    import capo_ec2.types.client_vpn_endpoint_status
    import capo_ec2.types.client_vpn_security_group_id_set
    import capo_ec2.types.connection_log_response_options
    import capo_ec2.types.endpoint_ip_address_type
    import capo_ec2.types.integer
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.traffic_ip_address_type
    import capo_ec2.types.transit_gateway_configuration_describe_endpoint_structure
    import capo_ec2.types.transport_protocol
    import capo_ec2.types.value_string_list
    import capo_ec2.types.vpc_id
    import capo_ec2.types.vpn_protocol


class ClientVpnEndpoint(TypedDict, closed=True):
    client_vpn_endpoint_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Client VPN endpoint.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A brief description of the endpoint.</p>"""
    status: NotRequired[
        "capo_ec2.types.client_vpn_endpoint_status.ClientVpnEndpointStatus"
    ]
    """<p>The current state of the Client VPN endpoint.</p>"""
    creation_time: NotRequired["capo_ec2.types.string.String"]
    """<p>The date and time the Client VPN endpoint was created.</p>"""
    deletion_time: NotRequired["capo_ec2.types.string.String"]
    """<p>The date and time the Client VPN endpoint was deleted, if applicable.</p>"""
    dns_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The DNS name to be used by clients when connecting to the Client VPN endpoint.</p>"""
    client_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 address range, in CIDR notation, from which client IP addresses are assigned.</p>"""
    dns_servers: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>Information about the DNS servers to be used for DNS resolution. </p>"""
    split_tunnel: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether split-tunnel is enabled in the Client VPN endpoint.</p> <p>For information about split-tunnel VPN endpoints, see <a href="https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html">Split-Tunnel Client VPN endpoint</a> in the <i>Client VPN Administrator Guide</i>.</p>"""
    vpn_protocol: NotRequired["capo_ec2.types.vpn_protocol.VpnProtocol"]
    """<p>The protocol used by the VPN session.</p>"""
    transport_protocol: NotRequired[
        "capo_ec2.types.transport_protocol.TransportProtocol"
    ]
    """<p>The transport protocol used by the Client VPN endpoint.</p>"""
    vpn_port: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The port number for the Client VPN endpoint.</p>"""
    associated_target_networks: NotRequired[
        "capo_ec2.types.associated_target_network_set.AssociatedTargetNetworkSet"
    ]
    """<p>Information about the associated target networks. A target network is a subnet in a VPC.</p>"""
    server_certificate_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the server certificate.</p>"""
    authentication_options: NotRequired[
        "capo_ec2.types.client_vpn_authentication_list.ClientVpnAuthenticationList"
    ]
    """<p>Information about the authentication method used by the Client VPN endpoint.</p>"""
    connection_log_options: NotRequired[
        "capo_ec2.types.connection_log_response_options.ConnectionLogResponseOptions"
    ]
    """<p>Information about the client connection logging options for the Client VPN endpoint.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the Client VPN endpoint.</p>"""
    security_group_ids: NotRequired[
        "capo_ec2.types.client_vpn_security_group_id_set.ClientVpnSecurityGroupIdSet"
    ]
    """<p>The IDs of the security groups for the target network.</p>"""
    vpc_id: NotRequired["capo_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    self_service_portal_url: NotRequired["capo_ec2.types.string.String"]
    """<p>The URL of the self-service portal.</p>"""
    client_connect_options: NotRequired[
        "capo_ec2.types.client_connect_response_options.ClientConnectResponseOptions"
    ]
    """<p>The options for managing connection authorization for new client connections.</p>"""
    session_timeout_hours: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum VPN session duration time in hours.</p> <p>Valid values: <code>8 | 10 | 12 | 24</code> </p> <p>Default value: <code>24</code> </p>"""
    client_login_banner_options: NotRequired[
        "capo_ec2.types.client_login_banner_response_options.ClientLoginBannerResponseOptions"
    ]
    """<p>Options for enabling a customizable text banner that will be displayed on Amazon Web Services provided clients when a VPN session is established.</p>"""
    client_route_enforcement_options: NotRequired[
        "capo_ec2.types.client_route_enforcement_response_options.ClientRouteEnforcementResponseOptions"
    ]
    """<p>Client route enforcement is a feature of the Client VPN service that helps enforce administrator defined routes on devices connected through the VPN. T his feature helps improve your security posture by ensuring that network traffic originating from a connected client is not inadvertently sent outside the VPN tunnel.</p> <p>Client route enforcement works by monitoring the route table of a connected device for routing policy changes to the VPN connection. If the feature detects any VPN routing policy modifications, it will automatically force an update to the route table, reverting it back to the expected route configurations.</p>"""
    disconnect_on_session_timeout: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the client VPN session is disconnected after the maximum <code>sessionTimeoutHours</code> is reached. If <code>true</code>, users are prompted to reconnect client VPN. If <code>false</code>, client VPN attempts to reconnect automatically. The default value is <code>true</code>.</p>"""
    endpoint_ip_address_type: NotRequired[
        "capo_ec2.types.endpoint_ip_address_type.EndpointIpAddressType"
    ]
    """<p>The IP address type of the Client VPN endpoint. Possible values are <code>ipv4</code> for IPv4 addressing only, <code>ipv6</code> for IPv6 addressing only, or <code>dual-stack </code>for both IPv4 and IPv6 addressing.</p>"""
    traffic_ip_address_type: NotRequired[
        "capo_ec2.types.traffic_ip_address_type.TrafficIpAddressType"
    ]
    """<p>The IP address type of the Client VPN endpoint. Possible values are either <code>ipv4</code> for IPv4 addressing only, <code>ipv6</code> for IPv6 addressing only, or <code>dual-stack</code> for both IPv4 and IPv6 addressing.</p>"""
    transit_gateway_configuration: NotRequired[
        "capo_ec2.types.transit_gateway_configuration_describe_endpoint_structure.TransitGatewayConfigurationDescribeEndpointStructure"
    ]
    """<p>The Transit Gateway configuration for the Client VPN endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientVpnEndpoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_vpn_endpoint_id" in value:
        pairs.append(
            (f"{key_prefix}ClientVpnEndpointId", str(value["client_vpn_endpoint_id"]))
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "status" in value:
        import capo_ec2.types.client_vpn_endpoint_status

        capo_ec2.types.client_vpn_endpoint_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "creation_time" in value:
        pairs.append((f"{key_prefix}CreationTime", str(value["creation_time"])))
    if "deletion_time" in value:
        pairs.append((f"{key_prefix}DeletionTime", str(value["deletion_time"])))
    if "dns_name" in value:
        pairs.append((f"{key_prefix}DnsName", str(value["dns_name"])))
    if "client_cidr_block" in value:
        pairs.append((f"{key_prefix}ClientCidrBlock", str(value["client_cidr_block"])))
    if "dns_servers" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["dns_servers"], pairs, f"{key_prefix}DnsServer"
        )
    if "split_tunnel" in value:
        pairs.append(
            (f"{key_prefix}SplitTunnel", "true" if value["split_tunnel"] else "false")
        )
    if "vpn_protocol" in value:
        import capo_ec2.types.vpn_protocol

        capo_ec2.types.vpn_protocol.serialize_ec2_query(
            value["vpn_protocol"], pairs, f"{key_prefix}VpnProtocol"
        )
    if "transport_protocol" in value:
        import capo_ec2.types.transport_protocol

        capo_ec2.types.transport_protocol.serialize_ec2_query(
            value["transport_protocol"], pairs, f"{key_prefix}TransportProtocol"
        )
    if "vpn_port" in value:
        pairs.append((f"{key_prefix}VpnPort", str(value["vpn_port"])))
    if "associated_target_networks" in value:
        import capo_ec2.types.associated_target_network_set

        capo_ec2.types.associated_target_network_set.serialize_ec2_query(
            value["associated_target_networks"],
            pairs,
            f"{key_prefix}AssociatedTargetNetwork",
        )
    if "server_certificate_arn" in value:
        pairs.append(
            (f"{key_prefix}ServerCertificateArn", str(value["server_certificate_arn"]))
        )
    if "authentication_options" in value:
        import capo_ec2.types.client_vpn_authentication_list

        capo_ec2.types.client_vpn_authentication_list.serialize_ec2_query(
            value["authentication_options"], pairs, f"{key_prefix}AuthenticationOptions"
        )
    if "connection_log_options" in value:
        import capo_ec2.types.connection_log_response_options

        capo_ec2.types.connection_log_response_options.serialize_ec2_query(
            value["connection_log_options"], pairs, f"{key_prefix}ConnectionLogOptions"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "security_group_ids" in value:
        import capo_ec2.types.client_vpn_security_group_id_set

        capo_ec2.types.client_vpn_security_group_id_set.serialize_ec2_query(
            value["security_group_ids"], pairs, f"{key_prefix}SecurityGroupIdSet"
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "self_service_portal_url" in value:
        pairs.append(
            (f"{key_prefix}SelfServicePortalUrl", str(value["self_service_portal_url"]))
        )
    if "client_connect_options" in value:
        import capo_ec2.types.client_connect_response_options

        capo_ec2.types.client_connect_response_options.serialize_ec2_query(
            value["client_connect_options"], pairs, f"{key_prefix}ClientConnectOptions"
        )
    if "session_timeout_hours" in value:
        pairs.append(
            (f"{key_prefix}SessionTimeoutHours", str(value["session_timeout_hours"]))
        )
    if "client_login_banner_options" in value:
        import capo_ec2.types.client_login_banner_response_options

        capo_ec2.types.client_login_banner_response_options.serialize_ec2_query(
            value["client_login_banner_options"],
            pairs,
            f"{key_prefix}ClientLoginBannerOptions",
        )
    if "client_route_enforcement_options" in value:
        import capo_ec2.types.client_route_enforcement_response_options

        capo_ec2.types.client_route_enforcement_response_options.serialize_ec2_query(
            value["client_route_enforcement_options"],
            pairs,
            f"{key_prefix}ClientRouteEnforcementOptions",
        )
    if "disconnect_on_session_timeout" in value:
        pairs.append(
            (
                f"{key_prefix}DisconnectOnSessionTimeout",
                "true" if value["disconnect_on_session_timeout"] else "false",
            )
        )
    if "endpoint_ip_address_type" in value:
        import capo_ec2.types.endpoint_ip_address_type

        capo_ec2.types.endpoint_ip_address_type.serialize_ec2_query(
            value["endpoint_ip_address_type"],
            pairs,
            f"{key_prefix}EndpointIpAddressType",
        )
    if "traffic_ip_address_type" in value:
        import capo_ec2.types.traffic_ip_address_type

        capo_ec2.types.traffic_ip_address_type.serialize_ec2_query(
            value["traffic_ip_address_type"], pairs, f"{key_prefix}TrafficIpAddressType"
        )
    if "transit_gateway_configuration" in value:
        import capo_ec2.types.transit_gateway_configuration_describe_endpoint_structure

        capo_ec2.types.transit_gateway_configuration_describe_endpoint_structure.serialize_ec2_query(
            value["transit_gateway_configuration"],
            pairs,
            f"{key_prefix}TransitGatewayConfiguration",
        )


def deserialize_ec2_query(el: Element) -> ClientVpnEndpoint:
    out: ClientVpnEndpoint = {}  # type: ignore[typeddict-item]
    child_client_vpn_endpoint_id = el.find("clientVpnEndpointId")
    if child_client_vpn_endpoint_id is not None:
        out["client_vpn_endpoint_id"] = str(child_client_vpn_endpoint_id.text or "")
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.client_vpn_endpoint_status

        out["status"] = capo_ec2.types.client_vpn_endpoint_status.deserialize_ec2_query(
            child_status
        )
    child_creation_time = el.find("creationTime")
    if child_creation_time is not None:
        out["creation_time"] = str(child_creation_time.text or "")
    child_deletion_time = el.find("deletionTime")
    if child_deletion_time is not None:
        out["deletion_time"] = str(child_deletion_time.text or "")
    child_dns_name = el.find("dnsName")
    if child_dns_name is not None:
        out["dns_name"] = str(child_dns_name.text or "")
    child_client_cidr_block = el.find("clientCidrBlock")
    if child_client_cidr_block is not None:
        out["client_cidr_block"] = str(child_client_cidr_block.text or "")
    child_dns_servers = el.find("dnsServer")
    if child_dns_servers is not None:
        import capo_ec2.types.value_string_list

        out["dns_servers"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            child_dns_servers
        )
    child_split_tunnel = el.find("splitTunnel")
    if child_split_tunnel is not None:
        out["split_tunnel"] = (child_split_tunnel.text or "").lower() == "true"
    child_vpn_protocol = el.find("vpnProtocol")
    if child_vpn_protocol is not None:
        import capo_ec2.types.vpn_protocol

        out["vpn_protocol"] = capo_ec2.types.vpn_protocol.deserialize_ec2_query(
            child_vpn_protocol
        )
    child_transport_protocol = el.find("transportProtocol")
    if child_transport_protocol is not None:
        import capo_ec2.types.transport_protocol

        out["transport_protocol"] = (
            capo_ec2.types.transport_protocol.deserialize_ec2_query(
                child_transport_protocol
            )
        )
    child_vpn_port = el.find("vpnPort")
    if child_vpn_port is not None:
        out["vpn_port"] = int(child_vpn_port.text or "")
    child_associated_target_networks = el.find("associatedTargetNetwork")
    if child_associated_target_networks is not None:
        import capo_ec2.types.associated_target_network_set

        out["associated_target_networks"] = (
            capo_ec2.types.associated_target_network_set.deserialize_ec2_query(
                child_associated_target_networks
            )
        )
    child_server_certificate_arn = el.find("serverCertificateArn")
    if child_server_certificate_arn is not None:
        out["server_certificate_arn"] = str(child_server_certificate_arn.text or "")
    child_authentication_options = el.find("authenticationOptions")
    if child_authentication_options is not None:
        import capo_ec2.types.client_vpn_authentication_list

        out["authentication_options"] = (
            capo_ec2.types.client_vpn_authentication_list.deserialize_ec2_query(
                child_authentication_options
            )
        )
    child_connection_log_options = el.find("connectionLogOptions")
    if child_connection_log_options is not None:
        import capo_ec2.types.connection_log_response_options

        out["connection_log_options"] = (
            capo_ec2.types.connection_log_response_options.deserialize_ec2_query(
                child_connection_log_options
            )
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_security_group_ids = el.find("securityGroupIdSet")
    if child_security_group_ids is not None:
        import capo_ec2.types.client_vpn_security_group_id_set

        out["security_group_ids"] = (
            capo_ec2.types.client_vpn_security_group_id_set.deserialize_ec2_query(
                child_security_group_ids
            )
        )
    child_vpc_id = el.find("vpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_self_service_portal_url = el.find("selfServicePortalUrl")
    if child_self_service_portal_url is not None:
        out["self_service_portal_url"] = str(child_self_service_portal_url.text or "")
    child_client_connect_options = el.find("clientConnectOptions")
    if child_client_connect_options is not None:
        import capo_ec2.types.client_connect_response_options

        out["client_connect_options"] = (
            capo_ec2.types.client_connect_response_options.deserialize_ec2_query(
                child_client_connect_options
            )
        )
    child_session_timeout_hours = el.find("sessionTimeoutHours")
    if child_session_timeout_hours is not None:
        out["session_timeout_hours"] = int(child_session_timeout_hours.text or "")
    child_client_login_banner_options = el.find("clientLoginBannerOptions")
    if child_client_login_banner_options is not None:
        import capo_ec2.types.client_login_banner_response_options

        out["client_login_banner_options"] = (
            capo_ec2.types.client_login_banner_response_options.deserialize_ec2_query(
                child_client_login_banner_options
            )
        )
    child_client_route_enforcement_options = el.find("clientRouteEnforcementOptions")
    if child_client_route_enforcement_options is not None:
        import capo_ec2.types.client_route_enforcement_response_options

        out["client_route_enforcement_options"] = (
            capo_ec2.types.client_route_enforcement_response_options.deserialize_ec2_query(
                child_client_route_enforcement_options
            )
        )
    child_disconnect_on_session_timeout = el.find("disconnectOnSessionTimeout")
    if child_disconnect_on_session_timeout is not None:
        out["disconnect_on_session_timeout"] = (
            child_disconnect_on_session_timeout.text or ""
        ).lower() == "true"
    child_endpoint_ip_address_type = el.find("endpointIpAddressType")
    if child_endpoint_ip_address_type is not None:
        import capo_ec2.types.endpoint_ip_address_type

        out["endpoint_ip_address_type"] = (
            capo_ec2.types.endpoint_ip_address_type.deserialize_ec2_query(
                child_endpoint_ip_address_type
            )
        )
    child_traffic_ip_address_type = el.find("trafficIpAddressType")
    if child_traffic_ip_address_type is not None:
        import capo_ec2.types.traffic_ip_address_type

        out["traffic_ip_address_type"] = (
            capo_ec2.types.traffic_ip_address_type.deserialize_ec2_query(
                child_traffic_ip_address_type
            )
        )
    child_transit_gateway_configuration = el.find("transitGatewayConfiguration")
    if child_transit_gateway_configuration is not None:
        import capo_ec2.types.transit_gateway_configuration_describe_endpoint_structure

        out["transit_gateway_configuration"] = (
            capo_ec2.types.transit_gateway_configuration_describe_endpoint_structure.deserialize_ec2_query(
                child_transit_gateway_configuration
            )
        )
    return out
