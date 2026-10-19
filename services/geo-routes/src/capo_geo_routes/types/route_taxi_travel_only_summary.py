"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiTravelOnlySummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds


class RouteTaxiTravelOnlySummary(TypedDict, closed=True):
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the travel portion of the taxi leg.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiTravelOnlySummary) -> dict:
    out: dict = {}
    out["Duration"] = value["duration"]
    return out


def deserialize_json(data: dict) -> RouteTaxiTravelOnlySummary:
    out: RouteTaxiTravelOnlySummary = {}  # type: ignore[typeddict-item]
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    return out


def redact_sensitive(value: RouteTaxiTravelOnlySummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "duration" in value:
        out["duration"] = "*** Sensitive Data Redacted ***"
    return out
