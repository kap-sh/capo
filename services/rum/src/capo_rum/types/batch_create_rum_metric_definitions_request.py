"""Generated from Smithy shape ``com.amazonaws.rum#BatchCreateRumMetricDefinitionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rum.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rum.types.app_monitor_name
    import capo_rum.types.destination_arn
    import capo_rum.types.metric_definitions_request
    import capo_rum.types.metric_destination


class BatchCreateRumMetricDefinitionsRequest(TypedDict, closed=True):
    app_monitor_name: "capo_rum.types.app_monitor_name.AppMonitorName"
    """<p>The name of the CloudWatch RUM app monitor that is to send the metrics.</p>"""
    destination: "capo_rum.types.metric_destination.MetricDestination"
    """<p>The destination to send the metrics to. Valid values are <code>CloudWatch</code> and <code>Evidently</code>. If you specify <code>Evidently</code>, you must also specify the Amazon Resource Name (ARN) of the CloudWatchEvidently experiment that will receive the metrics and an IAM role that has permission to write to the experiment.</p>"""
    destination_arn: NotRequired["capo_rum.types.destination_arn.DestinationArn"]
    """<p>This parameter is required if <code>Destination</code> is <code>Evidently</code>. If <code>Destination</code> is <code>CloudWatch</code>, do not use this parameter.</p> <p>This parameter specifies the ARN of the Evidently experiment that is to receive the metrics. You must have already defined this experiment as a valid destination. For more information, see <a href="https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html">PutRumMetricsDestination</a>.</p>"""
    metric_definitions: (
        "capo_rum.types.metric_definitions_request.MetricDefinitionsRequest"
    )
    """<p>An array of structures which define the metrics that you want to send.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateRumMetricDefinitionsRequest) -> dict:
    out: dict = {}
    out["Destination"] = value["destination"]
    if "destination_arn" in value:
        out["DestinationArn"] = value["destination_arn"]
    import capo_rum.types.metric_definitions_request

    out["MetricDefinitions"] = capo_rum.types.metric_definitions_request.serialize_json(
        value["metric_definitions"]
    )
    return out


def deserialize_json(data: dict) -> BatchCreateRumMetricDefinitionsRequest:
    out: BatchCreateRumMetricDefinitionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Destination") is not None:
        out["destination"] = data["Destination"]
    else:
        raise DeserializationError(
            "BatchCreateRumMetricDefinitionsRequest.destination required"
        )
    if data.get("DestinationArn") is not None:
        out["destination_arn"] = data["DestinationArn"]
    if data.get("MetricDefinitions") is not None:
        import capo_rum.types.metric_definitions_request

        out["metric_definitions"] = (
            capo_rum.types.metric_definitions_request.deserialize_json(
                data["MetricDefinitions"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateRumMetricDefinitionsRequest.metric_definitions required"
        )
    return out
