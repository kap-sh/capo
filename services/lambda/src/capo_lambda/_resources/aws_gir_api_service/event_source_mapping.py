from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_lambda._auth._signers
import capo_lambda._auth._sigv4
from capo_lambda._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_lambda.types.amazon_managed_kafka_event_source_config
    import capo_lambda.types.arn
    import capo_lambda.types.batch_size
    import capo_lambda.types.bisect_batch_on_function_error
    import capo_lambda.types.create_event_source_mapping_request
    import capo_lambda.types.date
    import capo_lambda.types.delete_event_source_mapping_request
    import capo_lambda.types.destination_config
    import capo_lambda.types.document_db_event_source_config
    import capo_lambda.types.enabled
    import capo_lambda.types.event_source_mapping_configuration
    import capo_lambda.types.event_source_mapping_logging_config
    import capo_lambda.types.event_source_mapping_metrics_config
    import capo_lambda.types.event_source_position
    import capo_lambda.types.filter_criteria
    import capo_lambda.types.function_response_type_list
    import capo_lambda.types.get_event_source_mapping_request
    import capo_lambda.types.kms_key_arn
    import capo_lambda.types.list_event_source_mappings_request
    import capo_lambda.types.list_event_source_mappings_response
    import capo_lambda.types.max_list_items
    import capo_lambda.types.maximum_batching_window_in_seconds
    import capo_lambda.types.maximum_record_age_in_seconds
    import capo_lambda.types.maximum_retry_attempts_event_source_mapping
    import capo_lambda.types.namespaced_function_name
    import capo_lambda.types.parallelization_factor
    import capo_lambda.types.provisioned_poller_config
    import capo_lambda.types.queues
    import capo_lambda.types.scaling_config
    import capo_lambda.types.self_managed_event_source
    import capo_lambda.types.self_managed_kafka_event_source_config
    import capo_lambda.types.source_access_configurations
    import capo_lambda.types.string
    import capo_lambda.types.tags
    import capo_lambda.types.topics
    import capo_lambda.types.tumbling_window_in_seconds
    import capo_lambda.types.update_event_source_mapping_request
    import capo_lambda.types.uuid_string
    from capo_lambda._services._lambda import LambdaClient, LambdaClientConfig
    from capo_lambda._services.async__lambda import (
        AsyncLambdaClient,
        AsyncLambdaClientConfig,
    )


class EventSourceMapping:
    def __init__(self, service: LambdaClient) -> None:
        self._service = service

    def create(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        event_source_arn: Optional["capo_lambda.types.arn.Arn"] = None,
        enabled: Optional["capo_lambda.types.enabled.Enabled"] = None,
        batch_size: Optional["capo_lambda.types.batch_size.BatchSize"] = None,
        filter_criteria: Optional[
            "capo_lambda.types.filter_criteria.FilterCriteria"
        ] = None,
        kms_key_arn: Optional["capo_lambda.types.kms_key_arn.KMSKeyArn"] = None,
        metrics_config: Optional[
            "capo_lambda.types.event_source_mapping_metrics_config.EventSourceMappingMetricsConfig"
        ] = None,
        logging_config: Optional[
            "capo_lambda.types.event_source_mapping_logging_config.EventSourceMappingLoggingConfig"
        ] = None,
        scaling_config: Optional[
            "capo_lambda.types.scaling_config.ScalingConfig"
        ] = None,
        maximum_batching_window_in_seconds: Optional[
            "capo_lambda.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
        ] = None,
        parallelization_factor: Optional[
            "capo_lambda.types.parallelization_factor.ParallelizationFactor"
        ] = None,
        starting_position: Optional[
            "capo_lambda.types.event_source_position.EventSourcePosition"
        ] = None,
        starting_position_timestamp: Optional["capo_lambda.types.date.Date"] = None,
        destination_config: Optional[
            "capo_lambda.types.destination_config.DestinationConfig"
        ] = None,
        maximum_record_age_in_seconds: Optional[
            "capo_lambda.types.maximum_record_age_in_seconds.MaximumRecordAgeInSeconds"
        ] = None,
        bisect_batch_on_function_error: Optional[
            "capo_lambda.types.bisect_batch_on_function_error.BisectBatchOnFunctionError"
        ] = None,
        maximum_retry_attempts: Optional[
            "capo_lambda.types.maximum_retry_attempts_event_source_mapping.MaximumRetryAttemptsEventSourceMapping"
        ] = None,
        tags: Optional["capo_lambda.types.tags.Tags"] = None,
        tumbling_window_in_seconds: Optional[
            "capo_lambda.types.tumbling_window_in_seconds.TumblingWindowInSeconds"
        ] = None,
        topics: Optional["capo_lambda.types.topics.Topics"] = None,
        queues: Optional["capo_lambda.types.queues.Queues"] = None,
        source_access_configurations: Optional[
            "capo_lambda.types.source_access_configurations.SourceAccessConfigurations"
        ] = None,
        self_managed_event_source: Optional[
            "capo_lambda.types.self_managed_event_source.SelfManagedEventSource"
        ] = None,
        function_response_types: Optional[
            "capo_lambda.types.function_response_type_list.FunctionResponseTypeList"
        ] = None,
        amazon_managed_kafka_event_source_config: Optional[
            "capo_lambda.types.amazon_managed_kafka_event_source_config.AmazonManagedKafkaEventSourceConfig"
        ] = None,
        self_managed_kafka_event_source_config: Optional[
            "capo_lambda.types.self_managed_kafka_event_source_config.SelfManagedKafkaEventSourceConfig"
        ] = None,
        document_db_event_source_config: Optional[
            "capo_lambda.types.document_db_event_source_config.DocumentDBEventSourceConfig"
        ] = None,
        provisioned_poller_config: Optional[
            "capo_lambda.types.provisioned_poller_config.ProvisionedPollerConfig"
        ] = None,
    ) -> "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration":
        """<p>Creates a mapping between an event source and an Lambda function. Lambda reads items from the event source and invokes the function.</p> <p>For details about how to configure different event sources, see the following topics. </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-dynamodb-eventsourcemapping"> Amazon DynamoDB Streams</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-eventsourcemapping"> Amazon Kinesis</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource"> Amazon SQS</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html#services-mq-eventsourcemapping"> Amazon MQ and RabbitMQ</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html"> Amazon MSK</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/kafka-smaa.html"> Apache Kafka</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html"> Amazon DocumentDB</a> </p> </li> </ul> <p>The following error handling options are available for stream sources (DynamoDB, Kinesis, Amazon MSK, and self-managed Apache Kafka):</p> <ul> <li> <p> <code>BisectBatchOnFunctionError</code> – If the function returns an error, split the batch in two and retry.</p> </li> <li> <p> <code>MaximumRecordAgeInSeconds</code> – Discard records older than the specified age. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires</p> </li> <li> <p> <code>MaximumRetryAttempts</code> – Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires.</p> </li> <li> <p> <code>OnFailure</code> – Send discarded records to an Amazon SQS queue, Amazon SNS topic, Kafka topic, or Amazon S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html#invocation-async-destinations">Adding a destination</a>.</p> </li> </ul> <p>The following option is available only for DynamoDB and Kinesis event sources:</p> <ul> <li> <p> <code>ParallelizationFactor</code> – Process multiple batches from each shard concurrently.</p> </li> </ul> <p>For information about which configuration parameters apply to each event source, see the following topics.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-ddb-params"> Amazon DynamoDB Streams</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-params"> Amazon Kinesis</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#services-sqs-params"> Amazon SQS</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html#services-mq-params"> Amazon MQ and RabbitMQ</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#services-msk-parms"> Amazon MSK</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html#services-kafka-parms"> Apache Kafka</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html#docdb-configuration"> Amazon DocumentDB</a> </p> </li> </ul>

        Args:
            event_source_arn: <p>The Amazon Resource Name (ARN) of the event source.</p> <ul> <li> <p> <b>Amazon Kinesis</b> – The ARN of the data stream or a stream consumer.</p> </li> <li> <p> <b>Amazon DynamoDB Streams</b> – The ARN of the stream.</p> </li> <li> <p> <b>Amazon Simple Queue Service</b> – The ARN of the queue.</p> </li> <li> <p> <b>Amazon Managed Streaming for Apache Kafka</b> – The ARN of the cluster or the ARN of the VPC connection (for <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#msk-multi-vpc">cross-account event source mappings</a>).</p> </li> <li> <p> <b>Amazon MQ</b> – The ARN of the broker.</p> </li> <li> <p> <b>Amazon DocumentDB</b> – The ARN of the DocumentDB change stream.</p> </li> </ul>
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Version or Alias ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.</p>
            enabled: <p>When true, the event source mapping is active. When false, Lambda pauses polling and invocation.</p> <p>Default: True</p>
            batch_size: <p>The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).</p> <ul> <li> <p> <b>Amazon Kinesis</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon DynamoDB Streams</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon Simple Queue Service</b> – Default 10. For standard queues the max is 10,000. For FIFO queues the max is 10.</p> </li> <li> <p> <b>Amazon Managed Streaming for Apache Kafka</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Self-managed Apache Kafka</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon MQ (ActiveMQ and RabbitMQ)</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>DocumentDB</b> – Default 100. Max 10,000.</p> </li> </ul>
            filter_criteria: <p>An object that defines the filter criteria that determine whether Lambda should process an event. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html">Lambda event filtering</a>.</p>
            kms_key_arn: <p> The ARN of the Key Management Service (KMS) customer managed key that Lambda uses to encrypt your function's <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-basics">filter criteria</a>. By default, Lambda does not encrypt your filter criteria object. Specify this property to encrypt data using your own customer managed key. </p>
            metrics_config: <p>The metrics configuration for your event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics">Event source mapping metrics</a>.</p>
            logging_config: <p>(Amazon MSK, and self-managed Apache Kafka only) The logging configuration for your event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/esm-logging.html">Event source mapping logging</a>.</p>
            scaling_config: <p>(Amazon SQS only) The scaling configuration for the event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-max-concurrency">Configuring maximum concurrency for Amazon SQS event sources</a>.</p>
            maximum_batching_window_in_seconds: <p>The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function. You can configure <code>MaximumBatchingWindowInSeconds</code> to any value from 0 seconds to 300 seconds in increments of seconds.</p> <p>For Kinesis, DynamoDB, and Amazon SQS event sources, the default batching window is 0 seconds. For Amazon MSK, Self-managed Apache Kafka, Amazon MQ, and DocumentDB event sources, the default batching window is 500 ms. Note that because you can only change <code>MaximumBatchingWindowInSeconds</code> in increments of seconds, you cannot revert back to the 500 ms default batching window after you have changed it. To restore the default batching window, you must create a new event source mapping.</p> <p>Related setting: For Kinesis, DynamoDB, and Amazon SQS event sources, when you set <code>BatchSize</code> to a value greater than 10, you must set <code>MaximumBatchingWindowInSeconds</code> to at least 1.</p>
            parallelization_factor: <p>(Kinesis and DynamoDB Streams only) The number of batches to process from each shard concurrently.</p>
            starting_position: <p>The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB Stream event sources. <code>AT_TIMESTAMP</code> is supported only for Amazon Kinesis streams, Amazon DocumentDB, Amazon MSK, and self-managed Apache Kafka.</p>
            starting_position_timestamp: <p>With <code>StartingPosition</code> set to <code>AT_TIMESTAMP</code>, the time from which to start reading. <code>StartingPositionTimestamp</code> cannot be in the future.</p>
            destination_config: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) A configuration object that specifies the destination of an event after Lambda processes it.</p>
            maximum_record_age_in_seconds: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records older than the specified age. The default value is infinite (-1).</p>
            bisect_batch_on_function_error: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) If the function returns an error, split the batch in two and retry.</p>
            maximum_retry_attempts: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires.</p>
            tags: <p>A list of tags to apply to the event source mapping.</p>
            tumbling_window_in_seconds: <p>(Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources. A value of 0 seconds indicates no tumbling window.</p>
            topics: <p>The name of the Kafka topic.</p>
            queues: <p> (MQ) The name of the Amazon MQ broker destination queue to consume. </p>
            source_access_configurations: <p>An array of authentication protocols or VPC components required to secure your event source.</p>
            self_managed_event_source: <p>The self-managed Apache Kafka cluster to receive records from.</p>
            function_response_types: <p>(Kinesis, DynamoDB Streams, Amazon MSK, self-managed Apache Kafka, and Amazon SQS) A list of current response type enums applied to the event source mapping.</p>
            amazon_managed_kafka_event_source_config: <p>Specific configuration settings for an Amazon Managed Streaming for Apache Kafka (Amazon MSK) event source.</p>
            self_managed_kafka_event_source_config: <p>Specific configuration settings for a self-managed Apache Kafka event source.</p>
            document_db_event_source_config: <p>Specific configuration settings for a DocumentDB event source.</p>
            provisioned_poller_config: <p>(Amazon SQS, Amazon MSK, and self-managed Apache Kafka only) The provisioned mode configuration for the event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html#invocation-eventsourcemapping-provisioned-mode">provisioned mode</a>.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a mapping between an event source and an AWS Lambda function
            The following example creates a mapping between an SQS queue and the my-function Lambda function.

            >>> client.create(batch_size=5, event_source_arn='arn:aws:sqs:us-west-2:123456789012:my-queue', function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.create_event_source_mapping_request.CreateEventSourceMappingRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.create_event_source_mapping

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.create_event_source_mapping.create_event_source_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.create_event_source_mapping_request.CreateEventSourceMappingRequest = {
            "function_name": function_name
        }
        if event_source_arn is not None:
            input_["event_source_arn"] = event_source_arn
        if enabled is not None:
            input_["enabled"] = enabled
        if batch_size is not None:
            input_["batch_size"] = batch_size
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if metrics_config is not None:
            input_["metrics_config"] = metrics_config
        if logging_config is not None:
            input_["logging_config"] = logging_config
        if scaling_config is not None:
            input_["scaling_config"] = scaling_config
        if maximum_batching_window_in_seconds is not None:
            input_["maximum_batching_window_in_seconds"] = (
                maximum_batching_window_in_seconds
            )
        if parallelization_factor is not None:
            input_["parallelization_factor"] = parallelization_factor
        if starting_position is not None:
            input_["starting_position"] = starting_position
        if starting_position_timestamp is not None:
            input_["starting_position_timestamp"] = starting_position_timestamp
        if destination_config is not None:
            input_["destination_config"] = destination_config
        if maximum_record_age_in_seconds is not None:
            input_["maximum_record_age_in_seconds"] = maximum_record_age_in_seconds
        if bisect_batch_on_function_error is not None:
            input_["bisect_batch_on_function_error"] = bisect_batch_on_function_error
        if maximum_retry_attempts is not None:
            input_["maximum_retry_attempts"] = maximum_retry_attempts
        if tags is not None:
            input_["tags"] = tags
        if tumbling_window_in_seconds is not None:
            input_["tumbling_window_in_seconds"] = tumbling_window_in_seconds
        if topics is not None:
            input_["topics"] = topics
        if queues is not None:
            input_["queues"] = queues
        if source_access_configurations is not None:
            input_["source_access_configurations"] = source_access_configurations
        if self_managed_event_source is not None:
            input_["self_managed_event_source"] = self_managed_event_source
        if function_response_types is not None:
            input_["function_response_types"] = function_response_types
        if amazon_managed_kafka_event_source_config is not None:
            input_["amazon_managed_kafka_event_source_config"] = (
                amazon_managed_kafka_event_source_config
            )
        if self_managed_kafka_event_source_config is not None:
            input_["self_managed_kafka_event_source_config"] = (
                self_managed_kafka_event_source_config
            )
        if document_db_event_source_config is not None:
            input_["document_db_event_source_config"] = document_db_event_source_config
        if provisioned_poller_config is not None:
            input_["provisioned_poller_config"] = provisioned_poller_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        uuid: "capo_lambda.types.uuid_string.UUIDString",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration":
        """<p>Returns details about an event source mapping. You can get the identifier of a mapping from the output of <a>ListEventSourceMappings</a>.</p>

        Args:
            uuid: <p>The identifier of the event source mapping.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a Lambda function's event source mapping
            The following example returns details about an event source mapping. To get a mapping's UUID, use ListEventSourceMappings.

            >>> client.read(uuid='14e0db71-xmpl-4eb5-b481-8945cf9d10c2')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_event_source_mapping_request.GetEventSourceMappingRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_event_source_mapping

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_event_source_mapping.get_event_source_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_event_source_mapping_request.GetEventSourceMappingRequest = {
            "uuid": uuid
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        uuid: "capo_lambda.types.uuid_string.UUIDString",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        function_name: Optional[
            "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
        ] = None,
        enabled: Optional["capo_lambda.types.enabled.Enabled"] = None,
        batch_size: Optional["capo_lambda.types.batch_size.BatchSize"] = None,
        filter_criteria: Optional[
            "capo_lambda.types.filter_criteria.FilterCriteria"
        ] = None,
        kms_key_arn: Optional["capo_lambda.types.kms_key_arn.KMSKeyArn"] = None,
        metrics_config: Optional[
            "capo_lambda.types.event_source_mapping_metrics_config.EventSourceMappingMetricsConfig"
        ] = None,
        logging_config: Optional[
            "capo_lambda.types.event_source_mapping_logging_config.EventSourceMappingLoggingConfig"
        ] = None,
        scaling_config: Optional[
            "capo_lambda.types.scaling_config.ScalingConfig"
        ] = None,
        maximum_batching_window_in_seconds: Optional[
            "capo_lambda.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
        ] = None,
        parallelization_factor: Optional[
            "capo_lambda.types.parallelization_factor.ParallelizationFactor"
        ] = None,
        destination_config: Optional[
            "capo_lambda.types.destination_config.DestinationConfig"
        ] = None,
        maximum_record_age_in_seconds: Optional[
            "capo_lambda.types.maximum_record_age_in_seconds.MaximumRecordAgeInSeconds"
        ] = None,
        bisect_batch_on_function_error: Optional[
            "capo_lambda.types.bisect_batch_on_function_error.BisectBatchOnFunctionError"
        ] = None,
        maximum_retry_attempts: Optional[
            "capo_lambda.types.maximum_retry_attempts_event_source_mapping.MaximumRetryAttemptsEventSourceMapping"
        ] = None,
        tumbling_window_in_seconds: Optional[
            "capo_lambda.types.tumbling_window_in_seconds.TumblingWindowInSeconds"
        ] = None,
        source_access_configurations: Optional[
            "capo_lambda.types.source_access_configurations.SourceAccessConfigurations"
        ] = None,
        function_response_types: Optional[
            "capo_lambda.types.function_response_type_list.FunctionResponseTypeList"
        ] = None,
        amazon_managed_kafka_event_source_config: Optional[
            "capo_lambda.types.amazon_managed_kafka_event_source_config.AmazonManagedKafkaEventSourceConfig"
        ] = None,
        self_managed_kafka_event_source_config: Optional[
            "capo_lambda.types.self_managed_kafka_event_source_config.SelfManagedKafkaEventSourceConfig"
        ] = None,
        document_db_event_source_config: Optional[
            "capo_lambda.types.document_db_event_source_config.DocumentDBEventSourceConfig"
        ] = None,
        provisioned_poller_config: Optional[
            "capo_lambda.types.provisioned_poller_config.ProvisionedPollerConfig"
        ] = None,
    ) -> "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration":
        """<p>Updates an event source mapping. You can change the function that Lambda invokes, or pause invocation and resume later from the same location.</p> <p>For details about how to configure different event sources, see the following topics. </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-dynamodb-eventsourcemapping"> Amazon DynamoDB Streams</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-eventsourcemapping"> Amazon Kinesis</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource"> Amazon SQS</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html#services-mq-eventsourcemapping"> Amazon MQ and RabbitMQ</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html"> Amazon MSK</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/kafka-smaa.html"> Apache Kafka</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html"> Amazon DocumentDB</a> </p> </li> </ul> <p>The following error handling options are available for stream sources (DynamoDB, Kinesis, Amazon MSK, and self-managed Apache Kafka):</p> <ul> <li> <p> <code>BisectBatchOnFunctionError</code> – If the function returns an error, split the batch in two and retry.</p> </li> <li> <p> <code>MaximumRecordAgeInSeconds</code> – Discard records older than the specified age. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires</p> </li> <li> <p> <code>MaximumRetryAttempts</code> – Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires.</p> </li> <li> <p> <code>OnFailure</code> – Send discarded records to an Amazon SQS queue, Amazon SNS topic, Kafka topic, or Amazon S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html#invocation-async-destinations">Adding a destination</a>.</p> </li> </ul> <p>The following option is available only for DynamoDB and Kinesis event sources:</p> <ul> <li> <p> <code>ParallelizationFactor</code> – Process multiple batches from each shard concurrently.</p> </li> </ul> <p>For information about which configuration parameters apply to each event source, see the following topics.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-ddb-params"> Amazon DynamoDB Streams</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-params"> Amazon Kinesis</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#services-sqs-params"> Amazon SQS</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html#services-mq-params"> Amazon MQ and RabbitMQ</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#services-msk-parms"> Amazon MSK</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html#services-kafka-parms"> Apache Kafka</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html#docdb-configuration"> Amazon DocumentDB</a> </p> </li> </ul>

        Args:
            uuid: <p>The identifier of the event source mapping.</p>
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Version or Alias ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.</p>
            enabled: <p>When true, the event source mapping is active. When false, Lambda pauses polling and invocation.</p> <p>Default: True</p>
            batch_size: <p>The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).</p> <ul> <li> <p> <b>Amazon Kinesis</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon DynamoDB Streams</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon Simple Queue Service</b> – Default 10. For standard queues the max is 10,000. For FIFO queues the max is 10.</p> </li> <li> <p> <b>Amazon Managed Streaming for Apache Kafka</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Self-managed Apache Kafka</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon MQ (ActiveMQ and RabbitMQ)</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>DocumentDB</b> – Default 100. Max 10,000.</p> </li> </ul>
            filter_criteria: <p>An object that defines the filter criteria that determine whether Lambda should process an event. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html">Lambda event filtering</a>.</p>
            kms_key_arn: <p> The ARN of the Key Management Service (KMS) customer managed key that Lambda uses to encrypt your function's <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-basics">filter criteria</a>. By default, Lambda does not encrypt your filter criteria object. Specify this property to encrypt data using your own customer managed key. </p>
            metrics_config: <p>The metrics configuration for your event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics">Event source mapping metrics</a>.</p>
            scaling_config: <p>(Amazon SQS only) The scaling configuration for the event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-max-concurrency">Configuring maximum concurrency for Amazon SQS event sources</a>.</p>
            maximum_batching_window_in_seconds: <p>The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function. You can configure <code>MaximumBatchingWindowInSeconds</code> to any value from 0 seconds to 300 seconds in increments of seconds.</p> <p>For Kinesis, DynamoDB, and Amazon SQS event sources, the default batching window is 0 seconds. For Amazon MSK, Self-managed Apache Kafka, Amazon MQ, and DocumentDB event sources, the default batching window is 500 ms. Note that because you can only change <code>MaximumBatchingWindowInSeconds</code> in increments of seconds, you cannot revert back to the 500 ms default batching window after you have changed it. To restore the default batching window, you must create a new event source mapping.</p> <p>Related setting: For Kinesis, DynamoDB, and Amazon SQS event sources, when you set <code>BatchSize</code> to a value greater than 10, you must set <code>MaximumBatchingWindowInSeconds</code> to at least 1.</p>
            parallelization_factor: <p>(Kinesis and DynamoDB Streams only) The number of batches to process from each shard concurrently.</p>
            destination_config: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) A configuration object that specifies the destination of an event after Lambda processes it.</p>
            maximum_record_age_in_seconds: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records older than the specified age. The default value is infinite (-1).</p>
            bisect_batch_on_function_error: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) If the function returns an error, split the batch in two and retry.</p>
            maximum_retry_attempts: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires.</p>
            tumbling_window_in_seconds: <p>(Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources. A value of 0 seconds indicates no tumbling window.</p>
            source_access_configurations: <p>An array of authentication protocols or VPC components required to secure your event source.</p>
            function_response_types: <p>(Kinesis, DynamoDB Streams, Amazon MSK, self-managed Apache Kafka, and Amazon SQS) A list of current response type enums applied to the event source mapping.</p>
            document_db_event_source_config: <p>Specific configuration settings for a DocumentDB event source.</p>
            provisioned_poller_config: <p>(Amazon SQS, Amazon MSK, and self-managed Apache Kafka only) The provisioned mode configuration for the event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html#invocation-eventsourcemapping-provisioned-mode">provisioned mode</a>.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example, you tried to update an event source mapping in the CREATING state, or you tried to delete an event source mapping currently UPDATING.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a Lambda function event source mapping
            This operation updates a Lambda function event source mapping

            >>> client.update(batch_size=123, enabled=True, function_name='myFunction', uuid='a1b2c3d4-5678-90ab-cdef-11111EXAMPLE')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.update_event_source_mapping_request.UpdateEventSourceMappingRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_event_source_mapping

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.update_event_source_mapping.update_event_source_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.update_event_source_mapping_request.UpdateEventSourceMappingRequest = {
            "uuid": uuid
        }
        if function_name is not None:
            input_["function_name"] = function_name
        if enabled is not None:
            input_["enabled"] = enabled
        if batch_size is not None:
            input_["batch_size"] = batch_size
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if metrics_config is not None:
            input_["metrics_config"] = metrics_config
        if logging_config is not None:
            input_["logging_config"] = logging_config
        if scaling_config is not None:
            input_["scaling_config"] = scaling_config
        if maximum_batching_window_in_seconds is not None:
            input_["maximum_batching_window_in_seconds"] = (
                maximum_batching_window_in_seconds
            )
        if parallelization_factor is not None:
            input_["parallelization_factor"] = parallelization_factor
        if destination_config is not None:
            input_["destination_config"] = destination_config
        if maximum_record_age_in_seconds is not None:
            input_["maximum_record_age_in_seconds"] = maximum_record_age_in_seconds
        if bisect_batch_on_function_error is not None:
            input_["bisect_batch_on_function_error"] = bisect_batch_on_function_error
        if maximum_retry_attempts is not None:
            input_["maximum_retry_attempts"] = maximum_retry_attempts
        if tumbling_window_in_seconds is not None:
            input_["tumbling_window_in_seconds"] = tumbling_window_in_seconds
        if source_access_configurations is not None:
            input_["source_access_configurations"] = source_access_configurations
        if function_response_types is not None:
            input_["function_response_types"] = function_response_types
        if amazon_managed_kafka_event_source_config is not None:
            input_["amazon_managed_kafka_event_source_config"] = (
                amazon_managed_kafka_event_source_config
            )
        if self_managed_kafka_event_source_config is not None:
            input_["self_managed_kafka_event_source_config"] = (
                self_managed_kafka_event_source_config
            )
        if document_db_event_source_config is not None:
            input_["document_db_event_source_config"] = document_db_event_source_config
        if provisioned_poller_config is not None:
            input_["provisioned_poller_config"] = provisioned_poller_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        uuid: "capo_lambda.types.uuid_string.UUIDString",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration":
        """<p>Deletes an <a href="https://docs.aws.amazon.com/lambda/latest/dg/intro-invocation-modes.html">event source mapping</a>. You can get the identifier of a mapping from the output of <a>ListEventSourceMappings</a>.</p> <p>When you delete an event source mapping, it enters a <code>Deleting</code> state and might not be completely deleted for several seconds.</p>

        Args:
            uuid: <p>The identifier of the event source mapping.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example, you tried to update an event source mapping in the CREATING state, or you tried to delete an event source mapping currently UPDATING.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a Lambda function event source mapping
            The following example deletes an event source mapping. To get a mapping's UUID, use ListEventSourceMappings.

            >>> client.delete(uuid='14e0db71-xmpl-4eb5-b481-8945cf9d10c2')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_event_source_mapping_request.DeleteEventSourceMappingRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.delete_event_source_mapping

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_event_source_mapping.delete_event_source_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.delete_event_source_mapping_request.DeleteEventSourceMappingRequest = {
            "uuid": uuid
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        event_source_arn: Optional["capo_lambda.types.arn.Arn"] = None,
        function_name: Optional[
            "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
        ] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "capo_lambda.types.list_event_source_mappings_response.ListEventSourceMappingsResponse":
        """<p>Lists event source mappings. Specify an <code>EventSourceArn</code> to show only event source mappings for a single event source.</p>

        Args:
            event_source_arn: <p>The Amazon Resource Name (ARN) of the event source.</p> <ul> <li> <p> <b>Amazon Kinesis</b> – The ARN of the data stream or a stream consumer.</p> </li> <li> <p> <b>Amazon DynamoDB Streams</b> – The ARN of the stream.</p> </li> <li> <p> <b>Amazon Simple Queue Service</b> – The ARN of the queue.</p> </li> <li> <p> <b>Amazon Managed Streaming for Apache Kafka</b> – The ARN of the cluster or the ARN of the VPC connection (for <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#msk-multi-vpc">cross-account event source mappings</a>).</p> </li> <li> <p> <b>Amazon MQ</b> – The ARN of the broker.</p> </li> <li> <p> <b>Amazon DocumentDB</b> – The ARN of the DocumentDB change stream.</p> </li> </ul>
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Version or Alias ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.</p>
            marker: <p>A pagination token returned by a previous call.</p>
            max_items: <p>The maximum number of event source mappings to return. Note that ListEventSourceMappings returns a maximum of 100 items in each response, even if you set the number higher.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the event source mappings for a function
            The following example returns a list of the event source mappings for a function named my-function.

            >>> client.list(function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_event_source_mappings_request.ListEventSourceMappingsRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_event_source_mappings_response.ListEventSourceMappingsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_event_source_mappings

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_event_source_mappings.list_event_source_mappings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_event_source_mappings_request.ListEventSourceMappingsRequest = {}
        if event_source_arn is not None:
            input_["event_source_arn"] = event_source_arn
        if function_name is not None:
            input_["function_name"] = function_name
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncEventSourceMapping:
    def __init__(self, service: AsyncLambdaClient) -> None:
        self._service = service

    async def create(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        event_source_arn: Optional["capo_lambda.types.arn.Arn"] = None,
        enabled: Optional["capo_lambda.types.enabled.Enabled"] = None,
        batch_size: Optional["capo_lambda.types.batch_size.BatchSize"] = None,
        filter_criteria: Optional[
            "capo_lambda.types.filter_criteria.FilterCriteria"
        ] = None,
        kms_key_arn: Optional["capo_lambda.types.kms_key_arn.KMSKeyArn"] = None,
        metrics_config: Optional[
            "capo_lambda.types.event_source_mapping_metrics_config.EventSourceMappingMetricsConfig"
        ] = None,
        logging_config: Optional[
            "capo_lambda.types.event_source_mapping_logging_config.EventSourceMappingLoggingConfig"
        ] = None,
        scaling_config: Optional[
            "capo_lambda.types.scaling_config.ScalingConfig"
        ] = None,
        maximum_batching_window_in_seconds: Optional[
            "capo_lambda.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
        ] = None,
        parallelization_factor: Optional[
            "capo_lambda.types.parallelization_factor.ParallelizationFactor"
        ] = None,
        starting_position: Optional[
            "capo_lambda.types.event_source_position.EventSourcePosition"
        ] = None,
        starting_position_timestamp: Optional["capo_lambda.types.date.Date"] = None,
        destination_config: Optional[
            "capo_lambda.types.destination_config.DestinationConfig"
        ] = None,
        maximum_record_age_in_seconds: Optional[
            "capo_lambda.types.maximum_record_age_in_seconds.MaximumRecordAgeInSeconds"
        ] = None,
        bisect_batch_on_function_error: Optional[
            "capo_lambda.types.bisect_batch_on_function_error.BisectBatchOnFunctionError"
        ] = None,
        maximum_retry_attempts: Optional[
            "capo_lambda.types.maximum_retry_attempts_event_source_mapping.MaximumRetryAttemptsEventSourceMapping"
        ] = None,
        tags: Optional["capo_lambda.types.tags.Tags"] = None,
        tumbling_window_in_seconds: Optional[
            "capo_lambda.types.tumbling_window_in_seconds.TumblingWindowInSeconds"
        ] = None,
        topics: Optional["capo_lambda.types.topics.Topics"] = None,
        queues: Optional["capo_lambda.types.queues.Queues"] = None,
        source_access_configurations: Optional[
            "capo_lambda.types.source_access_configurations.SourceAccessConfigurations"
        ] = None,
        self_managed_event_source: Optional[
            "capo_lambda.types.self_managed_event_source.SelfManagedEventSource"
        ] = None,
        function_response_types: Optional[
            "capo_lambda.types.function_response_type_list.FunctionResponseTypeList"
        ] = None,
        amazon_managed_kafka_event_source_config: Optional[
            "capo_lambda.types.amazon_managed_kafka_event_source_config.AmazonManagedKafkaEventSourceConfig"
        ] = None,
        self_managed_kafka_event_source_config: Optional[
            "capo_lambda.types.self_managed_kafka_event_source_config.SelfManagedKafkaEventSourceConfig"
        ] = None,
        document_db_event_source_config: Optional[
            "capo_lambda.types.document_db_event_source_config.DocumentDBEventSourceConfig"
        ] = None,
        provisioned_poller_config: Optional[
            "capo_lambda.types.provisioned_poller_config.ProvisionedPollerConfig"
        ] = None,
    ) -> "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration":
        """<p>Creates a mapping between an event source and an Lambda function. Lambda reads items from the event source and invokes the function.</p> <p>For details about how to configure different event sources, see the following topics. </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-dynamodb-eventsourcemapping"> Amazon DynamoDB Streams</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-eventsourcemapping"> Amazon Kinesis</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource"> Amazon SQS</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html#services-mq-eventsourcemapping"> Amazon MQ and RabbitMQ</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html"> Amazon MSK</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/kafka-smaa.html"> Apache Kafka</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html"> Amazon DocumentDB</a> </p> </li> </ul> <p>The following error handling options are available for stream sources (DynamoDB, Kinesis, Amazon MSK, and self-managed Apache Kafka):</p> <ul> <li> <p> <code>BisectBatchOnFunctionError</code> – If the function returns an error, split the batch in two and retry.</p> </li> <li> <p> <code>MaximumRecordAgeInSeconds</code> – Discard records older than the specified age. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires</p> </li> <li> <p> <code>MaximumRetryAttempts</code> – Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires.</p> </li> <li> <p> <code>OnFailure</code> – Send discarded records to an Amazon SQS queue, Amazon SNS topic, Kafka topic, or Amazon S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html#invocation-async-destinations">Adding a destination</a>.</p> </li> </ul> <p>The following option is available only for DynamoDB and Kinesis event sources:</p> <ul> <li> <p> <code>ParallelizationFactor</code> – Process multiple batches from each shard concurrently.</p> </li> </ul> <p>For information about which configuration parameters apply to each event source, see the following topics.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-ddb-params"> Amazon DynamoDB Streams</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-params"> Amazon Kinesis</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#services-sqs-params"> Amazon SQS</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html#services-mq-params"> Amazon MQ and RabbitMQ</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#services-msk-parms"> Amazon MSK</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html#services-kafka-parms"> Apache Kafka</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html#docdb-configuration"> Amazon DocumentDB</a> </p> </li> </ul>

        Args:
            event_source_arn: <p>The Amazon Resource Name (ARN) of the event source.</p> <ul> <li> <p> <b>Amazon Kinesis</b> – The ARN of the data stream or a stream consumer.</p> </li> <li> <p> <b>Amazon DynamoDB Streams</b> – The ARN of the stream.</p> </li> <li> <p> <b>Amazon Simple Queue Service</b> – The ARN of the queue.</p> </li> <li> <p> <b>Amazon Managed Streaming for Apache Kafka</b> – The ARN of the cluster or the ARN of the VPC connection (for <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#msk-multi-vpc">cross-account event source mappings</a>).</p> </li> <li> <p> <b>Amazon MQ</b> – The ARN of the broker.</p> </li> <li> <p> <b>Amazon DocumentDB</b> – The ARN of the DocumentDB change stream.</p> </li> </ul>
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Version or Alias ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.</p>
            enabled: <p>When true, the event source mapping is active. When false, Lambda pauses polling and invocation.</p> <p>Default: True</p>
            batch_size: <p>The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).</p> <ul> <li> <p> <b>Amazon Kinesis</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon DynamoDB Streams</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon Simple Queue Service</b> – Default 10. For standard queues the max is 10,000. For FIFO queues the max is 10.</p> </li> <li> <p> <b>Amazon Managed Streaming for Apache Kafka</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Self-managed Apache Kafka</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon MQ (ActiveMQ and RabbitMQ)</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>DocumentDB</b> – Default 100. Max 10,000.</p> </li> </ul>
            filter_criteria: <p>An object that defines the filter criteria that determine whether Lambda should process an event. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html">Lambda event filtering</a>.</p>
            kms_key_arn: <p> The ARN of the Key Management Service (KMS) customer managed key that Lambda uses to encrypt your function's <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-basics">filter criteria</a>. By default, Lambda does not encrypt your filter criteria object. Specify this property to encrypt data using your own customer managed key. </p>
            metrics_config: <p>The metrics configuration for your event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics">Event source mapping metrics</a>.</p>
            logging_config: <p>(Amazon MSK, and self-managed Apache Kafka only) The logging configuration for your event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/esm-logging.html">Event source mapping logging</a>.</p>
            scaling_config: <p>(Amazon SQS only) The scaling configuration for the event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-max-concurrency">Configuring maximum concurrency for Amazon SQS event sources</a>.</p>
            maximum_batching_window_in_seconds: <p>The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function. You can configure <code>MaximumBatchingWindowInSeconds</code> to any value from 0 seconds to 300 seconds in increments of seconds.</p> <p>For Kinesis, DynamoDB, and Amazon SQS event sources, the default batching window is 0 seconds. For Amazon MSK, Self-managed Apache Kafka, Amazon MQ, and DocumentDB event sources, the default batching window is 500 ms. Note that because you can only change <code>MaximumBatchingWindowInSeconds</code> in increments of seconds, you cannot revert back to the 500 ms default batching window after you have changed it. To restore the default batching window, you must create a new event source mapping.</p> <p>Related setting: For Kinesis, DynamoDB, and Amazon SQS event sources, when you set <code>BatchSize</code> to a value greater than 10, you must set <code>MaximumBatchingWindowInSeconds</code> to at least 1.</p>
            parallelization_factor: <p>(Kinesis and DynamoDB Streams only) The number of batches to process from each shard concurrently.</p>
            starting_position: <p>The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB Stream event sources. <code>AT_TIMESTAMP</code> is supported only for Amazon Kinesis streams, Amazon DocumentDB, Amazon MSK, and self-managed Apache Kafka.</p>
            starting_position_timestamp: <p>With <code>StartingPosition</code> set to <code>AT_TIMESTAMP</code>, the time from which to start reading. <code>StartingPositionTimestamp</code> cannot be in the future.</p>
            destination_config: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) A configuration object that specifies the destination of an event after Lambda processes it.</p>
            maximum_record_age_in_seconds: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records older than the specified age. The default value is infinite (-1).</p>
            bisect_batch_on_function_error: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) If the function returns an error, split the batch in two and retry.</p>
            maximum_retry_attempts: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires.</p>
            tags: <p>A list of tags to apply to the event source mapping.</p>
            tumbling_window_in_seconds: <p>(Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources. A value of 0 seconds indicates no tumbling window.</p>
            topics: <p>The name of the Kafka topic.</p>
            queues: <p> (MQ) The name of the Amazon MQ broker destination queue to consume. </p>
            source_access_configurations: <p>An array of authentication protocols or VPC components required to secure your event source.</p>
            self_managed_event_source: <p>The self-managed Apache Kafka cluster to receive records from.</p>
            function_response_types: <p>(Kinesis, DynamoDB Streams, Amazon MSK, self-managed Apache Kafka, and Amazon SQS) A list of current response type enums applied to the event source mapping.</p>
            amazon_managed_kafka_event_source_config: <p>Specific configuration settings for an Amazon Managed Streaming for Apache Kafka (Amazon MSK) event source.</p>
            self_managed_kafka_event_source_config: <p>Specific configuration settings for a self-managed Apache Kafka event source.</p>
            document_db_event_source_config: <p>Specific configuration settings for a DocumentDB event source.</p>
            provisioned_poller_config: <p>(Amazon SQS, Amazon MSK, and self-managed Apache Kafka only) The provisioned mode configuration for the event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html#invocation-eventsourcemapping-provisioned-mode">provisioned mode</a>.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a mapping between an event source and an AWS Lambda function
            The following example creates a mapping between an SQS queue and the my-function Lambda function.

            >>> await client.create(batch_size=5, event_source_arn='arn:aws:sqs:us-west-2:123456789012:my-queue', function_name='my-function')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.create_event_source_mapping_request.CreateEventSourceMappingRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.create_event_source_mapping

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.create_event_source_mapping.async_create_event_source_mapping(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.create_event_source_mapping_request.CreateEventSourceMappingRequest = {
            "function_name": function_name
        }
        if event_source_arn is not None:
            input_["event_source_arn"] = event_source_arn
        if enabled is not None:
            input_["enabled"] = enabled
        if batch_size is not None:
            input_["batch_size"] = batch_size
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if metrics_config is not None:
            input_["metrics_config"] = metrics_config
        if logging_config is not None:
            input_["logging_config"] = logging_config
        if scaling_config is not None:
            input_["scaling_config"] = scaling_config
        if maximum_batching_window_in_seconds is not None:
            input_["maximum_batching_window_in_seconds"] = (
                maximum_batching_window_in_seconds
            )
        if parallelization_factor is not None:
            input_["parallelization_factor"] = parallelization_factor
        if starting_position is not None:
            input_["starting_position"] = starting_position
        if starting_position_timestamp is not None:
            input_["starting_position_timestamp"] = starting_position_timestamp
        if destination_config is not None:
            input_["destination_config"] = destination_config
        if maximum_record_age_in_seconds is not None:
            input_["maximum_record_age_in_seconds"] = maximum_record_age_in_seconds
        if bisect_batch_on_function_error is not None:
            input_["bisect_batch_on_function_error"] = bisect_batch_on_function_error
        if maximum_retry_attempts is not None:
            input_["maximum_retry_attempts"] = maximum_retry_attempts
        if tags is not None:
            input_["tags"] = tags
        if tumbling_window_in_seconds is not None:
            input_["tumbling_window_in_seconds"] = tumbling_window_in_seconds
        if topics is not None:
            input_["topics"] = topics
        if queues is not None:
            input_["queues"] = queues
        if source_access_configurations is not None:
            input_["source_access_configurations"] = source_access_configurations
        if self_managed_event_source is not None:
            input_["self_managed_event_source"] = self_managed_event_source
        if function_response_types is not None:
            input_["function_response_types"] = function_response_types
        if amazon_managed_kafka_event_source_config is not None:
            input_["amazon_managed_kafka_event_source_config"] = (
                amazon_managed_kafka_event_source_config
            )
        if self_managed_kafka_event_source_config is not None:
            input_["self_managed_kafka_event_source_config"] = (
                self_managed_kafka_event_source_config
            )
        if document_db_event_source_config is not None:
            input_["document_db_event_source_config"] = document_db_event_source_config
        if provisioned_poller_config is not None:
            input_["provisioned_poller_config"] = provisioned_poller_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        uuid: "capo_lambda.types.uuid_string.UUIDString",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration":
        """<p>Returns details about an event source mapping. You can get the identifier of a mapping from the output of <a>ListEventSourceMappings</a>.</p>

        Args:
            uuid: <p>The identifier of the event source mapping.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a Lambda function's event source mapping
            The following example returns details about an event source mapping. To get a mapping's UUID, use ListEventSourceMappings.

            >>> await client.read(uuid='14e0db71-xmpl-4eb5-b481-8945cf9d10c2')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_event_source_mapping_request.GetEventSourceMappingRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_event_source_mapping

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_event_source_mapping.async_get_event_source_mapping(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_event_source_mapping_request.GetEventSourceMappingRequest = {
            "uuid": uuid
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        uuid: "capo_lambda.types.uuid_string.UUIDString",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        function_name: Optional[
            "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
        ] = None,
        enabled: Optional["capo_lambda.types.enabled.Enabled"] = None,
        batch_size: Optional["capo_lambda.types.batch_size.BatchSize"] = None,
        filter_criteria: Optional[
            "capo_lambda.types.filter_criteria.FilterCriteria"
        ] = None,
        kms_key_arn: Optional["capo_lambda.types.kms_key_arn.KMSKeyArn"] = None,
        metrics_config: Optional[
            "capo_lambda.types.event_source_mapping_metrics_config.EventSourceMappingMetricsConfig"
        ] = None,
        logging_config: Optional[
            "capo_lambda.types.event_source_mapping_logging_config.EventSourceMappingLoggingConfig"
        ] = None,
        scaling_config: Optional[
            "capo_lambda.types.scaling_config.ScalingConfig"
        ] = None,
        maximum_batching_window_in_seconds: Optional[
            "capo_lambda.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
        ] = None,
        parallelization_factor: Optional[
            "capo_lambda.types.parallelization_factor.ParallelizationFactor"
        ] = None,
        destination_config: Optional[
            "capo_lambda.types.destination_config.DestinationConfig"
        ] = None,
        maximum_record_age_in_seconds: Optional[
            "capo_lambda.types.maximum_record_age_in_seconds.MaximumRecordAgeInSeconds"
        ] = None,
        bisect_batch_on_function_error: Optional[
            "capo_lambda.types.bisect_batch_on_function_error.BisectBatchOnFunctionError"
        ] = None,
        maximum_retry_attempts: Optional[
            "capo_lambda.types.maximum_retry_attempts_event_source_mapping.MaximumRetryAttemptsEventSourceMapping"
        ] = None,
        tumbling_window_in_seconds: Optional[
            "capo_lambda.types.tumbling_window_in_seconds.TumblingWindowInSeconds"
        ] = None,
        source_access_configurations: Optional[
            "capo_lambda.types.source_access_configurations.SourceAccessConfigurations"
        ] = None,
        function_response_types: Optional[
            "capo_lambda.types.function_response_type_list.FunctionResponseTypeList"
        ] = None,
        amazon_managed_kafka_event_source_config: Optional[
            "capo_lambda.types.amazon_managed_kafka_event_source_config.AmazonManagedKafkaEventSourceConfig"
        ] = None,
        self_managed_kafka_event_source_config: Optional[
            "capo_lambda.types.self_managed_kafka_event_source_config.SelfManagedKafkaEventSourceConfig"
        ] = None,
        document_db_event_source_config: Optional[
            "capo_lambda.types.document_db_event_source_config.DocumentDBEventSourceConfig"
        ] = None,
        provisioned_poller_config: Optional[
            "capo_lambda.types.provisioned_poller_config.ProvisionedPollerConfig"
        ] = None,
    ) -> "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration":
        """<p>Updates an event source mapping. You can change the function that Lambda invokes, or pause invocation and resume later from the same location.</p> <p>For details about how to configure different event sources, see the following topics. </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-dynamodb-eventsourcemapping"> Amazon DynamoDB Streams</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-eventsourcemapping"> Amazon Kinesis</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource"> Amazon SQS</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html#services-mq-eventsourcemapping"> Amazon MQ and RabbitMQ</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html"> Amazon MSK</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/kafka-smaa.html"> Apache Kafka</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html"> Amazon DocumentDB</a> </p> </li> </ul> <p>The following error handling options are available for stream sources (DynamoDB, Kinesis, Amazon MSK, and self-managed Apache Kafka):</p> <ul> <li> <p> <code>BisectBatchOnFunctionError</code> – If the function returns an error, split the batch in two and retry.</p> </li> <li> <p> <code>MaximumRecordAgeInSeconds</code> – Discard records older than the specified age. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires</p> </li> <li> <p> <code>MaximumRetryAttempts</code> – Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires.</p> </li> <li> <p> <code>OnFailure</code> – Send discarded records to an Amazon SQS queue, Amazon SNS topic, Kafka topic, or Amazon S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html#invocation-async-destinations">Adding a destination</a>.</p> </li> </ul> <p>The following option is available only for DynamoDB and Kinesis event sources:</p> <ul> <li> <p> <code>ParallelizationFactor</code> – Process multiple batches from each shard concurrently.</p> </li> </ul> <p>For information about which configuration parameters apply to each event source, see the following topics.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-ddb-params"> Amazon DynamoDB Streams</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-params"> Amazon Kinesis</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#services-sqs-params"> Amazon SQS</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html#services-mq-params"> Amazon MQ and RabbitMQ</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#services-msk-parms"> Amazon MSK</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html#services-kafka-parms"> Apache Kafka</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html#docdb-configuration"> Amazon DocumentDB</a> </p> </li> </ul>

        Args:
            uuid: <p>The identifier of the event source mapping.</p>
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Version or Alias ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.</p>
            enabled: <p>When true, the event source mapping is active. When false, Lambda pauses polling and invocation.</p> <p>Default: True</p>
            batch_size: <p>The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).</p> <ul> <li> <p> <b>Amazon Kinesis</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon DynamoDB Streams</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon Simple Queue Service</b> – Default 10. For standard queues the max is 10,000. For FIFO queues the max is 10.</p> </li> <li> <p> <b>Amazon Managed Streaming for Apache Kafka</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Self-managed Apache Kafka</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon MQ (ActiveMQ and RabbitMQ)</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>DocumentDB</b> – Default 100. Max 10,000.</p> </li> </ul>
            filter_criteria: <p>An object that defines the filter criteria that determine whether Lambda should process an event. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html">Lambda event filtering</a>.</p>
            kms_key_arn: <p> The ARN of the Key Management Service (KMS) customer managed key that Lambda uses to encrypt your function's <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-basics">filter criteria</a>. By default, Lambda does not encrypt your filter criteria object. Specify this property to encrypt data using your own customer managed key. </p>
            metrics_config: <p>The metrics configuration for your event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics">Event source mapping metrics</a>.</p>
            scaling_config: <p>(Amazon SQS only) The scaling configuration for the event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-max-concurrency">Configuring maximum concurrency for Amazon SQS event sources</a>.</p>
            maximum_batching_window_in_seconds: <p>The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function. You can configure <code>MaximumBatchingWindowInSeconds</code> to any value from 0 seconds to 300 seconds in increments of seconds.</p> <p>For Kinesis, DynamoDB, and Amazon SQS event sources, the default batching window is 0 seconds. For Amazon MSK, Self-managed Apache Kafka, Amazon MQ, and DocumentDB event sources, the default batching window is 500 ms. Note that because you can only change <code>MaximumBatchingWindowInSeconds</code> in increments of seconds, you cannot revert back to the 500 ms default batching window after you have changed it. To restore the default batching window, you must create a new event source mapping.</p> <p>Related setting: For Kinesis, DynamoDB, and Amazon SQS event sources, when you set <code>BatchSize</code> to a value greater than 10, you must set <code>MaximumBatchingWindowInSeconds</code> to at least 1.</p>
            parallelization_factor: <p>(Kinesis and DynamoDB Streams only) The number of batches to process from each shard concurrently.</p>
            destination_config: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) A configuration object that specifies the destination of an event after Lambda processes it.</p>
            maximum_record_age_in_seconds: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records older than the specified age. The default value is infinite (-1).</p>
            bisect_batch_on_function_error: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) If the function returns an error, split the batch in two and retry.</p>
            maximum_retry_attempts: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires.</p>
            tumbling_window_in_seconds: <p>(Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources. A value of 0 seconds indicates no tumbling window.</p>
            source_access_configurations: <p>An array of authentication protocols or VPC components required to secure your event source.</p>
            function_response_types: <p>(Kinesis, DynamoDB Streams, Amazon MSK, self-managed Apache Kafka, and Amazon SQS) A list of current response type enums applied to the event source mapping.</p>
            document_db_event_source_config: <p>Specific configuration settings for a DocumentDB event source.</p>
            provisioned_poller_config: <p>(Amazon SQS, Amazon MSK, and self-managed Apache Kafka only) The provisioned mode configuration for the event source. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html#invocation-eventsourcemapping-provisioned-mode">provisioned mode</a>.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example, you tried to update an event source mapping in the CREATING state, or you tried to delete an event source mapping currently UPDATING.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a Lambda function event source mapping
            This operation updates a Lambda function event source mapping

            >>> await client.update(batch_size=123, enabled=True, function_name='myFunction', uuid='a1b2c3d4-5678-90ab-cdef-11111EXAMPLE')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.update_event_source_mapping_request.UpdateEventSourceMappingRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_event_source_mapping

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.update_event_source_mapping.async_update_event_source_mapping(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.update_event_source_mapping_request.UpdateEventSourceMappingRequest = {
            "uuid": uuid
        }
        if function_name is not None:
            input_["function_name"] = function_name
        if enabled is not None:
            input_["enabled"] = enabled
        if batch_size is not None:
            input_["batch_size"] = batch_size
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if metrics_config is not None:
            input_["metrics_config"] = metrics_config
        if logging_config is not None:
            input_["logging_config"] = logging_config
        if scaling_config is not None:
            input_["scaling_config"] = scaling_config
        if maximum_batching_window_in_seconds is not None:
            input_["maximum_batching_window_in_seconds"] = (
                maximum_batching_window_in_seconds
            )
        if parallelization_factor is not None:
            input_["parallelization_factor"] = parallelization_factor
        if destination_config is not None:
            input_["destination_config"] = destination_config
        if maximum_record_age_in_seconds is not None:
            input_["maximum_record_age_in_seconds"] = maximum_record_age_in_seconds
        if bisect_batch_on_function_error is not None:
            input_["bisect_batch_on_function_error"] = bisect_batch_on_function_error
        if maximum_retry_attempts is not None:
            input_["maximum_retry_attempts"] = maximum_retry_attempts
        if tumbling_window_in_seconds is not None:
            input_["tumbling_window_in_seconds"] = tumbling_window_in_seconds
        if source_access_configurations is not None:
            input_["source_access_configurations"] = source_access_configurations
        if function_response_types is not None:
            input_["function_response_types"] = function_response_types
        if amazon_managed_kafka_event_source_config is not None:
            input_["amazon_managed_kafka_event_source_config"] = (
                amazon_managed_kafka_event_source_config
            )
        if self_managed_kafka_event_source_config is not None:
            input_["self_managed_kafka_event_source_config"] = (
                self_managed_kafka_event_source_config
            )
        if document_db_event_source_config is not None:
            input_["document_db_event_source_config"] = document_db_event_source_config
        if provisioned_poller_config is not None:
            input_["provisioned_poller_config"] = provisioned_poller_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        uuid: "capo_lambda.types.uuid_string.UUIDString",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration":
        """<p>Deletes an <a href="https://docs.aws.amazon.com/lambda/latest/dg/intro-invocation-modes.html">event source mapping</a>. You can get the identifier of a mapping from the output of <a>ListEventSourceMappings</a>.</p> <p>When you delete an event source mapping, it enters a <code>Deleting</code> state and might not be completely deleted for several seconds.</p>

        Args:
            uuid: <p>The identifier of the event source mapping.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example, you tried to update an event source mapping in the CREATING state, or you tried to delete an event source mapping currently UPDATING.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a Lambda function event source mapping
            The following example deletes an event source mapping. To get a mapping's UUID, use ListEventSourceMappings.

            >>> await client.delete(uuid='14e0db71-xmpl-4eb5-b481-8945cf9d10c2')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.delete_event_source_mapping_request.DeleteEventSourceMappingRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.delete_event_source_mapping

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.delete_event_source_mapping.async_delete_event_source_mapping(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.delete_event_source_mapping_request.DeleteEventSourceMappingRequest = {
            "uuid": uuid
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        event_source_arn: Optional["capo_lambda.types.arn.Arn"] = None,
        function_name: Optional[
            "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
        ] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "capo_lambda.types.list_event_source_mappings_response.ListEventSourceMappingsResponse":
        """<p>Lists event source mappings. Specify an <code>EventSourceArn</code> to show only event source mappings for a single event source.</p>

        Args:
            event_source_arn: <p>The Amazon Resource Name (ARN) of the event source.</p> <ul> <li> <p> <b>Amazon Kinesis</b> – The ARN of the data stream or a stream consumer.</p> </li> <li> <p> <b>Amazon DynamoDB Streams</b> – The ARN of the stream.</p> </li> <li> <p> <b>Amazon Simple Queue Service</b> – The ARN of the queue.</p> </li> <li> <p> <b>Amazon Managed Streaming for Apache Kafka</b> – The ARN of the cluster or the ARN of the VPC connection (for <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#msk-multi-vpc">cross-account event source mappings</a>).</p> </li> <li> <p> <b>Amazon MQ</b> – The ARN of the broker.</p> </li> <li> <p> <b>Amazon DocumentDB</b> – The ARN of the DocumentDB change stream.</p> </li> </ul>
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Version or Alias ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.</p>
            marker: <p>A pagination token returned by a previous call.</p>
            max_items: <p>The maximum number of event source mappings to return. Note that ListEventSourceMappings returns a maximum of 100 items in each response, even if you set the number higher.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the event source mappings for a function
            The following example returns a list of the event source mappings for a function named my-function.

            >>> await client.list(function_name='my-function')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.list_event_source_mappings_request.ListEventSourceMappingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.list_event_source_mappings_response.ListEventSourceMappingsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_event_source_mappings

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.list_event_source_mappings.async_list_event_source_mappings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_event_source_mappings_request.ListEventSourceMappingsRequest = {}
        if event_source_arn is not None:
            input_["event_source_arn"] = event_source_arn
        if function_name is not None:
            input_["function_name"] = function_name
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
