"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalOverviewSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.duration_seconds


class RouteRentalOverviewSummary(TypedDict, closed=True):
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the entire leg.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    distance: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Distance of the entire leg.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalOverviewSummary) -> dict:
    out: dict = {}
    out["Duration"] = value["duration"]
    out["Distance"] = value["distance"]
    return out


def deserialize_json(data: dict) -> RouteRentalOverviewSummary:
    out: RouteRentalOverviewSummary = {}  # type: ignore[typeddict-item]
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("RouteRentalOverviewSummary.duration required")
    if data.get("Distance") is not None:
        out["distance"] = data["Distance"]
    else:
        raise DeserializationError("RouteRentalOverviewSummary.distance required")
    return out


def redact_sensitive(value: RouteRentalOverviewSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "duration" in value:
        out["duration"] = "*** Sensitive Data Redacted ***"
    if "distance" in value:
        out["distance"] = "*** Sensitive Data Redacted ***"
    return out
