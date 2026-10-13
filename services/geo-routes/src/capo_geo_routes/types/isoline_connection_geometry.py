"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineConnectionGeometry``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.line_string
    import capo_geo_routes.types.polyline


class IsolineConnectionGeometry(TypedDict, closed=True):
    line_string: NotRequired["capo_geo_routes.types.line_string.LineString"]
    """<p>A series of <code>[longitude, latitude]</code> coordinate pairs defining the connection path when <code>Simple</code> geometry format is requested. These coordinates can be directly used as the coordinates array in a GeoJSON LineString without transformation.</p> <note> <p>LineString and Polyline are mutually exclusive properties.</p> </note>"""
    polyline: NotRequired["capo_geo_routes.types.polyline.Polyline"]
    """<p>An encoded representation of the connection path when <code>FlexiblePolyline</code> geometry format is requested. This provides a more compact representation suitable for transmission and storage. To convert to GeoJSON, first decode to obtain coordinate pairs, then use those coordinates as the coordinates array in a GeoJSON LineString.</p> <note> <p>LineString and Polyline are mutually exclusive properties.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineConnectionGeometry) -> dict:
    out: dict = {}
    if "line_string" in value:
        import capo_geo_routes.types.line_string

        out["LineString"] = capo_geo_routes.types.line_string.serialize_json(
            value["line_string"]
        )
    if "polyline" in value:
        out["Polyline"] = value["polyline"]
    return out


def deserialize_json(data: dict) -> IsolineConnectionGeometry:
    out: IsolineConnectionGeometry = {}  # type: ignore[typeddict-item]
    if data.get("LineString") is not None:
        import capo_geo_routes.types.line_string

        out["line_string"] = capo_geo_routes.types.line_string.deserialize_json(
            data["LineString"]
        )
    if data.get("Polyline") is not None:
        out["polyline"] = data["Polyline"]
    return out


def redact_sensitive(value: IsolineConnectionGeometry) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "line_string" in value:
        import capo_geo_routes.types.line_string

        out["line_string"] = capo_geo_routes.types.line_string.redact_sensitive(
            value["line_string"]
        )
    if "polyline" in value:
        out["polyline"] = "*** Sensitive Data Redacted ***"
    return out
