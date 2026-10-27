"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

TransitGatewayRouteType: TypeAlias = Literal[
    "static",
    "propagated",
    "system",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TransitGatewayRouteType) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayRouteType:
    return cast(TransitGatewayRouteType, text)


def serialize_ec2_query(
    value: TransitGatewayRouteType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayRouteType:
    return from_ec2_query_text(el.text or "")
