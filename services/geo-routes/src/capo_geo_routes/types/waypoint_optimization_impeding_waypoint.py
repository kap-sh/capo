"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationImpedingWaypoint``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.position
    import capo_geo_routes.types.waypoint_id
    import capo_geo_routes.types.waypoint_optimization_failed_constraint_list


class WaypointOptimizationImpedingWaypoint(TypedDict, closed=True):
    failed_constraints: "capo_geo_routes.types.waypoint_optimization_failed_constraint_list.WaypointOptimizationFailedConstraintList"
    """<p>Failed constraints for an impeding waypoint.</p>"""
    id: "capo_geo_routes.types.waypoint_id.WaypointId"
    """<p>The waypoint Id.</p>"""
    position: "capo_geo_routes.types.position.Position"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationImpedingWaypoint) -> dict:
    out: dict = {}
    import capo_geo_routes.types.waypoint_optimization_failed_constraint_list

    out["FailedConstraints"] = (
        capo_geo_routes.types.waypoint_optimization_failed_constraint_list.serialize_json(
            value["failed_constraints"]
        )
    )
    out["Id"] = value["id"]
    import capo_geo_routes.types.position

    out["Position"] = capo_geo_routes.types.position.serialize_json(value["position"])
    return out


def deserialize_json(data: dict) -> WaypointOptimizationImpedingWaypoint:
    out: WaypointOptimizationImpedingWaypoint = {}  # type: ignore[typeddict-item]
    if data.get("FailedConstraints") is not None:
        import capo_geo_routes.types.waypoint_optimization_failed_constraint_list

        out["failed_constraints"] = (
            capo_geo_routes.types.waypoint_optimization_failed_constraint_list.deserialize_json(
                data["FailedConstraints"]
            )
        )
    else:
        out["failed_constraints"] = []
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Position") is not None:
        import capo_geo_routes.types.position

        out["position"] = capo_geo_routes.types.position.deserialize_json(
            data["Position"]
        )
    else:
        out["position"] = []
    return out


def redact_sensitive(value: WaypointOptimizationImpedingWaypoint) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "failed_constraints" in value:
        import capo_geo_routes.types.waypoint_optimization_failed_constraint_list

        out["failed_constraints"] = (
            capo_geo_routes.types.waypoint_optimization_failed_constraint_list.redact_sensitive(
                value["failed_constraints"]
            )
        )
    if "position" in value:
        out["position"] = "*** Sensitive Data Redacted ***"
    return out
