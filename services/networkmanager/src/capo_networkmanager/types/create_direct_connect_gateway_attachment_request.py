"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateDirectConnectGatewayAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.boxed_boolean
    import capo_networkmanager.types.client_token
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.direct_connect_gateway_arn
    import capo_networkmanager.types.external_region_code_list
    import capo_networkmanager.types.nat_gateway_support_value
    import capo_networkmanager.types.nat_rule_request_list
    import capo_networkmanager.types.tag_list


class CreateDirectConnectGatewayAttachmentRequest(TypedDict, closed=True):
    core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of the Cloud WAN core network that the Direct Connect gateway attachment should be attached to.</p>"""
    direct_connect_gateway_arn: (
        "capo_networkmanager.types.direct_connect_gateway_arn.DirectConnectGatewayArn"
    )
    """<p>The ARN of the Direct Connect gateway attachment.</p>"""
    routing_policy_label: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The routing policy label to apply to the Direct Connect Gateway attachment for traffic routing decisions.</p>"""
    edge_locations: (
        "capo_networkmanager.types.external_region_code_list.ExternalRegionCodeList"
    )
    """<p>One or more core network edge locations that the Direct Connect gateway attachment is associated with. </p>"""
    nat_gateway_support: NotRequired[
        "capo_networkmanager.types.nat_gateway_support_value.NatGatewaySupportValue"
    ]
    """<p>Specifies whether to enable NAT gateway support on the Direct Connect gateway attachment. To enable NAT gateway support, you must also specify at least one NAT rule. If you don't specify a value, NAT gateway support is disabled. Only the core network owner can configure NAT on an attachment.</p>"""
    nat_system_route_support: NotRequired[
        "capo_networkmanager.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Specifies whether the core network installs system routes for the NAT CIDR blocks of the attachment's NAT rules. System routes have a route type of <code>SYSTEM</code>. NAT is applied to traffic whether or not this option is enabled. The default is <code>true</code>.</p>"""
    nat_gateway_rules: NotRequired[
        "capo_networkmanager.types.nat_rule_request_list.NatRuleRequestList"
    ]
    """<p>The NAT rules for the Direct Connect gateway attachment, up to 50 rules.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The key value tags to apply to the Direct Connect gateway attachment during creation.</p>"""
    client_token: NotRequired["capo_networkmanager.types.client_token.ClientToken"]
    """<p>client token</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDirectConnectGatewayAttachmentRequest) -> dict:
    out: dict = {}
    out["CoreNetworkId"] = value["core_network_id"]
    out["DirectConnectGatewayArn"] = value["direct_connect_gateway_arn"]
    if "routing_policy_label" in value:
        out["RoutingPolicyLabel"] = value["routing_policy_label"]
    import capo_networkmanager.types.external_region_code_list

    out["EdgeLocations"] = (
        capo_networkmanager.types.external_region_code_list.serialize_json(
            value["edge_locations"]
        )
    )
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


def deserialize_json(data: dict) -> CreateDirectConnectGatewayAttachmentRequest:
    out: CreateDirectConnectGatewayAttachmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("CoreNetworkId") is not None:
        out["core_network_id"] = data["CoreNetworkId"]
    else:
        out["core_network_id"] = ""
    if data.get("DirectConnectGatewayArn") is not None:
        out["direct_connect_gateway_arn"] = data["DirectConnectGatewayArn"]
    else:
        out["direct_connect_gateway_arn"] = ""
    if data.get("RoutingPolicyLabel") is not None:
        out["routing_policy_label"] = data["RoutingPolicyLabel"]
    if data.get("EdgeLocations") is not None:
        import capo_networkmanager.types.external_region_code_list

        out["edge_locations"] = (
            capo_networkmanager.types.external_region_code_list.deserialize_json(
                data["EdgeLocations"]
            )
        )
    else:
        out["edge_locations"] = []
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
