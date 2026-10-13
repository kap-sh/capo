"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteWaypointList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_waypoint

RouteWaypointList: TypeAlias = list[
    "capo_geo_routes.types.route_waypoint.RouteWaypoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteWaypointList) -> list:
    import capo_geo_routes.types.route_waypoint

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_waypoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteWaypointList:
    import capo_geo_routes.types.route_waypoint

    out: RouteWaypointList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_waypoint.deserialize_json(item))
    return out


def redact_sensitive(value: RouteWaypointList) -> list[Any]:
    import capo_geo_routes.types.route_waypoint

    return [
        capo_geo_routes.types.route_waypoint.redact_sensitive(item) for item in value
    ]
