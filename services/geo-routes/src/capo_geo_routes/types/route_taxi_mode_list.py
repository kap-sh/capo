"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiModeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_taxi_mode

RouteTaxiModeList: TypeAlias = list[
    "capo_geo_routes.types.route_taxi_mode.RouteTaxiMode"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiModeList) -> list:
    import capo_geo_routes.types.route_taxi_mode

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_taxi_mode.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTaxiModeList:
    import capo_geo_routes.types.route_taxi_mode

    out: RouteTaxiModeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_taxi_mode.deserialize_json(item))
    return out


def redact_sensitive(value: RouteTaxiModeList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
