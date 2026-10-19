"""Generated from Smithy shape ``com.amazonaws.georoutes#PolylineCorridor``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.polyline


class PolylineCorridor(TypedDict, closed=True):
    polyline: "capo_geo_routes.types.polyline.Polyline"
    """<p>An ordered list of positions used to plot a route on a map in a lossy compression format.</p> <note> <p>LineString and Polyline are mutually exclusive properties.</p> </note>"""
    radius: "int"
    """<p>Considers all roads within the provided radius to match the provided destination to. The roads that are considered are determined by the provided Strategy.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolylineCorridor) -> dict:
    out: dict = {}
    out["Polyline"] = value["polyline"]
    out["Radius"] = value["radius"]
    return out


def deserialize_json(data: dict) -> PolylineCorridor:
    out: PolylineCorridor = {}  # type: ignore[typeddict-item]
    if data.get("Polyline") is not None:
        out["polyline"] = data["Polyline"]
    else:
        out["polyline"] = ""
    if data.get("Radius") is not None:
        out["radius"] = data["Radius"]
    else:
        out["radius"] = 0
    return out
