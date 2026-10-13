"""Generated from Smithy shape ``com.amazonaws.georoutes#TruckRoadTypeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.truck_road_type

TruckRoadTypeList: TypeAlias = list[
    "capo_geo_routes.types.truck_road_type.TruckRoadType"
]


# --- restJson1 ser/de ---
def serialize_json(value: TruckRoadTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> TruckRoadTypeList:
    return [item for item in data if item is not None]


def redact_sensitive(value: TruckRoadTypeList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
