"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#PerformanceMonitorTargetType``."""

from typing import Literal, TypeAlias, cast

PerformanceMonitorTargetType: TypeAlias = Literal["AWS::EC2::VPC",]


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceMonitorTargetType) -> str:
    return value


def deserialize_json(data: str) -> PerformanceMonitorTargetType:
    return cast(PerformanceMonitorTargetType, data)
