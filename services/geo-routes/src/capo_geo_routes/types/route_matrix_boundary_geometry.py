"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixBoundaryGeometry``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.bounding_box
    import capo_geo_routes.types.circle
    import capo_geo_routes.types.linear_rings
    import capo_geo_routes.types.route_matrix_auto_circle


class RouteMatrixBoundaryGeometry(TypedDict, closed=True):
    auto_circle: NotRequired[
        "capo_geo_routes.types.route_matrix_auto_circle.RouteMatrixAutoCircle"
    ]
    """<p> <code>AutoCircle</code> requests the route matrix service to define a <code>Circle</code> boundary that best attempts to include most waypoints (<code>Origins</code> and <code>Destinations</code>) using the <code>AutoCircle</code> settings. Any waypoints outside of the auto-defined <code>Circle</code> boundary will be considered out of the routing boundary, which results in a route matrix entry error.</p> <p> <code>AutoCircle</code> is only used in the request to configure a <code>Circle</code> for the route calculation. The derived <code>Circle</code> will also be provided in the response.</p>"""
    circle: NotRequired["capo_geo_routes.types.circle.Circle"]
    """<p>Geometry defined as a circle. The circle defines the routing boundary area. Any waypoints outside the circle will result in a route matrix entry error.</p> <p>You can specify a <code>Circle</code> directly in the request, or it will be auto-derived when <code>AutoCircle</code> is used. When <code>AutoCircle</code> is set in the request, the response routing boundary will return <code>Circle</code> derived from the <code>AutoCircle</code> settings.</p>"""
    bounding_box: NotRequired["capo_geo_routes.types.bounding_box.BoundingBox"]
    """<p>Geometry defined as a bounding box. The first pair represents the X and Y coordinates (longitude and latitude,) of the southwest corner of the bounding box; the second pair represents the X and Y coordinates (longitude and latitude) of the northeast corner.</p> <p>Diagonal distance of the bounding box must be less than or equal to 400,000 meters.</p>"""
    polygon: NotRequired["capo_geo_routes.types.linear_rings.LinearRings"]
    """<p>Geometry defined as a polygon with only one linear ring. A linear ring is a closed sequence of four or more coordinates. The first and last coordinates are the same, forming a closed boundary. Each coordinate is a position in [longitude, latitude] format.</p> <p>The structure is an array of linear rings (only 1 allowed). Each linear ring is an array of coordinates (minimum 4), and each coordinate is an array of two doubles [longitude, latitude].</p> <p>Maximum distance between any two vertices must be less than or equal to 400,000 meters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixBoundaryGeometry) -> dict:
    out: dict = {}
    if "auto_circle" in value:
        import capo_geo_routes.types.route_matrix_auto_circle

        out["AutoCircle"] = (
            capo_geo_routes.types.route_matrix_auto_circle.serialize_json(
                value["auto_circle"]
            )
        )
    if "circle" in value:
        import capo_geo_routes.types.circle

        out["Circle"] = capo_geo_routes.types.circle.serialize_json(value["circle"])
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
    return out


def deserialize_json(data: dict) -> RouteMatrixBoundaryGeometry:
    out: RouteMatrixBoundaryGeometry = {}  # type: ignore[typeddict-item]
    if data.get("AutoCircle") is not None:
        import capo_geo_routes.types.route_matrix_auto_circle

        out["auto_circle"] = (
            capo_geo_routes.types.route_matrix_auto_circle.deserialize_json(
                data["AutoCircle"]
            )
        )
    if data.get("Circle") is not None:
        import capo_geo_routes.types.circle

        out["circle"] = capo_geo_routes.types.circle.deserialize_json(data["Circle"])
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
    return out


def redact_sensitive(value: RouteMatrixBoundaryGeometry) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "auto_circle" in value:
        import capo_geo_routes.types.route_matrix_auto_circle

        out["auto_circle"] = (
            capo_geo_routes.types.route_matrix_auto_circle.redact_sensitive(
                value["auto_circle"]
            )
        )
    if "circle" in value:
        out["circle"] = "*** Sensitive Data Redacted ***"
    if "bounding_box" in value:
        out["bounding_box"] = "*** Sensitive Data Redacted ***"
    if "polygon" in value:
        import capo_geo_routes.types.linear_rings

        out["polygon"] = capo_geo_routes.types.linear_rings.redact_sensitive(
            value["polygon"]
        )
    return out
