"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#PerformanceMonitorQueryType``."""

from typing import Literal, TypeAlias, cast

PerformanceMonitorQueryType: TypeAlias = Literal["TOP_PATHS",]


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceMonitorQueryType) -> str:
    return value


def deserialize_json(data: str) -> PerformanceMonitorQueryType:
    return cast(PerformanceMonitorQueryType, data)
