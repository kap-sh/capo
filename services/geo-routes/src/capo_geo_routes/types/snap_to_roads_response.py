"""Generated from Smithy shape ``com.amazonaws.georoutes#SnapToRoadsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.geometry_format
    import capo_geo_routes.types.road_snap_notice_list
    import capo_geo_routes.types.road_snap_snapped_geometry
    import capo_geo_routes.types.road_snap_snapped_trace_point_list


class SnapToRoadsResponse(TypedDict, closed=True):
    notices: "capo_geo_routes.types.road_snap_notice_list.RoadSnapNoticeList"
    """<p>Notices are additional information returned that indicate issues that occurred during route calculation.</p>"""
    pricing_bucket: "str"
    """<p>The pricing bucket for which the query is charged at.</p>"""
    snapped_geometry: NotRequired[
        "capo_geo_routes.types.road_snap_snapped_geometry.RoadSnapSnappedGeometry"
    ]
    """<p>The interpolated geometry for the snapped route onto the road network.</p>"""
    snapped_geometry_format: "capo_geo_routes.types.geometry_format.GeometryFormat"
    """<p>Specifies the format of the geometry returned for each leg of the route.</p>"""
    snapped_trace_points: "capo_geo_routes.types.road_snap_snapped_trace_point_list.RoadSnapSnappedTracePointList"
    """<p>The trace points snapped onto the road network. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapToRoadsResponse) -> dict:
    out: dict = {}
    import capo_geo_routes.types.road_snap_notice_list

    out["Notices"] = capo_geo_routes.types.road_snap_notice_list.serialize_json(
        value["notices"]
    )
    if "snapped_geometry" in value:
        import capo_geo_routes.types.road_snap_snapped_geometry

        out["SnappedGeometry"] = (
            capo_geo_routes.types.road_snap_snapped_geometry.serialize_json(
                value["snapped_geometry"]
            )
        )
    import capo_geo_routes.types.geometry_format

    out["SnappedGeometryFormat"] = capo_geo_routes.types.geometry_format.serialize_json(
        value["snapped_geometry_format"]
    )
    import capo_geo_routes.types.road_snap_snapped_trace_point_list

    out["SnappedTracePoints"] = (
        capo_geo_routes.types.road_snap_snapped_trace_point_list.serialize_json(
            value["snapped_trace_points"]
        )
    )
    return out


def deserialize_json(data: dict) -> SnapToRoadsResponse:
    out: SnapToRoadsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Notices") is not None:
        import capo_geo_routes.types.road_snap_notice_list

        out["notices"] = capo_geo_routes.types.road_snap_notice_list.deserialize_json(
            data["Notices"]
        )
    else:
        out["notices"] = []
    if data.get("SnappedGeometry") is not None:
        import capo_geo_routes.types.road_snap_snapped_geometry

        out["snapped_geometry"] = (
            capo_geo_routes.types.road_snap_snapped_geometry.deserialize_json(
                data["SnappedGeometry"]
            )
        )
    if data.get("SnappedGeometryFormat") is not None:
        import capo_geo_routes.types.geometry_format

        out["snapped_geometry_format"] = (
            capo_geo_routes.types.geometry_format.deserialize_json(
                data["SnappedGeometryFormat"]
            )
        )
    else:
        import typing

        out["snapped_geometry_format"] = typing.cast(
            "capo_geo_routes.types.geometry_format.GeometryFormat", ""
        )
    if data.get("SnappedTracePoints") is not None:
        import capo_geo_routes.types.road_snap_snapped_trace_point_list

        out["snapped_trace_points"] = (
            capo_geo_routes.types.road_snap_snapped_trace_point_list.deserialize_json(
                data["SnappedTracePoints"]
            )
        )
    else:
        out["snapped_trace_points"] = []
    return out


def redact_sensitive(value: SnapToRoadsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "notices" in value:
        import capo_geo_routes.types.road_snap_notice_list

        out["notices"] = capo_geo_routes.types.road_snap_notice_list.redact_sensitive(
            value["notices"]
        )
    if "snapped_geometry" in value:
        import capo_geo_routes.types.road_snap_snapped_geometry

        out["snapped_geometry"] = (
            capo_geo_routes.types.road_snap_snapped_geometry.redact_sensitive(
                value["snapped_geometry"]
            )
        )
    if "snapped_trace_points" in value:
        import capo_geo_routes.types.road_snap_snapped_trace_point_list

        out["snapped_trace_points"] = (
            capo_geo_routes.types.road_snap_snapped_trace_point_list.redact_sensitive(
                value["snapped_trace_points"]
            )
        )
    return out
