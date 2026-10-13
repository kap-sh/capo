"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleSpanList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_vehicle_span

RouteVehicleSpanList: TypeAlias = list[
    "capo_geo_routes.types.route_vehicle_span.RouteVehicleSpan"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleSpanList) -> list:
    import capo_geo_routes.types.route_vehicle_span

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_vehicle_span.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteVehicleSpanList:
    import capo_geo_routes.types.route_vehicle_span

    out: RouteVehicleSpanList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_vehicle_span.deserialize_json(item))
    return out


def redact_sensitive(value: RouteVehicleSpanList) -> list[Any]:
    import capo_geo_routes.types.route_vehicle_span

    return [
        capo_geo_routes.types.route_vehicle_span.redact_sensitive(item)
        for item in value
    ]
