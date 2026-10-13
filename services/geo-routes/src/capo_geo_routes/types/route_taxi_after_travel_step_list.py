"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiAfterTravelStepList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_taxi_after_travel_step

RouteTaxiAfterTravelStepList: TypeAlias = list[
    "capo_geo_routes.types.route_taxi_after_travel_step.RouteTaxiAfterTravelStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiAfterTravelStepList) -> list:
    import capo_geo_routes.types.route_taxi_after_travel_step

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_taxi_after_travel_step.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteTaxiAfterTravelStepList:
    import capo_geo_routes.types.route_taxi_after_travel_step

    out: RouteTaxiAfterTravelStepList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_taxi_after_travel_step.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RouteTaxiAfterTravelStepList) -> list[Any]:
    import capo_geo_routes.types.route_taxi_after_travel_step

    return [
        capo_geo_routes.types.route_taxi_after_travel_step.redact_sensitive(item)
        for item in value
    ]
