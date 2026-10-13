"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineConnection``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.isoline_connection_geometry


class IsolineConnection(TypedDict, closed=True):
    from_polygon_index: "int"
    """<p>The index of the starting polygon in the isoline's <code>Geometries</code> list.</p>"""
    geometry: (
        "capo_geo_routes.types.isoline_connection_geometry.IsolineConnectionGeometry"
    )
    """<p>The shape of the connection, representing the actual path through the transportation network that links the polygons.</p>"""
    to_polygon_index: "int"
    """<p>The index of the ending polygon in the isoline's <code>Geometries</code> list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineConnection) -> dict:
    out: dict = {}
    out["FromPolygonIndex"] = value["from_polygon_index"]
    import capo_geo_routes.types.isoline_connection_geometry

    out["Geometry"] = capo_geo_routes.types.isoline_connection_geometry.serialize_json(
        value["geometry"]
    )
    out["ToPolygonIndex"] = value["to_polygon_index"]
    return out


def deserialize_json(data: dict) -> IsolineConnection:
    out: IsolineConnection = {}  # type: ignore[typeddict-item]
    if data.get("FromPolygonIndex") is not None:
        out["from_polygon_index"] = data["FromPolygonIndex"]
    else:
        raise DeserializationError("IsolineConnection.from_polygon_index required")
    if data.get("Geometry") is not None:
        import capo_geo_routes.types.isoline_connection_geometry

        out["geometry"] = (
            capo_geo_routes.types.isoline_connection_geometry.deserialize_json(
                data["Geometry"]
            )
        )
    else:
        raise DeserializationError("IsolineConnection.geometry required")
    if data.get("ToPolygonIndex") is not None:
        out["to_polygon_index"] = data["ToPolygonIndex"]
    else:
        raise DeserializationError("IsolineConnection.to_polygon_index required")
    return out


def redact_sensitive(value: IsolineConnection) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "geometry" in value:
        import capo_geo_routes.types.isoline_connection_geometry

        out["geometry"] = (
            capo_geo_routes.types.isoline_connection_geometry.redact_sensitive(
                value["geometry"]
            )
        )
    return out
