"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationPedestrianOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.speed_kilometers_per_hour


class WaypointOptimizationPedestrianOptions(TypedDict, closed=True):
    speed: NotRequired[
        "capo_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    ]
    """<p>Walking speed.</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationPedestrianOptions) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> WaypointOptimizationPedestrianOptions:
    out: WaypointOptimizationPedestrianOptions = {}  # type: ignore[typeddict-item]
    if data.get("Speed") is not None:
        out["speed"] = float(data["Speed"])
    return out


def redact_sensitive(value: WaypointOptimizationPedestrianOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "speed" in value:
        out["speed"] = "*** Sensitive Data Redacted ***"
    return out
