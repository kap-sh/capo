"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.monitor_arn
    import capo_networkflowmonitor.types.monitor_status
    import capo_networkflowmonitor.types.resource_name


class MonitorSummary(TypedDict, closed=True):
    monitor_arn: "capo_networkflowmonitor.types.monitor_arn.MonitorArn"
    """<p>The Amazon Resource Name (ARN) of the monitor.</p>"""
    monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""
    monitor_status: "capo_networkflowmonitor.types.monitor_status.MonitorStatus"
    """<p>The status of a monitor. The status can be one of the following</p> <ul> <li> <p> <code>PENDING</code>: The monitor is in the process of being created.</p> </li> <li> <p> <code>ACTIVE</code>: The monitor is active.</p> </li> <li> <p> <code>INACTIVE</code>: The monitor is inactive.</p> </li> <li> <p> <code>ERROR</code>: Monitor creation failed due to an error.</p> </li> <li> <p> <code>DELETING</code>: The monitor is in the process of being deleted.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonitorSummary) -> dict:
    out: dict = {}
    out["monitorArn"] = value["monitor_arn"]
    out["monitorName"] = value["monitor_name"]
    import capo_networkflowmonitor.types.monitor_status

    out["monitorStatus"] = capo_networkflowmonitor.types.monitor_status.serialize_json(
        value["monitor_status"]
    )
    return out


def deserialize_json(data: dict) -> MonitorSummary:
    out: MonitorSummary = {}  # type: ignore[typeddict-item]
    if data.get("monitorArn") is not None:
        out["monitor_arn"] = data["monitorArn"]
    else:
        out["monitor_arn"] = ""
    if data.get("monitorName") is not None:
        out["monitor_name"] = data["monitorName"]
    else:
        out["monitor_name"] = ""
    if data.get("monitorStatus") is not None:
        import capo_networkflowmonitor.types.monitor_status

        out["monitor_status"] = (
            capo_networkflowmonitor.types.monitor_status.deserialize_json(
                data["monitorStatus"]
            )
        )
    else:
        import typing

        out["monitor_status"] = typing.cast(
            "capo_networkflowmonitor.types.monitor_status.MonitorStatus", ""
        )
    return out
