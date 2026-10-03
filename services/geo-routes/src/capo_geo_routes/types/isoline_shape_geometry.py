"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineShapeGeometry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.linear_rings
    import capo_geo_routes.types.polyline_ring_list


class IsolineShapeGeometry(TypedDict, closed=True):
    polygon: NotRequired["capo_geo_routes.types.linear_rings.LinearRings"]
    """<p>A series of coordinate rings defining the reachable area when Simple geometry format is requested. Each ring is a list of <code>[longitude, latitude]</code> coordinate pairs. The first ring defines the outer boundary; subsequent rings define holes representing unreachable areas.</p> <note> <p>Polygon and PolylinePolygon are mutually exclusive properties.</p> </note>"""
    polyline_polygon: NotRequired[
        "capo_geo_routes.types.polyline_ring_list.PolylineRingList"
    ]
    """<p>An encoded representation of the reachable area when FlexiblePolyline geometry format is requested. Provides a compact representation suitable for transmission and storage. The first string defines the outer boundary; subsequent strings define holes representing unreachable areas. For more information on polyline encoding, see <a href="https://github.com/aws-geospatial/polyline">https://github.com/aws-geospatial/polyline</a>.</p> <note> <p>Polygon and PolylinePolygon are mutually exclusive properties.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineShapeGeometry) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> IsolineShapeGeometry:
    out: IsolineShapeGeometry = {}  # type: ignore[typeddict-item]
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
