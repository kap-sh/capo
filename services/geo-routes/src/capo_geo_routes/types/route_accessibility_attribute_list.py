"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAccessibilityAttributeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_accessibility_attribute

RouteAccessibilityAttributeList: TypeAlias = list[
    "capo_geo_routes.types.route_accessibility_attribute.RouteAccessibilityAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteAccessibilityAttributeList) -> list:
    import capo_geo_routes.types.route_accessibility_attribute

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_accessibility_attribute.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteAccessibilityAttributeList:
    import capo_geo_routes.types.route_accessibility_attribute

    out: RouteAccessibilityAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.route_accessibility_attribute.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RouteAccessibilityAttributeList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
