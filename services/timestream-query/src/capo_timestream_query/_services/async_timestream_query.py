"""Generated from Smithy shape ``com.amazonaws.timestreamquery#Timestream_20181101``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_timestream_query._auth._signers
import capo_timestream_query._auth._sigv4
from capo_timestream_query._auth._identity import Credentials
from capo_timestream_query._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_timestream_query._auth._zapros_handler import AuthMiddleware
from capo_timestream_query._pagination import resolve_path as _resolve_path
from capo_timestream_query._services._aws_config import aaws_config
from capo_timestream_query._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_timestream_query.types.amazon_resource_name
    import capo_timestream_query.types.cancel_query_request
    import capo_timestream_query.types.cancel_query_response
    import capo_timestream_query.types.client_request_token
    import capo_timestream_query.types.client_token
    import capo_timestream_query.types.create_scheduled_query_request
    import capo_timestream_query.types.create_scheduled_query_response
    import capo_timestream_query.types.delete_scheduled_query_request
    import capo_timestream_query.types.describe_account_settings_request
    import capo_timestream_query.types.describe_account_settings_response
    import capo_timestream_query.types.describe_endpoints_request
    import capo_timestream_query.types.describe_endpoints_response
    import capo_timestream_query.types.describe_scheduled_query_request
    import capo_timestream_query.types.describe_scheduled_query_response
    import capo_timestream_query.types.error_report_configuration
    import capo_timestream_query.types.execute_scheduled_query_request
    import capo_timestream_query.types.list_scheduled_queries_request
    import capo_timestream_query.types.list_scheduled_queries_response
    import capo_timestream_query.types.list_tags_for_resource_request
    import capo_timestream_query.types.list_tags_for_resource_response
    import capo_timestream_query.types.max_query_capacity
    import capo_timestream_query.types.max_query_results
    import capo_timestream_query.types.max_scheduled_queries_results
    import capo_timestream_query.types.max_tags_for_resource_result
    import capo_timestream_query.types.next_scheduled_queries_results_token
    import capo_timestream_query.types.next_tags_for_resource_results_token
    import capo_timestream_query.types.notification_configuration
    import capo_timestream_query.types.nullable_boolean
    import capo_timestream_query.types.pagination_token
    import capo_timestream_query.types.prepare_query_request
    import capo_timestream_query.types.prepare_query_response
    import capo_timestream_query.types.query_compute_request
    import capo_timestream_query.types.query_id
    import capo_timestream_query.types.query_insights
    import capo_timestream_query.types.query_pricing_model
    import capo_timestream_query.types.query_request
    import capo_timestream_query.types.query_response
    import capo_timestream_query.types.query_string
    import capo_timestream_query.types.row
    import capo_timestream_query.types.schedule_configuration
    import capo_timestream_query.types.scheduled_query
    import capo_timestream_query.types.scheduled_query_insights
    import capo_timestream_query.types.scheduled_query_name
    import capo_timestream_query.types.scheduled_query_state
    import capo_timestream_query.types.string_value2048
    import capo_timestream_query.types.tag
    import capo_timestream_query.types.tag_key_list
    import capo_timestream_query.types.tag_list
    import capo_timestream_query.types.tag_resource_request
    import capo_timestream_query.types.tag_resource_response
    import capo_timestream_query.types.target_configuration
    import capo_timestream_query.types.time
    import capo_timestream_query.types.untag_resource_request
    import capo_timestream_query.types.untag_resource_response
    import capo_timestream_query.types.update_account_settings_request
    import capo_timestream_query.types.update_account_settings_response
    import capo_timestream_query.types.update_scheduled_query_request


class AsyncTimestreamQueryClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncTimestreamQueryClient:
    """A client for the ``TimestreamQuery`` service.

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
        self._config = AsyncTimestreamQueryClientConfig(
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
        self, config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncTimestreamQueryClientConfig = config_overrides or {}
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

    async def cancel_query(
        self,
        query_id: "capo_timestream_query.types.query_id.QueryId",
        *,
        config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None,
    ) -> "capo_timestream_query.types.cancel_query_response.CancelQueryResponse":
        """<p> Cancels a query that has been issued. Cancellation is provided only if the query has not completed running before the cancellation request was issued. Because cancellation is an idempotent operation, subsequent cancellation requests will return a <code>CancellationMessage</code>, indicating that the query has already been canceled. See <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.cancel-query.html">code sample</a> for details. </p>

        Args:
            query_id: <p> The ID of the query that needs to be cancelled. <code>QueryID</code> is returned as part of the query result. </p>

        Raises:
            capo_timestream_query.errors.access_denied_exception.AccessDeniedException: <p>You do not have the necessary permissions to access the account settings.</p>
            capo_timestream_query.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_timestream_query.errors.invalid_endpoint_exception.InvalidEndpointException: <p>The requested endpoint is invalid.</p>
            capo_timestream_query.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to excessive requests.</p>
            capo_timestream_query.errors.validation_exception.ValidationException: <p> Invalid or malformed request. </p>
            capo_timestream_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_query.types.cancel_query_request.CancelQueryRequest]",
        ) -> AsyncOperationResponse[
            "capo_timestream_query.types.cancel_query_response.CancelQueryResponse"
        ]:
            import capo_timestream_query._operations.timestream_20181101.cancel_query

            (
                output,
                http_response,
            ) = await capo_timestream_query._operations.timestream_20181101.cancel_query.async_cancel_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_query.types.cancel_query_request.CancelQueryRequest = {
            "query_id": query_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_scheduled_query(
        self,
        name: "capo_timestream_query.types.scheduled_query_name.ScheduledQueryName",
        query_string: "capo_timestream_query.types.query_string.QueryString",
        schedule_configuration: "capo_timestream_query.types.schedule_configuration.ScheduleConfiguration",
        notification_configuration: "capo_timestream_query.types.notification_configuration.NotificationConfiguration",
        scheduled_query_execution_role_arn: "capo_timestream_query.types.amazon_resource_name.AmazonResourceName",
        error_report_configuration: "capo_timestream_query.types.error_report_configuration.ErrorReportConfiguration",
        *,
        config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None,
        target_configuration: Optional[
            "capo_timestream_query.types.target_configuration.TargetConfiguration"
        ] = None,
        client_token: Optional[
            "capo_timestream_query.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_timestream_query.types.tag_list.TagList"] = None,
        kms_key_id: Optional[
            "capo_timestream_query.types.string_value2048.StringValue2048"
        ] = None,
    ) -> "capo_timestream_query.types.create_scheduled_query_response.CreateScheduledQueryResponse":
        """<p> Create a scheduled query that will be run on your behalf at the configured schedule. Timestream assumes the execution role provided as part of the <code>ScheduledQueryExecutionRoleArn</code> parameter to run the query. You can use the <code>NotificationConfiguration</code> parameter to configure notification for your scheduled query operations.</p>

        Args:
            name: <p>Name of the scheduled query.</p>
            query_string: <p>The query string to run. Parameter names can be specified in the query string <code>@</code> character followed by an identifier. The named Parameter <code>@scheduled_runtime</code> is reserved and can be used in the query to get the time at which the query is scheduled to run.</p> <p>The timestamp calculated according to the ScheduleConfiguration parameter, will be the value of <code>@scheduled_runtime</code> paramater for each query run. For example, consider an instance of a scheduled query executing on 2021-12-01 00:00:00. For this instance, the <code>@scheduled_runtime</code> parameter is initialized to the timestamp 2021-12-01 00:00:00 when invoking the query.</p>
            schedule_configuration: <p>The schedule configuration for the query.</p>
            notification_configuration: <p>Notification configuration for the scheduled query. A notification is sent by Timestream when a query run finishes, when the state is updated or when you delete it. </p>
            target_configuration: <p>Configuration used for writing the result of a query.</p>
            client_token: <p>Using a ClientToken makes the call to CreateScheduledQuery idempotent, in other words, making the same request repeatedly will produce the same result. Making multiple identical CreateScheduledQuery requests has the same effect as making a single request. </p> <ul> <li> <p> If CreateScheduledQuery is called without a <code>ClientToken</code>, the Query SDK generates a <code>ClientToken</code> on your behalf.</p> </li> <li> <p> After 8 hours, any request with the same <code>ClientToken</code> is treated as a new request. </p> </li> </ul>
            scheduled_query_execution_role_arn: <p>The ARN for the IAM role that Timestream will assume when running the scheduled query. </p>
            tags: <p>A list of key-value pairs to label the scheduled query.</p>
            kms_key_id: <p>The Amazon KMS key used to encrypt the scheduled query resource, at-rest. If the Amazon KMS key is not specified, the scheduled query resource will be encrypted with a Timestream owned Amazon KMS key. To specify a KMS key, use the key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix the name with <i>alias/</i> </p> <p>If ErrorReportConfiguration uses <code>SSE_KMS</code> as encryption type, the same KmsKeyId is used to encrypt the error report at rest.</p>
            error_report_configuration: <p>Configuration for error reporting. Error reports will be generated when a problem is encountered when writing the query results. </p>

        Raises:
            capo_timestream_query.errors.access_denied_exception.AccessDeniedException: <p>You do not have the necessary permissions to access the account settings.</p>
            capo_timestream_query.errors.conflict_exception.ConflictException: <p> Unable to poll results for a cancelled query. </p>
            capo_timestream_query.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_timestream_query.errors.invalid_endpoint_exception.InvalidEndpointException: <p>The requested endpoint is invalid.</p>
            capo_timestream_query.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_timestream_query.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to excessive requests.</p>
            capo_timestream_query.errors.validation_exception.ValidationException: <p> Invalid or malformed request. </p>
            capo_timestream_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_query.types.create_scheduled_query_request.CreateScheduledQueryRequest]",
        ) -> AsyncOperationResponse[
            "capo_timestream_query.types.create_scheduled_query_response.CreateScheduledQueryResponse"
        ]:
            import capo_timestream_query._operations.timestream_20181101.create_scheduled_query

            (
                output,
                http_response,
            ) = await capo_timestream_query._operations.timestream_20181101.create_scheduled_query.async_create_scheduled_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_query.types.create_scheduled_query_request.CreateScheduledQueryRequest = {
            "name": name,
            "query_string": query_string,
            "schedule_configuration": schedule_configuration,
            "notification_configuration": notification_configuration,
            "scheduled_query_execution_role_arn": scheduled_query_execution_role_arn,
            "error_report_configuration": error_report_configuration,
        }
        if target_configuration is not None:
            input_["target_configuration"] = target_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_scheduled_query(
        self,
        scheduled_query_arn: "capo_timestream_query.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None,
    ) -> None:
        """<p>Deletes a given scheduled query. This is an irreversible operation. </p>

        Args:
            scheduled_query_arn: <p>The ARN of the scheduled query. </p>

        Raises:
            capo_timestream_query.errors.access_denied_exception.AccessDeniedException: <p>You do not have the necessary permissions to access the account settings.</p>
            capo_timestream_query.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_timestream_query.errors.invalid_endpoint_exception.InvalidEndpointException: <p>The requested endpoint is invalid.</p>
            capo_timestream_query.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_timestream_query.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to excessive requests.</p>
            capo_timestream_query.errors.validation_exception.ValidationException: <p> Invalid or malformed request. </p>
            capo_timestream_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_query.types.delete_scheduled_query_request.DeleteScheduledQueryRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_timestream_query._operations.timestream_20181101.delete_scheduled_query

            (
                output,
                http_response,
            ) = await capo_timestream_query._operations.timestream_20181101.delete_scheduled_query.async_delete_scheduled_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_query.types.delete_scheduled_query_request.DeleteScheduledQueryRequest = {
            "scheduled_query_arn": scheduled_query_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_account_settings(
        self, *, config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None
    ) -> "capo_timestream_query.types.describe_account_settings_response.DescribeAccountSettingsResponse":
        """<p>Describes the settings for your account that include the query pricing model and the configured maximum TCUs the service can use for your query workload.</p> <p>You're charged only for the duration of compute units used for your workloads.</p>

        Raises:
            capo_timestream_query.errors.access_denied_exception.AccessDeniedException: <p>You do not have the necessary permissions to access the account settings.</p>
            capo_timestream_query.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_timestream_query.errors.invalid_endpoint_exception.InvalidEndpointException: <p>The requested endpoint is invalid.</p>
            capo_timestream_query.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to excessive requests.</p>
            capo_timestream_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_query.types.describe_account_settings_request.DescribeAccountSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_timestream_query.types.describe_account_settings_response.DescribeAccountSettingsResponse"
        ]:
            import capo_timestream_query._operations.timestream_20181101.describe_account_settings

            (
                output,
                http_response,
            ) = await capo_timestream_query._operations.timestream_20181101.describe_account_settings.async_describe_account_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_query.types.describe_account_settings_request.DescribeAccountSettingsRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_endpoints(
        self, *, config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None
    ) -> "capo_timestream_query.types.describe_endpoints_response.DescribeEndpointsResponse":
        """<p>DescribeEndpoints returns a list of available endpoints to make Timestream API calls against. This API is available through both Write and Query.</p> <p>Because the Timestream SDKs are designed to transparently work with the service’s architecture, including the management and mapping of the service endpoints, <i>it is not recommended that you use this API unless</i>:</p> <ul> <li> <p>You are using <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/VPCEndpoints">VPC endpoints (Amazon Web Services PrivateLink) with Timestream </a> </p> </li> <li> <p>Your application uses a programming language that does not yet have SDK support</p> </li> <li> <p>You require better control over the client-side implementation</p> </li> </ul> <p>For detailed information on how and when to use and implement DescribeEndpoints, see <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/Using.API.html#Using-API.endpoint-discovery">The Endpoint Discovery Pattern</a>.</p>

        Raises:
            capo_timestream_query.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_timestream_query.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to excessive requests.</p>
            capo_timestream_query.errors.validation_exception.ValidationException: <p> Invalid or malformed request. </p>
            capo_timestream_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_query.types.describe_endpoints_request.DescribeEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_timestream_query.types.describe_endpoints_response.DescribeEndpointsResponse"
        ]:
            import capo_timestream_query._operations.timestream_20181101.describe_endpoints

            (
                output,
                http_response,
            ) = await capo_timestream_query._operations.timestream_20181101.describe_endpoints.async_describe_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_query.types.describe_endpoints_request.DescribeEndpointsRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_scheduled_query(
        self,
        scheduled_query_arn: "capo_timestream_query.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None,
    ) -> "capo_timestream_query.types.describe_scheduled_query_response.DescribeScheduledQueryResponse":
        """<p>Provides detailed information about a scheduled query.</p>

        Args:
            scheduled_query_arn: <p>The ARN of the scheduled query.</p>

        Raises:
            capo_timestream_query.errors.access_denied_exception.AccessDeniedException: <p>You do not have the necessary permissions to access the account settings.</p>
            capo_timestream_query.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_timestream_query.errors.invalid_endpoint_exception.InvalidEndpointException: <p>The requested endpoint is invalid.</p>
            capo_timestream_query.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_timestream_query.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to excessive requests.</p>
            capo_timestream_query.errors.validation_exception.ValidationException: <p> Invalid or malformed request. </p>
            capo_timestream_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_query.types.describe_scheduled_query_request.DescribeScheduledQueryRequest]",
        ) -> AsyncOperationResponse[
            "capo_timestream_query.types.describe_scheduled_query_response.DescribeScheduledQueryResponse"
        ]:
            import capo_timestream_query._operations.timestream_20181101.describe_scheduled_query

            (
                output,
                http_response,
            ) = await capo_timestream_query._operations.timestream_20181101.describe_scheduled_query.async_describe_scheduled_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_query.types.describe_scheduled_query_request.DescribeScheduledQueryRequest = {
            "scheduled_query_arn": scheduled_query_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def execute_scheduled_query(
        self,
        scheduled_query_arn: "capo_timestream_query.types.amazon_resource_name.AmazonResourceName",
        invocation_time: "capo_timestream_query.types.time.Time",
        *,
        config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None,
        client_token: Optional[
            "capo_timestream_query.types.client_token.ClientToken"
        ] = None,
        query_insights: Optional[
            "capo_timestream_query.types.scheduled_query_insights.ScheduledQueryInsights"
        ] = None,
    ) -> None:
        """<p> You can use this API to run a scheduled query manually. </p> <p>If you enabled <code>QueryInsights</code>, this API also returns insights and metrics related to the query that you executed as part of an Amazon SNS notification. <code>QueryInsights</code> helps with performance tuning of your query. For more information about <code>QueryInsights</code>, see <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/using-query-insights.html">Using query insights to optimize queries in Amazon Timestream</a>.</p>

        Args:
            scheduled_query_arn: <p>ARN of the scheduled query.</p>
            invocation_time: <p>The timestamp in UTC. Query will be run as if it was invoked at this timestamp. </p>
            client_token: <p>Not used. </p>
            query_insights: <p>Encapsulates settings for enabling <code>QueryInsights</code>.</p> <p>Enabling <code>QueryInsights</code> returns insights and metrics as a part of the Amazon SNS notification for the query that you executed. You can use <code>QueryInsights</code> to tune your query performance and cost.</p>

        Raises:
            capo_timestream_query.errors.access_denied_exception.AccessDeniedException: <p>You do not have the necessary permissions to access the account settings.</p>
            capo_timestream_query.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_timestream_query.errors.invalid_endpoint_exception.InvalidEndpointException: <p>The requested endpoint is invalid.</p>
            capo_timestream_query.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_timestream_query.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to excessive requests.</p>
            capo_timestream_query.errors.validation_exception.ValidationException: <p> Invalid or malformed request. </p>
            capo_timestream_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_query.types.execute_scheduled_query_request.ExecuteScheduledQueryRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_timestream_query._operations.timestream_20181101.execute_scheduled_query

            (
                output,
                http_response,
            ) = await capo_timestream_query._operations.timestream_20181101.execute_scheduled_query.async_execute_scheduled_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_query.types.execute_scheduled_query_request.ExecuteScheduledQueryRequest = {
            "scheduled_query_arn": scheduled_query_arn,
            "invocation_time": invocation_time,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if query_insights is not None:
            input_["query_insights"] = query_insights

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_scheduled_queries(
        self,
        *,
        config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None,
        max_results: Optional[
            "capo_timestream_query.types.max_scheduled_queries_results.MaxScheduledQueriesResults"
        ] = None,
        next_token: Optional[
            "capo_timestream_query.types.next_scheduled_queries_results_token.NextScheduledQueriesResultsToken"
        ] = None,
    ) -> "capo_timestream_query.types.list_scheduled_queries_response.ListScheduledQueriesResponse":
        """<p>Gets a list of all scheduled queries in the caller's Amazon account and Region. <code>ListScheduledQueries</code> is eventually consistent. </p>

        Args:
            max_results: <p>The maximum number of items to return in the output. If the total number of items available is more than the value specified, a <code>NextToken</code> is provided in the output. To resume pagination, provide the <code>NextToken</code> value as the argument to the subsequent call to <code>ListScheduledQueriesRequest</code>.</p>
            next_token: <p> A pagination token to resume pagination.</p>

        Raises:
            capo_timestream_query.errors.access_denied_exception.AccessDeniedException: <p>You do not have the necessary permissions to access the account settings.</p>
            capo_timestream_query.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_timestream_query.errors.invalid_endpoint_exception.InvalidEndpointException: <p>The requested endpoint is invalid.</p>
            capo_timestream_query.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to excessive requests.</p>
            capo_timestream_query.errors.validation_exception.ValidationException: <p> Invalid or malformed request. </p>
            capo_timestream_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_query.types.list_scheduled_queries_request.ListScheduledQueriesRequest]",
        ) -> AsyncOperationResponse[
            "capo_timestream_query.types.list_scheduled_queries_response.ListScheduledQueriesResponse"
        ]:
            import capo_timestream_query._operations.timestream_20181101.list_scheduled_queries

            (
                output,
                http_response,
            ) = await capo_timestream_query._operations.timestream_20181101.list_scheduled_queries.async_list_scheduled_queries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_query.types.list_scheduled_queries_request.ListScheduledQueriesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_scheduled_queries(
        self,
        *,
        config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None,
        max_results: Optional[
            "capo_timestream_query.types.max_scheduled_queries_results.MaxScheduledQueriesResults"
        ] = None,
        next_token: Optional[
            "capo_timestream_query.types.next_scheduled_queries_results_token.NextScheduledQueriesResultsToken"
        ] = None,
    ) -> "AsyncIterator[capo_timestream_query.types.scheduled_query.ScheduledQuery]":
        _token = next_token
        while True:
            _response = await self.list_scheduled_queries(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("scheduled_queries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_timestream_query.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None,
        max_results: Optional[
            "capo_timestream_query.types.max_tags_for_resource_result.MaxTagsForResourceResult"
        ] = None,
        next_token: Optional[
            "capo_timestream_query.types.next_tags_for_resource_results_token.NextTagsForResourceResultsToken"
        ] = None,
    ) -> "capo_timestream_query.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List all tags on a Timestream query resource.</p>

        Args:
            resource_arn: <p>The Timestream resource with tags to be listed. This value is an Amazon Resource Name (ARN).</p>
            max_results: <p>The maximum number of tags to return.</p>
            next_token: <p>A pagination token to resume pagination.</p>

        Raises:
            capo_timestream_query.errors.invalid_endpoint_exception.InvalidEndpointException: <p>The requested endpoint is invalid.</p>
            capo_timestream_query.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_timestream_query.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to excessive requests.</p>
            capo_timestream_query.errors.validation_exception.ValidationException: <p> Invalid or malformed request. </p>
            capo_timestream_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_query.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_timestream_query.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_timestream_query._operations.timestream_20181101.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_timestream_query._operations.timestream_20181101.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_query.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_tags_for_resource(
        self,
        resource_arn: "capo_timestream_query.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None,
        max_results: Optional[
            "capo_timestream_query.types.max_tags_for_resource_result.MaxTagsForResourceResult"
        ] = None,
        next_token: Optional[
            "capo_timestream_query.types.next_tags_for_resource_results_token.NextTagsForResourceResultsToken"
        ] = None,
    ) -> "AsyncIterator[capo_timestream_query.types.tag.Tag]":
        _token = next_token
        while True:
            _response = await self.list_tags_for_resource(
                resource_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def prepare_query(
        self,
        query_string: "capo_timestream_query.types.query_string.QueryString",
        *,
        config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None,
        validate_only: Optional[
            "capo_timestream_query.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "capo_timestream_query.types.prepare_query_response.PrepareQueryResponse":
        """<p>A synchronous operation that allows you to submit a query with parameters to be stored by Timestream for later running. Timestream only supports using this operation with <code>ValidateOnly</code> set to <code>true</code>. </p>

        Args:
            query_string: <p>The Timestream query string that you want to use as a prepared statement. Parameter names can be specified in the query string <code>@</code> character followed by an identifier. </p>
            validate_only: <p>By setting this value to <code>true</code>, Timestream will only validate that the query string is a valid Timestream query, and not store the prepared query for later use.</p>

        Raises:
            capo_timestream_query.errors.access_denied_exception.AccessDeniedException: <p>You do not have the necessary permissions to access the account settings.</p>
            capo_timestream_query.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_timestream_query.errors.invalid_endpoint_exception.InvalidEndpointException: <p>The requested endpoint is invalid.</p>
            capo_timestream_query.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to excessive requests.</p>
            capo_timestream_query.errors.validation_exception.ValidationException: <p> Invalid or malformed request. </p>
            capo_timestream_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_query.types.prepare_query_request.PrepareQueryRequest]",
        ) -> AsyncOperationResponse[
            "capo_timestream_query.types.prepare_query_response.PrepareQueryResponse"
        ]:
            import capo_timestream_query._operations.timestream_20181101.prepare_query

            (
                output,
                http_response,
            ) = await capo_timestream_query._operations.timestream_20181101.prepare_query.async_prepare_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_query.types.prepare_query_request.PrepareQueryRequest = {
            "query_string": query_string
        }
        if validate_only is not None:
            input_["validate_only"] = validate_only

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def query(
        self,
        query_string: "capo_timestream_query.types.query_string.QueryString",
        *,
        config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None,
        client_token: Optional[
            "capo_timestream_query.types.client_request_token.ClientRequestToken"
        ] = None,
        next_token: Optional[
            "capo_timestream_query.types.pagination_token.PaginationToken"
        ] = None,
        max_rows: Optional[
            "capo_timestream_query.types.max_query_results.MaxQueryResults"
        ] = None,
        query_insights: Optional[
            "capo_timestream_query.types.query_insights.QueryInsights"
        ] = None,
    ) -> "capo_timestream_query.types.query_response.QueryResponse":
        """<p> <code>Query</code> is a synchronous operation that enables you to run a query against your Amazon Timestream data.</p> <p>If you enabled <code>QueryInsights</code>, this API also returns insights and metrics related to the query that you executed. <code>QueryInsights</code> helps with performance tuning of your query. For more information about <code>QueryInsights</code>, see <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/using-query-insights.html">Using query insights to optimize queries in Amazon Timestream</a>.</p> <note> <p>The maximum number of <code>Query</code> API requests you're allowed to make with <code>QueryInsights</code> enabled is 1 query per second (QPS). If you exceed this query rate, it might result in throttling.</p> </note> <p> <code>Query</code> will time out after 60 seconds. You must update the default timeout in the SDK to support a timeout of 60 seconds. See the <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.run-query.html">code sample</a> for details. </p> <p>Your query request will fail in the following cases:</p> <ul> <li> <p> If you submit a <code>Query</code> request with the same client token outside of the 5-minute idempotency window. </p> </li> <li> <p> If you submit a <code>Query</code> request with the same client token, but change other parameters, within the 5-minute idempotency window. </p> </li> <li> <p> If the size of the row (including the query metadata) exceeds 1 MB, then the query will fail with the following error message: </p> <p> <code>Query aborted as max page response size has been exceeded by the output result row</code> </p> </li> <li> <p> If the IAM principal of the query initiator and the result reader are not the same and/or the query initiator and the result reader do not have the same query string in the query requests, the query will fail with an <code>Invalid pagination token</code> error. </p> </li> </ul>

        Args:
            query_string: <p> The query to be run by Timestream. </p>
            client_token: <p> Unique, case-sensitive string of up to 64 ASCII characters specified when a <code>Query</code> request is made. Providing a <code>ClientToken</code> makes the call to <code>Query</code> <i>idempotent</i>. This means that running the same query repeatedly will produce the same result. In other words, making multiple identical <code>Query</code> requests has the same effect as making a single request. When using <code>ClientToken</code> in a query, note the following: </p> <ul> <li> <p> If the Query API is instantiated without a <code>ClientToken</code>, the Query SDK generates a <code>ClientToken</code> on your behalf.</p> </li> <li> <p>If the <code>Query</code> invocation only contains the <code>ClientToken</code> but does not include a <code>NextToken</code>, that invocation of <code>Query</code> is assumed to be a new query run.</p> </li> <li> <p>If the invocation contains <code>NextToken</code>, that particular invocation is assumed to be a subsequent invocation of a prior call to the Query API, and a result set is returned.</p> </li> <li> <p> After 4 hours, any request with the same <code>ClientToken</code> is treated as a new request. </p> </li> </ul>
            next_token: <p> A pagination token used to return a set of results. When the <code>Query</code> API is invoked using <code>NextToken</code>, that particular invocation is assumed to be a subsequent invocation of a prior call to <code>Query</code>, and a result set is returned. However, if the <code>Query</code> invocation only contains the <code>ClientToken</code>, that invocation of <code>Query</code> is assumed to be a new query run. </p> <p>Note the following when using NextToken in a query:</p> <ul> <li> <p>A pagination token can be used for up to five <code>Query</code> invocations, OR for a duration of up to 1 hour – whichever comes first.</p> </li> <li> <p>Using the same <code>NextToken</code> will return the same set of records. To keep paginating through the result set, you must to use the most recent <code>nextToken</code>.</p> </li> <li> <p>Suppose a <code>Query</code> invocation returns two <code>NextToken</code> values, <code>TokenA</code> and <code>TokenB</code>. If <code>TokenB</code> is used in a subsequent <code>Query</code> invocation, then <code>TokenA</code> is invalidated and cannot be reused.</p> </li> <li> <p>To request a previous result set from a query after pagination has begun, you must re-invoke the Query API.</p> </li> <li> <p>The latest <code>NextToken</code> should be used to paginate until <code>null</code> is returned, at which point a new <code>NextToken</code> should be used.</p> </li> <li> <p> If the IAM principal of the query initiator and the result reader are not the same and/or the query initiator and the result reader do not have the same query string in the query requests, the query will fail with an <code>Invalid pagination token</code> error. </p> </li> </ul>
            max_rows: <p> The total number of rows to be returned in the <code>Query</code> output. The initial run of <code>Query</code> with a <code>MaxRows</code> value specified will return the result set of the query in two cases: </p> <ul> <li> <p>The size of the result is less than <code>1MB</code>.</p> </li> <li> <p>The number of rows in the result set is less than the value of <code>maxRows</code>.</p> </li> </ul> <p>Otherwise, the initial invocation of <code>Query</code> only returns a <code>NextToken</code>, which can then be used in subsequent calls to fetch the result set. To resume pagination, provide the <code>NextToken</code> value in the subsequent command.</p> <p>If the row size is large (e.g. a row has many columns), Timestream may return fewer rows to keep the response size from exceeding the 1 MB limit. If <code>MaxRows</code> is not provided, Timestream will send the necessary number of rows to meet the 1 MB limit.</p>
            query_insights: <p>Encapsulates settings for enabling <code>QueryInsights</code>.</p> <p>Enabling <code>QueryInsights</code> returns insights and metrics in addition to query results for the query that you executed. You can use <code>QueryInsights</code> to tune your query performance.</p>

        Raises:
            capo_timestream_query.errors.access_denied_exception.AccessDeniedException: <p>You do not have the necessary permissions to access the account settings.</p>
            capo_timestream_query.errors.conflict_exception.ConflictException: <p> Unable to poll results for a cancelled query. </p>
            capo_timestream_query.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_timestream_query.errors.invalid_endpoint_exception.InvalidEndpointException: <p>The requested endpoint is invalid.</p>
            capo_timestream_query.errors.query_execution_exception.QueryExecutionException: <p> Timestream was unable to run the query successfully. </p>
            capo_timestream_query.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to excessive requests.</p>
            capo_timestream_query.errors.validation_exception.ValidationException: <p> Invalid or malformed request. </p>
            capo_timestream_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_query.types.query_request.QueryRequest]",
        ) -> AsyncOperationResponse[
            "capo_timestream_query.types.query_response.QueryResponse"
        ]:
            import capo_timestream_query._operations.timestream_20181101.query

            (
                output,
                http_response,
            ) = await capo_timestream_query._operations.timestream_20181101.query.async_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_query.types.query_request.QueryRequest = {
            "query_string": query_string
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if next_token is not None:
            input_["next_token"] = next_token
        if max_rows is not None:
            input_["max_rows"] = max_rows
        if query_insights is not None:
            input_["query_insights"] = query_insights

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_query(
        self,
        query_string: "capo_timestream_query.types.query_string.QueryString",
        *,
        config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None,
        client_token: Optional[
            "capo_timestream_query.types.client_request_token.ClientRequestToken"
        ] = None,
        next_token: Optional[
            "capo_timestream_query.types.pagination_token.PaginationToken"
        ] = None,
        max_rows: Optional[
            "capo_timestream_query.types.max_query_results.MaxQueryResults"
        ] = None,
        query_insights: Optional[
            "capo_timestream_query.types.query_insights.QueryInsights"
        ] = None,
    ) -> "AsyncIterator[capo_timestream_query.types.row.Row]":
        _token = next_token
        while True:
            _response = await self.query(
                query_string,
                config_overrides=config_overrides,
                client_token=client_token,
                next_token=_token,
                max_rows=max_rows,
                query_insights=query_insights,
            )
            _page = _resolve_path(_response, ("rows",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def tag_resource(
        self,
        resource_arn: "capo_timestream_query.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_timestream_query.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None,
    ) -> "capo_timestream_query.types.tag_resource_response.TagResourceResponse":
        """<p>Associate a set of tags with a Timestream resource. You can then activate these user-defined tags so that they appear on the Billing and Cost Management console for cost allocation tracking. </p>

        Args:
            resource_arn: <p>Identifies the Timestream resource to which tags should be added. This value is an Amazon Resource Name (ARN).</p>
            tags: <p>The tags to be assigned to the Timestream resource.</p>

        Raises:
            capo_timestream_query.errors.invalid_endpoint_exception.InvalidEndpointException: <p>The requested endpoint is invalid.</p>
            capo_timestream_query.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_timestream_query.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_timestream_query.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to excessive requests.</p>
            capo_timestream_query.errors.validation_exception.ValidationException: <p> Invalid or malformed request. </p>
            capo_timestream_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_query.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_timestream_query.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_timestream_query._operations.timestream_20181101.tag_resource

            (
                output,
                http_response,
            ) = await capo_timestream_query._operations.timestream_20181101.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_query.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_timestream_query.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_timestream_query.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None,
    ) -> "capo_timestream_query.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the association of tags from a Timestream query resource.</p>

        Args:
            resource_arn: <p>The Timestream resource that the tags will be removed from. This value is an Amazon Resource Name (ARN). </p>
            tag_keys: <p>A list of tags keys. Existing tags of the resource whose keys are members of this list will be removed from the Timestream resource. </p>

        Raises:
            capo_timestream_query.errors.invalid_endpoint_exception.InvalidEndpointException: <p>The requested endpoint is invalid.</p>
            capo_timestream_query.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_timestream_query.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to excessive requests.</p>
            capo_timestream_query.errors.validation_exception.ValidationException: <p> Invalid or malformed request. </p>
            capo_timestream_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_query.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_timestream_query.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_timestream_query._operations.timestream_20181101.untag_resource

            (
                output,
                http_response,
            ) = await capo_timestream_query._operations.timestream_20181101.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_query.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_account_settings(
        self,
        *,
        config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None,
        max_query_tcu: Optional[
            "capo_timestream_query.types.max_query_capacity.MaxQueryCapacity"
        ] = None,
        query_pricing_model: Optional[
            "capo_timestream_query.types.query_pricing_model.QueryPricingModel"
        ] = None,
        query_compute: Optional[
            "capo_timestream_query.types.query_compute_request.QueryComputeRequest"
        ] = None,
    ) -> "capo_timestream_query.types.update_account_settings_response.UpdateAccountSettingsResponse":
        """<p>Transitions your account to use TCUs for query pricing and modifies the maximum query compute units that you've configured. If you reduce the value of <code>MaxQueryTCU</code> to a desired configuration, the new value can take up to 24 hours to be effective.</p> <note> <p>After you've transitioned your account to use TCUs for query pricing, you can't transition to using bytes scanned for query pricing.</p> </note>

        Args:
            max_query_tcu: <p>The maximum number of compute units the service will use at any point in time to serve your queries. To run queries, you must set a minimum capacity of 4 TCU. You can set the maximum number of TCU in multiples of 4, for example, 4, 8, 16, 32, and so on. The maximum value supported for <code>MaxQueryTCU</code> is 1000. To request an increase to this soft limit, contact Amazon Web Services Support. For information about the default quota for maxQueryTCU, see Default quotas. This configuration is applicable only for on-demand usage of Timestream Compute Units (TCUs).</p> <p>The maximum value supported for <code>MaxQueryTCU</code> is 1000. To request an increase to this soft limit, contact Amazon Web Services Support. For information about the default quota for <code>maxQueryTCU</code>, see <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html#limits.default">Default quotas</a>.</p>
            query_pricing_model: <p>The pricing model for queries in an account.</p> <note> <p>The <code>QueryPricingModel</code> parameter is used by several Timestream operations; however, the <code>UpdateAccountSettings</code> API operation doesn't recognize any values other than <code>COMPUTE_UNITS</code>.</p> </note>
            query_compute: <p>Modifies the query compute settings configured in your account, including the query pricing model and provisioned Timestream Compute Units (TCUs) in your account.</p> <note> <p>This API is idempotent, meaning that making the same request multiple times will have the same effect as making the request once.</p> </note>

        Raises:
            capo_timestream_query.errors.access_denied_exception.AccessDeniedException: <p>You do not have the necessary permissions to access the account settings.</p>
            capo_timestream_query.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_timestream_query.errors.invalid_endpoint_exception.InvalidEndpointException: <p>The requested endpoint is invalid.</p>
            capo_timestream_query.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to excessive requests.</p>
            capo_timestream_query.errors.validation_exception.ValidationException: <p> Invalid or malformed request. </p>
            capo_timestream_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_query.types.update_account_settings_request.UpdateAccountSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_timestream_query.types.update_account_settings_response.UpdateAccountSettingsResponse"
        ]:
            import capo_timestream_query._operations.timestream_20181101.update_account_settings

            (
                output,
                http_response,
            ) = await capo_timestream_query._operations.timestream_20181101.update_account_settings.async_update_account_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_query.types.update_account_settings_request.UpdateAccountSettingsRequest = {}
        if max_query_tcu is not None:
            input_["max_query_tcu"] = max_query_tcu
        if query_pricing_model is not None:
            input_["query_pricing_model"] = query_pricing_model
        if query_compute is not None:
            input_["query_compute"] = query_compute

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_scheduled_query(
        self,
        scheduled_query_arn: "capo_timestream_query.types.amazon_resource_name.AmazonResourceName",
        state: "capo_timestream_query.types.scheduled_query_state.ScheduledQueryState",
        *,
        config_overrides: Optional[AsyncTimestreamQueryClientConfig] = None,
    ) -> None:
        """<p>Update a scheduled query.</p>

        Args:
            scheduled_query_arn: <p>ARN of the scheuled query.</p>
            state: <p>State of the scheduled query. </p>

        Raises:
            capo_timestream_query.errors.access_denied_exception.AccessDeniedException: <p>You do not have the necessary permissions to access the account settings.</p>
            capo_timestream_query.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_timestream_query.errors.invalid_endpoint_exception.InvalidEndpointException: <p>The requested endpoint is invalid.</p>
            capo_timestream_query.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_timestream_query.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to excessive requests.</p>
            capo_timestream_query.errors.validation_exception.ValidationException: <p> Invalid or malformed request. </p>
            capo_timestream_query.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_query.types.update_scheduled_query_request.UpdateScheduledQueryRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_timestream_query._operations.timestream_20181101.update_scheduled_query

            (
                output,
                http_response,
            ) = await capo_timestream_query._operations.timestream_20181101.update_scheduled_query.async_update_scheduled_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_timestream_query.types.update_scheduled_query_request.UpdateScheduledQueryRequest = {
            "scheduled_query_arn": scheduled_query_arn,
            "state": state,
        }

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
