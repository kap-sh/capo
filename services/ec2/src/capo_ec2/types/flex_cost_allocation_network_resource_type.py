"""Generated from Smithy shape ``com.amazonaws.ec2#FlexCostAllocationNetworkResourceType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

"""<p>The type of network resource that a flex cost allocation policy applies to. Valid values are <code>natgw</code> (NAT gateway), <code>pcx</code> (Amazon VPC peering connection), and <code>ec2</code> (EC2 instance).</p>"""
FlexCostAllocationNetworkResourceType: TypeAlias = Literal[
    "natgw",
    "pcx",
    "ec2",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: FlexCostAllocationNetworkResourceType) -> str:
    return value


def from_ec2_query_text(text: str) -> FlexCostAllocationNetworkResourceType:
    return cast(FlexCostAllocationNetworkResourceType, text)


def serialize_ec2_query(
    value: FlexCostAllocationNetworkResourceType,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FlexCostAllocationNetworkResourceType:
    return from_ec2_query_text(el.text or "")
