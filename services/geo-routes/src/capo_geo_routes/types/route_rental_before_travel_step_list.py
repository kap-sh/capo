"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalBeforeTravelStepList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_rental_before_travel_step

RouteRentalBeforeTravelStepList: TypeAlias = list[
    "capo_geo_routes.types.route_rental_before_travel_step.RouteRentalBeforeTravelStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalBeforeTravelStepList) -> list:
    import capo_geo_routes.types.route_rental_before_travel_step

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_rental_before_travel_step.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteRentalBeforeTravelStepList:
    import capo_geo_routes.types.route_rental_before_travel_step

    out: RouteRentalBeforeTravelStepList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_rental_before_travel_step.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RouteRentalBeforeTravelStepList) -> list[Any]:
    import capo_geo_routes.types.route_rental_before_travel_step

    return [
        capo_geo_routes.types.route_rental_before_travel_step.redact_sensitive(item)
        for item in value
    ]
