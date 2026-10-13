"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapSnappedGeometry``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.line_string
    import capo_geo_routes.types.polyline


class RoadSnapSnappedGeometry(TypedDict, closed=True):
    line_string: NotRequired["capo_geo_routes.types.line_string.LineString"]
    """<p>An ordered list of positions used to plot a route on a map.</p> <note> <p>LineString and Polyline are mutually exclusive properties.</p> </note>"""
    polyline: NotRequired["capo_geo_routes.types.polyline.Polyline"]
    """<p>An ordered list of positions used to plot a route on a map in a lossy compression format.</p> <note> <p>LineString and Polyline are mutually exclusive properties.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapSnappedGeometry) -> dict:
    out: dict = {}
    if "line_string" in value:
        import capo_geo_routes.types.line_string

        out["LineString"] = capo_geo_routes.types.line_string.serialize_json(
            value["line_string"]
        )
    if "polyline" in value:
        out["Polyline"] = value["polyline"]
    return out


def deserialize_json(data: dict) -> RoadSnapSnappedGeometry:
    out: RoadSnapSnappedGeometry = {}  # type: ignore[typeddict-item]
    if data.get("LineString") is not None:
        import capo_geo_routes.types.line_string

        out["line_string"] = capo_geo_routes.types.line_string.deserialize_json(
            data["LineString"]
        )
    if data.get("Polyline") is not None:
        out["polyline"] = data["Polyline"]
    return out


def redact_sensitive(value: RoadSnapSnappedGeometry) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "line_string" in value:
        import capo_geo_routes.types.line_string

        out["line_string"] = capo_geo_routes.types.line_string.redact_sensitive(
            value["line_string"]
        )
    if "polyline" in value:
        out["polyline"] = "*** Sensitive Data Redacted ***"
    return out
