"""Generated from Smithy shape ``com.amazonaws.connect#CreateMetricRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.instance_id
    import capo_connect.types.metric_calculation
    import capo_connect.types.metric_description
    import capo_connect.types.metric_name
    import capo_connect.types.metric_status
    import capo_connect.types.metric_unit
    import capo_connect.types.tag_map
    import capo_connect.types.trend_indicator


class CreateMetricRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "capo_connect.types.metric_name.MetricName"
    """<p>The name of the metric.</p>"""
    metric_calculation: "capo_connect.types.metric_calculation.MetricCalculation"
    """<p>The calculation definition for the metric, including the formula expression and the component metrics it references.</p>"""
    unit: "capo_connect.types.metric_unit.MetricUnit"
    """<p>The display unit for the metric's data.</p>"""
    status: NotRequired["capo_connect.types.metric_status.MetricStatus"]
    """<p>The publish status of the metric. Set to <code>PUBLISHED</code> to make the metric available for use in dashboards and reports, or <code>SAVED</code> to keep it in draft state.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    description: NotRequired["capo_connect.types.metric_description.MetricDescription"]
    """<p>The description of the metric.</p>"""
    positive_trend_indicator: NotRequired[
        "capo_connect.types.trend_indicator.TrendIndicator"
    ]
    """<p>How an increase in the metric value should be interpreted. Valid values: <code>POSITIVE</code>, <code>NEUTRAL</code>, <code>NEGATIVE</code>.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMetricRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_connect.types.metric_calculation

    out["MetricCalculation"] = capo_connect.types.metric_calculation.serialize_json(
        value["metric_calculation"]
    )
    import capo_connect.types.metric_unit

    out["Unit"] = capo_connect.types.metric_unit.serialize_json(value["unit"])
    if "status" in value:
        import capo_connect.types.metric_status

        out["Status"] = capo_connect.types.metric_status.serialize_json(value["status"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "description" in value:
        out["Description"] = value["description"]
    if "positive_trend_indicator" in value:
        import capo_connect.types.trend_indicator

        out["PositiveTrendIndicator"] = (
            capo_connect.types.trend_indicator.serialize_json(
                value["positive_trend_indicator"]
            )
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMetricRequest:
    out: CreateMetricRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateMetricRequest.name required")
    if data.get("MetricCalculation") is not None:
        import capo_connect.types.metric_calculation

        out["metric_calculation"] = (
            capo_connect.types.metric_calculation.deserialize_json(
                data["MetricCalculation"]
            )
        )
    else:
        raise DeserializationError("CreateMetricRequest.metric_calculation required")
    if data.get("Unit") is not None:
        import capo_connect.types.metric_unit

        out["unit"] = capo_connect.types.metric_unit.deserialize_json(data["Unit"])
    else:
        raise DeserializationError("CreateMetricRequest.unit required")
    if data.get("Status") is not None:
        import capo_connect.types.metric_status

        out["status"] = capo_connect.types.metric_status.deserialize_json(
            data["Status"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("PositiveTrendIndicator") is not None:
        import capo_connect.types.trend_indicator

        out["positive_trend_indicator"] = (
            capo_connect.types.trend_indicator.deserialize_json(
                data["PositiveTrendIndicator"]
            )
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
