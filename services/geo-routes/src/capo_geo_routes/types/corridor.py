"""Generated from Smithy shape ``com.amazonaws.georoutes#Corridor``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.line_string


class Corridor(TypedDict, closed=True):
    line_string: "capo_geo_routes.types.line_string.LineString"
    """<p>An ordered list of positions used to plot a route on a map.</p> <note> <p>LineString and Polyline are mutually exclusive properties.</p> </note>"""
    radius: "int"
    """<p>Radius that defines the width of the corridor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Corridor) -> dict:
    out: dict = {}
    import capo_geo_routes.types.line_string

    out["LineString"] = capo_geo_routes.types.line_string.serialize_json(
        value["line_string"]
    )
    out["Radius"] = value["radius"]
    return out


def deserialize_json(data: dict) -> Corridor:
    out: Corridor = {}  # type: ignore[typeddict-item]
    if data.get("LineString") is not None:
        import capo_geo_routes.types.line_string

        out["line_string"] = capo_geo_routes.types.line_string.deserialize_json(
            data["LineString"]
        )
    else:
        out["line_string"] = []
    if data.get("Radius") is not None:
        out["radius"] = data["Radius"]
    else:
        out["radius"] = 0
    return out
