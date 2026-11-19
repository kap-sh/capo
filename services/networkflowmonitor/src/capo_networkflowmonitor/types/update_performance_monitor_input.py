"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#UpdatePerformanceMonitorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.performance_monitor_targets
    import capo_networkflowmonitor.types.resource_name
    import capo_networkflowmonitor.types.uuid_string


class UpdatePerformanceMonitorInput(TypedDict, closed=True):
    monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the performance monitor.</p>"""
    targets_to_add: NotRequired[
        "capo_networkflowmonitor.types.performance_monitor_targets.PerformanceMonitorTargets"
    ]
    """<p>The resources to add to the performance monitor.</p>"""
    targets_to_remove: NotRequired[
        "capo_networkflowmonitor.types.performance_monitor_targets.PerformanceMonitorTargets"
    ]
    """<p>The resources to remove from the performance monitor.</p>"""
    client_token: NotRequired["capo_networkflowmonitor.types.uuid_string.UuidString"]
    """<p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. If the token matches a previous request, the service ignores the request without returning an error. Don't reuse the same client token for other API requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePerformanceMonitorInput) -> dict:
    out: dict = {}
    if "targets_to_add" in value:
        import capo_networkflowmonitor.types.performance_monitor_targets

        out["targetsToAdd"] = (
            capo_networkflowmonitor.types.performance_monitor_targets.serialize_json(
                value["targets_to_add"]
            )
        )
    if "targets_to_remove" in value:
        import capo_networkflowmonitor.types.performance_monitor_targets

        out["targetsToRemove"] = (
            capo_networkflowmonitor.types.performance_monitor_targets.serialize_json(
                value["targets_to_remove"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdatePerformanceMonitorInput:
    out: UpdatePerformanceMonitorInput = {}  # type: ignore[typeddict-item]
    if data.get("targetsToAdd") is not None:
        import capo_networkflowmonitor.types.performance_monitor_targets

        out["targets_to_add"] = (
            capo_networkflowmonitor.types.performance_monitor_targets.deserialize_json(
                data["targetsToAdd"]
            )
        )
    if data.get("targetsToRemove") is not None:
        import capo_networkflowmonitor.types.performance_monitor_targets

        out["targets_to_remove"] = (
            capo_networkflowmonitor.types.performance_monitor_targets.deserialize_json(
                data["targetsToRemove"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
