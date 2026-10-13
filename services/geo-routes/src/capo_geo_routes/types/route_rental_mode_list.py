"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalModeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_rental_mode

RouteRentalModeList: TypeAlias = list[
    "capo_geo_routes.types.route_rental_mode.RouteRentalMode"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalModeList) -> list:
    import capo_geo_routes.types.route_rental_mode

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_rental_mode.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteRentalModeList:
    import capo_geo_routes.types.route_rental_mode

    out: RouteRentalModeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_rental_mode.deserialize_json(item))
    return out


def redact_sensitive(value: RouteRentalModeList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
