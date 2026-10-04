"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyClientVpnEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.client_connect_options
    import capo_ec2.types.client_login_banner_options
    import capo_ec2.types.client_route_enforcement_options
    import capo_ec2.types.client_vpn_endpoint_id
    import capo_ec2.types.client_vpn_security_group_id_set
    import capo_ec2.types.connection_log_options
    import capo_ec2.types.device_posture_options
    import capo_ec2.types.dns_servers_options_modify_structure
    import capo_ec2.types.integer
    import capo_ec2.types.self_service_portal
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_configuration_input_structure
    import capo_ec2.types.vpc_id


class ModifyClientVpnEndpointRequest(TypedDict, closed=True):
    client_vpn_endpoint_id: NotRequired[
        "capo_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
    ]
    """<p>The ID of the Client VPN endpoint to modify.</p>"""
    server_certificate_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the server certificate to be used. The server certificate must be provisioned in Certificate Manager (ACM).</p>"""
    connection_log_options: NotRequired[
        "capo_ec2.types.connection_log_options.ConnectionLogOptions"
    ]
    """<p>Information about the client connection logging options.</p> <p>If you enable client connection logging, data about client connections is sent to a Cloudwatch Logs log stream. The following information is logged:</p> <ul> <li> <p>Client connection requests</p> </li> <li> <p>Client connection results (successful and unsuccessful)</p> </li> <li> <p>Reasons for unsuccessful client connection requests</p> </li> <li> <p>Client connection termination time</p> </li> </ul>"""
    dns_servers: NotRequired[
        "capo_ec2.types.dns_servers_options_modify_structure.DnsServersOptionsModifyStructure"
    ]
    """<p>Information about the DNS servers to be used by Client VPN connections. A Client VPN endpoint can have up to two DNS servers.</p>"""
    vpn_port: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The port number to assign to the Client VPN endpoint for TCP and UDP traffic.</p> <p>Valid Values: <code>443</code> | <code>1194</code> </p> <p>Default Value: <code>443</code> </p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A brief description of the Client VPN endpoint.</p>"""
    split_tunnel: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the VPN is split-tunnel.</p> <p>For information about split-tunnel VPN endpoints, see <a href="https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html">Split-tunnel Client VPN endpoint</a> in the <i>Client VPN Administrator Guide</i>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    security_group_ids: NotRequired[
        "capo_ec2.types.client_vpn_security_group_id_set.ClientVpnSecurityGroupIdSet"
    ]
    """<p>The IDs of one or more security groups to apply to the target network.</p>"""
    vpc_id: NotRequired["capo_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC to associate with the Client VPN endpoint.</p>"""
    self_service_portal: NotRequired[
        "capo_ec2.types.self_service_portal.SelfServicePortal"
    ]
    """<p>Specify whether to enable the self-service portal for the Client VPN endpoint.</p>"""
    client_connect_options: NotRequired[
        "capo_ec2.types.client_connect_options.ClientConnectOptions"
    ]
    """<p>The options for managing connection authorization for new client connections.</p>"""
    session_timeout_hours: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum VPN session duration time in hours.</p> <p>Valid values: <code>8 | 10 | 12 | 24</code> </p> <p>Default value: <code>24</code> </p>"""
    client_login_banner_options: NotRequired[
        "capo_ec2.types.client_login_banner_options.ClientLoginBannerOptions"
    ]
    """<p>Options for enabling a customizable text banner that will be displayed on Amazon Web Services provided clients when a VPN session is established.</p>"""
    client_route_enforcement_options: NotRequired[
        "capo_ec2.types.client_route_enforcement_options.ClientRouteEnforcementOptions"
    ]
    """<p>Client route enforcement is a feature of the Client VPN service that helps enforce administrator defined routes on devices connected through the VPN. T his feature helps improve your security posture by ensuring that network traffic originating from a connected client is not inadvertently sent outside the VPN tunnel.</p> <p>Client route enforcement works by monitoring the route table of a connected device for routing policy changes to the VPN connection. If the feature detects any VPN routing policy modifications, it will automatically force an update to the route table, reverting it back to the expected route configurations.</p>"""
    disconnect_on_session_timeout: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the client VPN session is disconnected after the maximum timeout specified in <code>sessionTimeoutHours</code> is reached. If <code>true</code>, users are prompted to reconnect client VPN. If <code>false</code>, client VPN attempts to reconnect automatically. The default value is <code>true</code>.</p>"""
    transit_gateway_configuration: NotRequired[
        "capo_ec2.types.transit_gateway_configuration_input_structure.TransitGatewayConfigurationInputStructure"
    ]
    """<p>The Transit Gateway configuration for the Client VPN endpoint. This option is currently not supported.</p>"""
    device_posture_options: NotRequired[
        "capo_ec2.types.device_posture_options.DevicePostureOptions"
    ]
    """<p>The device posture options for the Client VPN endpoint. Specifying this parameter replaces the entire device posture configuration for the endpoint. To remove all device trust providers, specify an empty list.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyClientVpnEndpointRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_vpn_endpoint_id" in value:
        pairs.append(
            (f"{key_prefix}ClientVpnEndpointId", str(value["client_vpn_endpoint_id"]))
        )
    if "server_certificate_arn" in value:
        pairs.append(
            (f"{key_prefix}ServerCertificateArn", str(value["server_certificate_arn"]))
        )
    if "connection_log_options" in value:
        import capo_ec2.types.connection_log_options

        capo_ec2.types.connection_log_options.serialize_ec2_query(
            value["connection_log_options"], pairs, f"{key_prefix}ConnectionLogOptions"
        )
    if "dns_servers" in value:
        import capo_ec2.types.dns_servers_options_modify_structure

        capo_ec2.types.dns_servers_options_modify_structure.serialize_ec2_query(
            value["dns_servers"], pairs, f"{key_prefix}DnsServers"
        )
    if "vpn_port" in value:
        pairs.append((f"{key_prefix}VpnPort", str(value["vpn_port"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "split_tunnel" in value:
        pairs.append(
            (f"{key_prefix}SplitTunnel", "true" if value["split_tunnel"] else "false")
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "security_group_ids" in value:
        import capo_ec2.types.client_vpn_security_group_id_set

        capo_ec2.types.client_vpn_security_group_id_set.serialize_ec2_query(
            value["security_group_ids"], pairs, f"{key_prefix}SecurityGroupId"
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "self_service_portal" in value:
        import capo_ec2.types.self_service_portal

        capo_ec2.types.self_service_portal.serialize_ec2_query(
            value["self_service_portal"], pairs, f"{key_prefix}SelfServicePortal"
        )
    if "client_connect_options" in value:
        import capo_ec2.types.client_connect_options

        capo_ec2.types.client_connect_options.serialize_ec2_query(
            value["client_connect_options"], pairs, f"{key_prefix}ClientConnectOptions"
        )
    if "session_timeout_hours" in value:
        pairs.append(
            (f"{key_prefix}SessionTimeoutHours", str(value["session_timeout_hours"]))
        )
    if "client_login_banner_options" in value:
        import capo_ec2.types.client_login_banner_options

        capo_ec2.types.client_login_banner_options.serialize_ec2_query(
            value["client_login_banner_options"],
            pairs,
            f"{key_prefix}ClientLoginBannerOptions",
        )
    if "client_route_enforcement_options" in value:
        import capo_ec2.types.client_route_enforcement_options

        capo_ec2.types.client_route_enforcement_options.serialize_ec2_query(
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
    if "transit_gateway_configuration" in value:
        import capo_ec2.types.transit_gateway_configuration_input_structure

        capo_ec2.types.transit_gateway_configuration_input_structure.serialize_ec2_query(
            value["transit_gateway_configuration"],
            pairs,
            f"{key_prefix}TransitGatewayConfiguration",
        )
    if "device_posture_options" in value:
        import capo_ec2.types.device_posture_options

        capo_ec2.types.device_posture_options.serialize_ec2_query(
            value["device_posture_options"], pairs, f"{key_prefix}DevicePostureOptions"
        )


def deserialize_ec2_query(el: Element) -> ModifyClientVpnEndpointRequest:
    out: ModifyClientVpnEndpointRequest = {}  # type: ignore[typeddict-item]
    child_client_vpn_endpoint_id = el.find("ClientVpnEndpointId")
    if child_client_vpn_endpoint_id is not None:
        out["client_vpn_endpoint_id"] = str(child_client_vpn_endpoint_id.text or "")
    child_server_certificate_arn = el.find("ServerCertificateArn")
    if child_server_certificate_arn is not None:
        out["server_certificate_arn"] = str(child_server_certificate_arn.text or "")
    child_connection_log_options = el.find("ConnectionLogOptions")
    if child_connection_log_options is not None:
        import capo_ec2.types.connection_log_options

        out["connection_log_options"] = (
            capo_ec2.types.connection_log_options.deserialize_ec2_query(
                child_connection_log_options
            )
        )
    child_dns_servers = el.find("DnsServers")
    if child_dns_servers is not None:
        import capo_ec2.types.dns_servers_options_modify_structure

        out["dns_servers"] = (
            capo_ec2.types.dns_servers_options_modify_structure.deserialize_ec2_query(
                child_dns_servers
            )
        )
    child_vpn_port = el.find("VpnPort")
    if child_vpn_port is not None:
        out["vpn_port"] = int(child_vpn_port.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_split_tunnel = el.find("SplitTunnel")
    if child_split_tunnel is not None:
        out["split_tunnel"] = (child_split_tunnel.text or "").lower() == "true"
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_security_group_ids = el.find("SecurityGroupId")
    if child_security_group_ids is not None:
        import capo_ec2.types.client_vpn_security_group_id_set

        out["security_group_ids"] = (
            capo_ec2.types.client_vpn_security_group_id_set.deserialize_ec2_query(
                child_security_group_ids
            )
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_self_service_portal = el.find("SelfServicePortal")
    if child_self_service_portal is not None:
        import capo_ec2.types.self_service_portal

        out["self_service_portal"] = (
            capo_ec2.types.self_service_portal.deserialize_ec2_query(
                child_self_service_portal
            )
        )
    child_client_connect_options = el.find("ClientConnectOptions")
    if child_client_connect_options is not None:
        import capo_ec2.types.client_connect_options

        out["client_connect_options"] = (
            capo_ec2.types.client_connect_options.deserialize_ec2_query(
                child_client_connect_options
            )
        )
    child_session_timeout_hours = el.find("SessionTimeoutHours")
    if child_session_timeout_hours is not None:
        out["session_timeout_hours"] = int(child_session_timeout_hours.text or "")
    child_client_login_banner_options = el.find("ClientLoginBannerOptions")
    if child_client_login_banner_options is not None:
        import capo_ec2.types.client_login_banner_options

        out["client_login_banner_options"] = (
            capo_ec2.types.client_login_banner_options.deserialize_ec2_query(
                child_client_login_banner_options
            )
        )
    child_client_route_enforcement_options = el.find("ClientRouteEnforcementOptions")
    if child_client_route_enforcement_options is not None:
        import capo_ec2.types.client_route_enforcement_options

        out["client_route_enforcement_options"] = (
            capo_ec2.types.client_route_enforcement_options.deserialize_ec2_query(
                child_client_route_enforcement_options
            )
        )
    child_disconnect_on_session_timeout = el.find("DisconnectOnSessionTimeout")
    if child_disconnect_on_session_timeout is not None:
        out["disconnect_on_session_timeout"] = (
            child_disconnect_on_session_timeout.text or ""
        ).lower() == "true"
    child_transit_gateway_configuration = el.find("TransitGatewayConfiguration")
    if child_transit_gateway_configuration is not None:
        import capo_ec2.types.transit_gateway_configuration_input_structure

        out["transit_gateway_configuration"] = (
            capo_ec2.types.transit_gateway_configuration_input_structure.deserialize_ec2_query(
                child_transit_gateway_configuration
            )
        )
    child_device_posture_options = el.find("DevicePostureOptions")
    if child_device_posture_options is not None:
        import capo_ec2.types.device_posture_options

        out["device_posture_options"] = (
            capo_ec2.types.device_posture_options.deserialize_ec2_query(
                child_device_posture_options
            )
        )
    return out
