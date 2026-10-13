"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanCarAccessAttributeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_span_car_access_attribute

RouteSpanCarAccessAttributeList: TypeAlias = list[
    "capo_geo_routes.types.route_span_car_access_attribute.RouteSpanCarAccessAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanCarAccessAttributeList) -> list:
    import capo_geo_routes.types.route_span_car_access_attribute

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_span_car_access_attribute.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteSpanCarAccessAttributeList:
    import capo_geo_routes.types.route_span_car_access_attribute

    out: RouteSpanCarAccessAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_span_car_access_attribute.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RouteSpanCarAccessAttributeList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
