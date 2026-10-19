"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitIncident``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_transit_incident_effect
    import capo_geo_routes.types.route_transit_incident_type
    import capo_geo_routes.types.sensitive_string
    import capo_geo_routes.types.timestamp_with_timezone_offset


class RouteTransitIncident(TypedDict, closed=True):
    description: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>A human readable description of the incident.</p>"""
    effect: (
        "capo_geo_routes.types.route_transit_incident_effect.RouteTransitIncidentEffect"
    )
    """<p>The effect of the incident on the transit service.</p>"""
    end_time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>The end time of the incident.</p>"""
    start_time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>The start time of the incident.</p>"""
    type: "capo_geo_routes.types.route_transit_incident_type.RouteTransitIncidentType"
    """<p>Type of the incident.</p>"""
    url: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>URL to the original incident published at the agency website.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitIncident) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import capo_geo_routes.types.route_transit_incident_effect

    out["Effect"] = capo_geo_routes.types.route_transit_incident_effect.serialize_json(
        value["effect"]
    )
    if "end_time" in value:
        out["EndTime"] = value["end_time"]
    if "start_time" in value:
        out["StartTime"] = value["start_time"]
    import capo_geo_routes.types.route_transit_incident_type

    out["Type"] = capo_geo_routes.types.route_transit_incident_type.serialize_json(
        value["type"]
    )
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> RouteTransitIncident:
    out: RouteTransitIncident = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Effect") is not None:
        import capo_geo_routes.types.route_transit_incident_effect

        out["effect"] = (
            capo_geo_routes.types.route_transit_incident_effect.deserialize_json(
                data["Effect"]
            )
        )
    else:
        import typing

        out["effect"] = typing.cast(
            "capo_geo_routes.types.route_transit_incident_effect.RouteTransitIncidentEffect",
            "",
        )
    if data.get("EndTime") is not None:
        out["end_time"] = data["EndTime"]
    if data.get("StartTime") is not None:
        out["start_time"] = data["StartTime"]
    if data.get("Type") is not None:
        import capo_geo_routes.types.route_transit_incident_type

        out["type"] = (
            capo_geo_routes.types.route_transit_incident_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_geo_routes.types.route_transit_incident_type.RouteTransitIncidentType",
            "",
        )
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    return out


def redact_sensitive(value: RouteTransitIncident) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "effect" in value:
        out["effect"] = "*** Sensitive Data Redacted ***"
    if "end_time" in value:
        out["end_time"] = "*** Sensitive Data Redacted ***"
    if "start_time" in value:
        out["start_time"] = "*** Sensitive Data Redacted ***"
    if "type" in value:
        out["type"] = "*** Sensitive Data Redacted ***"
    if "url" in value:
        out["url"] = "*** Sensitive Data Redacted ***"
    return out
