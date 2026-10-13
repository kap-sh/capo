"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationDestinationOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.heading
    import capo_geo_routes.types.timestamp_with_timezone_offset
    import capo_geo_routes.types.waypoint_id
    import capo_geo_routes.types.waypoint_optimization_access_hours
    import capo_geo_routes.types.waypoint_optimization_side_of_street_options


class WaypointOptimizationDestinationOptions(TypedDict, closed=True):
    access_hours: NotRequired[
        "capo_geo_routes.types.waypoint_optimization_access_hours.WaypointOptimizationAccessHours"
    ]
    """<p>Access hours corresponding to when a waypoint can be visited.</p>"""
    appointment_time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>Appointment time at the destination.</p>"""
    heading: "capo_geo_routes.types.heading.Heading"
    """<p>GPS Heading at the position.</p>"""
    id: NotRequired["capo_geo_routes.types.waypoint_id.WaypointId"]
    """<p>The waypoint Id.</p>"""
    service_duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Service time spent at the destination. At an appointment, the service time should be the appointment duration.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    side_of_street: NotRequired[
        "capo_geo_routes.types.waypoint_optimization_side_of_street_options.WaypointOptimizationSideOfStreetOptions"
    ]
    """<p>Options to configure matching the provided position to a side of the street.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationDestinationOptions) -> dict:
    out: dict = {}
    if "access_hours" in value:
        import capo_geo_routes.types.waypoint_optimization_access_hours

        out["AccessHours"] = (
            capo_geo_routes.types.waypoint_optimization_access_hours.serialize_json(
                value["access_hours"]
            )
        )
    if "appointment_time" in value:
        out["AppointmentTime"] = value["appointment_time"]
    out["Heading"] = (
        "NaN"
        if value.get("heading", 0) != value.get("heading", 0)
        else "Infinity"
        if value.get("heading", 0) == float("inf")
        else "-Infinity"
        if value.get("heading", 0) == float("-inf")
        else value.get("heading", 0)
    )
    if "id" in value:
        out["Id"] = value["id"]
    out["ServiceDuration"] = value.get("service_duration", 0)
    if "side_of_street" in value:
        import capo_geo_routes.types.waypoint_optimization_side_of_street_options

        out["SideOfStreet"] = (
            capo_geo_routes.types.waypoint_optimization_side_of_street_options.serialize_json(
                value["side_of_street"]
            )
        )
    return out


def deserialize_json(data: dict) -> WaypointOptimizationDestinationOptions:
    out: WaypointOptimizationDestinationOptions = {}  # type: ignore[typeddict-item]
    if data.get("AccessHours") is not None:
        import capo_geo_routes.types.waypoint_optimization_access_hours

        out["access_hours"] = (
            capo_geo_routes.types.waypoint_optimization_access_hours.deserialize_json(
                data["AccessHours"]
            )
        )
    if data.get("AppointmentTime") is not None:
        out["appointment_time"] = data["AppointmentTime"]
    if data.get("Heading") is not None:
        out["heading"] = float(data["Heading"])
    else:
        out["heading"] = 0
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("ServiceDuration") is not None:
        out["service_duration"] = data["ServiceDuration"]
    else:
        out["service_duration"] = 0
    if data.get("SideOfStreet") is not None:
        import capo_geo_routes.types.waypoint_optimization_side_of_street_options

        out["side_of_street"] = (
            capo_geo_routes.types.waypoint_optimization_side_of_street_options.deserialize_json(
                data["SideOfStreet"]
            )
        )
    return out


def redact_sensitive(value: WaypointOptimizationDestinationOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_hours" in value:
        import capo_geo_routes.types.waypoint_optimization_access_hours

        out["access_hours"] = (
            capo_geo_routes.types.waypoint_optimization_access_hours.redact_sensitive(
                value["access_hours"]
            )
        )
    if "appointment_time" in value:
        out["appointment_time"] = "*** Sensitive Data Redacted ***"
    if "heading" in value:
        out["heading"] = "*** Sensitive Data Redacted ***"
    if "service_duration" in value:
        out["service_duration"] = "*** Sensitive Data Redacted ***"
    if "side_of_street" in value:
        import capo_geo_routes.types.waypoint_optimization_side_of_street_options

        out["side_of_street"] = (
            capo_geo_routes.types.waypoint_optimization_side_of_street_options.redact_sensitive(
                value["side_of_street"]
            )
        )
    return out
