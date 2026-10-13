"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitModeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_transit_mode

RouteTransitModeList: TypeAlias = list[
    "capo_geo_routes.types.route_transit_mode.RouteTransitMode"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitModeList) -> list:
    import capo_geo_routes.types.route_transit_mode

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_transit_mode.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTransitModeList:
    import capo_geo_routes.types.route_transit_mode

    out: RouteTransitModeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_transit_mode.deserialize_json(item))
    return out


def redact_sensitive(value: RouteTransitModeList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
