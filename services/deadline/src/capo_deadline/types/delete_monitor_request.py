"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteMonitorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.monitor_id


class DeleteMonitorRequest(TypedDict, closed=True):
    monitor_id: "capo_deadline.types.monitor_id.MonitorId"
    """The unique identifier of the monitor to delete. This ID is returned by the <code>CreateMonitor</code> operation, and is included in the response to the <code>GetMonitor</code> operation."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMonitorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMonitorRequest:
    out: DeleteMonitorRequest = {}  # type: ignore[typeddict-item]
    return out
