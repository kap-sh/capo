"""Generated from Smithy shape ``com.amazonaws.deadline#FleetSoftwareAddOns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.fleet_software_add_on

FleetSoftwareAddOns: TypeAlias = list[
    "capo_deadline.types.fleet_software_add_on.FleetSoftwareAddOn"
]


# --- restJson1 ser/de ---
def serialize_json(value: FleetSoftwareAddOns) -> list:
    import capo_deadline.types.fleet_software_add_on

    out: list = []
    for item in value:
        out.append(capo_deadline.types.fleet_software_add_on.serialize_json(item))
    return out


def deserialize_json(data: list) -> FleetSoftwareAddOns:
    import capo_deadline.types.fleet_software_add_on

    out: FleetSoftwareAddOns = []
    for item in data:
        if item is None:
            continue
        out.append(capo_deadline.types.fleet_software_add_on.deserialize_json(item))
    return out
