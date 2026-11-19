"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#ListPerformanceMonitorsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.max_results
    import capo_networkflowmonitor.types.monitor_status
    import capo_networkflowmonitor.types.performance_monitor_type


class ListPerformanceMonitorsInput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""
    max_results: NotRequired["capo_networkflowmonitor.types.max_results.MaxResults"]
    """<p>The number of performance monitors that you want to return with this call. If you don't specify a value, the default is 25.</p>"""
    monitor_status: NotRequired[
        "capo_networkflowmonitor.types.monitor_status.MonitorStatus"
    ]
    """<p>The status of the performance monitors that you want to return. If you don't specify a status, Network Flow Monitor returns performance monitors with any status.</p>"""
    monitor_type: NotRequired[
        "capo_networkflowmonitor.types.performance_monitor_type.PerformanceMonitorType"
    ]
    """<p>The type of the performance monitors that you want to return. If you don't specify a type, Network Flow Monitor returns performance monitors of any type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPerformanceMonitorsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPerformanceMonitorsInput:
    out: ListPerformanceMonitorsInput = {}  # type: ignore[typeddict-item]
    return out
