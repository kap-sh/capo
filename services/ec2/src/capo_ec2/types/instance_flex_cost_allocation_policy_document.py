"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceFlexCostAllocationPolicyDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.flex_cost_allocation_cidr_range_specifications
    import capo_ec2.types.flex_cost_allocation_cost_dimension_list
    import capo_ec2.types.flex_cost_allocation_reporting_granularity_list


class InstanceFlexCostAllocationPolicyDocument(TypedDict, closed=True):
    reporting_granularity: NotRequired[
        "capo_ec2.types.flex_cost_allocation_reporting_granularity_list.FlexCostAllocationReportingGranularityList"
    ]
    """<p>The resource granularity level at which networking costs are allocated. This parameter is required. Specify exactly one value. Valid values are <code>eni</code>, <code>ec2</code>, <code>subnet</code>, <code>vpc</code>, <code>account</code>, and <code>cidr</code>.</p>"""
    dimensions: NotRequired[
        "capo_ec2.types.flex_cost_allocation_cost_dimension_list.FlexCostAllocationCostDimensionList"
    ]
    """<p>The cost dimensions to report. This parameter is required. The only valid value is <code>data-transfer</code>.</p>"""
    cidr_range_specifications: NotRequired[
        "capo_ec2.types.flex_cost_allocation_cidr_range_specifications.FlexCostAllocationCidrRangeSpecifications"
    ]
    """<p>The CIDR range mappings to use for cost allocation. Specify this value when <code>ReportingGranularity</code> is <code>cidr</code>, and omit it otherwise.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceFlexCostAllocationPolicyDocument,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reporting_granularity" in value:
        import capo_ec2.types.flex_cost_allocation_reporting_granularity_list

        capo_ec2.types.flex_cost_allocation_reporting_granularity_list.serialize_ec2_query(
            value["reporting_granularity"], pairs, f"{key_prefix}ReportingGranularity"
        )
    if "dimensions" in value:
        import capo_ec2.types.flex_cost_allocation_cost_dimension_list

        capo_ec2.types.flex_cost_allocation_cost_dimension_list.serialize_ec2_query(
            value["dimensions"], pairs, f"{key_prefix}Dimensions"
        )
    if "cidr_range_specifications" in value:
        import capo_ec2.types.flex_cost_allocation_cidr_range_specifications

        capo_ec2.types.flex_cost_allocation_cidr_range_specifications.serialize_ec2_query(
            value["cidr_range_specifications"],
            pairs,
            f"{key_prefix}CidrRangeSpecifications",
        )


def deserialize_ec2_query(el: Element) -> InstanceFlexCostAllocationPolicyDocument:
    out: InstanceFlexCostAllocationPolicyDocument = {}  # type: ignore[typeddict-item]
    child_reporting_granularity = el.find("ReportingGranularity")
    if child_reporting_granularity is not None:
        import capo_ec2.types.flex_cost_allocation_reporting_granularity_list

        out["reporting_granularity"] = (
            capo_ec2.types.flex_cost_allocation_reporting_granularity_list.deserialize_ec2_query(
                child_reporting_granularity
            )
        )
    child_dimensions = el.find("Dimensions")
    if child_dimensions is not None:
        import capo_ec2.types.flex_cost_allocation_cost_dimension_list

        out["dimensions"] = (
            capo_ec2.types.flex_cost_allocation_cost_dimension_list.deserialize_ec2_query(
                child_dimensions
            )
        )
    child_cidr_range_specifications = el.find("CidrRangeSpecifications")
    if child_cidr_range_specifications is not None:
        import capo_ec2.types.flex_cost_allocation_cidr_range_specifications

        out["cidr_range_specifications"] = (
            capo_ec2.types.flex_cost_allocation_cidr_range_specifications.deserialize_ec2_query(
                child_cidr_range_specifications
            )
        )
    return out
