"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationTravelModeOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.waypoint_optimization_pedestrian_options
    import capo_geo_routes.types.waypoint_optimization_truck_options


class WaypointOptimizationTravelModeOptions(TypedDict, closed=True):
    pedestrian: NotRequired[
        "capo_geo_routes.types.waypoint_optimization_pedestrian_options.WaypointOptimizationPedestrianOptions"
    ]
    """<p>Travel mode options when the provided travel mode is <code>Pedestrian</code>.</p>"""
    truck: NotRequired[
        "capo_geo_routes.types.waypoint_optimization_truck_options.WaypointOptimizationTruckOptions"
    ]
    """<p>Travel mode options when the provided travel mode is <code>Truck</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationTravelModeOptions) -> dict:
    out: dict = {}
    if "pedestrian" in value:
        import capo_geo_routes.types.waypoint_optimization_pedestrian_options

        out["Pedestrian"] = (
            capo_geo_routes.types.waypoint_optimization_pedestrian_options.serialize_json(
                value["pedestrian"]
            )
        )
    if "truck" in value:
        import capo_geo_routes.types.waypoint_optimization_truck_options

        out["Truck"] = (
            capo_geo_routes.types.waypoint_optimization_truck_options.serialize_json(
                value["truck"]
            )
        )
    return out


def deserialize_json(data: dict) -> WaypointOptimizationTravelModeOptions:
    out: WaypointOptimizationTravelModeOptions = {}  # type: ignore[typeddict-item]
    if data.get("Pedestrian") is not None:
        import capo_geo_routes.types.waypoint_optimization_pedestrian_options

        out["pedestrian"] = (
            capo_geo_routes.types.waypoint_optimization_pedestrian_options.deserialize_json(
                data["Pedestrian"]
            )
        )
    if data.get("Truck") is not None:
        import capo_geo_routes.types.waypoint_optimization_truck_options

        out["truck"] = (
            capo_geo_routes.types.waypoint_optimization_truck_options.deserialize_json(
                data["Truck"]
            )
        )
    return out


def redact_sensitive(value: WaypointOptimizationTravelModeOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pedestrian" in value:
        import capo_geo_routes.types.waypoint_optimization_pedestrian_options

        out["pedestrian"] = (
            capo_geo_routes.types.waypoint_optimization_pedestrian_options.redact_sensitive(
                value["pedestrian"]
            )
        )
    if "truck" in value:
        import capo_geo_routes.types.waypoint_optimization_truck_options

        out["truck"] = (
            capo_geo_routes.types.waypoint_optimization_truck_options.redact_sensitive(
                value["truck"]
            )
        )
    return out
