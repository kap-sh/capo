"""Generated from Smithy shape ``com.amazonaws.costexplorer#DeleteAnomalyMonitorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string


class DeleteAnomalyMonitorRequest(TypedDict, closed=True):
    monitor_arn: "capo_cost_explorer.types.generic_string.GenericString"
    """<p>The unique identifier of the cost anomaly monitor that you want to delete. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAnomalyMonitorRequest) -> dict:
    out: dict = {}
    out["MonitorArn"] = value["monitor_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAnomalyMonitorRequest:
    out: DeleteAnomalyMonitorRequest = {}  # type: ignore[typeddict-item]
    if data.get("MonitorArn") is not None:
        out["monitor_arn"] = data["MonitorArn"]
    else:
        out["monitor_arn"] = ""
    return out
