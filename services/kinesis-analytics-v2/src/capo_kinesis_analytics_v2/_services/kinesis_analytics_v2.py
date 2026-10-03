"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#KinesisAnalytics_20180523``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_kinesis_analytics_v2._auth._signers
import capo_kinesis_analytics_v2._auth._sigv4
from capo_kinesis_analytics_v2._auth._identity import Credentials
from capo_kinesis_analytics_v2._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_kinesis_analytics_v2._auth._zapros_handler import AuthMiddleware
from capo_kinesis_analytics_v2._pagination import resolve_path as _resolve_path
from capo_kinesis_analytics_v2._services._aws_config import aws_config
from capo_kinesis_analytics_v2._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.add_application_cloud_watch_logging_option_request
    import capo_kinesis_analytics_v2.types.add_application_cloud_watch_logging_option_response
    import capo_kinesis_analytics_v2.types.add_application_input_processing_configuration_request
    import capo_kinesis_analytics_v2.types.add_application_input_processing_configuration_response
    import capo_kinesis_analytics_v2.types.add_application_input_request
    import capo_kinesis_analytics_v2.types.add_application_input_response
    import capo_kinesis_analytics_v2.types.add_application_output_request
    import capo_kinesis_analytics_v2.types.add_application_output_response
    import capo_kinesis_analytics_v2.types.add_application_reference_data_source_request
    import capo_kinesis_analytics_v2.types.add_application_reference_data_source_response
    import capo_kinesis_analytics_v2.types.add_application_vpc_configuration_request
    import capo_kinesis_analytics_v2.types.add_application_vpc_configuration_response
    import capo_kinesis_analytics_v2.types.application_configuration
    import capo_kinesis_analytics_v2.types.application_configuration_update
    import capo_kinesis_analytics_v2.types.application_description
    import capo_kinesis_analytics_v2.types.application_maintenance_configuration_update
    import capo_kinesis_analytics_v2.types.application_mode
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.application_operation_info
    import capo_kinesis_analytics_v2.types.application_summary
    import capo_kinesis_analytics_v2.types.application_version_id
    import capo_kinesis_analytics_v2.types.application_version_summary
    import capo_kinesis_analytics_v2.types.boolean_object
    import capo_kinesis_analytics_v2.types.cloud_watch_logging_option
    import capo_kinesis_analytics_v2.types.cloud_watch_logging_option_updates
    import capo_kinesis_analytics_v2.types.cloud_watch_logging_options
    import capo_kinesis_analytics_v2.types.conditional_token
    import capo_kinesis_analytics_v2.types.create_application_presigned_url_request
    import capo_kinesis_analytics_v2.types.create_application_presigned_url_response
    import capo_kinesis_analytics_v2.types.create_application_request
    import capo_kinesis_analytics_v2.types.create_application_response
    import capo_kinesis_analytics_v2.types.create_application_snapshot_request
    import capo_kinesis_analytics_v2.types.create_application_snapshot_response
    import capo_kinesis_analytics_v2.types.delete_application_cloud_watch_logging_option_request
    import capo_kinesis_analytics_v2.types.delete_application_cloud_watch_logging_option_response
    import capo_kinesis_analytics_v2.types.delete_application_input_processing_configuration_request
    import capo_kinesis_analytics_v2.types.delete_application_input_processing_configuration_response
    import capo_kinesis_analytics_v2.types.delete_application_output_request
    import capo_kinesis_analytics_v2.types.delete_application_output_response
    import capo_kinesis_analytics_v2.types.delete_application_reference_data_source_request
    import capo_kinesis_analytics_v2.types.delete_application_reference_data_source_response
    import capo_kinesis_analytics_v2.types.delete_application_request
    import capo_kinesis_analytics_v2.types.delete_application_response
    import capo_kinesis_analytics_v2.types.delete_application_snapshot_request
    import capo_kinesis_analytics_v2.types.delete_application_snapshot_response
    import capo_kinesis_analytics_v2.types.delete_application_vpc_configuration_request
    import capo_kinesis_analytics_v2.types.delete_application_vpc_configuration_response
    import capo_kinesis_analytics_v2.types.describe_application_operation_request
    import capo_kinesis_analytics_v2.types.describe_application_operation_response
    import capo_kinesis_analytics_v2.types.describe_application_request
    import capo_kinesis_analytics_v2.types.describe_application_response
    import capo_kinesis_analytics_v2.types.describe_application_snapshot_request
    import capo_kinesis_analytics_v2.types.describe_application_snapshot_response
    import capo_kinesis_analytics_v2.types.describe_application_version_request
    import capo_kinesis_analytics_v2.types.describe_application_version_response
    import capo_kinesis_analytics_v2.types.discover_input_schema_request
    import capo_kinesis_analytics_v2.types.discover_input_schema_response
    import capo_kinesis_analytics_v2.types.id
    import capo_kinesis_analytics_v2.types.input
    import capo_kinesis_analytics_v2.types.input_processing_configuration
    import capo_kinesis_analytics_v2.types.input_starting_position_configuration
    import capo_kinesis_analytics_v2.types.kinesis_analytics_arn
    import capo_kinesis_analytics_v2.types.list_application_operations_input_limit
    import capo_kinesis_analytics_v2.types.list_application_operations_request
    import capo_kinesis_analytics_v2.types.list_application_operations_response
    import capo_kinesis_analytics_v2.types.list_application_snapshots_request
    import capo_kinesis_analytics_v2.types.list_application_snapshots_response
    import capo_kinesis_analytics_v2.types.list_application_versions_input_limit
    import capo_kinesis_analytics_v2.types.list_application_versions_request
    import capo_kinesis_analytics_v2.types.list_application_versions_response
    import capo_kinesis_analytics_v2.types.list_applications_input_limit
    import capo_kinesis_analytics_v2.types.list_applications_request
    import capo_kinesis_analytics_v2.types.list_applications_response
    import capo_kinesis_analytics_v2.types.list_snapshots_input_limit
    import capo_kinesis_analytics_v2.types.list_tags_for_resource_request
    import capo_kinesis_analytics_v2.types.list_tags_for_resource_response
    import capo_kinesis_analytics_v2.types.next_token
    import capo_kinesis_analytics_v2.types.operation
    import capo_kinesis_analytics_v2.types.operation_id
    import capo_kinesis_analytics_v2.types.operation_status
    import capo_kinesis_analytics_v2.types.output
    import capo_kinesis_analytics_v2.types.reference_data_source
    import capo_kinesis_analytics_v2.types.resource_arn
    import capo_kinesis_analytics_v2.types.role_arn
    import capo_kinesis_analytics_v2.types.rollback_application_request
    import capo_kinesis_analytics_v2.types.rollback_application_response
    import capo_kinesis_analytics_v2.types.run_configuration
    import capo_kinesis_analytics_v2.types.run_configuration_update
    import capo_kinesis_analytics_v2.types.runtime_environment
    import capo_kinesis_analytics_v2.types.s3_configuration
    import capo_kinesis_analytics_v2.types.session_expiration_duration_in_seconds
    import capo_kinesis_analytics_v2.types.snapshot_details
    import capo_kinesis_analytics_v2.types.snapshot_name
    import capo_kinesis_analytics_v2.types.start_application_request
    import capo_kinesis_analytics_v2.types.start_application_response
    import capo_kinesis_analytics_v2.types.stop_application_request
    import capo_kinesis_analytics_v2.types.stop_application_response
    import capo_kinesis_analytics_v2.types.tag_keys
    import capo_kinesis_analytics_v2.types.tag_resource_request
    import capo_kinesis_analytics_v2.types.tag_resource_response
    import capo_kinesis_analytics_v2.types.tags
    import capo_kinesis_analytics_v2.types.timestamp
    import capo_kinesis_analytics_v2.types.untag_resource_request
    import capo_kinesis_analytics_v2.types.untag_resource_response
    import capo_kinesis_analytics_v2.types.update_application_maintenance_configuration_request
    import capo_kinesis_analytics_v2.types.update_application_maintenance_configuration_response
    import capo_kinesis_analytics_v2.types.update_application_request
    import capo_kinesis_analytics_v2.types.update_application_response
    import capo_kinesis_analytics_v2.types.url_type
    import capo_kinesis_analytics_v2.types.vpc_configuration


class KinesisAnalyticsV2ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class KinesisAnalyticsV2Client:
    """A client for the ``KinesisAnalyticsV2`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
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
        self._config = KinesisAnalyticsV2ClientConfig(
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
        self, config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: KinesisAnalyticsV2ClientConfig = config_overrides or {}
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
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def add_application_cloud_watch_logging_option(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        cloud_watch_logging_option: "capo_kinesis_analytics_v2.types.cloud_watch_logging_option.CloudWatchLoggingOption",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        current_application_version_id: Optional[
            "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
        ] = None,
        conditional_token: Optional[
            "capo_kinesis_analytics_v2.types.conditional_token.ConditionalToken"
        ] = None,
    ) -> "capo_kinesis_analytics_v2.types.add_application_cloud_watch_logging_option_response.AddApplicationCloudWatchLoggingOptionResponse":
        """<p>Adds an Amazon CloudWatch log stream to monitor application configuration errors.</p>

        Args:
            application_name: <p>The Kinesis Data Analytics application name.</p>
            current_application_version_id: <p>The version ID of the SQL-based Kinesis Data Analytics application. You must provide the <code>CurrentApplicationVersionId</code> or the <code>ConditionalToken</code>.You can retrieve the application version ID using <a>DescribeApplication</a>. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>
            cloud_watch_logging_option: <p>Provides the Amazon CloudWatch log stream Amazon Resource Name (ARN). </p>
            conditional_token: <p>A value you use to implement strong concurrency for application updates. You must provide the <code>CurrentApplicationVersionId</code> or the <code>ConditionalToken</code>. You get the application's current <code>ConditionalToken</code> using <a>DescribeApplication</a>. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_application_configuration_exception.InvalidApplicationConfigurationException: <p>The user-provided application configuration is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.add_application_cloud_watch_logging_option_request.AddApplicationCloudWatchLoggingOptionRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.add_application_cloud_watch_logging_option_response.AddApplicationCloudWatchLoggingOptionResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.add_application_cloud_watch_logging_option

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.add_application_cloud_watch_logging_option.add_application_cloud_watch_logging_option(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.add_application_cloud_watch_logging_option_request.AddApplicationCloudWatchLoggingOptionRequest = {
            "application_name": application_name,
            "cloud_watch_logging_option": cloud_watch_logging_option,
        }
        if current_application_version_id is not None:
            input_["current_application_version_id"] = current_application_version_id
        if conditional_token is not None:
            input_["conditional_token"] = conditional_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_application_input(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        current_application_version_id: "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId",
        input: "capo_kinesis_analytics_v2.types.input.Input",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
    ) -> "capo_kinesis_analytics_v2.types.add_application_input_response.AddApplicationInputResponse":
        """<p> Adds a streaming source to your SQL-based Kinesis Data Analytics application. </p> <p>You can add a streaming source when you create an application, or you can use this operation to add a streaming source after you create an application. For more information, see <a>CreateApplication</a>.</p> <p>Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the <a>DescribeApplication</a> operation to find the current application version. </p>

        Args:
            application_name: <p>The name of your existing application to which you want to add the streaming source.</p>
            current_application_version_id: <p>The current version of your application. You must provide the <code>ApplicationVersionID</code> or the <code>ConditionalToken</code>.You can use the <a>DescribeApplication</a> operation to find the current application version.</p>
            input: <p>The <a>Input</a> to add.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.code_validation_exception.CodeValidationException: <p>The user-provided application code (query) is not valid. This can be a simple syntax error.</p>
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.add_application_input_request.AddApplicationInputRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.add_application_input_response.AddApplicationInputResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.add_application_input

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.add_application_input.add_application_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.add_application_input_request.AddApplicationInputRequest = {
            "application_name": application_name,
            "current_application_version_id": current_application_version_id,
            "input": input,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_application_input_processing_configuration(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        current_application_version_id: "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId",
        input_id: "capo_kinesis_analytics_v2.types.id.Id",
        input_processing_configuration: "capo_kinesis_analytics_v2.types.input_processing_configuration.InputProcessingConfiguration",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
    ) -> "capo_kinesis_analytics_v2.types.add_application_input_processing_configuration_response.AddApplicationInputProcessingConfigurationResponse":
        """<p>Adds an <a>InputProcessingConfiguration</a> to a SQL-based Kinesis Data Analytics application. An input processor pre-processes records on the input stream before the application's SQL code executes. Currently, the only input processor available is <a href="https://docs.aws.amazon.com/lambda/">Amazon Lambda</a>.</p>

        Args:
            application_name: <p>The name of the application to which you want to add the input processing configuration.</p>
            current_application_version_id: <p>The version of the application to which you want to add the input processing configuration. You can use the <a>DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned.</p>
            input_id: <p>The ID of the input configuration to add the input processing configuration to. You can get a list of the input IDs for an application using the <a>DescribeApplication</a> operation.</p>
            input_processing_configuration: <p>The <a>InputProcessingConfiguration</a> to add to the application.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.add_application_input_processing_configuration_request.AddApplicationInputProcessingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.add_application_input_processing_configuration_response.AddApplicationInputProcessingConfigurationResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.add_application_input_processing_configuration

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.add_application_input_processing_configuration.add_application_input_processing_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.add_application_input_processing_configuration_request.AddApplicationInputProcessingConfigurationRequest = {
            "application_name": application_name,
            "current_application_version_id": current_application_version_id,
            "input_id": input_id,
            "input_processing_configuration": input_processing_configuration,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_application_output(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        current_application_version_id: "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId",
        output: "capo_kinesis_analytics_v2.types.output.Output",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
    ) -> "capo_kinesis_analytics_v2.types.add_application_output_response.AddApplicationOutputResponse":
        """<p>Adds an external destination to your SQL-based Kinesis Data Analytics application.</p> <p>If you want Kinesis Data Analytics to deliver data from an in-application stream within your application to an external destination (such as an Kinesis data stream, a Kinesis Data Firehose delivery stream, or an Amazon Lambda function), you add the relevant configuration to your application using this operation. You can configure one or more outputs for your application. Each output configuration maps an in-application stream and an external destination.</p> <p> You can use one of the output configurations to deliver data from your in-application error stream to an external destination so that you can analyze the errors. </p> <p> Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the <a>DescribeApplication</a> operation to find the current application version.</p>

        Args:
            application_name: <p>The name of the application to which you want to add the output configuration.</p>
            current_application_version_id: <p>The version of the application to which you want to add the output configuration. You can use the <a>DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned. </p>
            output: <p>An array of objects, each describing one output configuration. In the output configuration, you specify the name of an in-application stream, a destination (that is, a Kinesis data stream, a Kinesis Data Firehose delivery stream, or an Amazon Lambda function), and record the formation to use when writing to the destination.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.add_application_output_request.AddApplicationOutputRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.add_application_output_response.AddApplicationOutputResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.add_application_output

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.add_application_output.add_application_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.add_application_output_request.AddApplicationOutputRequest = {
            "application_name": application_name,
            "current_application_version_id": current_application_version_id,
            "output": output,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_application_reference_data_source(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        current_application_version_id: "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId",
        reference_data_source: "capo_kinesis_analytics_v2.types.reference_data_source.ReferenceDataSource",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
    ) -> "capo_kinesis_analytics_v2.types.add_application_reference_data_source_response.AddApplicationReferenceDataSourceResponse":
        """<p>Adds a reference data source to an existing SQL-based Kinesis Data Analytics application.</p> <p>Kinesis Data Analytics reads reference data (that is, an Amazon S3 object) and creates an in-application table within your application. In the request, you provide the source (S3 bucket name and object key name), name of the in-application table to create, and the necessary mapping information that describes how data in an Amazon S3 object maps to columns in the resulting in-application table.</p>

        Args:
            application_name: <p>The name of an existing application.</p>
            current_application_version_id: <p>The version of the application for which you are adding the reference data source. You can use the <a>DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned.</p>
            reference_data_source: <p>The reference data source can be an object in your Amazon S3 bucket. Kinesis Data Analytics reads the object and copies the data into the in-application table that is created. You provide an S3 bucket, object key name, and the resulting in-application table that is created. </p>

        Raises:
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.add_application_reference_data_source_request.AddApplicationReferenceDataSourceRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.add_application_reference_data_source_response.AddApplicationReferenceDataSourceResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.add_application_reference_data_source

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.add_application_reference_data_source.add_application_reference_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.add_application_reference_data_source_request.AddApplicationReferenceDataSourceRequest = {
            "application_name": application_name,
            "current_application_version_id": current_application_version_id,
            "reference_data_source": reference_data_source,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_application_vpc_configuration(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        vpc_configuration: "capo_kinesis_analytics_v2.types.vpc_configuration.VpcConfiguration",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        current_application_version_id: Optional[
            "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
        ] = None,
        conditional_token: Optional[
            "capo_kinesis_analytics_v2.types.conditional_token.ConditionalToken"
        ] = None,
    ) -> "capo_kinesis_analytics_v2.types.add_application_vpc_configuration_response.AddApplicationVpcConfigurationResponse":
        """<p>Adds a Virtual Private Cloud (VPC) configuration to the application. Applications can use VPCs to store and access resources securely.</p> <p>Note the following about VPC configurations for Managed Service for Apache Flink applications:</p> <ul> <li> <p>VPC configurations are not supported for SQL applications.</p> </li> <li> <p>When a VPC is added to a Managed Service for Apache Flink application, the application can no longer be accessed from the Internet directly. To enable Internet access to the application, add an Internet gateway to your VPC.</p> </li> </ul>

        Args:
            application_name: <p>The name of an existing application.</p>
            current_application_version_id: <p>The version of the application to which you want to add the VPC configuration. You must provide the <code>CurrentApplicationVersionId</code> or the <code>ConditionalToken</code>. You can use the <a>DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>
            vpc_configuration: <p>Description of the VPC to add to the application.</p>
            conditional_token: <p>A value you use to implement strong concurrency for application updates. You must provide the <code>ApplicationVersionID</code> or the <code>ConditionalToken</code>. You get the application's current <code>ConditionalToken</code> using <a>DescribeApplication</a>. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_application_configuration_exception.InvalidApplicationConfigurationException: <p>The user-provided application configuration is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.add_application_vpc_configuration_request.AddApplicationVpcConfigurationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.add_application_vpc_configuration_response.AddApplicationVpcConfigurationResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.add_application_vpc_configuration

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.add_application_vpc_configuration.add_application_vpc_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.add_application_vpc_configuration_request.AddApplicationVpcConfigurationRequest = {
            "application_name": application_name,
            "vpc_configuration": vpc_configuration,
        }
        if current_application_version_id is not None:
            input_["current_application_version_id"] = current_application_version_id
        if conditional_token is not None:
            input_["conditional_token"] = conditional_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_application(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        runtime_environment: "capo_kinesis_analytics_v2.types.runtime_environment.RuntimeEnvironment",
        service_execution_role: "capo_kinesis_analytics_v2.types.role_arn.RoleARN",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        application_description: Optional[
            "capo_kinesis_analytics_v2.types.application_description.ApplicationDescription"
        ] = None,
        application_configuration: Optional[
            "capo_kinesis_analytics_v2.types.application_configuration.ApplicationConfiguration"
        ] = None,
        cloud_watch_logging_options: Optional[
            "capo_kinesis_analytics_v2.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
        ] = None,
        tags: Optional["capo_kinesis_analytics_v2.types.tags.Tags"] = None,
        application_mode: Optional[
            "capo_kinesis_analytics_v2.types.application_mode.ApplicationMode"
        ] = None,
    ) -> "capo_kinesis_analytics_v2.types.create_application_response.CreateApplicationResponse":
        """<p>Creates a Managed Service for Apache Flink application. For information about creating a Managed Service for Apache Flink application, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/java/getting-started.html">Creating an Application</a>.</p>

        Args:
            application_name: <p>The name of your application (for example, <code>sample-app</code>).</p>
            application_description: <p>A summary description of the application.</p>
            runtime_environment: <p>The runtime environment for the application.</p>
            service_execution_role: <p>The IAM role used by the application to access Kinesis data streams, Kinesis Data Firehose delivery streams, Amazon S3 objects, and other external resources.</p>
            application_configuration: <p>Use this parameter to configure the application.</p>
            cloud_watch_logging_options: <p>Use this parameter to configure an Amazon CloudWatch log stream to monitor application configuration errors. </p>
            tags: <p>A list of one or more tags to assign to the application. A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-tagging.html">Using Tagging</a>.</p>
            application_mode: <p>Use the <code>STREAMING</code> mode to create a Managed Service for Apache Flink application. To create a Managed Service for Apache Flink Studio notebook, use the <code>INTERACTIVE</code> mode.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.code_validation_exception.CodeValidationException: <p>The user-provided application code (query) is not valid. This can be a simple syntax error.</p>
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.limit_exceeded_exception.LimitExceededException: <p>The number of allowed resources has been exceeded.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.too_many_tags_exception.TooManyTagsException: <p>Application created with too many tags, or too many tags added to an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.</p>
            capo_kinesis_analytics_v2.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.create_application

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.create_application_request.CreateApplicationRequest = {
            "application_name": application_name,
            "runtime_environment": runtime_environment,
            "service_execution_role": service_execution_role,
        }
        if application_description is not None:
            input_["application_description"] = application_description
        if application_configuration is not None:
            input_["application_configuration"] = application_configuration
        if cloud_watch_logging_options is not None:
            input_["cloud_watch_logging_options"] = cloud_watch_logging_options
        if tags is not None:
            input_["tags"] = tags
        if application_mode is not None:
            input_["application_mode"] = application_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_application_presigned_url(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        url_type: "capo_kinesis_analytics_v2.types.url_type.UrlType",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        session_expiration_duration_in_seconds: Optional[
            "capo_kinesis_analytics_v2.types.session_expiration_duration_in_seconds.SessionExpirationDurationInSeconds"
        ] = None,
    ) -> "capo_kinesis_analytics_v2.types.create_application_presigned_url_response.CreateApplicationPresignedUrlResponse":
        """<p>Creates and returns a URL that you can use to connect to an application's extension.</p> <p>The IAM role or user used to call this API defines the permissions to access the extension. After the presigned URL is created, no additional permission is required to access this URL. IAM authorization policies for this API are also enforced for every HTTP request that attempts to connect to the extension. </p> <p>You control the amount of time that the URL will be valid using the <code>SessionExpirationDurationInSeconds</code> parameter. If you do not provide this parameter, the returned URL is valid for twelve hours.</p> <note> <p>The URL that you get from a call to CreateApplicationPresignedUrl must be used within 3 minutes to be valid. If you first try to use the URL after the 3-minute limit expires, the service returns an HTTP 403 Forbidden error.</p> </note>

        Args:
            application_name: <p>The name of the application.</p>
            url_type: <p>The type of the extension for which to create and return a URL. Currently, the only valid extension URL type is <code>FLINK_DASHBOARD_URL</code>. </p>
            session_expiration_duration_in_seconds: <p>The duration in seconds for which the returned URL will be valid.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.create_application_presigned_url_request.CreateApplicationPresignedUrlRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.create_application_presigned_url_response.CreateApplicationPresignedUrlResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.create_application_presigned_url

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.create_application_presigned_url.create_application_presigned_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.create_application_presigned_url_request.CreateApplicationPresignedUrlRequest = {
            "application_name": application_name,
            "url_type": url_type,
        }
        if session_expiration_duration_in_seconds is not None:
            input_["session_expiration_duration_in_seconds"] = (
                session_expiration_duration_in_seconds
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_application_snapshot(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        snapshot_name: "capo_kinesis_analytics_v2.types.snapshot_name.SnapshotName",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
    ) -> "capo_kinesis_analytics_v2.types.create_application_snapshot_response.CreateApplicationSnapshotResponse":
        """<p>Creates a snapshot of the application's state data.</p>

        Args:
            application_name: <p>The name of an existing application</p>
            snapshot_name: <p>An identifier for the application snapshot.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.invalid_application_configuration_exception.InvalidApplicationConfigurationException: <p>The user-provided application configuration is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.limit_exceeded_exception.LimitExceededException: <p>The number of allowed resources has been exceeded.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.create_application_snapshot_request.CreateApplicationSnapshotRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.create_application_snapshot_response.CreateApplicationSnapshotResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.create_application_snapshot

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.create_application_snapshot.create_application_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.create_application_snapshot_request.CreateApplicationSnapshotRequest = {
            "application_name": application_name,
            "snapshot_name": snapshot_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_application(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        create_timestamp: "capo_kinesis_analytics_v2.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
    ) -> "capo_kinesis_analytics_v2.types.delete_application_response.DeleteApplicationResponse":
        """<p>Deletes the specified application. Managed Service for Apache Flink halts application execution and deletes the application.</p>

        Args:
            application_name: <p>The name of the application to delete.</p>
            create_timestamp: <p>Use the <code>DescribeApplication</code> operation to get this value.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_application_configuration_exception.InvalidApplicationConfigurationException: <p>The user-provided application configuration is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.delete_application

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.delete_application_request.DeleteApplicationRequest = {
            "application_name": application_name,
            "create_timestamp": create_timestamp,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_application_cloud_watch_logging_option(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        cloud_watch_logging_option_id: "capo_kinesis_analytics_v2.types.id.Id",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        current_application_version_id: Optional[
            "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
        ] = None,
        conditional_token: Optional[
            "capo_kinesis_analytics_v2.types.conditional_token.ConditionalToken"
        ] = None,
    ) -> "capo_kinesis_analytics_v2.types.delete_application_cloud_watch_logging_option_response.DeleteApplicationCloudWatchLoggingOptionResponse":
        """<p>Deletes an Amazon CloudWatch log stream from an SQL-based Kinesis Data Analytics application. </p>

        Args:
            application_name: <p>The application name.</p>
            current_application_version_id: <p>The version ID of the application. You must provide the <code>CurrentApplicationVersionId</code> or the <code>ConditionalToken</code>. You can retrieve the application version ID using <a>DescribeApplication</a>. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>
            cloud_watch_logging_option_id: <p>The <code>CloudWatchLoggingOptionId</code> of the Amazon CloudWatch logging option to delete. You can get the <code>CloudWatchLoggingOptionId</code> by using the <a>DescribeApplication</a> operation. </p>
            conditional_token: <p>A value you use to implement strong concurrency for application updates. You must provide the <code>CurrentApplicationVersionId</code> or the <code>ConditionalToken</code>. You get the application's current <code>ConditionalToken</code> using <a>DescribeApplication</a>. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_application_configuration_exception.InvalidApplicationConfigurationException: <p>The user-provided application configuration is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.delete_application_cloud_watch_logging_option_request.DeleteApplicationCloudWatchLoggingOptionRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.delete_application_cloud_watch_logging_option_response.DeleteApplicationCloudWatchLoggingOptionResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.delete_application_cloud_watch_logging_option

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.delete_application_cloud_watch_logging_option.delete_application_cloud_watch_logging_option(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.delete_application_cloud_watch_logging_option_request.DeleteApplicationCloudWatchLoggingOptionRequest = {
            "application_name": application_name,
            "cloud_watch_logging_option_id": cloud_watch_logging_option_id,
        }
        if current_application_version_id is not None:
            input_["current_application_version_id"] = current_application_version_id
        if conditional_token is not None:
            input_["conditional_token"] = conditional_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_application_input_processing_configuration(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        current_application_version_id: "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId",
        input_id: "capo_kinesis_analytics_v2.types.id.Id",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
    ) -> "capo_kinesis_analytics_v2.types.delete_application_input_processing_configuration_response.DeleteApplicationInputProcessingConfigurationResponse":
        """<p>Deletes an <a>InputProcessingConfiguration</a> from an input.</p>

        Args:
            application_name: <p>The name of the application.</p>
            current_application_version_id: <p>The application version. You can use the <a>DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned. </p>
            input_id: <p>The ID of the input configuration from which to delete the input processing configuration. You can get a list of the input IDs for an application by using the <a>DescribeApplication</a> operation.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.delete_application_input_processing_configuration_request.DeleteApplicationInputProcessingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.delete_application_input_processing_configuration_response.DeleteApplicationInputProcessingConfigurationResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.delete_application_input_processing_configuration

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.delete_application_input_processing_configuration.delete_application_input_processing_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.delete_application_input_processing_configuration_request.DeleteApplicationInputProcessingConfigurationRequest = {
            "application_name": application_name,
            "current_application_version_id": current_application_version_id,
            "input_id": input_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_application_output(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        current_application_version_id: "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId",
        output_id: "capo_kinesis_analytics_v2.types.id.Id",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
    ) -> "capo_kinesis_analytics_v2.types.delete_application_output_response.DeleteApplicationOutputResponse":
        """<p>Deletes the output destination configuration from your SQL-based Kinesis Data Analytics application's configuration. Kinesis Data Analytics will no longer write data from the corresponding in-application stream to the external output destination.</p>

        Args:
            application_name: <p>The application name.</p>
            current_application_version_id: <p>The application version. You can use the <a>DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned. </p>
            output_id: <p>The ID of the configuration to delete. Each output configuration that is added to the application (either when the application is created or later) using the <a>AddApplicationOutput</a> operation has a unique ID. You need to provide the ID to uniquely identify the output configuration that you want to delete from the application configuration. You can use the <a>DescribeApplication</a> operation to get the specific <code>OutputId</code>. </p>

        Raises:
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.delete_application_output_request.DeleteApplicationOutputRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.delete_application_output_response.DeleteApplicationOutputResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.delete_application_output

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.delete_application_output.delete_application_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.delete_application_output_request.DeleteApplicationOutputRequest = {
            "application_name": application_name,
            "current_application_version_id": current_application_version_id,
            "output_id": output_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_application_reference_data_source(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        current_application_version_id: "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId",
        reference_id: "capo_kinesis_analytics_v2.types.id.Id",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
    ) -> "capo_kinesis_analytics_v2.types.delete_application_reference_data_source_response.DeleteApplicationReferenceDataSourceResponse":
        """<p>Deletes a reference data source configuration from the specified SQL-based Kinesis Data Analytics application's configuration.</p> <p>If the application is running, Kinesis Data Analytics immediately removes the in-application table that you created using the <a>AddApplicationReferenceDataSource</a> operation. </p>

        Args:
            application_name: <p>The name of an existing application.</p>
            current_application_version_id: <p>The current application version. You can use the <a>DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned.</p>
            reference_id: <p>The ID of the reference data source. When you add a reference data source to your application using the <a>AddApplicationReferenceDataSource</a>, Kinesis Data Analytics assigns an ID. You can use the <a>DescribeApplication</a> operation to get the reference ID. </p>

        Raises:
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.delete_application_reference_data_source_request.DeleteApplicationReferenceDataSourceRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.delete_application_reference_data_source_response.DeleteApplicationReferenceDataSourceResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.delete_application_reference_data_source

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.delete_application_reference_data_source.delete_application_reference_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.delete_application_reference_data_source_request.DeleteApplicationReferenceDataSourceRequest = {
            "application_name": application_name,
            "current_application_version_id": current_application_version_id,
            "reference_id": reference_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_application_snapshot(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        snapshot_name: "capo_kinesis_analytics_v2.types.snapshot_name.SnapshotName",
        snapshot_creation_timestamp: "capo_kinesis_analytics_v2.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
    ) -> "capo_kinesis_analytics_v2.types.delete_application_snapshot_response.DeleteApplicationSnapshotResponse":
        """<p>Deletes a snapshot of application state.</p>

        Args:
            application_name: <p>The name of an existing application.</p>
            snapshot_name: <p>The identifier for the snapshot delete.</p>
            snapshot_creation_timestamp: <p>The creation timestamp of the application snapshot to delete. You can retrieve this value using or .</p>

        Raises:
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.delete_application_snapshot_request.DeleteApplicationSnapshotRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.delete_application_snapshot_response.DeleteApplicationSnapshotResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.delete_application_snapshot

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.delete_application_snapshot.delete_application_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.delete_application_snapshot_request.DeleteApplicationSnapshotRequest = {
            "application_name": application_name,
            "snapshot_name": snapshot_name,
            "snapshot_creation_timestamp": snapshot_creation_timestamp,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_application_vpc_configuration(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        vpc_configuration_id: "capo_kinesis_analytics_v2.types.id.Id",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        current_application_version_id: Optional[
            "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
        ] = None,
        conditional_token: Optional[
            "capo_kinesis_analytics_v2.types.conditional_token.ConditionalToken"
        ] = None,
    ) -> "capo_kinesis_analytics_v2.types.delete_application_vpc_configuration_response.DeleteApplicationVpcConfigurationResponse":
        """<p>Removes a VPC configuration from a Managed Service for Apache Flink application.</p>

        Args:
            application_name: <p>The name of an existing application.</p>
            current_application_version_id: <p>The current application version ID. You must provide the <code>CurrentApplicationVersionId</code> or the <code>ConditionalToken</code>. You can retrieve the application version ID using <a>DescribeApplication</a>. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>
            vpc_configuration_id: <p>The ID of the VPC configuration to delete.</p>
            conditional_token: <p>A value you use to implement strong concurrency for application updates. You must provide the <code>CurrentApplicationVersionId</code> or the <code>ConditionalToken</code>. You get the application's current <code>ConditionalToken</code> using <a>DescribeApplication</a>. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_application_configuration_exception.InvalidApplicationConfigurationException: <p>The user-provided application configuration is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.delete_application_vpc_configuration_request.DeleteApplicationVpcConfigurationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.delete_application_vpc_configuration_response.DeleteApplicationVpcConfigurationResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.delete_application_vpc_configuration

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.delete_application_vpc_configuration.delete_application_vpc_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.delete_application_vpc_configuration_request.DeleteApplicationVpcConfigurationRequest = {
            "application_name": application_name,
            "vpc_configuration_id": vpc_configuration_id,
        }
        if current_application_version_id is not None:
            input_["current_application_version_id"] = current_application_version_id
        if conditional_token is not None:
            input_["conditional_token"] = conditional_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_application(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        include_additional_details: Optional[
            "capo_kinesis_analytics_v2.types.boolean_object.BooleanObject"
        ] = None,
    ) -> "capo_kinesis_analytics_v2.types.describe_application_response.DescribeApplicationResponse":
        """<p>Returns information about a specific Managed Service for Apache Flink application.</p> <p>If you want to retrieve a list of all applications in your account, use the <a>ListApplications</a> operation.</p>

        Args:
            application_name: <p>The name of the application.</p>
            include_additional_details: <p>Displays verbose information about a Managed Service for Apache Flink application, including the application's job plan.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.describe_application_request.DescribeApplicationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.describe_application_response.DescribeApplicationResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.describe_application

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.describe_application.describe_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.describe_application_request.DescribeApplicationRequest = {
            "application_name": application_name
        }
        if include_additional_details is not None:
            input_["include_additional_details"] = include_additional_details

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_application_operation(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        operation_id: "capo_kinesis_analytics_v2.types.operation_id.OperationId",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
    ) -> "capo_kinesis_analytics_v2.types.describe_application_operation_response.DescribeApplicationOperationResponse":
        """<p>Provides a detailed description of a specified application operation. To see a list of all the operations of an application, invoke the <a>ListApplicationOperations</a> operation.</p> <note> <p>This operation is supported only for Managed Service for Apache Flink.</p> </note>

        Raises:
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.describe_application_operation_request.DescribeApplicationOperationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.describe_application_operation_response.DescribeApplicationOperationResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.describe_application_operation

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.describe_application_operation.describe_application_operation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.describe_application_operation_request.DescribeApplicationOperationRequest = {
            "application_name": application_name,
            "operation_id": operation_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_application_snapshot(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        snapshot_name: "capo_kinesis_analytics_v2.types.snapshot_name.SnapshotName",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
    ) -> "capo_kinesis_analytics_v2.types.describe_application_snapshot_response.DescribeApplicationSnapshotResponse":
        """<p>Returns information about a snapshot of application state data.</p>

        Args:
            application_name: <p>The name of an existing application.</p>
            snapshot_name: <p>The identifier of an application snapshot. You can retrieve this value using .</p>

        Raises:
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.describe_application_snapshot_request.DescribeApplicationSnapshotRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.describe_application_snapshot_response.DescribeApplicationSnapshotResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.describe_application_snapshot

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.describe_application_snapshot.describe_application_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.describe_application_snapshot_request.DescribeApplicationSnapshotRequest = {
            "application_name": application_name,
            "snapshot_name": snapshot_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_application_version(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        application_version_id: "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
    ) -> "capo_kinesis_analytics_v2.types.describe_application_version_response.DescribeApplicationVersionResponse":
        """<p>Provides a detailed description of a specified version of the application. To see a list of all the versions of an application, invoke the <a>ListApplicationVersions</a> operation.</p> <note> <p>This operation is supported only for Managed Service for Apache Flink.</p> </note>

        Args:
            application_name: <p>The name of the application for which you want to get the version description.</p>
            application_version_id: <p>The ID of the application version for which you want to get the description.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.describe_application_version_request.DescribeApplicationVersionRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.describe_application_version_response.DescribeApplicationVersionResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.describe_application_version

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.describe_application_version.describe_application_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.describe_application_version_request.DescribeApplicationVersionRequest = {
            "application_name": application_name,
            "application_version_id": application_version_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def discover_input_schema(
        self,
        service_execution_role: "capo_kinesis_analytics_v2.types.role_arn.RoleARN",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        resource_arn: Optional[
            "capo_kinesis_analytics_v2.types.resource_arn.ResourceARN"
        ] = None,
        input_starting_position_configuration: Optional[
            "capo_kinesis_analytics_v2.types.input_starting_position_configuration.InputStartingPositionConfiguration"
        ] = None,
        s3_configuration: Optional[
            "capo_kinesis_analytics_v2.types.s3_configuration.S3Configuration"
        ] = None,
        input_processing_configuration: Optional[
            "capo_kinesis_analytics_v2.types.input_processing_configuration.InputProcessingConfiguration"
        ] = None,
    ) -> "capo_kinesis_analytics_v2.types.discover_input_schema_response.DiscoverInputSchemaResponse":
        """<p>Infers a schema for a SQL-based Kinesis Data Analytics application by evaluating sample records on the specified streaming source (Kinesis data stream or Kinesis Data Firehose delivery stream) or Amazon S3 object. In the response, the operation returns the inferred schema and also the sample records that the operation used to infer the schema.</p> <p> You can use the inferred schema when configuring a streaming source for your application. When you create an application using the Kinesis Data Analytics console, the console uses this operation to infer a schema and show it in the console user interface. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the streaming source.</p>
            service_execution_role: <p>The ARN of the role that is used to access the streaming source.</p>
            input_starting_position_configuration: <p>The point at which you want Kinesis Data Analytics to start reading records from the specified streaming source for discovery purposes.</p>
            s3_configuration: <p>Specify this parameter to discover a schema from data in an Amazon S3 object.</p>
            input_processing_configuration: <p>The <a>InputProcessingConfiguration</a> to use to preprocess the records before discovering the schema of the records.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.resource_provisioned_throughput_exceeded_exception.ResourceProvisionedThroughputExceededException: <p>Discovery failed to get a record from the streaming source because of the Kinesis Streams <code>ProvisionedThroughputExceededException</code>. For more information, see <a href="http://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetRecords.html">GetRecords</a> in the Amazon Kinesis Streams API Reference.</p>
            capo_kinesis_analytics_v2.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_kinesis_analytics_v2.errors.unable_to_detect_schema_exception.UnableToDetectSchemaException: <p>The data format is not valid. Kinesis Data Analytics cannot detect the schema for the given streaming source.</p>
            capo_kinesis_analytics_v2.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.discover_input_schema_request.DiscoverInputSchemaRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.discover_input_schema_response.DiscoverInputSchemaResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.discover_input_schema

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.discover_input_schema.discover_input_schema(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.discover_input_schema_request.DiscoverInputSchemaRequest = {
            "service_execution_role": service_execution_role
        }
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if input_starting_position_configuration is not None:
            input_["input_starting_position_configuration"] = (
                input_starting_position_configuration
            )
        if s3_configuration is not None:
            input_["s3_configuration"] = s3_configuration
        if input_processing_configuration is not None:
            input_["input_processing_configuration"] = input_processing_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_application_operations(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        limit: Optional[
            "capo_kinesis_analytics_v2.types.list_application_operations_input_limit.ListApplicationOperationsInputLimit"
        ] = None,
        next_token: Optional[
            "capo_kinesis_analytics_v2.types.next_token.NextToken"
        ] = None,
        operation: Optional[
            "capo_kinesis_analytics_v2.types.operation.Operation"
        ] = None,
        operation_status: Optional[
            "capo_kinesis_analytics_v2.types.operation_status.OperationStatus"
        ] = None,
    ) -> "capo_kinesis_analytics_v2.types.list_application_operations_response.ListApplicationOperationsResponse":
        """<p>Lists all the operations performed for the specified application such as UpdateApplication, StartApplication etc. The response also includes a summary of the operation.</p> <p>To get the complete description of a specific operation, invoke the <a>DescribeApplicationOperation</a> operation.</p> <note> <p>This operation is supported only for Managed Service for Apache Flink.</p> </note>

        Raises:
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.list_application_operations_request.ListApplicationOperationsRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.list_application_operations_response.ListApplicationOperationsResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.list_application_operations

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.list_application_operations.list_application_operations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.list_application_operations_request.ListApplicationOperationsRequest = {
            "application_name": application_name
        }
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        if operation is not None:
            input_["operation"] = operation
        if operation_status is not None:
            input_["operation_status"] = operation_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_application_operations(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        limit: Optional[
            "capo_kinesis_analytics_v2.types.list_application_operations_input_limit.ListApplicationOperationsInputLimit"
        ] = None,
        next_token: Optional[
            "capo_kinesis_analytics_v2.types.next_token.NextToken"
        ] = None,
        operation: Optional[
            "capo_kinesis_analytics_v2.types.operation.Operation"
        ] = None,
        operation_status: Optional[
            "capo_kinesis_analytics_v2.types.operation_status.OperationStatus"
        ] = None,
    ) -> "Iterator[capo_kinesis_analytics_v2.types.application_operation_info.ApplicationOperationInfo]":
        _token = next_token
        while True:
            _response = self.list_application_operations(
                application_name,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
                operation=operation,
                operation_status=operation_status,
            )
            _page = _resolve_path(_response, ("application_operation_info_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_applications(
        self,
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        limit: Optional[
            "capo_kinesis_analytics_v2.types.list_applications_input_limit.ListApplicationsInputLimit"
        ] = None,
        next_token: Optional[
            "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
        ] = None,
    ) -> "capo_kinesis_analytics_v2.types.list_applications_response.ListApplicationsResponse":
        """<p>Returns a list of Managed Service for Apache Flink applications in your account. For each application, the response includes the application name, Amazon Resource Name (ARN), and status. </p> <p>If you want detailed information about a specific application, use <a>DescribeApplication</a>.</p>

        Args:
            limit: <p>The maximum number of applications to list.</p>
            next_token: <p>If a previous command returned a pagination token, pass it into this value to retrieve the next set of results. For more information about pagination, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/pagination.html">Using the Amazon Command Line Interface's Pagination Options</a>.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.list_applications_request.ListApplicationsRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.list_applications

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.list_applications_request.ListApplicationsRequest = {}
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_applications(
        self,
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        limit: Optional[
            "capo_kinesis_analytics_v2.types.list_applications_input_limit.ListApplicationsInputLimit"
        ] = None,
        next_token: Optional[
            "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
        ] = None,
    ) -> "Iterator[capo_kinesis_analytics_v2.types.application_summary.ApplicationSummary]":
        _token = next_token
        while True:
            _response = self.list_applications(
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("application_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_application_snapshots(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        limit: Optional[
            "capo_kinesis_analytics_v2.types.list_snapshots_input_limit.ListSnapshotsInputLimit"
        ] = None,
        next_token: Optional[
            "capo_kinesis_analytics_v2.types.next_token.NextToken"
        ] = None,
    ) -> "capo_kinesis_analytics_v2.types.list_application_snapshots_response.ListApplicationSnapshotsResponse":
        """<p>Lists information about the current application snapshots.</p>

        Args:
            application_name: <p>The name of an existing application.</p>
            limit: <p>The maximum number of application snapshots to list.</p>
            next_token: <p>Use this parameter if you receive a <code>NextToken</code> response in a previous request that indicates that there is more output available. Set it to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. </p>

        Raises:
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.list_application_snapshots_request.ListApplicationSnapshotsRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.list_application_snapshots_response.ListApplicationSnapshotsResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.list_application_snapshots

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.list_application_snapshots.list_application_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.list_application_snapshots_request.ListApplicationSnapshotsRequest = {
            "application_name": application_name
        }
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_application_snapshots(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        limit: Optional[
            "capo_kinesis_analytics_v2.types.list_snapshots_input_limit.ListSnapshotsInputLimit"
        ] = None,
        next_token: Optional[
            "capo_kinesis_analytics_v2.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_kinesis_analytics_v2.types.snapshot_details.SnapshotDetails]":
        _token = next_token
        while True:
            _response = self.list_application_snapshots(
                application_name,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("snapshot_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_application_versions(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        limit: Optional[
            "capo_kinesis_analytics_v2.types.list_application_versions_input_limit.ListApplicationVersionsInputLimit"
        ] = None,
        next_token: Optional[
            "capo_kinesis_analytics_v2.types.next_token.NextToken"
        ] = None,
    ) -> "capo_kinesis_analytics_v2.types.list_application_versions_response.ListApplicationVersionsResponse":
        """<p>Lists all the versions for the specified application, including versions that were rolled back. The response also includes a summary of the configuration associated with each version.</p> <p>To get the complete description of a specific application version, invoke the <a>DescribeApplicationVersion</a> operation.</p> <note> <p>This operation is supported only for Managed Service for Apache Flink.</p> </note>

        Args:
            application_name: <p>The name of the application for which you want to list all versions.</p>
            limit: <p>The maximum number of versions to list in this invocation of the operation.</p>
            next_token: <p>If a previous invocation of this operation returned a pagination token, pass it into this value to retrieve the next set of results. For more information about pagination, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/pagination.html">Using the Amazon Command Line Interface's Pagination Options</a>.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.list_application_versions_request.ListApplicationVersionsRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.list_application_versions_response.ListApplicationVersionsResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.list_application_versions

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.list_application_versions.list_application_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.list_application_versions_request.ListApplicationVersionsRequest = {
            "application_name": application_name
        }
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_application_versions(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        limit: Optional[
            "capo_kinesis_analytics_v2.types.list_application_versions_input_limit.ListApplicationVersionsInputLimit"
        ] = None,
        next_token: Optional[
            "capo_kinesis_analytics_v2.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_kinesis_analytics_v2.types.application_version_summary.ApplicationVersionSummary]":
        _token = next_token
        while True:
            _response = self.list_application_versions(
                application_name,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("application_version_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_kinesis_analytics_v2.types.kinesis_analytics_arn.KinesisAnalyticsARN",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
    ) -> "capo_kinesis_analytics_v2.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves the list of key-value tags assigned to the application. For more information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-tagging.html">Using Tagging</a>.</p>

        Args:
            resource_arn: <p>The ARN of the application for which to retrieve tags.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.list_tags_for_resource

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def rollback_application(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        current_application_version_id: "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
    ) -> "capo_kinesis_analytics_v2.types.rollback_application_response.RollbackApplicationResponse":
        """<p>Reverts the application to the previous running version. You can roll back an application if you suspect it is stuck in a transient status or in the running status. </p> <p>You can roll back an application only if it is in the <code>UPDATING</code>, <code>AUTOSCALING</code>, or <code>RUNNING</code> statuses.</p> <p>When you rollback an application, it loads state data from the last successful snapshot. If the application has no snapshots, Managed Service for Apache Flink rejects the rollback request.</p>

        Args:
            application_name: <p>The name of the application.</p>
            current_application_version_id: <p>The current application version ID. You can retrieve the application version ID using <a>DescribeApplication</a>.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.rollback_application_request.RollbackApplicationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.rollback_application_response.RollbackApplicationResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.rollback_application

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.rollback_application.rollback_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.rollback_application_request.RollbackApplicationRequest = {
            "application_name": application_name,
            "current_application_version_id": current_application_version_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_application(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        run_configuration: Optional[
            "capo_kinesis_analytics_v2.types.run_configuration.RunConfiguration"
        ] = None,
    ) -> "capo_kinesis_analytics_v2.types.start_application_response.StartApplicationResponse":
        """<p>Starts the specified Managed Service for Apache Flink application. After creating an application, you must exclusively call this operation to start your application.</p>

        Args:
            application_name: <p>The name of the application.</p>
            run_configuration: <p>Identifies the run configuration (start parameters) of a Managed Service for Apache Flink application.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.invalid_application_configuration_exception.InvalidApplicationConfigurationException: <p>The user-provided application configuration is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.start_application_request.StartApplicationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.start_application_response.StartApplicationResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.start_application

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.start_application.start_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.start_application_request.StartApplicationRequest = {
            "application_name": application_name
        }
        if run_configuration is not None:
            input_["run_configuration"] = run_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_application(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        force: Optional[
            "capo_kinesis_analytics_v2.types.boolean_object.BooleanObject"
        ] = None,
    ) -> "capo_kinesis_analytics_v2.types.stop_application_response.StopApplicationResponse":
        """<p>Stops the application from processing data. You can stop an application only if it is in the running status, unless you set the <code>Force</code> parameter to <code>true</code>.</p> <p>You can use the <a>DescribeApplication</a> operation to find the application status. </p> <p>Managed Service for Apache Flink takes a snapshot when the application is stopped, unless <code>Force</code> is set to <code>true</code>.</p>

        Args:
            application_name: <p>The name of the running application to stop.</p>
            force: <p>Set to <code>true</code> to force the application to stop. If you set <code>Force</code> to <code>true</code>, Managed Service for Apache Flink stops the application without taking a snapshot. </p> <note> <p>Force-stopping your application may lead to data loss or duplication. To prevent data loss or duplicate processing of data during application restarts, we recommend you to take frequent snapshots of your application.</p> </note> <p>You can only force stop a Managed Service for Apache Flink application. You can't force stop a SQL-based Kinesis Data Analytics application.</p> <p>The application must be in the <code>STARTING</code>, <code>UPDATING</code>, <code>STOPPING</code>, <code>AUTOSCALING</code>, or <code>RUNNING</code> status. </p>

        Raises:
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_application_configuration_exception.InvalidApplicationConfigurationException: <p>The user-provided application configuration is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.stop_application_request.StopApplicationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.stop_application_response.StopApplicationResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.stop_application

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.stop_application.stop_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.stop_application_request.StopApplicationRequest = {
            "application_name": application_name
        }
        if force is not None:
            input_["force"] = force

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_kinesis_analytics_v2.types.kinesis_analytics_arn.KinesisAnalyticsARN",
        tags: "capo_kinesis_analytics_v2.types.tags.Tags",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
    ) -> "capo_kinesis_analytics_v2.types.tag_resource_response.TagResourceResponse":
        """<p>Adds one or more key-value tags to a Managed Service for Apache Flink application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-tagging.html">Using Tagging</a>.</p>

        Args:
            resource_arn: <p>The ARN of the application to assign the tags.</p>
            tags: <p>The key-value tags to assign to the application.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.too_many_tags_exception.TooManyTagsException: <p>Application created with too many tags, or too many tags added to an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.tag_resource

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_kinesis_analytics_v2.types.kinesis_analytics_arn.KinesisAnalyticsARN",
        tag_keys: "capo_kinesis_analytics_v2.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
    ) -> (
        "capo_kinesis_analytics_v2.types.untag_resource_response.UntagResourceResponse"
    ):
        """<p>Removes one or more tags from a Managed Service for Apache Flink application. For more information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-tagging.html">Using Tagging</a>.</p>

        Args:
            resource_arn: <p>The ARN of the Managed Service for Apache Flink application from which to remove the tags.</p>
            tag_keys: <p>A list of keys of tags to remove from the specified application.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.too_many_tags_exception.TooManyTagsException: <p>Application created with too many tags, or too many tags added to an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.untag_resource

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_application(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
        current_application_version_id: Optional[
            "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
        ] = None,
        application_configuration_update: Optional[
            "capo_kinesis_analytics_v2.types.application_configuration_update.ApplicationConfigurationUpdate"
        ] = None,
        service_execution_role_update: Optional[
            "capo_kinesis_analytics_v2.types.role_arn.RoleARN"
        ] = None,
        run_configuration_update: Optional[
            "capo_kinesis_analytics_v2.types.run_configuration_update.RunConfigurationUpdate"
        ] = None,
        cloud_watch_logging_option_updates: Optional[
            "capo_kinesis_analytics_v2.types.cloud_watch_logging_option_updates.CloudWatchLoggingOptionUpdates"
        ] = None,
        conditional_token: Optional[
            "capo_kinesis_analytics_v2.types.conditional_token.ConditionalToken"
        ] = None,
        runtime_environment_update: Optional[
            "capo_kinesis_analytics_v2.types.runtime_environment.RuntimeEnvironment"
        ] = None,
    ) -> "capo_kinesis_analytics_v2.types.update_application_response.UpdateApplicationResponse":
        """<p>Updates an existing Managed Service for Apache Flink application. Using this operation, you can update application code, input configuration, and output configuration. </p> <p>Managed Service for Apache Flink updates the <code>ApplicationVersionId</code> each time you update your application. </p>

        Args:
            application_name: <p>The name of the application to update.</p>
            current_application_version_id: <p>The current application version ID. You must provide the <code>CurrentApplicationVersionId</code> or the <code>ConditionalToken</code>.You can retrieve the application version ID using <a>DescribeApplication</a>. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>
            application_configuration_update: <p>Describes application configuration updates.</p>
            service_execution_role_update: <p>Describes updates to the service execution role.</p>
            run_configuration_update: <p>Describes updates to the application's starting parameters.</p>
            cloud_watch_logging_option_updates: <p>Describes application Amazon CloudWatch logging option updates. You can only update existing CloudWatch logging options with this action. To add a new CloudWatch logging option, use <a>AddApplicationCloudWatchLoggingOption</a>.</p>
            conditional_token: <p>A value you use to implement strong concurrency for application updates. You must provide the <code>CurrentApplicationVersionId</code> or the <code>ConditionalToken</code>. You get the application's current <code>ConditionalToken</code> using <a>DescribeApplication</a>. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>
            runtime_environment_update: <p>Updates the Managed Service for Apache Flink runtime environment used to run your code. To avoid issues you must:</p> <ul> <li> <p>Ensure your new jar and dependencies are compatible with the new runtime selected.</p> </li> <li> <p>Ensure your new code's state is compatible with the snapshot from which your application will start</p> </li> </ul>

        Raises:
            capo_kinesis_analytics_v2.errors.code_validation_exception.CodeValidationException: <p>The user-provided application code (query) is not valid. This can be a simple syntax error.</p>
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_application_configuration_exception.InvalidApplicationConfigurationException: <p>The user-provided application configuration is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.invalid_request_exception.InvalidRequestException: <p>The request JSON is not valid for the operation.</p>
            capo_kinesis_analytics_v2.errors.limit_exceeded_exception.LimitExceededException: <p>The number of allowed resources has been exceeded.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.update_application_request.UpdateApplicationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.update_application

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.update_application_request.UpdateApplicationRequest = {
            "application_name": application_name
        }
        if current_application_version_id is not None:
            input_["current_application_version_id"] = current_application_version_id
        if application_configuration_update is not None:
            input_["application_configuration_update"] = (
                application_configuration_update
            )
        if service_execution_role_update is not None:
            input_["service_execution_role_update"] = service_execution_role_update
        if run_configuration_update is not None:
            input_["run_configuration_update"] = run_configuration_update
        if cloud_watch_logging_option_updates is not None:
            input_["cloud_watch_logging_option_updates"] = (
                cloud_watch_logging_option_updates
            )
        if conditional_token is not None:
            input_["conditional_token"] = conditional_token
        if runtime_environment_update is not None:
            input_["runtime_environment_update"] = runtime_environment_update

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_application_maintenance_configuration(
        self,
        application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName",
        application_maintenance_configuration_update: "capo_kinesis_analytics_v2.types.application_maintenance_configuration_update.ApplicationMaintenanceConfigurationUpdate",
        *,
        config_overrides: Optional[KinesisAnalyticsV2ClientConfig] = None,
    ) -> "capo_kinesis_analytics_v2.types.update_application_maintenance_configuration_response.UpdateApplicationMaintenanceConfigurationResponse":
        """<p>Updates the maintenance configuration of the Managed Service for Apache Flink application. </p> <p>You can invoke this operation on an application that is in one of the two following states: <code>READY</code> or <code>RUNNING</code>. If you invoke it when the application is in a state other than these two states, it throws a <code>ResourceInUseException</code>. The service makes use of the updated configuration the next time it schedules maintenance for the application. If you invoke this operation after the service schedules maintenance, the service will apply the configuration update the next time it schedules maintenance for the application. This means that you might not see the maintenance configuration update applied to the maintenance process that follows a successful invocation of this operation, but to the following maintenance process instead.</p> <p>To see the current maintenance configuration of your application, invoke the <a>DescribeApplication</a> operation.</p> <p>For information about application maintenance, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/java/maintenance.html">Managed Service for Apache Flink for Apache Flink Maintenance</a>.</p> <note> <p>This operation is supported only for Managed Service for Apache Flink.</p> </note>

        Args:
            application_name: <p>The name of the application for which you want to update the maintenance configuration.</p>
            application_maintenance_configuration_update: <p>Describes the application maintenance configuration update.</p>

        Raises:
            capo_kinesis_analytics_v2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.</p>
            capo_kinesis_analytics_v2.errors.invalid_argument_exception.InvalidArgumentException: <p>The specified input parameter value is not valid.</p>
            capo_kinesis_analytics_v2.errors.resource_in_use_exception.ResourceInUseException: <p>The application is not available for this operation.</p>
            capo_kinesis_analytics_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics_v2.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics_v2.types.update_application_maintenance_configuration_request.UpdateApplicationMaintenanceConfigurationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics_v2.types.update_application_maintenance_configuration_response.UpdateApplicationMaintenanceConfigurationResponse"
        ]:
            import capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.update_application_maintenance_configuration

            output, http_response = (
                capo_kinesis_analytics_v2._operations.kinesis_analytics_20180523.update_application_maintenance_configuration.update_application_maintenance_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics_v2.types.update_application_maintenance_configuration_request.UpdateApplicationMaintenanceConfigurationRequest = {
            "application_name": application_name,
            "application_maintenance_configuration_update": application_maintenance_configuration_update,
        }

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
