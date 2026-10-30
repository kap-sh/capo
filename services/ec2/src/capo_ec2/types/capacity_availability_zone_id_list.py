"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityAvailabilityZoneIdList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string

CapacityAvailabilityZoneIdList: TypeAlias = list["capo_ec2.types.string.String"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityAvailabilityZoneIdList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(el: Element) -> CapacityAvailabilityZoneIdList:
    out: CapacityAvailabilityZoneIdList = []
    for child in el.findall("item"):
        out.append(str(child.text or ""))
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> CapacityAvailabilityZoneIdList:
    out: CapacityAvailabilityZoneIdList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
