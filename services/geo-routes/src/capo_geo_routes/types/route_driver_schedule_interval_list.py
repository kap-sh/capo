"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteDriverScheduleIntervalList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_driver_schedule_interval

RouteDriverScheduleIntervalList: TypeAlias = list[
    "capo_geo_routes.types.route_driver_schedule_interval.RouteDriverScheduleInterval"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteDriverScheduleIntervalList) -> list:
    import capo_geo_routes.types.route_driver_schedule_interval

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_driver_schedule_interval.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteDriverScheduleIntervalList:
    import capo_geo_routes.types.route_driver_schedule_interval

    out: RouteDriverScheduleIntervalList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_driver_schedule_interval.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RouteDriverScheduleIntervalList) -> list[Any]:
    import capo_geo_routes.types.route_driver_schedule_interval

    return [
        capo_geo_routes.types.route_driver_schedule_interval.redact_sensitive(item)
        for item in value
    ]
