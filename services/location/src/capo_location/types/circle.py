"""Generated from Smithy shape ``com.amazonaws.location#Circle``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.position
    import capo_location.types.sensitive_double


class Circle(TypedDict, closed=True):
    center: "capo_location.types.position.Position"
    """<p>A single point geometry, specifying the center of the circle, using <a href="https://gisgeography.com/wgs84-world-geodetic-system/">WGS 84</a> coordinates, in the form <code>[longitude, latitude]</code>.</p>"""
    radius: "capo_location.types.sensitive_double.SensitiveDouble"
    """<p>The radius of the circle in meters. Must be greater than zero and no larger than 100,000 (100 kilometers).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Circle) -> dict:
    out: dict = {}
    import capo_location.types.position

    out["Center"] = capo_location.types.position.serialize_json(value["center"])
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
        import capo_location.types.position

        out["center"] = capo_location.types.position.deserialize_json(data["Center"])
    else:
        raise DeserializationError("Circle.center required")
    if data.get("Radius") is not None:
        out["radius"] = float(data["Radius"])
    else:
        raise DeserializationError("Circle.radius required")
    return out
