"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentNatGatewaySupportState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

TransitGatewayAttachmentNatGatewaySupportState: TypeAlias = Literal[
    "enabled",
    "disabled",
    "enabling",
    "disabling",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TransitGatewayAttachmentNatGatewaySupportState) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayAttachmentNatGatewaySupportState:
    return cast(TransitGatewayAttachmentNatGatewaySupportState, text)


def serialize_ec2_query(
    value: TransitGatewayAttachmentNatGatewaySupportState,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(
    el: Element,
) -> TransitGatewayAttachmentNatGatewaySupportState:
    return from_ec2_query_text(el.text or "")
