"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleNoticeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_vehicle_notice

RouteVehicleNoticeList: TypeAlias = list[
    "capo_geo_routes.types.route_vehicle_notice.RouteVehicleNotice"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleNoticeList) -> list:
    import capo_geo_routes.types.route_vehicle_notice

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_vehicle_notice.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteVehicleNoticeList:
    import capo_geo_routes.types.route_vehicle_notice

    out: RouteVehicleNoticeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_vehicle_notice.deserialize_json(item))
    return out


def redact_sensitive(value: RouteVehicleNoticeList) -> list[Any]:
    import capo_geo_routes.types.route_vehicle_notice

    return [
        capo_geo_routes.types.route_vehicle_notice.redact_sensitive(item)
        for item in value
    ]
