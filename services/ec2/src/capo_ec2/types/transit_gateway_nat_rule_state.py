"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayNatRuleState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

TransitGatewayNatRuleState: TypeAlias = Literal[
    "pending",
    "activated",
    "deactivated",
    "deleting",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TransitGatewayNatRuleState) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayNatRuleState:
    return cast(TransitGatewayNatRuleState, text)


def serialize_ec2_query(
    value: TransitGatewayNatRuleState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayNatRuleState:
    return from_ec2_query_text(el.text or "")
