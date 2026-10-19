"""Generated from Smithy shape ``com.amazonaws.costexplorer#UpdateAnomalyMonitorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string


class UpdateAnomalyMonitorResponse(TypedDict, closed=True):
    monitor_arn: "capo_cost_explorer.types.generic_string.GenericString"
    """<p>A cost anomaly monitor ARN. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAnomalyMonitorResponse) -> dict:
    out: dict = {}
    out["MonitorArn"] = value["monitor_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAnomalyMonitorResponse:
    out: UpdateAnomalyMonitorResponse = {}  # type: ignore[typeddict-item]
    if data.get("MonitorArn") is not None:
        out["monitor_arn"] = data["MonitorArn"]
    else:
        out["monitor_arn"] = ""
    return out
