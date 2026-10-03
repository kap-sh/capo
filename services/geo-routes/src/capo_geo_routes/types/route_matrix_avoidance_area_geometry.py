"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixAvoidanceAreaGeometry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.bounding_box
    import capo_geo_routes.types.linear_rings
    import capo_geo_routes.types.polyline_ring_list


class RouteMatrixAvoidanceAreaGeometry(TypedDict, closed=True):
    bounding_box: NotRequired["capo_geo_routes.types.bounding_box.BoundingBox"]
    """<p>Geometry defined as a bounding box. The first pair represents the X and Y coordinates (longitude and latitude,) of the southwest corner of the bounding box; the second pair represents the X and Y coordinates (longitude and latitude) of the northeast corner.</p>"""
    polygon: NotRequired["capo_geo_routes.types.linear_rings.LinearRings"]
    """<p>Geometry defined as a polygon with only one linear ring.</p>"""
    polyline_polygon: NotRequired[
        "capo_geo_routes.types.polyline_ring_list.PolylineRingList"
    ]
    """<p>A list of Isoline PolylinePolygon, for each isoline PolylinePolygon, it contains PolylinePolygon of the first linear ring (the outer ring) and from second item to the last item (the inner rings). For more information on polyline encoding, see <a href="https://github.com/aws-geospatial/polyline">https://github.com/aws-geospatial/polyline</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixAvoidanceAreaGeometry) -> dict:
    out: dict = {}
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
    if "polyline_polygon" in value:
        import capo_geo_routes.types.polyline_ring_list

        out["PolylinePolygon"] = (
            capo_geo_routes.types.polyline_ring_list.serialize_json(
                value["polyline_polygon"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteMatrixAvoidanceAreaGeometry:
    out: RouteMatrixAvoidanceAreaGeometry = {}  # type: ignore[typeddict-item]
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
    if data.get("PolylinePolygon") is not None:
        import capo_geo_routes.types.polyline_ring_list

        out["polyline_polygon"] = (
            capo_geo_routes.types.polyline_ring_list.deserialize_json(
                data["PolylinePolygon"]
            )
        )
    return out
