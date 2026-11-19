"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#StopQueryPerformanceMonitorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.resource_name


class StopQueryPerformanceMonitorInput(TypedDict, closed=True):
    monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the performance monitor.</p>"""
    query_id: "str"
    """<p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopQueryPerformanceMonitorInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopQueryPerformanceMonitorInput:
    out: StopQueryPerformanceMonitorInput = {}  # type: ignore[typeddict-item]
    return out
