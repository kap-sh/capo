"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePassThroughWaypointList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_pass_through_waypoint

RoutePassThroughWaypointList: TypeAlias = list[
    "capo_geo_routes.types.route_pass_through_waypoint.RoutePassThroughWaypoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutePassThroughWaypointList) -> list:
    import capo_geo_routes.types.route_pass_through_waypoint

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_pass_through_waypoint.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RoutePassThroughWaypointList:
    import capo_geo_routes.types.route_pass_through_waypoint

    out: RoutePassThroughWaypointList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_pass_through_waypoint.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RoutePassThroughWaypointList) -> list[Any]:
    import capo_geo_routes.types.route_pass_through_waypoint

    return [
        capo_geo_routes.types.route_pass_through_waypoint.redact_sensitive(item)
        for item in value
    ]
