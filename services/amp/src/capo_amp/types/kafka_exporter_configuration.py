"""Generated from Smithy shape ``com.amazonaws.amp#KafkaExporterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.kafka_exporter_filter
    import capo_amp.types.msk_cluster_arn


class KafkaExporterConfiguration(TypedDict, closed=True):
    cluster_arn: "capo_amp.types.msk_cluster_arn.MskClusterArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon MSK cluster.</p>"""
    topic_filter: NotRequired[
        "capo_amp.types.kafka_exporter_filter.KafkaExporterFilter"
    ]
    """<p>An anchored RE2 regular expression that selects the Kafka topics to monitor. The expression must start with <code>^</code> and end with <code>$</code>. If omitted, the default is <code>^.*$</code>, which selects all topics.</p>"""
    consumer_group_filter: NotRequired[
        "capo_amp.types.kafka_exporter_filter.KafkaExporterFilter"
    ]
    """<p>An anchored RE2 regular expression that selects the Kafka consumer groups to monitor. The expression must start with <code>^</code> and end with <code>$</code>. If omitted, the default is <code>^.*$</code>, which selects all consumer groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaExporterConfiguration) -> dict:
    out: dict = {}
    out["clusterArn"] = value["cluster_arn"]
    if "topic_filter" in value:
        out["topicFilter"] = value["topic_filter"]
    if "consumer_group_filter" in value:
        out["consumerGroupFilter"] = value["consumer_group_filter"]
    return out


def deserialize_json(data: dict) -> KafkaExporterConfiguration:
    out: KafkaExporterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    else:
        out["cluster_arn"] = ""
    if data.get("topicFilter") is not None:
        out["topic_filter"] = data["topicFilter"]
    if data.get("consumerGroupFilter") is not None:
        out["consumer_group_filter"] = data["consumerGroupFilter"]
    return out
