"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#PerformanceMonitorType``."""

from typing import Literal, TypeAlias, cast

PerformanceMonitorType: TypeAlias = Literal["VPC",]


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceMonitorType) -> str:
    return value


def deserialize_json(data: str) -> PerformanceMonitorType:
    return cast(PerformanceMonitorType, data)
