"""Generated from Smithy shape ``com.amazonaws.georoutes#SnapToRoadsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.api_key
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.geometry_format
    import capo_geo_routes.types.road_snap_trace_point_list
    import capo_geo_routes.types.road_snap_travel_mode
    import capo_geo_routes.types.road_snap_travel_mode_options


class SnapToRoadsRequest(TypedDict, closed=True):
    key: NotRequired["capo_geo_routes.types.api_key.ApiKey"]
    """<p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request. </p>"""
    snapped_geometry_format: NotRequired[
        "capo_geo_routes.types.geometry_format.GeometryFormat"
    ]
    """<p>Chooses what the returned SnappedGeometry format should be.</p> <p>Default value: <code>FlexiblePolyline</code> </p>"""
    snap_radius: NotRequired["capo_geo_routes.types.distance_meters.DistanceMeters"]
    """<p>The radius around the provided tracepoint that is considered for snapping.</p> <p> <b>Unit</b>: <code>meters</code> </p> <p>Default value: <code>300</code> </p>"""
    trace_points: (
        "capo_geo_routes.types.road_snap_trace_point_list.RoadSnapTracePointList"
    )
    """<p>List of trace points to be snapped onto the road network.</p>"""
    travel_mode: NotRequired[
        "capo_geo_routes.types.road_snap_travel_mode.RoadSnapTravelMode"
    ]
    """<p>Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility.</p> <p>Default value: <code>Car</code> </p>"""
    travel_mode_options: NotRequired[
        "capo_geo_routes.types.road_snap_travel_mode_options.RoadSnapTravelModeOptions"
    ]
    """<p>Travel mode related options for the provided travel mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapToRoadsRequest) -> dict:
    out: dict = {}
    if "snapped_geometry_format" in value:
        import capo_geo_routes.types.geometry_format

        out["SnappedGeometryFormat"] = (
            capo_geo_routes.types.geometry_format.serialize_json(
                value["snapped_geometry_format"]
            )
        )
    if "snap_radius" in value:
        out["SnapRadius"] = value["snap_radius"]
    import capo_geo_routes.types.road_snap_trace_point_list

    out["TracePoints"] = (
        capo_geo_routes.types.road_snap_trace_point_list.serialize_json(
            value["trace_points"]
        )
    )
    if "travel_mode" in value:
        import capo_geo_routes.types.road_snap_travel_mode

        out["TravelMode"] = capo_geo_routes.types.road_snap_travel_mode.serialize_json(
            value["travel_mode"]
        )
    if "travel_mode_options" in value:
        import capo_geo_routes.types.road_snap_travel_mode_options

        out["TravelModeOptions"] = (
            capo_geo_routes.types.road_snap_travel_mode_options.serialize_json(
                value["travel_mode_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnapToRoadsRequest:
    out: SnapToRoadsRequest = {}  # type: ignore[typeddict-item]
    if data.get("SnappedGeometryFormat") is not None:
        import capo_geo_routes.types.geometry_format

        out["snapped_geometry_format"] = (
            capo_geo_routes.types.geometry_format.deserialize_json(
                data["SnappedGeometryFormat"]
            )
        )
    if data.get("SnapRadius") is not None:
        out["snap_radius"] = data["SnapRadius"]
    if data.get("TracePoints") is not None:
        import capo_geo_routes.types.road_snap_trace_point_list

        out["trace_points"] = (
            capo_geo_routes.types.road_snap_trace_point_list.deserialize_json(
                data["TracePoints"]
            )
        )
    else:
        raise DeserializationError("SnapToRoadsRequest.trace_points required")
    if data.get("TravelMode") is not None:
        import capo_geo_routes.types.road_snap_travel_mode

        out["travel_mode"] = (
            capo_geo_routes.types.road_snap_travel_mode.deserialize_json(
                data["TravelMode"]
            )
        )
    if data.get("TravelModeOptions") is not None:
        import capo_geo_routes.types.road_snap_travel_mode_options

        out["travel_mode_options"] = (
            capo_geo_routes.types.road_snap_travel_mode_options.deserialize_json(
                data["TravelModeOptions"]
            )
        )
    return out


def redact_sensitive(value: SnapToRoadsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "key" in value:
        out["key"] = "*** Sensitive Data Redacted ***"
    if "snap_radius" in value:
        out["snap_radius"] = "*** Sensitive Data Redacted ***"
    if "trace_points" in value:
        import capo_geo_routes.types.road_snap_trace_point_list

        out["trace_points"] = (
            capo_geo_routes.types.road_snap_trace_point_list.redact_sensitive(
                value["trace_points"]
            )
        )
    if "travel_mode_options" in value:
        import capo_geo_routes.types.road_snap_travel_mode_options

        out["travel_mode_options"] = (
            capo_geo_routes.types.road_snap_travel_mode_options.redact_sensitive(
                value["travel_mode_options"]
            )
        )
    return out
