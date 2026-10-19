"""Generated from Smithy shape ``com.amazonaws.internetmonitor#Monitor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.monitor_arn
    import capo_internetmonitor.types.monitor_config_state
    import capo_internetmonitor.types.monitor_processing_status_code
    import capo_internetmonitor.types.resource_name


class Monitor(TypedDict, closed=True):
    monitor_name: "capo_internetmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""
    monitor_arn: "capo_internetmonitor.types.monitor_arn.MonitorArn"
    """<p>The Amazon Resource Name (ARN) of the monitor.</p>"""
    status: "capo_internetmonitor.types.monitor_config_state.MonitorConfigState"
    """<p>The status of a monitor.</p>"""
    processing_status: NotRequired[
        "capo_internetmonitor.types.monitor_processing_status_code.MonitorProcessingStatusCode"
    ]
    """<p>The health of data processing for the monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Monitor) -> dict:
    out: dict = {}
    out["MonitorName"] = value["monitor_name"]
    out["MonitorArn"] = value["monitor_arn"]
    out["Status"] = value["status"]
    if "processing_status" in value:
        out["ProcessingStatus"] = value["processing_status"]
    return out


def deserialize_json(data: dict) -> Monitor:
    out: Monitor = {}  # type: ignore[typeddict-item]
    if data.get("MonitorName") is not None:
        out["monitor_name"] = data["MonitorName"]
    else:
        out["monitor_name"] = ""
    if data.get("MonitorArn") is not None:
        out["monitor_arn"] = data["MonitorArn"]
    else:
        out["monitor_arn"] = ""
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    if data.get("ProcessingStatus") is not None:
        out["processing_status"] = data["ProcessingStatus"]
    return out
