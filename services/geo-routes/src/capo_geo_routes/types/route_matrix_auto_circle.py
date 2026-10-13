"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixAutoCircle``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters


class RouteMatrixAutoCircle(TypedDict, closed=True):
    margin: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>The minimal distance, in meters, between any waypoint and the perimeter of the circle auto-defined for the boundary. Some margin is usually recommended so that the routing has enough leeway to travel from one waypoint to another optimally without conflicting with the routing boundary.</p> <p>The total of <code>MaxRadius</code> and <code>Margin</code> must be less than or equal to 200,000 meters.</p>"""
    max_radius: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>The maximum radius, in meters, that the auto-defined <code>Circle</code> boundary should have, before the <code>Margin</code> distance is added to the circle.</p> <p>The total of <code>MaxRadius</code> and <code>Margin</code> must be less than or equal to 200,000 meters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixAutoCircle) -> dict:
    out: dict = {}
    out["Margin"] = value.get("margin", 0)
    out["MaxRadius"] = value.get("max_radius", 0)
    return out


def deserialize_json(data: dict) -> RouteMatrixAutoCircle:
    out: RouteMatrixAutoCircle = {}  # type: ignore[typeddict-item]
    if data.get("Margin") is not None:
        out["margin"] = data["Margin"]
    else:
        out["margin"] = 0
    if data.get("MaxRadius") is not None:
        out["max_radius"] = data["MaxRadius"]
    else:
        out["max_radius"] = 0
    return out


def redact_sensitive(value: RouteMatrixAutoCircle) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "margin" in value:
        out["margin"] = "*** Sensitive Data Redacted ***"
    if "max_radius" in value:
        out["max_radius"] = "*** Sensitive Data Redacted ***"
    return out
