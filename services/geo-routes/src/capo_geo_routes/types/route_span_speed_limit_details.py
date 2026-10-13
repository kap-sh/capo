"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanSpeedLimitDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_boolean
    import capo_geo_routes.types.speed_kilometers_per_hour


class RouteSpanSpeedLimitDetails(TypedDict, closed=True):
    max_speed: "capo_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    """<p>Maximum speed.</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""
    unlimited: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>If the span doesn't have a speed limit like the Autobahn.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanSpeedLimitDetails) -> dict:
    out: dict = {}
    out["MaxSpeed"] = (
        "NaN"
        if value.get("max_speed", 0) != value.get("max_speed", 0)
        else "Infinity"
        if value.get("max_speed", 0) == float("inf")
        else "-Infinity"
        if value.get("max_speed", 0) == float("-inf")
        else value.get("max_speed", 0)
    )
    if "unlimited" in value:
        out["Unlimited"] = value["unlimited"]
    return out


def deserialize_json(data: dict) -> RouteSpanSpeedLimitDetails:
    out: RouteSpanSpeedLimitDetails = {}  # type: ignore[typeddict-item]
    if data.get("MaxSpeed") is not None:
        out["max_speed"] = float(data["MaxSpeed"])
    else:
        out["max_speed"] = 0
    if data.get("Unlimited") is not None:
        out["unlimited"] = data["Unlimited"]
    return out


def redact_sensitive(value: RouteSpanSpeedLimitDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "max_speed" in value:
        out["max_speed"] = "*** Sensitive Data Redacted ***"
    if "unlimited" in value:
        out["unlimited"] = "*** Sensitive Data Redacted ***"
    return out
