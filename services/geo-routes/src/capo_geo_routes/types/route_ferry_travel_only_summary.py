"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryTravelOnlySummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds


class RouteFerryTravelOnlySummary(TypedDict, closed=True):
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Total duration in free flowing traffic, which is the best case or shortest duration possible to cover the leg.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerryTravelOnlySummary) -> dict:
    out: dict = {}
    out["Duration"] = value.get("duration", 0)
    return out


def deserialize_json(data: dict) -> RouteFerryTravelOnlySummary:
    out: RouteFerryTravelOnlySummary = {}  # type: ignore[typeddict-item]
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    return out


def redact_sensitive(value: RouteFerryTravelOnlySummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "duration" in value:
        out["duration"] = "*** Sensitive Data Redacted ***"
    return out
