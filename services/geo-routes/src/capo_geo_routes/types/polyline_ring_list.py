"""Generated from Smithy shape ``com.amazonaws.georoutes#PolylineRingList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.polyline_ring

PolylineRingList: TypeAlias = list["capo_geo_routes.types.polyline_ring.PolylineRing"]


# --- restJson1 ser/de ---
def serialize_json(value: PolylineRingList) -> list:
    return list(value)


def deserialize_json(data: list) -> PolylineRingList:
    return [item for item in data if item is not None]


def redact_sensitive(value: PolylineRingList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
