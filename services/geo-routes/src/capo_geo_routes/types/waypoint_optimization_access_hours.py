"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationAccessHours``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.waypoint_optimization_access_hours_entry

WaypointOptimizationAccessHours = TypedDict(
    "WaypointOptimizationAccessHours",
    {
        "from": "capo_geo_routes.types.waypoint_optimization_access_hours_entry.WaypointOptimizationAccessHoursEntry",
        "to": "capo_geo_routes.types.waypoint_optimization_access_hours_entry.WaypointOptimizationAccessHoursEntry",
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationAccessHours) -> dict:
    out: dict = {}
    import capo_geo_routes.types.waypoint_optimization_access_hours_entry

    out["From"] = (
        capo_geo_routes.types.waypoint_optimization_access_hours_entry.serialize_json(
            value["from"]
        )
    )
    import capo_geo_routes.types.waypoint_optimization_access_hours_entry

    out["To"] = (
        capo_geo_routes.types.waypoint_optimization_access_hours_entry.serialize_json(
            value["to"]
        )
    )
    return out


def deserialize_json(data: dict) -> WaypointOptimizationAccessHours:
    out: WaypointOptimizationAccessHours = {}  # type: ignore[typeddict-item]
    if data.get("From") is not None:
        import capo_geo_routes.types.waypoint_optimization_access_hours_entry

        out["from"] = (
            capo_geo_routes.types.waypoint_optimization_access_hours_entry.deserialize_json(
                data["From"]
            )
        )
    else:
        raise DeserializationError("WaypointOptimizationAccessHours.from required")
    if data.get("To") is not None:
        import capo_geo_routes.types.waypoint_optimization_access_hours_entry

        out["to"] = (
            capo_geo_routes.types.waypoint_optimization_access_hours_entry.deserialize_json(
                data["To"]
            )
        )
    else:
        raise DeserializationError("WaypointOptimizationAccessHours.to required")
    return out


def redact_sensitive(value: WaypointOptimizationAccessHours) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "from" in value:
        import capo_geo_routes.types.waypoint_optimization_access_hours_entry

        out["from"] = (
            capo_geo_routes.types.waypoint_optimization_access_hours_entry.redact_sensitive(
                value["from"]
            )
        )
    if "to" in value:
        import capo_geo_routes.types.waypoint_optimization_access_hours_entry

        out["to"] = (
            capo_geo_routes.types.waypoint_optimization_access_hours_entry.redact_sensitive(
                value["to"]
            )
        )
    return out
