"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalTravelStepList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_rental_travel_step

RouteRentalTravelStepList: TypeAlias = list[
    "capo_geo_routes.types.route_rental_travel_step.RouteRentalTravelStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalTravelStepList) -> list:
    import capo_geo_routes.types.route_rental_travel_step

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_rental_travel_step.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteRentalTravelStepList:
    import capo_geo_routes.types.route_rental_travel_step

    out: RouteRentalTravelStepList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_rental_travel_step.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RouteRentalTravelStepList) -> list[Any]:
    import capo_geo_routes.types.route_rental_travel_step

    return [
        capo_geo_routes.types.route_rental_travel_step.redact_sensitive(item)
        for item in value
    ]
