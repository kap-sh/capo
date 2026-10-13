"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixOriginList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_matrix_origin

RouteMatrixOriginList: TypeAlias = list[
    "capo_geo_routes.types.route_matrix_origin.RouteMatrixOrigin"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixOriginList) -> list:
    import capo_geo_routes.types.route_matrix_origin

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_matrix_origin.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteMatrixOriginList:
    import capo_geo_routes.types.route_matrix_origin

    out: RouteMatrixOriginList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_matrix_origin.deserialize_json(item))
    return out


def redact_sensitive(value: RouteMatrixOriginList) -> list[Any]:
    import capo_geo_routes.types.route_matrix_origin

    return [
        capo_geo_routes.types.route_matrix_origin.redact_sensitive(item)
        for item in value
    ]
