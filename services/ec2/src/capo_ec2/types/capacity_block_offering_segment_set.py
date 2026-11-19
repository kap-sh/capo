"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockOfferingSegmentSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_block_offering_segment

CapacityBlockOfferingSegmentSet: TypeAlias = list[
    "capo_ec2.types.capacity_block_offering_segment.CapacityBlockOfferingSegment"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityBlockOfferingSegmentSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.capacity_block_offering_segment

        capo_ec2.types.capacity_block_offering_segment.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> CapacityBlockOfferingSegmentSet:
    import capo_ec2.types.capacity_block_offering_segment

    out: CapacityBlockOfferingSegmentSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.capacity_block_offering_segment.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> CapacityBlockOfferingSegmentSet:
    import capo_ec2.types.capacity_block_offering_segment

    out: CapacityBlockOfferingSegmentSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.capacity_block_offering_segment.deserialize_ec2_query(child)
        )
    return out
