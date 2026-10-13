"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationAvoidanceArea``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.waypoint_optimization_avoidance_area_geometry


class WaypointOptimizationAvoidanceArea(TypedDict, closed=True):
    geometry: "capo_geo_routes.types.waypoint_optimization_avoidance_area_geometry.WaypointOptimizationAvoidanceAreaGeometry"
    """<p>Geometry of the area to be avoided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationAvoidanceArea) -> dict:
    out: dict = {}
    import capo_geo_routes.types.waypoint_optimization_avoidance_area_geometry

    out["Geometry"] = (
        capo_geo_routes.types.waypoint_optimization_avoidance_area_geometry.serialize_json(
            value["geometry"]
        )
    )
    return out


def deserialize_json(data: dict) -> WaypointOptimizationAvoidanceArea:
    out: WaypointOptimizationAvoidanceArea = {}  # type: ignore[typeddict-item]
    if data.get("Geometry") is not None:
        import capo_geo_routes.types.waypoint_optimization_avoidance_area_geometry

        out["geometry"] = (
            capo_geo_routes.types.waypoint_optimization_avoidance_area_geometry.deserialize_json(
                data["Geometry"]
            )
        )
    else:
        raise DeserializationError(
            "WaypointOptimizationAvoidanceArea.geometry required"
        )
    return out


def redact_sensitive(value: WaypointOptimizationAvoidanceArea) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "geometry" in value:
        import capo_geo_routes.types.waypoint_optimization_avoidance_area_geometry

        out["geometry"] = (
            capo_geo_routes.types.waypoint_optimization_avoidance_area_geometry.redact_sensitive(
                value["geometry"]
            )
        )
    return out
