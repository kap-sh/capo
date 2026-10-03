"""Generated from Smithy shape ``com.amazonaws.connect#UpdateMetricContentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.metric_calculation
    import capo_connect.types.metric_id
    import capo_connect.types.metric_unit
    import capo_connect.types.trend_indicator


class UpdateMetricContentRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    metric_id: "capo_connect.types.metric_id.MetricId"
    """<p>The identifier of the metric to update. Adding the <code>$SAVED</code> qualifier will update the saved version of the metric. Adding <code>$LATEST</code> or omitting a qualifier will update the published version.</p>"""
    metric_calculation: NotRequired[
        "capo_connect.types.metric_calculation.MetricCalculation"
    ]
    """<p>The updated calculation definition for the metric.</p>"""
    unit: NotRequired["capo_connect.types.metric_unit.MetricUnit"]
    """<p>The updated display unit for the metric.</p>"""
    positive_trend_indicator: NotRequired[
        "capo_connect.types.trend_indicator.TrendIndicator"
    ]
    """<p>How an increase in the metric value should be interpreted. Valid values: <code>POSITIVE</code>, <code>NEUTRAL</code>, <code>NEGATIVE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMetricContentRequest) -> dict:
    out: dict = {}
    if "metric_calculation" in value:
        import capo_connect.types.metric_calculation

        out["MetricCalculation"] = capo_connect.types.metric_calculation.serialize_json(
            value["metric_calculation"]
        )
    if "unit" in value:
        import capo_connect.types.metric_unit

        out["Unit"] = capo_connect.types.metric_unit.serialize_json(value["unit"])
    if "positive_trend_indicator" in value:
        import capo_connect.types.trend_indicator

        out["PositiveTrendIndicator"] = (
            capo_connect.types.trend_indicator.serialize_json(
                value["positive_trend_indicator"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMetricContentRequest:
    out: UpdateMetricContentRequest = {}  # type: ignore[typeddict-item]
    if data.get("MetricCalculation") is not None:
        import capo_connect.types.metric_calculation

        out["metric_calculation"] = (
            capo_connect.types.metric_calculation.deserialize_json(
                data["MetricCalculation"]
            )
        )
    if data.get("Unit") is not None:
        import capo_connect.types.metric_unit

        out["unit"] = capo_connect.types.metric_unit.deserialize_json(data["Unit"])
    if data.get("PositiveTrendIndicator") is not None:
        import capo_connect.types.trend_indicator

        out["positive_trend_indicator"] = (
            capo_connect.types.trend_indicator.deserialize_json(
                data["PositiveTrendIndicator"]
            )
        )
    return out
