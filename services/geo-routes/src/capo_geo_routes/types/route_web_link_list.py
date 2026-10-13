"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteWebLinkList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_web_link

RouteWebLinkList: TypeAlias = list["capo_geo_routes.types.route_web_link.RouteWebLink"]


# --- restJson1 ser/de ---
def serialize_json(value: RouteWebLinkList) -> list:
    import capo_geo_routes.types.route_web_link

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_web_link.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteWebLinkList:
    import capo_geo_routes.types.route_web_link

    out: RouteWebLinkList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_web_link.deserialize_json(item))
    return out


def redact_sensitive(value: RouteWebLinkList) -> list[Any]:
    import capo_geo_routes.types.route_web_link

    return [
        capo_geo_routes.types.route_web_link.redact_sensitive(item) for item in value
    ]
