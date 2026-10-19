"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetMonitorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.iso8601_timestamp
    import capo_networkflowmonitor.types.monitor_arn
    import capo_networkflowmonitor.types.monitor_local_resources
    import capo_networkflowmonitor.types.monitor_remote_resources
    import capo_networkflowmonitor.types.monitor_status
    import capo_networkflowmonitor.types.resource_name
    import capo_networkflowmonitor.types.tag_map


class GetMonitorOutput(TypedDict, closed=True):
    monitor_arn: "capo_networkflowmonitor.types.monitor_arn.MonitorArn"
    """<p>The Amazon Resource Name (ARN) of the monitor.</p>"""
    monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""
    monitor_status: "capo_networkflowmonitor.types.monitor_status.MonitorStatus"
    """<p>The status of a monitor. The status can be one of the following</p> <ul> <li> <p> <code>PENDING</code>: The monitor is in the process of being created.</p> </li> <li> <p> <code>ACTIVE</code>: The monitor is active.</p> </li> <li> <p> <code>INACTIVE</code>: The monitor is inactive.</p> </li> <li> <p> <code>ERROR</code>: Monitor creation failed due to an error.</p> </li> <li> <p> <code>DELETING</code>: The monitor is in the process of being deleted.</p> </li> </ul>"""
    local_resources: (
        "capo_networkflowmonitor.types.monitor_local_resources.MonitorLocalResources"
    )
    """<p>The local resources to monitor. A local resource in a workload is the location of the hosts where the Network Flow Monitor agent is installed. </p>"""
    remote_resources: (
        "capo_networkflowmonitor.types.monitor_remote_resources.MonitorRemoteResources"
    )
    """<p>The remote resources to monitor. A remote resource is the other endpoint specified for the network flow of a workload, with a local resource. For example, Amazon Dynamo DB can be a remote resource. </p>"""
    created_at: "capo_networkflowmonitor.types.iso8601_timestamp.Iso8601Timestamp"
    """<p>The date and time when the monitor was created.</p>"""
    modified_at: "capo_networkflowmonitor.types.iso8601_timestamp.Iso8601Timestamp"
    """<p>The date and time when the monitor was last modified.</p>"""
    tags: NotRequired["capo_networkflowmonitor.types.tag_map.TagMap"]
    """<p>The tags for a monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMonitorOutput) -> dict:
    out: dict = {}
    out["monitorArn"] = value["monitor_arn"]
    out["monitorName"] = value["monitor_name"]
    import capo_networkflowmonitor.types.monitor_status

    out["monitorStatus"] = capo_networkflowmonitor.types.monitor_status.serialize_json(
        value["monitor_status"]
    )
    import capo_networkflowmonitor.types.monitor_local_resources

    out["localResources"] = (
        capo_networkflowmonitor.types.monitor_local_resources.serialize_json(
            value["local_resources"]
        )
    )
    import capo_networkflowmonitor.types.monitor_remote_resources

    out["remoteResources"] = (
        capo_networkflowmonitor.types.monitor_remote_resources.serialize_json(
            value["remote_resources"]
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


def deserialize_json(data: dict) -> GetMonitorOutput:
    out: GetMonitorOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("localResources") is not None:
        import capo_networkflowmonitor.types.monitor_local_resources

        out["local_resources"] = (
            capo_networkflowmonitor.types.monitor_local_resources.deserialize_json(
                data["localResources"]
            )
        )
    else:
        out["local_resources"] = []
    if data.get("remoteResources") is not None:
        import capo_networkflowmonitor.types.monitor_remote_resources

        out["remote_resources"] = (
            capo_networkflowmonitor.types.monitor_remote_resources.deserialize_json(
                data["remoteResources"]
            )
        )
    else:
        out["remote_resources"] = []
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
