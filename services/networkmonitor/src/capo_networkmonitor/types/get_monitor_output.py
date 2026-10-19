"""Generated from Smithy shape ``com.amazonaws.networkmonitor#GetMonitorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmonitor.types.aggregation_period
    import capo_networkmonitor.types.iso8601_timestamp
    import capo_networkmonitor.types.monitor_arn
    import capo_networkmonitor.types.monitor_state
    import capo_networkmonitor.types.probe_list
    import capo_networkmonitor.types.resource_name
    import capo_networkmonitor.types.tag_map


class GetMonitorOutput(TypedDict, closed=True):
    monitor_arn: "capo_networkmonitor.types.monitor_arn.MonitorArn"
    """<p>The ARN of the selected monitor.</p>"""
    monitor_name: "capo_networkmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor. </p>"""
    state: "capo_networkmonitor.types.monitor_state.MonitorState"
    """<p>Lists the status of the <code>state</code> of each monitor. </p>"""
    aggregation_period: "capo_networkmonitor.types.aggregation_period.AggregationPeriod"
    """<p>The aggregation period for the specified monitor.</p>"""
    tags: NotRequired["capo_networkmonitor.types.tag_map.TagMap"]
    """<p>The list of key-value pairs assigned to the monitor.</p>"""
    probes: NotRequired["capo_networkmonitor.types.probe_list.ProbeList"]
    """<p>The details about each probe associated with that monitor. </p>"""
    created_at: "capo_networkmonitor.types.iso8601_timestamp.Iso8601Timestamp"
    """<p>The time and date when the monitor was created.</p>"""
    modified_at: "capo_networkmonitor.types.iso8601_timestamp.Iso8601Timestamp"
    """<p>The time and date when the monitor was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMonitorOutput) -> dict:
    out: dict = {}
    out["monitorArn"] = value["monitor_arn"]
    out["monitorName"] = value["monitor_name"]
    import capo_networkmonitor.types.monitor_state

    out["state"] = capo_networkmonitor.types.monitor_state.serialize_json(
        value["state"]
    )
    out["aggregationPeriod"] = value["aggregation_period"]
    if "tags" in value:
        import capo_networkmonitor.types.tag_map

        out["tags"] = capo_networkmonitor.types.tag_map.serialize_json(value["tags"])
    if "probes" in value:
        import capo_networkmonitor.types.probe_list

        out["probes"] = capo_networkmonitor.types.probe_list.serialize_json(
            value["probes"]
        )
    import capo_networkmonitor.types.iso8601_timestamp

    out["createdAt"] = capo_networkmonitor.types.iso8601_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_networkmonitor.types.iso8601_timestamp

    out["modifiedAt"] = capo_networkmonitor.types.iso8601_timestamp.serialize_json(
        value["modified_at"]
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
    else:
        out["aggregation_period"] = 0
    if data.get("tags") is not None:
        import capo_networkmonitor.types.tag_map

        out["tags"] = capo_networkmonitor.types.tag_map.deserialize_json(data["tags"])
    if data.get("probes") is not None:
        import capo_networkmonitor.types.probe_list

        out["probes"] = capo_networkmonitor.types.probe_list.deserialize_json(
            data["probes"]
        )
    if data.get("createdAt") is not None:
        import capo_networkmonitor.types.iso8601_timestamp

        out["created_at"] = (
            capo_networkmonitor.types.iso8601_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("modifiedAt") is not None:
        import capo_networkmonitor.types.iso8601_timestamp

        out["modified_at"] = (
            capo_networkmonitor.types.iso8601_timestamp.deserialize_json(
                data["modifiedAt"]
            )
        )
    else:
        import datetime

        out["modified_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
