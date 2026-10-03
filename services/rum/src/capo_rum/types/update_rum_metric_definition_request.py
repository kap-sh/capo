"""Generated from Smithy shape ``com.amazonaws.rum#UpdateRumMetricDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rum.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rum.types.app_monitor_name
    import capo_rum.types.destination_arn
    import capo_rum.types.metric_definition_id
    import capo_rum.types.metric_definition_request
    import capo_rum.types.metric_destination


class UpdateRumMetricDefinitionRequest(TypedDict, closed=True):
    app_monitor_name: "capo_rum.types.app_monitor_name.AppMonitorName"
    """<p>The name of the CloudWatch RUM app monitor that sends these metrics.</p>"""
    destination: "capo_rum.types.metric_destination.MetricDestination"
    """<p>The destination to send the metrics to. Valid values are <code>CloudWatch</code> and <code>Evidently</code>. If you specify <code>Evidently</code>, you must also specify the ARN of the CloudWatchEvidently experiment that will receive the metrics and an IAM role that has permission to write to the experiment.</p>"""
    destination_arn: NotRequired["capo_rum.types.destination_arn.DestinationArn"]
    """<p>This parameter is required if <code>Destination</code> is <code>Evidently</code>. If <code>Destination</code> is <code>CloudWatch</code>, do not use this parameter.</p> <p>This parameter specifies the ARN of the Evidently experiment that is to receive the metrics. You must have already defined this experiment as a valid destination. For more information, see <a href="https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html">PutRumMetricsDestination</a>.</p>"""
    metric_definition: (
        "capo_rum.types.metric_definition_request.MetricDefinitionRequest"
    )
    """<p>A structure that contains the new definition that you want to use for this metric.</p>"""
    metric_definition_id: "capo_rum.types.metric_definition_id.MetricDefinitionId"
    """<p>The ID of the metric definition to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRumMetricDefinitionRequest) -> dict:
    out: dict = {}
    out["Destination"] = value["destination"]
    if "destination_arn" in value:
        out["DestinationArn"] = value["destination_arn"]
    import capo_rum.types.metric_definition_request

    out["MetricDefinition"] = capo_rum.types.metric_definition_request.serialize_json(
        value["metric_definition"]
    )
    out["MetricDefinitionId"] = value["metric_definition_id"]
    return out


def deserialize_json(data: dict) -> UpdateRumMetricDefinitionRequest:
    out: UpdateRumMetricDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Destination") is not None:
        out["destination"] = data["Destination"]
    else:
        raise DeserializationError(
            "UpdateRumMetricDefinitionRequest.destination required"
        )
    if data.get("DestinationArn") is not None:
        out["destination_arn"] = data["DestinationArn"]
    if data.get("MetricDefinition") is not None:
        import capo_rum.types.metric_definition_request

        out["metric_definition"] = (
            capo_rum.types.metric_definition_request.deserialize_json(
                data["MetricDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRumMetricDefinitionRequest.metric_definition required"
        )
    if data.get("MetricDefinitionId") is not None:
        out["metric_definition_id"] = data["MetricDefinitionId"]
    else:
        raise DeserializationError(
            "UpdateRumMetricDefinitionRequest.metric_definition_id required"
        )
    return out
