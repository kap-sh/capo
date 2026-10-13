"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteLegList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_leg

RouteLegList: TypeAlias = list["capo_geo_routes.types.route_leg.RouteLeg"]


# --- restJson1 ser/de ---
def serialize_json(value: RouteLegList) -> list:
    import capo_geo_routes.types.route_leg

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_leg.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteLegList:
    import capo_geo_routes.types.route_leg

    out: RouteLegList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_leg.deserialize_json(item))
    return out


def redact_sensitive(value: RouteLegList) -> list[Any]:
    import capo_geo_routes.types.route_leg

    return [capo_geo_routes.types.route_leg.redact_sensitive(item) for item in value]
