"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixDestinationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_matrix_destination

RouteMatrixDestinationList: TypeAlias = list[
    "capo_geo_routes.types.route_matrix_destination.RouteMatrixDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixDestinationList) -> list:
    import capo_geo_routes.types.route_matrix_destination

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_matrix_destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteMatrixDestinationList:
    import capo_geo_routes.types.route_matrix_destination

    out: RouteMatrixDestinationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_matrix_destination.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RouteMatrixDestinationList) -> list[Any]:
    import capo_geo_routes.types.route_matrix_destination

    return [
        capo_geo_routes.types.route_matrix_destination.redact_sensitive(item)
        for item in value
    ]
