"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMajorRoadLabelList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_major_road_label

RouteMajorRoadLabelList: TypeAlias = list[
    "capo_geo_routes.types.route_major_road_label.RouteMajorRoadLabel"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMajorRoadLabelList) -> list:
    import capo_geo_routes.types.route_major_road_label

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_major_road_label.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteMajorRoadLabelList:
    import capo_geo_routes.types.route_major_road_label

    out: RouteMajorRoadLabelList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_major_road_label.deserialize_json(item))
    return out


def redact_sensitive(value: RouteMajorRoadLabelList) -> list[Any]:
    import capo_geo_routes.types.route_major_road_label

    return [
        capo_geo_routes.types.route_major_road_label.redact_sensitive(item)
        for item in value
    ]
