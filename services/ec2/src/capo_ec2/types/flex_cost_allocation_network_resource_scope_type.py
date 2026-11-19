"""Generated from Smithy shape ``com.amazonaws.ec2#FlexCostAllocationNetworkResourceScopeType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

"""<p>The type of scope used for a scope-based policy association. Valid values are <code>account</code>, <code>vpc</code>, and <code>subnet</code>.</p>"""
FlexCostAllocationNetworkResourceScopeType: TypeAlias = Literal[
    "account",
    "vpc",
    "subnet",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: FlexCostAllocationNetworkResourceScopeType) -> str:
    return value


def from_ec2_query_text(text: str) -> FlexCostAllocationNetworkResourceScopeType:
    return cast(FlexCostAllocationNetworkResourceScopeType, text)


def serialize_ec2_query(
    value: FlexCostAllocationNetworkResourceScopeType,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FlexCostAllocationNetworkResourceScopeType:
    return from_ec2_query_text(el.text or "")
