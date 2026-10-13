"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAvoidanceZoneCategoryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_avoidance_zone_category

RouteAvoidanceZoneCategoryList: TypeAlias = list[
    "capo_geo_routes.types.route_avoidance_zone_category.RouteAvoidanceZoneCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteAvoidanceZoneCategoryList) -> list:
    import capo_geo_routes.types.route_avoidance_zone_category

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_avoidance_zone_category.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteAvoidanceZoneCategoryList:
    import capo_geo_routes.types.route_avoidance_zone_category

    out: RouteAvoidanceZoneCategoryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_avoidance_zone_category.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RouteAvoidanceZoneCategoryList) -> list[Any]:
    import capo_geo_routes.types.route_avoidance_zone_category

    return [
        capo_geo_routes.types.route_avoidance_zone_category.redact_sensitive(item)
        for item in value
    ]
