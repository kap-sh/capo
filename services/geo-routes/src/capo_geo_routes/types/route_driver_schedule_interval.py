"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteDriverScheduleInterval``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds


class RouteDriverScheduleInterval(TypedDict, closed=True):
    drive_duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Maximum allowed driving time before stopping to rest.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    rest_duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Resting time before the driver can continue driving.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteDriverScheduleInterval) -> dict:
    out: dict = {}
    out["DriveDuration"] = value.get("drive_duration", 0)
    out["RestDuration"] = value.get("rest_duration", 0)
    return out


def deserialize_json(data: dict) -> RouteDriverScheduleInterval:
    out: RouteDriverScheduleInterval = {}  # type: ignore[typeddict-item]
    if data.get("DriveDuration") is not None:
        out["drive_duration"] = data["DriveDuration"]
    else:
        out["drive_duration"] = 0
    if data.get("RestDuration") is not None:
        out["rest_duration"] = data["RestDuration"]
    else:
        out["rest_duration"] = 0
    return out


def redact_sensitive(value: RouteDriverScheduleInterval) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "drive_duration" in value:
        out["drive_duration"] = "*** Sensitive Data Redacted ***"
    if "rest_duration" in value:
        out["rest_duration"] = "*** Sensitive Data Redacted ***"
    return out
