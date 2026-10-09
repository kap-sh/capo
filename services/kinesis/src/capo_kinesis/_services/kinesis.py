"""Generated from Smithy shape ``com.amazonaws.kinesis#Kinesis_20131202``."""

import random
import time
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_kinesis._auth._signers
import capo_kinesis._auth._sigv4
from capo_kinesis._auth._identity import Credentials
from capo_kinesis._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_kinesis._auth._zapros_handler import AuthMiddleware
from capo_kinesis._pagination import resolve_path as _resolve_path
from capo_kinesis._services._aws_config import aws_config
from capo_kinesis._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)
from capo_kinesis.errors import ServiceError, WaiterTimeoutError

if TYPE_CHECKING:
    import capo_kinesis.types.add_tags_to_stream_input
    import capo_kinesis.types.boolean_object
    import capo_kinesis.types.channel_arn
    import capo_kinesis.types.channel_encryption_configuration
    import capo_kinesis.types.channel_logging_configuration
    import capo_kinesis.types.channel_logging_update_input
    import capo_kinesis.types.channel_name
    import capo_kinesis.types.channel_stream_configuration_list
    import capo_kinesis.types.channel_summary
    import capo_kinesis.types.consumer_arn
    import capo_kinesis.types.consumer_name
    import capo_kinesis.types.create_channel_input
    import capo_kinesis.types.create_channel_output
    import capo_kinesis.types.create_stream_input
    import capo_kinesis.types.data
    import capo_kinesis.types.decrease_stream_retention_period_input
    import capo_kinesis.types.delete_channel_input
    import capo_kinesis.types.delete_resource_policy_input
    import capo_kinesis.types.delete_stream_input
    import capo_kinesis.types.deregister_stream_consumer_input
    import capo_kinesis.types.describe_account_settings_input
    import capo_kinesis.types.describe_account_settings_output
    import capo_kinesis.types.describe_channel_input
    import capo_kinesis.types.describe_channel_output
    import capo_kinesis.types.describe_limits_input
    import capo_kinesis.types.describe_limits_output
    import capo_kinesis.types.describe_stream_consumer_input
    import capo_kinesis.types.describe_stream_consumer_output
    import capo_kinesis.types.describe_stream_input
    import capo_kinesis.types.describe_stream_input_limit
    import capo_kinesis.types.describe_stream_output
    import capo_kinesis.types.describe_stream_summary_input
    import capo_kinesis.types.describe_stream_summary_output
    import capo_kinesis.types.disable_enhanced_monitoring_input
    import capo_kinesis.types.enable_enhanced_monitoring_input
    import capo_kinesis.types.encryption_type
    import capo_kinesis.types.enhanced_monitoring_output
    import capo_kinesis.types.get_records_input
    import capo_kinesis.types.get_records_input_limit
    import capo_kinesis.types.get_records_output
    import capo_kinesis.types.get_resource_policy_input
    import capo_kinesis.types.get_resource_policy_output
    import capo_kinesis.types.get_shard_iterator_input
    import capo_kinesis.types.get_shard_iterator_output
    import capo_kinesis.types.hash_key
    import capo_kinesis.types.increase_stream_retention_period_input
    import capo_kinesis.types.key_id
    import capo_kinesis.types.list_channels_input
    import capo_kinesis.types.list_channels_input_limit
    import capo_kinesis.types.list_channels_output
    import capo_kinesis.types.list_shards_input
    import capo_kinesis.types.list_shards_input_limit
    import capo_kinesis.types.list_shards_output
    import capo_kinesis.types.list_stream_consumers_input
    import capo_kinesis.types.list_stream_consumers_input_limit
    import capo_kinesis.types.list_stream_consumers_output
    import capo_kinesis.types.list_streams_input
    import capo_kinesis.types.list_streams_input_limit
    import capo_kinesis.types.list_streams_output
    import capo_kinesis.types.list_tags_for_resource_input
    import capo_kinesis.types.list_tags_for_resource_output
    import capo_kinesis.types.list_tags_for_stream_input
    import capo_kinesis.types.list_tags_for_stream_input_limit
    import capo_kinesis.types.list_tags_for_stream_output
    import capo_kinesis.types.max_record_size_in_ki_b
    import capo_kinesis.types.merge_shards_input
    import capo_kinesis.types.metrics_name_list
    import capo_kinesis.types.minimum_throughput_billing_commitment_input
    import capo_kinesis.types.natural_integer_object
    import capo_kinesis.types.next_token
    import capo_kinesis.types.partition_key
    import capo_kinesis.types.policy
    import capo_kinesis.types.positive_integer_object
    import capo_kinesis.types.put_record_input
    import capo_kinesis.types.put_record_output
    import capo_kinesis.types.put_records_input
    import capo_kinesis.types.put_records_output
    import capo_kinesis.types.put_records_request_entry_list
    import capo_kinesis.types.put_resource_policy_input
    import capo_kinesis.types.record_distribution_strategy
    import capo_kinesis.types.register_stream_consumer_input
    import capo_kinesis.types.register_stream_consumer_output
    import capo_kinesis.types.remove_tags_from_stream_input
    import capo_kinesis.types.resource_arn
    import capo_kinesis.types.retention_period_hours
    import capo_kinesis.types.role_arn
    import capo_kinesis.types.s3_destination_configuration
    import capo_kinesis.types.s3_destination_update_input
    import capo_kinesis.types.s3_tables_destination_configuration
    import capo_kinesis.types.s3_tables_destination_update_input
    import capo_kinesis.types.scaling_type
    import capo_kinesis.types.sequence_number
    import capo_kinesis.types.shard_filter
    import capo_kinesis.types.shard_id
    import capo_kinesis.types.shard_iterator
    import capo_kinesis.types.shard_iterator_type
    import capo_kinesis.types.split_shard_input
    import capo_kinesis.types.start_stream_encryption_input
    import capo_kinesis.types.starting_position
    import capo_kinesis.types.stop_stream_encryption_input
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_filter_list
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.stream_mode_details
    import capo_kinesis.types.stream_name
    import capo_kinesis.types.subscribe_to_shard_input
    import capo_kinesis.types.subscribe_to_shard_output
    import capo_kinesis.types.tag_key
    import capo_kinesis.types.tag_key_list
    import capo_kinesis.types.tag_map
    import capo_kinesis.types.tag_resource_input
    import capo_kinesis.types.timestamp
    import capo_kinesis.types.untag_resource_input
    import capo_kinesis.types.update_account_settings_input
    import capo_kinesis.types.update_account_settings_output
    import capo_kinesis.types.update_channel_input
    import capo_kinesis.types.update_channel_output
    import capo_kinesis.types.update_max_record_size_input
    import capo_kinesis.types.update_shard_count_input
    import capo_kinesis.types.update_shard_count_output
    import capo_kinesis.types.update_stream_mode_input
    import capo_kinesis.types.update_stream_record_distribution_strategy_input
    import capo_kinesis.types.update_stream_warm_throughput_input
    import capo_kinesis.types.update_stream_warm_throughput_output


class KinesisClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    account_id: str | None
    account_id_endpoint_mode: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class KinesisClient:
    """A client for the ``Kinesis`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        account_id: The value of the ``AWS::Auth::AccountId`` endpoint parameter.
        account_id_endpoint_mode: The value of the ``AWS::Auth::AccountIdEndpointMode`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        account_id: str | None = None,
        account_id_endpoint_mode: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = KinesisClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "account_id": account_id,
                "account_id_endpoint_mode": account_id_endpoint_mode,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[KinesisClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: KinesisClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            account_id=overrides.get("account_id", self._config.get("account_id")),
            account_id_endpoint_mode=overrides.get(
                "account_id_endpoint_mode", self._config.get("account_id_endpoint_mode")
            ),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def add_tags_to_stream(
        self,
        tags: "capo_kinesis.types.tag_map.TagMap",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> None:
        """<p>Adds or updates tags for the specified Kinesis data stream. You can assign up to 50 tags to a data stream.</p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note> <p>If tags have already been assigned to the stream, <code>AddTagsToStream</code> overwrites any existing tags that correspond to the specified tag keys.</p> <p> <a>AddTagsToStream</a> has a limit of five transactions per second per account.</p>

        Args:
            stream_name: <p>The name of the stream.</p>
            tags: <p>A set of up to 50 key-value pairs to use to create the tags. A tag consists of a required key and an optional value. You can add up to 50 tags per resource.</p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.add_tags_to_stream_input.AddTagsToStreamInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.add_tags_to_stream

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.add_tags_to_stream.add_tags_to_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.add_tags_to_stream_input.AddTagsToStreamInput = {
            "tags": tags
        }
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_channel(
        self,
        channel_name: "capo_kinesis.types.channel_name.ChannelName",
        service_execution_role_arn: "capo_kinesis.types.role_arn.RoleARN",
        stream_configuration_list: "capo_kinesis.types.channel_stream_configuration_list.ChannelStreamConfigurationList",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        s3_destination_configuration: Optional[
            "capo_kinesis.types.s3_destination_configuration.S3DestinationConfiguration"
        ] = None,
        s3_tables_destination_configuration: Optional[
            "capo_kinesis.types.s3_tables_destination_configuration.S3TablesDestinationConfiguration"
        ] = None,
        encryption_configuration: Optional[
            "capo_kinesis.types.channel_encryption_configuration.ChannelEncryptionConfiguration"
        ] = None,
        tags: Optional["capo_kinesis.types.tag_map.TagMap"] = None,
        logging_configuration: Optional[
            "capo_kinesis.types.channel_logging_configuration.ChannelLoggingConfiguration"
        ] = None,
    ) -> "capo_kinesis.types.create_channel_output.CreateChannelOutput":
        """<p>Creates a channel that delivers records from a Kinesis data stream to a destination. A channel reads records from the specified stream and writes them to streaming tables on Apache Iceberg (Amazon S3 Tables) or to a general purpose Amazon S3 bucket.</p> <p>You must specify either <code>S3DestinationConfiguration</code> or <code>S3TablesDestinationConfiguration</code>, but not both.</p> <p>To use this operation, you must have permission to pass the specified service execution IAM role to Amazon Kinesis Data Streams (the <code>iam:PassRole</code> permission on that role).</p> <p>Creating a channel is an asynchronous operation. Upon receiving the request, Amazon Kinesis Data Streams returns immediately with the channel in the <code>CREATING</code> state. After provisioning is complete, Amazon Kinesis Data Streams sets the state to <code>ACTIVE</code>. You can use <a>DescribeChannel</a> to check the current state.</p> <p>This operation is only supported for data streams with the on-demand capacity mode.</p> <p>This operation has a call limit of 5 transactions per second (TPS) for each Amazon Web Services account. Exceeding 5 TPS results in a <code>LimitExceededException</code>.</p>

        Args:
            channel_name: <p>The name of the channel. The name is unique within your Amazon Web Services account and Amazon Web Services Region.</p>
            service_execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that Amazon Kinesis Data Streams assumes to write records to the destination.</p>
            stream_configuration_list: <p>The source stream configuration for the channel. Currently, one stream is supported per channel.</p>
            s3_destination_configuration: <p>The configuration for delivery to a general purpose Amazon S3 bucket. Specify this parameter when <code>S3TablesDestinationConfiguration</code> is not specified.</p>
            s3_tables_destination_configuration: <p>The configuration for delivery to streaming tables on Apache Iceberg in Amazon S3 Tables. Specify this parameter when <code>S3DestinationConfiguration</code> is not specified.</p>
            encryption_configuration: <p>The server-side encryption configuration that uses an Amazon Web Services KMS key to encrypt data delivered to the destination.</p>
            tags: <p>A set of key-value pairs to assign to the channel. A tag consists of a required key and an optional value.</p>
            logging_configuration: <p>The Amazon CloudWatch Logs configuration for the channel.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>The ciphertext references a key that doesn't exist or that you don't have access to.</p>
            capo_kinesis.errors.kms_disabled_exception.KMSDisabledException: <p>The request was rejected because the specified customer master key (CMK) isn't enabled.</p>
            capo_kinesis.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>The request was rejected because the state of the specified resource isn't valid for this request. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html">How Key State Affects Use of a Customer Master Key</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p>
            capo_kinesis.errors.kms_not_found_exception.KMSNotFoundException: <p>The request was rejected because the specified entity or resource can't be found.</p>
            capo_kinesis.errors.kms_opt_in_required.KMSOptInRequired: <p>The Amazon Web Services access key ID needs a subscription for the service.</p>
            capo_kinesis.errors.kms_throttling_exception.KMSThrottlingException: <p>The request was denied due to request throttling. For more information about throttling, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/limits.html#requests-per-second">Limits</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.validation_exception.ValidationException: <p>Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode. </p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an S3 channel

            >>> client.create_channel(channel_name='my-channel-name', service_execution_role_arn='arn:aws:iam::123456789012:role/my-channel-role', stream_configuration_list=[{'StreamARN': 'arn:aws:kinesis:us-east-1:123456789012:stream/my-stream-name', 'RecordConfiguration': {'RecordFormatType': 'JSON'}}], s3_destination_configuration={'StorageConfiguration': {'BucketARN': 'arn:aws:s3:::my-channel-bucket', 'ExpectedBucketOwner': '123456789012', 'CompressionType': 'ZSTD'}, 'DeadLetterQueueS3Configuration': {'BucketARN': 'arn:aws:s3:::my-channel-dlq-bucket', 'ExpectedBucketOwner': '123456789012'}}, encryption_configuration={'EncryptionType': 'KMS', 'KeyId': 'arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab'}, logging_configuration={'CloudWatchLogs': {'Enabled': True, 'LogGroupName': '/aws/kinesis/my-channel', 'LogStreamName': 'my-channel-log-stream'}})
            To create an S3 Tables channel

            >>> client.create_channel(channel_name='my-channel-name', service_execution_role_arn='arn:aws:iam::123456789012:role/my-channel-role', stream_configuration_list=[{'StreamARN': 'arn:aws:kinesis:us-east-1:123456789012:stream/my-stream-name', 'RecordConfiguration': {'RecordFormatType': 'JSON', 'GSRSchemaARN': 'arn:aws:glue:us-east-1:123456789012:schema/my-registry/my-schema'}}], s3_tables_destination_configuration={'DeadLetterQueueS3Configuration': {'BucketARN': 'arn:aws:s3:::my-channel-dlq-bucket', 'ExpectedBucketOwner': '123456789012'}, 'S3TablesConfigurationList': [{'TableBucketARN': 'arn:aws:s3tables:us-east-1:123456789012:bucket/my-table-bucket', 'Namespace': 'my_namespace', 'TableName': 'my_table', 'CompressionType': 'ZSTD', 'PartitionSpec': {'PartitionFields': [{'Transform': 'TIME_HOUR', 'SourceName': 'creation_ts'}]}}]}, encryption_configuration={'EncryptionType': 'KMS', 'KeyId': 'arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab'}, logging_configuration={'CloudWatchLogs': {'Enabled': True, 'LogGroupName': '/aws/kinesis/my-channel', 'LogStreamName': 'my-channel-log-stream'}})
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.create_channel_input.CreateChannelInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.create_channel_output.CreateChannelOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.create_channel

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.create_channel.create_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.create_channel_input.CreateChannelInput = {
            "channel_name": channel_name,
            "service_execution_role_arn": service_execution_role_arn,
            "stream_configuration_list": stream_configuration_list,
        }
        if s3_destination_configuration is not None:
            input_["s3_destination_configuration"] = s3_destination_configuration
        if s3_tables_destination_configuration is not None:
            input_["s3_tables_destination_configuration"] = (
                s3_tables_destination_configuration
            )
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if tags is not None:
            input_["tags"] = tags
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_stream(
        self,
        stream_name: "capo_kinesis.types.stream_name.StreamName",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        shard_count: Optional[
            "capo_kinesis.types.positive_integer_object.PositiveIntegerObject"
        ] = None,
        stream_mode_details: Optional[
            "capo_kinesis.types.stream_mode_details.StreamModeDetails"
        ] = None,
        tags: Optional["capo_kinesis.types.tag_map.TagMap"] = None,
        warm_throughput_mi_bps: Optional[
            "capo_kinesis.types.natural_integer_object.NaturalIntegerObject"
        ] = None,
        max_record_size_in_ki_b: Optional[
            "capo_kinesis.types.max_record_size_in_ki_b.MaxRecordSizeInKiB"
        ] = None,
        record_distribution_strategy: Optional[
            "capo_kinesis.types.record_distribution_strategy.RecordDistributionStrategy"
        ] = None,
    ) -> None:
        """<p>Creates a Kinesis data stream. A stream captures and transports data records that are continuously emitted from different data sources or <i>producers</i>. Scale-out within a stream is explicitly supported by means of shards, which are uniquely identified groups of data records in a stream.</p> <p>You can create your data stream using either on-demand or provisioned capacity mode. Data streams with an on-demand mode require no capacity planning and automatically scale to handle gigabytes of write and read throughput per minute. With the on-demand mode, Kinesis Data Streams automatically manages the shards in order to provide the necessary throughput.</p> <p>If you'd still like to proactively scale your on-demand data stream’s capacity, you can unlock the warm throughput feature for on-demand data streams by enabling <code>MinimumThroughputBillingCommitment</code> for your account. Once your account has <code>MinimumThroughputBillingCommitment</code> enabled, you can specify the warm throughput in MiB per second that your stream can support in writes.</p> <p>For the data streams with a provisioned mode, you must specify the number of shards for the data stream. Each shard can support reads up to five transactions per second, up to a maximum data read total of 2 MiB per second. Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 1 MiB per second. If the amount of data input increases or decreases, you can add or remove shards.</p> <p>The stream name identifies the stream. The name is scoped to the Amazon Web Services account used by the application. It is also scoped by Amazon Web Services Region. That is, two streams in two different accounts can have the same name, and two streams in the same account, but in two different Regions, can have the same name.</p> <p> <code>CreateStream</code> is an asynchronous operation. Upon receiving a <code>CreateStream</code> request, Kinesis Data Streams immediately returns and sets the stream status to <code>CREATING</code>. After the stream is created, Kinesis Data Streams sets the stream status to <code>ACTIVE</code>. You should perform read and write operations only on an <code>ACTIVE</code> stream. </p> <p>You receive a <code>LimitExceededException</code> when making a <code>CreateStream</code> request when you try to do one of the following:</p> <ul> <li> <p>Have more than five streams in the <code>CREATING</code> state at any point in time.</p> </li> <li> <p>Create more shards than are authorized for your account.</p> </li> </ul> <p>For the default shard or on-demand throughput limits for an Amazon Web Services account, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html">Amazon Kinesis Data Streams Limits</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>. To increase this limit, <a href="https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html">contact Amazon Web Services Support</a>.</p> <p>You can use <a>DescribeStreamSummary</a> to check the stream status, which is returned in <code>StreamStatus</code>.</p> <p> <a>CreateStream</a> has a limit of five transactions per second per account.</p> <p>You can add tags to the stream when making a <code>CreateStream</code> request by setting the <code>Tags</code> parameter. If you pass the <code>Tags</code> parameter, in addition to having the <code>kinesis:CreateStream</code> permission, you must also have the <code>kinesis:AddTagsToStream</code> permission for the stream that will be created. The <code>kinesis:TagResource</code> permission won’t work to tag streams on creation. Tags will take effect from the <code>CREATING</code> status of the stream, but you can't make any updates to the tags until the stream is in <code>ACTIVE</code> state.</p>

        Args:
            stream_name: <p>A name to identify the stream. The stream name is scoped to the Amazon Web Services account used by the application that creates the stream. It is also scoped by Amazon Web Services Region. That is, two streams in two different Amazon Web Services accounts can have the same name. Two streams in the same Amazon Web Services account but in two different Regions can also have the same name.</p>
            shard_count: <p>The number of shards that the stream will use. The throughput of the stream is a function of the number of shards; more shards are required for greater provisioned throughput.</p>
            stream_mode_details: <p> Indicates the capacity mode of the data stream. Currently, in Kinesis Data Streams, you can choose between an <b>on-demand</b> capacity mode and a <b>provisioned</b> capacity mode for your data streams.</p>
            tags: <p>A set of up to 50 key-value pairs to use to create the tags. A tag consists of a required key and an optional value.</p>
            warm_throughput_mi_bps: <p>The target warm throughput in MB/s that the stream should be scaled to handle. This represents the throughput capacity that will be immediately available for write operations.</p>
            max_record_size_in_ki_b: <p>The maximum record size of a single record in kibibyte (KiB) that you can write to, and read from a stream.</p>
            record_distribution_strategy: <p>The record distribution strategy for the stream, which determines how Amazon Kinesis Data Streams distributes records across shards. Specify one of the following values:</p> <ul> <li> <p> <code>AUTO</code> – Amazon Kinesis Data Streams distributes records evenly across shards and ignores any partition key and <code>ExplicitHashKey</code> that producers supply. Use this value for stateless workloads that do not require partition-key ordering.</p> </li> <li> <p> <code>USER_PARTITION_KEY</code> – Producers must supply a partition key, which Amazon Kinesis Data Streams uses to determine shard placement. This is the default.</p> </li> </ul> <p>The record distribution strategy is only supported for streams that use the on-demand capacity mode. If you do not specify this parameter, the stream uses <code>USER_PARTITION_KEY</code>.</p>

        Raises:
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.validation_exception.ValidationException: <p>Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode. </p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.create_stream_input.CreateStreamInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.create_stream

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.create_stream.create_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.create_stream_input.CreateStreamInput = {
            "stream_name": stream_name
        }
        if shard_count is not None:
            input_["shard_count"] = shard_count
        if stream_mode_details is not None:
            input_["stream_mode_details"] = stream_mode_details
        if tags is not None:
            input_["tags"] = tags
        if warm_throughput_mi_bps is not None:
            input_["warm_throughput_mi_bps"] = warm_throughput_mi_bps
        if max_record_size_in_ki_b is not None:
            input_["max_record_size_in_ki_b"] = max_record_size_in_ki_b
        if record_distribution_strategy is not None:
            input_["record_distribution_strategy"] = record_distribution_strategy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def decrease_stream_retention_period(
        self,
        retention_period_hours: "capo_kinesis.types.retention_period_hours.RetentionPeriodHours",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> None:
        """<p>Decreases the Kinesis data stream's retention period, which is the length of time data records are accessible after they are added to the stream. The minimum value of a stream's retention period is 24 hours.</p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note> <p>This operation may result in lost data. For example, if the stream's retention period is 48 hours and is decreased to 24 hours, any data already in the stream that is older than 24 hours is inaccessible.</p>

        Args:
            stream_name: <p>The name of the stream to modify.</p>
            retention_period_hours: <p>The new retention period of the stream, in hours. Must be less than the current retention period.</p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.decrease_stream_retention_period_input.DecreaseStreamRetentionPeriodInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.decrease_stream_retention_period

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.decrease_stream_retention_period.decrease_stream_retention_period(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.decrease_stream_retention_period_input.DecreaseStreamRetentionPeriodInput = {
            "retention_period_hours": retention_period_hours
        }
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_channel(
        self,
        channel_arn: "capo_kinesis.types.channel_arn.ChannelARN",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified channel. Deleting a channel stops delivery from the source stream to the destination. Data already delivered to the destination is not deleted.</p> <p>A stream cannot be deleted while it has active channels. Use <a>ListChannels</a> with a stream filter to find the channels attached to a stream before deleting it.</p> <p>This operation has a call limit of 5 transactions per second (TPS) for each Amazon Web Services account. Exceeding 5 TPS results in a <code>LimitExceededException</code>.</p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) of the channel to delete.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.validation_exception.ValidationException: <p>Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode. </p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a channel

            >>> client.delete_channel(channel_arn='arn:aws:kinesis:us-east-1:123456789012:channel/my-channel-id')
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.delete_channel_input.DeleteChannelInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.delete_channel

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.delete_channel.delete_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.delete_channel_input.DeleteChannelInput = {
            "channel_arn": channel_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_policy(
        self,
        resource_arn: "capo_kinesis.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> None:
        r"""<p>Delete a policy for the specified data stream or consumer. Request patterns can be one of the following:</p> <ul> <li> <p>Data stream pattern: <code>arn:aws.*:kinesis:.*:\d{12}:.*stream/\S+</code> </p> </li> <li> <p>Consumer pattern: <code>^(arn):aws.*:kinesis:.*:\d{12}:.*stream\/[a-zA-Z0-9_.-]+\/consumer\/[a-zA-Z0-9_.-]+:[0-9]+</code> </p> </li> </ul>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the data stream or consumer.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.delete_resource_policy_input.DeleteResourcePolicyInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.delete_resource_policy

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.delete_resource_policy_input.DeleteResourcePolicyInput = {
            "resource_arn": resource_arn
        }
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_stream(
        self,
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        enforce_consumer_deletion: Optional[
            "capo_kinesis.types.boolean_object.BooleanObject"
        ] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> None:
        """<p>Deletes a Kinesis data stream and all its shards and data. You must shut down any applications that are operating on the stream before you delete the stream. If an application attempts to operate on a deleted stream, it receives the exception <code>ResourceNotFoundException</code>.</p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note> <p>If the stream is in the <code>ACTIVE</code> state, you can delete it. After a <code>DeleteStream</code> request, the specified stream is in the <code>DELETING</code> state until Kinesis Data Streams completes the deletion.</p> <p> <b>Note:</b> Kinesis Data Streams might continue to accept data read and write operations, such as <a>PutRecord</a>, <a>PutRecords</a>, and <a>GetRecords</a>, on a stream in the <code>DELETING</code> state until the stream deletion is complete.</p> <p>When you delete a stream, any shards in that stream are also deleted, and any tags are dissociated from the stream.</p> <p>You can use the <a>DescribeStreamSummary</a> operation to check the state of the stream, which is returned in <code>StreamStatus</code>.</p> <p> <a>DeleteStream</a> has a limit of five transactions per second per account.</p>

        Args:
            stream_name: <p>The name of the stream to delete.</p>
            enforce_consumer_deletion: <p>If this parameter is unset (<code>null</code>) or if you set it to <code>false</code>, and the stream has registered consumers, the call to <code>DeleteStream</code> fails with a <code>ResourceInUseException</code>. </p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.delete_stream_input.DeleteStreamInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.delete_stream

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.delete_stream.delete_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.delete_stream_input.DeleteStreamInput = {}
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if enforce_consumer_deletion is not None:
            input_["enforce_consumer_deletion"] = enforce_consumer_deletion
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_stream_consumer(
        self,
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        consumer_name: Optional["capo_kinesis.types.consumer_name.ConsumerName"] = None,
        consumer_arn: Optional["capo_kinesis.types.consumer_arn.ConsumerARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> None:
        """<p>To deregister a consumer, provide its ARN. Alternatively, you can provide the ARN of the data stream and the name you gave the consumer when you registered it. You may also provide all three parameters, as long as they don't conflict with each other. If you don't know the name or ARN of the consumer that you want to deregister, you can use the <a>ListStreamConsumers</a> operation to get a list of the descriptions of all the consumers that are currently registered with a given data stream. The description of a consumer contains its name and ARN.</p> <p>This operation has a limit of five transactions per second per stream.</p>

        Args:
            stream_arn: <p>The ARN of the Kinesis data stream that the consumer is registered with. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>
            consumer_name: <p>The name that you gave to the consumer.</p>
            consumer_arn: <p>The ARN returned by Kinesis Data Streams when you registered the consumer. If you don't know the ARN of the consumer that you want to deregister, you can use the ListStreamConsumers operation to get a list of the descriptions of all the consumers that are currently registered with a given data stream. The description of a consumer contains its ARN.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.deregister_stream_consumer_input.DeregisterStreamConsumerInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.deregister_stream_consumer

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.deregister_stream_consumer.deregister_stream_consumer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.deregister_stream_consumer_input.DeregisterStreamConsumerInput = {}
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if consumer_name is not None:
            input_["consumer_name"] = consumer_name
        if consumer_arn is not None:
            input_["consumer_arn"] = consumer_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_account_settings(
        self, *, config_overrides: Optional[KinesisClientConfig] = None
    ) -> "capo_kinesis.types.describe_account_settings_output.DescribeAccountSettingsOutput":
        """<p>Describes the account-level settings for Amazon Kinesis Data Streams. This operation returns information about the minimum throughput billing commitments and other account-level configurations.</p> <p>This API has a call limit of 5 transactions per second (TPS) for each Amazon Web Services account. TPS over 5 will initiate the <code>LimitExceededException</code>.</p>

        Raises:
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.describe_account_settings_input.DescribeAccountSettingsInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.describe_account_settings_output.DescribeAccountSettingsOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.describe_account_settings

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.describe_account_settings.describe_account_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.describe_account_settings_input.DescribeAccountSettingsInput = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_channel(
        self,
        channel_arn: "capo_kinesis.types.channel_arn.ChannelARN",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
    ) -> "capo_kinesis.types.describe_channel_output.DescribeChannelOutput":
        """<p>Describes the specified channel, including its configuration and current status.</p> <p>Use this operation to verify that a channel reached the <code>ACTIVE</code> state after creation, or to diagnose a channel in the <code>FAILED</code> state by reading the <code>ChannelStatusReason</code>.</p> <p>This operation has a call limit of 5 transactions per second (TPS) for each Amazon Web Services account. Exceeding 5 TPS results in a <code>LimitExceededException</code>.</p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) of the channel to describe.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.validation_exception.ValidationException: <p>Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode. </p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a channel

            >>> client.describe_channel(channel_arn='arn:aws:kinesis:us-east-1:123456789012:channel/my-channel-id')
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.describe_channel_input.DescribeChannelInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.describe_channel_output.DescribeChannelOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.describe_channel

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.describe_channel.describe_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.describe_channel_input.DescribeChannelInput = {
            "channel_arn": channel_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_limits(
        self, *, config_overrides: Optional[KinesisClientConfig] = None
    ) -> "capo_kinesis.types.describe_limits_output.DescribeLimitsOutput":
        """<p>Describes the shard limits and usage for the account.</p> <p>If you update your account limits, the old limits might be returned for a few minutes.</p> <p>This operation has a limit of one transaction per second per account.</p>

        Raises:
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.describe_limits_input.DescribeLimitsInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.describe_limits_output.DescribeLimitsOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.describe_limits

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.describe_limits.describe_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.describe_limits_input.DescribeLimitsInput = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_stream(
        self,
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        limit: Optional[
            "capo_kinesis.types.describe_stream_input_limit.DescribeStreamInputLimit"
        ] = None,
        exclusive_start_shard_id: Optional[
            "capo_kinesis.types.shard_id.ShardId"
        ] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> "capo_kinesis.types.describe_stream_output.DescribeStreamOutput":
        """<p>Describes the specified Kinesis data stream.</p> <note> <p>This API has been revised. It's highly recommended that you use the <a>DescribeStreamSummary</a> API to get a summarized description of the specified Kinesis data stream and the <a>ListShards</a> API to list the shards in a specified data stream and obtain information about each shard. </p> </note> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note> <p>The information returned includes the stream name, Amazon Resource Name (ARN), creation time, enhanced metric configuration, and shard map. The shard map is an array of shard objects. For each shard object, there is the hash key and sequence number ranges that the shard spans, and the IDs of any earlier shards that played in a role in creating the shard. Every record ingested in the stream is identified by a sequence number, which is assigned when the record is put into the stream.</p> <p>You can limit the number of shards returned by each call. For more information, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/kinesis-using-sdk-java-retrieve-shards.html">Retrieving Shards from a Stream</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>.</p> <p>There are no guarantees about the chronological order shards returned. To process shards in chronological order, use the ID of the parent shard to track the lineage to the oldest shard.</p> <p>This operation has a limit of 10 transactions per second per account.</p>

        Args:
            stream_name: <p>The name of the stream to describe.</p>
            limit: <p>The maximum number of shards to return in a single call. The default value is 100. If you specify a value greater than 100, at most 100 results are returned.</p>
            exclusive_start_shard_id: <p>The shard ID of the shard to start with.</p> <p>Specify this parameter to indicate that you want to describe the stream starting with the shard whose ID immediately follows <code>ExclusiveStartShardId</code>.</p> <p>If you don't specify this parameter, the default behavior for <code>DescribeStream</code> is to describe the stream starting with the first shard in the stream.</p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.describe_stream_input.DescribeStreamInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.describe_stream_output.DescribeStreamOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.describe_stream

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.describe_stream.describe_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.describe_stream_input.DescribeStreamInput = {}
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if limit is not None:
            input_["limit"] = limit
        if exclusive_start_shard_id is not None:
            input_["exclusive_start_shard_id"] = exclusive_start_shard_id
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def wait_until_stream_not_exists(
        self,
        *,
        max_wait_time: float,
        min_delay: float = 10,
        max_delay: float = 120,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        limit: Optional[
            "capo_kinesis.types.describe_stream_input_limit.DescribeStreamInputLimit"
        ] = None,
        exclusive_start_shard_id: Optional[
            "capo_kinesis.types.shard_id.ShardId"
        ] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> ServiceError:
        """Wait for stream_not_exists.

        Args:
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
            stream_name: <p>The name of the stream to describe.</p>
            limit: <p>The maximum number of shards to return in a single call. The default value is 100. If you specify a value greater than 100, at most 100 results are returned.</p>
            exclusive_start_shard_id: <p>The shard ID of the shard to start with.</p> <p>Specify this parameter to indicate that you want to describe the stream starting with the shard whose ID immediately follows <code>ExclusiveStartShardId</code>.</p> <p>If you don't specify this parameter, the default behavior for <code>DescribeStream</code> is to describe the stream starting with the first shard in the stream.</p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "capo_kinesis.types.describe_stream_output.DescribeStreamOutput | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = self.describe_stream(  # noqa: F841
                    config_overrides=config_overrides,
                    stream_name=stream_name,
                    limit=limit,
                    exclusive_start_shard_id=exclusive_start_shard_id,
                    stream_arn=stream_arn,
                    stream_id=stream_id,
                )
            except ServiceError as e:
                op_error = e
            if op_error is not None and op_error.code == "ResourceNotFoundException":
                return op_error
            elif op_error is not None:
                raise op_error

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("stream_not_exists", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = random.uniform(min_delay, delay)
            delay = min(delay, remaining)
            time.sleep(delay)
            attempt += 1

    def describe_stream_consumer(
        self,
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        consumer_name: Optional["capo_kinesis.types.consumer_name.ConsumerName"] = None,
        consumer_arn: Optional["capo_kinesis.types.consumer_arn.ConsumerARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> "capo_kinesis.types.describe_stream_consumer_output.DescribeStreamConsumerOutput":
        """<p>To get the description of a registered consumer, provide the ARN of the consumer. Alternatively, you can provide the ARN of the data stream and the name you gave the consumer when you registered it. You may also provide all three parameters, as long as they don't conflict with each other. If you don't know the name or ARN of the consumer that you want to describe, you can use the <a>ListStreamConsumers</a> operation to get a list of the descriptions of all the consumers that are currently registered with a given data stream.</p> <p>This operation has a limit of 20 transactions per second per stream.</p> <note> <p>When making a cross-account call with <code>DescribeStreamConsumer</code>, make sure to provide the ARN of the consumer. </p> </note>

        Args:
            stream_arn: <p>The ARN of the Kinesis data stream that the consumer is registered with. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>
            consumer_name: <p>The name that you gave to the consumer.</p>
            consumer_arn: <p>The ARN returned by Kinesis Data Streams when you registered the consumer.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.describe_stream_consumer_input.DescribeStreamConsumerInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.describe_stream_consumer_output.DescribeStreamConsumerOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.describe_stream_consumer

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.describe_stream_consumer.describe_stream_consumer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.describe_stream_consumer_input.DescribeStreamConsumerInput = {}
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if consumer_name is not None:
            input_["consumer_name"] = consumer_name
        if consumer_arn is not None:
            input_["consumer_arn"] = consumer_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_stream_summary(
        self,
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> (
        "capo_kinesis.types.describe_stream_summary_output.DescribeStreamSummaryOutput"
    ):
        """<p>Provides a summarized description of the specified Kinesis data stream without the shard list.</p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note> <p>The information returned includes the stream name, Amazon Resource Name (ARN), status, record retention period, approximate creation time, monitoring, encryption details, and open shard count. </p> <p> <a>DescribeStreamSummary</a> has a limit of 20 transactions per second per account.</p>

        Args:
            stream_name: <p>The name of the stream to describe.</p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.describe_stream_summary_input.DescribeStreamSummaryInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.describe_stream_summary_output.DescribeStreamSummaryOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.describe_stream_summary

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.describe_stream_summary.describe_stream_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.describe_stream_summary_input.DescribeStreamSummaryInput = {}
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disable_enhanced_monitoring(
        self,
        shard_level_metrics: "capo_kinesis.types.metrics_name_list.MetricsNameList",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> "capo_kinesis.types.enhanced_monitoring_output.EnhancedMonitoringOutput":
        """<p>Disables enhanced monitoring.</p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note>

        Args:
            stream_name: <p>The name of the Kinesis data stream for which to disable enhanced monitoring.</p>
            shard_level_metrics: <p>List of shard-level metrics to disable.</p> <p>The following are the valid shard-level metrics. The value "<code>ALL</code>" disables every metric.</p> <ul> <li> <p> <code>IncomingBytes</code> </p> </li> <li> <p> <code>IncomingRecords</code> </p> </li> <li> <p> <code>OutgoingBytes</code> </p> </li> <li> <p> <code>OutgoingRecords</code> </p> </li> <li> <p> <code>WriteProvisionedThroughputExceeded</code> </p> </li> <li> <p> <code>ReadProvisionedThroughputExceeded</code> </p> </li> <li> <p> <code>IteratorAgeMilliseconds</code> </p> </li> <li> <p> <code>ALL</code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html">Monitoring the Amazon Kinesis Data Streams Service with Amazon CloudWatch</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>.</p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.disable_enhanced_monitoring_input.DisableEnhancedMonitoringInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.enhanced_monitoring_output.EnhancedMonitoringOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.disable_enhanced_monitoring

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.disable_enhanced_monitoring.disable_enhanced_monitoring(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.disable_enhanced_monitoring_input.DisableEnhancedMonitoringInput = {
            "shard_level_metrics": shard_level_metrics
        }
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def enable_enhanced_monitoring(
        self,
        shard_level_metrics: "capo_kinesis.types.metrics_name_list.MetricsNameList",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> "capo_kinesis.types.enhanced_monitoring_output.EnhancedMonitoringOutput":
        """<p>Enables enhanced Kinesis data stream monitoring for shard-level metrics.</p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note>

        Args:
            stream_name: <p>The name of the stream for which to enable enhanced monitoring.</p>
            shard_level_metrics: <p>List of shard-level metrics to enable.</p> <p>The following are the valid shard-level metrics. The value "<code>ALL</code>" enables every metric.</p> <ul> <li> <p> <code>IncomingBytes</code> </p> </li> <li> <p> <code>IncomingRecords</code> </p> </li> <li> <p> <code>OutgoingBytes</code> </p> </li> <li> <p> <code>OutgoingRecords</code> </p> </li> <li> <p> <code>WriteProvisionedThroughputExceeded</code> </p> </li> <li> <p> <code>ReadProvisionedThroughputExceeded</code> </p> </li> <li> <p> <code>IteratorAgeMilliseconds</code> </p> </li> <li> <p> <code>ALL</code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html">Monitoring the Amazon Kinesis Data Streams Service with Amazon CloudWatch</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>.</p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.enable_enhanced_monitoring_input.EnableEnhancedMonitoringInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.enhanced_monitoring_output.EnhancedMonitoringOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.enable_enhanced_monitoring

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.enable_enhanced_monitoring.enable_enhanced_monitoring(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.enable_enhanced_monitoring_input.EnableEnhancedMonitoringInput = {
            "shard_level_metrics": shard_level_metrics
        }
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_records(
        self,
        shard_iterator: "capo_kinesis.types.shard_iterator.ShardIterator",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        limit: Optional[
            "capo_kinesis.types.get_records_input_limit.GetRecordsInputLimit"
        ] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
        dry_run: Optional["capo_kinesis.types.boolean_object.BooleanObject"] = None,
    ) -> "capo_kinesis.types.get_records_output.GetRecordsOutput":
        """<p>Gets data records from a Kinesis data stream's shard.</p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note> <p>Specify a shard iterator using the <code>ShardIterator</code> parameter. The shard iterator specifies the position in the shard from which you want to start reading data records sequentially. If there are no records available in the portion of the shard that the iterator points to, <a>GetRecords</a> returns an empty list. It might take multiple calls to get to a portion of the shard that contains records.</p> <p>You can scale by provisioning multiple shards per stream while considering service limits (for more information, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html">Amazon Kinesis Data Streams Limits</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>). Your application should have one thread per shard, each reading continuously from its stream. To read from a stream continually, call <a>GetRecords</a> in a loop. Use <a>GetShardIterator</a> to get the shard iterator to specify in the first <a>GetRecords</a> call. <a>GetRecords</a> returns a new shard iterator in <code>NextShardIterator</code>. Specify the shard iterator returned in <code>NextShardIterator</code> in subsequent calls to <a>GetRecords</a>. If the shard has been closed, the shard iterator can't return more data and <a>GetRecords</a> returns <code>null</code> in <code>NextShardIterator</code>. You can terminate the loop when the shard is closed, or when the shard iterator reaches the record with the sequence number or other attribute that marks it as the last record to process.</p> <p>Each data record can be up to 1 MiB in size by default. Amazon Kinesis Data Streams supports large records up to 10 MiB in size, but the average throughput for your stream cannot exceed 1 MiB per second. For more information about how large records are handled, see <a href="https://docs.aws.amazon.com/streams/latest/dev/large-records.html">Large records</a>. Each shard can read up to 2 MiB per second. You can ensure that your calls don't exceed the maximum supported size or throughput by using the <code>Limit</code> parameter to specify the maximum number of records that <a>GetRecords</a> can return. Consider your average record size when determining this limit. The maximum number of records that can be returned per call is 10,000.</p> <p>The size of the data returned by <a>GetRecords</a> varies depending on the utilization of the shard. It is recommended that consumer applications retrieve records via the <code>GetRecords</code> command using the 5 TPS limit to remain caught up. Retrieving records less frequently can lead to consumer applications falling behind. The maximum size of data that <a>GetRecords</a> can return is 10 MiB. If a call returns this amount of data, subsequent calls made within the next 5 seconds throw <code>ProvisionedThroughputExceededException</code>. If there is insufficient provisioned throughput on the stream, subsequent calls made within the next 1 second throw <code>ProvisionedThroughputExceededException</code>. <a>GetRecords</a> doesn't return any data when it throws an exception. For this reason, we recommend that you wait 1 second between calls to <a>GetRecords</a>. However, it's possible that the application will get exceptions for longer than 1 second.</p> <p>To detect whether the application is falling behind in processing, you can use the <code>MillisBehindLatest</code> response attribute. You can also monitor the stream using CloudWatch metrics and other mechanisms (see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/monitoring.html">Monitoring</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>).</p> <p>Each Amazon Kinesis record includes a value, <code>ApproximateArrivalTimestamp</code>, that is set when a stream successfully receives and stores a record. This is commonly referred to as a server-side time stamp, whereas a client-side time stamp is set when a data producer creates or sends the record to a stream (a data producer is any data source putting data records into a stream, for example with <a>PutRecords</a>). The time stamp has millisecond precision. There are no guarantees about the time stamp accuracy, or that the time stamp is always increasing. For example, records in a shard or across a stream might have time stamps that are out of order.</p> <p>This operation has a limit of five transactions per second per shard.</p>

        Args:
            shard_iterator: <p>The position in the shard from which you want to start sequentially reading data records. A shard iterator specifies this position using the sequence number of a data record in the shard.</p>
            limit: <p>The maximum number of records to return. Specify a value of up to 10,000. If you specify a value that is greater than 10,000, <a>GetRecords</a> throws <code>InvalidArgumentException</code>. The default value is 10,000.</p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>
            dry_run: <p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was rejected because the DryRun parameter was specified.</p>
            capo_kinesis.errors.expired_iterator_exception.ExpiredIteratorException: <p>The provided iterator exceeds the maximum age allowed.</p>
            capo_kinesis.errors.internal_failure_exception.InternalFailureException: <p>The processing of the request failed because of an unknown error, exception, or failure.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>The ciphertext references a key that doesn't exist or that you don't have access to.</p>
            capo_kinesis.errors.kms_disabled_exception.KMSDisabledException: <p>The request was rejected because the specified customer master key (CMK) isn't enabled.</p>
            capo_kinesis.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>The request was rejected because the state of the specified resource isn't valid for this request. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html">How Key State Affects Use of a Customer Master Key</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p>
            capo_kinesis.errors.kms_not_found_exception.KMSNotFoundException: <p>The request was rejected because the specified entity or resource can't be found.</p>
            capo_kinesis.errors.kms_opt_in_required.KMSOptInRequired: <p>The Amazon Web Services access key ID needs a subscription for the service.</p>
            capo_kinesis.errors.kms_throttling_exception.KMSThrottlingException: <p>The request was denied due to request throttling. For more information about throttling, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/limits.html#requests-per-second">Limits</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p>
            capo_kinesis.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The request rate for the stream is too high, or the requested data is too large for the available throughput. Reduce the frequency or size of your requests. For more information, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html">Streams Limits</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>, and <a href="https://docs.aws.amazon.com/general/latest/gr/api-retries.html">Error Retries and Exponential Backoff in Amazon Web Services</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.get_records_input.GetRecordsInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.get_records_output.GetRecordsOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.get_records

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.get_records.get_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.get_records_input.GetRecordsInput = {
            "shard_iterator": shard_iterator
        }
        if limit is not None:
            input_["limit"] = limit
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_policy(
        self,
        resource_arn: "capo_kinesis.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> "capo_kinesis.types.get_resource_policy_output.GetResourcePolicyOutput":
        r"""<p>Returns a policy attached to the specified data stream or consumer. Request patterns can be one of the following:</p> <ul> <li> <p>Data stream pattern: <code>arn:aws.*:kinesis:.*:\d{12}:.*stream/\S+</code> </p> </li> <li> <p> Consumer pattern: <code>^(arn):aws.*:kinesis:.*:\d{12}:.*stream\/[a-zA-Z0-9_.-]+\/consumer\/[a-zA-Z0-9_.-]+:[0-9]+</code> </p> </li> </ul>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the data stream or consumer.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.get_resource_policy_input.GetResourcePolicyInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.get_resource_policy_output.GetResourcePolicyOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.get_resource_policy

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.get_resource_policy_input.GetResourcePolicyInput = {
            "resource_arn": resource_arn
        }
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_shard_iterator(
        self,
        shard_id: "capo_kinesis.types.shard_id.ShardId",
        shard_iterator_type: "capo_kinesis.types.shard_iterator_type.ShardIteratorType",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        starting_sequence_number: Optional[
            "capo_kinesis.types.sequence_number.SequenceNumber"
        ] = None,
        timestamp: Optional["capo_kinesis.types.timestamp.Timestamp"] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
        dry_run: Optional["capo_kinesis.types.boolean_object.BooleanObject"] = None,
    ) -> "capo_kinesis.types.get_shard_iterator_output.GetShardIteratorOutput":
        """<p>Gets an Amazon Kinesis shard iterator. A shard iterator expires 5 minutes after it is returned to the requester.</p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note> <p>A shard iterator specifies the shard position from which to start reading data records sequentially. The position is specified using the sequence number of a data record in a shard. A sequence number is the identifier associated with every record ingested in the stream, and is assigned when a record is put into the stream. Each stream has one or more shards.</p> <p>You must specify the shard iterator type. For example, you can set the <code>ShardIteratorType</code> parameter to read exactly from the position denoted by a specific sequence number by using the <code>AT_SEQUENCE_NUMBER</code> shard iterator type. Alternatively, the parameter can read right after the sequence number by using the <code>AFTER_SEQUENCE_NUMBER</code> shard iterator type, using sequence numbers returned by earlier calls to <a>PutRecord</a>, <a>PutRecords</a>, <a>GetRecords</a>, or <a>DescribeStream</a>. In the request, you can specify the shard iterator type <code>AT_TIMESTAMP</code> to read records from an arbitrary point in time, <code>TRIM_HORIZON</code> to cause <code>ShardIterator</code> to point to the last untrimmed record in the shard in the system (the oldest data record in the shard), or <code>LATEST</code> so that you always read the most recent data in the shard. </p> <p>When you read repeatedly from a stream, use a <a>GetShardIterator</a> request to get the first shard iterator for use in your first <a>GetRecords</a> request and for subsequent reads use the shard iterator returned by the <a>GetRecords</a> request in <code>NextShardIterator</code>. A new shard iterator is returned by every <a>GetRecords</a> request in <code>NextShardIterator</code>, which you use in the <code>ShardIterator</code> parameter of the next <a>GetRecords</a> request. </p> <p>If a <a>GetShardIterator</a> request is made too often, you receive a <code>ProvisionedThroughputExceededException</code>. For more information about throughput limits, see <a>GetRecords</a>, and <a href="https://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html">Streams Limits</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>.</p> <p>If the shard is closed, <a>GetShardIterator</a> returns a valid iterator for the last sequence number of the shard. A shard can be closed as a result of using <a>SplitShard</a> or <a>MergeShards</a>.</p> <p> <a>GetShardIterator</a> has a limit of five transactions per second per account per open shard.</p>

        Args:
            stream_name: <p>The name of the Amazon Kinesis data stream.</p>
            shard_id: <p>The shard ID of the Kinesis Data Streams shard to get the iterator for.</p>
            shard_iterator_type: <p>Determines how the shard iterator is used to start reading data records from the shard.</p> <p>The following are the valid Amazon Kinesis shard iterator types:</p> <ul> <li> <p>AT_SEQUENCE_NUMBER - Start reading from the position denoted by a specific sequence number, provided in the value <code>StartingSequenceNumber</code>.</p> </li> <li> <p>AFTER_SEQUENCE_NUMBER - Start reading right after the position denoted by a specific sequence number, provided in the value <code>StartingSequenceNumber</code>.</p> </li> <li> <p>AT_TIMESTAMP - Start reading from the position denoted by a specific time stamp, provided in the value <code>Timestamp</code>.</p> </li> <li> <p>TRIM_HORIZON - Start reading at the last untrimmed record in the shard in the system, which is the oldest data record in the shard.</p> </li> <li> <p>LATEST - Start reading just after the most recent record in the shard, so that you always read the most recent data in the shard.</p> </li> </ul>
            starting_sequence_number: <p>The sequence number of the data record in the shard from which to start reading. Used with shard iterator type AT_SEQUENCE_NUMBER and AFTER_SEQUENCE_NUMBER.</p>
            timestamp: <p>The time stamp of the data record from which to start reading. Used with shard iterator type AT_TIMESTAMP. A time stamp is the Unix epoch date with precision in milliseconds. For example, <code>2016-04-04T19:58:46.480-00:00</code> or <code>1459799926.480</code>. If a record with this exact time stamp does not exist, the iterator returned is for the next (later) record. If the time stamp is older than the current trim horizon, the iterator returned is for the oldest untrimmed data record (TRIM_HORIZON).</p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>
            dry_run: <p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was rejected because the DryRun parameter was specified.</p>
            capo_kinesis.errors.internal_failure_exception.InternalFailureException: <p>The processing of the request failed because of an unknown error, exception, or failure.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The request rate for the stream is too high, or the requested data is too large for the available throughput. Reduce the frequency or size of your requests. For more information, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html">Streams Limits</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>, and <a href="https://docs.aws.amazon.com/general/latest/gr/api-retries.html">Error Retries and Exponential Backoff in Amazon Web Services</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.get_shard_iterator_input.GetShardIteratorInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.get_shard_iterator_output.GetShardIteratorOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.get_shard_iterator

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.get_shard_iterator.get_shard_iterator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.get_shard_iterator_input.GetShardIteratorInput = {
            "shard_id": shard_id,
            "shard_iterator_type": shard_iterator_type,
        }
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if starting_sequence_number is not None:
            input_["starting_sequence_number"] = starting_sequence_number
        if timestamp is not None:
            input_["timestamp"] = timestamp
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def increase_stream_retention_period(
        self,
        retention_period_hours: "capo_kinesis.types.retention_period_hours.RetentionPeriodHours",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> None:
        """<p>Increases the Kinesis data stream's retention period, which is the length of time data records are accessible after they are added to the stream. The maximum value of a stream's retention period is 8760 hours (365 days).</p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note> <p>If you choose a longer stream retention period, this operation increases the time period during which records that have not yet expired are accessible. However, it does not make previous, expired data (older than the stream's previous retention period) accessible after the operation has been called. For example, if a stream's retention period is set to 24 hours and is increased to 168 hours, any data that is older than 24 hours remains inaccessible to consumer applications.</p>

        Args:
            stream_name: <p>The name of the stream to modify.</p>
            retention_period_hours: <p>The new retention period of the stream, in hours. Must be more than the current retention period.</p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.increase_stream_retention_period_input.IncreaseStreamRetentionPeriodInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.increase_stream_retention_period

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.increase_stream_retention_period.increase_stream_retention_period(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.increase_stream_retention_period_input.IncreaseStreamRetentionPeriodInput = {
            "retention_period_hours": retention_period_hours
        }
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_channels(
        self,
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_filter: Optional[
            "capo_kinesis.types.stream_filter_list.StreamFilterList"
        ] = None,
        max_results: Optional[
            "capo_kinesis.types.list_channels_input_limit.ListChannelsInputLimit"
        ] = None,
        next_token: Optional["capo_kinesis.types.next_token.NextToken"] = None,
    ) -> "capo_kinesis.types.list_channels_output.ListChannelsOutput":
        """<p>Lists the channels in your account. You can filter the results by source stream. The results are paginated. Use the <code>NextToken</code> value returned in the response to retrieve additional results.</p> <p>Use this operation to find channels before deleting a stream, or to audit the channels configured in an Amazon Web Services Region.</p> <p>This operation has a call limit of 5 transactions per second (TPS) for each Amazon Web Services account. Exceeding 5 TPS results in a <code>LimitExceededException</code>.</p>

        Args:
            stream_filter: <p>Filters the results to channels associated with the specified streams.</p>
            max_results: <p>The maximum number of channels to return in a single call. The default value is 100. If you specify a value greater than 100, at most 100 results are returned.</p>
            next_token: <p>The pagination token returned by a previous call. Specify this token to retrieve the next page of results.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.expired_next_token_exception.ExpiredNextTokenException: <p>The pagination token passed to the operation is expired.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.validation_exception.ValidationException: <p>Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode. </p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list channels

            >>> client.list_channels()
            To list channels filtered by stream

            >>> client.list_channels(stream_filter=[{'StreamARN': 'arn:aws:kinesis:us-east-1:123456789012:stream/my-stream-name'}], max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.list_channels_input.ListChannelsInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.list_channels_output.ListChannelsOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.list_channels

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.list_channels.list_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.list_channels_input.ListChannelsInput = {}
        if stream_filter is not None:
            input_["stream_filter"] = stream_filter
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_channels(
        self,
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_filter: Optional[
            "capo_kinesis.types.stream_filter_list.StreamFilterList"
        ] = None,
        max_results: Optional[
            "capo_kinesis.types.list_channels_input_limit.ListChannelsInputLimit"
        ] = None,
        next_token: Optional["capo_kinesis.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_kinesis.types.channel_summary.ChannelSummary]":
        _token = next_token
        while True:
            _response = self.list_channels(
                config_overrides=config_overrides,
                stream_filter=stream_filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("channel_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_shards(
        self,
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        next_token: Optional["capo_kinesis.types.next_token.NextToken"] = None,
        exclusive_start_shard_id: Optional[
            "capo_kinesis.types.shard_id.ShardId"
        ] = None,
        max_results: Optional[
            "capo_kinesis.types.list_shards_input_limit.ListShardsInputLimit"
        ] = None,
        stream_creation_timestamp: Optional[
            "capo_kinesis.types.timestamp.Timestamp"
        ] = None,
        shard_filter: Optional["capo_kinesis.types.shard_filter.ShardFilter"] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> "capo_kinesis.types.list_shards_output.ListShardsOutput":
        """<p>Lists the shards in a stream and provides information about each shard. This operation has a limit of 1000 transactions per second per data stream.</p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note> <p>This action does not list expired shards. For information about expired shards, see <a href="https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-after-resharding.html#kinesis-using-sdk-java-resharding-data-routing">Data Routing, Data Persistence, and Shard State after a Reshard</a>. </p> <important> <p>This API is a new operation that is used by the Amazon Kinesis Client Library (KCL). If you have a fine-grained IAM policy that only allows specific operations, you must update your policy to allow calls to this API. For more information, see <a href="https://docs.aws.amazon.com/streams/latest/dev/controlling-access.html">Controlling Access to Amazon Kinesis Data Streams Resources Using IAM</a>.</p> </important>

        Args:
            stream_name: <p>The name of the data stream whose shards you want to list. </p> <p>You cannot specify this parameter if you specify the <code>NextToken</code> parameter.</p>
            next_token: <p>When the number of shards in the data stream is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of shards in the data stream, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListShards</code> to list the next set of shards.</p> <p>Don't specify <code>StreamName</code> or <code>StreamCreationTimestamp</code> if you specify <code>NextToken</code> because the latter unambiguously identifies the stream.</p> <p>You can optionally specify a value for the <code>MaxResults</code> parameter when you specify <code>NextToken</code>. If you specify a <code>MaxResults</code> value that is less than the number of shards that the operation returns if you don't specify <code>MaxResults</code>, the response will contain a new <code>NextToken</code> value. You can use the new <code>NextToken</code> value in a subsequent call to the <code>ListShards</code> operation.</p> <important> <p>Tokens expire after 300 seconds. When you obtain a value for <code>NextToken</code> in the response to a call to <code>ListShards</code>, you have 300 seconds to use that value. If you specify an expired token in a call to <code>ListShards</code>, you get <code>ExpiredNextTokenException</code>.</p> </important>
            exclusive_start_shard_id: <p>Specify this parameter to indicate that you want to list the shards starting with the shard whose ID immediately follows <code>ExclusiveStartShardId</code>.</p> <p>If you don't specify this parameter, the default behavior is for <code>ListShards</code> to list the shards starting with the first one in the stream.</p> <p>You cannot specify this parameter if you specify <code>NextToken</code>.</p>
            max_results: <p>The maximum number of shards to return in a single call to <code>ListShards</code>. The maximum number of shards to return in a single call. The default value is 1000. If you specify a value greater than 1000, at most 1000 results are returned. </p> <p>When the number of shards to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListShards</code> to list the next set of shards.</p>
            stream_creation_timestamp: <p>Specify this input parameter to distinguish data streams that have the same name. For example, if you create a data stream and then delete it, and you later create another data stream with the same name, you can use this input parameter to specify which of the two streams you want to list the shards for.</p> <p>You cannot specify this parameter if you specify the <code>NextToken</code> parameter.</p>
            shard_filter: <p>Enables you to filter out the response of the <code>ListShards</code> API. You can only specify one filter at a time. </p> <p>If you use the <code>ShardFilter</code> parameter when invoking the ListShards API, the <code>Type</code> is the required property and must be specified. If you specify the <code>AT_TRIM_HORIZON</code>, <code>FROM_TRIM_HORIZON</code>, or <code>AT_LATEST</code> types, you do not need to specify either the <code>ShardId</code> or the <code>Timestamp</code> optional properties. </p> <p>If you specify the <code>AFTER_SHARD_ID</code> type, you must also provide the value for the optional <code>ShardId</code> property. The <code>ShardId</code> property is identical in fuctionality to the <code>ExclusiveStartShardId</code> parameter of the <code>ListShards</code> API. When <code>ShardId</code> property is specified, the response includes the shards starting with the shard whose ID immediately follows the <code>ShardId</code> that you provided. </p> <p>If you specify the <code>AT_TIMESTAMP</code> or <code>FROM_TIMESTAMP_ID</code> type, you must also provide the value for the optional <code>Timestamp</code> property. If you specify the AT_TIMESTAMP type, then all shards that were open at the provided timestamp are returned. If you specify the FROM_TIMESTAMP type, then all shards starting from the provided timestamp to TIP are returned. </p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.expired_next_token_exception.ExpiredNextTokenException: <p>The pagination token passed to the operation is expired.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.list_shards_input.ListShardsInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.list_shards_output.ListShardsOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.list_shards

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.list_shards.list_shards(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.list_shards_input.ListShardsInput = {}
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if next_token is not None:
            input_["next_token"] = next_token
        if exclusive_start_shard_id is not None:
            input_["exclusive_start_shard_id"] = exclusive_start_shard_id
        if max_results is not None:
            input_["max_results"] = max_results
        if stream_creation_timestamp is not None:
            input_["stream_creation_timestamp"] = stream_creation_timestamp
        if shard_filter is not None:
            input_["shard_filter"] = shard_filter
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_stream_consumers(
        self,
        stream_arn: "capo_kinesis.types.stream_arn.StreamARN",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        next_token: Optional["capo_kinesis.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kinesis.types.list_stream_consumers_input_limit.ListStreamConsumersInputLimit"
        ] = None,
        stream_creation_timestamp: Optional[
            "capo_kinesis.types.timestamp.Timestamp"
        ] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> "capo_kinesis.types.list_stream_consumers_output.ListStreamConsumersOutput":
        """<p>Lists the consumers registered to receive data from a stream using enhanced fan-out, and provides information about each consumer.</p> <p>This operation has a limit of 5 transactions per second per stream.</p>

        Args:
            stream_arn: <p>The ARN of the Kinesis data stream for which you want to list the registered consumers. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>
            next_token: <p>When the number of consumers that are registered with the data stream is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of consumers that are registered with the data stream, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListStreamConsumers</code> to list the next set of registered consumers.</p> <p>Don't specify <code>StreamName</code> or <code>StreamCreationTimestamp</code> if you specify <code>NextToken</code> because the latter unambiguously identifies the stream.</p> <p>You can optionally specify a value for the <code>MaxResults</code> parameter when you specify <code>NextToken</code>. If you specify a <code>MaxResults</code> value that is less than the number of consumers that the operation returns if you don't specify <code>MaxResults</code>, the response will contain a new <code>NextToken</code> value. You can use the new <code>NextToken</code> value in a subsequent call to the <code>ListStreamConsumers</code> operation to list the next set of consumers.</p> <important> <p>Tokens expire after 300 seconds. When you obtain a value for <code>NextToken</code> in the response to a call to <code>ListStreamConsumers</code>, you have 300 seconds to use that value. If you specify an expired token in a call to <code>ListStreamConsumers</code>, you get <code>ExpiredNextTokenException</code>.</p> </important>
            max_results: <p>The maximum number of consumers that you want a single call of <code>ListStreamConsumers</code> to return. The default value is 100. If you specify a value greater than 100, at most 100 results are returned. </p>
            stream_creation_timestamp: <p>Specify this input parameter to distinguish data streams that have the same name. For example, if you create a data stream and then delete it, and you later create another data stream with the same name, you can use this input parameter to specify which of the two streams you want to list the consumers for. </p> <p>You can't specify this parameter if you specify the NextToken parameter. </p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.expired_next_token_exception.ExpiredNextTokenException: <p>The pagination token passed to the operation is expired.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.list_stream_consumers_input.ListStreamConsumersInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.list_stream_consumers_output.ListStreamConsumersOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.list_stream_consumers

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.list_stream_consumers.list_stream_consumers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.list_stream_consumers_input.ListStreamConsumersInput = {
            "stream_arn": stream_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if stream_creation_timestamp is not None:
            input_["stream_creation_timestamp"] = stream_creation_timestamp
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_stream_consumers(
        self,
        stream_arn: "capo_kinesis.types.stream_arn.StreamARN",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        next_token: Optional["capo_kinesis.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kinesis.types.list_stream_consumers_input_limit.ListStreamConsumersInputLimit"
        ] = None,
        stream_creation_timestamp: Optional[
            "capo_kinesis.types.timestamp.Timestamp"
        ] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> "Iterator[capo_kinesis.types.list_stream_consumers_output.ListStreamConsumersOutput]":
        _token = next_token
        while True:
            _response = self.list_stream_consumers(
                stream_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                stream_creation_timestamp=stream_creation_timestamp,
                stream_id=stream_id,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_streams(
        self,
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        limit: Optional[
            "capo_kinesis.types.list_streams_input_limit.ListStreamsInputLimit"
        ] = None,
        exclusive_start_stream_name: Optional[
            "capo_kinesis.types.stream_name.StreamName"
        ] = None,
        next_token: Optional["capo_kinesis.types.next_token.NextToken"] = None,
    ) -> "capo_kinesis.types.list_streams_output.ListStreamsOutput":
        """<p>Lists your Kinesis data streams.</p> <p>The number of streams may be too large to return from a single call to <code>ListStreams</code>. You can limit the number of returned streams using the <code>Limit</code> parameter. If you do not specify a value for the <code>Limit</code> parameter, Kinesis Data Streams uses the default limit, which is currently 100.</p> <p>You can detect if there are more streams available to list by using the <code>HasMoreStreams</code> flag from the returned output. If there are more streams available, you can request more streams by using the name of the last stream returned by the <code>ListStreams</code> request in the <code>ExclusiveStartStreamName</code> parameter in a subsequent request to <code>ListStreams</code>. The group of stream names returned by the subsequent request is then added to the list. You can continue this process until all the stream names have been collected in the list. </p> <p> <a>ListStreams</a> has a limit of five transactions per second per account.</p>

        Args:
            limit: <p>The maximum number of streams to list. The default value is 100. If you specify a value greater than 100, at most 100 results are returned.</p>
            exclusive_start_stream_name: <p>The name of the stream to start the list with.</p>
            next_token: <p></p>

        Raises:
            capo_kinesis.errors.expired_next_token_exception.ExpiredNextTokenException: <p>The pagination token passed to the operation is expired.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.list_streams_input.ListStreamsInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.list_streams_output.ListStreamsOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.list_streams

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.list_streams.list_streams(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.list_streams_input.ListStreamsInput = {}
        if limit is not None:
            input_["limit"] = limit
        if exclusive_start_stream_name is not None:
            input_["exclusive_start_stream_name"] = exclusive_start_stream_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_streams(
        self,
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        limit: Optional[
            "capo_kinesis.types.list_streams_input_limit.ListStreamsInputLimit"
        ] = None,
        exclusive_start_stream_name: Optional[
            "capo_kinesis.types.stream_name.StreamName"
        ] = None,
        next_token: Optional["capo_kinesis.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_kinesis.types.list_streams_output.ListStreamsOutput]":
        _token = next_token
        while True:
            _response = self.list_streams(
                config_overrides=config_overrides,
                limit=limit,
                exclusive_start_stream_name=exclusive_start_stream_name,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_kinesis.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> "capo_kinesis.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>List all tags added to the specified Kinesis resource. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources.</p> <p>For more information about tagging Kinesis resources, see <a href="https://docs.aws.amazon.com/streams/latest/dev/tagging.html">Tag your Amazon Kinesis Data Streams resources</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Kinesis resource for which to list tags.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.list_tags_for_resource

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_stream(
        self,
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        exclusive_start_tag_key: Optional["capo_kinesis.types.tag_key.TagKey"] = None,
        limit: Optional[
            "capo_kinesis.types.list_tags_for_stream_input_limit.ListTagsForStreamInputLimit"
        ] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> "capo_kinesis.types.list_tags_for_stream_output.ListTagsForStreamOutput":
        """<p>Lists the tags for the specified Kinesis data stream. This operation has a limit of five transactions per second per account.</p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note>

        Args:
            stream_name: <p>The name of the stream.</p>
            exclusive_start_tag_key: <p>The key to use as the starting point for the list of tags. If this parameter is set, <code>ListTagsForStream</code> gets all tags that occur after <code>ExclusiveStartTagKey</code>. </p>
            limit: <p>The number of tags to return. If this number is less than the total number of tags associated with the stream, <code>HasMoreTags</code> is set to <code>true</code>. To list additional tags, set <code>ExclusiveStartTagKey</code> to the last key in the response.</p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.list_tags_for_stream_input.ListTagsForStreamInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.list_tags_for_stream_output.ListTagsForStreamOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.list_tags_for_stream

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.list_tags_for_stream.list_tags_for_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.list_tags_for_stream_input.ListTagsForStreamInput = {}
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if exclusive_start_tag_key is not None:
            input_["exclusive_start_tag_key"] = exclusive_start_tag_key
        if limit is not None:
            input_["limit"] = limit
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def merge_shards(
        self,
        shard_to_merge: "capo_kinesis.types.shard_id.ShardId",
        adjacent_shard_to_merge: "capo_kinesis.types.shard_id.ShardId",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> None:
        """<p>Merges two adjacent shards in a Kinesis data stream and combines them into a single shard to reduce the stream's capacity to ingest and transport data. This API is only supported for the data streams with the provisioned capacity mode. Two shards are considered adjacent if the union of the hash key ranges for the two shards form a contiguous set with no gaps. For example, if you have two shards, one with a hash key range of 276...381 and the other with a hash key range of 382...454, then you could merge these two shards into a single shard that would have a hash key range of 276...454. After the merge, the single child shard receives data for all hash key values covered by the two parent shards.</p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note> <p> <code>MergeShards</code> is called when there is a need to reduce the overall capacity of a stream because of excess capacity that is not being used. You must specify the shard to be merged and the adjacent shard for a stream. For more information about merging shards, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/kinesis-using-sdk-java-resharding-merge.html">Merge Two Shards</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>.</p> <p>If the stream is in the <code>ACTIVE</code> state, you can call <code>MergeShards</code>. If a stream is in the <code>CREATING</code>, <code>UPDATING</code>, or <code>DELETING</code> state, <code>MergeShards</code> returns a <code>ResourceInUseException</code>. If the specified stream does not exist, <code>MergeShards</code> returns a <code>ResourceNotFoundException</code>. </p> <p>You can use <a>DescribeStreamSummary</a> to check the state of the stream, which is returned in <code>StreamStatus</code>.</p> <p> <code>MergeShards</code> is an asynchronous operation. Upon receiving a <code>MergeShards</code> request, Amazon Kinesis Data Streams immediately returns a response and sets the <code>StreamStatus</code> to <code>UPDATING</code>. After the operation is completed, Kinesis Data Streams sets the <code>StreamStatus</code> to <code>ACTIVE</code>. Read and write operations continue to work while the stream is in the <code>UPDATING</code> state. </p> <p>You use <a>DescribeStreamSummary</a> and the <a>ListShards</a> APIs to determine the shard IDs that are specified in the <code>MergeShards</code> request. </p> <p>If you try to operate on too many streams in parallel using <a>CreateStream</a>, <a>DeleteStream</a>, <code>MergeShards</code>, or <a>SplitShard</a>, you receive a <code>LimitExceededException</code>. </p> <p> <code>MergeShards</code> has a limit of five transactions per second per account.</p>

        Args:
            stream_name: <p>The name of the stream for the merge.</p>
            shard_to_merge: <p>The shard ID of the shard to combine with the adjacent shard for the merge.</p>
            adjacent_shard_to_merge: <p>The shard ID of the adjacent shard for the merge.</p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.validation_exception.ValidationException: <p>Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode. </p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.merge_shards_input.MergeShardsInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.merge_shards

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.merge_shards.merge_shards(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.merge_shards_input.MergeShardsInput = {
            "shard_to_merge": shard_to_merge,
            "adjacent_shard_to_merge": adjacent_shard_to_merge,
        }
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_record(
        self,
        data: "capo_kinesis.types.data.Data",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        partition_key: Optional["capo_kinesis.types.partition_key.PartitionKey"] = None,
        explicit_hash_key: Optional["capo_kinesis.types.hash_key.HashKey"] = None,
        sequence_number_for_ordering: Optional[
            "capo_kinesis.types.sequence_number.SequenceNumber"
        ] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
        dry_run: Optional["capo_kinesis.types.boolean_object.BooleanObject"] = None,
    ) -> "capo_kinesis.types.put_record_output.PutRecordOutput":
        """<p>Writes a single data record into an Amazon Kinesis data stream. Call <code>PutRecord</code> to send data into the stream for real-time ingestion and subsequent processing, one record at a time. Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 10 MiB per second.</p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note> <p>You must specify the name of the stream that captures, stores, and transports the data; a partition key; and the data blob itself.</p> <p>The data blob can be any type of data; for example, a segment from a log file, geographic/location data, website clickstream data, and so on.</p> <p>The partition key is used by Kinesis Data Streams to distribute data across shards. Kinesis Data Streams segregates the data records that belong to a stream into multiple shards, using the partition key associated with each data record to determine the shard to which a given data record belongs.</p> <p>Partition keys are Unicode strings, with a maximum length limit of 256 characters for each key. An MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards using the hash key ranges of the shards. You can override hashing the partition key to determine the shard by explicitly specifying a hash value using the <code>ExplicitHashKey</code> parameter. For more information, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/developing-producers-with-sdk.html#kinesis-using-sdk-java-add-data-to-stream">Adding Data to a Stream</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>.</p> <p> <code>PutRecord</code> returns the shard ID of where the data record was placed and the sequence number that was assigned to the data record.</p> <p>Sequence numbers increase over time and are specific to a shard within a stream, not across all shards within a stream. To guarantee strictly increasing ordering, write serially to a shard and use the <code>SequenceNumberForOrdering</code> parameter. For more information, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/developing-producers-with-sdk.html#kinesis-using-sdk-java-add-data-to-stream">Adding Data to a Stream</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>.</p> <important> <p>After you write a record to a stream, you cannot modify that record or its order within the stream.</p> </important> <p>If a <code>PutRecord</code> request cannot be processed because of insufficient provisioned throughput on the shard involved in the request, <code>PutRecord</code> throws <code>ProvisionedThroughputExceededException</code>. </p> <p>By default, data records are accessible for 24 hours from the time that they are added to a stream. You can use <a>IncreaseStreamRetentionPeriod</a> or <a>DecreaseStreamRetentionPeriod</a> to modify this retention period.</p>

        Args:
            stream_name: <p>The name of the stream to put the data record into.</p>
            data: <p>The data blob to put into the record, which is base64-encoded when the blob is serialized. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (10 MiB).</p>
            partition_key: <p>Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis Data Streams uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.</p> <p>If the stream uses the <code>USER_PARTITION_KEY</code> record distribution strategy (the default), a partition key is required. If the stream uses the <code>AUTO</code> record distribution strategy, the partition key is optional and any value you provide is ignored, along with any <code>ExplicitHashKey</code> you provide. In that case, Amazon Kinesis Data Streams distributes the record across shards using service-managed algorithms. For more information, see <code>UpdateStreamRecordDistributionStrategy</code>.</p>
            explicit_hash_key: <p>The hash value used to explicitly determine the shard the data record is assigned to by overriding the partition key hash.</p>
            sequence_number_for_ordering: <p>Guarantees strictly increasing sequence numbers, for puts from the same client and to the same partition key. Usage: set the <code>SequenceNumberForOrdering</code> of record <i>n</i> to the sequence number of record <i>n-1</i> (as returned in the result when putting record <i>n-1</i>). If this parameter is not set, records are coarsely ordered based on arrival time.</p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>
            dry_run: <p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was rejected because the DryRun parameter was specified.</p>
            capo_kinesis.errors.internal_failure_exception.InternalFailureException: <p>The processing of the request failed because of an unknown error, exception, or failure.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>The ciphertext references a key that doesn't exist or that you don't have access to.</p>
            capo_kinesis.errors.kms_disabled_exception.KMSDisabledException: <p>The request was rejected because the specified customer master key (CMK) isn't enabled.</p>
            capo_kinesis.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>The request was rejected because the state of the specified resource isn't valid for this request. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html">How Key State Affects Use of a Customer Master Key</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p>
            capo_kinesis.errors.kms_not_found_exception.KMSNotFoundException: <p>The request was rejected because the specified entity or resource can't be found.</p>
            capo_kinesis.errors.kms_opt_in_required.KMSOptInRequired: <p>The Amazon Web Services access key ID needs a subscription for the service.</p>
            capo_kinesis.errors.kms_throttling_exception.KMSThrottlingException: <p>The request was denied due to request throttling. For more information about throttling, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/limits.html#requests-per-second">Limits</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p>
            capo_kinesis.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The request rate for the stream is too high, or the requested data is too large for the available throughput. Reduce the frequency or size of your requests. For more information, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html">Streams Limits</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>, and <a href="https://docs.aws.amazon.com/general/latest/gr/api-retries.html">Error Retries and Exponential Backoff in Amazon Web Services</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.put_record_input.PutRecordInput]",
        ) -> OperationResponse["capo_kinesis.types.put_record_output.PutRecordOutput"]:
            import capo_kinesis._operations.kinesis_20131202.put_record

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.put_record.put_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.put_record_input.PutRecordInput = {"data": data}
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if partition_key is not None:
            input_["partition_key"] = partition_key
        if explicit_hash_key is not None:
            input_["explicit_hash_key"] = explicit_hash_key
        if sequence_number_for_ordering is not None:
            input_["sequence_number_for_ordering"] = sequence_number_for_ordering
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_records(
        self,
        records: "capo_kinesis.types.put_records_request_entry_list.PutRecordsRequestEntryList",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
        dry_run: Optional["capo_kinesis.types.boolean_object.BooleanObject"] = None,
    ) -> "capo_kinesis.types.put_records_output.PutRecordsOutput":
        """<p>Writes multiple data records into a Kinesis data stream in a single call (also referred to as a <code>PutRecords</code> request). Use this operation to send data into the stream for data ingestion and processing. </p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note> <p>Each <code>PutRecords</code> request can support up to 500 records. Each record in the request can be as large as 10 MiB, up to a limit of 10 MiB for the entire request, including partition keys. Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 1 MB per second.</p> <p>You must specify the name of the stream that captures, stores, and transports the data; and an array of request <code>Records</code>, with each record in the array requiring a partition key and data blob. The record size limit applies to the total size of the partition key and data blob.</p> <p>The data blob can be any type of data; for example, a segment from a log file, geographic/location data, website clickstream data, and so on.</p> <p>The partition key is used by Kinesis Data Streams as input to a hash function that maps the partition key and associated data to a specific shard. An MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream. For more information, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/developing-producers-with-sdk.html#kinesis-using-sdk-java-add-data-to-stream">Adding Data to a Stream</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>.</p> <p>Each record in the <code>Records</code> array may include an optional parameter, <code>ExplicitHashKey</code>, which overrides the partition key to shard mapping. This parameter allows a data producer to determine explicitly the shard where the record is stored. For more information, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/developing-producers-with-sdk.html#kinesis-using-sdk-java-putrecords">Adding Multiple Records with PutRecords</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>.</p> <p>The <code>PutRecords</code> response includes an array of response <code>Records</code>. Each record in the response array directly correlates with a record in the request array using natural ordering, from the top to the bottom of the request and response. The response <code>Records</code> array always includes the same number of records as the request array.</p> <p>The response <code>Records</code> array includes both successfully and unsuccessfully processed records. Kinesis Data Streams attempts to process all records in each <code>PutRecords</code> request. A single record failure does not stop the processing of subsequent records. As a result, PutRecords doesn't guarantee the ordering of records. If you need to read records in the same order they are written to the stream, use <a>PutRecord</a> instead of <code>PutRecords</code>, and write to the same shard.</p> <p>A successfully processed record includes <code>ShardId</code> and <code>SequenceNumber</code> values. The <code>ShardId</code> parameter identifies the shard in the stream where the record is stored. The <code>SequenceNumber</code> parameter is an identifier assigned to the put record, unique to all records in the stream.</p> <p>An unsuccessfully processed record includes <code>ErrorCode</code> and <code>ErrorMessage</code> values. <code>ErrorCode</code> reflects the type of error and can be one of the following values: <code>ProvisionedThroughputExceededException</code> or <code>InternalFailure</code>. <code>ErrorMessage</code> provides more detailed information about the <code>ProvisionedThroughputExceededException</code> exception including the account ID, stream name, and shard ID of the record that was throttled. For more information about partially successful responses, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/kinesis-using-sdk-java-add-data-to-stream.html#kinesis-using-sdk-java-putrecords">Adding Multiple Records with PutRecords</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>.</p> <important> <p>After you write a record to a stream, you cannot modify that record or its order within the stream.</p> </important> <p>By default, data records are accessible for 24 hours from the time that they are added to a stream. You can use <a>IncreaseStreamRetentionPeriod</a> or <a>DecreaseStreamRetentionPeriod</a> to modify this retention period.</p>

        Args:
            records: <p>The records associated with the request.</p>
            stream_name: <p>The stream name associated with the request.</p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>
            dry_run: <p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was rejected because the DryRun parameter was specified.</p>
            capo_kinesis.errors.internal_failure_exception.InternalFailureException: <p>The processing of the request failed because of an unknown error, exception, or failure.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>The ciphertext references a key that doesn't exist or that you don't have access to.</p>
            capo_kinesis.errors.kms_disabled_exception.KMSDisabledException: <p>The request was rejected because the specified customer master key (CMK) isn't enabled.</p>
            capo_kinesis.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>The request was rejected because the state of the specified resource isn't valid for this request. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html">How Key State Affects Use of a Customer Master Key</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p>
            capo_kinesis.errors.kms_not_found_exception.KMSNotFoundException: <p>The request was rejected because the specified entity or resource can't be found.</p>
            capo_kinesis.errors.kms_opt_in_required.KMSOptInRequired: <p>The Amazon Web Services access key ID needs a subscription for the service.</p>
            capo_kinesis.errors.kms_throttling_exception.KMSThrottlingException: <p>The request was denied due to request throttling. For more information about throttling, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/limits.html#requests-per-second">Limits</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p>
            capo_kinesis.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The request rate for the stream is too high, or the requested data is too large for the available throughput. Reduce the frequency or size of your requests. For more information, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html">Streams Limits</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>, and <a href="https://docs.aws.amazon.com/general/latest/gr/api-retries.html">Error Retries and Exponential Backoff in Amazon Web Services</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.put_records_input.PutRecordsInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.put_records_output.PutRecordsOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.put_records

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.put_records.put_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.put_records_input.PutRecordsInput = {
            "records": records
        }
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_resource_policy(
        self,
        resource_arn: "capo_kinesis.types.resource_arn.ResourceARN",
        policy: "capo_kinesis.types.policy.Policy",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> None:
        r"""<p>Attaches a resource-based policy to a data stream or registered consumer. If you are using an identity other than the root user of the Amazon Web Services account that owns the resource, the calling identity must have the <code>PutResourcePolicy</code> permissions on the specified Kinesis Data Streams resource and belong to the owner's account in order to use this operation. If you don't have <code>PutResourcePolicy</code> permissions, Amazon Kinesis Data Streams returns a <code>403 Access Denied error</code>. If you receive a <code>ResourceNotFoundException</code>, check to see if you passed a valid stream or consumer resource. </p> <p> Request patterns can be one of the following:</p> <ul> <li> <p>Data stream pattern: <code>arn:aws.*:kinesis:.*:\d{12}:.*stream/\S+</code> </p> </li> <li> <p>Consumer pattern: <code>^(arn):aws.*:kinesis:.*:\d{12}:.*stream\/[a-zA-Z0-9_.-]+\/consumer\/[a-zA-Z0-9_.-]+:[0-9]+</code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/streams/latest/dev/controlling-access.html">Controlling Access to Amazon Kinesis Data Streams Resources Using IAM</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the data stream or consumer.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>
            policy: <p>Details of the resource policy. It must include the identity of the principal and the actions allowed on this resource. This is formatted as a JSON string.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.put_resource_policy_input.PutResourcePolicyInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.put_resource_policy

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.put_resource_policy_input.PutResourcePolicyInput = {
            "resource_arn": resource_arn,
            "policy": policy,
        }
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_stream_consumer(
        self,
        stream_arn: "capo_kinesis.types.stream_arn.StreamARN",
        consumer_name: "capo_kinesis.types.consumer_name.ConsumerName",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
        tags: Optional["capo_kinesis.types.tag_map.TagMap"] = None,
    ) -> "capo_kinesis.types.register_stream_consumer_output.RegisterStreamConsumerOutput":
        """<p>Registers a consumer with a Kinesis data stream. When you use this operation, the consumer you register can then call <a>SubscribeToShard</a> to receive data from the stream using enhanced fan-out, at a rate of up to 2 MiB per second for every shard you subscribe to. This rate is unaffected by the total number of consumers that read from the same stream.</p> <p>You can add tags to the registered consumer when making a <code>RegisterStreamConsumer</code> request by setting the <code>Tags</code> parameter. If you pass the <code>Tags</code> parameter, in addition to having the <code>kinesis:RegisterStreamConsumer</code> permission, you must also have the <code>kinesis:TagResource</code> permission for the consumer that will be registered. Tags will take effect from the <code>CREATING</code> status of the consumer.</p> <p>With On-demand Advantage streams, you can register up to 50 consumers per stream to use Enhanced Fan-out. With On-demand Standard and Provisioned streams, you can register up to 20 consumers per stream to use Enhanced Fan-out. A given consumer can only be registered with one stream at a time.</p> <p>For an example of how to use this operation, see <a href="https://docs.aws.amazon.com/streams/latest/dev/building-enhanced-consumers-api.html">Enhanced Fan-Out Using the Kinesis Data Streams API</a>.</p> <p>The use of this operation has a limit of five transactions per second per account. Also, only 5 consumers can be created simultaneously. In other words, you cannot have more than 5 consumers in a <code>CREATING</code> status at the same time. Registering a 6th consumer while there are 5 in a <code>CREATING</code> status results in a <code>LimitExceededException</code>.</p>

        Args:
            stream_arn: <p>The ARN of the Kinesis data stream that you want to register the consumer with. For more info, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>
            consumer_name: <p>For a given Kinesis data stream, each consumer must have a unique name. However, consumer names don't have to be unique across data streams.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>
            tags: <p>A set of up to 50 key-value pairs. A tag consists of a required key and an optional value.</p>

        Raises:
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.register_stream_consumer_input.RegisterStreamConsumerInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.register_stream_consumer_output.RegisterStreamConsumerOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.register_stream_consumer

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.register_stream_consumer.register_stream_consumer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.register_stream_consumer_input.RegisterStreamConsumerInput = {
            "stream_arn": stream_arn,
            "consumer_name": consumer_name,
        }
        if stream_id is not None:
            input_["stream_id"] = stream_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_tags_from_stream(
        self,
        tag_keys: "capo_kinesis.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> None:
        """<p>Removes tags from the specified Kinesis data stream. Removed tags are deleted and cannot be recovered after this operation successfully completes.</p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note> <p>If you specify a tag that does not exist, it is ignored.</p> <p> <a>RemoveTagsFromStream</a> has a limit of five transactions per second per account.</p>

        Args:
            stream_name: <p>The name of the stream.</p>
            tag_keys: <p>A list of tag keys. Each corresponding tag is removed from the stream.</p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.remove_tags_from_stream_input.RemoveTagsFromStreamInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.remove_tags_from_stream

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.remove_tags_from_stream.remove_tags_from_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.remove_tags_from_stream_input.RemoveTagsFromStreamInput = {
            "tag_keys": tag_keys
        }
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def split_shard(
        self,
        shard_to_split: "capo_kinesis.types.shard_id.ShardId",
        new_starting_hash_key: "capo_kinesis.types.hash_key.HashKey",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> None:
        """<p>Splits a shard into two new shards in the Kinesis data stream, to increase the stream's capacity to ingest and transport data. <code>SplitShard</code> is called when there is a need to increase the overall capacity of a stream because of an expected increase in the volume of data records being ingested. This API is only supported for the data streams with the provisioned capacity mode.</p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note> <p>You can also use <code>SplitShard</code> when a shard appears to be approaching its maximum utilization; for example, the producers sending data into the specific shard are suddenly sending more than previously anticipated. You can also call <code>SplitShard</code> to increase stream capacity, so that more Kinesis Data Streams applications can simultaneously read data from the stream for real-time processing. </p> <p>You must specify the shard to be split and the new hash key, which is the position in the shard where the shard gets split in two. In many cases, the new hash key might be the average of the beginning and ending hash key, but it can be any hash key value in the range being mapped into the shard. For more information, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/kinesis-using-sdk-java-resharding-split.html">Split a Shard</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>.</p> <p>You can use <a>DescribeStreamSummary</a> and the <a>ListShards</a> APIs to determine the shard ID and hash key values for the <code>ShardToSplit</code> and <code>NewStartingHashKey</code> parameters that are specified in the <code>SplitShard</code> request.</p> <p> <code>SplitShard</code> is an asynchronous operation. Upon receiving a <code>SplitShard</code> request, Kinesis Data Streams immediately returns a response and sets the stream status to <code>UPDATING</code>. After the operation is completed, Kinesis Data Streams sets the stream status to <code>ACTIVE</code>. Read and write operations continue to work while the stream is in the <code>UPDATING</code> state. </p> <p>You can use <a>DescribeStreamSummary</a> to check the status of the stream, which is returned in <code>StreamStatus</code>. If the stream is in the <code>ACTIVE</code> state, you can call <code>SplitShard</code>. </p> <p>If the specified stream does not exist, <a>DescribeStreamSummary</a> returns a <code>ResourceNotFoundException</code>. If you try to create more shards than are authorized for your account, you receive a <code>LimitExceededException</code>. </p> <p>For the default shard limit for an Amazon Web Services account, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html">Kinesis Data Streams Limits</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>. To increase this limit, <a href="https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html">contact Amazon Web Services Support</a>.</p> <p>If you try to operate on too many streams simultaneously using <a>CreateStream</a>, <a>DeleteStream</a>, <a>MergeShards</a>, and/or <a>SplitShard</a>, you receive a <code>LimitExceededException</code>. </p> <p> <code>SplitShard</code> has a limit of five transactions per second per account.</p>

        Args:
            stream_name: <p>The name of the stream for the shard split.</p>
            shard_to_split: <p>The shard ID of the shard to split.</p>
            new_starting_hash_key: <p>A hash key value for the starting hash key of one of the child shards created by the split. The hash key range for a given shard constitutes a set of ordered contiguous positive integers. The value for <code>NewStartingHashKey</code> must be in the range of hash keys being mapped into the shard. The <code>NewStartingHashKey</code> hash key value and all higher hash key values in hash key range are distributed to one of the child shards. All the lower hash key values in the range are distributed to the other child shard.</p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.validation_exception.ValidationException: <p>Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode. </p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.split_shard_input.SplitShardInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.split_shard

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.split_shard.split_shard(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.split_shard_input.SplitShardInput = {
            "shard_to_split": shard_to_split,
            "new_starting_hash_key": new_starting_hash_key,
        }
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_stream_encryption(
        self,
        encryption_type: "capo_kinesis.types.encryption_type.EncryptionType",
        key_id: "capo_kinesis.types.key_id.KeyId",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> None:
        """<p>Enables or updates server-side encryption using an Amazon Web Services KMS key for a specified stream. </p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note> <p>Starting encryption is an asynchronous operation. Upon receiving the request, Kinesis Data Streams returns immediately and sets the status of the stream to <code>UPDATING</code>. After the update is complete, Kinesis Data Streams sets the status of the stream back to <code>ACTIVE</code>. Updating or applying encryption normally takes a few seconds to complete, but it can take minutes. You can continue to read and write data to your stream while its status is <code>UPDATING</code>. Once the status of the stream is <code>ACTIVE</code>, encryption begins for records written to the stream. </p> <p>API Limits: You can successfully apply a new Amazon Web Services KMS key for server-side encryption 25 times in a rolling 24-hour period.</p> <p>Note: It can take up to 5 seconds after the stream is in an <code>ACTIVE</code> status before all records written to the stream are encrypted. After you enable encryption, you can verify that encryption is applied by inspecting the API response from <code>PutRecord</code> or <code>PutRecords</code>.</p>

        Args:
            stream_name: <p>The name of the stream for which to start encrypting records.</p>
            encryption_type: <p>The encryption type to use. The only valid value is <code>KMS</code>.</p>
            key_id: <p>The GUID for the customer-managed Amazon Web Services KMS key to use for encryption. This value can be a globally unique identifier, a fully specified Amazon Resource Name (ARN) to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by specifying the alias <code>aws/kinesis</code>.</p> <ul> <li> <p>Key ARN example: <code>arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012</code> </p> </li> <li> <p>Alias ARN example: <code>arn:aws:kms:us-east-1:123456789012:alias/MyAliasName</code> </p> </li> <li> <p>Globally unique key ID example: <code>12345678-1234-1234-1234-123456789012</code> </p> </li> <li> <p>Alias name example: <code>alias/MyAliasName</code> </p> </li> <li> <p>Master key owned by Kinesis Data Streams: <code>alias/aws/kinesis</code> </p> </li> </ul>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>The ciphertext references a key that doesn't exist or that you don't have access to.</p>
            capo_kinesis.errors.kms_disabled_exception.KMSDisabledException: <p>The request was rejected because the specified customer master key (CMK) isn't enabled.</p>
            capo_kinesis.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>The request was rejected because the state of the specified resource isn't valid for this request. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html">How Key State Affects Use of a Customer Master Key</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p>
            capo_kinesis.errors.kms_not_found_exception.KMSNotFoundException: <p>The request was rejected because the specified entity or resource can't be found.</p>
            capo_kinesis.errors.kms_opt_in_required.KMSOptInRequired: <p>The Amazon Web Services access key ID needs a subscription for the service.</p>
            capo_kinesis.errors.kms_throttling_exception.KMSThrottlingException: <p>The request was denied due to request throttling. For more information about throttling, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/limits.html#requests-per-second">Limits</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.start_stream_encryption_input.StartStreamEncryptionInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.start_stream_encryption

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.start_stream_encryption.start_stream_encryption(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.start_stream_encryption_input.StartStreamEncryptionInput = {
            "encryption_type": encryption_type,
            "key_id": key_id,
        }
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_stream_encryption(
        self,
        encryption_type: "capo_kinesis.types.encryption_type.EncryptionType",
        key_id: "capo_kinesis.types.key_id.KeyId",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> None:
        """<p>Disables server-side encryption for a specified stream. </p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note> <p>Stopping encryption is an asynchronous operation. Upon receiving the request, Kinesis Data Streams returns immediately and sets the status of the stream to <code>UPDATING</code>. After the update is complete, Kinesis Data Streams sets the status of the stream back to <code>ACTIVE</code>. Stopping encryption normally takes a few seconds to complete, but it can take minutes. You can continue to read and write data to your stream while its status is <code>UPDATING</code>. Once the status of the stream is <code>ACTIVE</code>, records written to the stream are no longer encrypted by Kinesis Data Streams. </p> <p>API Limits: You can successfully disable server-side encryption 25 times in a rolling 24-hour period. </p> <p>Note: It can take up to 5 seconds after the stream is in an <code>ACTIVE</code> status before all records written to the stream are no longer subject to encryption. After you disabled encryption, you can verify that encryption is not applied by inspecting the API response from <code>PutRecord</code> or <code>PutRecords</code>.</p>

        Args:
            stream_name: <p>The name of the stream on which to stop encrypting records.</p>
            encryption_type: <p>The encryption type. The only valid value is <code>KMS</code>.</p>
            key_id: <p>The GUID for the customer-managed Amazon Web Services KMS key to use for encryption. This value can be a globally unique identifier, a fully specified Amazon Resource Name (ARN) to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by specifying the alias <code>aws/kinesis</code>.</p> <ul> <li> <p>Key ARN example: <code>arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012</code> </p> </li> <li> <p>Alias ARN example: <code>arn:aws:kms:us-east-1:123456789012:alias/MyAliasName</code> </p> </li> <li> <p>Globally unique key ID example: <code>12345678-1234-1234-1234-123456789012</code> </p> </li> <li> <p>Alias name example: <code>alias/MyAliasName</code> </p> </li> <li> <p>Master key owned by Kinesis Data Streams: <code>alias/aws/kinesis</code> </p> </li> </ul>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.stop_stream_encryption_input.StopStreamEncryptionInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.stop_stream_encryption

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.stop_stream_encryption.stop_stream_encryption(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.stop_stream_encryption_input.StopStreamEncryptionInput = {
            "encryption_type": encryption_type,
            "key_id": key_id,
        }
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def subscribe_to_shard(
        self,
        consumer_arn: "capo_kinesis.types.consumer_arn.ConsumerARN",
        shard_id: "capo_kinesis.types.shard_id.ShardId",
        starting_position: "capo_kinesis.types.starting_position.StartingPosition",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
        dry_run: Optional["capo_kinesis.types.boolean_object.BooleanObject"] = None,
    ) -> "capo_kinesis.types.subscribe_to_shard_output.SubscribeToShardOutput":
        """<p>This operation establishes an HTTP/2 connection between the consumer you specify in the <code>ConsumerARN</code> parameter and the shard you specify in the <code>ShardId</code> parameter. After the connection is successfully established, Kinesis Data Streams pushes records from the shard to the consumer over this connection. Before you call this operation, call <a>RegisterStreamConsumer</a> to register the consumer with Kinesis Data Streams.</p> <p>When the <code>SubscribeToShard</code> call succeeds, your consumer starts receiving events of type <a>SubscribeToShardEvent</a> over the HTTP/2 connection for up to 5 minutes, after which time you need to call <code>SubscribeToShard</code> again to renew the subscription if you want to continue to receive records.</p> <p>You can make one call to <code>SubscribeToShard</code> per second per registered consumer per shard. For example, if you have a 4000 shard stream and two registered stream consumers, you can make one <code>SubscribeToShard</code> request per second for each combination of shard and registered consumer, allowing you to subscribe both consumers to all 4000 shards in one second. </p> <p>If you call <code>SubscribeToShard</code> again with the same <code>ConsumerARN</code> and <code>ShardId</code> within 5 seconds of a successful call, you'll get a <code>ResourceInUseException</code>. If you call <code>SubscribeToShard</code> 5 seconds or more after a successful call, the second call takes over the subscription and the previous connection expires or fails with a <code>ResourceInUseException</code>.</p> <p>For an example of how to use this operation, see <a href="https://docs.aws.amazon.com/streams/latest/dev/building-enhanced-consumers-api.html">Enhanced Fan-Out Using the Kinesis Data Streams API</a>.</p>

        Args:
            consumer_arn: <p>For this parameter, use the value you obtained when you called <a>RegisterStreamConsumer</a>.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>
            shard_id: <p>The ID of the shard you want to subscribe to. To see a list of all the shards for a given stream, use <a>ListShards</a>.</p>
            starting_position: <p>The starting position in the data stream from which to start streaming.</p>
            dry_run: <p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was rejected because the DryRun parameter was specified.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.subscribe_to_shard_input.SubscribeToShardInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.subscribe_to_shard_output.SubscribeToShardOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.subscribe_to_shard

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.subscribe_to_shard.subscribe_to_shard(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.subscribe_to_shard_input.SubscribeToShardInput = {
            "consumer_arn": consumer_arn,
            "shard_id": shard_id,
            "starting_position": starting_position,
        }
        if stream_id is not None:
            input_["stream_id"] = stream_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        tags: "capo_kinesis.types.tag_map.TagMap",
        resource_arn: "capo_kinesis.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> None:
        """<p>Adds or updates tags for the specified Kinesis resource. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources. You can assign up to 50 tags to a Kinesis resource.</p>

        Args:
            tags: <p>An array of tags to be added to the Kinesis resource. A tag consists of a required key and an optional value. You can add up to 50 tags per resource.</p> <p>Tags may only contain Unicode letters, digits, white space, or these symbols: _ . : / = + - @.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the Kinesis resource to which to add tags.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.tag_resource

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.tag_resource_input.TagResourceInput = {
            "tags": tags,
            "resource_arn": resource_arn,
        }
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        tag_keys: "capo_kinesis.types.tag_key_list.TagKeyList",
        resource_arn: "capo_kinesis.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> None:
        """<p>Removes tags from the specified Kinesis resource. Removed tags are deleted and can't be recovered after this operation completes successfully.</p>

        Args:
            tag_keys: <p>A list of tag key-value pairs. Existing tags of the resource whose keys are members of this list will be removed from the Kinesis resource.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the Kinesis resource from which to remove tags.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.untag_resource

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.untag_resource_input.UntagResourceInput = {
            "tag_keys": tag_keys,
            "resource_arn": resource_arn,
        }
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_account_settings(
        self,
        minimum_throughput_billing_commitment: "capo_kinesis.types.minimum_throughput_billing_commitment_input.MinimumThroughputBillingCommitmentInput",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
    ) -> (
        "capo_kinesis.types.update_account_settings_output.UpdateAccountSettingsOutput"
    ):
        """<p>Updates the account-level settings for Amazon Kinesis Data Streams.</p> <p>Updating account settings is a synchronous operation. Upon receiving the request, Kinesis Data Streams will return immediately with your account’s updated settings.</p> <p> <b>API limits</b> </p> <ul> <li> <p>Certain account configurations have minimum commitment windows. Attempting to update your settings prior to the end of the minimum commitment window might have certain restrictions.</p> </li> <li> <p>This API has a call limit of 5 transactions per second (TPS) for each Amazon Web Services account. TPS over 5 will initiate the <code>LimitExceededException</code>.</p> </li> </ul>

        Args:
            minimum_throughput_billing_commitment: <p>Specifies the minimum throughput billing commitment configuration for your account.</p>

        Raises:
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.validation_exception.ValidationException: <p>Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode. </p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.update_account_settings_input.UpdateAccountSettingsInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.update_account_settings_output.UpdateAccountSettingsOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.update_account_settings

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.update_account_settings.update_account_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.update_account_settings_input.UpdateAccountSettingsInput = {
            "minimum_throughput_billing_commitment": minimum_throughput_billing_commitment
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_channel(
        self,
        channel_arn: "capo_kinesis.types.channel_arn.ChannelARN",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        s3_destination_configuration: Optional[
            "capo_kinesis.types.s3_destination_update_input.S3DestinationUpdateInput"
        ] = None,
        s3_tables_destination_configuration: Optional[
            "capo_kinesis.types.s3_tables_destination_update_input.S3TablesDestinationUpdateInput"
        ] = None,
        logging_configuration: Optional[
            "capo_kinesis.types.channel_logging_update_input.ChannelLoggingUpdateInput"
        ] = None,
    ) -> "capo_kinesis.types.update_channel_output.UpdateChannelOutput":
        """<p>Updates the data freshness interval or the Amazon CloudWatch Logs configuration of an existing channel. You cannot change the destination, source stream, record format, schema, encryption configuration, or service execution role of an existing channel. To change any other setting, delete the channel and create a new one.</p> <p>Updating a channel is an asynchronous operation. Upon receiving the request, Amazon Kinesis Data Streams sets the channel to the <code>UPDATING</code> state and returns immediately. After the change is applied, Amazon Kinesis Data Streams sets the channel back to the <code>ACTIVE</code> state.</p> <p>This operation has a call limit of 5 transactions per second (TPS) for each Amazon Web Services account. Exceeding 5 TPS results in a <code>LimitExceededException</code>.</p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) of the channel to update.</p>
            s3_destination_configuration: <p>The updated configuration for a general purpose Amazon S3 destination. Specify this parameter when the channel delivers to a general purpose Amazon S3 bucket. Only <code>DataFreshnessInSeconds</code> can be updated.</p>
            s3_tables_destination_configuration: <p>The updated configuration for a streaming table destination. Specify this parameter when the channel delivers to streaming tables on Apache Iceberg in Amazon S3 Tables. Only <code>DataFreshnessInSeconds</code> can be updated.</p>
            logging_configuration: <p>The updated Amazon CloudWatch Logs configuration for the channel.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.validation_exception.ValidationException: <p>Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode. </p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a channel

            >>> client.update_channel(channel_arn='arn:aws:kinesis:us-east-1:123456789012:channel/my-channel-id', s3_destination_configuration={'DataFreshnessInSeconds': 600}, logging_configuration={'CloudWatchLogs': {'Enabled': True, 'LogGroupName': '/aws/kinesis/my-channel', 'LogStreamName': 'my-channel-log-stream'}})
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.update_channel_input.UpdateChannelInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.update_channel_output.UpdateChannelOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.update_channel

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.update_channel.update_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.update_channel_input.UpdateChannelInput = {
            "channel_arn": channel_arn
        }
        if s3_destination_configuration is not None:
            input_["s3_destination_configuration"] = s3_destination_configuration
        if s3_tables_destination_configuration is not None:
            input_["s3_tables_destination_configuration"] = (
                s3_tables_destination_configuration
            )
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_max_record_size(
        self,
        max_record_size_in_ki_b: "capo_kinesis.types.max_record_size_in_ki_b.MaxRecordSizeInKiB",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> None:
        """<p>This allows you to update the <code>MaxRecordSize</code> of a single record that you can write to, and read from a stream. You can ingest and digest single records up to 10240 KiB.</p>

        Args:
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream for the <code>MaxRecordSize</code> update.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>
            max_record_size_in_ki_b: <p>The maximum record size of a single record in KiB that you can write to, and read from a stream. Specify a value between 1024 and 10240 KiB (1 to 10 MiB). If you specify a value that is out of this range, <code>UpdateMaxRecordSize</code> sends back an <code>ValidationException</code> message.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.validation_exception.ValidationException: <p>Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode. </p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.update_max_record_size_input.UpdateMaxRecordSizeInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.update_max_record_size

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.update_max_record_size.update_max_record_size(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.update_max_record_size_input.UpdateMaxRecordSizeInput = {
            "max_record_size_in_ki_b": max_record_size_in_ki_b
        }
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_shard_count(
        self,
        target_shard_count: "capo_kinesis.types.positive_integer_object.PositiveIntegerObject",
        scaling_type: "capo_kinesis.types.scaling_type.ScalingType",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> "capo_kinesis.types.update_shard_count_output.UpdateShardCountOutput":
        """<p>Updates the shard count of the specified stream to the specified number of shards. This API is only supported for the data streams with the provisioned capacity mode.</p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note> <p>Updating the shard count is an asynchronous operation. Upon receiving the request, Kinesis Data Streams returns immediately and sets the status of the stream to <code>UPDATING</code>. After the update is complete, Kinesis Data Streams sets the status of the stream back to <code>ACTIVE</code>. Depending on the size of the stream, the scaling action could take a few minutes to complete. You can continue to read and write data to your stream while its status is <code>UPDATING</code>.</p> <p>To update the shard count, Kinesis Data Streams performs splits or merges on individual shards. This can cause short-lived shards to be created, in addition to the final shards. These short-lived shards count towards your total shard limit for your account in the Region.</p> <p>When using this operation, we recommend that you specify a target shard count that is a multiple of 25% (25%, 50%, 75%, 100%). You can specify any target value within your shard limit. However, if you specify a target that isn't a multiple of 25%, the scaling action might take longer to complete. </p> <p>This operation has the following default limits. By default, you cannot do the following:</p> <ul> <li> <p>Scale more than ten times per rolling 24-hour period per stream</p> </li> <li> <p>Scale up to more than double your current shard count for a stream</p> </li> <li> <p>Scale down below half your current shard count for a stream</p> </li> <li> <p>Scale up to more than 10000 shards in a stream</p> </li> <li> <p>Scale a stream with more than 10000 shards down unless the result is less than 10000 shards</p> </li> <li> <p>Scale up to more than the shard limit for your account</p> </li> <li> <p>Make over 10 TPS. TPS over 10 will trigger the LimitExceededException</p> </li> </ul> <p>For the default limits for an Amazon Web Services account, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html">Streams Limits</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>. To request an increase in the call rate limit, the shard limit for this API, or your overall shard limit, use the <a href="https://console.aws.amazon.com/support/v1#/case/create?issueType=service-limit-increase&limitType=service-code-kinesis">limits form</a>.</p>

        Args:
            stream_name: <p>The name of the stream.</p>
            target_shard_count: <p>The new number of shards. This value has the following default limits. By default, you cannot do the following: </p> <ul> <li> <p>Set this value to more than double your current shard count for a stream.</p> </li> <li> <p>Set this value below half your current shard count for a stream.</p> </li> <li> <p>Set this value to more than 10000 shards in a stream (the default limit for shard count per stream is 10000 per account per region), unless you request a limit increase.</p> </li> <li> <p>Scale a stream with more than 10000 shards down unless you set this value to less than 10000 shards.</p> </li> </ul>
            scaling_type: <p>The scaling type. Uniform scaling creates shards of equal size.</p>
            stream_arn: <p>The ARN of the stream.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.validation_exception.ValidationException: <p>Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode. </p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.update_shard_count_input.UpdateShardCountInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.update_shard_count_output.UpdateShardCountOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.update_shard_count

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.update_shard_count.update_shard_count(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.update_shard_count_input.UpdateShardCountInput = {
            "target_shard_count": target_shard_count,
            "scaling_type": scaling_type,
        }
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_stream_mode(
        self,
        stream_arn: "capo_kinesis.types.stream_arn.StreamARN",
        stream_mode_details: "capo_kinesis.types.stream_mode_details.StreamModeDetails",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
        warm_throughput_mi_bps: Optional[
            "capo_kinesis.types.natural_integer_object.NaturalIntegerObject"
        ] = None,
    ) -> None:
        """<p> Updates the capacity mode of the data stream. Currently, in Kinesis Data Streams, you can choose between an <b>on-demand</b> capacity mode and a <b>provisioned</b> capacity mode for your data stream. </p> <p>If you'd still like to proactively scale your on-demand data stream’s capacity, you can unlock the warm throughput feature for on-demand data streams by enabling <code>MinimumThroughputBillingCommitment</code> for your account. Once your account has <code>MinimumThroughputBillingCommitment</code> enabled, you can specify the warm throughput in MiB per second that your stream can support in writes.</p>

        Args:
            stream_arn: <p> Specifies the ARN of the data stream whose capacity mode you want to update. </p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>
            stream_mode_details: <p> Specifies the capacity mode to which you want to set your data stream. Currently, in Kinesis Data Streams, you can choose between an <b>on-demand</b> capacity mode and a <b>provisioned</b> capacity mode for your data streams. </p>
            warm_throughput_mi_bps: <p>The target warm throughput in MB/s that the stream should be scaled to handle. This represents the throughput capacity that will be immediately available for write operations. This field is only valid when the stream mode is being updated to on-demand.</p>

        Raises:
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.validation_exception.ValidationException: <p>Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode. </p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.update_stream_mode_input.UpdateStreamModeInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.update_stream_mode

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.update_stream_mode.update_stream_mode(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.update_stream_mode_input.UpdateStreamModeInput = {
            "stream_arn": stream_arn,
            "stream_mode_details": stream_mode_details,
        }
        if stream_id is not None:
            input_["stream_id"] = stream_id
        if warm_throughput_mi_bps is not None:
            input_["warm_throughput_mi_bps"] = warm_throughput_mi_bps

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_stream_record_distribution_strategy(
        self,
        stream_arn: "capo_kinesis.types.stream_arn.StreamARN",
        record_distribution_strategy: "capo_kinesis.types.record_distribution_strategy.RecordDistributionStrategy",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> None:
        """<p>Updates the record distribution strategy for the specified Amazon Kinesis Data Streams on-demand data stream. The record distribution strategy determines how Amazon Kinesis Data Streams distributes records across the shards in a stream.</p> <note> <p>You must specify the stream using the <code>StreamARN</code> parameter.</p> </note> <p>The record distribution strategy is a stream-level setting. You can switch between the following strategies at any time, and the change takes effect immediately without downtime, data loss, or disruption to producer or consumer applications:</p> <ul> <li> <p> <code>AUTO</code> – Amazon Kinesis Data Streams distributes records evenly across shards using service-managed algorithms, and ignores any partition key and <code>ExplicitHashKey</code> that a producer provides. Use this strategy for stateless workloads that do not require partition-key ordering.</p> </li> <li> <p> <code>USER_PARTITION_KEY</code> – Producers must provide a partition key, and Amazon Kinesis Data Streams uses the partition key to determine shard placement. Records that share a partition key are sent to the same shard. This is the default strategy.</p> </li> </ul> <p>This operation is only supported for data streams that use the on-demand capacity mode. Provisioned capacity mode streams do not support the record distribution strategy setting. Attempting to set <code>AUTO</code> on a provisioned stream results in an <code>InvalidArgumentException</code>.</p> <p>New records that arrive after the change are distributed according to the new strategy. Records already in the stream keep their original shard assignments and are not redistributed.</p>

        Args:
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream to update.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>
            record_distribution_strategy: <p>The record distribution strategy to apply to the stream. Specify one of the following values:</p> <ul> <li> <p> <code>AUTO</code> – Amazon Kinesis Data Streams distributes records evenly across shards and ignores any partition key and <code>ExplicitHashKey</code> that producers supply.</p> </li> <li> <p> <code>USER_PARTITION_KEY</code> – Producers must supply a partition key, which Amazon Kinesis Data Streams uses to determine shard placement. This is the default.</p> </li> </ul>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.validation_exception.ValidationException: <p>Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode. </p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.update_stream_record_distribution_strategy_input.UpdateStreamRecordDistributionStrategyInput]",
        ) -> OperationResponse[None]:
            import capo_kinesis._operations.kinesis_20131202.update_stream_record_distribution_strategy

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.update_stream_record_distribution_strategy.update_stream_record_distribution_strategy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.update_stream_record_distribution_strategy_input.UpdateStreamRecordDistributionStrategyInput = {
            "stream_arn": stream_arn,
            "record_distribution_strategy": record_distribution_strategy,
        }
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_stream_warm_throughput(
        self,
        warm_throughput_mi_bps: "capo_kinesis.types.natural_integer_object.NaturalIntegerObject",
        *,
        config_overrides: Optional[KinesisClientConfig] = None,
        stream_arn: Optional["capo_kinesis.types.stream_arn.StreamARN"] = None,
        stream_name: Optional["capo_kinesis.types.stream_name.StreamName"] = None,
        stream_id: Optional["capo_kinesis.types.stream_id.StreamId"] = None,
    ) -> "capo_kinesis.types.update_stream_warm_throughput_output.UpdateStreamWarmThroughputOutput":
        """<p>Updates the warm throughput configuration for the specified Amazon Kinesis Data Streams on-demand data stream. Updates the warm throughput configuration for the specified on-demand data stream. Use this operation to scale your stream to a specified throughput level before anticipated traffic spikes, or to release excess capacity after traffic has decreased. </p> <note> <p>When invoking this API, you must use either the <code>StreamARN</code> or the <code>StreamName</code> parameter, or both. It is recommended that you use the <code>StreamARN</code> input parameter when you invoke this API.</p> </note> <p>Updating the warm throughput is an asynchronous operation. Upon receiving the request, Kinesis Data Streams returns immediately and sets the status of the stream to <code>UPDATING</code>. After the update is complete, Kinesis Data Streams sets the status of the stream back to <code>ACTIVE</code>. Depending on the size of the stream, the scaling action could take a few minutes to complete. You can continue to read and write data to your stream while its status is <code>UPDATING</code>.</p> <p>This operation is only supported for data streams with the on-demand capacity mode in accounts that have <code>MinimumThroughputBillingCommitment</code> enabled. Provisioned capacity mode streams do not support warm throughput configuration.</p> <p>To release excess capacity, call the API again and set the warm throughput to the same or a lower value.</p> <p>This operation has the following default limits. By default, you cannot do the following:</p> <ul> <li> <p>Scale to more than 10 GiBps for an on-demand stream.</p> </li> <li> <p>This API has a call limit of 5 transactions per second (TPS) for each Amazon Web Services account. TPS over 5 will initiate the <code>LimitExceededException</code>.</p> </li> </ul> <p>For the default limits for an Amazon Web Services account, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html">Streams Limits</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>. To request an increase in the call rate limit, the shard limit for this API, or your overall shard limit, use the <a href="https://console.aws.amazon.com/support/v1#/case/create?issueType=service-limit-increase&limitType=service-code-kinesis">limits form</a>.</p>

        Args:
            stream_arn: <p>The ARN of the stream to be updated.</p>
            stream_name: <p>The name of the stream to be updated.</p>
            stream_id: <p>Not Implemented. Reserved for future use.</p>
            warm_throughput_mi_bps: <p>The target warm throughput in MB/s that the stream should be scaled to handle. This represents the throughput capacity that will be immediately available for write operations.</p>

        Raises:
            capo_kinesis.errors.access_denied_exception.AccessDeniedException: <p>Specifies that you do not have the permissions required to perform this operation.</p>
            capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException: <p>A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.</p>
            capo_kinesis.errors.limit_exceeded_exception.LimitExceededException: <p>The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed. </p>
            capo_kinesis.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is not available for this operation. For successful operation, the resource must be in the <code>ACTIVE</code> state.</p>
            capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found. The stream might not be specified correctly.</p>
            capo_kinesis.errors.validation_exception.ValidationException: <p>Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode. </p>
            capo_kinesis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis.types.update_stream_warm_throughput_input.UpdateStreamWarmThroughputInput]",
        ) -> OperationResponse[
            "capo_kinesis.types.update_stream_warm_throughput_output.UpdateStreamWarmThroughputOutput"
        ]:
            import capo_kinesis._operations.kinesis_20131202.update_stream_warm_throughput

            output, http_response = (
                capo_kinesis._operations.kinesis_20131202.update_stream_warm_throughput.update_stream_warm_throughput(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis.types.update_stream_warm_throughput_input.UpdateStreamWarmThroughputInput = {
            "warm_throughput_mi_bps": warm_throughput_mi_bps
        }
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
