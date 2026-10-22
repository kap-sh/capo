"""Generated from Smithy shape ``com.amazonaws.rds#AvailableCapacityPerAvailabilityZoneList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.available_capacity_per_availability_zone

AvailableCapacityPerAvailabilityZoneList: TypeAlias = list[
    "capo_rds.types.available_capacity_per_availability_zone.AvailableCapacityPerAvailabilityZone"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailableCapacityPerAvailabilityZoneList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_rds.types.available_capacity_per_availability_zone

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.available_capacity_per_availability_zone.serialize_query(
            item, pairs, f"{prefix}.AvailableCapacityPerAvailabilityZone.{n}"
        )


def deserialize_query(el: Element) -> AvailableCapacityPerAvailabilityZoneList:
    import capo_rds.types.available_capacity_per_availability_zone

    out: AvailableCapacityPerAvailabilityZoneList = []
    for child in el.findall("AvailableCapacityPerAvailabilityZone"):
        out.append(
            capo_rds.types.available_capacity_per_availability_zone.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: AvailableCapacityPerAvailabilityZoneList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_rds.types.available_capacity_per_availability_zone

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.available_capacity_per_availability_zone.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> AvailableCapacityPerAvailabilityZoneList:
    import capo_rds.types.available_capacity_per_availability_zone

    out: AvailableCapacityPerAvailabilityZoneList = []
    for child in parent.findall(tag):
        out.append(
            capo_rds.types.available_capacity_per_availability_zone.deserialize_query(
                child
            )
        )
    return out
