"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitNextDeparture``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.route_transit_transport_mode_details
    import capo_geo_routes.types.route_transit_trip_status
    import capo_geo_routes.types.sensitive_string
    import capo_geo_routes.types.timestamp_with_timezone_offset


class RouteTransitNextDeparture(TypedDict, closed=True):
    delay: NotRequired["capo_geo_routes.types.duration_seconds.DurationSeconds"]
    """<p>The delay from the scheduled departure time.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    platform_name: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Platform name or number for the departure.</p>"""
    status: NotRequired[
        "capo_geo_routes.types.route_transit_trip_status.RouteTransitTripStatus"
    ]
    """<p>The status of the departure.</p>"""
    time: "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    """<p>The departure time.</p>"""
    transport: NotRequired[
        "capo_geo_routes.types.route_transit_transport_mode_details.RouteTransitTransportModeDetails"
    ]
    """<p>Transport mode details for this departure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitNextDeparture) -> dict:
    out: dict = {}
    if "delay" in value:
        out["Delay"] = value["delay"]
    if "platform_name" in value:
        out["PlatformName"] = value["platform_name"]
    if "status" in value:
        import capo_geo_routes.types.route_transit_trip_status

        out["Status"] = capo_geo_routes.types.route_transit_trip_status.serialize_json(
            value["status"]
        )
    out["Time"] = value["time"]
    if "transport" in value:
        import capo_geo_routes.types.route_transit_transport_mode_details

        out["Transport"] = (
            capo_geo_routes.types.route_transit_transport_mode_details.serialize_json(
                value["transport"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteTransitNextDeparture:
    out: RouteTransitNextDeparture = {}  # type: ignore[typeddict-item]
    if data.get("Delay") is not None:
        out["delay"] = data["Delay"]
    if data.get("PlatformName") is not None:
        out["platform_name"] = data["PlatformName"]
    if data.get("Status") is not None:
        import capo_geo_routes.types.route_transit_trip_status

        out["status"] = (
            capo_geo_routes.types.route_transit_trip_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("Time") is not None:
        out["time"] = data["Time"]
    else:
        out["time"] = ""
    if data.get("Transport") is not None:
        import capo_geo_routes.types.route_transit_transport_mode_details

        out["transport"] = (
            capo_geo_routes.types.route_transit_transport_mode_details.deserialize_json(
                data["Transport"]
            )
        )
    return out


def redact_sensitive(value: RouteTransitNextDeparture) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "delay" in value:
        out["delay"] = "*** Sensitive Data Redacted ***"
    if "platform_name" in value:
        out["platform_name"] = "*** Sensitive Data Redacted ***"
    if "status" in value:
        out["status"] = "*** Sensitive Data Redacted ***"
    if "time" in value:
        out["time"] = "*** Sensitive Data Redacted ***"
    if "transport" in value:
        import capo_geo_routes.types.route_transit_transport_mode_details

        out["transport"] = (
            capo_geo_routes.types.route_transit_transport_mode_details.redact_sensitive(
                value["transport"]
            )
        )
    return out
