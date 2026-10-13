"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixAvoidanceAreaList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_matrix_avoidance_area

RouteMatrixAvoidanceAreaList: TypeAlias = list[
    "capo_geo_routes.types.route_matrix_avoidance_area.RouteMatrixAvoidanceArea"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixAvoidanceAreaList) -> list:
    import capo_geo_routes.types.route_matrix_avoidance_area

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_matrix_avoidance_area.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteMatrixAvoidanceAreaList:
    import capo_geo_routes.types.route_matrix_avoidance_area

    out: RouteMatrixAvoidanceAreaList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_matrix_avoidance_area.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RouteMatrixAvoidanceAreaList) -> list[Any]:
    import capo_geo_routes.types.route_matrix_avoidance_area

    return [
        capo_geo_routes.types.route_matrix_avoidance_area.redact_sensitive(item)
        for item in value
    ]
