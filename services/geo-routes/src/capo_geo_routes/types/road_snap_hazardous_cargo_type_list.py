"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapHazardousCargoTypeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.road_snap_hazardous_cargo_type

RoadSnapHazardousCargoTypeList: TypeAlias = list[
    "capo_geo_routes.types.road_snap_hazardous_cargo_type.RoadSnapHazardousCargoType"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapHazardousCargoTypeList) -> list:
    import capo_geo_routes.types.road_snap_hazardous_cargo_type

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.road_snap_hazardous_cargo_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RoadSnapHazardousCargoTypeList:
    import capo_geo_routes.types.road_snap_hazardous_cargo_type

    out: RoadSnapHazardousCargoTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.road_snap_hazardous_cargo_type.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RoadSnapHazardousCargoTypeList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
