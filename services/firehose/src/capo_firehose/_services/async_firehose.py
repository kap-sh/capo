"""Generated from Smithy shape ``com.amazonaws.firehose#Firehose_20150804``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_firehose._auth._signers
import capo_firehose._auth._sigv4
from capo_firehose._auth._identity import Credentials
from capo_firehose._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_firehose._auth._zapros_handler import AuthMiddleware
from capo_firehose._services._aws_config import aaws_config
from capo_firehose._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_firehose.types.amazon_open_search_serverless_destination_configuration
    import capo_firehose.types.amazon_open_search_serverless_destination_update
    import capo_firehose.types.amazonopensearchservice_destination_configuration
    import capo_firehose.types.amazonopensearchservice_destination_update
    import capo_firehose.types.boolean_object
    import capo_firehose.types.create_delivery_stream_input
    import capo_firehose.types.create_delivery_stream_output
    import capo_firehose.types.database_source_configuration
    import capo_firehose.types.delete_delivery_stream_input
    import capo_firehose.types.delete_delivery_stream_output
    import capo_firehose.types.delivery_stream_encryption_configuration_input
    import capo_firehose.types.delivery_stream_name
    import capo_firehose.types.delivery_stream_type
    import capo_firehose.types.delivery_stream_version_id
    import capo_firehose.types.describe_delivery_stream_input
    import capo_firehose.types.describe_delivery_stream_input_limit
    import capo_firehose.types.describe_delivery_stream_output
    import capo_firehose.types.destination_id
    import capo_firehose.types.direct_put_source_configuration
    import capo_firehose.types.elasticsearch_destination_configuration
    import capo_firehose.types.elasticsearch_destination_update
    import capo_firehose.types.extended_s3_destination_configuration
    import capo_firehose.types.extended_s3_destination_update
    import capo_firehose.types.http_endpoint_destination_configuration
    import capo_firehose.types.http_endpoint_destination_update
    import capo_firehose.types.iceberg_destination_configuration
    import capo_firehose.types.iceberg_destination_update
    import capo_firehose.types.kinesis_stream_source_configuration
    import capo_firehose.types.list_delivery_streams_input
    import capo_firehose.types.list_delivery_streams_input_limit
    import capo_firehose.types.list_delivery_streams_output
    import capo_firehose.types.list_tags_for_delivery_stream_input
    import capo_firehose.types.list_tags_for_delivery_stream_input_limit
    import capo_firehose.types.list_tags_for_delivery_stream_output
    import capo_firehose.types.msk_source_configuration
    import capo_firehose.types.put_record_batch_input
    import capo_firehose.types.put_record_batch_output
    import capo_firehose.types.put_record_batch_request_entry_list
    import capo_firehose.types.put_record_input
    import capo_firehose.types.put_record_output
    import capo_firehose.types.record
    import capo_firehose.types.redshift_destination_configuration
    import capo_firehose.types.redshift_destination_update
    import capo_firehose.types.s3_destination_configuration
    import capo_firehose.types.s3_destination_update
    import capo_firehose.types.snowflake_destination_configuration
    import capo_firehose.types.snowflake_destination_update
    import capo_firehose.types.splunk_destination_configuration
    import capo_firehose.types.splunk_destination_update
    import capo_firehose.types.start_delivery_stream_encryption_input
    import capo_firehose.types.start_delivery_stream_encryption_output
    import capo_firehose.types.stop_delivery_stream_encryption_input
    import capo_firehose.types.stop_delivery_stream_encryption_output
    import capo_firehose.types.tag_delivery_stream_input
    import capo_firehose.types.tag_delivery_stream_input_tag_list
    import capo_firehose.types.tag_delivery_stream_output
    import capo_firehose.types.tag_key
    import capo_firehose.types.tag_key_list
    import capo_firehose.types.untag_delivery_stream_input
    import capo_firehose.types.untag_delivery_stream_output
    import capo_firehose.types.update_destination_input
    import capo_firehose.types.update_destination_output


class AsyncFirehoseClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncFirehoseClient:
    """A client for the ``Firehose`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncFirehoseClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncFirehoseClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncFirehoseClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def create_delivery_stream(
        self,
        delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName",
        *,
        config_overrides: Optional[AsyncFirehoseClientConfig] = None,
        delivery_stream_type: Optional[
            "capo_firehose.types.delivery_stream_type.DeliveryStreamType"
        ] = None,
        direct_put_source_configuration: Optional[
            "capo_firehose.types.direct_put_source_configuration.DirectPutSourceConfiguration"
        ] = None,
        kinesis_stream_source_configuration: Optional[
            "capo_firehose.types.kinesis_stream_source_configuration.KinesisStreamSourceConfiguration"
        ] = None,
        delivery_stream_encryption_configuration_input: Optional[
            "capo_firehose.types.delivery_stream_encryption_configuration_input.DeliveryStreamEncryptionConfigurationInput"
        ] = None,
        s3_destination_configuration: Optional[
            "capo_firehose.types.s3_destination_configuration.S3DestinationConfiguration"
        ] = None,
        extended_s3_destination_configuration: Optional[
            "capo_firehose.types.extended_s3_destination_configuration.ExtendedS3DestinationConfiguration"
        ] = None,
        redshift_destination_configuration: Optional[
            "capo_firehose.types.redshift_destination_configuration.RedshiftDestinationConfiguration"
        ] = None,
        elasticsearch_destination_configuration: Optional[
            "capo_firehose.types.elasticsearch_destination_configuration.ElasticsearchDestinationConfiguration"
        ] = None,
        amazonopensearchservice_destination_configuration: Optional[
            "capo_firehose.types.amazonopensearchservice_destination_configuration.AmazonopensearchserviceDestinationConfiguration"
        ] = None,
        splunk_destination_configuration: Optional[
            "capo_firehose.types.splunk_destination_configuration.SplunkDestinationConfiguration"
        ] = None,
        http_endpoint_destination_configuration: Optional[
            "capo_firehose.types.http_endpoint_destination_configuration.HttpEndpointDestinationConfiguration"
        ] = None,
        tags: Optional[
            "capo_firehose.types.tag_delivery_stream_input_tag_list.TagDeliveryStreamInputTagList"
        ] = None,
        amazon_open_search_serverless_destination_configuration: Optional[
            "capo_firehose.types.amazon_open_search_serverless_destination_configuration.AmazonOpenSearchServerlessDestinationConfiguration"
        ] = None,
        msk_source_configuration: Optional[
            "capo_firehose.types.msk_source_configuration.MSKSourceConfiguration"
        ] = None,
        snowflake_destination_configuration: Optional[
            "capo_firehose.types.snowflake_destination_configuration.SnowflakeDestinationConfiguration"
        ] = None,
        iceberg_destination_configuration: Optional[
            "capo_firehose.types.iceberg_destination_configuration.IcebergDestinationConfiguration"
        ] = None,
        database_source_configuration: Optional[
            "capo_firehose.types.database_source_configuration.DatabaseSourceConfiguration"
        ] = None,
    ) -> "capo_firehose.types.create_delivery_stream_output.CreateDeliveryStreamOutput":
        """<p>Creates a Firehose stream.</p> <p>By default, you can create up to 5,000 Firehose streams per Amazon Web Services Region.</p> <p>This is an asynchronous operation that immediately returns. The initial status of the Firehose stream is <code>CREATING</code>. After the Firehose stream is created, its status is <code>ACTIVE</code> and it now accepts data. If the Firehose stream creation fails, the status transitions to <code>CREATING_FAILED</code>. Attempts to send data to a delivery stream that is not in the <code>ACTIVE</code> state cause an exception. To check the state of a Firehose stream, use <a>DescribeDeliveryStream</a>.</p> <p>If the status of a Firehose stream is <code>CREATING_FAILED</code>, this status doesn't change, and you can't invoke <code>CreateDeliveryStream</code> again on it. However, you can invoke the <a>DeleteDeliveryStream</a> operation to delete it.</p> <p>A Firehose stream can be configured to receive records directly from providers using <a>PutRecord</a> or <a>PutRecordBatch</a>, or it can be configured to use an existing Kinesis stream as its source. To specify a Kinesis data stream as input, set the <code>DeliveryStreamType</code> parameter to <code>KinesisStreamAsSource</code>, and provide the Kinesis stream Amazon Resource Name (ARN) and role ARN in the <code>KinesisStreamSourceConfiguration</code> parameter.</p> <p>To create a Firehose stream with server-side encryption (SSE) enabled, include <a>DeliveryStreamEncryptionConfigurationInput</a> in your request. This is optional. You can also invoke <a>StartDeliveryStreamEncryption</a> to turn on SSE for an existing Firehose stream that doesn't have SSE enabled.</p> <p>A Firehose stream is configured with a single destination, such as Amazon Simple Storage Service (Amazon S3), Amazon Redshift, Amazon OpenSearch Service, Amazon OpenSearch Serverless, Splunk, and any custom HTTP endpoint or HTTP endpoints owned by or supported by third-party service providers, including Datadog, Dynatrace, LogicMonitor, MongoDB, New Relic, and Sumo Logic. You must specify only one of the following destination configuration parameters: <code>ExtendedS3DestinationConfiguration</code>, <code>S3DestinationConfiguration</code>, <code>ElasticsearchDestinationConfiguration</code>, <code>RedshiftDestinationConfiguration</code>, or <code>SplunkDestinationConfiguration</code>.</p> <p>When you specify <code>S3DestinationConfiguration</code>, you can also provide the following optional values: BufferingHints, <code>EncryptionConfiguration</code>, and <code>CompressionFormat</code>. By default, if no <code>BufferingHints</code> value is provided, Firehose buffers data up to 5 MB or for 5 minutes, whichever condition is satisfied first. <code>BufferingHints</code> is a hint, so there are some cases where the service cannot adhere to these conditions strictly. For example, record boundaries might be such that the size is a little over or under the configured buffering size. By default, no encryption is performed. We strongly recommend that you enable encryption to ensure secure data storage in Amazon S3.</p> <p>A few notes about Amazon Redshift as a destination:</p> <ul> <li> <p>An Amazon Redshift destination requires an S3 bucket as intermediate location. Firehose first delivers data to Amazon S3 and then uses <code>COPY</code> syntax to load data into an Amazon Redshift table. This is specified in the <code>RedshiftDestinationConfiguration.S3Configuration</code> parameter.</p> </li> <li> <p>The compression formats <code>SNAPPY</code> or <code>ZIP</code> cannot be specified in <code>RedshiftDestinationConfiguration.S3Configuration</code> because the Amazon Redshift <code>COPY</code> operation that reads from the S3 bucket doesn't support these compression formats.</p> </li> <li> <p>We strongly recommend that you use the user name and password you provide exclusively with Firehose, and that the permissions for the account are restricted for Amazon Redshift <code>INSERT</code> permissions.</p> </li> </ul> <p>Firehose assumes the IAM role that is configured as part of the destination. The role should allow the Firehose principal to assume the role, and the role should have permissions that allow the service to deliver the data. For more information, see <a href="https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-s3">Grant Firehose Access to an Amazon S3 Destination</a> in the <i>Amazon Firehose Developer Guide</i>.</p>

        Args:
            delivery_stream_name: <p>The name of the Firehose stream. This name must be unique per Amazon Web Services account in the same Amazon Web Services Region. If the Firehose streams are in different accounts or different Regions, you can have multiple Firehose streams with the same name.</p>
            delivery_stream_type: <p>The Firehose stream type. This parameter can be one of the following values:</p> <ul> <li> <p> <code>DirectPut</code>: Provider applications access the Firehose stream directly.</p> </li> <li> <p> <code>KinesisStreamAsSource</code>: The Firehose stream uses a Kinesis data stream as a source.</p> </li> </ul>
            direct_put_source_configuration: <p>The structure that configures parameters such as <code>ThroughputHintInMBs</code> for a stream configured with Direct PUT as a source. </p>
            kinesis_stream_source_configuration: <p>When a Kinesis data stream is used as the source for the Firehose stream, a <a>KinesisStreamSourceConfiguration</a> containing the Kinesis data stream Amazon Resource Name (ARN) and the role ARN for the source stream.</p>
            delivery_stream_encryption_configuration_input: <p>Used to specify the type and Amazon Resource Name (ARN) of the KMS key needed for Server-Side Encryption (SSE).</p>
            s3_destination_configuration: <p>[Deprecated] The destination in Amazon S3. You can specify only one destination.</p>
            extended_s3_destination_configuration: <p>The destination in Amazon S3. You can specify only one destination.</p>
            redshift_destination_configuration: <p>The destination in Amazon Redshift. You can specify only one destination.</p>
            elasticsearch_destination_configuration: <p>The destination in Amazon OpenSearch Service. You can specify only one destination.</p>
            amazonopensearchservice_destination_configuration: <p>The destination in Amazon OpenSearch Service. You can specify only one destination.</p>
            splunk_destination_configuration: <p>The destination in Splunk. You can specify only one destination.</p>
            http_endpoint_destination_configuration: <p>Enables configuring Kinesis Firehose to deliver data to any HTTP endpoint destination. You can specify only one destination.</p>
            tags: <p>A set of tags to assign to the Firehose stream. A tag is a key-value pair that you can define and assign to Amazon Web Services resources. Tags are metadata. For example, you can add friendly names and descriptions or other types of information that can help you distinguish the Firehose stream. For more information about tags, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html">Using Cost Allocation Tags</a> in the Amazon Web Services Billing and Cost Management User Guide.</p> <p>You can specify up to 50 tags when creating a Firehose stream.</p> <p>If you specify tags in the <code>CreateDeliveryStream</code> action, Amazon Data Firehose performs an additional authorization on the <code>firehose:TagDeliveryStream</code> action to verify if users have permissions to create tags. If you do not provide this permission, requests to create new Firehose streams with IAM resource tags will fail with an <code>AccessDeniedException</code> such as following.</p> <p> <b>AccessDeniedException</b> </p> <p>User: arn:aws:sts::x:assumed-role/x/x is not authorized to perform: firehose:TagDeliveryStream on resource: arn:aws:firehose:us-east-1:x:deliverystream/x with an explicit deny in an identity-based policy.</p> <p>For an example IAM policy, see <a href="https://docs.aws.amazon.com/firehose/latest/APIReference/API_CreateDeliveryStream.html#API_CreateDeliveryStream_Examples">Tag example.</a> </p>
            amazon_open_search_serverless_destination_configuration: <p>The destination in the Serverless offering for Amazon OpenSearch Service. You can specify only one destination.</p>
            snowflake_destination_configuration: <p>Configure Snowflake destination</p>
            iceberg_destination_configuration: <p> Configure Apache Iceberg Tables destination. </p>
            database_source_configuration: <p> The top level object for configuring streams with database as a source. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>

        Raises:
            capo_firehose.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter has a value that is not valid.</p>
            capo_firehose.errors.invalid_kms_resource_exception.InvalidKMSResourceException: <p>Firehose throws this exception when an attempt to put records or to start or stop Firehose stream encryption fails. This happens when the KMS service throws one of the following exception types: <code>AccessDeniedException</code>, <code>InvalidStateException</code>, <code>DisabledException</code>, or <code>NotFoundException</code>.</p>
            capo_firehose.errors.limit_exceeded_exception.LimitExceededException: <p>You have already reached the limit for a requested resource.</p>
            capo_firehose.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is already in use and not available for this operation.</p>
            capo_firehose.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_firehose.types.create_delivery_stream_input.CreateDeliveryStreamInput]",
        ) -> AsyncOperationResponse[
            "capo_firehose.types.create_delivery_stream_output.CreateDeliveryStreamOutput"
        ]:
            import capo_firehose._operations.firehose_20150804.create_delivery_stream

            (
                output,
                http_response,
            ) = await capo_firehose._operations.firehose_20150804.create_delivery_stream.async_create_delivery_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_firehose.types.create_delivery_stream_input.CreateDeliveryStreamInput = {
            "delivery_stream_name": delivery_stream_name
        }
        if delivery_stream_type is not None:
            input_["delivery_stream_type"] = delivery_stream_type
        if direct_put_source_configuration is not None:
            input_["direct_put_source_configuration"] = direct_put_source_configuration
        if kinesis_stream_source_configuration is not None:
            input_["kinesis_stream_source_configuration"] = (
                kinesis_stream_source_configuration
            )
        if delivery_stream_encryption_configuration_input is not None:
            input_["delivery_stream_encryption_configuration_input"] = (
                delivery_stream_encryption_configuration_input
            )
        if s3_destination_configuration is not None:
            input_["s3_destination_configuration"] = s3_destination_configuration
        if extended_s3_destination_configuration is not None:
            input_["extended_s3_destination_configuration"] = (
                extended_s3_destination_configuration
            )
        if redshift_destination_configuration is not None:
            input_["redshift_destination_configuration"] = (
                redshift_destination_configuration
            )
        if elasticsearch_destination_configuration is not None:
            input_["elasticsearch_destination_configuration"] = (
                elasticsearch_destination_configuration
            )
        if amazonopensearchservice_destination_configuration is not None:
            input_["amazonopensearchservice_destination_configuration"] = (
                amazonopensearchservice_destination_configuration
            )
        if splunk_destination_configuration is not None:
            input_["splunk_destination_configuration"] = (
                splunk_destination_configuration
            )
        if http_endpoint_destination_configuration is not None:
            input_["http_endpoint_destination_configuration"] = (
                http_endpoint_destination_configuration
            )
        if tags is not None:
            input_["tags"] = tags
        if amazon_open_search_serverless_destination_configuration is not None:
            input_["amazon_open_search_serverless_destination_configuration"] = (
                amazon_open_search_serverless_destination_configuration
            )
        if msk_source_configuration is not None:
            input_["msk_source_configuration"] = msk_source_configuration
        if snowflake_destination_configuration is not None:
            input_["snowflake_destination_configuration"] = (
                snowflake_destination_configuration
            )
        if iceberg_destination_configuration is not None:
            input_["iceberg_destination_configuration"] = (
                iceberg_destination_configuration
            )
        if database_source_configuration is not None:
            input_["database_source_configuration"] = database_source_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_delivery_stream(
        self,
        delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName",
        *,
        config_overrides: Optional[AsyncFirehoseClientConfig] = None,
        allow_force_delete: Optional[
            "capo_firehose.types.boolean_object.BooleanObject"
        ] = None,
    ) -> "capo_firehose.types.delete_delivery_stream_output.DeleteDeliveryStreamOutput":
        """<p>Deletes a Firehose stream and its data.</p> <p>You can delete a Firehose stream only if it is in one of the following states: <code>ACTIVE</code>, <code>DELETING</code>, <code>CREATING_FAILED</code>, or <code>DELETING_FAILED</code>. You can't delete a Firehose stream that is in the <code>CREATING</code> state. To check the state of a Firehose stream, use <a>DescribeDeliveryStream</a>. </p> <p>DeleteDeliveryStream is an asynchronous API. When an API request to DeleteDeliveryStream succeeds, the Firehose stream is marked for deletion, and it goes into the <code>DELETING</code> state.While the Firehose stream is in the <code>DELETING</code> state, the service might continue to accept records, but it doesn't make any guarantees with respect to delivering the data. Therefore, as a best practice, first stop any applications that are sending records before you delete a Firehose stream.</p> <p>Removal of a Firehose stream that is in the <code>DELETING</code> state is a low priority operation for the service. A stream may remain in the <code>DELETING</code> state for several minutes. Therefore, as a best practice, applications should not wait for streams in the <code>DELETING</code> state to be removed. </p>

        Args:
            delivery_stream_name: <p>The name of the Firehose stream.</p>
            allow_force_delete: <p>Set this to true if you want to delete the Firehose stream even if Firehose is unable to retire the grant for the CMK. Firehose might be unable to retire the grant due to a customer error, such as when the CMK or the grant are in an invalid state. If you force deletion, you can then use the <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_RevokeGrant.html">RevokeGrant</a> operation to revoke the grant you gave to Firehose. If a failure to retire the grant happens due to an Amazon Web Services KMS issue, Firehose keeps retrying the delete operation.</p> <p>The default value is false.</p>

        Raises:
            capo_firehose.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is already in use and not available for this operation.</p>
            capo_firehose.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_firehose.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_firehose.types.delete_delivery_stream_input.DeleteDeliveryStreamInput]",
        ) -> AsyncOperationResponse[
            "capo_firehose.types.delete_delivery_stream_output.DeleteDeliveryStreamOutput"
        ]:
            import capo_firehose._operations.firehose_20150804.delete_delivery_stream

            (
                output,
                http_response,
            ) = await capo_firehose._operations.firehose_20150804.delete_delivery_stream.async_delete_delivery_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_firehose.types.delete_delivery_stream_input.DeleteDeliveryStreamInput = {
            "delivery_stream_name": delivery_stream_name
        }
        if allow_force_delete is not None:
            input_["allow_force_delete"] = allow_force_delete

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_delivery_stream(
        self,
        delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName",
        *,
        config_overrides: Optional[AsyncFirehoseClientConfig] = None,
        limit: Optional[
            "capo_firehose.types.describe_delivery_stream_input_limit.DescribeDeliveryStreamInputLimit"
        ] = None,
        exclusive_start_destination_id: Optional[
            "capo_firehose.types.destination_id.DestinationId"
        ] = None,
    ) -> "capo_firehose.types.describe_delivery_stream_output.DescribeDeliveryStreamOutput":
        """<p>Describes the specified Firehose stream and its status. For example, after your Firehose stream is created, call <code>DescribeDeliveryStream</code> to see whether the Firehose stream is <code>ACTIVE</code> and therefore ready for data to be sent to it. </p> <p>If the status of a Firehose stream is <code>CREATING_FAILED</code>, this status doesn't change, and you can't invoke <a>CreateDeliveryStream</a> again on it. However, you can invoke the <a>DeleteDeliveryStream</a> operation to delete it. If the status is <code>DELETING_FAILED</code>, you can force deletion by invoking <a>DeleteDeliveryStream</a> again but with <a>DeleteDeliveryStreamInput$AllowForceDelete</a> set to true.</p>

        Args:
            delivery_stream_name: <p>The name of the Firehose stream.</p>
            limit: <p>The limit on the number of destinations to return. You can have one destination per Firehose stream.</p>
            exclusive_start_destination_id: <p>The ID of the destination to start returning the destination information. Firehose supports one destination per Firehose stream.</p>

        Raises:
            capo_firehose.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_firehose.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_firehose.types.describe_delivery_stream_input.DescribeDeliveryStreamInput]",
        ) -> AsyncOperationResponse[
            "capo_firehose.types.describe_delivery_stream_output.DescribeDeliveryStreamOutput"
        ]:
            import capo_firehose._operations.firehose_20150804.describe_delivery_stream

            (
                output,
                http_response,
            ) = await capo_firehose._operations.firehose_20150804.describe_delivery_stream.async_describe_delivery_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_firehose.types.describe_delivery_stream_input.DescribeDeliveryStreamInput = {
            "delivery_stream_name": delivery_stream_name
        }
        if limit is not None:
            input_["limit"] = limit
        if exclusive_start_destination_id is not None:
            input_["exclusive_start_destination_id"] = exclusive_start_destination_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_delivery_streams(
        self,
        *,
        config_overrides: Optional[AsyncFirehoseClientConfig] = None,
        limit: Optional[
            "capo_firehose.types.list_delivery_streams_input_limit.ListDeliveryStreamsInputLimit"
        ] = None,
        delivery_stream_type: Optional[
            "capo_firehose.types.delivery_stream_type.DeliveryStreamType"
        ] = None,
        exclusive_start_delivery_stream_name: Optional[
            "capo_firehose.types.delivery_stream_name.DeliveryStreamName"
        ] = None,
    ) -> "capo_firehose.types.list_delivery_streams_output.ListDeliveryStreamsOutput":
        """<p>Lists your Firehose streams in alphabetical order of their names.</p> <p>The number of Firehose streams might be too large to return using a single call to <code>ListDeliveryStreams</code>. You can limit the number of Firehose streams returned, using the <code>Limit</code> parameter. To determine whether there are more delivery streams to list, check the value of <code>HasMoreDeliveryStreams</code> in the output. If there are more Firehose streams to list, you can request them by calling this operation again and setting the <code>ExclusiveStartDeliveryStreamName</code> parameter to the name of the last Firehose stream returned in the last call.</p>

        Args:
            limit: <p>The maximum number of Firehose streams to list. The default value is 10.</p>
            delivery_stream_type: <p>The Firehose stream type. This can be one of the following values:</p> <ul> <li> <p> <code>DirectPut</code>: Provider applications access the Firehose stream directly.</p> </li> <li> <p> <code>KinesisStreamAsSource</code>: The Firehose stream uses a Kinesis data stream as a source.</p> </li> </ul> <p>This parameter is optional. If this parameter is omitted, Firehose streams of all types are returned.</p>
            exclusive_start_delivery_stream_name: <p>The list of Firehose streams returned by this call to <code>ListDeliveryStreams</code> will start with the Firehose stream whose name comes alphabetically immediately after the name you specify in <code>ExclusiveStartDeliveryStreamName</code>.</p>

        Raises:
            capo_firehose.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_firehose.types.list_delivery_streams_input.ListDeliveryStreamsInput]",
        ) -> AsyncOperationResponse[
            "capo_firehose.types.list_delivery_streams_output.ListDeliveryStreamsOutput"
        ]:
            import capo_firehose._operations.firehose_20150804.list_delivery_streams

            (
                output,
                http_response,
            ) = await capo_firehose._operations.firehose_20150804.list_delivery_streams.async_list_delivery_streams(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_firehose.types.list_delivery_streams_input.ListDeliveryStreamsInput = {}
        if limit is not None:
            input_["limit"] = limit
        if delivery_stream_type is not None:
            input_["delivery_stream_type"] = delivery_stream_type
        if exclusive_start_delivery_stream_name is not None:
            input_["exclusive_start_delivery_stream_name"] = (
                exclusive_start_delivery_stream_name
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_delivery_stream(
        self,
        delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName",
        *,
        config_overrides: Optional[AsyncFirehoseClientConfig] = None,
        exclusive_start_tag_key: Optional["capo_firehose.types.tag_key.TagKey"] = None,
        limit: Optional[
            "capo_firehose.types.list_tags_for_delivery_stream_input_limit.ListTagsForDeliveryStreamInputLimit"
        ] = None,
    ) -> "capo_firehose.types.list_tags_for_delivery_stream_output.ListTagsForDeliveryStreamOutput":
        """<p>Lists the tags for the specified Firehose stream. This operation has a limit of five transactions per second per account. </p>

        Args:
            delivery_stream_name: <p>The name of the Firehose stream whose tags you want to list.</p>
            exclusive_start_tag_key: <p>The key to use as the starting point for the list of tags. If you set this parameter, <code>ListTagsForDeliveryStream</code> gets all tags that occur after <code>ExclusiveStartTagKey</code>.</p>
            limit: <p>The number of tags to return. If this number is less than the total number of tags associated with the Firehose stream, <code>HasMoreTags</code> is set to <code>true</code> in the response. To list additional tags, set <code>ExclusiveStartTagKey</code> to the last key in the response. </p>

        Raises:
            capo_firehose.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter has a value that is not valid.</p>
            capo_firehose.errors.limit_exceeded_exception.LimitExceededException: <p>You have already reached the limit for a requested resource.</p>
            capo_firehose.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_firehose.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_firehose.types.list_tags_for_delivery_stream_input.ListTagsForDeliveryStreamInput]",
        ) -> AsyncOperationResponse[
            "capo_firehose.types.list_tags_for_delivery_stream_output.ListTagsForDeliveryStreamOutput"
        ]:
            import capo_firehose._operations.firehose_20150804.list_tags_for_delivery_stream

            (
                output,
                http_response,
            ) = await capo_firehose._operations.firehose_20150804.list_tags_for_delivery_stream.async_list_tags_for_delivery_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_firehose.types.list_tags_for_delivery_stream_input.ListTagsForDeliveryStreamInput = {
            "delivery_stream_name": delivery_stream_name
        }
        if exclusive_start_tag_key is not None:
            input_["exclusive_start_tag_key"] = exclusive_start_tag_key
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_record(
        self,
        delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName",
        record: "capo_firehose.types.record.Record",
        *,
        config_overrides: Optional[AsyncFirehoseClientConfig] = None,
    ) -> "capo_firehose.types.put_record_output.PutRecordOutput":
        r"""<p>Writes a single data record into an Firehose stream. To write multiple data records into a Firehose stream, use <a>PutRecordBatch</a>. Applications using these operations are referred to as producers.</p> <p>By default, each Firehose stream can take in up to 2,000 transactions per second, 5,000 records per second, or 5 MB per second. If you use <a>PutRecord</a> and <a>PutRecordBatch</a>, the limits are an aggregate across these two operations for each Firehose stream. For more information about limits and how to request an increase, see <a href="https://docs.aws.amazon.com/firehose/latest/dev/limits.html">Amazon Firehose Limits</a>. </p> <p>Firehose accumulates and publishes a particular metric for a customer account in one minute intervals. It is possible that the bursts of incoming bytes/records ingested to a Firehose stream last only for a few seconds. Due to this, the actual spikes in the traffic might not be fully visible in the customer's 1 minute CloudWatch metrics.</p> <p>You must specify the name of the Firehose stream and the data record when using <a>PutRecord</a>. The data record consists of a data blob that can be up to 1,000 KiB in size, and any kind of data. For example, it can be a segment from a log file, geographic location data, website clickstream data, and so on.</p> <p>For multi record de-aggregation, you can not put more than 500 records even if the data blob length is less than 1000 KiB. If you include more than 500 records, the request succeeds but the record de-aggregation doesn't work as expected and transformation lambda is invoked with the complete base64 encoded data blob instead of de-aggregated base64 decoded records.</p> <p>Firehose buffers records before delivering them to the destination. To disambiguate the data blobs at the destination, a common solution is to use delimiters in the data, such as a newline (<code>\n</code>) or some other character unique within the data. This allows the consumer application to parse individual data items when reading the data from the destination.</p> <p>The <code>PutRecord</code> operation returns a <code>RecordId</code>, which is a unique string assigned to each record. Producer applications can use this ID for purposes such as auditability and investigation.</p> <p>If the <code>PutRecord</code> operation throws a <code>ServiceUnavailableException</code>, the API is automatically reinvoked (retried) 3 times. If the exception persists, it is possible that the throughput limits have been exceeded for the Firehose stream. </p> <p>Re-invoking the Put API operations (for example, PutRecord and PutRecordBatch) can result in data duplicates. For larger data assets, allow for a longer time out before retrying Put API operations.</p> <p>Data records sent to Firehose are stored for 24 hours from the time they are added to a Firehose stream as it tries to send the records to the destination. If the destination is unreachable for more than 24 hours, the data is no longer available.</p> <important> <p>Don't concatenate two or more base64 strings to form the data fields of your records. Instead, concatenate the raw data, then perform base64 encoding.</p> </important>

        Args:
            delivery_stream_name: <p>The name of the Firehose stream.</p>
            record: <p>The record.</p>

        Raises:
            capo_firehose.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter has a value that is not valid.</p>
            capo_firehose.errors.invalid_kms_resource_exception.InvalidKMSResourceException: <p>Firehose throws this exception when an attempt to put records or to start or stop Firehose stream encryption fails. This happens when the KMS service throws one of the following exception types: <code>AccessDeniedException</code>, <code>InvalidStateException</code>, <code>DisabledException</code>, or <code>NotFoundException</code>.</p>
            capo_firehose.errors.invalid_source_exception.InvalidSourceException: <p>Only requests from CloudWatch Logs are supported when CloudWatch Logs decompression is enabled.</p>
            capo_firehose.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_firehose.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation. If you continue to see the exception, throughput limits for the Firehose stream may have been exceeded. For more information about limits and how to request an increase, see <a href="https://docs.aws.amazon.com/firehose/latest/dev/limits.html">Amazon Firehose Limits</a>.</p>
            capo_firehose.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_firehose.types.put_record_input.PutRecordInput]",
        ) -> AsyncOperationResponse[
            "capo_firehose.types.put_record_output.PutRecordOutput"
        ]:
            import capo_firehose._operations.firehose_20150804.put_record

            (
                output,
                http_response,
            ) = await capo_firehose._operations.firehose_20150804.put_record.async_put_record(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_firehose.types.put_record_input.PutRecordInput = {
            "delivery_stream_name": delivery_stream_name,
            "record": record,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_record_batch(
        self,
        delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName",
        records: "capo_firehose.types.put_record_batch_request_entry_list.PutRecordBatchRequestEntryList",
        *,
        config_overrides: Optional[AsyncFirehoseClientConfig] = None,
    ) -> "capo_firehose.types.put_record_batch_output.PutRecordBatchOutput":
        r"""<p>Writes multiple data records into a Firehose stream in a single call, which can achieve higher throughput per producer than when writing single records. To write single data records into a Firehose stream, use <a>PutRecord</a>. Applications using these operations are referred to as producers.</p> <p>Firehose accumulates and publishes a particular metric for a customer account in one minute intervals. It is possible that the bursts of incoming bytes/records ingested to a Firehose stream last only for a few seconds. Due to this, the actual spikes in the traffic might not be fully visible in the customer's 1 minute CloudWatch metrics.</p> <p>For information about service quota, see <a href="https://docs.aws.amazon.com/firehose/latest/dev/limits.html">Amazon Firehose Quota</a>.</p> <p>Each <a>PutRecordBatch</a> request supports up to 500 records. Each record in the request can be as large as 1,000 KB (before base64 encoding), up to a limit of 4 MB for the entire request. These limits cannot be changed.</p> <p>You must specify the name of the Firehose stream and the data record when using <a>PutRecord</a>. The data record consists of a data blob that can be up to 1,000 KB in size, and any kind of data. For example, it could be a segment from a log file, geographic location data, website clickstream data, and so on.</p> <p>For multi record de-aggregation, you can not put more than 500 records even if the data blob length is less than 1000 KiB. If you include more than 500 records, the request succeeds but the record de-aggregation doesn't work as expected and transformation lambda is invoked with the complete base64 encoded data blob instead of de-aggregated base64 decoded records.</p> <p>Firehose buffers records before delivering them to the destination. To disambiguate the data blobs at the destination, a common solution is to use delimiters in the data, such as a newline (<code>\n</code>) or some other character unique within the data. This allows the consumer application to parse individual data items when reading the data from the destination.</p> <p>The <a>PutRecordBatch</a> response includes a count of failed records, <code>FailedPutCount</code>, and an array of responses, <code>RequestResponses</code>. Even if the <a>PutRecordBatch</a> call succeeds, the value of <code>FailedPutCount</code> may be greater than 0, indicating that there are records for which the operation didn't succeed. Each entry in the <code>RequestResponses</code> array provides additional information about the processed record. It directly correlates with a record in the request array using the same ordering, from the top to the bottom. The response array always includes the same number of records as the request array. <code>RequestResponses</code> includes both successfully and unsuccessfully processed records. Firehose tries to process all records in each <a>PutRecordBatch</a> request. A single record failure does not stop the processing of subsequent records. </p> <p>A successfully processed record includes a <code>RecordId</code> value, which is unique for the record. An unsuccessfully processed record includes <code>ErrorCode</code> and <code>ErrorMessage</code> values. <code>ErrorCode</code> reflects the type of error, and is one of the following values: <code>ServiceUnavailableException</code> or <code>InternalFailure</code>. <code>ErrorMessage</code> provides more detailed information about the error.</p> <p>If there is an internal server error or a timeout, the write might have completed or it might have failed. If <code>FailedPutCount</code> is greater than 0, retry the request, resending only those records that might have failed processing. This minimizes the possible duplicate records and also reduces the total bytes sent (and corresponding charges). We recommend that you handle any duplicates at the destination.</p> <p>If <a>PutRecordBatch</a> throws <code>ServiceUnavailableException</code>, the API is automatically reinvoked (retried) 3 times. If the exception persists, it is possible that the throughput limits have been exceeded for the Firehose stream.</p> <p>Re-invoking the Put API operations (for example, PutRecord and PutRecordBatch) can result in data duplicates. For larger data assets, allow for a longer time out before retrying Put API operations.</p> <p>Data records sent to Firehose are stored for 24 hours from the time they are added to a Firehose stream as it attempts to send the records to the destination. If the destination is unreachable for more than 24 hours, the data is no longer available.</p> <important> <p>Don't concatenate two or more base64 strings to form the data fields of your records. Instead, concatenate the raw data, then perform base64 encoding.</p> </important>

        Args:
            delivery_stream_name: <p>The name of the Firehose stream.</p>
            records: <p>One or more records.</p>

        Raises:
            capo_firehose.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter has a value that is not valid.</p>
            capo_firehose.errors.invalid_kms_resource_exception.InvalidKMSResourceException: <p>Firehose throws this exception when an attempt to put records or to start or stop Firehose stream encryption fails. This happens when the KMS service throws one of the following exception types: <code>AccessDeniedException</code>, <code>InvalidStateException</code>, <code>DisabledException</code>, or <code>NotFoundException</code>.</p>
            capo_firehose.errors.invalid_source_exception.InvalidSourceException: <p>Only requests from CloudWatch Logs are supported when CloudWatch Logs decompression is enabled.</p>
            capo_firehose.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_firehose.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation. If you continue to see the exception, throughput limits for the Firehose stream may have been exceeded. For more information about limits and how to request an increase, see <a href="https://docs.aws.amazon.com/firehose/latest/dev/limits.html">Amazon Firehose Limits</a>.</p>
            capo_firehose.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_firehose.types.put_record_batch_input.PutRecordBatchInput]",
        ) -> AsyncOperationResponse[
            "capo_firehose.types.put_record_batch_output.PutRecordBatchOutput"
        ]:
            import capo_firehose._operations.firehose_20150804.put_record_batch

            (
                output,
                http_response,
            ) = await capo_firehose._operations.firehose_20150804.put_record_batch.async_put_record_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_firehose.types.put_record_batch_input.PutRecordBatchInput = {
            "delivery_stream_name": delivery_stream_name,
            "records": records,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_delivery_stream_encryption(
        self,
        delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName",
        *,
        config_overrides: Optional[AsyncFirehoseClientConfig] = None,
        delivery_stream_encryption_configuration_input: Optional[
            "capo_firehose.types.delivery_stream_encryption_configuration_input.DeliveryStreamEncryptionConfigurationInput"
        ] = None,
    ) -> "capo_firehose.types.start_delivery_stream_encryption_output.StartDeliveryStreamEncryptionOutput":
        """<p>Enables server-side encryption (SSE) for the Firehose stream. </p> <p>This operation is asynchronous. It returns immediately. When you invoke it, Firehose first sets the encryption status of the stream to <code>ENABLING</code>, and then to <code>ENABLED</code>. The encryption status of a Firehose stream is the <code>Status</code> property in <a>DeliveryStreamEncryptionConfiguration</a>. If the operation fails, the encryption status changes to <code>ENABLING_FAILED</code>. You can continue to read and write data to your Firehose stream while the encryption status is <code>ENABLING</code>, but the data is not encrypted. It can take up to 5 seconds after the encryption status changes to <code>ENABLED</code> before all records written to the Firehose stream are encrypted. To find out whether a record or a batch of records was encrypted, check the response elements <a>PutRecordOutput$Encrypted</a> and <a>PutRecordBatchOutput$Encrypted</a>, respectively.</p> <p>To check the encryption status of a Firehose stream, use <a>DescribeDeliveryStream</a>.</p> <p>Even if encryption is currently enabled for a Firehose stream, you can still invoke this operation on it to change the ARN of the CMK or both its type and ARN. If you invoke this method to change the CMK, and the old CMK is of type <code>CUSTOMER_MANAGED_CMK</code>, Firehose schedules the grant it had on the old CMK for retirement. If the new CMK is of type <code>CUSTOMER_MANAGED_CMK</code>, Firehose creates a grant that enables it to use the new CMK to encrypt and decrypt data and to manage the grant.</p> <p>For the KMS grant creation to be successful, the Firehose API operations <code>StartDeliveryStreamEncryption</code> and <code>CreateDeliveryStream</code> should not be called with session credentials that are more than 6 hours old.</p> <p>If a Firehose stream already has encryption enabled and then you invoke this operation to change the ARN of the CMK or both its type and ARN and you get <code>ENABLING_FAILED</code>, this only means that the attempt to change the CMK failed. In this case, encryption remains enabled with the old CMK.</p> <p>If the encryption status of your Firehose stream is <code>ENABLING_FAILED</code>, you can invoke this operation again with a valid CMK. The CMK must be enabled and the key policy mustn't explicitly deny the permission for Firehose to invoke KMS encrypt and decrypt operations.</p> <p>You can enable SSE for a Firehose stream only if it's a Firehose stream that uses <code>DirectPut</code> as its source. </p> <p>The <code>StartDeliveryStreamEncryption</code> and <code>StopDeliveryStreamEncryption</code> operations have a combined limit of 25 calls per Firehose stream per 24 hours. For example, you reach the limit if you call <code>StartDeliveryStreamEncryption</code> 13 times and <code>StopDeliveryStreamEncryption</code> 12 times for the same Firehose stream in a 24-hour period.</p>

        Args:
            delivery_stream_name: <p>The name of the Firehose stream for which you want to enable server-side encryption (SSE).</p>
            delivery_stream_encryption_configuration_input: <p>Used to specify the type and Amazon Resource Name (ARN) of the KMS key needed for Server-Side Encryption (SSE).</p>

        Raises:
            capo_firehose.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter has a value that is not valid.</p>
            capo_firehose.errors.invalid_kms_resource_exception.InvalidKMSResourceException: <p>Firehose throws this exception when an attempt to put records or to start or stop Firehose stream encryption fails. This happens when the KMS service throws one of the following exception types: <code>AccessDeniedException</code>, <code>InvalidStateException</code>, <code>DisabledException</code>, or <code>NotFoundException</code>.</p>
            capo_firehose.errors.limit_exceeded_exception.LimitExceededException: <p>You have already reached the limit for a requested resource.</p>
            capo_firehose.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is already in use and not available for this operation.</p>
            capo_firehose.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_firehose.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_firehose.types.start_delivery_stream_encryption_input.StartDeliveryStreamEncryptionInput]",
        ) -> AsyncOperationResponse[
            "capo_firehose.types.start_delivery_stream_encryption_output.StartDeliveryStreamEncryptionOutput"
        ]:
            import capo_firehose._operations.firehose_20150804.start_delivery_stream_encryption

            (
                output,
                http_response,
            ) = await capo_firehose._operations.firehose_20150804.start_delivery_stream_encryption.async_start_delivery_stream_encryption(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_firehose.types.start_delivery_stream_encryption_input.StartDeliveryStreamEncryptionInput = {
            "delivery_stream_name": delivery_stream_name
        }
        if delivery_stream_encryption_configuration_input is not None:
            input_["delivery_stream_encryption_configuration_input"] = (
                delivery_stream_encryption_configuration_input
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_delivery_stream_encryption(
        self,
        delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName",
        *,
        config_overrides: Optional[AsyncFirehoseClientConfig] = None,
    ) -> "capo_firehose.types.stop_delivery_stream_encryption_output.StopDeliveryStreamEncryptionOutput":
        """<p>Disables server-side encryption (SSE) for the Firehose stream. </p> <p>This operation is asynchronous. It returns immediately. When you invoke it, Firehose first sets the encryption status of the stream to <code>DISABLING</code>, and then to <code>DISABLED</code>. You can continue to read and write data to your stream while its status is <code>DISABLING</code>. It can take up to 5 seconds after the encryption status changes to <code>DISABLED</code> before all records written to the Firehose stream are no longer subject to encryption. To find out whether a record or a batch of records was encrypted, check the response elements <a>PutRecordOutput$Encrypted</a> and <a>PutRecordBatchOutput$Encrypted</a>, respectively.</p> <p>To check the encryption state of a Firehose stream, use <a>DescribeDeliveryStream</a>. </p> <p>If SSE is enabled using a customer managed CMK and then you invoke <code>StopDeliveryStreamEncryption</code>, Firehose schedules the related KMS grant for retirement and then retires it after it ensures that it is finished delivering records to the destination.</p> <p>The <code>StartDeliveryStreamEncryption</code> and <code>StopDeliveryStreamEncryption</code> operations have a combined limit of 25 calls per Firehose stream per 24 hours. For example, you reach the limit if you call <code>StartDeliveryStreamEncryption</code> 13 times and <code>StopDeliveryStreamEncryption</code> 12 times for the same Firehose stream in a 24-hour period.</p>

        Args:
            delivery_stream_name: <p>The name of the Firehose stream for which you want to disable server-side encryption (SSE).</p>

        Raises:
            capo_firehose.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter has a value that is not valid.</p>
            capo_firehose.errors.limit_exceeded_exception.LimitExceededException: <p>You have already reached the limit for a requested resource.</p>
            capo_firehose.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is already in use and not available for this operation.</p>
            capo_firehose.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_firehose.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_firehose.types.stop_delivery_stream_encryption_input.StopDeliveryStreamEncryptionInput]",
        ) -> AsyncOperationResponse[
            "capo_firehose.types.stop_delivery_stream_encryption_output.StopDeliveryStreamEncryptionOutput"
        ]:
            import capo_firehose._operations.firehose_20150804.stop_delivery_stream_encryption

            (
                output,
                http_response,
            ) = await capo_firehose._operations.firehose_20150804.stop_delivery_stream_encryption.async_stop_delivery_stream_encryption(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_firehose.types.stop_delivery_stream_encryption_input.StopDeliveryStreamEncryptionInput = {
            "delivery_stream_name": delivery_stream_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_delivery_stream(
        self,
        delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName",
        tags: "capo_firehose.types.tag_delivery_stream_input_tag_list.TagDeliveryStreamInputTagList",
        *,
        config_overrides: Optional[AsyncFirehoseClientConfig] = None,
    ) -> "capo_firehose.types.tag_delivery_stream_output.TagDeliveryStreamOutput":
        """<p>Adds or updates tags for the specified Firehose stream. A tag is a key-value pair that you can define and assign to Amazon Web Services resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. Tags are metadata. For example, you can add friendly names and descriptions or other types of information that can help you distinguish the Firehose stream. For more information about tags, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html">Using Cost Allocation Tags</a> in the <i>Amazon Web Services Billing and Cost Management User Guide</i>. </p> <p>Each Firehose stream can have up to 50 tags. </p> <p>This operation has a limit of five transactions per second per account. </p>

        Args:
            delivery_stream_name: <p>The name of the Firehose stream to which you want to add the tags.</p>
            tags: <p>A set of key-value pairs to use to create the tags.</p>

        Raises:
            capo_firehose.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter has a value that is not valid.</p>
            capo_firehose.errors.limit_exceeded_exception.LimitExceededException: <p>You have already reached the limit for a requested resource.</p>
            capo_firehose.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is already in use and not available for this operation.</p>
            capo_firehose.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_firehose.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_firehose.types.tag_delivery_stream_input.TagDeliveryStreamInput]",
        ) -> AsyncOperationResponse[
            "capo_firehose.types.tag_delivery_stream_output.TagDeliveryStreamOutput"
        ]:
            import capo_firehose._operations.firehose_20150804.tag_delivery_stream

            (
                output,
                http_response,
            ) = await capo_firehose._operations.firehose_20150804.tag_delivery_stream.async_tag_delivery_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_firehose.types.tag_delivery_stream_input.TagDeliveryStreamInput = {
            "delivery_stream_name": delivery_stream_name,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_delivery_stream(
        self,
        delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName",
        tag_keys: "capo_firehose.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncFirehoseClientConfig] = None,
    ) -> "capo_firehose.types.untag_delivery_stream_output.UntagDeliveryStreamOutput":
        """<p>Removes tags from the specified Firehose stream. Removed tags are deleted, and you can't recover them after this operation successfully completes.</p> <p>If you specify a tag that doesn't exist, the operation ignores it.</p> <p>This operation has a limit of five transactions per second per account. </p>

        Args:
            delivery_stream_name: <p>The name of the Firehose stream.</p>
            tag_keys: <p>A list of tag keys. Each corresponding tag is removed from the delivery stream.</p>

        Raises:
            capo_firehose.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter has a value that is not valid.</p>
            capo_firehose.errors.limit_exceeded_exception.LimitExceededException: <p>You have already reached the limit for a requested resource.</p>
            capo_firehose.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is already in use and not available for this operation.</p>
            capo_firehose.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_firehose.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_firehose.types.untag_delivery_stream_input.UntagDeliveryStreamInput]",
        ) -> AsyncOperationResponse[
            "capo_firehose.types.untag_delivery_stream_output.UntagDeliveryStreamOutput"
        ]:
            import capo_firehose._operations.firehose_20150804.untag_delivery_stream

            (
                output,
                http_response,
            ) = await capo_firehose._operations.firehose_20150804.untag_delivery_stream.async_untag_delivery_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_firehose.types.untag_delivery_stream_input.UntagDeliveryStreamInput = {
            "delivery_stream_name": delivery_stream_name,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_destination(
        self,
        delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName",
        current_delivery_stream_version_id: "capo_firehose.types.delivery_stream_version_id.DeliveryStreamVersionId",
        destination_id: "capo_firehose.types.destination_id.DestinationId",
        *,
        config_overrides: Optional[AsyncFirehoseClientConfig] = None,
        s3_destination_update: Optional[
            "capo_firehose.types.s3_destination_update.S3DestinationUpdate"
        ] = None,
        extended_s3_destination_update: Optional[
            "capo_firehose.types.extended_s3_destination_update.ExtendedS3DestinationUpdate"
        ] = None,
        redshift_destination_update: Optional[
            "capo_firehose.types.redshift_destination_update.RedshiftDestinationUpdate"
        ] = None,
        elasticsearch_destination_update: Optional[
            "capo_firehose.types.elasticsearch_destination_update.ElasticsearchDestinationUpdate"
        ] = None,
        amazonopensearchservice_destination_update: Optional[
            "capo_firehose.types.amazonopensearchservice_destination_update.AmazonopensearchserviceDestinationUpdate"
        ] = None,
        splunk_destination_update: Optional[
            "capo_firehose.types.splunk_destination_update.SplunkDestinationUpdate"
        ] = None,
        http_endpoint_destination_update: Optional[
            "capo_firehose.types.http_endpoint_destination_update.HttpEndpointDestinationUpdate"
        ] = None,
        amazon_open_search_serverless_destination_update: Optional[
            "capo_firehose.types.amazon_open_search_serverless_destination_update.AmazonOpenSearchServerlessDestinationUpdate"
        ] = None,
        snowflake_destination_update: Optional[
            "capo_firehose.types.snowflake_destination_update.SnowflakeDestinationUpdate"
        ] = None,
        iceberg_destination_update: Optional[
            "capo_firehose.types.iceberg_destination_update.IcebergDestinationUpdate"
        ] = None,
    ) -> "capo_firehose.types.update_destination_output.UpdateDestinationOutput":
        """<p>Updates the specified destination of the specified Firehose stream.</p> <p>Use this operation to change the destination type (for example, to replace the Amazon S3 destination with Amazon Redshift) or change the parameters associated with a destination (for example, to change the bucket name of the Amazon S3 destination). The update might not occur immediately. The target Firehose stream remains active while the configurations are updated, so data writes to the Firehose stream can continue during this process. The updated configurations are usually effective within a few minutes.</p> <p>Switching between Amazon OpenSearch Service and other services is not supported. For an Amazon OpenSearch Service destination, you can only update to another Amazon OpenSearch Service destination.</p> <p>If the destination type is the same, Firehose merges the configuration parameters specified with the destination configuration that already exists on the delivery stream. If any of the parameters are not specified in the call, the existing values are retained. For example, in the Amazon S3 destination, if <a>EncryptionConfiguration</a> is not specified, then the existing <code>EncryptionConfiguration</code> is maintained on the destination.</p> <p>If the destination type is not the same, for example, changing the destination from Amazon S3 to Amazon Redshift, Firehose does not merge any parameters. In this case, all parameters must be specified.</p> <p>Firehose uses <code>CurrentDeliveryStreamVersionId</code> to avoid race conditions and conflicting merges. This is a required field, and the service updates the configuration only if the existing configuration has a version ID that matches. After the update is applied successfully, the version ID is updated, and can be retrieved using <a>DescribeDeliveryStream</a>. Use the new version ID to set <code>CurrentDeliveryStreamVersionId</code> in the next call.</p>

        Args:
            delivery_stream_name: <p>The name of the Firehose stream.</p>
            current_delivery_stream_version_id: <p>Obtain this value from the <code>VersionId</code> result of <a>DeliveryStreamDescription</a>. This value is required, and helps the service perform conditional operations. For example, if there is an interleaving update and this value is null, then the update destination fails. After the update is successful, the <code>VersionId</code> value is updated. The service then performs a merge of the old configuration with the new configuration.</p>
            destination_id: <p>The ID of the destination.</p>
            s3_destination_update: <p>[Deprecated] Describes an update for a destination in Amazon S3.</p>
            extended_s3_destination_update: <p>Describes an update for a destination in Amazon S3.</p>
            redshift_destination_update: <p>Describes an update for a destination in Amazon Redshift.</p>
            elasticsearch_destination_update: <p>Describes an update for a destination in Amazon OpenSearch Service.</p>
            amazonopensearchservice_destination_update: <p>Describes an update for a destination in Amazon OpenSearch Service.</p>
            splunk_destination_update: <p>Describes an update for a destination in Splunk.</p>
            http_endpoint_destination_update: <p>Describes an update to the specified HTTP endpoint destination.</p>
            amazon_open_search_serverless_destination_update: <p>Describes an update for a destination in the Serverless offering for Amazon OpenSearch Service.</p>
            snowflake_destination_update: <p>Update to the Snowflake destination configuration settings.</p>
            iceberg_destination_update: <p> Describes an update for a destination in Apache Iceberg Tables. </p>

        Raises:
            capo_firehose.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification has already happened. Fetch <code>VersionId</code> again and use it to update the destination.</p>
            capo_firehose.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter has a value that is not valid.</p>
            capo_firehose.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is already in use and not available for this operation.</p>
            capo_firehose.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_firehose.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_firehose.types.update_destination_input.UpdateDestinationInput]",
        ) -> AsyncOperationResponse[
            "capo_firehose.types.update_destination_output.UpdateDestinationOutput"
        ]:
            import capo_firehose._operations.firehose_20150804.update_destination

            (
                output,
                http_response,
            ) = await capo_firehose._operations.firehose_20150804.update_destination.async_update_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_firehose.types.update_destination_input.UpdateDestinationInput = {
            "delivery_stream_name": delivery_stream_name,
            "current_delivery_stream_version_id": current_delivery_stream_version_id,
            "destination_id": destination_id,
        }
        if s3_destination_update is not None:
            input_["s3_destination_update"] = s3_destination_update
        if extended_s3_destination_update is not None:
            input_["extended_s3_destination_update"] = extended_s3_destination_update
        if redshift_destination_update is not None:
            input_["redshift_destination_update"] = redshift_destination_update
        if elasticsearch_destination_update is not None:
            input_["elasticsearch_destination_update"] = (
                elasticsearch_destination_update
            )
        if amazonopensearchservice_destination_update is not None:
            input_["amazonopensearchservice_destination_update"] = (
                amazonopensearchservice_destination_update
            )
        if splunk_destination_update is not None:
            input_["splunk_destination_update"] = splunk_destination_update
        if http_endpoint_destination_update is not None:
            input_["http_endpoint_destination_update"] = (
                http_endpoint_destination_update
            )
        if amazon_open_search_serverless_destination_update is not None:
            input_["amazon_open_search_serverless_destination_update"] = (
                amazon_open_search_serverless_destination_update
            )
        if snowflake_destination_update is not None:
            input_["snowflake_destination_update"] = snowflake_destination_update
        if iceberg_destination_update is not None:
            input_["iceberg_destination_update"] = iceberg_destination_update

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
