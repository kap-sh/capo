"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapTracePointList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.road_snap_trace_point

RoadSnapTracePointList: TypeAlias = list[
    "capo_geo_routes.types.road_snap_trace_point.RoadSnapTracePoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapTracePointList) -> list:
    import capo_geo_routes.types.road_snap_trace_point

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.road_snap_trace_point.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoadSnapTracePointList:
    import capo_geo_routes.types.road_snap_trace_point

    out: RoadSnapTracePointList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.road_snap_trace_point.deserialize_json(item))
    return out


def redact_sensitive(value: RoadSnapTracePointList) -> list[Any]:
    import capo_geo_routes.types.road_snap_trace_point

    return [
        capo_geo_routes.types.road_snap_trace_point.redact_sensitive(item)
        for item in value
    ]
