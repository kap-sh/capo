"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitTravelOnlySummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds


class RouteTransitTravelOnlySummary(TypedDict, closed=True):
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the travel portion of the transit leg.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitTravelOnlySummary) -> dict:
    out: dict = {}
    out["Duration"] = value["duration"]
    return out


def deserialize_json(data: dict) -> RouteTransitTravelOnlySummary:
    out: RouteTransitTravelOnlySummary = {}  # type: ignore[typeddict-item]
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    return out


def redact_sensitive(value: RouteTransitTravelOnlySummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "duration" in value:
        out["duration"] = "*** Sensitive Data Redacted ***"
    return out
