"""Generated from Smithy shape ``com.amazonaws.georoutes#Circle``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.position
    import capo_geo_routes.types.sensitive_double


class Circle(TypedDict, closed=True):
    center: "capo_geo_routes.types.position.Position"
    """<p>Center of the Circle in World Geodetic System (WGS 84) format: [longitude, latitude].</p> <p>Example: <code>[-123.1174, 49.2847]</code> represents the position with longitude <code>-123.1174</code> and latitude <code>49.2847</code>. </p>"""
    radius: "capo_geo_routes.types.sensitive_double.SensitiveDouble"
    """<p>Radius of the Circle.</p> <p> <b>Unit</b>: <code>meters</code> </p> <p>Valid Range: Minimum value of 0. Maximum value of 200000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Circle) -> dict:
    out: dict = {}
    import capo_geo_routes.types.position

    out["Center"] = capo_geo_routes.types.position.serialize_json(value["center"])
    out["Radius"] = (
        "NaN"
        if value["radius"] != value["radius"]
        else "Infinity"
        if value["radius"] == float("inf")
        else "-Infinity"
        if value["radius"] == float("-inf")
        else value["radius"]
    )
    return out


def deserialize_json(data: dict) -> Circle:
    out: Circle = {}  # type: ignore[typeddict-item]
    if data.get("Center") is not None:
        import capo_geo_routes.types.position

        out["center"] = capo_geo_routes.types.position.deserialize_json(data["Center"])
    else:
        out["center"] = []
    if data.get("Radius") is not None:
        out["radius"] = float(data["Radius"])
    else:
        out["radius"] = 0.0
    return out
