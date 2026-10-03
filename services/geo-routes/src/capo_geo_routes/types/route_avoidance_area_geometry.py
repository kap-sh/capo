"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAvoidanceAreaGeometry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.bounding_box
    import capo_geo_routes.types.corridor
    import capo_geo_routes.types.linear_rings
    import capo_geo_routes.types.polyline_corridor
    import capo_geo_routes.types.polyline_ring_list


class RouteAvoidanceAreaGeometry(TypedDict, closed=True):
    corridor: NotRequired["capo_geo_routes.types.corridor.Corridor"]
    """<p>Geometry defined as a corridor - a LineString with a radius that defines the width of the corridor.</p>"""
    bounding_box: NotRequired["capo_geo_routes.types.bounding_box.BoundingBox"]
    """<p>Geometry defined as a bounding box. The first pair represents the X and Y coordinates (longitude and latitude,) of the southwest corner of the bounding box; the second pair represents the X and Y coordinates (longitude and latitude) of the northeast corner.</p>"""
    polygon: NotRequired["capo_geo_routes.types.linear_rings.LinearRings"]
    """<p>Geometry defined as a polygon with only one linear ring.</p>"""
    polyline_corridor: NotRequired[
        "capo_geo_routes.types.polyline_corridor.PolylineCorridor"
    ]
    """<p>Geometry defined as an encoded corridor - an encoded polyline with a radius that defines the width of the corridor.</p>"""
    polyline_polygon: NotRequired[
        "capo_geo_routes.types.polyline_ring_list.PolylineRingList"
    ]
    """<p>A list of Isoline PolylinePolygon, for each isoline PolylinePolygon, it contains PolylinePolygon of the first linear ring (the outer ring) and from 2nd item to the last item (the inner rings). For more information on polyline encoding, see <a href="https://github.com/aws-geospatial/polyline">https://github.com/aws-geospatial/polyline</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteAvoidanceAreaGeometry) -> dict:
    out: dict = {}
    if "corridor" in value:
        import capo_geo_routes.types.corridor

        out["Corridor"] = capo_geo_routes.types.corridor.serialize_json(
            value["corridor"]
        )
    if "bounding_box" in value:
        import capo_geo_routes.types.bounding_box

        out["BoundingBox"] = capo_geo_routes.types.bounding_box.serialize_json(
            value["bounding_box"]
        )
    if "polygon" in value:
        import capo_geo_routes.types.linear_rings

        out["Polygon"] = capo_geo_routes.types.linear_rings.serialize_json(
            value["polygon"]
        )
    if "polyline_corridor" in value:
        import capo_geo_routes.types.polyline_corridor

        out["PolylineCorridor"] = (
            capo_geo_routes.types.polyline_corridor.serialize_json(
                value["polyline_corridor"]
            )
        )
    if "polyline_polygon" in value:
        import capo_geo_routes.types.polyline_ring_list

        out["PolylinePolygon"] = (
            capo_geo_routes.types.polyline_ring_list.serialize_json(
                value["polyline_polygon"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteAvoidanceAreaGeometry:
    out: RouteAvoidanceAreaGeometry = {}  # type: ignore[typeddict-item]
    if data.get("Corridor") is not None:
        import capo_geo_routes.types.corridor

        out["corridor"] = capo_geo_routes.types.corridor.deserialize_json(
            data["Corridor"]
        )
    if data.get("BoundingBox") is not None:
        import capo_geo_routes.types.bounding_box

        out["bounding_box"] = capo_geo_routes.types.bounding_box.deserialize_json(
            data["BoundingBox"]
        )
    if data.get("Polygon") is not None:
        import capo_geo_routes.types.linear_rings

        out["polygon"] = capo_geo_routes.types.linear_rings.deserialize_json(
            data["Polygon"]
        )
    if data.get("PolylineCorridor") is not None:
        import capo_geo_routes.types.polyline_corridor

        out["polyline_corridor"] = (
            capo_geo_routes.types.polyline_corridor.deserialize_json(
                data["PolylineCorridor"]
            )
        )
    if data.get("PolylinePolygon") is not None:
        import capo_geo_routes.types.polyline_ring_list

        out["polyline_polygon"] = (
            capo_geo_routes.types.polyline_ring_list.deserialize_json(
                data["PolylinePolygon"]
            )
        )
    return out
