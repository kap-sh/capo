"""Generated from Smithy shape ``com.amazonaws.costexplorer#CreateAnomalyMonitorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string


class CreateAnomalyMonitorResponse(TypedDict, closed=True):
    monitor_arn: "capo_cost_explorer.types.generic_string.GenericString"
    """<p>The unique identifier of your newly created cost anomaly detection monitor.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAnomalyMonitorResponse) -> dict:
    out: dict = {}
    out["MonitorArn"] = value["monitor_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAnomalyMonitorResponse:
    out: CreateAnomalyMonitorResponse = {}  # type: ignore[typeddict-item]
    if data.get("MonitorArn") is not None:
        out["monitor_arn"] = data["MonitorArn"]
    else:
        out["monitor_arn"] = ""
    return out
