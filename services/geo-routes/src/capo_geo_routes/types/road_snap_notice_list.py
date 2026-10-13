"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapNoticeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.road_snap_notice

RoadSnapNoticeList: TypeAlias = list[
    "capo_geo_routes.types.road_snap_notice.RoadSnapNotice"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapNoticeList) -> list:
    import capo_geo_routes.types.road_snap_notice

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.road_snap_notice.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoadSnapNoticeList:
    import capo_geo_routes.types.road_snap_notice

    out: RoadSnapNoticeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.road_snap_notice.deserialize_json(item))
    return out


def redact_sensitive(value: RoadSnapNoticeList) -> list[Any]:
    import capo_geo_routes.types.road_snap_notice

    return [
        capo_geo_routes.types.road_snap_notice.redact_sensitive(item) for item in value
    ]
