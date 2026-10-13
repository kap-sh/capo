"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineAvoidanceAreaGeometryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.isoline_avoidance_area_geometry

IsolineAvoidanceAreaGeometryList: TypeAlias = list[
    "capo_geo_routes.types.isoline_avoidance_area_geometry.IsolineAvoidanceAreaGeometry"
]


# --- restJson1 ser/de ---
def serialize_json(value: IsolineAvoidanceAreaGeometryList) -> list:
    import capo_geo_routes.types.isoline_avoidance_area_geometry

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.isoline_avoidance_area_geometry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IsolineAvoidanceAreaGeometryList:
    import capo_geo_routes.types.isoline_avoidance_area_geometry

    out: IsolineAvoidanceAreaGeometryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.isoline_avoidance_area_geometry.deserialize_json(item)
        )
    return out


def redact_sensitive(value: IsolineAvoidanceAreaGeometryList) -> list[Any]:
    import capo_geo_routes.types.isoline_avoidance_area_geometry

    return [
        capo_geo_routes.types.isoline_avoidance_area_geometry.redact_sensitive(item)
        for item in value
    ]
