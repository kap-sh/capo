"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitNextDepartureList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_transit_next_departure

RouteTransitNextDepartureList: TypeAlias = list[
    "capo_geo_routes.types.route_transit_next_departure.RouteTransitNextDeparture"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitNextDepartureList) -> list:
    import capo_geo_routes.types.route_transit_next_departure

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_transit_next_departure.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteTransitNextDepartureList:
    import capo_geo_routes.types.route_transit_next_departure

    out: RouteTransitNextDepartureList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_transit_next_departure.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RouteTransitNextDepartureList) -> list[Any]:
    import capo_geo_routes.types.route_transit_next_departure

    return [
        capo_geo_routes.types.route_transit_next_departure.redact_sensitive(item)
        for item in value
    ]
