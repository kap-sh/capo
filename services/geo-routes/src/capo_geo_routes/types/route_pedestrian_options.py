"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.speed_kilometers_per_hour


class RoutePedestrianOptions(TypedDict, closed=True):
    speed: NotRequired[
        "capo_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    ]
    """<p>Walking speed in Kilometers per hour.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutePedestrianOptions) -> dict:
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


def deserialize_json(data: dict) -> RoutePedestrianOptions:
    out: RoutePedestrianOptions = {}  # type: ignore[typeddict-item]
    if data.get("Speed") is not None:
        out["speed"] = float(data["Speed"])
    return out


def redact_sensitive(value: RoutePedestrianOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "speed" in value:
        out["speed"] = "*** Sensitive Data Redacted ***"
    return out
