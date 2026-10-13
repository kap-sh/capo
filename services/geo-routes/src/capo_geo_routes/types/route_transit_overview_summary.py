"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitOverviewSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.duration_seconds


class RouteTransitOverviewSummary(TypedDict, closed=True):
    distance: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Distance of the entire leg.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the entire leg.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitOverviewSummary) -> dict:
    out: dict = {}
    out["Distance"] = value["distance"]
    out["Duration"] = value["duration"]
    return out


def deserialize_json(data: dict) -> RouteTransitOverviewSummary:
    out: RouteTransitOverviewSummary = {}  # type: ignore[typeddict-item]
    if data.get("Distance") is not None:
        out["distance"] = data["Distance"]
    else:
        raise DeserializationError("RouteTransitOverviewSummary.distance required")
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("RouteTransitOverviewSummary.duration required")
    return out


def redact_sensitive(value: RouteTransitOverviewSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "distance" in value:
        out["distance"] = "*** Sensitive Data Redacted ***"
    if "duration" in value:
        out["duration"] = "*** Sensitive Data Redacted ***"
    return out
