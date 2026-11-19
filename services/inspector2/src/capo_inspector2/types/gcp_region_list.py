"""Generated from Smithy shape ``com.amazonaws.inspector2#GcpRegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.gcp_region

GcpRegionList: TypeAlias = list["capo_inspector2.types.gcp_region.GcpRegion"]


# --- restJson1 ser/de ---
def serialize_json(value: GcpRegionList) -> list:
    return list(value)


def deserialize_json(data: list) -> GcpRegionList:
    return [item for item in data if item is not None]
