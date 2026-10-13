"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAvoidanceAreaList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_avoidance_area

RouteAvoidanceAreaList: TypeAlias = list[
    "capo_geo_routes.types.route_avoidance_area.RouteAvoidanceArea"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteAvoidanceAreaList) -> list:
    import capo_geo_routes.types.route_avoidance_area

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_avoidance_area.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteAvoidanceAreaList:
    import capo_geo_routes.types.route_avoidance_area

    out: RouteAvoidanceAreaList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_avoidance_area.deserialize_json(item))
    return out


def redact_sensitive(value: RouteAvoidanceAreaList) -> list[Any]:
    import capo_geo_routes.types.route_avoidance_area

    return [
        capo_geo_routes.types.route_avoidance_area.redact_sensitive(item)
        for item in value
    ]
