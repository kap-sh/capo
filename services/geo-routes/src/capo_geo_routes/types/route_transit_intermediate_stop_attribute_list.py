"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitIntermediateStopAttributeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_transit_intermediate_stop_attribute

RouteTransitIntermediateStopAttributeList: TypeAlias = list[
    "capo_geo_routes.types.route_transit_intermediate_stop_attribute.RouteTransitIntermediateStopAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitIntermediateStopAttributeList) -> list:
    import capo_geo_routes.types.route_transit_intermediate_stop_attribute

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_transit_intermediate_stop_attribute.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RouteTransitIntermediateStopAttributeList:
    import capo_geo_routes.types.route_transit_intermediate_stop_attribute

    out: RouteTransitIntermediateStopAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_transit_intermediate_stop_attribute.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: RouteTransitIntermediateStopAttributeList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
