"""Generated from Smithy shape ``com.amazonaws.ec2#FlexCostAllocationReportingGranularity``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

"""<p>The resource granularity level at which networking costs are allocated. Valid values are <code>eni</code>, <code>ec2</code>, <code>subnet</code>, <code>vpc</code>, <code>account</code>, <code>peering-id</code>, and <code>cidr</code>.</p> <p>Which values you can use depends on the policy document. <code>peering-id</code> is valid only in a <code>PcxFcaPolicyDocument</code>.</p>"""
FlexCostAllocationReportingGranularity: TypeAlias = Literal[
    "eni",
    "ec2",
    "subnet",
    "vpc",
    "account",
    "peering-id",
    "cidr",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: FlexCostAllocationReportingGranularity) -> str:
    return value


def from_ec2_query_text(text: str) -> FlexCostAllocationReportingGranularity:
    return cast(FlexCostAllocationReportingGranularity, text)


def serialize_ec2_query(
    value: FlexCostAllocationReportingGranularity,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FlexCostAllocationReportingGranularity:
    return from_ec2_query_text(el.text or "")
