"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetPerformanceMonitorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.iso8601_timestamp
    import capo_networkflowmonitor.types.monitor_arn
    import capo_networkflowmonitor.types.monitor_status
    import capo_networkflowmonitor.types.performance_monitor_targets
    import capo_networkflowmonitor.types.performance_monitor_type
    import capo_networkflowmonitor.types.resource_name
    import capo_networkflowmonitor.types.tag_map


class GetPerformanceMonitorOutput(TypedDict, closed=True):
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
    targets: "capo_networkflowmonitor.types.performance_monitor_targets.PerformanceMonitorTargets"
    """<p>The resources that the performance monitor tracks network performance for.</p>"""
    created_at: "capo_networkflowmonitor.types.iso8601_timestamp.Iso8601Timestamp"
    """<p>The date and time when the performance monitor was created.</p>"""
    modified_at: "capo_networkflowmonitor.types.iso8601_timestamp.Iso8601Timestamp"
    """<p>The date and time when the performance monitor was last modified.</p>"""
    tags: NotRequired["capo_networkflowmonitor.types.tag_map.TagMap"]
    """<p>The tags for a performance monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPerformanceMonitorOutput) -> dict:
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
    import capo_networkflowmonitor.types.performance_monitor_targets

    out["targets"] = (
        capo_networkflowmonitor.types.performance_monitor_targets.serialize_json(
            value["targets"]
        )
    )
    import capo_networkflowmonitor.types.iso8601_timestamp

    out["createdAt"] = capo_networkflowmonitor.types.iso8601_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_networkflowmonitor.types.iso8601_timestamp

    out["modifiedAt"] = capo_networkflowmonitor.types.iso8601_timestamp.serialize_json(
        value["modified_at"]
    )
    if "tags" in value:
        import capo_networkflowmonitor.types.tag_map

        out["tags"] = capo_networkflowmonitor.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetPerformanceMonitorOutput:
    out: GetPerformanceMonitorOutput = {}  # type: ignore[typeddict-item]
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
    else:
        out["targets"] = []
    if data.get("createdAt") is not None:
        import capo_networkflowmonitor.types.iso8601_timestamp

        out["created_at"] = (
            capo_networkflowmonitor.types.iso8601_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("modifiedAt") is not None:
        import capo_networkflowmonitor.types.iso8601_timestamp

        out["modified_at"] = (
            capo_networkflowmonitor.types.iso8601_timestamp.deserialize_json(
                data["modifiedAt"]
            )
        )
    else:
        import datetime

        out["modified_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("tags") is not None:
        import capo_networkflowmonitor.types.tag_map

        out["tags"] = capo_networkflowmonitor.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
