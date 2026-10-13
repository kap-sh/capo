"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanDynamicSpeedDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.speed_kilometers_per_hour


class RouteSpanDynamicSpeedDetails(TypedDict, closed=True):
    best_case_speed: (
        "capo_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    )
    """<p>Estimated speed while traversing the span without traffic congestion.</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""
    turn_duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Estimated time to turn from this span into the next. </p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    typical_speed: (
        "capo_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    )
    """<p>Estimated speed while traversing the span under typical traffic congestion.</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanDynamicSpeedDetails) -> dict:
    out: dict = {}
    out["BestCaseSpeed"] = (
        "NaN"
        if value.get("best_case_speed", 0) != value.get("best_case_speed", 0)
        else "Infinity"
        if value.get("best_case_speed", 0) == float("inf")
        else "-Infinity"
        if value.get("best_case_speed", 0) == float("-inf")
        else value.get("best_case_speed", 0)
    )
    out["TurnDuration"] = value.get("turn_duration", 0)
    out["TypicalSpeed"] = (
        "NaN"
        if value.get("typical_speed", 0) != value.get("typical_speed", 0)
        else "Infinity"
        if value.get("typical_speed", 0) == float("inf")
        else "-Infinity"
        if value.get("typical_speed", 0) == float("-inf")
        else value.get("typical_speed", 0)
    )
    return out


def deserialize_json(data: dict) -> RouteSpanDynamicSpeedDetails:
    out: RouteSpanDynamicSpeedDetails = {}  # type: ignore[typeddict-item]
    if data.get("BestCaseSpeed") is not None:
        out["best_case_speed"] = float(data["BestCaseSpeed"])
    else:
        out["best_case_speed"] = 0
    if data.get("TurnDuration") is not None:
        out["turn_duration"] = data["TurnDuration"]
    else:
        out["turn_duration"] = 0
    if data.get("TypicalSpeed") is not None:
        out["typical_speed"] = float(data["TypicalSpeed"])
    else:
        out["typical_speed"] = 0
    return out


def redact_sensitive(value: RouteSpanDynamicSpeedDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "best_case_speed" in value:
        out["best_case_speed"] = "*** Sensitive Data Redacted ***"
    if "turn_duration" in value:
        out["turn_duration"] = "*** Sensitive Data Redacted ***"
    if "typical_speed" in value:
        out["typical_speed"] = "*** Sensitive Data Redacted ***"
    return out
