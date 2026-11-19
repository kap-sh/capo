"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPeeringAttachmentMultipathResilienceStatus``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

TransitGatewayPeeringAttachmentMultipathResilienceStatus: TypeAlias = Literal[
    "pending",
    "enabled",
    "disabled",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(
    value: TransitGatewayPeeringAttachmentMultipathResilienceStatus,
) -> str:
    return value


def from_ec2_query_text(
    text: str,
) -> TransitGatewayPeeringAttachmentMultipathResilienceStatus:
    return cast(TransitGatewayPeeringAttachmentMultipathResilienceStatus, text)


def serialize_ec2_query(
    value: TransitGatewayPeeringAttachmentMultipathResilienceStatus,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(
    el: Element,
) -> TransitGatewayPeeringAttachmentMultipathResilienceStatus:
    return from_ec2_query_text(el.text or "")
