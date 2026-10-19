"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#CreateMonitorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.arn
    import capo_networkflowmonitor.types.monitor_local_resources
    import capo_networkflowmonitor.types.monitor_remote_resources
    import capo_networkflowmonitor.types.resource_name
    import capo_networkflowmonitor.types.tag_map
    import capo_networkflowmonitor.types.uuid_string


class CreateMonitorInput(TypedDict, closed=True):
    monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor. </p>"""
    local_resources: (
        "capo_networkflowmonitor.types.monitor_local_resources.MonitorLocalResources"
    )
    """<p>The local resources to monitor. A local resource in a workload is the location of the host, or hosts, where the Network Flow Monitor agent is installed. For example, if a workload consists of an interaction between a web service and a backend database (for example, Amazon Dynamo DB), the subnet with the EC2 instance that hosts the web service, which also runs the agent, is the local resource.</p> <p>Be aware that all local resources must belong to the current Region.</p>"""
    remote_resources: NotRequired[
        "capo_networkflowmonitor.types.monitor_remote_resources.MonitorRemoteResources"
    ]
    """<p>The remote resources to monitor. A remote resource is the other endpoint in the bi-directional flow of a workload, with a local resource. For example, Amazon Dynamo DB can be a remote resource.</p> <p>When you specify remote resources, be aware that specific combinations of resources are allowed and others are not, including the following constraints:</p> <ul> <li> <p>All remote resources that you specify must all belong to a single Region.</p> </li> <li> <p>If you specify Amazon Web Services services as remote resources, any other remote resources that you specify must be in the current Region.</p> </li> <li> <p>When you specify a remote resource for another Region, you can only specify the <code>Region</code> resource type. You cannot specify a subnet, VPC, or Availability Zone in another Region.</p> </li> <li> <p>If you leave the <code>RemoteResources</code> parameter empty, the monitor will include all network flows that terminate in the current Region.</p> </li> </ul>"""
    scope_arn: "capo_networkflowmonitor.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the scope for the monitor.</p>"""
    client_token: NotRequired["capo_networkflowmonitor.types.uuid_string.UuidString"]
    """<p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. Don't reuse the same client token for other API requests.</p>"""
    tags: NotRequired["capo_networkflowmonitor.types.tag_map.TagMap"]
    """<p>The tags for a monitor. You can add a maximum of 200 tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMonitorInput) -> dict:
    out: dict = {}
    out["monitorName"] = value["monitor_name"]
    import capo_networkflowmonitor.types.monitor_local_resources

    out["localResources"] = (
        capo_networkflowmonitor.types.monitor_local_resources.serialize_json(
            value["local_resources"]
        )
    )
    if "remote_resources" in value:
        import capo_networkflowmonitor.types.monitor_remote_resources

        out["remoteResources"] = (
            capo_networkflowmonitor.types.monitor_remote_resources.serialize_json(
                value["remote_resources"]
            )
        )
    out["scopeArn"] = value["scope_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_networkflowmonitor.types.tag_map

        out["tags"] = capo_networkflowmonitor.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateMonitorInput:
    out: CreateMonitorInput = {}  # type: ignore[typeddict-item]
    if data.get("monitorName") is not None:
        out["monitor_name"] = data["monitorName"]
    else:
        out["monitor_name"] = ""
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
    if data.get("scopeArn") is not None:
        out["scope_arn"] = data["scopeArn"]
    else:
        out["scope_arn"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_networkflowmonitor.types.tag_map

        out["tags"] = capo_networkflowmonitor.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
