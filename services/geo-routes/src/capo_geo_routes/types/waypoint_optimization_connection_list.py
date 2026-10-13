"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationConnectionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.waypoint_optimization_connection

WaypointOptimizationConnectionList: TypeAlias = list[
    "capo_geo_routes.types.waypoint_optimization_connection.WaypointOptimizationConnection"
]


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationConnectionList) -> list:
    import capo_geo_routes.types.waypoint_optimization_connection

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.waypoint_optimization_connection.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WaypointOptimizationConnectionList:
    import capo_geo_routes.types.waypoint_optimization_connection

    out: WaypointOptimizationConnectionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.waypoint_optimization_connection.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: WaypointOptimizationConnectionList) -> list[Any]:
    import capo_geo_routes.types.waypoint_optimization_connection

    return [
        capo_geo_routes.types.waypoint_optimization_connection.redact_sensitive(item)
        for item in value
    ]
