"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayNatRuleRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_nat_rule_request

TransitGatewayNatRuleRequestList: TypeAlias = list[
    "capo_ec2.types.transit_gateway_nat_rule_request.TransitGatewayNatRuleRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayNatRuleRequestList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.transit_gateway_nat_rule_request

        capo_ec2.types.transit_gateway_nat_rule_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayNatRuleRequestList:
    import capo_ec2.types.transit_gateway_nat_rule_request

    out: TransitGatewayNatRuleRequestList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.transit_gateway_nat_rule_request.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> TransitGatewayNatRuleRequestList:
    import capo_ec2.types.transit_gateway_nat_rule_request

    out: TransitGatewayNatRuleRequestList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.transit_gateway_nat_rule_request.deserialize_ec2_query(child)
        )
    return out
