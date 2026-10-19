"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationClusteringOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.waypoint_optimization_clustering_algorithm
    import capo_geo_routes.types.waypoint_optimization_driving_distance_options


class WaypointOptimizationClusteringOptions(TypedDict, closed=True):
    algorithm: "capo_geo_routes.types.waypoint_optimization_clustering_algorithm.WaypointOptimizationClusteringAlgorithm"
    """<p>The algorithm to be used. <code>DrivingDistance</code> assigns all the waypoints that are within driving distance of each other into a single cluster. <code>TopologySegment</code> assigns all the waypoints that are within the same topology segment into a single cluster. A Topology segment is a linear stretch of road between two junctions.</p>"""
    driving_distance_options: NotRequired[
        "capo_geo_routes.types.waypoint_optimization_driving_distance_options.WaypointOptimizationDrivingDistanceOptions"
    ]
    """<p>Driving distance options to be used when the clustering algorithm is DrivingDistance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationClusteringOptions) -> dict:
    out: dict = {}
    import capo_geo_routes.types.waypoint_optimization_clustering_algorithm

    out["Algorithm"] = (
        capo_geo_routes.types.waypoint_optimization_clustering_algorithm.serialize_json(
            value["algorithm"]
        )
    )
    if "driving_distance_options" in value:
        import capo_geo_routes.types.waypoint_optimization_driving_distance_options

        out["DrivingDistanceOptions"] = (
            capo_geo_routes.types.waypoint_optimization_driving_distance_options.serialize_json(
                value["driving_distance_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> WaypointOptimizationClusteringOptions:
    out: WaypointOptimizationClusteringOptions = {}  # type: ignore[typeddict-item]
    if data.get("Algorithm") is not None:
        import capo_geo_routes.types.waypoint_optimization_clustering_algorithm

        out["algorithm"] = (
            capo_geo_routes.types.waypoint_optimization_clustering_algorithm.deserialize_json(
                data["Algorithm"]
            )
        )
    else:
        import typing

        out["algorithm"] = typing.cast(
            "capo_geo_routes.types.waypoint_optimization_clustering_algorithm.WaypointOptimizationClusteringAlgorithm",
            "",
        )
    if data.get("DrivingDistanceOptions") is not None:
        import capo_geo_routes.types.waypoint_optimization_driving_distance_options

        out["driving_distance_options"] = (
            capo_geo_routes.types.waypoint_optimization_driving_distance_options.deserialize_json(
                data["DrivingDistanceOptions"]
            )
        )
    return out


def redact_sensitive(value: WaypointOptimizationClusteringOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "algorithm" in value:
        out["algorithm"] = "*** Sensitive Data Redacted ***"
    return out
