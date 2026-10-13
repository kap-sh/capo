"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleModeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_vehicle_mode

RouteVehicleModeList: TypeAlias = list[
    "capo_geo_routes.types.route_vehicle_mode.RouteVehicleMode"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleModeList) -> list:
    import capo_geo_routes.types.route_vehicle_mode

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_vehicle_mode.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteVehicleModeList:
    import capo_geo_routes.types.route_vehicle_mode

    out: RouteVehicleModeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_vehicle_mode.deserialize_json(item))
    return out


def redact_sensitive(value: RouteVehicleModeList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
