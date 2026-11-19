"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#PerformanceMonitorTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.performance_monitor_target_type


class PerformanceMonitorTarget(TypedDict, closed=True):
    type: "capo_networkflowmonitor.types.performance_monitor_target_type.PerformanceMonitorTargetType"
    """<p>The type of the resource that you want Network Flow Monitor to track network performance for. Specify <code>AWS::EC2::VPC</code>.</p>"""
    identifier: "str"
    """<p>The Amazon Resource Name (ARN) of the resource that you want Network Flow Monitor to track network performance for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceMonitorTarget) -> dict:
    out: dict = {}
    import capo_networkflowmonitor.types.performance_monitor_target_type

    out["type"] = (
        capo_networkflowmonitor.types.performance_monitor_target_type.serialize_json(
            value["type"]
        )
    )
    out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> PerformanceMonitorTarget:
    out: PerformanceMonitorTarget = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_networkflowmonitor.types.performance_monitor_target_type

        out["type"] = (
            capo_networkflowmonitor.types.performance_monitor_target_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_networkflowmonitor.types.performance_monitor_target_type.PerformanceMonitorTargetType",
            "",
        )
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    return out
