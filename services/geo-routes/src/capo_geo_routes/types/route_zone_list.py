"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteZoneList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_zone

RouteZoneList: TypeAlias = list["capo_geo_routes.types.route_zone.RouteZone"]


# --- restJson1 ser/de ---
def serialize_json(value: RouteZoneList) -> list:
    import capo_geo_routes.types.route_zone

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_zone.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteZoneList:
    import capo_geo_routes.types.route_zone

    out: RouteZoneList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_zone.deserialize_json(item))
    return out


def redact_sensitive(value: RouteZoneList) -> list[Any]:
    import capo_geo_routes.types.route_zone

    return [capo_geo_routes.types.route_zone.redact_sensitive(item) for item in value]
