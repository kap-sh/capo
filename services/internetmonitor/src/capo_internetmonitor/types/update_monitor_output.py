"""Generated from Smithy shape ``com.amazonaws.internetmonitor#UpdateMonitorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.monitor_arn
    import capo_internetmonitor.types.monitor_config_state


class UpdateMonitorOutput(TypedDict, closed=True):
    monitor_arn: "capo_internetmonitor.types.monitor_arn.MonitorArn"
    """<p>The Amazon Resource Name (ARN) of the monitor.</p>"""
    status: "capo_internetmonitor.types.monitor_config_state.MonitorConfigState"
    """<p>The status of a monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMonitorOutput) -> dict:
    out: dict = {}
    out["MonitorArn"] = value["monitor_arn"]
    out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> UpdateMonitorOutput:
    out: UpdateMonitorOutput = {}  # type: ignore[typeddict-item]
    if data.get("MonitorArn") is not None:
        out["monitor_arn"] = data["MonitorArn"]
    else:
        out["monitor_arn"] = ""
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    return out
