"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationOptimizedWaypoint``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.cluster_index
    import capo_geo_routes.types.position
    import capo_geo_routes.types.timestamp_with_timezone_offset
    import capo_geo_routes.types.waypoint_id


class WaypointOptimizationOptimizedWaypoint(TypedDict, closed=True):
    arrival_time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>Estimated time of arrival at the destination.</p> <p>Time format:<code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>"""
    cluster_index: NotRequired["capo_geo_routes.types.cluster_index.ClusterIndex"]
    """<p>Index of the cluster the waypoint is associated with. The index is included in the response only if clustering was performed while processing the request.</p>"""
    departure_time: "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    """<p>Estimated time of departure from the origin.</p> <p>Time format:<code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>"""
    id: "capo_geo_routes.types.waypoint_id.WaypointId"
    """<p>The waypoint Id.</p>"""
    position: "capo_geo_routes.types.position.Position"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationOptimizedWaypoint) -> dict:
    out: dict = {}
    if "arrival_time" in value:
        out["ArrivalTime"] = value["arrival_time"]
    if "cluster_index" in value:
        out["ClusterIndex"] = value["cluster_index"]
    out["DepartureTime"] = value["departure_time"]
    out["Id"] = value["id"]
    import capo_geo_routes.types.position

    out["Position"] = capo_geo_routes.types.position.serialize_json(value["position"])
    return out


def deserialize_json(data: dict) -> WaypointOptimizationOptimizedWaypoint:
    out: WaypointOptimizationOptimizedWaypoint = {}  # type: ignore[typeddict-item]
    if data.get("ArrivalTime") is not None:
        out["arrival_time"] = data["ArrivalTime"]
    if data.get("ClusterIndex") is not None:
        out["cluster_index"] = data["ClusterIndex"]
    if data.get("DepartureTime") is not None:
        out["departure_time"] = data["DepartureTime"]
    else:
        out["departure_time"] = ""
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


def redact_sensitive(value: WaypointOptimizationOptimizedWaypoint) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "arrival_time" in value:
        out["arrival_time"] = "*** Sensitive Data Redacted ***"
    if "departure_time" in value:
        out["departure_time"] = "*** Sensitive Data Redacted ***"
    if "position" in value:
        out["position"] = "*** Sensitive Data Redacted ***"
    return out
