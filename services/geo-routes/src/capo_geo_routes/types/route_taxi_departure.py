"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiDeparture``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.route_taxi_place
    import capo_geo_routes.types.timestamp_with_timezone_offset


class RouteTaxiDeparture(TypedDict, closed=True):
    place: "capo_geo_routes.types.route_taxi_place.RouteTaxiPlace"
    """<p>Place details corresponding to the departure.</p>"""
    time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>The departure time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiDeparture) -> dict:
    out: dict = {}
    import capo_geo_routes.types.route_taxi_place

    out["Place"] = capo_geo_routes.types.route_taxi_place.serialize_json(value["place"])
    if "time" in value:
        out["Time"] = value["time"]
    return out


def deserialize_json(data: dict) -> RouteTaxiDeparture:
    out: RouteTaxiDeparture = {}  # type: ignore[typeddict-item]
    if data.get("Place") is not None:
        import capo_geo_routes.types.route_taxi_place

        out["place"] = capo_geo_routes.types.route_taxi_place.deserialize_json(
            data["Place"]
        )
    else:
        raise DeserializationError("RouteTaxiDeparture.place required")
    if data.get("Time") is not None:
        out["time"] = data["Time"]
    return out


def redact_sensitive(value: RouteTaxiDeparture) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "place" in value:
        import capo_geo_routes.types.route_taxi_place

        out["place"] = capo_geo_routes.types.route_taxi_place.redact_sensitive(
            value["place"]
        )
    if "time" in value:
        out["time"] = "*** Sensitive Data Redacted ***"
    return out
