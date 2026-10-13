"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#RegionStatusList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.region_status

RegionStatusList: TypeAlias = list[
    "capo_resource_explorer_2.types.region_status.RegionStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegionStatusList) -> list:
    import capo_resource_explorer_2.types.region_status

    out: list = []
    for item in value:
        out.append(capo_resource_explorer_2.types.region_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> RegionStatusList:
    import capo_resource_explorer_2.types.region_status

    out: RegionStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_resource_explorer_2.types.region_status.deserialize_json(item))
    return out


def redact_sensitive(value: RegionStatusList) -> list[Any]:
    import capo_resource_explorer_2.types.region_status

    return [
        capo_resource_explorer_2.types.region_status.redact_sensitive(item)
        for item in value
    ]
