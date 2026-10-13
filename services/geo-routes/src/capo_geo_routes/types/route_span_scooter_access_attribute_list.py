"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanScooterAccessAttributeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_span_scooter_access_attribute

RouteSpanScooterAccessAttributeList: TypeAlias = list[
    "capo_geo_routes.types.route_span_scooter_access_attribute.RouteSpanScooterAccessAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanScooterAccessAttributeList) -> list:
    import capo_geo_routes.types.route_span_scooter_access_attribute

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_span_scooter_access_attribute.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RouteSpanScooterAccessAttributeList:
    import capo_geo_routes.types.route_span_scooter_access_attribute

    out: RouteSpanScooterAccessAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_span_scooter_access_attribute.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: RouteSpanScooterAccessAttributeList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
