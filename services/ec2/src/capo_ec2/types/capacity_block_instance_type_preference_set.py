"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockInstanceTypePreferenceSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_block_instance_type_preference

CapacityBlockInstanceTypePreferenceSet: TypeAlias = list[
    "capo_ec2.types.capacity_block_instance_type_preference.CapacityBlockInstanceTypePreference"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityBlockInstanceTypePreferenceSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.capacity_block_instance_type_preference

        capo_ec2.types.capacity_block_instance_type_preference.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> CapacityBlockInstanceTypePreferenceSet:
    import capo_ec2.types.capacity_block_instance_type_preference

    out: CapacityBlockInstanceTypePreferenceSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.capacity_block_instance_type_preference.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> CapacityBlockInstanceTypePreferenceSet:
    import capo_ec2.types.capacity_block_instance_type_preference

    out: CapacityBlockInstanceTypePreferenceSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.capacity_block_instance_type_preference.deserialize_ec2_query(
                child
            )
        )
    return out
