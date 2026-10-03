"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineAvoidanceAreaGeometry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.bounding_box
    import capo_geo_routes.types.corridor
    import capo_geo_routes.types.linear_rings
    import capo_geo_routes.types.polyline_corridor
    import capo_geo_routes.types.polyline_ring_list


class IsolineAvoidanceAreaGeometry(TypedDict, closed=True):
    bounding_box: NotRequired["capo_geo_routes.types.bounding_box.BoundingBox"]
    """<p>A rectangular area defined by its southwest and northeast corners: <code>[min longitude, min latitude, max longitude, max latitude]</code>.</p>"""
    corridor: NotRequired["capo_geo_routes.types.corridor.Corridor"]
    """<p>A buffer zone around a line, defined by a series of coordinates and a radius in meters.</p>"""
    polygon: NotRequired["capo_geo_routes.types.linear_rings.LinearRings"]
    """<p>A polygon defined by a list of coordinate rings. The first ring defines the outer boundary; subsequent rings will be ignored.</p>"""
    polyline_corridor: NotRequired[
        "capo_geo_routes.types.polyline_corridor.PolylineCorridor"
    ]
    """<p>A buffer zone around a compressed polyline, defined by an encoded polyline string and a radius in meters. For more information on polyline encoding, see <a href="https://github.com/aws-geospatial/polyline">https://github.com/aws-geospatial/polyline</a>.</p>"""
    polyline_polygon: NotRequired[
        "capo_geo_routes.types.polyline_ring_list.PolylineRingList"
    ]
    """<p>A polygon defined by encoded polyline strings. The first string defines the outer boundary; subsequent strings will be ignored. For more information on polyline encoding, see <a href="https://github.com/aws-geospatial/polyline">https://github.com/aws-geospatial/polyline</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineAvoidanceAreaGeometry) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import capo_geo_routes.types.bounding_box

        out["BoundingBox"] = capo_geo_routes.types.bounding_box.serialize_json(
            value["bounding_box"]
        )
    if "corridor" in value:
        import capo_geo_routes.types.corridor

        out["Corridor"] = capo_geo_routes.types.corridor.serialize_json(
            value["corridor"]
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


def deserialize_json(data: dict) -> IsolineAvoidanceAreaGeometry:
    out: IsolineAvoidanceAreaGeometry = {}  # type: ignore[typeddict-item]
    if data.get("BoundingBox") is not None:
        import capo_geo_routes.types.bounding_box

        out["bounding_box"] = capo_geo_routes.types.bounding_box.deserialize_json(
            data["BoundingBox"]
        )
    if data.get("Corridor") is not None:
        import capo_geo_routes.types.corridor

        out["corridor"] = capo_geo_routes.types.corridor.deserialize_json(
            data["Corridor"]
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
