"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixAvoidanceZoneCategoryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_matrix_avoidance_zone_category

RouteMatrixAvoidanceZoneCategoryList: TypeAlias = list[
    "capo_geo_routes.types.route_matrix_avoidance_zone_category.RouteMatrixAvoidanceZoneCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixAvoidanceZoneCategoryList) -> list:
    import capo_geo_routes.types.route_matrix_avoidance_zone_category

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_matrix_avoidance_zone_category.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RouteMatrixAvoidanceZoneCategoryList:
    import capo_geo_routes.types.route_matrix_avoidance_zone_category

    out: RouteMatrixAvoidanceZoneCategoryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_matrix_avoidance_zone_category.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: RouteMatrixAvoidanceZoneCategoryList) -> list[Any]:
    import capo_geo_routes.types.route_matrix_avoidance_zone_category

    return [
        capo_geo_routes.types.route_matrix_avoidance_zone_category.redact_sensitive(
            item
        )
        for item in value
    ]
