"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalDeparture``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.route_rental_place
    import capo_geo_routes.types.timestamp_with_timezone_offset


class RouteRentalDeparture(TypedDict, closed=True):
    place: "capo_geo_routes.types.route_rental_place.RouteRentalPlace"
    """<p>Place details corresponding to the departure.</p>"""
    time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>The departure time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalDeparture) -> dict:
    out: dict = {}
    import capo_geo_routes.types.route_rental_place

    out["Place"] = capo_geo_routes.types.route_rental_place.serialize_json(
        value["place"]
    )
    if "time" in value:
        out["Time"] = value["time"]
    return out


def deserialize_json(data: dict) -> RouteRentalDeparture:
    out: RouteRentalDeparture = {}  # type: ignore[typeddict-item]
    if data.get("Place") is not None:
        import capo_geo_routes.types.route_rental_place

        out["place"] = capo_geo_routes.types.route_rental_place.deserialize_json(
            data["Place"]
        )
    else:
        raise DeserializationError("RouteRentalDeparture.place required")
    if data.get("Time") is not None:
        out["time"] = data["Time"]
    return out


def redact_sensitive(value: RouteRentalDeparture) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "place" in value:
        import capo_geo_routes.types.route_rental_place

        out["place"] = capo_geo_routes.types.route_rental_place.redact_sensitive(
            value["place"]
        )
    if "time" in value:
        out["time"] = "*** Sensitive Data Redacted ***"
    return out
