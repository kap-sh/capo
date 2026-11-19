"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPeeringAttachmentMultipathResilienceMode``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

TransitGatewayPeeringAttachmentMultipathResilienceMode: TypeAlias = Literal[
    "always-on",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(
    value: TransitGatewayPeeringAttachmentMultipathResilienceMode,
) -> str:
    return value


def from_ec2_query_text(
    text: str,
) -> TransitGatewayPeeringAttachmentMultipathResilienceMode:
    return cast(TransitGatewayPeeringAttachmentMultipathResilienceMode, text)


def serialize_ec2_query(
    value: TransitGatewayPeeringAttachmentMultipathResilienceMode,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(
    el: Element,
) -> TransitGatewayPeeringAttachmentMultipathResilienceMode:
    return from_ec2_query_text(el.text or "")
