"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#KinesisAnalytics_20150814``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_kinesis_analytics._auth._signers
import capo_kinesis_analytics._auth._sigv4
from capo_kinesis_analytics._auth._identity import Credentials
from capo_kinesis_analytics._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_kinesis_analytics._auth._zapros_handler import AuthMiddleware
from capo_kinesis_analytics._services._aws_config import aws_config
from capo_kinesis_analytics._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.add_application_cloud_watch_logging_option_request
    import capo_kinesis_analytics.types.add_application_cloud_watch_logging_option_response
    import capo_kinesis_analytics.types.add_application_input_processing_configuration_request
    import capo_kinesis_analytics.types.add_application_input_processing_configuration_response
    import capo_kinesis_analytics.types.add_application_input_request
    import capo_kinesis_analytics.types.add_application_input_response
    import capo_kinesis_analytics.types.add_application_output_request
    import capo_kinesis_analytics.types.add_application_output_response
    import capo_kinesis_analytics.types.add_application_reference_data_source_request
    import capo_kinesis_analytics.types.add_application_reference_data_source_response
    import capo_kinesis_analytics.types.application_code
    import capo_kinesis_analytics.types.application_description
    import capo_kinesis_analytics.types.application_name
    import capo_kinesis_analytics.types.application_update
    import capo_kinesis_analytics.types.application_version_id
    import capo_kinesis_analytics.types.cloud_watch_logging_option
    import capo_kinesis_analytics.types.cloud_watch_logging_options
    import capo_kinesis_analytics.types.create_application_request
    import capo_kinesis_analytics.types.create_application_response
    import capo_kinesis_analytics.types.delete_application_cloud_watch_logging_option_request
    import capo_kinesis_analytics.types.delete_application_cloud_watch_logging_option_response
    import capo_kinesis_analytics.types.delete_application_input_processing_configuration_request
    import capo_kinesis_analytics.types.delete_application_input_processing_configuration_response
    import capo_kinesis_analytics.types.delete_application_output_request
    import capo_kinesis_analytics.types.delete_application_output_response
    import capo_kinesis_analytics.types.delete_application_reference_data_source_request
    import capo_kinesis_analytics.types.delete_application_reference_data_source_response
    import capo_kinesis_analytics.types.delete_application_request
    import capo_kinesis_analytics.types.delete_application_response
    import capo_kinesis_analytics.types.describe_application_request
    import capo_kinesis_analytics.types.describe_application_response
    import capo_kinesis_analytics.types.discover_input_schema_request
    import capo_kinesis_analytics.types.discover_input_schema_response
    import capo_kinesis_analytics.types.id
    import capo_kinesis_analytics.types.input
    import capo_kinesis_analytics.types.input_configurations
    import capo_kinesis_analytics.types.input_processing_configuration
    import capo_kinesis_analytics.types.input_starting_position_configuration
    import capo_kinesis_analytics.types.inputs
    import capo_kinesis_analytics.types.kinesis_analytics_arn
    import capo_kinesis_analytics.types.list_applications_input_limit
    import capo_kinesis_analytics.types.list_applications_request
    import capo_kinesis_analytics.types.list_applications_response
    import capo_kinesis_analytics.types.list_tags_for_resource_request
    import capo_kinesis_analytics.types.list_tags_for_resource_response
    import capo_kinesis_analytics.types.output
    import capo_kinesis_analytics.types.outputs
    import capo_kinesis_analytics.types.reference_data_source
    import capo_kinesis_analytics.types.resource_arn
    import capo_kinesis_analytics.types.role_arn
    import capo_kinesis_analytics.types.s3_configuration
    import capo_kinesis_analytics.types.start_application_request
    import capo_kinesis_analytics.types.start_application_response
    import capo_kinesis_analytics.types.stop_application_request
    import capo_kinesis_analytics.types.stop_application_response
    import capo_kinesis_analytics.types.tag_keys
    import capo_kinesis_analytics.types.tag_resource_request
    import capo_kinesis_analytics.types.tag_resource_response
    import capo_kinesis_analytics.types.tags
    import capo_kinesis_analytics.types.timestamp
    import capo_kinesis_analytics.types.untag_resource_request
    import capo_kinesis_analytics.types.untag_resource_response
    import capo_kinesis_analytics.types.update_application_request
    import capo_kinesis_analytics.types.update_application_response


class KinesisAnalyticsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class KinesisAnalyticsClient:
    """A client for the ``KinesisAnalytics`` service.

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
        self._config = KinesisAnalyticsClientConfig(
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
        self, config_overrides: Optional[KinesisAnalyticsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: KinesisAnalyticsClientConfig = config_overrides or {}
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
        application_name: "capo_kinesis_analytics.types.application_name.ApplicationName",
        current_application_version_id: "capo_kinesis_analytics.types.application_version_id.ApplicationVersionId",
        cloud_watch_logging_option: "capo_kinesis_analytics.types.cloud_watch_logging_option.CloudWatchLoggingOption",
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
    ) -> "capo_kinesis_analytics.types.add_application_cloud_watch_logging_option_response.AddApplicationCloudWatchLoggingOptionResponse":
        """<note> <p>This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see <a href="/kinesisanalytics/latest/apiv2/Welcome.html">Amazon Kinesis Data Analytics API V2 Documentation</a>.</p> </note> <p>Adds a CloudWatch log stream to monitor application configuration errors. For more information about using CloudWatch log streams with Amazon Kinesis Analytics applications, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-logs.html">Working with Amazon CloudWatch Logs</a>.</p>

        Args:
            application_name: <p>The Kinesis Analytics application name.</p>
            current_application_version_id: <p>The version ID of the Kinesis Analytics application.</p>
            cloud_watch_logging_option: <p>Provides the CloudWatch log stream Amazon Resource Name (ARN) and the IAM role ARN. Note: To write application messages to CloudWatch, the IAM role that is used must have the <code>PutLogEvents</code> policy action enabled.</p>

        Raises:
            capo_kinesis_analytics.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.</p>
            capo_kinesis_analytics.errors.invalid_argument_exception.InvalidArgumentException: <p>Specified input parameter value is invalid.</p>
            capo_kinesis_analytics.errors.resource_in_use_exception.ResourceInUseException: <p>Application is not available for this operation.</p>
            capo_kinesis_analytics.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.add_application_cloud_watch_logging_option_request.AddApplicationCloudWatchLoggingOptionRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.add_application_cloud_watch_logging_option_response.AddApplicationCloudWatchLoggingOptionResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.add_application_cloud_watch_logging_option

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.add_application_cloud_watch_logging_option.add_application_cloud_watch_logging_option(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.add_application_cloud_watch_logging_option_request.AddApplicationCloudWatchLoggingOptionRequest = {
            "application_name": application_name,
            "current_application_version_id": current_application_version_id,
            "cloud_watch_logging_option": cloud_watch_logging_option,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_application_input(
        self,
        application_name: "capo_kinesis_analytics.types.application_name.ApplicationName",
        current_application_version_id: "capo_kinesis_analytics.types.application_version_id.ApplicationVersionId",
        input: "capo_kinesis_analytics.types.input.Input",
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
    ) -> "capo_kinesis_analytics.types.add_application_input_response.AddApplicationInputResponse":
        """<note> <p>This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see <a href="/kinesisanalytics/latest/apiv2/Welcome.html">Amazon Kinesis Data Analytics API V2 Documentation</a>.</p> </note> <p> Adds a streaming source to your Amazon Kinesis application. For conceptual information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html">Configuring Application Input</a>. </p> <p>You can add a streaming source either when you create an application or you can use this operation to add a streaming source after you create an application. For more information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_CreateApplication.html">CreateApplication</a>.</p> <p>Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to find the current application version. </p> <p>This operation requires permissions to perform the <code>kinesisanalytics:AddApplicationInput</code> action.</p>

        Args:
            application_name: <p>Name of your existing Amazon Kinesis Analytics application to which you want to add the streaming source.</p>
            current_application_version_id: <p>Current version of your Amazon Kinesis Analytics application. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to find the current application version.</p>
            input: <p>The <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_Input.html">Input</a> to add.</p>

        Raises:
            capo_kinesis_analytics.errors.code_validation_exception.CodeValidationException: <p>User-provided application code (query) is invalid. This can be a simple syntax error.</p>
            capo_kinesis_analytics.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.</p>
            capo_kinesis_analytics.errors.invalid_argument_exception.InvalidArgumentException: <p>Specified input parameter value is invalid.</p>
            capo_kinesis_analytics.errors.resource_in_use_exception.ResourceInUseException: <p>Application is not available for this operation.</p>
            capo_kinesis_analytics.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.add_application_input_request.AddApplicationInputRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.add_application_input_response.AddApplicationInputResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.add_application_input

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.add_application_input.add_application_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.add_application_input_request.AddApplicationInputRequest = {
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
        application_name: "capo_kinesis_analytics.types.application_name.ApplicationName",
        current_application_version_id: "capo_kinesis_analytics.types.application_version_id.ApplicationVersionId",
        input_id: "capo_kinesis_analytics.types.id.Id",
        input_processing_configuration: "capo_kinesis_analytics.types.input_processing_configuration.InputProcessingConfiguration",
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
    ) -> "capo_kinesis_analytics.types.add_application_input_processing_configuration_response.AddApplicationInputProcessingConfigurationResponse":
        """<note> <p>This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see <a href="/kinesisanalytics/latest/apiv2/Welcome.html">Amazon Kinesis Data Analytics API V2 Documentation</a>.</p> </note> <p>Adds an <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html">InputProcessingConfiguration</a> to an application. An input processor preprocesses records on the input stream before the application's SQL code executes. Currently, the only input processor available is <a href="https://docs.aws.amazon.com/lambda/">AWS Lambda</a>.</p>

        Args:
            application_name: <p>Name of the application to which you want to add the input processing configuration.</p>
            current_application_version_id: <p>Version of the application to which you want to add the input processing configuration. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned.</p>
            input_id: <p>The ID of the input configuration to add the input processing configuration to. You can get a list of the input IDs for an application using the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation.</p>
            input_processing_configuration: <p>The <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html">InputProcessingConfiguration</a> to add to the application.</p>

        Raises:
            capo_kinesis_analytics.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.</p>
            capo_kinesis_analytics.errors.invalid_argument_exception.InvalidArgumentException: <p>Specified input parameter value is invalid.</p>
            capo_kinesis_analytics.errors.resource_in_use_exception.ResourceInUseException: <p>Application is not available for this operation.</p>
            capo_kinesis_analytics.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.add_application_input_processing_configuration_request.AddApplicationInputProcessingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.add_application_input_processing_configuration_response.AddApplicationInputProcessingConfigurationResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.add_application_input_processing_configuration

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.add_application_input_processing_configuration.add_application_input_processing_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.add_application_input_processing_configuration_request.AddApplicationInputProcessingConfigurationRequest = {
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
        application_name: "capo_kinesis_analytics.types.application_name.ApplicationName",
        current_application_version_id: "capo_kinesis_analytics.types.application_version_id.ApplicationVersionId",
        output: "capo_kinesis_analytics.types.output.Output",
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
    ) -> "capo_kinesis_analytics.types.add_application_output_response.AddApplicationOutputResponse":
        """<note> <p>This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see <a href="/kinesisanalytics/latest/apiv2/Welcome.html">Amazon Kinesis Data Analytics API V2 Documentation</a>.</p> </note> <p>Adds an external destination to your Amazon Kinesis Analytics application.</p> <p>If you want Amazon Kinesis Analytics to deliver data from an in-application stream within your application to an external destination (such as an Amazon Kinesis stream, an Amazon Kinesis Firehose delivery stream, or an AWS Lambda function), you add the relevant configuration to your application using this operation. You can configure one or more outputs for your application. Each output configuration maps an in-application stream and an external destination.</p> <p> You can use one of the output configurations to deliver data from your in-application error stream to an external destination so that you can analyze the errors. For more information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html">Understanding Application Output (Destination)</a>. </p> <p> Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to find the current application version.</p> <p>For the limits on the number of application inputs and outputs you can configure, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html">Limits</a>.</p> <p>This operation requires permissions to perform the <code>kinesisanalytics:AddApplicationOutput</code> action.</p>

        Args:
            application_name: <p>Name of the application to which you want to add the output configuration.</p>
            current_application_version_id: <p>Version of the application to which you want to add the output configuration. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned. </p>
            output: <p>An array of objects, each describing one output configuration. In the output configuration, you specify the name of an in-application stream, a destination (that is, an Amazon Kinesis stream, an Amazon Kinesis Firehose delivery stream, or an AWS Lambda function), and record the formation to use when writing to the destination.</p>

        Raises:
            capo_kinesis_analytics.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.</p>
            capo_kinesis_analytics.errors.invalid_argument_exception.InvalidArgumentException: <p>Specified input parameter value is invalid.</p>
            capo_kinesis_analytics.errors.resource_in_use_exception.ResourceInUseException: <p>Application is not available for this operation.</p>
            capo_kinesis_analytics.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.add_application_output_request.AddApplicationOutputRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.add_application_output_response.AddApplicationOutputResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.add_application_output

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.add_application_output.add_application_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.add_application_output_request.AddApplicationOutputRequest = {
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
        application_name: "capo_kinesis_analytics.types.application_name.ApplicationName",
        current_application_version_id: "capo_kinesis_analytics.types.application_version_id.ApplicationVersionId",
        reference_data_source: "capo_kinesis_analytics.types.reference_data_source.ReferenceDataSource",
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
    ) -> "capo_kinesis_analytics.types.add_application_reference_data_source_response.AddApplicationReferenceDataSourceResponse":
        """<note> <p>This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see <a href="/kinesisanalytics/latest/apiv2/Welcome.html">Amazon Kinesis Data Analytics API V2 Documentation</a>.</p> </note> <p>Adds a reference data source to an existing application.</p> <p>Amazon Kinesis Analytics reads reference data (that is, an Amazon S3 object) and creates an in-application table within your application. In the request, you provide the source (S3 bucket name and object key name), name of the in-application table to create, and the necessary mapping information that describes how data in Amazon S3 object maps to columns in the resulting in-application table.</p> <p> For conceptual information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html">Configuring Application Input</a>. For the limits on data sources you can add to your application, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html">Limits</a>. </p> <p> This operation requires permissions to perform the <code>kinesisanalytics:AddApplicationOutput</code> action. </p>

        Args:
            application_name: <p>Name of an existing application.</p>
            current_application_version_id: <p>Version of the application for which you are adding the reference data source. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned.</p>
            reference_data_source: <p>The reference data source can be an object in your Amazon S3 bucket. Amazon Kinesis Analytics reads the object and copies the data into the in-application table that is created. You provide an S3 bucket, object key name, and the resulting in-application table that is created. You must also provide an IAM role with the necessary permissions that Amazon Kinesis Analytics can assume to read the object from your S3 bucket on your behalf.</p>

        Raises:
            capo_kinesis_analytics.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.</p>
            capo_kinesis_analytics.errors.invalid_argument_exception.InvalidArgumentException: <p>Specified input parameter value is invalid.</p>
            capo_kinesis_analytics.errors.resource_in_use_exception.ResourceInUseException: <p>Application is not available for this operation.</p>
            capo_kinesis_analytics.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.add_application_reference_data_source_request.AddApplicationReferenceDataSourceRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.add_application_reference_data_source_response.AddApplicationReferenceDataSourceResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.add_application_reference_data_source

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.add_application_reference_data_source.add_application_reference_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.add_application_reference_data_source_request.AddApplicationReferenceDataSourceRequest = {
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

    def create_application(
        self,
        application_name: "capo_kinesis_analytics.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
        application_description: Optional[
            "capo_kinesis_analytics.types.application_description.ApplicationDescription"
        ] = None,
        inputs: Optional["capo_kinesis_analytics.types.inputs.Inputs"] = None,
        outputs: Optional["capo_kinesis_analytics.types.outputs.Outputs"] = None,
        cloud_watch_logging_options: Optional[
            "capo_kinesis_analytics.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
        ] = None,
        application_code: Optional[
            "capo_kinesis_analytics.types.application_code.ApplicationCode"
        ] = None,
        tags: Optional["capo_kinesis_analytics.types.tags.Tags"] = None,
    ) -> "capo_kinesis_analytics.types.create_application_response.CreateApplicationResponse":
        """<note> <p>This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see <a href="/kinesisanalytics/latest/apiv2/Welcome.html">Amazon Kinesis Data Analytics API V2 Documentation</a>.</p> </note> <p> Creates an Amazon Kinesis Analytics application. You can configure each application with one streaming source as input, application code to process the input, and up to three destinations where you want Amazon Kinesis Analytics to write the output data from your application. For an overview, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works.html">How it Works</a>. </p> <p>In the input configuration, you map the streaming source to an in-application stream, which you can think of as a constantly updating table. In the mapping, you must provide a schema for the in-application stream and map each data column in the in-application stream to a data element in the streaming source.</p> <p>Your application code is one or more SQL statements that read input data, transform it, and generate output. Your application code can create one or more SQL artifacts like SQL streams or pumps.</p> <p>In the output configuration, you can configure the application to write data from in-application streams created in your applications to up to three destinations.</p> <p> To read data from your source stream or write data to destination streams, Amazon Kinesis Analytics needs your permissions. You grant these permissions by creating IAM roles. This operation requires permissions to perform the <code>kinesisanalytics:CreateApplication</code> action. </p> <p> For introductory exercises to create an Amazon Kinesis Analytics application, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/getting-started.html">Getting Started</a>. </p>

        Args:
            application_name: <p>Name of your Amazon Kinesis Analytics application (for example, <code>sample-app</code>).</p>
            application_description: <p>Summary description of the application.</p>
            inputs: <p>Use this parameter to configure the application input.</p> <p>You can configure your application to receive input from a single streaming source. In this configuration, you map this streaming source to an in-application stream that is created. Your application code can then query the in-application stream like a table (you can think of it as a constantly updating table).</p> <p>For the streaming source, you provide its Amazon Resource Name (ARN) and format of data on the stream (for example, JSON, CSV, etc.). You also must provide an IAM role that Amazon Kinesis Analytics can assume to read this stream on your behalf.</p> <p>To create the in-application stream, you need to specify a schema to transform your data into a schematized version used in SQL. In the schema, you provide the necessary mapping of the data elements in the streaming source to record columns in the in-app stream.</p>
            outputs: <p>You can configure application output to write data from any of the in-application streams to up to three destinations.</p> <p>These destinations can be Amazon Kinesis streams, Amazon Kinesis Firehose delivery streams, AWS Lambda destinations, or any combination of the three.</p> <p>In the configuration, you specify the in-application stream name, the destination stream or Lambda function Amazon Resource Name (ARN), and the format to use when writing data. You must also provide an IAM role that Amazon Kinesis Analytics can assume to write to the destination stream or Lambda function on your behalf.</p> <p>In the output configuration, you also provide the output stream or Lambda function ARN. For stream destinations, you provide the format of data in the stream (for example, JSON, CSV). You also must provide an IAM role that Amazon Kinesis Analytics can assume to write to the stream or Lambda function on your behalf.</p>
            cloud_watch_logging_options: <p>Use this parameter to configure a CloudWatch log stream to monitor application configuration errors. For more information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-logs.html">Working with Amazon CloudWatch Logs</a>.</p>
            application_code: <p>One or more SQL statements that read input data, transform it, and generate output. For example, you can write a SQL statement that reads data from one in-application stream, generates a running average of the number of advertisement clicks by vendor, and insert resulting rows in another in-application stream using pumps. For more information about the typical pattern, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-app-code.html">Application Code</a>. </p> <p>You can provide such series of SQL statements, where output of one statement can be used as the input for the next statement. You store intermediate results by creating in-application streams and pumps.</p> <p>Note that the application code must create the streams with names specified in the <code>Outputs</code>. For example, if your <code>Outputs</code> defines output streams named <code>ExampleOutputStream1</code> and <code>ExampleOutputStream2</code>, then your application code must create these streams. </p>
            tags: <p>A list of one or more tags to assign to the application. A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html">Using Tagging</a>.</p>

        Raises:
            capo_kinesis_analytics.errors.code_validation_exception.CodeValidationException: <p>User-provided application code (query) is invalid. This can be a simple syntax error.</p>
            capo_kinesis_analytics.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.</p>
            capo_kinesis_analytics.errors.invalid_argument_exception.InvalidArgumentException: <p>Specified input parameter value is invalid.</p>
            capo_kinesis_analytics.errors.limit_exceeded_exception.LimitExceededException: <p>Exceeded the number of applications allowed.</p>
            capo_kinesis_analytics.errors.resource_in_use_exception.ResourceInUseException: <p>Application is not available for this operation.</p>
            capo_kinesis_analytics.errors.too_many_tags_exception.TooManyTagsException: <p>Application created with too many tags, or too many tags added to an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.</p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.create_application

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.create_application_request.CreateApplicationRequest = {
            "application_name": application_name
        }
        if application_description is not None:
            input_["application_description"] = application_description
        if inputs is not None:
            input_["inputs"] = inputs
        if outputs is not None:
            input_["outputs"] = outputs
        if cloud_watch_logging_options is not None:
            input_["cloud_watch_logging_options"] = cloud_watch_logging_options
        if application_code is not None:
            input_["application_code"] = application_code
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_application(
        self,
        application_name: "capo_kinesis_analytics.types.application_name.ApplicationName",
        create_timestamp: "capo_kinesis_analytics.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
    ) -> "capo_kinesis_analytics.types.delete_application_response.DeleteApplicationResponse":
        """<note> <p>This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see <a href="/kinesisanalytics/latest/apiv2/Welcome.html">Amazon Kinesis Data Analytics API V2 Documentation</a>.</p> </note> <p>Deletes the specified application. Amazon Kinesis Analytics halts application execution and deletes the application, including any application artifacts (such as in-application streams, reference table, and application code).</p> <p>This operation requires permissions to perform the <code>kinesisanalytics:DeleteApplication</code> action.</p>

        Args:
            application_name: <p>Name of the Amazon Kinesis Analytics application to delete.</p>
            create_timestamp: <p> You can use the <code>DescribeApplication</code> operation to get this value. </p>

        Raises:
            capo_kinesis_analytics.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.</p>
            capo_kinesis_analytics.errors.resource_in_use_exception.ResourceInUseException: <p>Application is not available for this operation.</p>
            capo_kinesis_analytics.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.delete_application

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.delete_application_request.DeleteApplicationRequest = {
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
        application_name: "capo_kinesis_analytics.types.application_name.ApplicationName",
        current_application_version_id: "capo_kinesis_analytics.types.application_version_id.ApplicationVersionId",
        cloud_watch_logging_option_id: "capo_kinesis_analytics.types.id.Id",
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
    ) -> "capo_kinesis_analytics.types.delete_application_cloud_watch_logging_option_response.DeleteApplicationCloudWatchLoggingOptionResponse":
        """<note> <p>This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see <a href="/kinesisanalytics/latest/apiv2/Welcome.html">Amazon Kinesis Data Analytics API V2 Documentation</a>.</p> </note> <p>Deletes a CloudWatch log stream from an application. For more information about using CloudWatch log streams with Amazon Kinesis Analytics applications, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-logs.html">Working with Amazon CloudWatch Logs</a>.</p>

        Args:
            application_name: <p>The Kinesis Analytics application name.</p>
            current_application_version_id: <p>The version ID of the Kinesis Analytics application.</p>
            cloud_watch_logging_option_id: <p>The <code>CloudWatchLoggingOptionId</code> of the CloudWatch logging option to delete. You can get the <code>CloudWatchLoggingOptionId</code> by using the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation. </p>

        Raises:
            capo_kinesis_analytics.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.</p>
            capo_kinesis_analytics.errors.invalid_argument_exception.InvalidArgumentException: <p>Specified input parameter value is invalid.</p>
            capo_kinesis_analytics.errors.resource_in_use_exception.ResourceInUseException: <p>Application is not available for this operation.</p>
            capo_kinesis_analytics.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.delete_application_cloud_watch_logging_option_request.DeleteApplicationCloudWatchLoggingOptionRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.delete_application_cloud_watch_logging_option_response.DeleteApplicationCloudWatchLoggingOptionResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.delete_application_cloud_watch_logging_option

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.delete_application_cloud_watch_logging_option.delete_application_cloud_watch_logging_option(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.delete_application_cloud_watch_logging_option_request.DeleteApplicationCloudWatchLoggingOptionRequest = {
            "application_name": application_name,
            "current_application_version_id": current_application_version_id,
            "cloud_watch_logging_option_id": cloud_watch_logging_option_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_application_input_processing_configuration(
        self,
        application_name: "capo_kinesis_analytics.types.application_name.ApplicationName",
        current_application_version_id: "capo_kinesis_analytics.types.application_version_id.ApplicationVersionId",
        input_id: "capo_kinesis_analytics.types.id.Id",
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
    ) -> "capo_kinesis_analytics.types.delete_application_input_processing_configuration_response.DeleteApplicationInputProcessingConfigurationResponse":
        """<note> <p>This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see <a href="/kinesisanalytics/latest/apiv2/Welcome.html">Amazon Kinesis Data Analytics API V2 Documentation</a>.</p> </note> <p>Deletes an <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html">InputProcessingConfiguration</a> from an input.</p>

        Args:
            application_name: <p>The Kinesis Analytics application name.</p>
            current_application_version_id: <p>The version ID of the Kinesis Analytics application.</p>
            input_id: <p>The ID of the input configuration from which to delete the input processing configuration. You can get a list of the input IDs for an application by using the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation.</p>

        Raises:
            capo_kinesis_analytics.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.</p>
            capo_kinesis_analytics.errors.invalid_argument_exception.InvalidArgumentException: <p>Specified input parameter value is invalid.</p>
            capo_kinesis_analytics.errors.resource_in_use_exception.ResourceInUseException: <p>Application is not available for this operation.</p>
            capo_kinesis_analytics.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.delete_application_input_processing_configuration_request.DeleteApplicationInputProcessingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.delete_application_input_processing_configuration_response.DeleteApplicationInputProcessingConfigurationResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.delete_application_input_processing_configuration

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.delete_application_input_processing_configuration.delete_application_input_processing_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.delete_application_input_processing_configuration_request.DeleteApplicationInputProcessingConfigurationRequest = {
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
        application_name: "capo_kinesis_analytics.types.application_name.ApplicationName",
        current_application_version_id: "capo_kinesis_analytics.types.application_version_id.ApplicationVersionId",
        output_id: "capo_kinesis_analytics.types.id.Id",
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
    ) -> "capo_kinesis_analytics.types.delete_application_output_response.DeleteApplicationOutputResponse":
        """<note> <p>This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see <a href="/kinesisanalytics/latest/apiv2/Welcome.html">Amazon Kinesis Data Analytics API V2 Documentation</a>.</p> </note> <p>Deletes output destination configuration from your application configuration. Amazon Kinesis Analytics will no longer write data from the corresponding in-application stream to the external output destination.</p> <p>This operation requires permissions to perform the <code>kinesisanalytics:DeleteApplicationOutput</code> action.</p>

        Args:
            application_name: <p>Amazon Kinesis Analytics application name.</p>
            current_application_version_id: <p>Amazon Kinesis Analytics application version. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned. </p>
            output_id: <p>The ID of the configuration to delete. Each output configuration that is added to the application, either when the application is created or later using the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationOutput.html">AddApplicationOutput</a> operation, has a unique ID. You need to provide the ID to uniquely identify the output configuration that you want to delete from the application configuration. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to get the specific <code>OutputId</code>. </p>

        Raises:
            capo_kinesis_analytics.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.</p>
            capo_kinesis_analytics.errors.invalid_argument_exception.InvalidArgumentException: <p>Specified input parameter value is invalid.</p>
            capo_kinesis_analytics.errors.resource_in_use_exception.ResourceInUseException: <p>Application is not available for this operation.</p>
            capo_kinesis_analytics.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.delete_application_output_request.DeleteApplicationOutputRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.delete_application_output_response.DeleteApplicationOutputResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.delete_application_output

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.delete_application_output.delete_application_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.delete_application_output_request.DeleteApplicationOutputRequest = {
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
        application_name: "capo_kinesis_analytics.types.application_name.ApplicationName",
        current_application_version_id: "capo_kinesis_analytics.types.application_version_id.ApplicationVersionId",
        reference_id: "capo_kinesis_analytics.types.id.Id",
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
    ) -> "capo_kinesis_analytics.types.delete_application_reference_data_source_response.DeleteApplicationReferenceDataSourceResponse":
        """<note> <p>This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see <a href="/kinesisanalytics/latest/apiv2/Welcome.html">Amazon Kinesis Data Analytics API V2 Documentation</a>.</p> </note> <p>Deletes a reference data source configuration from the specified application configuration.</p> <p>If the application is running, Amazon Kinesis Analytics immediately removes the in-application table that you created using the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationReferenceDataSource.html">AddApplicationReferenceDataSource</a> operation. </p> <p>This operation requires permissions to perform the <code>kinesisanalytics.DeleteApplicationReferenceDataSource</code> action.</p>

        Args:
            application_name: <p>Name of an existing application.</p>
            current_application_version_id: <p>Version of the application. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned.</p>
            reference_id: <p>ID of the reference data source. When you add a reference data source to your application using the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationReferenceDataSource.html">AddApplicationReferenceDataSource</a>, Amazon Kinesis Analytics assigns an ID. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to get the reference ID. </p>

        Raises:
            capo_kinesis_analytics.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.</p>
            capo_kinesis_analytics.errors.invalid_argument_exception.InvalidArgumentException: <p>Specified input parameter value is invalid.</p>
            capo_kinesis_analytics.errors.resource_in_use_exception.ResourceInUseException: <p>Application is not available for this operation.</p>
            capo_kinesis_analytics.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.delete_application_reference_data_source_request.DeleteApplicationReferenceDataSourceRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.delete_application_reference_data_source_response.DeleteApplicationReferenceDataSourceResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.delete_application_reference_data_source

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.delete_application_reference_data_source.delete_application_reference_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.delete_application_reference_data_source_request.DeleteApplicationReferenceDataSourceRequest = {
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

    def describe_application(
        self,
        application_name: "capo_kinesis_analytics.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
    ) -> "capo_kinesis_analytics.types.describe_application_response.DescribeApplicationResponse":
        """<note> <p>This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see <a href="/kinesisanalytics/latest/apiv2/Welcome.html">Amazon Kinesis Data Analytics API V2 Documentation</a>.</p> </note> <p>Returns information about a specific Amazon Kinesis Analytics application.</p> <p>If you want to retrieve a list of all applications in your account, use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_ListApplications.html">ListApplications</a> operation.</p> <p>This operation requires permissions to perform the <code>kinesisanalytics:DescribeApplication</code> action. You can use <code>DescribeApplication</code> to get the current application versionId, which you need to call other operations such as <code>Update</code>. </p>

        Args:
            application_name: <p>Name of the application.</p>

        Raises:
            capo_kinesis_analytics.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.describe_application_request.DescribeApplicationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.describe_application_response.DescribeApplicationResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.describe_application

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.describe_application.describe_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.describe_application_request.DescribeApplicationRequest = {
            "application_name": application_name
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
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
        resource_arn: Optional[
            "capo_kinesis_analytics.types.resource_arn.ResourceARN"
        ] = None,
        role_arn: Optional["capo_kinesis_analytics.types.role_arn.RoleARN"] = None,
        input_starting_position_configuration: Optional[
            "capo_kinesis_analytics.types.input_starting_position_configuration.InputStartingPositionConfiguration"
        ] = None,
        s3_configuration: Optional[
            "capo_kinesis_analytics.types.s3_configuration.S3Configuration"
        ] = None,
        input_processing_configuration: Optional[
            "capo_kinesis_analytics.types.input_processing_configuration.InputProcessingConfiguration"
        ] = None,
    ) -> "capo_kinesis_analytics.types.discover_input_schema_response.DiscoverInputSchemaResponse":
        """<note> <p>This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see <a href="/kinesisanalytics/latest/apiv2/Welcome.html">Amazon Kinesis Data Analytics API V2 Documentation</a>.</p> </note> <p>Infers a schema by evaluating sample records on the specified streaming source (Amazon Kinesis stream or Amazon Kinesis Firehose delivery stream) or S3 object. In the response, the operation returns the inferred schema and also the sample records that the operation used to infer the schema.</p> <p> You can use the inferred schema when configuring a streaming source for your application. For conceptual information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html">Configuring Application Input</a>. Note that when you create an application using the Amazon Kinesis Analytics console, the console uses this operation to infer a schema and show it in the console user interface. </p> <p> This operation requires permissions to perform the <code>kinesisanalytics:DiscoverInputSchema</code> action. </p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the streaming source.</p>
            role_arn: <p>ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf.</p>
            input_starting_position_configuration: <p>Point at which you want Amazon Kinesis Analytics to start reading records from the specified streaming source discovery purposes.</p>
            s3_configuration: <p>Specify this parameter to discover a schema from data in an Amazon S3 object.</p>
            input_processing_configuration: <p>The <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html">InputProcessingConfiguration</a> to use to preprocess the records before discovering the schema of the records.</p>

        Raises:
            capo_kinesis_analytics.errors.invalid_argument_exception.InvalidArgumentException: <p>Specified input parameter value is invalid.</p>
            capo_kinesis_analytics.errors.resource_provisioned_throughput_exceeded_exception.ResourceProvisionedThroughputExceededException: <p>Discovery failed to get a record from the streaming source because of the Amazon Kinesis Streams ProvisionedThroughputExceededException. For more information, see <a href="https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetRecords.html">GetRecords</a> in the Amazon Kinesis Streams API Reference.</p>
            capo_kinesis_analytics.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation. </p>
            capo_kinesis_analytics.errors.unable_to_detect_schema_exception.UnableToDetectSchemaException: <p>Data format is not valid. Amazon Kinesis Analytics is not able to detect schema for the given streaming source.</p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.discover_input_schema_request.DiscoverInputSchemaRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.discover_input_schema_response.DiscoverInputSchemaResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.discover_input_schema

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.discover_input_schema.discover_input_schema(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.discover_input_schema_request.DiscoverInputSchemaRequest = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if role_arn is not None:
            input_["role_arn"] = role_arn
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

    def list_applications(
        self,
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
        limit: Optional[
            "capo_kinesis_analytics.types.list_applications_input_limit.ListApplicationsInputLimit"
        ] = None,
        exclusive_start_application_name: Optional[
            "capo_kinesis_analytics.types.application_name.ApplicationName"
        ] = None,
    ) -> "capo_kinesis_analytics.types.list_applications_response.ListApplicationsResponse":
        """<note> <p>This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see <a href="/kinesisanalytics/latest/apiv2/Welcome.html">Amazon Kinesis Data Analytics API V2 Documentation</a>.</p> </note> <p>Returns a list of Amazon Kinesis Analytics applications in your account. For each application, the response includes the application name, Amazon Resource Name (ARN), and status. If the response returns the <code>HasMoreApplications</code> value as true, you can send another request by adding the <code>ExclusiveStartApplicationName</code> in the request body, and set the value of this to the last application name from the previous response. </p> <p>If you want detailed information about a specific application, use <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a>.</p> <p>This operation requires permissions to perform the <code>kinesisanalytics:ListApplications</code> action.</p>

        Args:
            limit: <p>Maximum number of applications to list.</p>
            exclusive_start_application_name: <p>Name of the application to start the list with. When using pagination to retrieve the list, you don't need to specify this parameter in the first request. However, in subsequent requests, you add the last application name from the previous response to get the next page of applications.</p>

        Raises:
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.list_applications_request.ListApplicationsRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.list_applications

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.list_applications_request.ListApplicationsRequest = {}
        if limit is not None:
            input_["limit"] = limit
        if exclusive_start_application_name is not None:
            input_["exclusive_start_application_name"] = (
                exclusive_start_application_name
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "capo_kinesis_analytics.types.kinesis_analytics_arn.KinesisAnalyticsARN",
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
    ) -> "capo_kinesis_analytics.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves the list of key-value tags assigned to the application. For more information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html">Using Tagging</a>.</p>

        Args:
            resource_arn: <p>The ARN of the application for which to retrieve tags.</p>

        Raises:
            capo_kinesis_analytics.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.</p>
            capo_kinesis_analytics.errors.invalid_argument_exception.InvalidArgumentException: <p>Specified input parameter value is invalid.</p>
            capo_kinesis_analytics.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.list_tags_for_resource

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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
        application_name: "capo_kinesis_analytics.types.application_name.ApplicationName",
        input_configurations: "capo_kinesis_analytics.types.input_configurations.InputConfigurations",
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
    ) -> "capo_kinesis_analytics.types.start_application_response.StartApplicationResponse":
        """<note> <p>This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see <a href="/kinesisanalytics/latest/apiv2/Welcome.html">Amazon Kinesis Data Analytics API V2 Documentation</a>.</p> </note> <p>Starts the specified Amazon Kinesis Analytics application. After creating an application, you must exclusively call this operation to start your application.</p> <p>After the application starts, it begins consuming the input data, processes it, and writes the output to the configured destination.</p> <p> The application status must be <code>READY</code> for you to start an application. You can get the application status in the console or using the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation.</p> <p>After you start the application, you can stop the application from processing the input by calling the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_StopApplication.html">StopApplication</a> operation.</p> <p>This operation requires permissions to perform the <code>kinesisanalytics:StartApplication</code> action.</p>

        Args:
            application_name: <p>Name of the application.</p>
            input_configurations: <p>Identifies the specific input, by ID, that the application starts consuming. Amazon Kinesis Analytics starts reading the streaming source associated with the input. You can also specify where in the streaming source you want Amazon Kinesis Analytics to start reading.</p>

        Raises:
            capo_kinesis_analytics.errors.invalid_application_configuration_exception.InvalidApplicationConfigurationException: <p>User-provided application configuration is not valid.</p>
            capo_kinesis_analytics.errors.invalid_argument_exception.InvalidArgumentException: <p>Specified input parameter value is invalid.</p>
            capo_kinesis_analytics.errors.resource_in_use_exception.ResourceInUseException: <p>Application is not available for this operation.</p>
            capo_kinesis_analytics.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.start_application_request.StartApplicationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.start_application_response.StartApplicationResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.start_application

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.start_application.start_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.start_application_request.StartApplicationRequest = {
            "application_name": application_name,
            "input_configurations": input_configurations,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_application(
        self,
        application_name: "capo_kinesis_analytics.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
    ) -> (
        "capo_kinesis_analytics.types.stop_application_response.StopApplicationResponse"
    ):
        """<note> <p>This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see <a href="/kinesisanalytics/latest/apiv2/Welcome.html">Amazon Kinesis Data Analytics API V2 Documentation</a>.</p> </note> <p>Stops the application from processing input data. You can stop an application only if it is in the running state. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to find the application state. After the application is stopped, Amazon Kinesis Analytics stops reading data from the input, the application stops processing data, and there is no output written to the destination. </p> <p>This operation requires permissions to perform the <code>kinesisanalytics:StopApplication</code> action.</p>

        Args:
            application_name: <p>Name of the running application to stop.</p>

        Raises:
            capo_kinesis_analytics.errors.resource_in_use_exception.ResourceInUseException: <p>Application is not available for this operation.</p>
            capo_kinesis_analytics.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.stop_application_request.StopApplicationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.stop_application_response.StopApplicationResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.stop_application

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.stop_application.stop_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.stop_application_request.StopApplicationRequest = {
            "application_name": application_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_kinesis_analytics.types.kinesis_analytics_arn.KinesisAnalyticsARN",
        tags: "capo_kinesis_analytics.types.tags.Tags",
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
    ) -> "capo_kinesis_analytics.types.tag_resource_response.TagResourceResponse":
        """<p>Adds one or more key-value tags to a Kinesis Analytics application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html">Using Tagging</a>.</p>

        Args:
            resource_arn: <p>The ARN of the application to assign the tags.</p>
            tags: <p>The key-value tags to assign to the application.</p>

        Raises:
            capo_kinesis_analytics.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.</p>
            capo_kinesis_analytics.errors.invalid_argument_exception.InvalidArgumentException: <p>Specified input parameter value is invalid.</p>
            capo_kinesis_analytics.errors.resource_in_use_exception.ResourceInUseException: <p>Application is not available for this operation.</p>
            capo_kinesis_analytics.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics.errors.too_many_tags_exception.TooManyTagsException: <p>Application created with too many tags, or too many tags added to an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.</p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.tag_resource

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_kinesis_analytics.types.kinesis_analytics_arn.KinesisAnalyticsARN",
        tag_keys: "capo_kinesis_analytics.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
    ) -> "capo_kinesis_analytics.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from a Kinesis Analytics application. For more information, see <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html">Using Tagging</a>.</p>

        Args:
            resource_arn: <p>The ARN of the Kinesis Analytics application from which to remove the tags.</p>
            tag_keys: <p>A list of keys of tags to remove from the specified application.</p>

        Raises:
            capo_kinesis_analytics.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.</p>
            capo_kinesis_analytics.errors.invalid_argument_exception.InvalidArgumentException: <p>Specified input parameter value is invalid.</p>
            capo_kinesis_analytics.errors.resource_in_use_exception.ResourceInUseException: <p>Application is not available for this operation.</p>
            capo_kinesis_analytics.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics.errors.too_many_tags_exception.TooManyTagsException: <p>Application created with too many tags, or too many tags added to an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.</p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.untag_resource

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.untag_resource_request.UntagResourceRequest = {
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
        application_name: "capo_kinesis_analytics.types.application_name.ApplicationName",
        current_application_version_id: "capo_kinesis_analytics.types.application_version_id.ApplicationVersionId",
        application_update: "capo_kinesis_analytics.types.application_update.ApplicationUpdate",
        *,
        config_overrides: Optional[KinesisAnalyticsClientConfig] = None,
    ) -> "capo_kinesis_analytics.types.update_application_response.UpdateApplicationResponse":
        """<note> <p>This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see <a href="/kinesisanalytics/latest/apiv2/Welcome.html">Amazon Kinesis Data Analytics API V2 Documentation</a>.</p> </note> <p>Updates an existing Amazon Kinesis Analytics application. Using this API, you can update application code, input configuration, and output configuration. </p> <p>Note that Amazon Kinesis Analytics updates the <code>CurrentApplicationVersionId</code> each time you update your application. </p> <p>This operation requires permission for the <code>kinesisanalytics:UpdateApplication</code> action.</p>

        Args:
            application_name: <p>Name of the Amazon Kinesis Analytics application to update.</p>
            current_application_version_id: <p>The current application version ID. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to get this value.</p>
            application_update: <p>Describes application updates.</p>

        Raises:
            capo_kinesis_analytics.errors.code_validation_exception.CodeValidationException: <p>User-provided application code (query) is invalid. This can be a simple syntax error.</p>
            capo_kinesis_analytics.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.</p>
            capo_kinesis_analytics.errors.invalid_argument_exception.InvalidArgumentException: <p>Specified input parameter value is invalid.</p>
            capo_kinesis_analytics.errors.resource_in_use_exception.ResourceInUseException: <p>Application is not available for this operation.</p>
            capo_kinesis_analytics.errors.resource_not_found_exception.ResourceNotFoundException: <p>Specified application can't be found.</p>
            capo_kinesis_analytics.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation. </p>
            capo_kinesis_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kinesis_analytics.types.update_application_request.UpdateApplicationRequest]",
        ) -> OperationResponse[
            "capo_kinesis_analytics.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_kinesis_analytics._operations.kinesis_analytics_20150814.update_application

            output, http_response = (
                capo_kinesis_analytics._operations.kinesis_analytics_20150814.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_analytics.types.update_application_request.UpdateApplicationRequest = {
            "application_name": application_name,
            "current_application_version_id": current_application_version_id,
            "application_update": application_update,
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
