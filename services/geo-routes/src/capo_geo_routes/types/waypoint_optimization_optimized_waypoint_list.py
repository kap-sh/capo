"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationOptimizedWaypointList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.waypoint_optimization_optimized_waypoint

WaypointOptimizationOptimizedWaypointList: TypeAlias = list[
    "capo_geo_routes.types.waypoint_optimization_optimized_waypoint.WaypointOptimizationOptimizedWaypoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationOptimizedWaypointList) -> list:
    import capo_geo_routes.types.waypoint_optimization_optimized_waypoint

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.waypoint_optimization_optimized_waypoint.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WaypointOptimizationOptimizedWaypointList:
    import capo_geo_routes.types.waypoint_optimization_optimized_waypoint

    out: WaypointOptimizationOptimizedWaypointList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.waypoint_optimization_optimized_waypoint.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: WaypointOptimizationOptimizedWaypointList) -> list[Any]:
    import capo_geo_routes.types.waypoint_optimization_optimized_waypoint

    return [
        capo_geo_routes.types.waypoint_optimization_optimized_waypoint.redact_sensitive(
            item
        )
        for item in value
    ]
