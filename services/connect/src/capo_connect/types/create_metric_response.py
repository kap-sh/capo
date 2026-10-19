"""Generated from Smithy shape ``com.amazonaws.connect#CreateMetricResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.metric_id


class CreateMetricResponse(TypedDict, closed=True):
    metric_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the metric.</p>"""
    metric_id: "capo_connect.types.metric_id.MetricId"
    """<p>The identifier of the metric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMetricResponse) -> dict:
    out: dict = {}
    out["MetricArn"] = value["metric_arn"]
    out["MetricId"] = value["metric_id"]
    return out


def deserialize_json(data: dict) -> CreateMetricResponse:
    out: CreateMetricResponse = {}  # type: ignore[typeddict-item]
    if data.get("MetricArn") is not None:
        out["metric_arn"] = data["MetricArn"]
    else:
        out["metric_arn"] = ""
    if data.get("MetricId") is not None:
        out["metric_id"] = data["MetricId"]
    else:
        out["metric_id"] = ""
    return out
