"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationRestCycleDurations``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds


class WaypointOptimizationRestCycleDurations(TypedDict, closed=True):
    rest_duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Resting phase of the cycle.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    work_duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Working phase of the cycle.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationRestCycleDurations) -> dict:
    out: dict = {}
    out["RestDuration"] = value.get("rest_duration", 0)
    out["WorkDuration"] = value.get("work_duration", 0)
    return out


def deserialize_json(data: dict) -> WaypointOptimizationRestCycleDurations:
    out: WaypointOptimizationRestCycleDurations = {}  # type: ignore[typeddict-item]
    if data.get("RestDuration") is not None:
        out["rest_duration"] = data["RestDuration"]
    else:
        out["rest_duration"] = 0
    if data.get("WorkDuration") is not None:
        out["work_duration"] = data["WorkDuration"]
    else:
        out["work_duration"] = 0
    return out


def redact_sensitive(value: WaypointOptimizationRestCycleDurations) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rest_duration" in value:
        out["rest_duration"] = "*** Sensitive Data Redacted ***"
    if "work_duration" in value:
        out["work_duration"] = "*** Sensitive Data Redacted ***"
    return out
