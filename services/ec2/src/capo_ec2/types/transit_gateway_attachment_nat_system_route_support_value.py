"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentNatSystemRouteSupportValue``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

TransitGatewayAttachmentNatSystemRouteSupportValue: TypeAlias = Literal[
    "enable",
    "disable",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TransitGatewayAttachmentNatSystemRouteSupportValue) -> str:
    return value


def from_ec2_query_text(
    text: str,
) -> TransitGatewayAttachmentNatSystemRouteSupportValue:
    return cast(TransitGatewayAttachmentNatSystemRouteSupportValue, text)


def serialize_ec2_query(
    value: TransitGatewayAttachmentNatSystemRouteSupportValue,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(
    el: Element,
) -> TransitGatewayAttachmentNatSystemRouteSupportValue:
    return from_ec2_query_text(el.text or "")
