"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransponderList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_transponder

RouteTransponderList: TypeAlias = list[
    "capo_geo_routes.types.route_transponder.RouteTransponder"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransponderList) -> list:
    import capo_geo_routes.types.route_transponder

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_transponder.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTransponderList:
    import capo_geo_routes.types.route_transponder

    out: RouteTransponderList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_transponder.deserialize_json(item))
    return out


def redact_sensitive(value: RouteTransponderList) -> list[Any]:
    import capo_geo_routes.types.route_transponder

    return [
        capo_geo_routes.types.route_transponder.redact_sensitive(item) for item in value
    ]
