"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationTimeBreakdown``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds


class WaypointOptimizationTimeBreakdown(TypedDict, closed=True):
    rest_duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Resting phase of the cycle.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    service_duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Service time spent at the destination. At an appointment, the service time should be the appointment duration.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    travel_duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Traveling phase of the cycle.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    wait_duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Waiting phase of the cycle.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationTimeBreakdown) -> dict:
    out: dict = {}
    out["RestDuration"] = value.get("rest_duration", 0)
    out["ServiceDuration"] = value.get("service_duration", 0)
    out["TravelDuration"] = value.get("travel_duration", 0)
    out["WaitDuration"] = value.get("wait_duration", 0)
    return out


def deserialize_json(data: dict) -> WaypointOptimizationTimeBreakdown:
    out: WaypointOptimizationTimeBreakdown = {}  # type: ignore[typeddict-item]
    if data.get("RestDuration") is not None:
        out["rest_duration"] = data["RestDuration"]
    else:
        out["rest_duration"] = 0
    if data.get("ServiceDuration") is not None:
        out["service_duration"] = data["ServiceDuration"]
    else:
        out["service_duration"] = 0
    if data.get("TravelDuration") is not None:
        out["travel_duration"] = data["TravelDuration"]
    else:
        out["travel_duration"] = 0
    if data.get("WaitDuration") is not None:
        out["wait_duration"] = data["WaitDuration"]
    else:
        out["wait_duration"] = 0
    return out


def redact_sensitive(value: WaypointOptimizationTimeBreakdown) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rest_duration" in value:
        out["rest_duration"] = "*** Sensitive Data Redacted ***"
    if "service_duration" in value:
        out["service_duration"] = "*** Sensitive Data Redacted ***"
    if "travel_duration" in value:
        out["travel_duration"] = "*** Sensitive Data Redacted ***"
    if "wait_duration" in value:
        out["wait_duration"] = "*** Sensitive Data Redacted ***"
    return out
