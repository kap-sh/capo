"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayAttachmentNatConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.transit_gateway_attachment_id
    import capo_ec2.types.transit_gateway_attachment_nat_gateway_support_value
    import capo_ec2.types.transit_gateway_attachment_nat_system_route_support_value
    import capo_ec2.types.transit_gateway_nat_rule_request_list


class ModifyTransitGatewayAttachmentNatConfigurationRequest(TypedDict, closed=True):
    transit_gateway_attachment_id: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the transit gateway attachment.</p>"""
    nat_gateway_support: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_nat_gateway_support_value.TransitGatewayAttachmentNatGatewaySupportValue"
    ]
    """<p>Specifies whether to enable or disable NAT gateway support for the attachment. To enable NAT gateway support, the attachment must have at least one NAT gateway rule. You can't modify the NAT configuration while NAT gateway support is <code>enabling</code> or <code>disabling</code>. If you omit this parameter, the current value doesn't change.</p>"""
    nat_system_route_support: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_nat_system_route_support_value.TransitGatewayAttachmentNatSystemRouteSupportValue"
    ]
    """<p>Specifies whether the transit gateway installs routes for the NAT CIDRs in the route tables to which the attachment propagates. For VPC attachments, the transit gateway always installs these routes. You can enable or disable this option only for Amazon Web Services Direct Connect gateway attachments and Site-to-Site VPN attachments that use dynamic routing. For these attachments, the default is <code>enable</code>. If you omit this parameter, the current value doesn't change.</p>"""
    nat_gateway_rules: NotRequired[
        "capo_ec2.types.transit_gateway_nat_rule_request_list.TransitGatewayNatRuleRequestList"
    ]
    """<p>The NAT gateway rules for the attachment. The rules that you specify replace all existing NAT gateway rules for the attachment. You can specify up to 50 rules for an attachment. If you omit this parameter, the existing rules don't change. To remove all rules, use <code>ResetNatGatewayRules</code>.</p>"""
    reset_nat_gateway_rules: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to remove all NAT gateway rules from the attachment. If you omit this parameter, the transit gateway doesn't remove any rules. You can't specify this parameter together with <code>NatGatewayRules</code>. Because you can't enable NAT gateway support without rules, also set <code>NatGatewaySupport</code> to <code>disable</code> in the same request if NAT gateway support is currently enabled.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTransitGatewayAttachmentNatConfigurationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "nat_gateway_support" in value:
        import capo_ec2.types.transit_gateway_attachment_nat_gateway_support_value

        capo_ec2.types.transit_gateway_attachment_nat_gateway_support_value.serialize_ec2_query(
            value["nat_gateway_support"], pairs, f"{key_prefix}NatGatewaySupport"
        )
    if "nat_system_route_support" in value:
        import capo_ec2.types.transit_gateway_attachment_nat_system_route_support_value

        capo_ec2.types.transit_gateway_attachment_nat_system_route_support_value.serialize_ec2_query(
            value["nat_system_route_support"],
            pairs,
            f"{key_prefix}NatSystemRouteSupport",
        )
    if "nat_gateway_rules" in value:
        import capo_ec2.types.transit_gateway_nat_rule_request_list

        capo_ec2.types.transit_gateway_nat_rule_request_list.serialize_ec2_query(
            value["nat_gateway_rules"], pairs, f"{key_prefix}NatGatewayRule"
        )
    if "reset_nat_gateway_rules" in value:
        pairs.append(
            (
                f"{key_prefix}ResetNatGatewayRules",
                "true" if value["reset_nat_gateway_rules"] else "false",
            )
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> ModifyTransitGatewayAttachmentNatConfigurationRequest:
    out: ModifyTransitGatewayAttachmentNatConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_nat_gateway_support = el.find("NatGatewaySupport")
    if child_nat_gateway_support is not None:
        import capo_ec2.types.transit_gateway_attachment_nat_gateway_support_value

        out["nat_gateway_support"] = (
            capo_ec2.types.transit_gateway_attachment_nat_gateway_support_value.deserialize_ec2_query(
                child_nat_gateway_support
            )
        )
    child_nat_system_route_support = el.find("NatSystemRouteSupport")
    if child_nat_system_route_support is not None:
        import capo_ec2.types.transit_gateway_attachment_nat_system_route_support_value

        out["nat_system_route_support"] = (
            capo_ec2.types.transit_gateway_attachment_nat_system_route_support_value.deserialize_ec2_query(
                child_nat_system_route_support
            )
        )
    child_nat_gateway_rules = el.find("NatGatewayRule")
    if child_nat_gateway_rules is not None:
        import capo_ec2.types.transit_gateway_nat_rule_request_list

        out["nat_gateway_rules"] = (
            capo_ec2.types.transit_gateway_nat_rule_request_list.deserialize_ec2_query(
                child_nat_gateway_rules
            )
        )
    child_reset_nat_gateway_rules = el.find("ResetNatGatewayRules")
    if child_reset_nat_gateway_rules is not None:
        out["reset_nat_gateway_rules"] = (
            child_reset_nat_gateway_rules.text or ""
        ).lower() == "true"
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
