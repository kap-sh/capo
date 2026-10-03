"""Generated from Smithy shape ``com.amazonaws.mwaa#AmazonMWAA``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_mwaa._auth._signers
import capo_mwaa._auth._sigv4
from capo_mwaa._auth._identity import Credentials
from capo_mwaa._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_mwaa._auth._zapros_handler import AuthMiddleware
from capo_mwaa._pagination import resolve_path as _resolve_path
from capo_mwaa._services._aws_config import aaws_config
from capo_mwaa._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_mwaa.types.airflow_configuration_options
    import capo_mwaa.types.airflow_version
    import capo_mwaa.types.create_cli_token_request
    import capo_mwaa.types.create_cli_token_response
    import capo_mwaa.types.create_environment_input
    import capo_mwaa.types.create_environment_output
    import capo_mwaa.types.create_web_login_token_request
    import capo_mwaa.types.create_web_login_token_response
    import capo_mwaa.types.delete_environment_input
    import capo_mwaa.types.delete_environment_output
    import capo_mwaa.types.endpoint_management
    import capo_mwaa.types.environment_arn
    import capo_mwaa.types.environment_class
    import capo_mwaa.types.environment_name
    import capo_mwaa.types.get_environment_input
    import capo_mwaa.types.get_environment_output
    import capo_mwaa.types.iam_role_arn
    import capo_mwaa.types.invoke_rest_api_request
    import capo_mwaa.types.invoke_rest_api_response
    import capo_mwaa.types.kms_key
    import capo_mwaa.types.list_environments_input
    import capo_mwaa.types.list_environments_output
    import capo_mwaa.types.list_tags_for_resource_input
    import capo_mwaa.types.list_tags_for_resource_output
    import capo_mwaa.types.logging_configuration_input
    import capo_mwaa.types.max_webservers
    import capo_mwaa.types.max_workers
    import capo_mwaa.types.metric_data
    import capo_mwaa.types.min_webservers
    import capo_mwaa.types.min_workers
    import capo_mwaa.types.network_configuration
    import capo_mwaa.types.next_token
    import capo_mwaa.types.publish_metrics_input
    import capo_mwaa.types.publish_metrics_output
    import capo_mwaa.types.relative_path
    import capo_mwaa.types.rest_api_method
    import capo_mwaa.types.rest_api_path
    import capo_mwaa.types.rest_api_request_body
    import capo_mwaa.types.s3_bucket_arn
    import capo_mwaa.types.s3_object_version
    import capo_mwaa.types.schedulers
    import capo_mwaa.types.tag_key_list
    import capo_mwaa.types.tag_map
    import capo_mwaa.types.tag_resource_input
    import capo_mwaa.types.tag_resource_output
    import capo_mwaa.types.untag_resource_input
    import capo_mwaa.types.untag_resource_output
    import capo_mwaa.types.update_environment_input
    import capo_mwaa.types.update_environment_output
    import capo_mwaa.types.update_network_configuration_input
    import capo_mwaa.types.webserver_access_mode
    import capo_mwaa.types.weekly_maintenance_window_start
    import capo_mwaa.types.worker_replacement_strategy


class AsyncMWAAClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncMWAAClient:
    """A client for the ``MWAA`` service.

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
        self._config = AsyncMWAAClientConfig(
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
        self, config_overrides: Optional[AsyncMWAAClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMWAAClientConfig = config_overrides or {}
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

    async def create_cli_token(
        self,
        name: "capo_mwaa.types.environment_name.EnvironmentName",
        *,
        config_overrides: Optional[AsyncMWAAClientConfig] = None,
    ) -> "capo_mwaa.types.create_cli_token_response.CreateCliTokenResponse":
        """<p>Creates a CLI token for the Airflow CLI. To learn more, see <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/call-mwaa-apis-cli.html">Creating an Apache Airflow CLI token</a>.</p>

        Args:
            name: <p>The name of the Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.</p>

        Raises:
            capo_mwaa.errors.resource_not_found_exception.ResourceNotFoundException: <p>ResourceNotFoundException: The resource is not available.</p>
            capo_mwaa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa.types.create_cli_token_request.CreateCliTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_mwaa.types.create_cli_token_response.CreateCliTokenResponse"
        ]:
            import capo_mwaa._operations.amazon_mwaa.create_cli_token

            (
                output,
                http_response,
            ) = await capo_mwaa._operations.amazon_mwaa.create_cli_token.async_create_cli_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa.types.create_cli_token_request.CreateCliTokenRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_environment(
        self,
        name: "capo_mwaa.types.environment_name.EnvironmentName",
        execution_role_arn: "capo_mwaa.types.iam_role_arn.IamRoleArn",
        source_bucket_arn: "capo_mwaa.types.s3_bucket_arn.S3BucketArn",
        dag_s3_path: "capo_mwaa.types.relative_path.RelativePath",
        network_configuration: "capo_mwaa.types.network_configuration.NetworkConfiguration",
        *,
        config_overrides: Optional[AsyncMWAAClientConfig] = None,
        plugins_s3_path: Optional["capo_mwaa.types.relative_path.RelativePath"] = None,
        plugins_s3_object_version: Optional[
            "capo_mwaa.types.s3_object_version.S3ObjectVersion"
        ] = None,
        requirements_s3_path: Optional[
            "capo_mwaa.types.relative_path.RelativePath"
        ] = None,
        requirements_s3_object_version: Optional[
            "capo_mwaa.types.s3_object_version.S3ObjectVersion"
        ] = None,
        startup_script_s3_path: Optional[
            "capo_mwaa.types.relative_path.RelativePath"
        ] = None,
        startup_script_s3_object_version: Optional[
            "capo_mwaa.types.s3_object_version.S3ObjectVersion"
        ] = None,
        airflow_configuration_options: Optional[
            "capo_mwaa.types.airflow_configuration_options.AirflowConfigurationOptions"
        ] = None,
        environment_class: Optional[
            "capo_mwaa.types.environment_class.EnvironmentClass"
        ] = None,
        max_workers: Optional["capo_mwaa.types.max_workers.MaxWorkers"] = None,
        kms_key: Optional["capo_mwaa.types.kms_key.KmsKey"] = None,
        airflow_version: Optional[
            "capo_mwaa.types.airflow_version.AirflowVersion"
        ] = None,
        logging_configuration: Optional[
            "capo_mwaa.types.logging_configuration_input.LoggingConfigurationInput"
        ] = None,
        weekly_maintenance_window_start: Optional[
            "capo_mwaa.types.weekly_maintenance_window_start.WeeklyMaintenanceWindowStart"
        ] = None,
        tags: Optional["capo_mwaa.types.tag_map.TagMap"] = None,
        webserver_access_mode: Optional[
            "capo_mwaa.types.webserver_access_mode.WebserverAccessMode"
        ] = None,
        min_workers: Optional["capo_mwaa.types.min_workers.MinWorkers"] = None,
        schedulers: Optional["capo_mwaa.types.schedulers.Schedulers"] = None,
        endpoint_management: Optional[
            "capo_mwaa.types.endpoint_management.EndpointManagement"
        ] = None,
        min_webservers: Optional["capo_mwaa.types.min_webservers.MinWebservers"] = None,
        max_webservers: Optional["capo_mwaa.types.max_webservers.MaxWebservers"] = None,
    ) -> "capo_mwaa.types.create_environment_output.CreateEnvironmentOutput":
        """<p>Creates an Amazon Managed Workflows for Apache Airflow (Amazon MWAA) environment.</p>

        Args:
            name: <p>The name of the Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the execution role for your environment. An execution role is an Amazon Web Services Identity and Access Management (IAM) role that grants MWAA permission to access Amazon Web Services services and resources used by your environment. For example, <code>arn:aws:iam::123456789:role/my-execution-role</code>. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html">Amazon MWAA Execution role</a>.</p>
            source_bucket_arn: <p>The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG code and supporting files are stored. For example, <code>arn:aws:s3:::my-airflow-bucket-unique-name</code>. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html">Create an Amazon S3 bucket for Amazon MWAA</a>.</p>
            dag_s3_path: <p>The relative path to the DAGs folder on your Amazon S3 bucket. For example, <code>dags</code>. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-folder.html">Adding or updating DAGs</a>.</p>
            network_configuration: <p>The VPC networking components used to secure and enable network traffic between the Amazon Web Services resources for your environment. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html">About networking on Amazon MWAA</a>.</p>
            plugins_s3_path: <p>The relative path to the <code>plugins.zip</code> file on your Amazon S3 bucket. For example, <code>plugins.zip</code>. If specified, then the <code>plugins.zip</code> version is required. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html">Installing custom plugins</a>.</p>
            plugins_s3_object_version: <p>The version of the plugins.zip file on your Amazon S3 bucket. You must specify a version each time a plugins.zip file is updated. For more information, refer to <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html">How S3 Versioning works</a>.</p>
            requirements_s3_path: <p>The relative path to the <code>requirements.txt</code> file on your Amazon S3 bucket. For example, <code>requirements.txt</code>. If specified, then a version is required. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html">Installing Python dependencies</a>.</p>
            requirements_s3_object_version: <p>The version of the <code>requirements.txt</code> file on your Amazon S3 bucket. You must specify a version each time a requirements.txt file is updated. For more information, refer to <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html">How S3 Versioning works</a>.</p>
            startup_script_s3_path: <p>The relative path to the startup shell script in your Amazon S3 bucket. For example, <code>s3://mwaa-environment/startup.sh</code>.</p> <p> Amazon MWAA runs the script as your environment starts, and before running the Apache Airflow process. You can use this script to install dependencies, modify Apache Airflow configuration options, and set environment variables. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html">Using a startup script</a>. </p>
            startup_script_s3_object_version: <p>The version of the startup shell script in your Amazon S3 bucket. You must specify the <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html">version ID</a> that Amazon S3 assigns to the file every time you update the script. </p> <p> Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long. The following is an example: </p> <p> <code>3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo</code> </p> <p> For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html">Using a startup script</a>. </p>
            airflow_configuration_options: <p>A list of key-value pairs containing the Apache Airflow configuration options you want to attach to your environment. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html">Apache Airflow configuration options</a>.</p>
            environment_class: <p>The environment class type. Valid values: <code>mw1.micro</code>, <code>mw1.small</code>, <code>mw1.medium</code>, <code>mw1.large</code>, <code>mw1.xlarge</code>, and <code>mw1.2xlarge</code>. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html">Amazon MWAA environment class</a>.</p>
            max_workers: <p>The maximum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the <code>MaxWorkers</code> field. For example, <code>20</code>. When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the one worker that is included with your environment, or the number you specify in <code>MinWorkers</code>.</p>
            kms_key: <p>The Amazon Web Services Key Management Service (KMS) key to encrypt the data in your environment. You can use an Amazon Web Services owned CMK, or a Customer managed CMK (advanced). For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/create-environment.html">Create an Amazon MWAA environment</a>.</p>
            airflow_version: <p>The Apache Airflow version for your environment. If no value is specified, it defaults to the latest version. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/airflow-versions.html">Apache Airflow versions on Amazon Managed Workflows for Apache Airflow (Amazon MWAA)</a>.</p> <p>Valid values: <code>2.7.2</code>, <code>2.8.1</code>, <code>2.9.2</code>, <code>2.10.1</code>, <code>2.10.3</code>, <code>2.11.0</code>, and <code>3.0.6</code>.</p>
            logging_configuration: <p>Defines the Apache Airflow logs to send to CloudWatch Logs.</p>
            weekly_maintenance_window_start: <p>The day and time of the week in Coordinated Universal Time (UTC) 24-hour standard time to start weekly maintenance updates of your environment in the following format: <code>DAY:HH:MM</code>. For example: <code>TUE:03:30</code>. You can specify a start time in 30 minute increments only.</p>
            tags: <p>The key-value tag pairs you want to associate to your environment. For example, <code>"Environment": "Staging"</code>. For more information, refer to <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a>.</p>
            webserver_access_mode: <p>Defines the access mode for the Apache Airflow <i>web server</i>. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-networking.html">Apache Airflow access modes</a>.</p> <p>If set to <code>PUBLIC_AND_PRIVATE</code>, creates both a public network load balancer (NLB) for browser access and a private VPC endpoint (VPCE) for worker-to-webserver communication. This mode is only available for Apache Airflow version 3.2 and later.</p>
            min_workers: <p>The minimum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the <code>MaxWorkers</code> field. When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the worker count you specify in the <code>MinWorkers</code> field. For example, <code>2</code>.</p>
            schedulers: <p>The number of Apache Airflow schedulers to run in your environment. Valid values:</p> <ul> <li> <p>v2 - For environments larger than mw1.micro, accepts values from <code>2</code> to <code>5</code>. Defaults to <code>2</code> for all environment sizes except mw1.micro, which defaults to <code>1</code>.</p> </li> <li> <p>v1 - Accepts <code>1</code>.</p> </li> </ul>
            endpoint_management: <p>Defines whether the VPC endpoints configured for the environment are created, and managed, by the customer or by Amazon MWAA. If set to <code>SERVICE</code>, Amazon MWAA will create and manage the required VPC endpoints in your VPC. If set to <code>CUSTOMER</code>, you must create, and manage, the VPC endpoints for your VPC. If you choose to create an environment in a shared VPC, you must set this value to <code>CUSTOMER</code>. In a shared VPC deployment, the environment will remain in <code>PENDING</code> status until you create the VPC endpoints. If you do not take action to create the endpoints within 72 hours, the status will change to <code>CREATE_FAILED</code>. You can delete the failed environment and create a new one.</p>
            min_webservers: <p> The minimum number of web servers that you want to run in your environment. Amazon MWAA scales the number of Apache Airflow web servers up to the number you specify for <code>MaxWebservers</code> when you interact with your Apache Airflow environment using Apache Airflow REST API, or the Apache Airflow CLI. As the transaction-per-second rate, and the network load, decrease, Amazon MWAA disposes of the additional web servers, and scales down to the number set in <code>MinxWebserers</code>. </p> <p>Valid values: For environments larger than mw1.micro, accepts values from <code>2</code> to <code>5</code>. Defaults to <code>2</code> for all environment sizes except mw1.micro, which defaults to <code>1</code>.</p>
            max_webservers: <p> The maximum number of web servers that you want to run in your environment. Amazon MWAA scales the number of Apache Airflow web servers up to the number you specify for <code>MaxWebservers</code> when you interact with your Apache Airflow environment using Apache Airflow REST API, or the Apache Airflow CLI. For example, in scenarios where your workload requires network calls to the Apache Airflow REST API with a high transaction-per-second (TPS) rate, Amazon MWAA will increase the number of web servers up to the number set in <code>MaxWebserers</code>. As TPS rates decrease Amazon MWAA disposes of the additional web servers, and scales down to the number set in <code>MinxWebserers</code>. </p> <p>Valid values: For environments larger than mw1.micro, accepts values from <code>2</code> to <code>5</code>. Defaults to <code>2</code> for all environment sizes except mw1.micro, which defaults to <code>1</code>.</p>

        Raises:
            capo_mwaa.errors.internal_server_exception.InternalServerException: <p>InternalServerException: An internal error has occurred.</p>
            capo_mwaa.errors.service_unavailable_exception.ServiceUnavailableException: <p>ServiceUnavailableException: The service is currently unavailable.</p>
            capo_mwaa.errors.validation_exception.ValidationException: <p>ValidationException: The provided input is not valid.</p>
            capo_mwaa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa.types.create_environment_input.CreateEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "capo_mwaa.types.create_environment_output.CreateEnvironmentOutput"
        ]:
            import capo_mwaa._operations.amazon_mwaa.create_environment

            (
                output,
                http_response,
            ) = await capo_mwaa._operations.amazon_mwaa.create_environment.async_create_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa.types.create_environment_input.CreateEnvironmentInput = {
            "name": name,
            "execution_role_arn": execution_role_arn,
            "source_bucket_arn": source_bucket_arn,
            "dag_s3_path": dag_s3_path,
            "network_configuration": network_configuration,
        }
        if plugins_s3_path is not None:
            input_["plugins_s3_path"] = plugins_s3_path
        if plugins_s3_object_version is not None:
            input_["plugins_s3_object_version"] = plugins_s3_object_version
        if requirements_s3_path is not None:
            input_["requirements_s3_path"] = requirements_s3_path
        if requirements_s3_object_version is not None:
            input_["requirements_s3_object_version"] = requirements_s3_object_version
        if startup_script_s3_path is not None:
            input_["startup_script_s3_path"] = startup_script_s3_path
        if startup_script_s3_object_version is not None:
            input_["startup_script_s3_object_version"] = (
                startup_script_s3_object_version
            )
        if airflow_configuration_options is not None:
            input_["airflow_configuration_options"] = airflow_configuration_options
        if environment_class is not None:
            input_["environment_class"] = environment_class
        if max_workers is not None:
            input_["max_workers"] = max_workers
        if kms_key is not None:
            input_["kms_key"] = kms_key
        if airflow_version is not None:
            input_["airflow_version"] = airflow_version
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if weekly_maintenance_window_start is not None:
            input_["weekly_maintenance_window_start"] = weekly_maintenance_window_start
        if tags is not None:
            input_["tags"] = tags
        if webserver_access_mode is not None:
            input_["webserver_access_mode"] = webserver_access_mode
        if min_workers is not None:
            input_["min_workers"] = min_workers
        if schedulers is not None:
            input_["schedulers"] = schedulers
        if endpoint_management is not None:
            input_["endpoint_management"] = endpoint_management
        if min_webservers is not None:
            input_["min_webservers"] = min_webservers
        if max_webservers is not None:
            input_["max_webservers"] = max_webservers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_web_login_token(
        self,
        name: "capo_mwaa.types.environment_name.EnvironmentName",
        *,
        config_overrides: Optional[AsyncMWAAClientConfig] = None,
    ) -> "capo_mwaa.types.create_web_login_token_response.CreateWebLoginTokenResponse":
        """<p>Creates a web login token for the Airflow Web UI. To learn more, see <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/call-mwaa-apis-web.html">Creating an Apache Airflow web login token</a>.</p>

        Args:
            name: <p>The name of the Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.</p>

        Raises:
            capo_mwaa.errors.access_denied_exception.AccessDeniedException: <p>Access to the Apache Airflow Web UI or CLI has been denied due to insufficient permissions. To learn more, see <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/access-policies.html">Accessing an Amazon MWAA environment</a>.</p>
            capo_mwaa.errors.internal_server_exception.InternalServerException: <p>InternalServerException: An internal error has occurred.</p>
            capo_mwaa.errors.resource_not_found_exception.ResourceNotFoundException: <p>ResourceNotFoundException: The resource is not available.</p>
            capo_mwaa.errors.validation_exception.ValidationException: <p>ValidationException: The provided input is not valid.</p>
            capo_mwaa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa.types.create_web_login_token_request.CreateWebLoginTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_mwaa.types.create_web_login_token_response.CreateWebLoginTokenResponse"
        ]:
            import capo_mwaa._operations.amazon_mwaa.create_web_login_token

            (
                output,
                http_response,
            ) = await capo_mwaa._operations.amazon_mwaa.create_web_login_token.async_create_web_login_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa.types.create_web_login_token_request.CreateWebLoginTokenRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_environment(
        self,
        name: "capo_mwaa.types.environment_name.EnvironmentName",
        *,
        config_overrides: Optional[AsyncMWAAClientConfig] = None,
    ) -> "capo_mwaa.types.delete_environment_output.DeleteEnvironmentOutput":
        """<p>Deletes an Amazon Managed Workflows for Apache Airflow (Amazon MWAA) environment.</p>

        Args:
            name: <p>The name of the Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.</p>

        Raises:
            capo_mwaa.errors.internal_server_exception.InternalServerException: <p>InternalServerException: An internal error has occurred.</p>
            capo_mwaa.errors.resource_not_found_exception.ResourceNotFoundException: <p>ResourceNotFoundException: The resource is not available.</p>
            capo_mwaa.errors.service_unavailable_exception.ServiceUnavailableException: <p>ServiceUnavailableException: The service is currently unavailable.</p>
            capo_mwaa.errors.validation_exception.ValidationException: <p>ValidationException: The provided input is not valid.</p>
            capo_mwaa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa.types.delete_environment_input.DeleteEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "capo_mwaa.types.delete_environment_output.DeleteEnvironmentOutput"
        ]:
            import capo_mwaa._operations.amazon_mwaa.delete_environment

            (
                output,
                http_response,
            ) = await capo_mwaa._operations.amazon_mwaa.delete_environment.async_delete_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa.types.delete_environment_input.DeleteEnvironmentInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_environment(
        self,
        name: "capo_mwaa.types.environment_name.EnvironmentName",
        *,
        config_overrides: Optional[AsyncMWAAClientConfig] = None,
    ) -> "capo_mwaa.types.get_environment_output.GetEnvironmentOutput":
        """<p>Describes an Amazon Managed Workflows for Apache Airflow (MWAA) environment.</p>

        Args:
            name: <p>The name of the Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.</p>

        Raises:
            capo_mwaa.errors.internal_server_exception.InternalServerException: <p>InternalServerException: An internal error has occurred.</p>
            capo_mwaa.errors.resource_not_found_exception.ResourceNotFoundException: <p>ResourceNotFoundException: The resource is not available.</p>
            capo_mwaa.errors.validation_exception.ValidationException: <p>ValidationException: The provided input is not valid.</p>
            capo_mwaa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa.types.get_environment_input.GetEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "capo_mwaa.types.get_environment_output.GetEnvironmentOutput"
        ]:
            import capo_mwaa._operations.amazon_mwaa.get_environment

            (
                output,
                http_response,
            ) = await capo_mwaa._operations.amazon_mwaa.get_environment.async_get_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa.types.get_environment_input.GetEnvironmentInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def invoke_rest_api(
        self,
        name: "capo_mwaa.types.environment_name.EnvironmentName",
        path: "capo_mwaa.types.rest_api_path.RestApiPath",
        method: "capo_mwaa.types.rest_api_method.RestApiMethod",
        *,
        config_overrides: Optional[AsyncMWAAClientConfig] = None,
        query_parameters: Optional[object] = None,
        body: Optional[
            "capo_mwaa.types.rest_api_request_body.RestApiRequestBody"
        ] = None,
    ) -> "capo_mwaa.types.invoke_rest_api_response.InvokeRestApiResponse":
        """<p>Invokes the Apache Airflow REST API on the webserver with the specified inputs. To learn more, see <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/access-mwaa-apache-airflow-rest-api.html">Using the Apache Airflow REST API</a> </p>

        Args:
            name: <p>The name of the Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.</p>
            path: <p>The Apache Airflow REST API endpoint path to be called. For example, <code>/dags/123456/clearTaskInstances</code>. For more information, see <a href="https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html">Apache Airflow API</a> </p>
            method: <p>The HTTP method used for making Airflow REST API calls. For example, <code>POST</code>. </p>
            query_parameters: <p>Query parameters to be included in the Apache Airflow REST API call, provided as a JSON object. </p>
            body: <p>The request body for the Apache Airflow REST API call, provided as a JSON object.</p>

        Raises:
            capo_mwaa.errors.access_denied_exception.AccessDeniedException: <p>Access to the Apache Airflow Web UI or CLI has been denied due to insufficient permissions. To learn more, see <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/access-policies.html">Accessing an Amazon MWAA environment</a>.</p>
            capo_mwaa.errors.internal_server_exception.InternalServerException: <p>InternalServerException: An internal error has occurred.</p>
            capo_mwaa.errors.resource_not_found_exception.ResourceNotFoundException: <p>ResourceNotFoundException: The resource is not available.</p>
            capo_mwaa.errors.rest_api_client_exception.RestApiClientException: <p>An exception indicating that a client-side error occurred during the Apache Airflow REST API call.</p>
            capo_mwaa.errors.rest_api_server_exception.RestApiServerException: <p>An exception indicating that a server-side error occurred during the Apache Airflow REST API call.</p>
            capo_mwaa.errors.validation_exception.ValidationException: <p>ValidationException: The provided input is not valid.</p>
            capo_mwaa.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Listing Airflow variables.

            >>> await client.invoke_rest_api(name='MyEnvironment', path='/variables', method='GET')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa.types.invoke_rest_api_request.InvokeRestApiRequest]",
        ) -> AsyncOperationResponse[
            "capo_mwaa.types.invoke_rest_api_response.InvokeRestApiResponse"
        ]:
            import capo_mwaa._operations.amazon_mwaa.invoke_rest_api

            (
                output,
                http_response,
            ) = await capo_mwaa._operations.amazon_mwaa.invoke_rest_api.async_invoke_rest_api(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa.types.invoke_rest_api_request.InvokeRestApiRequest = {
            "name": name,
            "path": path,
            "method": method,
        }
        if query_parameters is not None:
            input_["query_parameters"] = query_parameters
        if body is not None:
            input_["body"] = body

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_environments(
        self,
        *,
        config_overrides: Optional[AsyncMWAAClientConfig] = None,
        next_token: Optional["capo_mwaa.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_mwaa.types.list_environments_output.ListEnvironmentsOutput":
        """<p>Lists the Amazon Managed Workflows for Apache Airflow (MWAA) environments.</p>

        Args:
            next_token: <p>Retrieves the next page of the results.</p>
            max_results: <p>The maximum number of results to retrieve per page. For example, <code>5</code> environments per page.</p>

        Raises:
            capo_mwaa.errors.internal_server_exception.InternalServerException: <p>InternalServerException: An internal error has occurred.</p>
            capo_mwaa.errors.validation_exception.ValidationException: <p>ValidationException: The provided input is not valid.</p>
            capo_mwaa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa.types.list_environments_input.ListEnvironmentsInput]",
        ) -> AsyncOperationResponse[
            "capo_mwaa.types.list_environments_output.ListEnvironmentsOutput"
        ]:
            import capo_mwaa._operations.amazon_mwaa.list_environments

            (
                output,
                http_response,
            ) = await capo_mwaa._operations.amazon_mwaa.list_environments.async_list_environments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa.types.list_environments_input.ListEnvironmentsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_environments(
        self,
        *,
        config_overrides: Optional[AsyncMWAAClientConfig] = None,
        next_token: Optional["capo_mwaa.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_mwaa.types.environment_name.EnvironmentName]":
        _token = next_token
        while True:
            _response = await self.list_environments(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("environments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_mwaa.types.environment_arn.EnvironmentArn",
        *,
        config_overrides: Optional[AsyncMWAAClientConfig] = None,
    ) -> "capo_mwaa.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the key-value tag pairs associated to the Amazon Managed Workflows for Apache Airflow (MWAA) environment. For example, <code>"Environment": "Staging"</code>. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon MWAA environment. For example, <code>arn:aws:airflow:us-east-1:123456789012:environment/MyMWAAEnvironment</code>.</p>

        Raises:
            capo_mwaa.errors.internal_server_exception.InternalServerException: <p>InternalServerException: An internal error has occurred.</p>
            capo_mwaa.errors.resource_not_found_exception.ResourceNotFoundException: <p>ResourceNotFoundException: The resource is not available.</p>
            capo_mwaa.errors.validation_exception.ValidationException: <p>ValidationException: The provided input is not valid.</p>
            capo_mwaa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_mwaa.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_mwaa._operations.amazon_mwaa.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_mwaa._operations.amazon_mwaa.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def publish_metrics(
        self,
        environment_name: "capo_mwaa.types.environment_name.EnvironmentName",
        metric_data: "capo_mwaa.types.metric_data.MetricData",
        *,
        config_overrides: Optional[AsyncMWAAClientConfig] = None,
    ) -> "capo_mwaa.types.publish_metrics_output.PublishMetricsOutput":
        """<p> <b>Internal only</b>. Publishes environment health metrics to Amazon CloudWatch.</p>

        Args:
            environment_name: <p> <b>Internal only</b>. The name of the environment.</p>
            metric_data: <p> <b>Internal only</b>. Publishes metrics to Amazon CloudWatch. To learn more about the metrics published to Amazon CloudWatch, see <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/cw-metrics.html">Amazon MWAA performance metrics in Amazon CloudWatch</a>.</p>

        Raises:
            capo_mwaa.errors.internal_server_exception.InternalServerException: <p>InternalServerException: An internal error has occurred.</p>
            capo_mwaa.errors.validation_exception.ValidationException: <p>ValidationException: The provided input is not valid.</p>
            capo_mwaa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa.types.publish_metrics_input.PublishMetricsInput]",
        ) -> AsyncOperationResponse[
            "capo_mwaa.types.publish_metrics_output.PublishMetricsOutput"
        ]:
            import capo_mwaa._operations.amazon_mwaa.publish_metrics

            (
                output,
                http_response,
            ) = await capo_mwaa._operations.amazon_mwaa.publish_metrics.async_publish_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa.types.publish_metrics_input.PublishMetricsInput = {
            "environment_name": environment_name,
            "metric_data": metric_data,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_mwaa.types.environment_arn.EnvironmentArn",
        tags: "capo_mwaa.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncMWAAClientConfig] = None,
    ) -> "capo_mwaa.types.tag_resource_output.TagResourceOutput":
        """<p>Associates key-value tag pairs to your Amazon Managed Workflows for Apache Airflow (MWAA) environment. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon MWAA environment. For example, <code>arn:aws:airflow:us-east-1:123456789012:environment/MyMWAAEnvironment</code>.</p>
            tags: <p>The key-value tag pairs you want to associate to your environment. For example, <code>"Environment": "Staging"</code>. For more information, refer to <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a>.</p>

        Raises:
            capo_mwaa.errors.internal_server_exception.InternalServerException: <p>InternalServerException: An internal error has occurred.</p>
            capo_mwaa.errors.resource_not_found_exception.ResourceNotFoundException: <p>ResourceNotFoundException: The resource is not available.</p>
            capo_mwaa.errors.validation_exception.ValidationException: <p>ValidationException: The provided input is not valid.</p>
            capo_mwaa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_mwaa.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_mwaa._operations.amazon_mwaa.tag_resource

            (
                output,
                http_response,
            ) = await capo_mwaa._operations.amazon_mwaa.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_mwaa.types.environment_arn.EnvironmentArn",
        tag_keys: "capo_mwaa.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncMWAAClientConfig] = None,
    ) -> "capo_mwaa.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes key-value tag pairs associated to your Amazon Managed Workflows for Apache Airflow (MWAA) environment. For example, <code>"Environment": "Staging"</code>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon MWAA environment. For example, <code>arn:aws:airflow:us-east-1:123456789012:environment/MyMWAAEnvironment</code>.</p>
            tag_keys: <p>The key-value tag pair you want to remove. For example, <code>"Environment": "Staging"</code>. </p>

        Raises:
            capo_mwaa.errors.internal_server_exception.InternalServerException: <p>InternalServerException: An internal error has occurred.</p>
            capo_mwaa.errors.resource_not_found_exception.ResourceNotFoundException: <p>ResourceNotFoundException: The resource is not available.</p>
            capo_mwaa.errors.validation_exception.ValidationException: <p>ValidationException: The provided input is not valid.</p>
            capo_mwaa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_mwaa.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_mwaa._operations.amazon_mwaa.untag_resource

            (
                output,
                http_response,
            ) = await capo_mwaa._operations.amazon_mwaa.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa.types.untag_resource_input.UntagResourceInput = {
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

    async def update_environment(
        self,
        name: "capo_mwaa.types.environment_name.EnvironmentName",
        *,
        config_overrides: Optional[AsyncMWAAClientConfig] = None,
        execution_role_arn: Optional["capo_mwaa.types.iam_role_arn.IamRoleArn"] = None,
        airflow_configuration_options: Optional[
            "capo_mwaa.types.airflow_configuration_options.AirflowConfigurationOptions"
        ] = None,
        airflow_version: Optional[
            "capo_mwaa.types.airflow_version.AirflowVersion"
        ] = None,
        dag_s3_path: Optional["capo_mwaa.types.relative_path.RelativePath"] = None,
        environment_class: Optional[
            "capo_mwaa.types.environment_class.EnvironmentClass"
        ] = None,
        logging_configuration: Optional[
            "capo_mwaa.types.logging_configuration_input.LoggingConfigurationInput"
        ] = None,
        max_workers: Optional["capo_mwaa.types.max_workers.MaxWorkers"] = None,
        min_workers: Optional["capo_mwaa.types.min_workers.MinWorkers"] = None,
        max_webservers: Optional["capo_mwaa.types.max_webservers.MaxWebservers"] = None,
        min_webservers: Optional["capo_mwaa.types.min_webservers.MinWebservers"] = None,
        worker_replacement_strategy: Optional[
            "capo_mwaa.types.worker_replacement_strategy.WorkerReplacementStrategy"
        ] = None,
        network_configuration: Optional[
            "capo_mwaa.types.update_network_configuration_input.UpdateNetworkConfigurationInput"
        ] = None,
        plugins_s3_path: Optional["capo_mwaa.types.relative_path.RelativePath"] = None,
        plugins_s3_object_version: Optional[
            "capo_mwaa.types.s3_object_version.S3ObjectVersion"
        ] = None,
        requirements_s3_path: Optional[
            "capo_mwaa.types.relative_path.RelativePath"
        ] = None,
        requirements_s3_object_version: Optional[
            "capo_mwaa.types.s3_object_version.S3ObjectVersion"
        ] = None,
        schedulers: Optional["capo_mwaa.types.schedulers.Schedulers"] = None,
        source_bucket_arn: Optional["capo_mwaa.types.s3_bucket_arn.S3BucketArn"] = None,
        startup_script_s3_path: Optional[
            "capo_mwaa.types.relative_path.RelativePath"
        ] = None,
        startup_script_s3_object_version: Optional[
            "capo_mwaa.types.s3_object_version.S3ObjectVersion"
        ] = None,
        webserver_access_mode: Optional[
            "capo_mwaa.types.webserver_access_mode.WebserverAccessMode"
        ] = None,
        weekly_maintenance_window_start: Optional[
            "capo_mwaa.types.weekly_maintenance_window_start.WeeklyMaintenanceWindowStart"
        ] = None,
    ) -> "capo_mwaa.types.update_environment_output.UpdateEnvironmentOutput":
        """<p>Updates an Amazon Managed Workflows for Apache Airflow (MWAA) environment.</p>

        Args:
            name: <p>The name of your Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the execution role in IAM that allows MWAA to access Amazon Web Services resources in your environment. For example, <code>arn:aws:iam::123456789:role/my-execution-role</code>. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html">Amazon MWAA Execution role</a>.</p>
            airflow_configuration_options: <p>A list of key-value pairs containing the Apache Airflow configuration options you want to attach to your environment. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html">Apache Airflow configuration options</a>.</p>
            airflow_version: <p>The Apache Airflow version for your environment. To upgrade your environment, specify a newer version of Apache Airflow supported by Amazon MWAA. To downgrade your environment, specify an older version of Apache Airflow supported by Amazon MWAA.</p> <p>Before you upgrade or downgrade an environment, make sure your requirements, DAGs, plugins, and other resources used in your workflows are compatible with the new Apache Airflow version. For more information about updating your resources, see <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/upgrading-environment.html">Upgrading and downgrading an Amazon MWAA environment</a>.</p> <p>Valid values: <code>2.7.2</code>, <code>2.8.1</code>, <code>2.9.2</code>, <code>2.10.1</code>, <code>2.10.3</code>, <code>2.11.0</code>, and <code>3.0.6</code>.</p>
            dag_s3_path: <p>The relative path to the DAGs folder on your Amazon S3 bucket. For example, <code>dags</code>. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-folder.html">Adding or updating DAGs</a>.</p>
            environment_class: <p>The environment class type. Valid values: <code>mw1.micro</code>, <code>mw1.small</code>, <code>mw1.medium</code>, <code>mw1.large</code>, <code>mw1.xlarge</code>, and <code>mw1.2xlarge</code>. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html">Amazon MWAA environment class</a>. </p>
            logging_configuration: <p>The Apache Airflow log types to send to CloudWatch Logs.</p>
            max_workers: <p>The maximum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the <code>MaxWorkers</code> field. For example, <code>20</code>. When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the one worker that is included with your environment, or the number you specify in <code>MinWorkers</code>.</p>
            min_workers: <p>The minimum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the <code>MaxWorkers</code> field. When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the worker count you specify in the <code>MinWorkers</code> field. For example, <code>2</code>.</p>
            max_webservers: <p> The maximum number of web servers that you want to run in your environment. Amazon MWAA scales the number of Apache Airflow web servers up to the number you specify for <code>MaxWebservers</code> when you interact with your Apache Airflow environment using Apache Airflow REST API, or the Apache Airflow CLI. For example, in scenarios where your workload requires network calls to the Apache Airflow REST API with a high transaction-per-second (TPS) rate, Amazon MWAA will increase the number of web servers up to the number set in <code>MaxWebserers</code>. As TPS rates decrease Amazon MWAA disposes of the additional web servers, and scales down to the number set in <code>MinxWebserers</code>. </p> <p>Valid values: For environments larger than mw1.micro, accepts values from <code>2</code> to <code>5</code>. Defaults to <code>2</code> for all environment sizes except mw1.micro, which defaults to <code>1</code>.</p>
            min_webservers: <p> The minimum number of web servers that you want to run in your environment. Amazon MWAA scales the number of Apache Airflow web servers up to the number you specify for <code>MaxWebservers</code> when you interact with your Apache Airflow environment using Apache Airflow REST API, or the Apache Airflow CLI. As the transaction-per-second rate, and the network load, decrease, Amazon MWAA disposes of the additional web servers, and scales down to the number set in <code>MinxWebserers</code>. </p> <p>Valid values: For environments larger than mw1.micro, accepts values from <code>2</code> to <code>5</code>. Defaults to <code>2</code> for all environment sizes except mw1.micro, which defaults to <code>1</code>.</p>
            worker_replacement_strategy: <p>The worker replacement strategy to use when updating the environment.</p> <p>You can select one of the following strategies:</p> <ul> <li> <p> <b>Forced -</b> Stops and replaces Apache Airflow workers without waiting for tasks to complete before an update.</p> </li> <li> <p> <b>Graceful -</b> Allows Apache Airflow workers to complete running tasks for up to 12 hours during an update before they're stopped and replaced.</p> </li> </ul>
            network_configuration: <p>The VPC networking components used to secure and enable network traffic between the Amazon Web Services resources for your environment. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html">About networking on Amazon MWAA</a>.</p>
            plugins_s3_path: <p>The relative path to the <code>plugins.zip</code> file on your Amazon S3 bucket. For example, <code>plugins.zip</code>. If specified, then the plugins.zip version is required. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html">Installing custom plugins</a>.</p>
            plugins_s3_object_version: <p>The version of the plugins.zip file on your Amazon S3 bucket. You must specify a version each time a <code>plugins.zip</code> file is updated. For more information, refer to <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html">How S3 Versioning works</a>.</p>
            requirements_s3_path: <p>The relative path to the <code>requirements.txt</code> file on your Amazon S3 bucket. For example, <code>requirements.txt</code>. If specified, then a file version is required. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html">Installing Python dependencies</a>.</p>
            requirements_s3_object_version: <p>The version of the requirements.txt file on your Amazon S3 bucket. You must specify a version each time a <code>requirements.txt</code> file is updated. For more information, refer to <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html">How S3 Versioning works</a>.</p>
            schedulers: <p>The number of Apache Airflow schedulers to run in your Amazon MWAA environment.</p>
            source_bucket_arn: <p>The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG code and supporting files are stored. For example, <code>arn:aws:s3:::my-airflow-bucket-unique-name</code>. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html">Create an Amazon S3 bucket for Amazon MWAA</a>.</p>
            startup_script_s3_path: <p>The relative path to the startup shell script in your Amazon S3 bucket. For example, <code>s3://mwaa-environment/startup.sh</code>.</p> <p> Amazon MWAA runs the script as your environment starts, and before running the Apache Airflow process. You can use this script to install dependencies, modify Apache Airflow configuration options, and set environment variables. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html">Using a startup script</a>. </p>
            startup_script_s3_object_version: <p> The version of the startup shell script in your Amazon S3 bucket. You must specify the <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html">version ID</a> that Amazon S3 assigns to the file every time you update the script. </p> <p> Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long. The following is an example: </p> <p> <code>3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo</code> </p> <p> For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html">Using a startup script</a>. </p>
            webserver_access_mode: <p>The Apache Airflow <i>Web server</i> access mode. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-networking.html">Apache Airflow access modes</a>.</p> <p>If set to <code>PUBLIC_AND_PRIVATE</code>, creates both a public network load balancer (NLB) for browser access and a private VPC endpoint (VPCE) for worker-to-webserver communication. This mode is only available for Apache Airflow version 3.2 and later.</p>
            weekly_maintenance_window_start: <p>The day and time of the week in Coordinated Universal Time (UTC) 24-hour standard time to start weekly maintenance updates of your environment in the following format: <code>DAY:HH:MM</code>. For example: <code>TUE:03:30</code>. You can specify a start time in 30 minute increments only.</p>

        Raises:
            capo_mwaa.errors.internal_server_exception.InternalServerException: <p>InternalServerException: An internal error has occurred.</p>
            capo_mwaa.errors.resource_not_found_exception.ResourceNotFoundException: <p>ResourceNotFoundException: The resource is not available.</p>
            capo_mwaa.errors.service_unavailable_exception.ServiceUnavailableException: <p>ServiceUnavailableException: The service is currently unavailable.</p>
            capo_mwaa.errors.validation_exception.ValidationException: <p>ValidationException: The provided input is not valid.</p>
            capo_mwaa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa.types.update_environment_input.UpdateEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "capo_mwaa.types.update_environment_output.UpdateEnvironmentOutput"
        ]:
            import capo_mwaa._operations.amazon_mwaa.update_environment

            (
                output,
                http_response,
            ) = await capo_mwaa._operations.amazon_mwaa.update_environment.async_update_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa.types.update_environment_input.UpdateEnvironmentInput = {
            "name": name
        }
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if airflow_configuration_options is not None:
            input_["airflow_configuration_options"] = airflow_configuration_options
        if airflow_version is not None:
            input_["airflow_version"] = airflow_version
        if dag_s3_path is not None:
            input_["dag_s3_path"] = dag_s3_path
        if environment_class is not None:
            input_["environment_class"] = environment_class
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if max_workers is not None:
            input_["max_workers"] = max_workers
        if min_workers is not None:
            input_["min_workers"] = min_workers
        if max_webservers is not None:
            input_["max_webservers"] = max_webservers
        if min_webservers is not None:
            input_["min_webservers"] = min_webservers
        if worker_replacement_strategy is not None:
            input_["worker_replacement_strategy"] = worker_replacement_strategy
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if plugins_s3_path is not None:
            input_["plugins_s3_path"] = plugins_s3_path
        if plugins_s3_object_version is not None:
            input_["plugins_s3_object_version"] = plugins_s3_object_version
        if requirements_s3_path is not None:
            input_["requirements_s3_path"] = requirements_s3_path
        if requirements_s3_object_version is not None:
            input_["requirements_s3_object_version"] = requirements_s3_object_version
        if schedulers is not None:
            input_["schedulers"] = schedulers
        if source_bucket_arn is not None:
            input_["source_bucket_arn"] = source_bucket_arn
        if startup_script_s3_path is not None:
            input_["startup_script_s3_path"] = startup_script_s3_path
        if startup_script_s3_object_version is not None:
            input_["startup_script_s3_object_version"] = (
                startup_script_s3_object_version
            )
        if webserver_access_mode is not None:
            input_["webserver_access_mode"] = webserver_access_mode
        if weekly_maintenance_window_start is not None:
            input_["weekly_maintenance_window_start"] = weekly_maintenance_window_start

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
