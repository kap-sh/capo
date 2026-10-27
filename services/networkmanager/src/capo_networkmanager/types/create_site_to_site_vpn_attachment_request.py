"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateSiteToSiteVpnAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.boxed_boolean
    import capo_networkmanager.types.client_token
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.nat_gateway_support_value
    import capo_networkmanager.types.nat_rule_request_list
    import capo_networkmanager.types.tag_list
    import capo_networkmanager.types.vpn_connection_arn


class CreateSiteToSiteVpnAttachmentRequest(TypedDict, closed=True):
    core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of a core network where you're creating a site-to-site VPN attachment.</p>"""
    vpn_connection_arn: "capo_networkmanager.types.vpn_connection_arn.VpnConnectionArn"
    """<p>The ARN identifying the VPN attachment.</p>"""
    routing_policy_label: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The routing policy label to apply to the Site-to-Site VPN attachment for traffic routing decisions.</p>"""
    nat_gateway_support: NotRequired[
        "capo_networkmanager.types.nat_gateway_support_value.NatGatewaySupportValue"
    ]
    """<p>Specifies whether to enable NAT gateway support on the Site-to-Site VPN attachment. To enable NAT gateway support, you must also specify at least one NAT rule. If you don't specify a value, NAT gateway support is disabled. Only the core network owner can configure NAT on an attachment.</p>"""
    nat_system_route_support: NotRequired[
        "capo_networkmanager.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Specifies whether the core network installs system routes for the NAT CIDR blocks of the attachment's NAT rules. System routes have a route type of <code>SYSTEM</code>. NAT is applied to traffic whether or not this option is enabled. The default is <code>true</code> for VPN connections that use BGP and <code>false</code> for VPN connections that use static routing. If the VPN connection uses static routing, you must specify <code>false</code> or omit this parameter.</p>"""
    nat_gateway_rules: NotRequired[
        "capo_networkmanager.types.nat_rule_request_list.NatRuleRequestList"
    ]
    """<p>The NAT rules for the Site-to-Site VPN attachment, up to 50 rules.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The tags associated with the request.</p>"""
    client_token: NotRequired["capo_networkmanager.types.client_token.ClientToken"]
    """<p>The client token associated with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSiteToSiteVpnAttachmentRequest) -> dict:
    out: dict = {}
    out["CoreNetworkId"] = value["core_network_id"]
    out["VpnConnectionArn"] = value["vpn_connection_arn"]
    if "routing_policy_label" in value:
        out["RoutingPolicyLabel"] = value["routing_policy_label"]
    if "nat_gateway_support" in value:
        import capo_networkmanager.types.nat_gateway_support_value

        out["NatGatewaySupport"] = (
            capo_networkmanager.types.nat_gateway_support_value.serialize_json(
                value["nat_gateway_support"]
            )
        )
    if "nat_system_route_support" in value:
        out["NatSystemRouteSupport"] = value["nat_system_route_support"]
    if "nat_gateway_rules" in value:
        import capo_networkmanager.types.nat_rule_request_list

        out["NatGatewayRules"] = (
            capo_networkmanager.types.nat_rule_request_list.serialize_json(
                value["nat_gateway_rules"]
            )
        )
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateSiteToSiteVpnAttachmentRequest:
    out: CreateSiteToSiteVpnAttachmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("CoreNetworkId") is not None:
        out["core_network_id"] = data["CoreNetworkId"]
    else:
        out["core_network_id"] = ""
    if data.get("VpnConnectionArn") is not None:
        out["vpn_connection_arn"] = data["VpnConnectionArn"]
    else:
        out["vpn_connection_arn"] = ""
    if data.get("RoutingPolicyLabel") is not None:
        out["routing_policy_label"] = data["RoutingPolicyLabel"]
    if data.get("NatGatewaySupport") is not None:
        import capo_networkmanager.types.nat_gateway_support_value

        out["nat_gateway_support"] = (
            capo_networkmanager.types.nat_gateway_support_value.deserialize_json(
                data["NatGatewaySupport"]
            )
        )
    if data.get("NatSystemRouteSupport") is not None:
        out["nat_system_route_support"] = data["NatSystemRouteSupport"]
    if data.get("NatGatewayRules") is not None:
        import capo_networkmanager.types.nat_rule_request_list

        out["nat_gateway_rules"] = (
            capo_networkmanager.types.nat_rule_request_list.deserialize_json(
                data["NatGatewayRules"]
            )
        )
    if data.get("Tags") is not None:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
