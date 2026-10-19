"""Generated from Smithy shape ``com.amazonaws.internetmonitor#CreateMonitorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.monitor_arn
    import capo_internetmonitor.types.monitor_config_state


class CreateMonitorOutput(TypedDict, closed=True):
    arn: "capo_internetmonitor.types.monitor_arn.MonitorArn"
    """<p>The Amazon Resource Name (ARN) of the monitor.</p>"""
    status: "capo_internetmonitor.types.monitor_config_state.MonitorConfigState"
    """<p>The status of a monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMonitorOutput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> CreateMonitorOutput:
    out: CreateMonitorOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    return out
