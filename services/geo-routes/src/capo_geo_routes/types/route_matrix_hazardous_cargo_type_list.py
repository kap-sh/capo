"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixHazardousCargoTypeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_matrix_hazardous_cargo_type

RouteMatrixHazardousCargoTypeList: TypeAlias = list[
    "capo_geo_routes.types.route_matrix_hazardous_cargo_type.RouteMatrixHazardousCargoType"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixHazardousCargoTypeList) -> list:
    import capo_geo_routes.types.route_matrix_hazardous_cargo_type

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_matrix_hazardous_cargo_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteMatrixHazardousCargoTypeList:
    import capo_geo_routes.types.route_matrix_hazardous_cargo_type

    out: RouteMatrixHazardousCargoTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_matrix_hazardous_cargo_type.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: RouteMatrixHazardousCargoTypeList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
