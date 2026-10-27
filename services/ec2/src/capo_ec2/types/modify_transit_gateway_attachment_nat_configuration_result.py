"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayAttachmentNatConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_attachment_id
    import capo_ec2.types.transit_gateway_attachment_nat_gateway_support_state
    import capo_ec2.types.transit_gateway_attachment_nat_system_route_support_value
    import capo_ec2.types.transit_gateway_nat_rule_list


class ModifyTransitGatewayAttachmentNatConfigurationResult(TypedDict, closed=True):
    transit_gateway_attachment_id: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the transit gateway attachment.</p>"""
    nat_gateway_support: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_nat_gateway_support_state.TransitGatewayAttachmentNatGatewaySupportState"
    ]
    """<p>The state of NAT gateway support for the attachment.</p>"""
    nat_system_route_support: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_nat_system_route_support_value.TransitGatewayAttachmentNatSystemRouteSupportValue"
    ]
    """<p>Specifies whether the transit gateway installs routes for the NAT CIDRs in the route tables to which the attachment propagates.</p>"""
    nat_gateway_rules: NotRequired[
        "capo_ec2.types.transit_gateway_nat_rule_list.TransitGatewayNatRuleList"
    ]
    """<p>The NAT gateway rules for the attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTransitGatewayAttachmentNatConfigurationResult,
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
        import capo_ec2.types.transit_gateway_attachment_nat_gateway_support_state

        capo_ec2.types.transit_gateway_attachment_nat_gateway_support_state.serialize_ec2_query(
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
        import capo_ec2.types.transit_gateway_nat_rule_list

        capo_ec2.types.transit_gateway_nat_rule_list.serialize_ec2_query(
            value["nat_gateway_rules"], pairs, f"{key_prefix}NatGatewayRuleSet"
        )


def deserialize_ec2_query(
    el: Element,
) -> ModifyTransitGatewayAttachmentNatConfigurationResult:
    out: ModifyTransitGatewayAttachmentNatConfigurationResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_attachment_id = el.find("transitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_nat_gateway_support = el.find("natGatewaySupport")
    if child_nat_gateway_support is not None:
        import capo_ec2.types.transit_gateway_attachment_nat_gateway_support_state

        out["nat_gateway_support"] = (
            capo_ec2.types.transit_gateway_attachment_nat_gateway_support_state.deserialize_ec2_query(
                child_nat_gateway_support
            )
        )
    child_nat_system_route_support = el.find("natSystemRouteSupport")
    if child_nat_system_route_support is not None:
        import capo_ec2.types.transit_gateway_attachment_nat_system_route_support_value

        out["nat_system_route_support"] = (
            capo_ec2.types.transit_gateway_attachment_nat_system_route_support_value.deserialize_ec2_query(
                child_nat_system_route_support
            )
        )
    child_nat_gateway_rules = el.find("natGatewayRuleSet")
    if child_nat_gateway_rules is not None:
        import capo_ec2.types.transit_gateway_nat_rule_list

        out["nat_gateway_rules"] = (
            capo_ec2.types.transit_gateway_nat_rule_list.deserialize_ec2_query(
                child_nat_gateway_rules
            )
        )
    return out
