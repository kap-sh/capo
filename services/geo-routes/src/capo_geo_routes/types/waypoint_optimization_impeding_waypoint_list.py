"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationImpedingWaypointList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.waypoint_optimization_impeding_waypoint

WaypointOptimizationImpedingWaypointList: TypeAlias = list[
    "capo_geo_routes.types.waypoint_optimization_impeding_waypoint.WaypointOptimizationImpedingWaypoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationImpedingWaypointList) -> list:
    import capo_geo_routes.types.waypoint_optimization_impeding_waypoint

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.waypoint_optimization_impeding_waypoint.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WaypointOptimizationImpedingWaypointList:
    import capo_geo_routes.types.waypoint_optimization_impeding_waypoint

    out: WaypointOptimizationImpedingWaypointList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.waypoint_optimization_impeding_waypoint.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: WaypointOptimizationImpedingWaypointList) -> list[Any]:
    import capo_geo_routes.types.waypoint_optimization_impeding_waypoint

    return [
        capo_geo_routes.types.waypoint_optimization_impeding_waypoint.redact_sensitive(
            item
        )
        for item in value
    ]
