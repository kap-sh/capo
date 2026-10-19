"""Generated from Smithy shape ``com.amazonaws.location#ForecastGeofenceEventsDeviceState``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.position


class ForecastGeofenceEventsDeviceState(TypedDict, closed=True):
    position: "capo_location.types.position.Position"
    """<p>The device's position.</p>"""
    speed: NotRequired["float"]
    """<p>The device's speed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForecastGeofenceEventsDeviceState) -> dict:
    out: dict = {}
    import capo_location.types.position

    out["Position"] = capo_location.types.position.serialize_json(value["position"])
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


def deserialize_json(data: dict) -> ForecastGeofenceEventsDeviceState:
    out: ForecastGeofenceEventsDeviceState = {}  # type: ignore[typeddict-item]
    if data.get("Position") is not None:
        import capo_location.types.position

        out["position"] = capo_location.types.position.deserialize_json(
            data["Position"]
        )
    else:
        out["position"] = []
    if data.get("Speed") is not None:
        out["speed"] = float(data["Speed"])
    return out


def redact_sensitive(value: ForecastGeofenceEventsDeviceState) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "position" in value:
        out["position"] = "*** Sensitive Data Redacted ***"
    return out
