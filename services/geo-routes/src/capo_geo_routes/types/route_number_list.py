"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteNumberList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_number

RouteNumberList: TypeAlias = list["capo_geo_routes.types.route_number.RouteNumber"]


# --- restJson1 ser/de ---
def serialize_json(value: RouteNumberList) -> list:
    import capo_geo_routes.types.route_number

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_number.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteNumberList:
    import capo_geo_routes.types.route_number

    out: RouteNumberList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_number.deserialize_json(item))
    return out


def redact_sensitive(value: RouteNumberList) -> list[Any]:
    import capo_geo_routes.types.route_number

    return [capo_geo_routes.types.route_number.redact_sensitive(item) for item in value]
