"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#PerformanceMonitorTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.performance_monitor_target

PerformanceMonitorTargets: TypeAlias = list[
    "capo_networkflowmonitor.types.performance_monitor_target.PerformanceMonitorTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceMonitorTargets) -> list:
    import capo_networkflowmonitor.types.performance_monitor_target

    out: list = []
    for item in value:
        out.append(
            capo_networkflowmonitor.types.performance_monitor_target.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PerformanceMonitorTargets:
    import capo_networkflowmonitor.types.performance_monitor_target

    out: PerformanceMonitorTargets = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_networkflowmonitor.types.performance_monitor_target.deserialize_json(
                item
            )
        )
    return out
