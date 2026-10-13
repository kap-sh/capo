"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanTruckAccessAttributeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_span_truck_access_attribute

RouteSpanTruckAccessAttributeList: TypeAlias = list[
    "capo_geo_routes.types.route_span_truck_access_attribute.RouteSpanTruckAccessAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanTruckAccessAttributeList) -> list:
    import capo_geo_routes.types.route_span_truck_access_attribute

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_span_truck_access_attribute.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteSpanTruckAccessAttributeList:
    import capo_geo_routes.types.route_span_truck_access_attribute

    out: RouteSpanTruckAccessAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_span_truck_access_attribute.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: RouteSpanTruckAccessAttributeList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
