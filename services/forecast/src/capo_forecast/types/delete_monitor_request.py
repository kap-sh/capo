"""Generated from Smithy shape ``com.amazonaws.forecast#DeleteMonitorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn


class DeleteMonitorRequest(TypedDict, closed=True):
    monitor_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the monitor resource to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMonitorRequest) -> dict:
    out: dict = {}
    out["MonitorArn"] = value["monitor_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMonitorRequest:
    out: DeleteMonitorRequest = {}  # type: ignore[typeddict-item]
    if data.get("MonitorArn") is not None:
        out["monitor_arn"] = data["MonitorArn"]
    else:
        out["monitor_arn"] = ""
    return out
