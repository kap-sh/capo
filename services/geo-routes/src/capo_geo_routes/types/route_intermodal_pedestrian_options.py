"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteIntermodalPedestrianOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.speed_kilometers_per_hour


class RouteIntermodalPedestrianOptions(TypedDict, closed=True):
    max_distance: NotRequired["capo_geo_routes.types.distance_meters.DistanceMeters"]
    """<p>Maximum walking distance allowed.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""
    speed: NotRequired[
        "capo_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    ]
    """<p>Walking speed.</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteIntermodalPedestrianOptions) -> dict:
    out: dict = {}
    if "max_distance" in value:
        out["MaxDistance"] = value["max_distance"]
    if "speed" in value:
        out["Speed"] = (
            "NaN"
            if value["speed"] != value["speed"]
            else "Infinity"
            if value["speed"] == float("inf")
            else "-Infinity"
            if value["speed"] == float("-inf")
            else value["speed"]
        )
    return out


def deserialize_json(data: dict) -> RouteIntermodalPedestrianOptions:
    out: RouteIntermodalPedestrianOptions = {}  # type: ignore[typeddict-item]
    if data.get("MaxDistance") is not None:
        out["max_distance"] = data["MaxDistance"]
    if data.get("Speed") is not None:
        out["speed"] = float(data["Speed"])
    return out


def redact_sensitive(value: RouteIntermodalPedestrianOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "max_distance" in value:
        out["max_distance"] = "*** Sensitive Data Redacted ***"
    if "speed" in value:
        out["speed"] = "*** Sensitive Data Redacted ***"
    return out
