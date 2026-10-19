"""Generated from Smithy shape ``com.amazonaws.networkmonitor#CreateMonitorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmonitor.types.aggregation_period
    import capo_networkmonitor.types.create_monitor_probe_input_list
    import capo_networkmonitor.types.resource_name
    import capo_networkmonitor.types.tag_map


class CreateMonitorInput(TypedDict, closed=True):
    monitor_name: "capo_networkmonitor.types.resource_name.ResourceName"
    """<p>The name identifying the monitor. It can contain only letters, underscores (_), or dashes (-), and can be up to 200 characters.</p>"""
    probes: NotRequired[
        "capo_networkmonitor.types.create_monitor_probe_input_list.CreateMonitorProbeInputList"
    ]
    """<p>Displays a list of all of the probes created for a monitor.</p>"""
    aggregation_period: NotRequired[
        "capo_networkmonitor.types.aggregation_period.AggregationPeriod"
    ]
    """<p>The time, in seconds, that metrics are aggregated and sent to Amazon CloudWatch. Valid values are either <code>30</code> or <code>60</code>. <code>60</code> is the default if no period is chosen.</p>"""
    client_token: NotRequired["str"]
    """<p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>"""
    tags: NotRequired["capo_networkmonitor.types.tag_map.TagMap"]
    """<p>The list of key-value pairs created and assigned to the monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMonitorInput) -> dict:
    out: dict = {}
    out["monitorName"] = value["monitor_name"]
    if "probes" in value:
        import capo_networkmonitor.types.create_monitor_probe_input_list

        out["probes"] = (
            capo_networkmonitor.types.create_monitor_probe_input_list.serialize_json(
                value["probes"]
            )
        )
    if "aggregation_period" in value:
        out["aggregationPeriod"] = value["aggregation_period"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_networkmonitor.types.tag_map

        out["tags"] = capo_networkmonitor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMonitorInput:
    out: CreateMonitorInput = {}  # type: ignore[typeddict-item]
    if data.get("monitorName") is not None:
        out["monitor_name"] = data["monitorName"]
    else:
        out["monitor_name"] = ""
    if data.get("probes") is not None:
        import capo_networkmonitor.types.create_monitor_probe_input_list

        out["probes"] = (
            capo_networkmonitor.types.create_monitor_probe_input_list.deserialize_json(
                data["probes"]
            )
        )
    if data.get("aggregationPeriod") is not None:
        out["aggregation_period"] = data["aggregationPeriod"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_networkmonitor.types.tag_map

        out["tags"] = capo_networkmonitor.types.tag_map.deserialize_json(data["tags"])
    return out
