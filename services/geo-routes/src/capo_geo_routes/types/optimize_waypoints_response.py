"""Generated from Smithy shape ``com.amazonaws.georoutes#OptimizeWaypointsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.waypoint_optimization_connection_list
    import capo_geo_routes.types.waypoint_optimization_impeding_waypoint_list
    import capo_geo_routes.types.waypoint_optimization_optimized_waypoint_list
    import capo_geo_routes.types.waypoint_optimization_time_breakdown


class OptimizeWaypointsResponse(TypedDict, closed=True):
    connections: "capo_geo_routes.types.waypoint_optimization_connection_list.WaypointOptimizationConnectionList"
    """<p>Details about the connection from one waypoint to the next, within the optimized sequence.</p>"""
    distance: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Overall distance to travel the whole sequence.</p>"""
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Overall duration to travel the whole sequence.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    impeding_waypoints: "capo_geo_routes.types.waypoint_optimization_impeding_waypoint_list.WaypointOptimizationImpedingWaypointList"
    """<p>Returns waypoints that caused the optimization problem to fail, and the constraints that were unsatisfied leading to the failure.</p>"""
    optimized_waypoints: "capo_geo_routes.types.waypoint_optimization_optimized_waypoint_list.WaypointOptimizationOptimizedWaypointList"
    """<p>Waypoints in the order of the optimized sequence.</p>"""
    pricing_bucket: "str"
    """<p>The pricing bucket for which the query is charged at.</p>"""
    time_breakdown: "capo_geo_routes.types.waypoint_optimization_time_breakdown.WaypointOptimizationTimeBreakdown"
    """<p>Time breakdown for the sequence.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OptimizeWaypointsResponse) -> dict:
    out: dict = {}
    import capo_geo_routes.types.waypoint_optimization_connection_list

    out["Connections"] = (
        capo_geo_routes.types.waypoint_optimization_connection_list.serialize_json(
            value["connections"]
        )
    )
    out["Distance"] = value.get("distance", 0)
    out["Duration"] = value.get("duration", 0)
    import capo_geo_routes.types.waypoint_optimization_impeding_waypoint_list

    out["ImpedingWaypoints"] = (
        capo_geo_routes.types.waypoint_optimization_impeding_waypoint_list.serialize_json(
            value["impeding_waypoints"]
        )
    )
    import capo_geo_routes.types.waypoint_optimization_optimized_waypoint_list

    out["OptimizedWaypoints"] = (
        capo_geo_routes.types.waypoint_optimization_optimized_waypoint_list.serialize_json(
            value["optimized_waypoints"]
        )
    )
    import capo_geo_routes.types.waypoint_optimization_time_breakdown

    out["TimeBreakdown"] = (
        capo_geo_routes.types.waypoint_optimization_time_breakdown.serialize_json(
            value["time_breakdown"]
        )
    )
    return out


def deserialize_json(data: dict) -> OptimizeWaypointsResponse:
    out: OptimizeWaypointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Connections") is not None:
        import capo_geo_routes.types.waypoint_optimization_connection_list

        out["connections"] = (
            capo_geo_routes.types.waypoint_optimization_connection_list.deserialize_json(
                data["Connections"]
            )
        )
    else:
        out["connections"] = []
    if data.get("Distance") is not None:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if data.get("ImpedingWaypoints") is not None:
        import capo_geo_routes.types.waypoint_optimization_impeding_waypoint_list

        out["impeding_waypoints"] = (
            capo_geo_routes.types.waypoint_optimization_impeding_waypoint_list.deserialize_json(
                data["ImpedingWaypoints"]
            )
        )
    else:
        out["impeding_waypoints"] = []
    if data.get("OptimizedWaypoints") is not None:
        import capo_geo_routes.types.waypoint_optimization_optimized_waypoint_list

        out["optimized_waypoints"] = (
            capo_geo_routes.types.waypoint_optimization_optimized_waypoint_list.deserialize_json(
                data["OptimizedWaypoints"]
            )
        )
    else:
        out["optimized_waypoints"] = []
    if data.get("TimeBreakdown") is not None:
        import capo_geo_routes.types.waypoint_optimization_time_breakdown

        out["time_breakdown"] = (
            capo_geo_routes.types.waypoint_optimization_time_breakdown.deserialize_json(
                data["TimeBreakdown"]
            )
        )
    else:
        raise DeserializationError("OptimizeWaypointsResponse.time_breakdown required")
    return out


def redact_sensitive(value: OptimizeWaypointsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connections" in value:
        import capo_geo_routes.types.waypoint_optimization_connection_list

        out["connections"] = (
            capo_geo_routes.types.waypoint_optimization_connection_list.redact_sensitive(
                value["connections"]
            )
        )
    if "distance" in value:
        out["distance"] = "*** Sensitive Data Redacted ***"
    if "duration" in value:
        out["duration"] = "*** Sensitive Data Redacted ***"
    if "impeding_waypoints" in value:
        import capo_geo_routes.types.waypoint_optimization_impeding_waypoint_list

        out["impeding_waypoints"] = (
            capo_geo_routes.types.waypoint_optimization_impeding_waypoint_list.redact_sensitive(
                value["impeding_waypoints"]
            )
        )
    if "optimized_waypoints" in value:
        import capo_geo_routes.types.waypoint_optimization_optimized_waypoint_list

        out["optimized_waypoints"] = (
            capo_geo_routes.types.waypoint_optimization_optimized_waypoint_list.redact_sensitive(
                value["optimized_waypoints"]
            )
        )
    if "time_breakdown" in value:
        import capo_geo_routes.types.waypoint_optimization_time_breakdown

        out["time_breakdown"] = (
            capo_geo_routes.types.waypoint_optimization_time_breakdown.redact_sensitive(
                value["time_breakdown"]
            )
        )
    return out
