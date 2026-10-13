"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationConnection``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.waypoint_id

WaypointOptimizationConnection = TypedDict(
    "WaypointOptimizationConnection",
    {
        "distance": "capo_geo_routes.types.distance_meters.DistanceMeters",
        "from": "capo_geo_routes.types.waypoint_id.WaypointId",
        "rest_duration": "capo_geo_routes.types.duration_seconds.DurationSeconds",
        "to": "capo_geo_routes.types.waypoint_id.WaypointId",
        "travel_duration": "capo_geo_routes.types.duration_seconds.DurationSeconds",
        "wait_duration": "capo_geo_routes.types.duration_seconds.DurationSeconds",
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationConnection) -> dict:
    out: dict = {}
    out["Distance"] = value.get("distance", 0)
    out["From"] = value["from"]
    out["RestDuration"] = value.get("rest_duration", 0)
    out["To"] = value["to"]
    out["TravelDuration"] = value.get("travel_duration", 0)
    out["WaitDuration"] = value.get("wait_duration", 0)
    return out


def deserialize_json(data: dict) -> WaypointOptimizationConnection:
    out: WaypointOptimizationConnection = {}  # type: ignore[typeddict-item]
    if data.get("Distance") is not None:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if data.get("From") is not None:
        out["from"] = data["From"]
    else:
        raise DeserializationError("WaypointOptimizationConnection.from required")
    if data.get("RestDuration") is not None:
        out["rest_duration"] = data["RestDuration"]
    else:
        out["rest_duration"] = 0
    if data.get("To") is not None:
        out["to"] = data["To"]
    else:
        raise DeserializationError("WaypointOptimizationConnection.to required")
    if data.get("TravelDuration") is not None:
        out["travel_duration"] = data["TravelDuration"]
    else:
        out["travel_duration"] = 0
    if data.get("WaitDuration") is not None:
        out["wait_duration"] = data["WaitDuration"]
    else:
        out["wait_duration"] = 0
    return out


def redact_sensitive(value: WaypointOptimizationConnection) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "distance" in value:
        out["distance"] = "*** Sensitive Data Redacted ***"
    if "rest_duration" in value:
        out["rest_duration"] = "*** Sensitive Data Redacted ***"
    if "travel_duration" in value:
        out["travel_duration"] = "*** Sensitive Data Redacted ***"
    if "wait_duration" in value:
        out["wait_duration"] = "*** Sensitive Data Redacted ***"
    return out
