"""Generated from Smithy shape ``com.amazonaws.networkmonitor#UpdateMonitorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmonitor.types.aggregation_period
    import capo_networkmonitor.types.resource_name


class UpdateMonitorInput(TypedDict, closed=True):
    monitor_name: "capo_networkmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor to update. </p>"""
    aggregation_period: "capo_networkmonitor.types.aggregation_period.AggregationPeriod"
    """<p>The aggregation time, in seconds, to change to. This must be either <code>30</code> or <code>60</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMonitorInput) -> dict:
    out: dict = {}
    out["aggregationPeriod"] = value["aggregation_period"]
    return out


def deserialize_json(data: dict) -> UpdateMonitorInput:
    out: UpdateMonitorInput = {}  # type: ignore[typeddict-item]
    if data.get("aggregationPeriod") is not None:
        out["aggregation_period"] = data["aggregationPeriod"]
    else:
        out["aggregation_period"] = 0
    return out
