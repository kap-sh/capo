"""Generated from Smithy shape ``com.amazonaws.ec2#FlexCostAllocationCidrMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.flex_cost_allocation_cidr_label
    import capo_ec2.types.flex_cost_allocation_cidr_mapping_cidr_range_string


class FlexCostAllocationCidrMapping(TypedDict, closed=True):
    cidr_range: NotRequired[
        "capo_ec2.types.flex_cost_allocation_cidr_mapping_cidr_range_string.FlexCostAllocationCidrMappingCidrRangeString"
    ]
    """<p>The CIDR range. This parameter is required.</p>"""
    cidr_label: NotRequired[
        "capo_ec2.types.flex_cost_allocation_cidr_label.FlexCostAllocationCidrLabel"
    ]
    """<p>The label to assign to the CIDR range. The label can be up to 64 characters long. It can contain letters, numbers, hyphens (<code>-</code>), and underscores (<code>_</code>), and must start with a letter or a number. This parameter is required.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FlexCostAllocationCidrMapping, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cidr_range" in value:
        pairs.append((f"{key_prefix}CidrRange", str(value["cidr_range"])))
    if "cidr_label" in value:
        pairs.append((f"{key_prefix}CidrLabel", str(value["cidr_label"])))


def deserialize_ec2_query(el: Element) -> FlexCostAllocationCidrMapping:
    out: FlexCostAllocationCidrMapping = {}  # type: ignore[typeddict-item]
    child_cidr_range = el.find("CidrRange")
    if child_cidr_range is not None:
        out["cidr_range"] = str(child_cidr_range.text or "")
    child_cidr_label = el.find("CidrLabel")
    if child_cidr_label is not None:
        out["cidr_label"] = str(child_cidr_label.text or "")
    return out
