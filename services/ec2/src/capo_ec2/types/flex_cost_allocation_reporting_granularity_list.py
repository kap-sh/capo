"""Generated from Smithy shape ``com.amazonaws.ec2#FlexCostAllocationReportingGranularityList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.flex_cost_allocation_reporting_granularity

FlexCostAllocationReportingGranularityList: TypeAlias = list[
    "capo_ec2.types.flex_cost_allocation_reporting_granularity.FlexCostAllocationReportingGranularity"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FlexCostAllocationReportingGranularityList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.flex_cost_allocation_reporting_granularity

        capo_ec2.types.flex_cost_allocation_reporting_granularity.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> FlexCostAllocationReportingGranularityList:
    import capo_ec2.types.flex_cost_allocation_reporting_granularity

    out: FlexCostAllocationReportingGranularityList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.flex_cost_allocation_reporting_granularity.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> FlexCostAllocationReportingGranularityList:
    import capo_ec2.types.flex_cost_allocation_reporting_granularity

    out: FlexCostAllocationReportingGranularityList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.flex_cost_allocation_reporting_granularity.deserialize_ec2_query(
                child
            )
        )
    return out
