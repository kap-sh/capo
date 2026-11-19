"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#PerformanceMonitorSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.performance_monitor_summary

PerformanceMonitorSummaryList: TypeAlias = list[
    "capo_networkflowmonitor.types.performance_monitor_summary.PerformanceMonitorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceMonitorSummaryList) -> list:
    import capo_networkflowmonitor.types.performance_monitor_summary

    out: list = []
    for item in value:
        out.append(
            capo_networkflowmonitor.types.performance_monitor_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PerformanceMonitorSummaryList:
    import capo_networkflowmonitor.types.performance_monitor_summary

    out: PerformanceMonitorSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_networkflowmonitor.types.performance_monitor_summary.deserialize_json(
                item
            )
        )
    return out
