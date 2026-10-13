"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route

RouteList: TypeAlias = list["capo_geo_routes.types.route.Route"]


# --- restJson1 ser/de ---
def serialize_json(value: RouteList) -> list:
    import capo_geo_routes.types.route

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteList:
    import capo_geo_routes.types.route

    out: RouteList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route.deserialize_json(item))
    return out


def redact_sensitive(value: RouteList) -> list[Any]:
    import capo_geo_routes.types.route

    return [capo_geo_routes.types.route.redact_sensitive(item) for item in value]
