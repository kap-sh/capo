"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#CreatePerformanceMonitorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.arn
    import capo_networkflowmonitor.types.performance_monitor_targets
    import capo_networkflowmonitor.types.resource_name
    import capo_networkflowmonitor.types.tag_map
    import capo_networkflowmonitor.types.uuid_string


class CreatePerformanceMonitorInput(TypedDict, closed=True):
    monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the performance monitor.</p>"""
    scope_arn: NotRequired["capo_networkflowmonitor.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the scope for the performance monitor.</p>"""
    targets: "capo_networkflowmonitor.types.performance_monitor_targets.PerformanceMonitorTargets"
    """<p>The resources to monitor. Each target identifies a resource, currently a VPC, for which you can track network performance. For a VPC, specify the VPC ARN.</p>"""
    client_token: NotRequired["capo_networkflowmonitor.types.uuid_string.UuidString"]
    """<p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. If the token matches a previous request, the service ignores the request without returning an error. Don't reuse the same client token for other API requests.</p>"""
    tags: NotRequired["capo_networkflowmonitor.types.tag_map.TagMap"]
    """<p>The tags for a performance monitor. You can add a maximum of 200 tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePerformanceMonitorInput) -> dict:
    out: dict = {}
    out["monitorName"] = value["monitor_name"]
    if "scope_arn" in value:
        out["scopeArn"] = value["scope_arn"]
    import capo_networkflowmonitor.types.performance_monitor_targets

    out["targets"] = (
        capo_networkflowmonitor.types.performance_monitor_targets.serialize_json(
            value["targets"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_networkflowmonitor.types.tag_map

        out["tags"] = capo_networkflowmonitor.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreatePerformanceMonitorInput:
    out: CreatePerformanceMonitorInput = {}  # type: ignore[typeddict-item]
    if data.get("monitorName") is not None:
        out["monitor_name"] = data["monitorName"]
    else:
        out["monitor_name"] = ""
    if data.get("scopeArn") is not None:
        out["scope_arn"] = data["scopeArn"]
    if data.get("targets") is not None:
        import capo_networkflowmonitor.types.performance_monitor_targets

        out["targets"] = (
            capo_networkflowmonitor.types.performance_monitor_targets.deserialize_json(
                data["targets"]
            )
        )
    else:
        out["targets"] = []
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_networkflowmonitor.types.tag_map

        out["tags"] = capo_networkflowmonitor.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
