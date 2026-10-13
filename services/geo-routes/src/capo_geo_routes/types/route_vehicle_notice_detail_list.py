"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleNoticeDetailList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_vehicle_notice_detail

RouteVehicleNoticeDetailList: TypeAlias = list[
    "capo_geo_routes.types.route_vehicle_notice_detail.RouteVehicleNoticeDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleNoticeDetailList) -> list:
    import capo_geo_routes.types.route_vehicle_notice_detail

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_vehicle_notice_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteVehicleNoticeDetailList:
    import capo_geo_routes.types.route_vehicle_notice_detail

    out: RouteVehicleNoticeDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_vehicle_notice_detail.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RouteVehicleNoticeDetailList) -> list[Any]:
    import capo_geo_routes.types.route_vehicle_notice_detail

    return [
        capo_geo_routes.types.route_vehicle_notice_detail.redact_sensitive(item)
        for item in value
    ]
