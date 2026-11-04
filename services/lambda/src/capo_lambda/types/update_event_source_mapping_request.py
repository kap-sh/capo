"""Generated from Smithy shape ``com.amazonaws.lambda#UpdateEventSourceMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.amazon_managed_kafka_event_source_config
    import capo_lambda.types.batch_size
    import capo_lambda.types.bisect_batch_on_function_error
    import capo_lambda.types.destination_config
    import capo_lambda.types.document_db_event_source_config
    import capo_lambda.types.enabled
    import capo_lambda.types.event_source_mapping_logging_config
    import capo_lambda.types.event_source_mapping_metrics_config
    import capo_lambda.types.filter_criteria
    import capo_lambda.types.function_response_type_list
    import capo_lambda.types.kms_key_arn
    import capo_lambda.types.maximum_batching_window_in_seconds
    import capo_lambda.types.maximum_record_age_in_seconds
    import capo_lambda.types.maximum_retry_attempts_event_source_mapping
    import capo_lambda.types.namespaced_function_name
    import capo_lambda.types.parallelization_factor
    import capo_lambda.types.provisioned_poller_config
    import capo_lambda.types.scaling_config
    import capo_lambda.types.self_managed_kafka_event_source_config
    import capo_lambda.types.source_access_configurations
    import capo_lambda.types.tumbling_window_in_seconds
    import capo_lambda.types.uuid_string


class UpdateEventSourceMappingRequest(TypedDict, closed=True):
    uuid: "capo_lambda.types.uuid_string.UUIDString"
    """<p>The identifier of the event source mapping.</p>"""
    function_name: NotRequired[
        "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
    ]
    """<p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Version or Alias ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.</p>"""
    enabled: NotRequired["capo_lambda.types.enabled.Enabled"]
    """<p>When true, the event source mapping is active. When false, Lambda pauses polling and invocation.</p> <p>Default: True</p>"""
    batch_size: NotRequired["capo_lambda.types.batch_size.BatchSize"]
    """<p>The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).</p> <ul> <li> <p> <b>Amazon Kinesis</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon DynamoDB Streams</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon Simple Queue Service</b> – Default 10. For standard queues the max is 10,000. For FIFO queues the max is 10.</p> </li> <li> <p> <b>Amazon Managed Streaming for Apache Kafka</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Self-managed Apache Kafka</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon MQ (ActiveMQ and RabbitMQ)</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>DocumentDB</b> – Default 100. Max 10,000.</p> </li> </ul>"""
    filter_criteria: NotRequired["capo_lambda.types.filter_criteria.FilterCriteria"]
    """<p>An object that defines the filter criteria that determine whether Lambda should process an event. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html">Lambda event filtering</a>.</p>"""
    kms_key_arn: NotRequired["capo_lambda.types.kms_key_arn.KMSKeyArn"]
    """<p> The ARN of the Key Management Service (KMS) customer managed key that Lambda uses to encrypt your function's <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-basics">filter criteria</a>. By default, Lambda does not encrypt your filter criteria object. Specify this property to encrypt data using your own customer managed key. </p>"""
    metrics_config: NotRequired[
        "capo_lambda.types.event_source_mapping_metrics_config.EventSourceMappingMetricsConfig"
    ]
    """<p>The metrics configuration for your event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics">Event source mapping metrics</a>.</p>"""
    logging_config: NotRequired[
        "capo_lambda.types.event_source_mapping_logging_config.EventSourceMappingLoggingConfig"
    ]
    scaling_config: NotRequired["capo_lambda.types.scaling_config.ScalingConfig"]
    """<p>(Amazon SQS only) The scaling configuration for the event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-max-concurrency">Configuring maximum concurrency for Amazon SQS event sources</a>.</p>"""
    maximum_batching_window_in_seconds: NotRequired[
        "capo_lambda.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
    ]
    """<p>The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function. You can configure <code>MaximumBatchingWindowInSeconds</code> to any value from 0 seconds to 300 seconds in increments of seconds.</p> <p>For Kinesis, DynamoDB, and Amazon SQS event sources, the default batching window is 0 seconds. For Amazon MSK, Self-managed Apache Kafka, Amazon MQ, and DocumentDB event sources, the default batching window is 500 ms. Note that because you can only change <code>MaximumBatchingWindowInSeconds</code> in increments of seconds, you cannot revert back to the 500 ms default batching window after you have changed it. To restore the default batching window, you must create a new event source mapping.</p> <p>Related setting: For Kinesis, DynamoDB, and Amazon SQS event sources, when you set <code>BatchSize</code> to a value greater than 10, you must set <code>MaximumBatchingWindowInSeconds</code> to at least 1.</p>"""
    parallelization_factor: NotRequired[
        "capo_lambda.types.parallelization_factor.ParallelizationFactor"
    ]
    """<p>(Kinesis and DynamoDB Streams only) The number of batches to process from each shard concurrently.</p>"""
    destination_config: NotRequired[
        "capo_lambda.types.destination_config.DestinationConfig"
    ]
    """<p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) A configuration object that specifies the destination of an event after Lambda processes it.</p>"""
    maximum_record_age_in_seconds: NotRequired[
        "capo_lambda.types.maximum_record_age_in_seconds.MaximumRecordAgeInSeconds"
    ]
    """<p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records older than the specified age. The default value is infinite (-1).</p>"""
    bisect_batch_on_function_error: NotRequired[
        "capo_lambda.types.bisect_batch_on_function_error.BisectBatchOnFunctionError"
    ]
    """<p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) If the function returns an error, split the batch in two and retry.</p>"""
    maximum_retry_attempts: NotRequired[
        "capo_lambda.types.maximum_retry_attempts_event_source_mapping.MaximumRetryAttemptsEventSourceMapping"
    ]
    """<p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires.</p>"""
    tumbling_window_in_seconds: NotRequired[
        "capo_lambda.types.tumbling_window_in_seconds.TumblingWindowInSeconds"
    ]
    """<p>(Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources. A value of 0 seconds indicates no tumbling window.</p>"""
    source_access_configurations: NotRequired[
        "capo_lambda.types.source_access_configurations.SourceAccessConfigurations"
    ]
    """<p>An array of authentication protocols or VPC components required to secure your event source.</p>"""
    function_response_types: NotRequired[
        "capo_lambda.types.function_response_type_list.FunctionResponseTypeList"
    ]
    """<p>(Kinesis, DynamoDB Streams, Amazon MSK, self-managed Apache Kafka, and Amazon SQS) A list of current response type enums applied to the event source mapping.</p>"""
    amazon_managed_kafka_event_source_config: NotRequired[
        "capo_lambda.types.amazon_managed_kafka_event_source_config.AmazonManagedKafkaEventSourceConfig"
    ]
    self_managed_kafka_event_source_config: NotRequired[
        "capo_lambda.types.self_managed_kafka_event_source_config.SelfManagedKafkaEventSourceConfig"
    ]
    document_db_event_source_config: NotRequired[
        "capo_lambda.types.document_db_event_source_config.DocumentDBEventSourceConfig"
    ]
    """<p>Specific configuration settings for a DocumentDB event source.</p>"""
    provisioned_poller_config: NotRequired[
        "capo_lambda.types.provisioned_poller_config.ProvisionedPollerConfig"
    ]
    """<p>(Amazon SQS, Amazon MSK, and self-managed Apache Kafka only) The provisioned mode configuration for the event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html#invocation-eventsourcemapping-provisioned-mode">provisioned mode</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEventSourceMappingRequest) -> dict:
    out: dict = {}
    if "function_name" in value:
        out["FunctionName"] = value["function_name"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "batch_size" in value:
        out["BatchSize"] = value["batch_size"]
    if "filter_criteria" in value:
        import capo_lambda.types.filter_criteria

        out["FilterCriteria"] = capo_lambda.types.filter_criteria.serialize_json(
            value["filter_criteria"]
        )
    if "kms_key_arn" in value:
        out["KMSKeyArn"] = value["kms_key_arn"]
    if "metrics_config" in value:
        import capo_lambda.types.event_source_mapping_metrics_config

        out["MetricsConfig"] = (
            capo_lambda.types.event_source_mapping_metrics_config.serialize_json(
                value["metrics_config"]
            )
        )
    if "logging_config" in value:
        import capo_lambda.types.event_source_mapping_logging_config

        out["LoggingConfig"] = (
            capo_lambda.types.event_source_mapping_logging_config.serialize_json(
                value["logging_config"]
            )
        )
    if "scaling_config" in value:
        import capo_lambda.types.scaling_config

        out["ScalingConfig"] = capo_lambda.types.scaling_config.serialize_json(
            value["scaling_config"]
        )
    if "maximum_batching_window_in_seconds" in value:
        out["MaximumBatchingWindowInSeconds"] = value[
            "maximum_batching_window_in_seconds"
        ]
    if "parallelization_factor" in value:
        out["ParallelizationFactor"] = value["parallelization_factor"]
    if "destination_config" in value:
        import capo_lambda.types.destination_config

        out["DestinationConfig"] = capo_lambda.types.destination_config.serialize_json(
            value["destination_config"]
        )
    if "maximum_record_age_in_seconds" in value:
        out["MaximumRecordAgeInSeconds"] = value["maximum_record_age_in_seconds"]
    if "bisect_batch_on_function_error" in value:
        out["BisectBatchOnFunctionError"] = value["bisect_batch_on_function_error"]
    if "maximum_retry_attempts" in value:
        out["MaximumRetryAttempts"] = value["maximum_retry_attempts"]
    if "tumbling_window_in_seconds" in value:
        out["TumblingWindowInSeconds"] = value["tumbling_window_in_seconds"]
    if "source_access_configurations" in value:
        import capo_lambda.types.source_access_configurations

        out["SourceAccessConfigurations"] = (
            capo_lambda.types.source_access_configurations.serialize_json(
                value["source_access_configurations"]
            )
        )
    if "function_response_types" in value:
        import capo_lambda.types.function_response_type_list

        out["FunctionResponseTypes"] = (
            capo_lambda.types.function_response_type_list.serialize_json(
                value["function_response_types"]
            )
        )
    if "amazon_managed_kafka_event_source_config" in value:
        import capo_lambda.types.amazon_managed_kafka_event_source_config

        out["AmazonManagedKafkaEventSourceConfig"] = (
            capo_lambda.types.amazon_managed_kafka_event_source_config.serialize_json(
                value["amazon_managed_kafka_event_source_config"]
            )
        )
    if "self_managed_kafka_event_source_config" in value:
        import capo_lambda.types.self_managed_kafka_event_source_config

        out["SelfManagedKafkaEventSourceConfig"] = (
            capo_lambda.types.self_managed_kafka_event_source_config.serialize_json(
                value["self_managed_kafka_event_source_config"]
            )
        )
    if "document_db_event_source_config" in value:
        import capo_lambda.types.document_db_event_source_config

        out["DocumentDBEventSourceConfig"] = (
            capo_lambda.types.document_db_event_source_config.serialize_json(
                value["document_db_event_source_config"]
            )
        )
    if "provisioned_poller_config" in value:
        import capo_lambda.types.provisioned_poller_config

        out["ProvisionedPollerConfig"] = (
            capo_lambda.types.provisioned_poller_config.serialize_json(
                value["provisioned_poller_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateEventSourceMappingRequest:
    out: UpdateEventSourceMappingRequest = {}  # type: ignore[typeddict-item]
    if data.get("FunctionName") is not None:
        out["function_name"] = data["FunctionName"]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("BatchSize") is not None:
        out["batch_size"] = data["BatchSize"]
    if data.get("FilterCriteria") is not None:
        import capo_lambda.types.filter_criteria

        out["filter_criteria"] = capo_lambda.types.filter_criteria.deserialize_json(
            data["FilterCriteria"]
        )
    if data.get("KMSKeyArn") is not None:
        out["kms_key_arn"] = data["KMSKeyArn"]
    if data.get("MetricsConfig") is not None:
        import capo_lambda.types.event_source_mapping_metrics_config

        out["metrics_config"] = (
            capo_lambda.types.event_source_mapping_metrics_config.deserialize_json(
                data["MetricsConfig"]
            )
        )
    if data.get("LoggingConfig") is not None:
        import capo_lambda.types.event_source_mapping_logging_config

        out["logging_config"] = (
            capo_lambda.types.event_source_mapping_logging_config.deserialize_json(
                data["LoggingConfig"]
            )
        )
    if data.get("ScalingConfig") is not None:
        import capo_lambda.types.scaling_config

        out["scaling_config"] = capo_lambda.types.scaling_config.deserialize_json(
            data["ScalingConfig"]
        )
    if data.get("MaximumBatchingWindowInSeconds") is not None:
        out["maximum_batching_window_in_seconds"] = data[
            "MaximumBatchingWindowInSeconds"
        ]
    if data.get("ParallelizationFactor") is not None:
        out["parallelization_factor"] = data["ParallelizationFactor"]
    if data.get("DestinationConfig") is not None:
        import capo_lambda.types.destination_config

        out["destination_config"] = (
            capo_lambda.types.destination_config.deserialize_json(
                data["DestinationConfig"]
            )
        )
    if data.get("MaximumRecordAgeInSeconds") is not None:
        out["maximum_record_age_in_seconds"] = data["MaximumRecordAgeInSeconds"]
    if data.get("BisectBatchOnFunctionError") is not None:
        out["bisect_batch_on_function_error"] = data["BisectBatchOnFunctionError"]
    if data.get("MaximumRetryAttempts") is not None:
        out["maximum_retry_attempts"] = data["MaximumRetryAttempts"]
    if data.get("TumblingWindowInSeconds") is not None:
        out["tumbling_window_in_seconds"] = data["TumblingWindowInSeconds"]
    if data.get("SourceAccessConfigurations") is not None:
        import capo_lambda.types.source_access_configurations

        out["source_access_configurations"] = (
            capo_lambda.types.source_access_configurations.deserialize_json(
                data["SourceAccessConfigurations"]
            )
        )
    if data.get("FunctionResponseTypes") is not None:
        import capo_lambda.types.function_response_type_list

        out["function_response_types"] = (
            capo_lambda.types.function_response_type_list.deserialize_json(
                data["FunctionResponseTypes"]
            )
        )
    if data.get("AmazonManagedKafkaEventSourceConfig") is not None:
        import capo_lambda.types.amazon_managed_kafka_event_source_config

        out["amazon_managed_kafka_event_source_config"] = (
            capo_lambda.types.amazon_managed_kafka_event_source_config.deserialize_json(
                data["AmazonManagedKafkaEventSourceConfig"]
            )
        )
    if data.get("SelfManagedKafkaEventSourceConfig") is not None:
        import capo_lambda.types.self_managed_kafka_event_source_config

        out["self_managed_kafka_event_source_config"] = (
            capo_lambda.types.self_managed_kafka_event_source_config.deserialize_json(
                data["SelfManagedKafkaEventSourceConfig"]
            )
        )
    if data.get("DocumentDBEventSourceConfig") is not None:
        import capo_lambda.types.document_db_event_source_config

        out["document_db_event_source_config"] = (
            capo_lambda.types.document_db_event_source_config.deserialize_json(
                data["DocumentDBEventSourceConfig"]
            )
        )
    if data.get("ProvisionedPollerConfig") is not None:
        import capo_lambda.types.provisioned_poller_config

        out["provisioned_poller_config"] = (
            capo_lambda.types.provisioned_poller_config.deserialize_json(
                data["ProvisionedPollerConfig"]
            )
        )
    return out
