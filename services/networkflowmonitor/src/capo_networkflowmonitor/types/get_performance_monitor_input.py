"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetPerformanceMonitorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.resource_name


class GetPerformanceMonitorInput(TypedDict, closed=True):
    monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the performance monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPerformanceMonitorInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPerformanceMonitorInput:
    out: GetPerformanceMonitorInput = {}  # type: ignore[typeddict-item]
    return out
