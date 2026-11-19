"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#DeletePerformanceMonitorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.resource_name


class DeletePerformanceMonitorInput(TypedDict, closed=True):
    monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the performance monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePerformanceMonitorInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePerformanceMonitorInput:
    out: DeletePerformanceMonitorInput = {}  # type: ignore[typeddict-item]
    return out
