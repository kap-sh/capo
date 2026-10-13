"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleIncident``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_vehicle_incident_severity
    import capo_geo_routes.types.route_vehicle_incident_type
    import capo_geo_routes.types.sensitive_string
    import capo_geo_routes.types.timestamp_with_timezone_offset


class RouteVehicleIncident(TypedDict, closed=True):
    description: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Brief readable description of the incident.</p>"""
    end_time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>End timestamp of the incident.</p>"""
    severity: NotRequired[
        "capo_geo_routes.types.route_vehicle_incident_severity.RouteVehicleIncidentSeverity"
    ]
    """<p>Severity of the incident Critical - The part of the route the incident affects is unusable. Major- Major impact on the leg duration, for example stop and go Minor- Minor impact on the leg duration, for example traffic jam Low - Low on duration, for example slightly increased traffic</p>"""
    start_time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>Start time of the incident.</p>"""
    type: NotRequired[
        "capo_geo_routes.types.route_vehicle_incident_type.RouteVehicleIncidentType"
    ]
    """<p>Type of the incident.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleIncident) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "end_time" in value:
        out["EndTime"] = value["end_time"]
    if "severity" in value:
        import capo_geo_routes.types.route_vehicle_incident_severity

        out["Severity"] = (
            capo_geo_routes.types.route_vehicle_incident_severity.serialize_json(
                value["severity"]
            )
        )
    if "start_time" in value:
        out["StartTime"] = value["start_time"]
    if "type" in value:
        import capo_geo_routes.types.route_vehicle_incident_type

        out["Type"] = capo_geo_routes.types.route_vehicle_incident_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> RouteVehicleIncident:
    out: RouteVehicleIncident = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EndTime") is not None:
        out["end_time"] = data["EndTime"]
    if data.get("Severity") is not None:
        import capo_geo_routes.types.route_vehicle_incident_severity

        out["severity"] = (
            capo_geo_routes.types.route_vehicle_incident_severity.deserialize_json(
                data["Severity"]
            )
        )
    if data.get("StartTime") is not None:
        out["start_time"] = data["StartTime"]
    if data.get("Type") is not None:
        import capo_geo_routes.types.route_vehicle_incident_type

        out["type"] = (
            capo_geo_routes.types.route_vehicle_incident_type.deserialize_json(
                data["Type"]
            )
        )
    return out


def redact_sensitive(value: RouteVehicleIncident) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "end_time" in value:
        out["end_time"] = "*** Sensitive Data Redacted ***"
    if "severity" in value:
        out["severity"] = "*** Sensitive Data Redacted ***"
    if "start_time" in value:
        out["start_time"] = "*** Sensitive Data Redacted ***"
    if "type" in value:
        out["type"] = "*** Sensitive Data Redacted ***"
    return out
