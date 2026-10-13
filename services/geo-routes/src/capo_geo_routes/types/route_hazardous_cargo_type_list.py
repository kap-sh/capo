"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteHazardousCargoTypeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_hazardous_cargo_type

RouteHazardousCargoTypeList: TypeAlias = list[
    "capo_geo_routes.types.route_hazardous_cargo_type.RouteHazardousCargoType"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteHazardousCargoTypeList) -> list:
    import capo_geo_routes.types.route_hazardous_cargo_type

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_hazardous_cargo_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteHazardousCargoTypeList:
    import capo_geo_routes.types.route_hazardous_cargo_type

    out: RouteHazardousCargoTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_hazardous_cargo_type.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RouteHazardousCargoTypeList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
