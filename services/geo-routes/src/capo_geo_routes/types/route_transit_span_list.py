"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitSpanList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_transit_span

RouteTransitSpanList: TypeAlias = list[
    "capo_geo_routes.types.route_transit_span.RouteTransitSpan"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitSpanList) -> list:
    import capo_geo_routes.types.route_transit_span

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_transit_span.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTransitSpanList:
    import capo_geo_routes.types.route_transit_span

    out: RouteTransitSpanList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_transit_span.deserialize_json(item))
    return out


def redact_sensitive(value: RouteTransitSpanList) -> list[Any]:
    import capo_geo_routes.types.route_transit_span

    return [
        capo_geo_routes.types.route_transit_span.redact_sensitive(item)
        for item in value
    ]
