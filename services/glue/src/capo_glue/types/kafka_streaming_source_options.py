"""Generated from Smithy shape ``com.amazonaws.glue#KafkaStreamingSourceOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boxed_boolean
    import capo_glue.types.boxed_non_negative_int
    import capo_glue.types.boxed_non_negative_long
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.iso8601_date_time


class KafkaStreamingSourceOptions(TypedDict, closed=True):
    bootstrap_servers: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>A list of bootstrap server URLs, for example, as <code>b-1.vpc-test-2.o4q88o.c6.kafka.us-east-1.amazonaws.com:9094</code>. This option must be specified in the API call or defined in the table metadata in the Data Catalog.</p>"""
    security_protocol: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The protocol used to communicate with brokers. The possible values are <code>"SSL"</code> or <code>"PLAINTEXT"</code>.</p>"""
    connection_name: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The name of the connection.</p>"""
    topic_name: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The topic name as specified in Apache Kafka. You must specify at least one of <code>"topicName"</code>, <code>"assign"</code> or <code>"subscribePattern"</code>.</p>"""
    assign: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The specific <code>TopicPartitions</code> to consume. You must specify at least one of <code>"topicName"</code>, <code>"assign"</code> or <code>"subscribePattern"</code>.</p>"""
    subscribe_pattern: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>A Java regex string that identifies the topic list to subscribe to. You must specify at least one of <code>"topicName"</code>, <code>"assign"</code> or <code>"subscribePattern"</code>.</p>"""
    classification: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>An optional classification.</p>"""
    delimiter: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Specifies the delimiter character.</p>"""
    starting_offsets: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The starting position in the Kafka topic to read data from. The possible values are <code>"earliest"</code> or <code>"latest"</code>. The default value is <code>"latest"</code>.</p>"""
    ending_offsets: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The end point when a batch query is ended. Possible values are either <code>"latest"</code> or a JSON string that specifies an ending offset for each <code>TopicPartition</code>.</p>"""
    poll_timeout_ms: NotRequired[
        "capo_glue.types.boxed_non_negative_long.BoxedNonNegativeLong"
    ]
    """<p>The timeout in milliseconds to poll data from Kafka in Spark job executors. The default value is <code>512</code>.</p>"""
    num_retries: NotRequired[
        "capo_glue.types.boxed_non_negative_int.BoxedNonNegativeInt"
    ]
    """<p>The number of times to retry before failing to fetch Kafka offsets. The default value is <code>3</code>.</p>"""
    retry_interval_ms: NotRequired[
        "capo_glue.types.boxed_non_negative_long.BoxedNonNegativeLong"
    ]
    """<p>The time in milliseconds to wait before retrying to fetch Kafka offsets. The default value is <code>10</code>.</p>"""
    max_offsets_per_trigger: NotRequired[
        "capo_glue.types.boxed_non_negative_long.BoxedNonNegativeLong"
    ]
    """<p>The rate limit on the maximum number of offsets that are processed per trigger interval. The specified total number of offsets is proportionally split across <code>topicPartitions</code> of different volumes. The default value is null, which means that the consumer reads all offsets until the known latest offset.</p>"""
    min_partitions: NotRequired[
        "capo_glue.types.boxed_non_negative_int.BoxedNonNegativeInt"
    ]
    """<p>The desired minimum number of partitions to read from Kafka. The default value is null, which means that the number of spark partitions is equal to the number of Kafka partitions.</p>"""
    include_headers: NotRequired["capo_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>Whether to include the Kafka headers. When the option is set to "true", the data output will contain an additional column named "glue_streaming_kafka_headers" with type <code>Array[Struct(key: String, value: String)]</code>. The default value is "false". This option is available in Glue version 3.0 or later only.</p>"""
    add_record_timestamp: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>When this option is set to 'true', the data output will contain an additional column named "__src_timestamp" that indicates the time when the corresponding record received by the topic. The default value is 'false'. This option is supported in Glue version 4.0 or later.</p>"""
    emit_consumer_lag_metrics: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>When this option is set to 'true', for each batch, it will emit the metrics for the duration between the oldest record received by the topic and the time it arrives in Glue to CloudWatch. The metric's name is "glue.driver.streaming.maxConsumerLagInMs". The default value is 'false'. This option is supported in Glue version 4.0 or later.</p>"""
    starting_timestamp: NotRequired["capo_glue.types.iso8601_date_time.Iso8601DateTime"]
    """<p>The timestamp of the record in the Kafka topic to start reading data from. The possible values are a timestamp string in UTC format of the pattern <code>yyyy-mm-ddTHH:MM:SSZ</code> (where Z represents a UTC timezone offset with a +/-. For example: "2023-04-04T08:00:00+08:00"). </p> <p>Only one of <code>StartingTimestamp</code> or <code>StartingOffsets</code> must be set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KafkaStreamingSourceOptions) -> dict:
    out: dict = {}
    if "bootstrap_servers" in value:
        out["BootstrapServers"] = value["bootstrap_servers"]
    if "security_protocol" in value:
        out["SecurityProtocol"] = value["security_protocol"]
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "topic_name" in value:
        out["TopicName"] = value["topic_name"]
    if "assign" in value:
        out["Assign"] = value["assign"]
    if "subscribe_pattern" in value:
        out["SubscribePattern"] = value["subscribe_pattern"]
    if "classification" in value:
        out["Classification"] = value["classification"]
    if "delimiter" in value:
        out["Delimiter"] = value["delimiter"]
    if "starting_offsets" in value:
        out["StartingOffsets"] = value["starting_offsets"]
    if "ending_offsets" in value:
        out["EndingOffsets"] = value["ending_offsets"]
    if "poll_timeout_ms" in value:
        out["PollTimeoutMs"] = value["poll_timeout_ms"]
    if "num_retries" in value:
        out["NumRetries"] = value["num_retries"]
    if "retry_interval_ms" in value:
        out["RetryIntervalMs"] = value["retry_interval_ms"]
    if "max_offsets_per_trigger" in value:
        out["MaxOffsetsPerTrigger"] = value["max_offsets_per_trigger"]
    if "min_partitions" in value:
        out["MinPartitions"] = value["min_partitions"]
    if "include_headers" in value:
        out["IncludeHeaders"] = value["include_headers"]
    if "add_record_timestamp" in value:
        out["AddRecordTimestamp"] = value["add_record_timestamp"]
    if "emit_consumer_lag_metrics" in value:
        out["EmitConsumerLagMetrics"] = value["emit_consumer_lag_metrics"]
    if "starting_timestamp" in value:
        import capo_glue.types.iso8601_date_time

        out["StartingTimestamp"] = (
            capo_glue.types.iso8601_date_time.serialize_aws_json_1_1(
                value["starting_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> KafkaStreamingSourceOptions:
    out: KafkaStreamingSourceOptions = {}  # type: ignore[typeddict-item]
    if data.get("BootstrapServers") is not None:
        out["bootstrap_servers"] = data["BootstrapServers"]
    if data.get("SecurityProtocol") is not None:
        out["security_protocol"] = data["SecurityProtocol"]
    if data.get("ConnectionName") is not None:
        out["connection_name"] = data["ConnectionName"]
    if data.get("TopicName") is not None:
        out["topic_name"] = data["TopicName"]
    if data.get("Assign") is not None:
        out["assign"] = data["Assign"]
    if data.get("SubscribePattern") is not None:
        out["subscribe_pattern"] = data["SubscribePattern"]
    if data.get("Classification") is not None:
        out["classification"] = data["Classification"]
    if data.get("Delimiter") is not None:
        out["delimiter"] = data["Delimiter"]
    if data.get("StartingOffsets") is not None:
        out["starting_offsets"] = data["StartingOffsets"]
    if data.get("EndingOffsets") is not None:
        out["ending_offsets"] = data["EndingOffsets"]
    if data.get("PollTimeoutMs") is not None:
        out["poll_timeout_ms"] = data["PollTimeoutMs"]
    if data.get("NumRetries") is not None:
        out["num_retries"] = data["NumRetries"]
    if data.get("RetryIntervalMs") is not None:
        out["retry_interval_ms"] = data["RetryIntervalMs"]
    if data.get("MaxOffsetsPerTrigger") is not None:
        out["max_offsets_per_trigger"] = data["MaxOffsetsPerTrigger"]
    if data.get("MinPartitions") is not None:
        out["min_partitions"] = data["MinPartitions"]
    if data.get("IncludeHeaders") is not None:
        out["include_headers"] = data["IncludeHeaders"]
    if data.get("AddRecordTimestamp") is not None:
        out["add_record_timestamp"] = data["AddRecordTimestamp"]
    if data.get("EmitConsumerLagMetrics") is not None:
        out["emit_consumer_lag_metrics"] = data["EmitConsumerLagMetrics"]
    if data.get("StartingTimestamp") is not None:
        import capo_glue.types.iso8601_date_time

        out["starting_timestamp"] = (
            capo_glue.types.iso8601_date_time.deserialize_aws_json_1_1(
                data["StartingTimestamp"]
            )
        )
    return out
