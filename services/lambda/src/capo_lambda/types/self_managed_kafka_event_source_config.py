"""Generated from Smithy shape ``com.amazonaws.lambda#SelfManagedKafkaEventSourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.kafka_event_source_mapping_consumption_mode
    import capo_lambda.types.kafka_schema_registry_config
    import capo_lambda.types.uri


class SelfManagedKafkaEventSourceConfig(TypedDict, closed=True):
    consumer_group_id: NotRequired["capo_lambda.types.uri.URI"]
    """<p> The identifier for the Kafka consumer group to join. The consumer group ID must be unique among all your Kafka event sources. After creating a Kafka event source mapping with the consumer group ID specified, you cannot update this value. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-kafka-process.html#services-smaa-topic-add">Customizable consumer group ID</a>.</p>"""
    schema_registry_config: NotRequired[
        "capo_lambda.types.kafka_schema_registry_config.KafkaSchemaRegistryConfig"
    ]
    """<p>Specific configuration settings for a Kafka schema registry.</p>"""
    consumption_mode: NotRequired[
        "capo_lambda.types.kafka_event_source_mapping_consumption_mode.KafkaEventSourceMappingConsumptionMode"
    ]
    """<p>The mode that Lambda uses to consume records from your self-managed Apache Kafka topic. The default is <code>Stream</code>.</p> <ul> <li> <p> <code>Stream</code> – Lambda consumes records using a Kafka consumer group and preserves the order of records within each partition. This is the default when you omit <code>ConsumptionMode</code>.</p> </li> <li> <p> <code>Queue</code> – Lambda consumes records using a Kafka share group. Multiple consumers can process records from the same partitions concurrently. Queue mode does not preserve per-partition order. Queue mode requires an Apache Kafka cluster running version 4.2 or later with share groups enabled.</p> </li> </ul> <p>You cannot change <code>ConsumptionMode</code> after you create the event source mapping. To use a different consumption mode, create a new event source mapping.</p> <p>When <code>ConsumptionMode</code> is <code>Queue</code>, the <code>StartingPosition</code>, <code>StartingPositionTimestamp</code>, and <code>MaximumBatchingWindowInSeconds</code> parameters are not supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelfManagedKafkaEventSourceConfig) -> dict:
    out: dict = {}
    if "consumer_group_id" in value:
        out["ConsumerGroupId"] = value["consumer_group_id"]
    if "schema_registry_config" in value:
        import capo_lambda.types.kafka_schema_registry_config

        out["SchemaRegistryConfig"] = (
            capo_lambda.types.kafka_schema_registry_config.serialize_json(
                value["schema_registry_config"]
            )
        )
    if "consumption_mode" in value:
        import capo_lambda.types.kafka_event_source_mapping_consumption_mode

        out["ConsumptionMode"] = (
            capo_lambda.types.kafka_event_source_mapping_consumption_mode.serialize_json(
                value["consumption_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> SelfManagedKafkaEventSourceConfig:
    out: SelfManagedKafkaEventSourceConfig = {}  # type: ignore[typeddict-item]
    if data.get("ConsumerGroupId") is not None:
        out["consumer_group_id"] = data["ConsumerGroupId"]
    if data.get("SchemaRegistryConfig") is not None:
        import capo_lambda.types.kafka_schema_registry_config

        out["schema_registry_config"] = (
            capo_lambda.types.kafka_schema_registry_config.deserialize_json(
                data["SchemaRegistryConfig"]
            )
        )
    if data.get("ConsumptionMode") is not None:
        import capo_lambda.types.kafka_event_source_mapping_consumption_mode

        out["consumption_mode"] = (
            capo_lambda.types.kafka_event_source_mapping_consumption_mode.deserialize_json(
                data["ConsumptionMode"]
            )
        )
    return out
