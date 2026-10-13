"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryAfterTravelStepList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_ferry_after_travel_step

RouteFerryAfterTravelStepList: TypeAlias = list[
    "capo_geo_routes.types.route_ferry_after_travel_step.RouteFerryAfterTravelStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerryAfterTravelStepList) -> list:
    import capo_geo_routes.types.route_ferry_after_travel_step

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_ferry_after_travel_step.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteFerryAfterTravelStepList:
    import capo_geo_routes.types.route_ferry_after_travel_step

    out: RouteFerryAfterTravelStepList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_ferry_after_travel_step.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RouteFerryAfterTravelStepList) -> list[Any]:
    import capo_geo_routes.types.route_ferry_after_travel_step

    return [
        capo_geo_routes.types.route_ferry_after_travel_step.redact_sensitive(item)
        for item in value
    ]
