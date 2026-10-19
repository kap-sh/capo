"""Generated from Smithy shape ``com.amazonaws.iot#UpdateCustomMetricRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.custom_metric_display_name
    import capo_iot.types.metric_name


class UpdateCustomMetricRequest(TypedDict, closed=True):
    metric_name: "capo_iot.types.metric_name.MetricName"
    """<p> The name of the custom metric. Cannot be updated. </p>"""
    display_name: "capo_iot.types.custom_metric_display_name.CustomMetricDisplayName"
    """<p> Field represents a friendly name in the console for the custom metric, it doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. Can be updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomMetricRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> UpdateCustomMetricRequest:
    out: UpdateCustomMetricRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    return out
