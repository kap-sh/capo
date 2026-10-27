"""Generated from Smithy shape ``com.amazonaws.deadline#GetMonitorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.monitor_id


class GetMonitorRequest(TypedDict, closed=True):
    monitor_id: "capo_deadline.types.monitor_id.MonitorId"
    """The unique identifier for the monitor. This ID is returned by the <code>CreateMonitor</code> operation."""


# --- restJson1 ser/de ---
def serialize_json(value: GetMonitorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMonitorRequest:
    out: GetMonitorRequest = {}  # type: ignore[typeddict-item]
    return out
