"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAvoidanceAreaGeometryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_avoidance_area_geometry

RouteAvoidanceAreaGeometryList: TypeAlias = list[
    "capo_geo_routes.types.route_avoidance_area_geometry.RouteAvoidanceAreaGeometry"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteAvoidanceAreaGeometryList) -> list:
    import capo_geo_routes.types.route_avoidance_area_geometry

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_avoidance_area_geometry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteAvoidanceAreaGeometryList:
    import capo_geo_routes.types.route_avoidance_area_geometry

    out: RouteAvoidanceAreaGeometryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_avoidance_area_geometry.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RouteAvoidanceAreaGeometryList) -> list[Any]:
    import capo_geo_routes.types.route_avoidance_area_geometry

    return [
        capo_geo_routes.types.route_avoidance_area_geometry.redact_sensitive(item)
        for item in value
    ]
