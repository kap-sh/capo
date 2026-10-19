"""Generated from Smithy shape ``com.amazonaws.costexplorer#UpdateAnomalyMonitorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string


class UpdateAnomalyMonitorRequest(TypedDict, closed=True):
    monitor_arn: "capo_cost_explorer.types.generic_string.GenericString"
    """<p>Cost anomaly monitor Amazon Resource Names (ARNs). </p>"""
    monitor_name: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The new name for the cost anomaly monitor. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAnomalyMonitorRequest) -> dict:
    out: dict = {}
    out["MonitorArn"] = value["monitor_arn"]
    if "monitor_name" in value:
        out["MonitorName"] = value["monitor_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAnomalyMonitorRequest:
    out: UpdateAnomalyMonitorRequest = {}  # type: ignore[typeddict-item]
    if data.get("MonitorArn") is not None:
        out["monitor_arn"] = data["MonitorArn"]
    else:
        out["monitor_arn"] = ""
    if data.get("MonitorName") is not None:
        out["monitor_name"] = data["MonitorName"]
    return out
