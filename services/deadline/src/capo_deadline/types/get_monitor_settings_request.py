"""Generated from Smithy shape ``com.amazonaws.deadline#GetMonitorSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.monitor_id


class GetMonitorSettingsRequest(TypedDict, closed=True):
    monitor_id: "capo_deadline.types.monitor_id.MonitorId"
    """The unique identifier of the monitor. This ID is returned by the <code>CreateMonitor</code> operation, and is included in the response to the <code>ListMonitors</code> operation."""


# --- restJson1 ser/de ---
def serialize_json(value: GetMonitorSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMonitorSettingsRequest:
    out: GetMonitorSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
