"""Generated from Smithy shape ``com.amazonaws.pipes#PipeSourceParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.filter_criteria
    import capo_pipes.types.pipe_source_active_mq_broker_parameters
    import capo_pipes.types.pipe_source_dynamo_db_stream_parameters
    import capo_pipes.types.pipe_source_kinesis_stream_parameters
    import capo_pipes.types.pipe_source_managed_streaming_kafka_parameters
    import capo_pipes.types.pipe_source_rabbit_mq_broker_parameters
    import capo_pipes.types.pipe_source_self_managed_kafka_parameters
    import capo_pipes.types.pipe_source_sqs_queue_parameters


class PipeSourceParameters(TypedDict, closed=True):
    filter_criteria: NotRequired["capo_pipes.types.filter_criteria.FilterCriteria"]
    """<p>The collection of event patterns used to filter events.</p> <p>To remove a filter, specify a <code>FilterCriteria</code> object with an empty array of <code>Filter</code> objects.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html">Events and Event Patterns</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    kinesis_stream_parameters: NotRequired[
        "capo_pipes.types.pipe_source_kinesis_stream_parameters.PipeSourceKinesisStreamParameters"
    ]
    """<p>The parameters for using a Kinesis stream as a source.</p>"""
    dynamo_db_stream_parameters: NotRequired[
        "capo_pipes.types.pipe_source_dynamo_db_stream_parameters.PipeSourceDynamoDBStreamParameters"
    ]
    """<p>The parameters for using a DynamoDB stream as a source.</p>"""
    sqs_queue_parameters: NotRequired[
        "capo_pipes.types.pipe_source_sqs_queue_parameters.PipeSourceSqsQueueParameters"
    ]
    """<p>The parameters for using a Amazon SQS stream as a source.</p>"""
    active_mq_broker_parameters: NotRequired[
        "capo_pipes.types.pipe_source_active_mq_broker_parameters.PipeSourceActiveMQBrokerParameters"
    ]
    """<p>The parameters for using an Active MQ broker as a source.</p>"""
    rabbit_mq_broker_parameters: NotRequired[
        "capo_pipes.types.pipe_source_rabbit_mq_broker_parameters.PipeSourceRabbitMQBrokerParameters"
    ]
    """<p>The parameters for using a Rabbit MQ broker as a source.</p>"""
    managed_streaming_kafka_parameters: NotRequired[
        "capo_pipes.types.pipe_source_managed_streaming_kafka_parameters.PipeSourceManagedStreamingKafkaParameters"
    ]
    """<p>The parameters for using an MSK stream as a source.</p>"""
    self_managed_kafka_parameters: NotRequired[
        "capo_pipes.types.pipe_source_self_managed_kafka_parameters.PipeSourceSelfManagedKafkaParameters"
    ]
    """<p>The parameters for using a self-managed Apache Kafka stream as a source.</p> <p>A <i>self managed</i> cluster refers to any Apache Kafka cluster not hosted by Amazon Web Services. This includes both clusters you manage yourself, as well as those hosted by a third-party provider, such as <a href="https://www.confluent.io/">Confluent Cloud</a>, <a href="https://www.cloudkarafka.com/">CloudKarafka</a>, or <a href="https://redpanda.com/">Redpanda</a>. For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-kafka.html">Apache Kafka streams as a source</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeSourceParameters) -> dict:
    out: dict = {}
    if "filter_criteria" in value:
        import capo_pipes.types.filter_criteria

        out["FilterCriteria"] = capo_pipes.types.filter_criteria.serialize_json(
            value["filter_criteria"]
        )
    if "kinesis_stream_parameters" in value:
        import capo_pipes.types.pipe_source_kinesis_stream_parameters

        out["KinesisStreamParameters"] = (
            capo_pipes.types.pipe_source_kinesis_stream_parameters.serialize_json(
                value["kinesis_stream_parameters"]
            )
        )
    if "dynamo_db_stream_parameters" in value:
        import capo_pipes.types.pipe_source_dynamo_db_stream_parameters

        out["DynamoDBStreamParameters"] = (
            capo_pipes.types.pipe_source_dynamo_db_stream_parameters.serialize_json(
                value["dynamo_db_stream_parameters"]
            )
        )
    if "sqs_queue_parameters" in value:
        import capo_pipes.types.pipe_source_sqs_queue_parameters

        out["SqsQueueParameters"] = (
            capo_pipes.types.pipe_source_sqs_queue_parameters.serialize_json(
                value["sqs_queue_parameters"]
            )
        )
    if "active_mq_broker_parameters" in value:
        import capo_pipes.types.pipe_source_active_mq_broker_parameters

        out["ActiveMQBrokerParameters"] = (
            capo_pipes.types.pipe_source_active_mq_broker_parameters.serialize_json(
                value["active_mq_broker_parameters"]
            )
        )
    if "rabbit_mq_broker_parameters" in value:
        import capo_pipes.types.pipe_source_rabbit_mq_broker_parameters

        out["RabbitMQBrokerParameters"] = (
            capo_pipes.types.pipe_source_rabbit_mq_broker_parameters.serialize_json(
                value["rabbit_mq_broker_parameters"]
            )
        )
    if "managed_streaming_kafka_parameters" in value:
        import capo_pipes.types.pipe_source_managed_streaming_kafka_parameters

        out["ManagedStreamingKafkaParameters"] = (
            capo_pipes.types.pipe_source_managed_streaming_kafka_parameters.serialize_json(
                value["managed_streaming_kafka_parameters"]
            )
        )
    if "self_managed_kafka_parameters" in value:
        import capo_pipes.types.pipe_source_self_managed_kafka_parameters

        out["SelfManagedKafkaParameters"] = (
            capo_pipes.types.pipe_source_self_managed_kafka_parameters.serialize_json(
                value["self_managed_kafka_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> PipeSourceParameters:
    out: PipeSourceParameters = {}  # type: ignore[typeddict-item]
    if data.get("FilterCriteria") is not None:
        import capo_pipes.types.filter_criteria

        out["filter_criteria"] = capo_pipes.types.filter_criteria.deserialize_json(
            data["FilterCriteria"]
        )
    if data.get("KinesisStreamParameters") is not None:
        import capo_pipes.types.pipe_source_kinesis_stream_parameters

        out["kinesis_stream_parameters"] = (
            capo_pipes.types.pipe_source_kinesis_stream_parameters.deserialize_json(
                data["KinesisStreamParameters"]
            )
        )
    if data.get("DynamoDBStreamParameters") is not None:
        import capo_pipes.types.pipe_source_dynamo_db_stream_parameters

        out["dynamo_db_stream_parameters"] = (
            capo_pipes.types.pipe_source_dynamo_db_stream_parameters.deserialize_json(
                data["DynamoDBStreamParameters"]
            )
        )
    if data.get("SqsQueueParameters") is not None:
        import capo_pipes.types.pipe_source_sqs_queue_parameters

        out["sqs_queue_parameters"] = (
            capo_pipes.types.pipe_source_sqs_queue_parameters.deserialize_json(
                data["SqsQueueParameters"]
            )
        )
    if data.get("ActiveMQBrokerParameters") is not None:
        import capo_pipes.types.pipe_source_active_mq_broker_parameters

        out["active_mq_broker_parameters"] = (
            capo_pipes.types.pipe_source_active_mq_broker_parameters.deserialize_json(
                data["ActiveMQBrokerParameters"]
            )
        )
    if data.get("RabbitMQBrokerParameters") is not None:
        import capo_pipes.types.pipe_source_rabbit_mq_broker_parameters

        out["rabbit_mq_broker_parameters"] = (
            capo_pipes.types.pipe_source_rabbit_mq_broker_parameters.deserialize_json(
                data["RabbitMQBrokerParameters"]
            )
        )
    if data.get("ManagedStreamingKafkaParameters") is not None:
        import capo_pipes.types.pipe_source_managed_streaming_kafka_parameters

        out["managed_streaming_kafka_parameters"] = (
            capo_pipes.types.pipe_source_managed_streaming_kafka_parameters.deserialize_json(
                data["ManagedStreamingKafkaParameters"]
            )
        )
    if data.get("SelfManagedKafkaParameters") is not None:
        import capo_pipes.types.pipe_source_self_managed_kafka_parameters

        out["self_managed_kafka_parameters"] = (
            capo_pipes.types.pipe_source_self_managed_kafka_parameters.deserialize_json(
                data["SelfManagedKafkaParameters"]
            )
        )
    return out
