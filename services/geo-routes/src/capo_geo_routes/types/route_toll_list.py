"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_toll

RouteTollList: TypeAlias = list["capo_geo_routes.types.route_toll.RouteToll"]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollList) -> list:
    import capo_geo_routes.types.route_toll

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_toll.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTollList:
    import capo_geo_routes.types.route_toll

    out: RouteTollList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_toll.deserialize_json(item))
    return out


def redact_sensitive(value: RouteTollList) -> list[Any]:
    import capo_geo_routes.types.route_toll

    return [capo_geo_routes.types.route_toll.redact_sensitive(item) for item in value]
