"""Generated from Smithy shape ``com.amazonaws.ec2#VpnConnectionOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string
    import capo_ec2.types.tunnel_inside_ip_version
    import capo_ec2.types.tunnel_options_list
    import capo_ec2.types.vpn_tunnel_bandwidth


class VpnConnectionOptions(TypedDict, closed=True):
    enable_acceleration: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether acceleration is enabled for the VPN connection.</p>"""
    static_routes_only: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the VPN connection uses static routes only. Static routes must be used for devices that don't support BGP.</p>"""
    local_ipv4_network_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 CIDR on the customer gateway (on-premises) side of the VPN connection.</p>"""
    remote_ipv4_network_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 CIDR on the Amazon Web Services side of the VPN connection.</p>"""
    local_ipv6_network_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv6 CIDR on the customer gateway (on-premises) side of the VPN connection.</p>"""
    remote_ipv6_network_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv6 CIDR on the Amazon Web Services side of the VPN connection.</p>"""
    outside_ip_address_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The type of IPv4 address assigned to the outside interface of the customer gateway.</p> <p>Valid values: <code>PrivateIpv4</code> | <code>PublicIpv4</code> | <code>Ipv6</code> </p> <p>Default: <code>PublicIpv4</code> </p>"""
    transport_transit_gateway_attachment_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The transit gateway attachment ID in use for the VPN tunnel.</p>"""
    tunnel_inside_ip_version: NotRequired[
        "capo_ec2.types.tunnel_inside_ip_version.TunnelInsideIpVersion"
    ]
    """<p>Indicates whether the VPN tunnels process IPv4 or IPv6 traffic.</p>"""
    tunnel_options: NotRequired["capo_ec2.types.tunnel_options_list.TunnelOptionsList"]
    """<p>Indicates the VPN tunnel options.</p>"""
    tunnel_bandwidth: NotRequired[
        "capo_ec2.types.vpn_tunnel_bandwidth.VpnTunnelBandwidth"
    ]
    """<p> The configured bandwidth for the VPN tunnel. Represents the current throughput capacity setting for the tunnel connection. <code>standard</code> tunnel bandwidth supports up to 1.25 Gbps per tunnel while <code>large</code> supports up to 5 Gbps per tunnel. If no tunnel bandwidth was specified for the connection, <code>standard</code> is used as the default value. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnConnectionOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "enable_acceleration" in value:
        pairs.append(
            (
                f"{key_prefix}EnableAcceleration",
                "true" if value["enable_acceleration"] else "false",
            )
        )
    if "static_routes_only" in value:
        pairs.append(
            (
                f"{key_prefix}StaticRoutesOnly",
                "true" if value["static_routes_only"] else "false",
            )
        )
    if "local_ipv4_network_cidr" in value:
        pairs.append(
            (f"{key_prefix}LocalIpv4NetworkCidr", str(value["local_ipv4_network_cidr"]))
        )
    if "remote_ipv4_network_cidr" in value:
        pairs.append(
            (
                f"{key_prefix}RemoteIpv4NetworkCidr",
                str(value["remote_ipv4_network_cidr"]),
            )
        )
    if "local_ipv6_network_cidr" in value:
        pairs.append(
            (f"{key_prefix}LocalIpv6NetworkCidr", str(value["local_ipv6_network_cidr"]))
        )
    if "remote_ipv6_network_cidr" in value:
        pairs.append(
            (
                f"{key_prefix}RemoteIpv6NetworkCidr",
                str(value["remote_ipv6_network_cidr"]),
            )
        )
    if "outside_ip_address_type" in value:
        pairs.append(
            (f"{key_prefix}OutsideIpAddressType", str(value["outside_ip_address_type"]))
        )
    if "transport_transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransportTransitGatewayAttachmentId",
                str(value["transport_transit_gateway_attachment_id"]),
            )
        )
    if "tunnel_inside_ip_version" in value:
        import capo_ec2.types.tunnel_inside_ip_version

        capo_ec2.types.tunnel_inside_ip_version.serialize_ec2_query(
            value["tunnel_inside_ip_version"],
            pairs,
            f"{key_prefix}TunnelInsideIpVersion",
        )
    if "tunnel_options" in value:
        import capo_ec2.types.tunnel_options_list

        capo_ec2.types.tunnel_options_list.serialize_ec2_query(
            value["tunnel_options"], pairs, f"{key_prefix}TunnelOptionSet"
        )
    if "tunnel_bandwidth" in value:
        import capo_ec2.types.vpn_tunnel_bandwidth

        capo_ec2.types.vpn_tunnel_bandwidth.serialize_ec2_query(
            value["tunnel_bandwidth"], pairs, f"{key_prefix}TunnelBandwidth"
        )


def deserialize_ec2_query(el: Element) -> VpnConnectionOptions:
    out: VpnConnectionOptions = {}  # type: ignore[typeddict-item]
    child_enable_acceleration = el.find("enableAcceleration")
    if child_enable_acceleration is not None:
        out["enable_acceleration"] = (
            child_enable_acceleration.text or ""
        ).lower() == "true"
    child_static_routes_only = el.find("staticRoutesOnly")
    if child_static_routes_only is not None:
        out["static_routes_only"] = (
            child_static_routes_only.text or ""
        ).lower() == "true"
    child_local_ipv4_network_cidr = el.find("localIpv4NetworkCidr")
    if child_local_ipv4_network_cidr is not None:
        out["local_ipv4_network_cidr"] = str(child_local_ipv4_network_cidr.text or "")
    child_remote_ipv4_network_cidr = el.find("remoteIpv4NetworkCidr")
    if child_remote_ipv4_network_cidr is not None:
        out["remote_ipv4_network_cidr"] = str(child_remote_ipv4_network_cidr.text or "")
    child_local_ipv6_network_cidr = el.find("localIpv6NetworkCidr")
    if child_local_ipv6_network_cidr is not None:
        out["local_ipv6_network_cidr"] = str(child_local_ipv6_network_cidr.text or "")
    child_remote_ipv6_network_cidr = el.find("remoteIpv6NetworkCidr")
    if child_remote_ipv6_network_cidr is not None:
        out["remote_ipv6_network_cidr"] = str(child_remote_ipv6_network_cidr.text or "")
    child_outside_ip_address_type = el.find("outsideIpAddressType")
    if child_outside_ip_address_type is not None:
        out["outside_ip_address_type"] = str(child_outside_ip_address_type.text or "")
    child_transport_transit_gateway_attachment_id = el.find(
        "transportTransitGatewayAttachmentId"
    )
    if child_transport_transit_gateway_attachment_id is not None:
        out["transport_transit_gateway_attachment_id"] = str(
            child_transport_transit_gateway_attachment_id.text or ""
        )
    child_tunnel_inside_ip_version = el.find("tunnelInsideIpVersion")
    if child_tunnel_inside_ip_version is not None:
        import capo_ec2.types.tunnel_inside_ip_version

        out["tunnel_inside_ip_version"] = (
            capo_ec2.types.tunnel_inside_ip_version.deserialize_ec2_query(
                child_tunnel_inside_ip_version
            )
        )
    child_tunnel_options = el.find("tunnelOptionSet")
    if child_tunnel_options is not None:
        import capo_ec2.types.tunnel_options_list

        out["tunnel_options"] = (
            capo_ec2.types.tunnel_options_list.deserialize_ec2_query(
                child_tunnel_options
            )
        )
    child_tunnel_bandwidth = el.find("tunnelBandwidth")
    if child_tunnel_bandwidth is not None:
        import capo_ec2.types.vpn_tunnel_bandwidth

        out["tunnel_bandwidth"] = (
            capo_ec2.types.vpn_tunnel_bandwidth.deserialize_ec2_query(
                child_tunnel_bandwidth
            )
        )
    return out


def redact_sensitive(value: VpnConnectionOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tunnel_options" in value:
        import capo_ec2.types.tunnel_options_list

        out["tunnel_options"] = capo_ec2.types.tunnel_options_list.redact_sensitive(
            value["tunnel_options"]
        )
    return out
