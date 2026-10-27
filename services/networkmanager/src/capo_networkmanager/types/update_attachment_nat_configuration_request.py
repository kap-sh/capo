"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateAttachmentNatConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_id
    import capo_networkmanager.types.boxed_boolean
    import capo_networkmanager.types.client_token
    import capo_networkmanager.types.nat_gateway_support_value
    import capo_networkmanager.types.nat_rule_request_list


class UpdateAttachmentNatConfigurationRequest(TypedDict, closed=True):
    attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId"
    """<p>The ID of the attachment to update the NAT configuration for.</p>"""
    nat_gateway_support: NotRequired[
        "capo_networkmanager.types.nat_gateway_support_value.NatGatewaySupportValue"
    ]
    """<p>Specifies whether to enable or disable NAT gateway support on the attachment. When you disable NAT gateway support, the attachment keeps its NAT rules but doesn't apply them. To enable NAT gateway support, the attachment must have at least one NAT rule, either specified in this request or already configured on the attachment. If you omit this parameter, NAT gateway support is unchanged.</p>"""
    nat_system_route_support: NotRequired[
        "capo_networkmanager.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Specifies whether the core network installs system routes for the NAT CIDR blocks of the attachment's NAT rules. System routes have a route type of <code>SYSTEM</code>. NAT is applied to traffic whether or not this option is enabled. If you omit this parameter, the current value is unchanged.</p>"""
    nat_gateway_rules: NotRequired[
        "capo_networkmanager.types.nat_rule_request_list.NatRuleRequestList"
    ]
    """<p>The complete set of NAT rules for the attachment, up to 50 rules. The rules that you specify replace the existing rules of the attachment, matched by rule number. Existing rules that aren't included in the request are deleted. To delete all NAT rules, specify an empty list. You can delete all NAT rules only when NAT gateway support is disabled, or when you disable it in the same request. If you omit this parameter, the existing rules are unchanged.</p>"""
    client_token: NotRequired["capo_networkmanager.types.client_token.ClientToken"]
    """<p>The client token associated with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAttachmentNatConfigurationRequest) -> dict:
    out: dict = {}
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
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateAttachmentNatConfigurationRequest:
    out: UpdateAttachmentNatConfigurationRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
