"""Generated from Smithy shape ``com.amazonaws.networkmonitor#CreateMonitorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmonitor.types.aggregation_period
    import capo_networkmonitor.types.monitor_arn
    import capo_networkmonitor.types.monitor_state
    import capo_networkmonitor.types.resource_name
    import capo_networkmonitor.types.tag_map


class CreateMonitorOutput(TypedDict, closed=True):
    monitor_arn: "capo_networkmonitor.types.monitor_arn.MonitorArn"
    """<p>The ARN of the monitor.</p>"""
    monitor_name: "capo_networkmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""
    state: "capo_networkmonitor.types.monitor_state.MonitorState"
    """<p>The state of the monitor.</p>"""
    aggregation_period: NotRequired[
        "capo_networkmonitor.types.aggregation_period.AggregationPeriod"
    ]
    """<p>The number of seconds that metrics are aggregated by and sent to Amazon CloudWatch. This will be either <code>30</code> or <code>60</code>. </p>"""
    tags: NotRequired["capo_networkmonitor.types.tag_map.TagMap"]
    """<p>The list of key-value pairs assigned to the monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMonitorOutput) -> dict:
    out: dict = {}
    out["monitorArn"] = value["monitor_arn"]
    out["monitorName"] = value["monitor_name"]
    import capo_networkmonitor.types.monitor_state

    out["state"] = capo_networkmonitor.types.monitor_state.serialize_json(
        value["state"]
    )
    if "aggregation_period" in value:
        out["aggregationPeriod"] = value["aggregation_period"]
    if "tags" in value:
        import capo_networkmonitor.types.tag_map

        out["tags"] = capo_networkmonitor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMonitorOutput:
    out: CreateMonitorOutput = {}  # type: ignore[typeddict-item]
    if data.get("monitorArn") is not None:
        out["monitor_arn"] = data["monitorArn"]
    else:
        out["monitor_arn"] = ""
    if data.get("monitorName") is not None:
        out["monitor_name"] = data["monitorName"]
    else:
        out["monitor_name"] = ""
    if data.get("state") is not None:
        import capo_networkmonitor.types.monitor_state

        out["state"] = capo_networkmonitor.types.monitor_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_networkmonitor.types.monitor_state.MonitorState", ""
        )
    if data.get("aggregationPeriod") is not None:
        out["aggregation_period"] = data["aggregationPeriod"]
    if data.get("tags") is not None:
        import capo_networkmonitor.types.tag_map

        out["tags"] = capo_networkmonitor.types.tag_map.deserialize_json(data["tags"])
    return out
