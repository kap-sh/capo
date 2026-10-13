"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapSnappedTracePointList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.road_snap_snapped_trace_point

RoadSnapSnappedTracePointList: TypeAlias = list[
    "capo_geo_routes.types.road_snap_snapped_trace_point.RoadSnapSnappedTracePoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapSnappedTracePointList) -> list:
    import capo_geo_routes.types.road_snap_snapped_trace_point

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.road_snap_snapped_trace_point.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RoadSnapSnappedTracePointList:
    import capo_geo_routes.types.road_snap_snapped_trace_point

    out: RoadSnapSnappedTracePointList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.road_snap_snapped_trace_point.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RoadSnapSnappedTracePointList) -> list[Any]:
    import capo_geo_routes.types.road_snap_snapped_trace_point

    return [
        capo_geo_routes.types.road_snap_snapped_trace_point.redact_sensitive(item)
        for item in value
    ]
