"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#PerformanceMonitorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.monitor_arn
    import capo_networkflowmonitor.types.monitor_status
    import capo_networkflowmonitor.types.performance_monitor_targets
    import capo_networkflowmonitor.types.performance_monitor_type
    import capo_networkflowmonitor.types.resource_name


class PerformanceMonitorSummary(TypedDict, closed=True):
    monitor_arn: "capo_networkflowmonitor.types.monitor_arn.MonitorArn"
    """<p>The Amazon Resource Name (ARN) of the performance monitor.</p>"""
    monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the performance monitor.</p>"""
    monitor_status: "capo_networkflowmonitor.types.monitor_status.MonitorStatus"
    """<p>The status of a performance monitor. The status can be one of the following</p> <ul> <li> <p> <code>PENDING</code>: The performance monitor is in the process of being created.</p> </li> <li> <p> <code>ACTIVE</code>: The performance monitor is active.</p> </li> <li> <p> <code>INACTIVE</code>: The performance monitor is inactive.</p> </li> <li> <p> <code>ERROR</code>: The performance monitor can't be created or updated.</p> </li> <li> <p> <code>DELETING</code>: The performance monitor is in the process of being deleted.</p> </li> </ul>"""
    monitor_type: (
        "capo_networkflowmonitor.types.performance_monitor_type.PerformanceMonitorType"
    )
    """<p>The type of resource that you monitor determines the type of the performance monitor.</p>"""
    targets: NotRequired[
        "capo_networkflowmonitor.types.performance_monitor_targets.PerformanceMonitorTargets"
    ]
    """<p>The resources that the performance monitor tracks network performance for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceMonitorSummary) -> dict:
    out: dict = {}
    out["monitorArn"] = value["monitor_arn"]
    out["monitorName"] = value["monitor_name"]
    import capo_networkflowmonitor.types.monitor_status

    out["monitorStatus"] = capo_networkflowmonitor.types.monitor_status.serialize_json(
        value["monitor_status"]
    )
    import capo_networkflowmonitor.types.performance_monitor_type

    out["monitorType"] = (
        capo_networkflowmonitor.types.performance_monitor_type.serialize_json(
            value["monitor_type"]
        )
    )
    if "targets" in value:
        import capo_networkflowmonitor.types.performance_monitor_targets

        out["targets"] = (
            capo_networkflowmonitor.types.performance_monitor_targets.serialize_json(
                value["targets"]
            )
        )
    return out


def deserialize_json(data: dict) -> PerformanceMonitorSummary:
    out: PerformanceMonitorSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("monitorType") is not None:
        import capo_networkflowmonitor.types.performance_monitor_type

        out["monitor_type"] = (
            capo_networkflowmonitor.types.performance_monitor_type.deserialize_json(
                data["monitorType"]
            )
        )
    else:
        import typing

        out["monitor_type"] = typing.cast(
            "capo_networkflowmonitor.types.performance_monitor_type.PerformanceMonitorType",
            "",
        )
    if data.get("targets") is not None:
        import capo_networkflowmonitor.types.performance_monitor_targets

        out["targets"] = (
            capo_networkflowmonitor.types.performance_monitor_targets.deserialize_json(
                data["targets"]
            )
        )
    return out
