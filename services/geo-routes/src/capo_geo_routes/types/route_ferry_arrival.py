"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryArrival``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.route_ferry_place
    import capo_geo_routes.types.timestamp_with_timezone_offset


class RouteFerryArrival(TypedDict, closed=True):
    place: "capo_geo_routes.types.route_ferry_place.RouteFerryPlace"
    """<p>Place details corresponding to the arrival.</p>"""
    time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>The arrival time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerryArrival) -> dict:
    out: dict = {}
    import capo_geo_routes.types.route_ferry_place

    out["Place"] = capo_geo_routes.types.route_ferry_place.serialize_json(
        value["place"]
    )
    if "time" in value:
        out["Time"] = value["time"]
    return out


def deserialize_json(data: dict) -> RouteFerryArrival:
    out: RouteFerryArrival = {}  # type: ignore[typeddict-item]
    if data.get("Place") is not None:
        import capo_geo_routes.types.route_ferry_place

        out["place"] = capo_geo_routes.types.route_ferry_place.deserialize_json(
            data["Place"]
        )
    else:
        raise DeserializationError("RouteFerryArrival.place required")
    if data.get("Time") is not None:
        out["time"] = data["Time"]
    return out


def redact_sensitive(value: RouteFerryArrival) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "place" in value:
        import capo_geo_routes.types.route_ferry_place

        out["place"] = capo_geo_routes.types.route_ferry_place.redact_sensitive(
            value["place"]
        )
    if "time" in value:
        out["time"] = "*** Sensitive Data Redacted ***"
    return out
