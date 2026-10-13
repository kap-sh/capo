"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitIntermediateStopList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_transit_intermediate_stop

RouteTransitIntermediateStopList: TypeAlias = list[
    "capo_geo_routes.types.route_transit_intermediate_stop.RouteTransitIntermediateStop"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitIntermediateStopList) -> list:
    import capo_geo_routes.types.route_transit_intermediate_stop

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_transit_intermediate_stop.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteTransitIntermediateStopList:
    import capo_geo_routes.types.route_transit_intermediate_stop

    out: RouteTransitIntermediateStopList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_transit_intermediate_stop.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RouteTransitIntermediateStopList) -> list[Any]:
    import capo_geo_routes.types.route_transit_intermediate_stop

    return [
        capo_geo_routes.types.route_transit_intermediate_stop.redact_sensitive(item)
        for item in value
    ]
