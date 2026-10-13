"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationFailedConstraintList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.waypoint_optimization_failed_constraint

WaypointOptimizationFailedConstraintList: TypeAlias = list[
    "capo_geo_routes.types.waypoint_optimization_failed_constraint.WaypointOptimizationFailedConstraint"
]


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationFailedConstraintList) -> list:
    import capo_geo_routes.types.waypoint_optimization_failed_constraint

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.waypoint_optimization_failed_constraint.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WaypointOptimizationFailedConstraintList:
    import capo_geo_routes.types.waypoint_optimization_failed_constraint

    out: WaypointOptimizationFailedConstraintList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.waypoint_optimization_failed_constraint.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: WaypointOptimizationFailedConstraintList) -> list[Any]:
    import capo_geo_routes.types.waypoint_optimization_failed_constraint

    return [
        capo_geo_routes.types.waypoint_optimization_failed_constraint.redact_sensitive(
            item
        )
        for item in value
    ]
