"""Generated from Smithy shape ``com.amazonaws.ec2#FlexCostAllocationCidrRangeSpecifications``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.flex_cost_allocation_cidr_mapping_list
    import capo_ec2.types.flex_cost_allocation_cidr_range_specifications_prefixes_type_string


class FlexCostAllocationCidrRangeSpecifications(TypedDict, closed=True):
    prefixes_type: NotRequired[
        "capo_ec2.types.flex_cost_allocation_cidr_range_specifications_prefixes_type_string.FlexCostAllocationCidrRangeSpecificationsPrefixesTypeString"
    ]
    """<p>The type of prefixes to use. This parameter is required. Valid values are <code>source-prefixes</code> and <code>destination-prefixes</code>.</p>"""
    prefixes: NotRequired[
        "capo_ec2.types.flex_cost_allocation_cidr_mapping_list.FlexCostAllocationCidrMappingList"
    ]
    """<p>The CIDR range to label mappings. You can specify from 1 to 100 mappings. This parameter is required.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FlexCostAllocationCidrRangeSpecifications,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "prefixes_type" in value:
        pairs.append((f"{key_prefix}PrefixesType", str(value["prefixes_type"])))
    if "prefixes" in value:
        import capo_ec2.types.flex_cost_allocation_cidr_mapping_list

        capo_ec2.types.flex_cost_allocation_cidr_mapping_list.serialize_ec2_query(
            value["prefixes"], pairs, f"{key_prefix}Prefixes"
        )


def deserialize_ec2_query(el: Element) -> FlexCostAllocationCidrRangeSpecifications:
    out: FlexCostAllocationCidrRangeSpecifications = {}  # type: ignore[typeddict-item]
    child_prefixes_type = el.find("PrefixesType")
    if child_prefixes_type is not None:
        out["prefixes_type"] = str(child_prefixes_type.text or "")
    child_prefixes = el.find("Prefixes")
    if child_prefixes is not None:
        import capo_ec2.types.flex_cost_allocation_cidr_mapping_list

        out["prefixes"] = (
            capo_ec2.types.flex_cost_allocation_cidr_mapping_list.deserialize_ec2_query(
                child_prefixes
            )
        )
    return out
