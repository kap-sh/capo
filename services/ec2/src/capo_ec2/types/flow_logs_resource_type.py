"""Generated from Smithy shape ``com.amazonaws.ec2#FlowLogsResourceType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

FlowLogsResourceType: TypeAlias = Literal[
    "VPC",
    "Subnet",
    "NetworkInterface",
    "TransitGateway",
    "TransitGatewayAttachment",
    "RegionalNatGateway",
    "CoreNetwork",
    "CoreNetworkEdge",
    "CoreNetworkAttachment",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: FlowLogsResourceType) -> str:
    return value


def from_ec2_query_text(text: str) -> FlowLogsResourceType:
    return cast(FlowLogsResourceType, text)


def serialize_ec2_query(
    value: FlowLogsResourceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FlowLogsResourceType:
    return from_ec2_query_text(el.text or "")
