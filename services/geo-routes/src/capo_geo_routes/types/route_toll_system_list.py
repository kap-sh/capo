"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollSystemList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_toll_system

RouteTollSystemList: TypeAlias = list[
    "capo_geo_routes.types.route_toll_system.RouteTollSystem"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollSystemList) -> list:
    import capo_geo_routes.types.route_toll_system

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_toll_system.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTollSystemList:
    import capo_geo_routes.types.route_toll_system

    out: RouteTollSystemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_toll_system.deserialize_json(item))
    return out


def redact_sensitive(value: RouteTollSystemList) -> list[Any]:
    import capo_geo_routes.types.route_toll_system

    return [
        capo_geo_routes.types.route_toll_system.redact_sensitive(item) for item in value
    ]
