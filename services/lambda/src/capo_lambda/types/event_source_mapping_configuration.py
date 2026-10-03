"""Generated from Smithy shape ``com.amazonaws.lambda#EventSourceMappingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.amazon_managed_kafka_event_source_config
    import capo_lambda.types.arn
    import capo_lambda.types.batch_size
    import capo_lambda.types.bisect_batch_on_function_error
    import capo_lambda.types.date
    import capo_lambda.types.destination_config
    import capo_lambda.types.document_db_event_source_config
    import capo_lambda.types.event_source_mapping_arn
    import capo_lambda.types.event_source_mapping_logging_config
    import capo_lambda.types.event_source_mapping_metrics_config
    import capo_lambda.types.event_source_position
    import capo_lambda.types.filter_criteria
    import capo_lambda.types.filter_criteria_error
    import capo_lambda.types.function_arn
    import capo_lambda.types.function_response_type_list
    import capo_lambda.types.kms_key_arn
    import capo_lambda.types.maximum_batching_window_in_seconds
    import capo_lambda.types.maximum_record_age_in_seconds
    import capo_lambda.types.maximum_retry_attempts_event_source_mapping
    import capo_lambda.types.parallelization_factor
    import capo_lambda.types.provisioned_poller_config
    import capo_lambda.types.queues
    import capo_lambda.types.scaling_config
    import capo_lambda.types.self_managed_event_source
    import capo_lambda.types.self_managed_kafka_event_source_config
    import capo_lambda.types.source_access_configurations
    import capo_lambda.types.string
    import capo_lambda.types.topics
    import capo_lambda.types.tumbling_window_in_seconds
    import capo_lambda.types.uuid_string


class EventSourceMappingConfiguration(TypedDict, closed=True):
    uuid: NotRequired["capo_lambda.types.uuid_string.UUIDString"]
    """<p>The identifier of the event source mapping.</p>"""
    starting_position: NotRequired[
        "capo_lambda.types.event_source_position.EventSourcePosition"
    ]
    """<p>The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB Stream event sources. <code>AT_TIMESTAMP</code> is supported only for Amazon Kinesis streams, Amazon DocumentDB, Amazon MSK, and self-managed Apache Kafka.</p>"""
    starting_position_timestamp: NotRequired["capo_lambda.types.date.Date"]
    """<p>With <code>StartingPosition</code> set to <code>AT_TIMESTAMP</code>, the time from which to start reading. <code>StartingPositionTimestamp</code> cannot be in the future.</p>"""
    batch_size: NotRequired["capo_lambda.types.batch_size.BatchSize"]
    """<p>The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).</p> <p>Default value: Varies by service. For Amazon SQS, the default is 10. For all other services, the default is 100.</p> <p>Related setting: When you set <code>BatchSize</code> to a value greater than 10, you must set <code>MaximumBatchingWindowInSeconds</code> to at least 1.</p>"""
    maximum_batching_window_in_seconds: NotRequired[
        "capo_lambda.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
    ]
    """<p>The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function. You can configure <code>MaximumBatchingWindowInSeconds</code> to any value from 0 seconds to 300 seconds in increments of seconds.</p> <p>For streams and Amazon SQS event sources, the default batching window is 0 seconds. For Amazon MSK, Self-managed Apache Kafka, Amazon MQ, and DocumentDB event sources, the default batching window is 500 ms. Note that because you can only change <code>MaximumBatchingWindowInSeconds</code> in increments of seconds, you cannot revert back to the 500 ms default batching window after you have changed it. To restore the default batching window, you must create a new event source mapping.</p> <p>Related setting: For streams and Amazon SQS event sources, when you set <code>BatchSize</code> to a value greater than 10, you must set <code>MaximumBatchingWindowInSeconds</code> to at least 1.</p>"""
    parallelization_factor: NotRequired[
        "capo_lambda.types.parallelization_factor.ParallelizationFactor"
    ]
    """<p>(Kinesis and DynamoDB Streams only) The number of batches to process concurrently from each shard. The default value is 1.</p>"""
    event_source_arn: NotRequired["capo_lambda.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the event source.</p>"""
    filter_criteria: NotRequired["capo_lambda.types.filter_criteria.FilterCriteria"]
    """<p>An object that defines the filter criteria that determine whether Lambda should process an event. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html">Lambda event filtering</a>.</p> <p>If filter criteria is encrypted, this field shows up as <code>null</code> in the response of ListEventSourceMapping API calls. You can view this field in plaintext in the response of GetEventSourceMapping and DeleteEventSourceMapping calls if you have <code>kms:Decrypt</code> permissions for the correct KMS key.</p>"""
    filter_criteria_error: NotRequired[
        "capo_lambda.types.filter_criteria_error.FilterCriteriaError"
    ]
    """<p>An object that contains details about an error related to filter criteria encryption.</p>"""
    kms_key_arn: NotRequired["capo_lambda.types.kms_key_arn.KMSKeyArn"]
    """<p> The ARN of the Key Management Service (KMS) customer managed key that Lambda uses to encrypt your function's <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-basics">filter criteria</a>.</p>"""
    metrics_config: NotRequired[
        "capo_lambda.types.event_source_mapping_metrics_config.EventSourceMappingMetricsConfig"
    ]
    """<p>The metrics configuration for your event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics">Event source mapping metrics</a>.</p>"""
    logging_config: NotRequired[
        "capo_lambda.types.event_source_mapping_logging_config.EventSourceMappingLoggingConfig"
    ]
    """<p>(Amazon MSK, and self-managed Apache Kafka only) The logging configuration for your event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/esm-logging.html">Event source mapping logging</a>.</p>"""
    scaling_config: NotRequired["capo_lambda.types.scaling_config.ScalingConfig"]
    """<p>(Amazon SQS only) The scaling configuration for the event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-max-concurrency">Configuring maximum concurrency for Amazon SQS event sources</a>.</p>"""
    function_arn: NotRequired["capo_lambda.types.function_arn.FunctionArn"]
    """<p>The ARN of the Lambda function.</p>"""
    last_modified: NotRequired["capo_lambda.types.date.Date"]
    """<p>The date that the event source mapping was last updated or that its state changed.</p>"""
    last_processing_result: NotRequired["capo_lambda.types.string.String"]
    """<p>The result of the event source mapping's last processing attempt.</p>"""
    state: NotRequired["capo_lambda.types.string.String"]
    """<p>The state of the event source mapping. It can be one of the following: <code>Creating</code>, <code>Enabling</code>, <code>Enabled</code>, <code>Disabling</code>, <code>Disabled</code>, <code>Updating</code>, or <code>Deleting</code>.</p>"""
    state_transition_reason: NotRequired["capo_lambda.types.string.String"]
    """<p>Indicates whether a user or Lambda made the last change to the event source mapping.</p>"""
    destination_config: NotRequired[
        "capo_lambda.types.destination_config.DestinationConfig"
    ]
    """<p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) A configuration object that specifies the destination of an event after Lambda processes it.</p>"""
    topics: NotRequired["capo_lambda.types.topics.Topics"]
    """<p>The name of the Kafka topic.</p>"""
    queues: NotRequired["capo_lambda.types.queues.Queues"]
    """<p> (Amazon MQ) The name of the Amazon MQ broker destination queue to consume.</p>"""
    source_access_configurations: NotRequired[
        "capo_lambda.types.source_access_configurations.SourceAccessConfigurations"
    ]
    """<p>An array of the authentication protocol, VPC components, or virtual host to secure and define your event source.</p>"""
    self_managed_event_source: NotRequired[
        "capo_lambda.types.self_managed_event_source.SelfManagedEventSource"
    ]
    """<p>The self-managed Apache Kafka cluster for your event source.</p>"""
    maximum_record_age_in_seconds: NotRequired[
        "capo_lambda.types.maximum_record_age_in_seconds.MaximumRecordAgeInSeconds"
    ]
    """<p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records older than the specified age. The default value is -1, which sets the maximum age to infinite. When the value is set to infinite, Lambda never discards old records.</p> <note> <p>The minimum valid value for maximum record age is 60s. Although values less than 60 and greater than -1 fall within the parameter's absolute range, they are not allowed</p> </note>"""
    bisect_batch_on_function_error: NotRequired[
        "capo_lambda.types.bisect_batch_on_function_error.BisectBatchOnFunctionError"
    ]
    """<p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) If the function returns an error, split the batch in two and retry. The default value is false.</p>"""
    maximum_retry_attempts: NotRequired[
        "capo_lambda.types.maximum_retry_attempts_event_source_mapping.MaximumRetryAttemptsEventSourceMapping"
    ]
    """<p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records after the specified number of retries. The default value is -1, which sets the maximum number of retries to infinite. When MaximumRetryAttempts is infinite, Lambda retries failed records until the record expires in the event source.</p>"""
    tumbling_window_in_seconds: NotRequired[
        "capo_lambda.types.tumbling_window_in_seconds.TumblingWindowInSeconds"
    ]
    """<p>(Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources. A value of 0 seconds indicates no tumbling window.</p>"""
    function_response_types: NotRequired[
        "capo_lambda.types.function_response_type_list.FunctionResponseTypeList"
    ]
    """<p>(Kinesis, DynamoDB Streams, Amazon MSK, self-managed Apache Kafka, and Amazon SQS) A list of current response type enums applied to the event source mapping.</p>"""
    amazon_managed_kafka_event_source_config: NotRequired[
        "capo_lambda.types.amazon_managed_kafka_event_source_config.AmazonManagedKafkaEventSourceConfig"
    ]
    """<p>Specific configuration settings for an Amazon Managed Streaming for Apache Kafka (Amazon MSK) event source.</p>"""
    self_managed_kafka_event_source_config: NotRequired[
        "capo_lambda.types.self_managed_kafka_event_source_config.SelfManagedKafkaEventSourceConfig"
    ]
    """<p>Specific configuration settings for a self-managed Apache Kafka event source.</p>"""
    document_db_event_source_config: NotRequired[
        "capo_lambda.types.document_db_event_source_config.DocumentDBEventSourceConfig"
    ]
    """<p>Specific configuration settings for a DocumentDB event source.</p>"""
    event_source_mapping_arn: NotRequired[
        "capo_lambda.types.event_source_mapping_arn.EventSourceMappingArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the event source mapping.</p>"""
    provisioned_poller_config: NotRequired[
        "capo_lambda.types.provisioned_poller_config.ProvisionedPollerConfig"
    ]
    """<p>(Amazon SQS, Amazon MSK, and self-managed Apache Kafka only) The provisioned mode configuration for the event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html#invocation-eventsourcemapping-provisioned-mode">provisioned mode</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventSourceMappingConfiguration) -> dict:
    out: dict = {}
    if "uuid" in value:
        out["UUID"] = value["uuid"]
    if "starting_position" in value:
        import capo_lambda.types.event_source_position

        out["StartingPosition"] = (
            capo_lambda.types.event_source_position.serialize_json(
                value["starting_position"]
            )
        )
    if "starting_position_timestamp" in value:
        import capo_lambda.types.date

        out["StartingPositionTimestamp"] = capo_lambda.types.date.serialize_json(
            value["starting_position_timestamp"]
        )
    if "batch_size" in value:
        out["BatchSize"] = value["batch_size"]
    if "maximum_batching_window_in_seconds" in value:
        out["MaximumBatchingWindowInSeconds"] = value[
            "maximum_batching_window_in_seconds"
        ]
    if "parallelization_factor" in value:
        out["ParallelizationFactor"] = value["parallelization_factor"]
    if "event_source_arn" in value:
        out["EventSourceArn"] = value["event_source_arn"]
    if "filter_criteria" in value:
        import capo_lambda.types.filter_criteria

        out["FilterCriteria"] = capo_lambda.types.filter_criteria.serialize_json(
            value["filter_criteria"]
        )
    if "filter_criteria_error" in value:
        import capo_lambda.types.filter_criteria_error

        out["FilterCriteriaError"] = (
            capo_lambda.types.filter_criteria_error.serialize_json(
                value["filter_criteria_error"]
            )
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
    if "function_arn" in value:
        out["FunctionArn"] = value["function_arn"]
    if "last_modified" in value:
        import capo_lambda.types.date

        out["LastModified"] = capo_lambda.types.date.serialize_json(
            value["last_modified"]
        )
    if "last_processing_result" in value:
        out["LastProcessingResult"] = value["last_processing_result"]
    if "state" in value:
        out["State"] = value["state"]
    if "state_transition_reason" in value:
        out["StateTransitionReason"] = value["state_transition_reason"]
    if "destination_config" in value:
        import capo_lambda.types.destination_config

        out["DestinationConfig"] = capo_lambda.types.destination_config.serialize_json(
            value["destination_config"]
        )
    if "topics" in value:
        import capo_lambda.types.topics

        out["Topics"] = capo_lambda.types.topics.serialize_json(value["topics"])
    if "queues" in value:
        import capo_lambda.types.queues

        out["Queues"] = capo_lambda.types.queues.serialize_json(value["queues"])
    if "source_access_configurations" in value:
        import capo_lambda.types.source_access_configurations

        out["SourceAccessConfigurations"] = (
            capo_lambda.types.source_access_configurations.serialize_json(
                value["source_access_configurations"]
            )
        )
    if "self_managed_event_source" in value:
        import capo_lambda.types.self_managed_event_source

        out["SelfManagedEventSource"] = (
            capo_lambda.types.self_managed_event_source.serialize_json(
                value["self_managed_event_source"]
            )
        )
    if "maximum_record_age_in_seconds" in value:
        out["MaximumRecordAgeInSeconds"] = value["maximum_record_age_in_seconds"]
    if "bisect_batch_on_function_error" in value:
        out["BisectBatchOnFunctionError"] = value["bisect_batch_on_function_error"]
    if "maximum_retry_attempts" in value:
        out["MaximumRetryAttempts"] = value["maximum_retry_attempts"]
    if "tumbling_window_in_seconds" in value:
        out["TumblingWindowInSeconds"] = value["tumbling_window_in_seconds"]
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
    if "event_source_mapping_arn" in value:
        out["EventSourceMappingArn"] = value["event_source_mapping_arn"]
    if "provisioned_poller_config" in value:
        import capo_lambda.types.provisioned_poller_config

        out["ProvisionedPollerConfig"] = (
            capo_lambda.types.provisioned_poller_config.serialize_json(
                value["provisioned_poller_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventSourceMappingConfiguration:
    out: EventSourceMappingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("UUID") is not None:
        out["uuid"] = data["UUID"]
    if data.get("StartingPosition") is not None:
        import capo_lambda.types.event_source_position

        out["starting_position"] = (
            capo_lambda.types.event_source_position.deserialize_json(
                data["StartingPosition"]
            )
        )
    if data.get("StartingPositionTimestamp") is not None:
        import capo_lambda.types.date

        out["starting_position_timestamp"] = capo_lambda.types.date.deserialize_json(
            data["StartingPositionTimestamp"]
        )
    if data.get("BatchSize") is not None:
        out["batch_size"] = data["BatchSize"]
    if data.get("MaximumBatchingWindowInSeconds") is not None:
        out["maximum_batching_window_in_seconds"] = data[
            "MaximumBatchingWindowInSeconds"
        ]
    if data.get("ParallelizationFactor") is not None:
        out["parallelization_factor"] = data["ParallelizationFactor"]
    if data.get("EventSourceArn") is not None:
        out["event_source_arn"] = data["EventSourceArn"]
    if data.get("FilterCriteria") is not None:
        import capo_lambda.types.filter_criteria

        out["filter_criteria"] = capo_lambda.types.filter_criteria.deserialize_json(
            data["FilterCriteria"]
        )
    if data.get("FilterCriteriaError") is not None:
        import capo_lambda.types.filter_criteria_error

        out["filter_criteria_error"] = (
            capo_lambda.types.filter_criteria_error.deserialize_json(
                data["FilterCriteriaError"]
            )
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
    if data.get("FunctionArn") is not None:
        out["function_arn"] = data["FunctionArn"]
    if data.get("LastModified") is not None:
        import capo_lambda.types.date

        out["last_modified"] = capo_lambda.types.date.deserialize_json(
            data["LastModified"]
        )
    if data.get("LastProcessingResult") is not None:
        out["last_processing_result"] = data["LastProcessingResult"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("StateTransitionReason") is not None:
        out["state_transition_reason"] = data["StateTransitionReason"]
    if data.get("DestinationConfig") is not None:
        import capo_lambda.types.destination_config

        out["destination_config"] = (
            capo_lambda.types.destination_config.deserialize_json(
                data["DestinationConfig"]
            )
        )
    if data.get("Topics") is not None:
        import capo_lambda.types.topics

        out["topics"] = capo_lambda.types.topics.deserialize_json(data["Topics"])
    if data.get("Queues") is not None:
        import capo_lambda.types.queues

        out["queues"] = capo_lambda.types.queues.deserialize_json(data["Queues"])
    if data.get("SourceAccessConfigurations") is not None:
        import capo_lambda.types.source_access_configurations

        out["source_access_configurations"] = (
            capo_lambda.types.source_access_configurations.deserialize_json(
                data["SourceAccessConfigurations"]
            )
        )
    if data.get("SelfManagedEventSource") is not None:
        import capo_lambda.types.self_managed_event_source

        out["self_managed_event_source"] = (
            capo_lambda.types.self_managed_event_source.deserialize_json(
                data["SelfManagedEventSource"]
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
    if data.get("EventSourceMappingArn") is not None:
        out["event_source_mapping_arn"] = data["EventSourceMappingArn"]
    if data.get("ProvisionedPollerConfig") is not None:
        import capo_lambda.types.provisioned_poller_config

        out["provisioned_poller_config"] = (
            capo_lambda.types.provisioned_poller_config.deserialize_json(
                data["ProvisionedPollerConfig"]
            )
        )
    return out
