"""Generated from Smithy shape ``com.amazonaws.ec2#VpnConnection``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.customer_gateway_configuration
    import capo_ec2.types.gateway_association_state
    import capo_ec2.types.gateway_type
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.vgw_telemetry_list
    import capo_ec2.types.vpn_connection_options
    import capo_ec2.types.vpn_state
    import capo_ec2.types.vpn_static_route_list


class VpnConnection(TypedDict, closed=True):
    category: NotRequired["capo_ec2.types.string.String"]
    """<p>The category of the VPN connection. A value of <code>VPN</code> indicates an Amazon Web Services VPN connection. A value of <code>VPN-Classic</code> indicates an Amazon Web Services Classic VPN connection.</p>"""
    transit_gateway_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the transit gateway associated with the VPN connection.</p>"""
    vpn_concentrator_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPN concentrator associated with the VPN connection.</p>"""
    core_network_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the core network.</p>"""
    core_network_attachment_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the core network attachment.</p>"""
    gateway_association_state: NotRequired[
        "capo_ec2.types.gateway_association_state.GatewayAssociationState"
    ]
    """<p>The current state of the gateway association.</p>"""
    options: NotRequired["capo_ec2.types.vpn_connection_options.VpnConnectionOptions"]
    """<p>The VPN connection options.</p>"""
    routes: NotRequired["capo_ec2.types.vpn_static_route_list.VpnStaticRouteList"]
    """<p>The static routes associated with the VPN connection.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the VPN connection.</p>"""
    vgw_telemetry: NotRequired["capo_ec2.types.vgw_telemetry_list.VgwTelemetryList"]
    """<p>Information about the VPN tunnel.</p>"""
    pre_shared_key_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Secrets Manager secret storing the pre-shared key(s) for the VPN connection.</p>"""
    vpn_connection_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPN connection.</p>"""
    state: NotRequired["capo_ec2.types.vpn_state.VpnState"]
    """<p>The current state of the VPN connection.</p>"""
    customer_gateway_configuration: NotRequired[
        "capo_ec2.types.customer_gateway_configuration.customerGatewayConfiguration"
    ]
    """<p>The configuration information for the VPN connection's customer gateway (in the native XML format). This element is always present in the <a>CreateVpnConnection</a> response; however, it's present in the <a>DescribeVpnConnections</a> response only if the VPN connection is in the <code>pending</code> or <code>available</code> state.</p>"""
    type: NotRequired["capo_ec2.types.gateway_type.GatewayType"]
    """<p>The type of VPN connection.</p>"""
    customer_gateway_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the customer gateway at your end of the VPN connection.</p>"""
    vpn_gateway_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the virtual private gateway at the Amazon Web Services side of the VPN connection.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnConnection, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "category" in value:
        pairs.append((f"{key_prefix}Category", str(value["category"])))
    if "transit_gateway_id" in value:
        pairs.append(
            (f"{key_prefix}TransitGatewayId", str(value["transit_gateway_id"]))
        )
    if "vpn_concentrator_id" in value:
        pairs.append(
            (f"{key_prefix}VpnConcentratorId", str(value["vpn_concentrator_id"]))
        )
    if "core_network_arn" in value:
        pairs.append((f"{key_prefix}CoreNetworkArn", str(value["core_network_arn"])))
    if "core_network_attachment_arn" in value:
        pairs.append(
            (
                f"{key_prefix}CoreNetworkAttachmentArn",
                str(value["core_network_attachment_arn"]),
            )
        )
    if "gateway_association_state" in value:
        import capo_ec2.types.gateway_association_state

        capo_ec2.types.gateway_association_state.serialize_ec2_query(
            value["gateway_association_state"],
            pairs,
            f"{key_prefix}GatewayAssociationState",
        )
    if "options" in value:
        import capo_ec2.types.vpn_connection_options

        capo_ec2.types.vpn_connection_options.serialize_ec2_query(
            value["options"], pairs, f"{key_prefix}Options"
        )
    if "routes" in value:
        import capo_ec2.types.vpn_static_route_list

        capo_ec2.types.vpn_static_route_list.serialize_ec2_query(
            value["routes"], pairs, f"{key_prefix}Routes"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "vgw_telemetry" in value:
        import capo_ec2.types.vgw_telemetry_list

        capo_ec2.types.vgw_telemetry_list.serialize_ec2_query(
            value["vgw_telemetry"], pairs, f"{key_prefix}VgwTelemetry"
        )
    if "pre_shared_key_arn" in value:
        pairs.append((f"{key_prefix}PreSharedKeyArn", str(value["pre_shared_key_arn"])))
    if "vpn_connection_id" in value:
        pairs.append((f"{key_prefix}VpnConnectionId", str(value["vpn_connection_id"])))
    if "state" in value:
        import capo_ec2.types.vpn_state

        capo_ec2.types.vpn_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "customer_gateway_configuration" in value:
        pairs.append(
            (
                f"{key_prefix}CustomerGatewayConfiguration",
                str(value["customer_gateway_configuration"]),
            )
        )
    if "type" in value:
        import capo_ec2.types.gateway_type

        capo_ec2.types.gateway_type.serialize_ec2_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "customer_gateway_id" in value:
        pairs.append(
            (f"{key_prefix}CustomerGatewayId", str(value["customer_gateway_id"]))
        )
    if "vpn_gateway_id" in value:
        pairs.append((f"{key_prefix}VpnGatewayId", str(value["vpn_gateway_id"])))


def deserialize_ec2_query(el: Element) -> VpnConnection:
    out: VpnConnection = {}  # type: ignore[typeddict-item]
    child_category = el.find("category")
    if child_category is not None:
        out["category"] = str(child_category.text or "")
    child_transit_gateway_id = el.find("transitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_vpn_concentrator_id = el.find("vpnConcentratorId")
    if child_vpn_concentrator_id is not None:
        out["vpn_concentrator_id"] = str(child_vpn_concentrator_id.text or "")
    child_core_network_arn = el.find("coreNetworkArn")
    if child_core_network_arn is not None:
        out["core_network_arn"] = str(child_core_network_arn.text or "")
    child_core_network_attachment_arn = el.find("coreNetworkAttachmentArn")
    if child_core_network_attachment_arn is not None:
        out["core_network_attachment_arn"] = str(
            child_core_network_attachment_arn.text or ""
        )
    child_gateway_association_state = el.find("gatewayAssociationState")
    if child_gateway_association_state is not None:
        import capo_ec2.types.gateway_association_state

        out["gateway_association_state"] = (
            capo_ec2.types.gateway_association_state.deserialize_ec2_query(
                child_gateway_association_state
            )
        )
    child_options = el.find("options")
    if child_options is not None:
        import capo_ec2.types.vpn_connection_options

        out["options"] = capo_ec2.types.vpn_connection_options.deserialize_ec2_query(
            child_options
        )
    child_routes = el.find("routes")
    if child_routes is not None:
        import capo_ec2.types.vpn_static_route_list

        out["routes"] = capo_ec2.types.vpn_static_route_list.deserialize_ec2_query(
            child_routes
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_vgw_telemetry = el.find("vgwTelemetry")
    if child_vgw_telemetry is not None:
        import capo_ec2.types.vgw_telemetry_list

        out["vgw_telemetry"] = capo_ec2.types.vgw_telemetry_list.deserialize_ec2_query(
            child_vgw_telemetry
        )
    child_pre_shared_key_arn = el.find("preSharedKeyArn")
    if child_pre_shared_key_arn is not None:
        out["pre_shared_key_arn"] = str(child_pre_shared_key_arn.text or "")
    child_vpn_connection_id = el.find("vpnConnectionId")
    if child_vpn_connection_id is not None:
        out["vpn_connection_id"] = str(child_vpn_connection_id.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.vpn_state

        out["state"] = capo_ec2.types.vpn_state.deserialize_ec2_query(child_state)
    child_customer_gateway_configuration = el.find("customerGatewayConfiguration")
    if child_customer_gateway_configuration is not None:
        out["customer_gateway_configuration"] = str(
            child_customer_gateway_configuration.text or ""
        )
    child_type = el.find("type")
    if child_type is not None:
        import capo_ec2.types.gateway_type

        out["type"] = capo_ec2.types.gateway_type.deserialize_ec2_query(child_type)
    child_customer_gateway_id = el.find("customerGatewayId")
    if child_customer_gateway_id is not None:
        out["customer_gateway_id"] = str(child_customer_gateway_id.text or "")
    child_vpn_gateway_id = el.find("vpnGatewayId")
    if child_vpn_gateway_id is not None:
        out["vpn_gateway_id"] = str(child_vpn_gateway_id.text or "")
    return out


def redact_sensitive(value: VpnConnection) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "options" in value:
        import capo_ec2.types.vpn_connection_options

        out["options"] = capo_ec2.types.vpn_connection_options.redact_sensitive(
            value["options"]
        )
    if "customer_gateway_configuration" in value:
        out["customer_gateway_configuration"] = "*** Sensitive Data Redacted ***"
    return out
