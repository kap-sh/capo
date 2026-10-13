"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianSpanList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_pedestrian_span

RoutePedestrianSpanList: TypeAlias = list[
    "capo_geo_routes.types.route_pedestrian_span.RoutePedestrianSpan"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutePedestrianSpanList) -> list:
    import capo_geo_routes.types.route_pedestrian_span

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_pedestrian_span.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoutePedestrianSpanList:
    import capo_geo_routes.types.route_pedestrian_span

    out: RoutePedestrianSpanList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_pedestrian_span.deserialize_json(item))
    return out


def redact_sensitive(value: RoutePedestrianSpanList) -> list[Any]:
    import capo_geo_routes.types.route_pedestrian_span

    return [
        capo_geo_routes.types.route_pedestrian_span.redact_sensitive(item)
        for item in value
    ]
