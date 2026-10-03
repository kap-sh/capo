"""Generated from Smithy shape ``com.amazonaws.location#GeofenceGeometry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.base64_encoded_geobuf
    import capo_location.types.circle
    import capo_location.types.linear_rings
    import capo_location.types.multi_linear_rings


class GeofenceGeometry(TypedDict, closed=True):
    polygon: NotRequired["capo_location.types.linear_rings.LinearRings"]
    """<p>A <code>Polygon</code> is a list of up to 250 linear rings which represent the shape of a geofence. This list <i>must</i> include 1 exterior ring (representing the outer perimeter of the geofence), and can optionally include up to 249 interior rings (representing polygonal spaces within the perimeter, which are excluded from the geofence area).</p> <p>A linear ring is an array of 4 or more vertices, where the first and last vertex are the same (to form a closed boundary). Each vertex is a 2-dimensional point represented as an array of doubles of length 2: <code>[longitude, latitude]</code>.</p> <p>Each linear ring is represented as an array of arrays of doubles (<code>[[longitude, latitude], [longitude, latitude], ...]</code>). The vertices for the exterior ring must be listed in <i>counter-clockwise</i> sequence. Vertices for all interior rings must be listed in <i>clockwise</i> sequence.</p> <p>The list of linear rings that describe the entire <code>Polygon</code> is represented as an array of arrays of arrays of doubles (<code>[[[longitude, latitude], [longitude, latitude], ...], [[longitude, latitude], [longitude, latitude], ...], ...]</code>). The exterior ring must be listed first, before any interior rings.</p> <note> <p>The following additional requirements and limitations apply to geometries defined using the <code>Polygon</code> parameter:</p> <ul> <li> <p>The entire <code>Polygon</code> must consist of no more than 1,000 vertices, including all vertices from the exterior ring and all interior rings.</p> </li> <li> <p>Rings must not touch or cross each other.</p> </li> <li> <p>All interior rings must be fully contained within the exterior ring.</p> </li> <li> <p>Interior rings must not contain other interior rings.</p> </li> <li> <p>No ring is permitted to intersect itself.</p> </li> </ul> </note>"""
    circle: NotRequired["capo_location.types.circle.Circle"]
    """<p>A circle on the earth, as defined by a center point and a radius.</p>"""
    geobuf: NotRequired["capo_location.types.base64_encoded_geobuf.Base64EncodedGeobuf"]
    """<p>Geobuf is a compact binary encoding for geographic data that provides lossless compression of GeoJSON polygons. The Geobuf must be Base64-encoded.</p> <p>This parameter can contain a Geobuf-encoded GeoJSON geometry object of type <code>Polygon</code> <i>OR</i> <code>MultiPolygon</code>. For more information and specific configuration requirements for these object types, see <a href="https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_GeofenceGeometry.html#location-Type-WaypointGeofencing_GeofenceGeometry-Polygon">Polygon</a> and <a href="https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_GeofenceGeometry.html#location-Type-WaypointGeofencing_GeofenceGeometry-MultiPolygon">MultiPolygon</a>.</p> <note> <p>The following limitations apply specifically to geometries defined using the <code>Geobuf</code> parameter, and supercede the corresponding limitations of the <code>Polygon</code> and <code>MultiPolygon</code> parameters:</p> <ul> <li> <p>A <code>Polygon</code> in <code>Geobuf</code> format can have up to 25,000 rings and up to 100,000 total vertices, including all vertices from all component rings.</p> </li> <li> <p>A <code>MultiPolygon</code> in <code>Geobuf</code> format can contain up to 10,000 <code>Polygons</code> and up to 100,000 total vertices, including all vertices from all component <code>Polygons</code>.</p> </li> </ul> </note>"""
    multi_polygon: NotRequired[
        "capo_location.types.multi_linear_rings.MultiLinearRings"
    ]
    """<p>A <code>MultiPolygon</code> is a list of up to 250 <code>Polygon</code> elements which represent the shape of a geofence. The <code>Polygon</code> components of a <code>MultiPolygon</code> geometry can define separate geographical areas that are considered part of the same geofence, perimeters of larger exterior areas with smaller interior spaces that are excluded from the geofence, or some combination of these use cases to form complex geofence boundaries.</p> <p>For more information and specific configuration requirements for the <code>Polygon</code> components that form a <code>MultiPolygon</code>, see <a href="https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_GeofenceGeometry.html#location-Type-WaypointGeofencing_GeofenceGeometry-Polygon">Polygon</a>.</p> <note> <p>The following additional requirements and limitations apply to geometries defined using the <code>MultiPolygon</code> parameter:</p> <ul> <li> <p>The entire <code>MultiPolygon</code> must consist of no more than 1,000 vertices, including all vertices from all component <code>Polygons</code>.</p> </li> <li> <p>Each edge of a component <code>Polygon</code> must intersect no more than 5 edges from other <code>Polygons</code>. Parallel edges that are shared but do not cross are not counted toward this limit.</p> </li> <li> <p>The total number of intersecting edges of component <code>Polygons</code> must be no more than 100,000. Parallel edges that are shared but do not cross are not counted toward this limit.</p> </li> </ul> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeofenceGeometry) -> dict:
    out: dict = {}
    if "polygon" in value:
        import capo_location.types.linear_rings

        out["Polygon"] = capo_location.types.linear_rings.serialize_json(
            value["polygon"]
        )
    if "circle" in value:
        import capo_location.types.circle

        out["Circle"] = capo_location.types.circle.serialize_json(value["circle"])
    if "geobuf" in value:
        import capo_location.types.base64_encoded_geobuf

        out["Geobuf"] = capo_location.types.base64_encoded_geobuf.serialize_json(
            value["geobuf"]
        )
    if "multi_polygon" in value:
        import capo_location.types.multi_linear_rings

        out["MultiPolygon"] = capo_location.types.multi_linear_rings.serialize_json(
            value["multi_polygon"]
        )
    return out


def deserialize_json(data: dict) -> GeofenceGeometry:
    out: GeofenceGeometry = {}  # type: ignore[typeddict-item]
    if data.get("Polygon") is not None:
        import capo_location.types.linear_rings

        out["polygon"] = capo_location.types.linear_rings.deserialize_json(
            data["Polygon"]
        )
    if data.get("Circle") is not None:
        import capo_location.types.circle

        out["circle"] = capo_location.types.circle.deserialize_json(data["Circle"])
    if data.get("Geobuf") is not None:
        import capo_location.types.base64_encoded_geobuf

        out["geobuf"] = capo_location.types.base64_encoded_geobuf.deserialize_json(
            data["Geobuf"]
        )
    if data.get("MultiPolygon") is not None:
        import capo_location.types.multi_linear_rings

        out["multi_polygon"] = capo_location.types.multi_linear_rings.deserialize_json(
            data["MultiPolygon"]
        )
    return out
