"""Generated from Smithy shape ``com.amazonaws.forecast#MonitorConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.name


class MonitorConfig(TypedDict, closed=True):
    monitor_name: "capo_forecast.types.name.Name"
    """<p>The name of the monitor resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitorConfig) -> dict:
    out: dict = {}
    out["MonitorName"] = value["monitor_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitorConfig:
    out: MonitorConfig = {}  # type: ignore[typeddict-item]
    if data.get("MonitorName") is not None:
        out["monitor_name"] = data["MonitorName"]
    else:
        out["monitor_name"] = ""
    return out
