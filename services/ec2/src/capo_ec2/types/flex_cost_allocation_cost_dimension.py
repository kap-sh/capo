"""Generated from Smithy shape ``com.amazonaws.ec2#FlexCostAllocationCostDimension``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

"""<p>A cost dimension used for allocation. Valid values are <code>data-transfer</code> and <code>data-processing</code>. <code>data-processing</code> is valid only in a <code>NatFcaPolicyDocument</code>.</p>"""
FlexCostAllocationCostDimension: TypeAlias = Literal[
    "data-transfer",
    "data-processing",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: FlexCostAllocationCostDimension) -> str:
    return value


def from_ec2_query_text(text: str) -> FlexCostAllocationCostDimension:
    return cast(FlexCostAllocationCostDimension, text)


def serialize_ec2_query(
    value: FlexCostAllocationCostDimension, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FlexCostAllocationCostDimension:
    return from_ec2_query_text(el.text or "")
