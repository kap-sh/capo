"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitArrival``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.route_transit_place
    import capo_geo_routes.types.route_transit_trip_status
    import capo_geo_routes.types.timestamp_with_timezone_offset


class RouteTransitArrival(TypedDict, closed=True):
    delay: NotRequired["capo_geo_routes.types.duration_seconds.DurationSeconds"]
    """<p>The delay from the scheduled arrival time.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    place: "capo_geo_routes.types.route_transit_place.RouteTransitPlace"
    """<p>Place details corresponding to the arrival.</p>"""
    status: NotRequired[
        "capo_geo_routes.types.route_transit_trip_status.RouteTransitTripStatus"
    ]
    """<p>The status of the arrival.</p>"""
    time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>The arrival time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitArrival) -> dict:
    out: dict = {}
    if "delay" in value:
        out["Delay"] = value["delay"]
    import capo_geo_routes.types.route_transit_place

    out["Place"] = capo_geo_routes.types.route_transit_place.serialize_json(
        value["place"]
    )
    if "status" in value:
        import capo_geo_routes.types.route_transit_trip_status

        out["Status"] = capo_geo_routes.types.route_transit_trip_status.serialize_json(
            value["status"]
        )
    if "time" in value:
        out["Time"] = value["time"]
    return out


def deserialize_json(data: dict) -> RouteTransitArrival:
    out: RouteTransitArrival = {}  # type: ignore[typeddict-item]
    if data.get("Delay") is not None:
        out["delay"] = data["Delay"]
    if data.get("Place") is not None:
        import capo_geo_routes.types.route_transit_place

        out["place"] = capo_geo_routes.types.route_transit_place.deserialize_json(
            data["Place"]
        )
    else:
        raise DeserializationError("RouteTransitArrival.place required")
    if data.get("Status") is not None:
        import capo_geo_routes.types.route_transit_trip_status

        out["status"] = (
            capo_geo_routes.types.route_transit_trip_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("Time") is not None:
        out["time"] = data["Time"]
    return out


def redact_sensitive(value: RouteTransitArrival) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "delay" in value:
        out["delay"] = "*** Sensitive Data Redacted ***"
    if "place" in value:
        import capo_geo_routes.types.route_transit_place

        out["place"] = capo_geo_routes.types.route_transit_place.redact_sensitive(
            value["place"]
        )
    if "status" in value:
        out["status"] = "*** Sensitive Data Redacted ***"
    if "time" in value:
        out["time"] = "*** Sensitive Data Redacted ***"
    return out
