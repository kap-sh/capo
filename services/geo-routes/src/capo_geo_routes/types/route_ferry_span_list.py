"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerrySpanList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_ferry_span

RouteFerrySpanList: TypeAlias = list[
    "capo_geo_routes.types.route_ferry_span.RouteFerrySpan"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerrySpanList) -> list:
    import capo_geo_routes.types.route_ferry_span

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_ferry_span.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteFerrySpanList:
    import capo_geo_routes.types.route_ferry_span

    out: RouteFerrySpanList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_ferry_span.deserialize_json(item))
    return out


def redact_sensitive(value: RouteFerrySpanList) -> list[Any]:
    import capo_geo_routes.types.route_ferry_span

    return [
        capo_geo_routes.types.route_ferry_span.redact_sensitive(item) for item in value
    ]
