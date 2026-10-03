"""Generated from Smithy shape ``com.amazonaws.lambda#EventSourceMappingMetricsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.event_source_mapping_metric_list


class EventSourceMappingMetricsConfig(TypedDict, closed=True):
    metrics: NotRequired[
        "capo_lambda.types.event_source_mapping_metric_list.EventSourceMappingMetricList"
    ]
    """<p> The metrics you want your event source mapping to produce, including <code>EventCount</code>, <code>ErrorCount</code>, <code>KafkaMetrics</code>. </p> <ul> <li> <p> <code>EventCount</code> to receive metrics related to the number of events processed by your event source mapping.</p> </li> <li> <p> <code>ErrorCount</code> (Amazon MSK and self-managed Apache Kafka) to receive metrics related to the number of errors in your event source mapping processing.</p> </li> <li> <p> <code>KafkaMetrics</code> (Amazon MSK and self-managed Apache Kafka) to receive metrics related to the Kafka consumers from your event source mapping.</p> </li> </ul> <p> For more information about these metrics, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics"> Event source mapping metrics</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventSourceMappingMetricsConfig) -> dict:
    out: dict = {}
    if "metrics" in value:
        import capo_lambda.types.event_source_mapping_metric_list

        out["Metrics"] = (
            capo_lambda.types.event_source_mapping_metric_list.serialize_json(
                value["metrics"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventSourceMappingMetricsConfig:
    out: EventSourceMappingMetricsConfig = {}  # type: ignore[typeddict-item]
    if data.get("Metrics") is not None:
        import capo_lambda.types.event_source_mapping_metric_list

        out["metrics"] = (
            capo_lambda.types.event_source_mapping_metric_list.deserialize_json(
                data["Metrics"]
            )
        )
    return out
