"""Generated from Smithy shape ``com.amazonaws.emrserverless#AwsToledoWebService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_emr_serverless._auth._signers
import capo_emr_serverless._auth._sigv4
from capo_emr_serverless._auth._identity import Credentials
from capo_emr_serverless._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_emr_serverless._auth._zapros_handler import AuthMiddleware
from capo_emr_serverless._pagination import resolve_path as _resolve_path
from capo_emr_serverless._resources.aws_toledo_web_service.application_resource import (
    AsyncApplicationResource,
)
from capo_emr_serverless._resources.aws_toledo_web_service.job_run_resource import (
    AsyncJobRunResource,
)
from capo_emr_serverless._resources.aws_toledo_web_service.session_resource import (
    AsyncSessionResource,
)
from capo_emr_serverless._services._aws_config import aaws_config
from capo_emr_serverless._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_id
    import capo_emr_serverless.types.application_name
    import capo_emr_serverless.types.application_state_set
    import capo_emr_serverless.types.application_summary
    import capo_emr_serverless.types.architecture
    import capo_emr_serverless.types.attempt_number
    import capo_emr_serverless.types.auto_start_config
    import capo_emr_serverless.types.auto_stop_config
    import capo_emr_serverless.types.cancel_job_run_request
    import capo_emr_serverless.types.cancel_job_run_response
    import capo_emr_serverless.types.client_token
    import capo_emr_serverless.types.configuration_list
    import capo_emr_serverless.types.configuration_overrides
    import capo_emr_serverless.types.create_application_request
    import capo_emr_serverless.types.create_application_response
    import capo_emr_serverless.types.date
    import capo_emr_serverless.types.delete_application_request
    import capo_emr_serverless.types.delete_application_response
    import capo_emr_serverless.types.disk_encryption_configuration
    import capo_emr_serverless.types.duration
    import capo_emr_serverless.types.engine_type
    import capo_emr_serverless.types.get_application_request
    import capo_emr_serverless.types.get_application_response
    import capo_emr_serverless.types.get_dashboard_for_job_run_request
    import capo_emr_serverless.types.get_dashboard_for_job_run_response
    import capo_emr_serverless.types.get_job_run_request
    import capo_emr_serverless.types.get_job_run_response
    import capo_emr_serverless.types.get_resource_dashboard_request
    import capo_emr_serverless.types.get_resource_dashboard_response
    import capo_emr_serverless.types.get_session_endpoint_request
    import capo_emr_serverless.types.get_session_endpoint_response
    import capo_emr_serverless.types.get_session_request
    import capo_emr_serverless.types.get_session_response
    import capo_emr_serverless.types.iam_role_arn
    import capo_emr_serverless.types.identity_center_configuration_input
    import capo_emr_serverless.types.image_configuration_input
    import capo_emr_serverless.types.initial_capacity_config_map
    import capo_emr_serverless.types.interactive_configuration
    import capo_emr_serverless.types.job_driver
    import capo_emr_serverless.types.job_level_cost_allocation_configuration
    import capo_emr_serverless.types.job_run_attempt_summary
    import capo_emr_serverless.types.job_run_execution_iam_policy
    import capo_emr_serverless.types.job_run_id
    import capo_emr_serverless.types.job_run_mode
    import capo_emr_serverless.types.job_run_state_set
    import capo_emr_serverless.types.job_run_summary
    import capo_emr_serverless.types.list_applications_request
    import capo_emr_serverless.types.list_applications_response
    import capo_emr_serverless.types.list_job_run_attempts_request
    import capo_emr_serverless.types.list_job_run_attempts_response
    import capo_emr_serverless.types.list_job_runs_request
    import capo_emr_serverless.types.list_job_runs_response
    import capo_emr_serverless.types.list_sessions_request
    import capo_emr_serverless.types.list_sessions_response
    import capo_emr_serverless.types.list_tags_for_resource_request
    import capo_emr_serverless.types.list_tags_for_resource_response
    import capo_emr_serverless.types.maximum_allowed_resources
    import capo_emr_serverless.types.monitoring_configuration
    import capo_emr_serverless.types.network_configuration
    import capo_emr_serverless.types.next_token
    import capo_emr_serverless.types.release_label
    import capo_emr_serverless.types.resource_arn
    import capo_emr_serverless.types.resource_id
    import capo_emr_serverless.types.resource_type
    import capo_emr_serverless.types.retry_policy
    import capo_emr_serverless.types.scheduler_configuration
    import capo_emr_serverless.types.session_configuration_overrides
    import capo_emr_serverless.types.session_id
    import capo_emr_serverless.types.session_state_set
    import capo_emr_serverless.types.session_summary
    import capo_emr_serverless.types.shutdown_grace_period_in_seconds
    import capo_emr_serverless.types.start_application_request
    import capo_emr_serverless.types.start_application_response
    import capo_emr_serverless.types.start_job_run_request
    import capo_emr_serverless.types.start_job_run_response
    import capo_emr_serverless.types.start_session_request
    import capo_emr_serverless.types.start_session_response
    import capo_emr_serverless.types.stop_application_request
    import capo_emr_serverless.types.stop_application_response
    import capo_emr_serverless.types.string256
    import capo_emr_serverless.types.tag_key_list
    import capo_emr_serverless.types.tag_map
    import capo_emr_serverless.types.tag_resource_request
    import capo_emr_serverless.types.tag_resource_response
    import capo_emr_serverless.types.terminate_session_request
    import capo_emr_serverless.types.terminate_session_response
    import capo_emr_serverless.types.untag_resource_request
    import capo_emr_serverless.types.untag_resource_response
    import capo_emr_serverless.types.update_application_request
    import capo_emr_serverless.types.update_application_response
    import capo_emr_serverless.types.worker_type_specification_input_map


class AsyncEMRServerlessClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncEMRServerlessClient:
    """A client for the ``EMRServerless`` service.

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
        self._config = AsyncEMRServerlessClientConfig(
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

        # resources
        self.application_resource = AsyncApplicationResource(self)
        self.job_run_resource = AsyncJobRunResource(self)
        self.session_resource = AsyncSessionResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncEMRServerlessClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncEMRServerlessClientConfig = config_overrides or {}
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

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_emr_serverless.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags assigned to the resources.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource to list the tags for. Currently, the supported resources are Amazon EMR Serverless applications and job runs.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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
        resource_arn: "capo_emr_serverless.types.resource_arn.ResourceArn",
        tags: "capo_emr_serverless.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns tags to resources. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value, both of which you define. Tags enable you to categorize your Amazon Web Services resources by attributes such as purpose, owner, or environment. When you have many resources of the same type, you can quickly identify a specific resource based on the tags you've assigned to it. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource to list the tags for. Currently, the supported resources are Amazon EMR Serverless applications and job runs.</p>
            tags: <p>The tags to add to the resource. A tag is an array of key-value pairs.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_emr_serverless.types.resource_arn.ResourceArn",
        tag_keys: "capo_emr_serverless.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from resources.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource to list the tags for. Currently, the supported resources are Amazon EMR Serverless applications and job runs.</p>
            tag_keys: <p>The keys of the tags to be removed.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_application(
        self,
        release_label: "capo_emr_serverless.types.release_label.ReleaseLabel",
        type: "capo_emr_serverless.types.engine_type.EngineType",
        client_token: "capo_emr_serverless.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        name: Optional[
            "capo_emr_serverless.types.application_name.ApplicationName"
        ] = None,
        initial_capacity: Optional[
            "capo_emr_serverless.types.initial_capacity_config_map.InitialCapacityConfigMap"
        ] = None,
        maximum_capacity: Optional[
            "capo_emr_serverless.types.maximum_allowed_resources.MaximumAllowedResources"
        ] = None,
        tags: Optional["capo_emr_serverless.types.tag_map.TagMap"] = None,
        auto_start_configuration: Optional[
            "capo_emr_serverless.types.auto_start_config.AutoStartConfig"
        ] = None,
        auto_stop_configuration: Optional[
            "capo_emr_serverless.types.auto_stop_config.AutoStopConfig"
        ] = None,
        network_configuration: Optional[
            "capo_emr_serverless.types.network_configuration.NetworkConfiguration"
        ] = None,
        architecture: Optional[
            "capo_emr_serverless.types.architecture.Architecture"
        ] = None,
        image_configuration: Optional[
            "capo_emr_serverless.types.image_configuration_input.ImageConfigurationInput"
        ] = None,
        worker_type_specifications: Optional[
            "capo_emr_serverless.types.worker_type_specification_input_map.WorkerTypeSpecificationInputMap"
        ] = None,
        runtime_configuration: Optional[
            "capo_emr_serverless.types.configuration_list.ConfigurationList"
        ] = None,
        monitoring_configuration: Optional[
            "capo_emr_serverless.types.monitoring_configuration.MonitoringConfiguration"
        ] = None,
        disk_encryption_configuration: Optional[
            "capo_emr_serverless.types.disk_encryption_configuration.DiskEncryptionConfiguration"
        ] = None,
        interactive_configuration: Optional[
            "capo_emr_serverless.types.interactive_configuration.InteractiveConfiguration"
        ] = None,
        scheduler_configuration: Optional[
            "capo_emr_serverless.types.scheduler_configuration.SchedulerConfiguration"
        ] = None,
        identity_center_configuration: Optional[
            "capo_emr_serverless.types.identity_center_configuration_input.IdentityCenterConfigurationInput"
        ] = None,
        job_level_cost_allocation_configuration: Optional[
            "capo_emr_serverless.types.job_level_cost_allocation_configuration.JobLevelCostAllocationConfiguration"
        ] = None,
    ) -> "capo_emr_serverless.types.create_application_response.CreateApplicationResponse":
        r"""<p>Creates an application.</p>

        Args:
            name: <p>The name of the application.</p>
            release_label: <p>The Amazon EMR release associated with the application.</p>
            type: <p>The type of application you want to start, such as Spark or Hive.</p>
            client_token: <p>The client idempotency token of the application to create. Its value must be unique for each request.</p>
            initial_capacity: <p>The capacity to initialize when the application is created.</p>
            maximum_capacity: <p>The maximum capacity to allocate when the application is created. This is cumulative across all workers at any given point in time, not just when an application is created. No new resources will be created once any one of the defined limits is hit.</p>
            tags: <p>The tags assigned to the application.</p>
            auto_start_configuration: <p>The configuration for an application to automatically start on job submission.</p>
            auto_stop_configuration: <p>The configuration for an application to automatically stop after a certain amount of time being idle.</p>
            network_configuration: <p>The network configuration for customer VPC connectivity.</p>
            architecture: <p>The CPU architecture of an application.</p>
            image_configuration: <p>The image configuration for all worker types. You can either set this parameter or <code>imageConfiguration</code> for each worker type in <code>workerTypeSpecifications</code>.</p>
            worker_type_specifications: <p>The key-value pairs that specify worker type to <code>WorkerTypeSpecificationInput</code>. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include <code>Driver</code> and <code>Executor</code> for Spark applications and <code>HiveDriver</code> and <code>TezTask</code> for Hive applications. You can either set image details in this parameter for each worker type, or in <code>imageConfiguration</code> for all worker types.</p>
            runtime_configuration: <p>The <a href=\"https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html\">Configuration</a> specifications to use when creating an application. Each configuration consists of a classification and properties. This configuration is applied to all the job runs submitted under the application.</p>
            monitoring_configuration: <p>The configuration setting for monitoring.</p>
            disk_encryption_configuration: <p>The configuration object that allows encrypting local disks.</p>
            interactive_configuration: <p>The interactive configuration object that enables the interactive use cases to use when running an application.</p>
            scheduler_configuration: <p>The scheduler configuration for batch and streaming jobs running on this application. Supported with release labels emr-7.0.0 and above.</p>
            identity_center_configuration: <p>The IAM Identity Center Configuration accepts the Identity Center instance parameter required to enable trusted identity propagation. This configuration allows identity propagation between integrated services and the Identity Center instance.</p>
            job_level_cost_allocation_configuration: <p>The configuration object that enables job level cost allocation.</p>

        Raises:
            capo_emr_serverless.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.create_application_request.CreateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.create_application

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.create_application_request.CreateApplicationRequest = {
            "release_label": release_label,
            "type": type,
            "client_token": client_token,
        }
        if name is not None:
            input_["name"] = name
        if initial_capacity is not None:
            input_["initial_capacity"] = initial_capacity
        if maximum_capacity is not None:
            input_["maximum_capacity"] = maximum_capacity
        if tags is not None:
            input_["tags"] = tags
        if auto_start_configuration is not None:
            input_["auto_start_configuration"] = auto_start_configuration
        if auto_stop_configuration is not None:
            input_["auto_stop_configuration"] = auto_stop_configuration
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if architecture is not None:
            input_["architecture"] = architecture
        if image_configuration is not None:
            input_["image_configuration"] = image_configuration
        if worker_type_specifications is not None:
            input_["worker_type_specifications"] = worker_type_specifications
        if runtime_configuration is not None:
            input_["runtime_configuration"] = runtime_configuration
        if monitoring_configuration is not None:
            input_["monitoring_configuration"] = monitoring_configuration
        if disk_encryption_configuration is not None:
            input_["disk_encryption_configuration"] = disk_encryption_configuration
        if interactive_configuration is not None:
            input_["interactive_configuration"] = interactive_configuration
        if scheduler_configuration is not None:
            input_["scheduler_configuration"] = scheduler_configuration
        if identity_center_configuration is not None:
            input_["identity_center_configuration"] = identity_center_configuration
        if job_level_cost_allocation_configuration is not None:
            input_["job_level_cost_allocation_configuration"] = (
                job_level_cost_allocation_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_application(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.get_application_response.GetApplicationResponse":
        """<p>Displays detailed information about a specified application.</p>

        Args:
            application_id: <p>The ID of the application that will be described.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.get_application_request.GetApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.get_application_response.GetApplicationResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.get_application

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.get_application.async_get_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.get_application_request.GetApplicationRequest = {
            "application_id": application_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_application(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        client_token: "capo_emr_serverless.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        initial_capacity: Optional[
            "capo_emr_serverless.types.initial_capacity_config_map.InitialCapacityConfigMap"
        ] = None,
        maximum_capacity: Optional[
            "capo_emr_serverless.types.maximum_allowed_resources.MaximumAllowedResources"
        ] = None,
        auto_start_configuration: Optional[
            "capo_emr_serverless.types.auto_start_config.AutoStartConfig"
        ] = None,
        auto_stop_configuration: Optional[
            "capo_emr_serverless.types.auto_stop_config.AutoStopConfig"
        ] = None,
        network_configuration: Optional[
            "capo_emr_serverless.types.network_configuration.NetworkConfiguration"
        ] = None,
        architecture: Optional[
            "capo_emr_serverless.types.architecture.Architecture"
        ] = None,
        image_configuration: Optional[
            "capo_emr_serverless.types.image_configuration_input.ImageConfigurationInput"
        ] = None,
        worker_type_specifications: Optional[
            "capo_emr_serverless.types.worker_type_specification_input_map.WorkerTypeSpecificationInputMap"
        ] = None,
        interactive_configuration: Optional[
            "capo_emr_serverless.types.interactive_configuration.InteractiveConfiguration"
        ] = None,
        release_label: Optional[
            "capo_emr_serverless.types.release_label.ReleaseLabel"
        ] = None,
        runtime_configuration: Optional[
            "capo_emr_serverless.types.configuration_list.ConfigurationList"
        ] = None,
        monitoring_configuration: Optional[
            "capo_emr_serverless.types.monitoring_configuration.MonitoringConfiguration"
        ] = None,
        disk_encryption_configuration: Optional[
            "capo_emr_serverless.types.disk_encryption_configuration.DiskEncryptionConfiguration"
        ] = None,
        scheduler_configuration: Optional[
            "capo_emr_serverless.types.scheduler_configuration.SchedulerConfiguration"
        ] = None,
        identity_center_configuration: Optional[
            "capo_emr_serverless.types.identity_center_configuration_input.IdentityCenterConfigurationInput"
        ] = None,
        job_level_cost_allocation_configuration: Optional[
            "capo_emr_serverless.types.job_level_cost_allocation_configuration.JobLevelCostAllocationConfiguration"
        ] = None,
    ) -> "capo_emr_serverless.types.update_application_response.UpdateApplicationResponse":
        r"""<p>Updates a specified application. An application has to be in a stopped or created state in order to be updated.</p>

        Args:
            application_id: <p>The ID of the application to update.</p>
            client_token: <p>The client idempotency token of the application to update. Its value must be unique for each request.</p>
            initial_capacity: <p>The capacity to initialize when the application is updated.</p>
            maximum_capacity: <p>The maximum capacity to allocate when the application is updated. This is cumulative across all workers at any given point in time during the lifespan of the application. No new resources will be created once any one of the defined limits is hit.</p>
            auto_start_configuration: <p>The configuration for an application to automatically start on job submission.</p>
            auto_stop_configuration: <p>The configuration for an application to automatically stop after a certain amount of time being idle.</p>
            architecture: <p>The CPU architecture of an application.</p>
            image_configuration: <p>The image configuration to be used for all worker types. You can either set this parameter or <code>imageConfiguration</code> for each worker type in <code>WorkerTypeSpecificationInput</code>.</p>
            worker_type_specifications: <p>The key-value pairs that specify worker type to <code>WorkerTypeSpecificationInput</code>. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include <code>Driver</code> and <code>Executor</code> for Spark applications and <code>HiveDriver</code> and <code>TezTask</code> for Hive applications. You can either set image details in this parameter for each worker type, or in <code>imageConfiguration</code> for all worker types.</p>
            interactive_configuration: <p>The interactive configuration object that contains new interactive use cases when the application is updated.</p>
            release_label: <p>The Amazon EMR release label for the application. You can change the release label to use a different release of Amazon EMR.</p>
            runtime_configuration: <p>The <a href=\"https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html\">Configuration</a> specifications to use when updating an application. Each configuration consists of a classification and properties. This configuration is applied across all the job runs submitted under the application.</p>
            monitoring_configuration: <p>The configuration setting for monitoring.</p>
            disk_encryption_configuration: <p>The configuration object that allows encrypting local disks.</p>
            scheduler_configuration: <p>The scheduler configuration for batch and streaming jobs running on this application. Supported with release labels emr-7.0.0 and above.</p>
            identity_center_configuration: <p>Specifies the IAM Identity Center configuration used to enable or disable trusted identity propagation. When provided, this configuration determines how the application interacts with IAM Identity Center for user authentication and access control.</p>
            job_level_cost_allocation_configuration: <p>The configuration object that enables job level cost allocation.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.update_application_request.UpdateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.update_application

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.update_application.async_update_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.update_application_request.UpdateApplicationRequest = {
            "application_id": application_id,
            "client_token": client_token,
        }
        if initial_capacity is not None:
            input_["initial_capacity"] = initial_capacity
        if maximum_capacity is not None:
            input_["maximum_capacity"] = maximum_capacity
        if auto_start_configuration is not None:
            input_["auto_start_configuration"] = auto_start_configuration
        if auto_stop_configuration is not None:
            input_["auto_stop_configuration"] = auto_stop_configuration
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if architecture is not None:
            input_["architecture"] = architecture
        if image_configuration is not None:
            input_["image_configuration"] = image_configuration
        if worker_type_specifications is not None:
            input_["worker_type_specifications"] = worker_type_specifications
        if interactive_configuration is not None:
            input_["interactive_configuration"] = interactive_configuration
        if release_label is not None:
            input_["release_label"] = release_label
        if runtime_configuration is not None:
            input_["runtime_configuration"] = runtime_configuration
        if monitoring_configuration is not None:
            input_["monitoring_configuration"] = monitoring_configuration
        if disk_encryption_configuration is not None:
            input_["disk_encryption_configuration"] = disk_encryption_configuration
        if scheduler_configuration is not None:
            input_["scheduler_configuration"] = scheduler_configuration
        if identity_center_configuration is not None:
            input_["identity_center_configuration"] = identity_center_configuration
        if job_level_cost_allocation_configuration is not None:
            input_["job_level_cost_allocation_configuration"] = (
                job_level_cost_allocation_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_application(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.delete_application_response.DeleteApplicationResponse":
        """<p>Deletes an application. An application has to be in a stopped or created state in order to be deleted.</p>

        Args:
            application_id: <p>The ID of the application that will be deleted.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.delete_application_request.DeleteApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.delete_application

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.delete_application.async_delete_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.delete_application_request.DeleteApplicationRequest = {
            "application_id": application_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_applications(
        self,
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        next_token: Optional["capo_emr_serverless.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
        states: Optional[
            "capo_emr_serverless.types.application_state_set.ApplicationStateSet"
        ] = None,
    ) -> (
        "capo_emr_serverless.types.list_applications_response.ListApplicationsResponse"
    ):
        """<p>Lists applications based on a set of parameters.</p>

        Args:
            next_token: <p>The token for the next set of application results.</p>
            max_results: <p>The maximum number of applications that can be listed.</p>
            states: <p>An optional filter for application states. Note that if this filter contains multiple states, the resulting list will be grouped by the state.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.list_applications_request.ListApplicationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.list_applications

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.list_applications.async_list_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.list_applications_request.ListApplicationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if states is not None:
            input_["states"] = states

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_applications(
        self,
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        next_token: Optional["capo_emr_serverless.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
        states: Optional[
            "capo_emr_serverless.types.application_state_set.ApplicationStateSet"
        ] = None,
    ) -> "AsyncIterator[capo_emr_serverless.types.application_summary.ApplicationSummary]":
        _token = next_token
        while True:
            _response = await self.list_applications(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                states=states,
            )
            _page = _resolve_path(_response, ("applications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_resource_dashboard(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        resource_id: "capo_emr_serverless.types.resource_id.ResourceId",
        resource_type: "capo_emr_serverless.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.get_resource_dashboard_response.GetResourceDashboardResponse":
        """<p>Returns a URL that you can use to access the application UIs for a specified resource, such as a session.</p> <p>For resources in a running state, the application UI is a live user interface such as the Spark web UI. For terminated resources, the application UI is a persistent application user interface such as the Spark History Server.</p> <note> <p>The URL is valid for one hour after you generate it. To access the application UI after that hour elapses, you must invoke the API again to generate a new URL.</p> </note>

        Args:
            application_id: <p>The ID of the application that the resource belongs to.</p>
            resource_id: <p>The ID of the resource.</p>
            resource_type: <p>The type of resource to access the dashboard for. Currently, only <code>Session</code> is supported.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.get_resource_dashboard_request.GetResourceDashboardRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.get_resource_dashboard_response.GetResourceDashboardResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.get_resource_dashboard

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.get_resource_dashboard.async_get_resource_dashboard(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.get_resource_dashboard_request.GetResourceDashboardRequest = {
            "application_id": application_id,
            "resource_id": resource_id,
            "resource_type": resource_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_application(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
    ) -> (
        "capo_emr_serverless.types.start_application_response.StartApplicationResponse"
    ):
        """<p>Starts a specified application and initializes initial capacity if configured.</p>

        Args:
            application_id: <p>The ID of the application to start.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The maximum number of resources per account has been reached.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.start_application_request.StartApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.start_application_response.StartApplicationResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.start_application

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.start_application.async_start_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.start_application_request.StartApplicationRequest = {
            "application_id": application_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_application(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.stop_application_response.StopApplicationResponse":
        """<p>Stops a specified application and releases initial capacity if configured. All scheduled and running jobs must be completed or cancelled before stopping an application.</p>

        Args:
            application_id: <p>The ID of the application to stop.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.stop_application_request.StopApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.stop_application_response.StopApplicationResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.stop_application

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.stop_application.async_stop_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.stop_application_request.StopApplicationRequest = {
            "application_id": application_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_job_run(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        client_token: "capo_emr_serverless.types.client_token.ClientToken",
        execution_role_arn: "capo_emr_serverless.types.iam_role_arn.IAMRoleArn",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        execution_iam_policy: Optional[
            "capo_emr_serverless.types.job_run_execution_iam_policy.JobRunExecutionIamPolicy"
        ] = None,
        job_driver: Optional["capo_emr_serverless.types.job_driver.JobDriver"] = None,
        configuration_overrides: Optional[
            "capo_emr_serverless.types.configuration_overrides.ConfigurationOverrides"
        ] = None,
        tags: Optional["capo_emr_serverless.types.tag_map.TagMap"] = None,
        execution_timeout_minutes: Optional[
            "capo_emr_serverless.types.duration.Duration"
        ] = None,
        name: Optional["capo_emr_serverless.types.string256.String256"] = None,
        mode: Optional["capo_emr_serverless.types.job_run_mode.JobRunMode"] = None,
        retry_policy: Optional[
            "capo_emr_serverless.types.retry_policy.RetryPolicy"
        ] = None,
    ) -> "capo_emr_serverless.types.start_job_run_response.StartJobRunResponse":
        """<p>Starts a job run.</p>

        Args:
            application_id: <p>The ID of the application on which to run the job.</p>
            client_token: <p>The client idempotency token of the job run to start. Its value must be unique for each request.</p>
            execution_role_arn: <p>The execution role ARN for the job run.</p>
            execution_iam_policy: <p>You can pass an optional IAM policy. The resulting job IAM role permissions will be an intersection of this policy and the policy associated with your job execution role.</p>
            job_driver: <p>The job driver for the job run.</p>
            configuration_overrides: <p>The configuration overrides for the job run.</p>
            tags: <p>The tags assigned to the job run.</p>
            execution_timeout_minutes: <p>The maximum duration for the job run to run. If the job run runs beyond this duration, it will be automatically cancelled.</p>
            name: <p>The optional job run name. This doesn't have to be unique.</p>
            mode: <p>The mode of the job run when it starts.</p>
            retry_policy: <p>The retry policy when job run starts.</p>

        Raises:
            capo_emr_serverless.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.start_job_run_request.StartJobRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.start_job_run_response.StartJobRunResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.start_job_run

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.start_job_run.async_start_job_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.start_job_run_request.StartJobRunRequest = {
            "application_id": application_id,
            "client_token": client_token,
            "execution_role_arn": execution_role_arn,
        }
        if execution_iam_policy is not None:
            input_["execution_iam_policy"] = execution_iam_policy
        if job_driver is not None:
            input_["job_driver"] = job_driver
        if configuration_overrides is not None:
            input_["configuration_overrides"] = configuration_overrides
        if tags is not None:
            input_["tags"] = tags
        if execution_timeout_minutes is not None:
            input_["execution_timeout_minutes"] = execution_timeout_minutes
        if name is not None:
            input_["name"] = name
        if mode is not None:
            input_["mode"] = mode
        if retry_policy is not None:
            input_["retry_policy"] = retry_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_job_run(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        job_run_id: "capo_emr_serverless.types.job_run_id.JobRunId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        attempt: Optional[
            "capo_emr_serverless.types.attempt_number.AttemptNumber"
        ] = None,
    ) -> "capo_emr_serverless.types.get_job_run_response.GetJobRunResponse":
        """<p>Displays detailed information about a job run.</p>

        Args:
            application_id: <p>The ID of the application on which the job run is submitted.</p>
            job_run_id: <p>The ID of the job run.</p>
            attempt: <p>An optimal parameter that indicates the amount of attempts for the job. If not specified, this value defaults to the attempt of the latest job.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.get_job_run_request.GetJobRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.get_job_run_response.GetJobRunResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.get_job_run

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.get_job_run.async_get_job_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.get_job_run_request.GetJobRunRequest = {
            "application_id": application_id,
            "job_run_id": job_run_id,
        }
        if attempt is not None:
            input_["attempt"] = attempt

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_job_run(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        job_run_id: "capo_emr_serverless.types.job_run_id.JobRunId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        shutdown_grace_period_in_seconds: Optional[
            "capo_emr_serverless.types.shutdown_grace_period_in_seconds.ShutdownGracePeriodInSeconds"
        ] = None,
    ) -> "capo_emr_serverless.types.cancel_job_run_response.CancelJobRunResponse":
        """<p>Cancels a job run.</p>

        Args:
            application_id: <p>The ID of the application on which the job run will be canceled.</p>
            job_run_id: <p>The ID of the job run to cancel.</p>
            shutdown_grace_period_in_seconds: <p>The duration in seconds to wait before forcefully terminating the job after cancellation is requested.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.cancel_job_run_request.CancelJobRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.cancel_job_run_response.CancelJobRunResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.cancel_job_run

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.cancel_job_run.async_cancel_job_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.cancel_job_run_request.CancelJobRunRequest = {
            "application_id": application_id,
            "job_run_id": job_run_id,
        }
        if shutdown_grace_period_in_seconds is not None:
            input_["shutdown_grace_period_in_seconds"] = (
                shutdown_grace_period_in_seconds
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_job_runs(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        next_token: Optional["capo_emr_serverless.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
        created_at_after: Optional["capo_emr_serverless.types.date.Date"] = None,
        created_at_before: Optional["capo_emr_serverless.types.date.Date"] = None,
        states: Optional[
            "capo_emr_serverless.types.job_run_state_set.JobRunStateSet"
        ] = None,
        mode: Optional["capo_emr_serverless.types.job_run_mode.JobRunMode"] = None,
    ) -> "capo_emr_serverless.types.list_job_runs_response.ListJobRunsResponse":
        """<p>Lists job runs based on a set of parameters.</p>

        Args:
            application_id: <p>The ID of the application for which to list the job run.</p>
            next_token: <p>The token for the next set of job run results.</p>
            max_results: <p>The maximum number of job runs that can be listed.</p>
            created_at_after: <p>The lower bound of the option to filter by creation date and time.</p>
            created_at_before: <p>The upper bound of the option to filter by creation date and time.</p>
            states: <p>An optional filter for job run states. Note that if this filter contains multiple states, the resulting list will be grouped by the state.</p>
            mode: <p>The mode of the job runs to list.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.list_job_runs_request.ListJobRunsRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.list_job_runs_response.ListJobRunsResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.list_job_runs

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.list_job_runs.async_list_job_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.list_job_runs_request.ListJobRunsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if created_at_after is not None:
            input_["created_at_after"] = created_at_after
        if created_at_before is not None:
            input_["created_at_before"] = created_at_before
        if states is not None:
            input_["states"] = states
        if mode is not None:
            input_["mode"] = mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_job_runs(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        next_token: Optional["capo_emr_serverless.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
        created_at_after: Optional["capo_emr_serverless.types.date.Date"] = None,
        created_at_before: Optional["capo_emr_serverless.types.date.Date"] = None,
        states: Optional[
            "capo_emr_serverless.types.job_run_state_set.JobRunStateSet"
        ] = None,
        mode: Optional["capo_emr_serverless.types.job_run_mode.JobRunMode"] = None,
    ) -> "AsyncIterator[capo_emr_serverless.types.job_run_summary.JobRunSummary]":
        _token = next_token
        while True:
            _response = await self.list_job_runs(
                application_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                created_at_after=created_at_after,
                created_at_before=created_at_before,
                states=states,
                mode=mode,
            )
            _page = _resolve_path(_response, ("job_runs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_dashboard_for_job_run(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        job_run_id: "capo_emr_serverless.types.job_run_id.JobRunId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        attempt: Optional[
            "capo_emr_serverless.types.attempt_number.AttemptNumber"
        ] = None,
        access_system_profile_logs: Optional[bool] = None,
    ) -> "capo_emr_serverless.types.get_dashboard_for_job_run_response.GetDashboardForJobRunResponse":
        """<p>Creates and returns a URL that you can use to access the application UIs for a job run.</p> <p>For jobs in a running state, the application UI is a live user interface such as the Spark or Tez web UI. For completed jobs, the application UI is a persistent application user interface such as the Spark History Server or persistent Tez UI.</p> <note> <p>The URL is valid for one hour after you generate it. To access the application UI after that hour elapses, you must invoke the API again to generate a new URL.</p> </note>

        Args:
            application_id: <p>The ID of the application.</p>
            job_run_id: <p>The ID of the job run.</p>
            attempt: <p>An optimal parameter that indicates the amount of attempts for the job. If not specified, this value defaults to the attempt of the latest job.</p>
            access_system_profile_logs: <p>Allows access to system profile logs for Lake Formation-enabled jobs. Default is false.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.get_dashboard_for_job_run_request.GetDashboardForJobRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.get_dashboard_for_job_run_response.GetDashboardForJobRunResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.get_dashboard_for_job_run

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.get_dashboard_for_job_run.async_get_dashboard_for_job_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.get_dashboard_for_job_run_request.GetDashboardForJobRunRequest = {
            "application_id": application_id,
            "job_run_id": job_run_id,
        }
        if attempt is not None:
            input_["attempt"] = attempt
        if access_system_profile_logs is not None:
            input_["access_system_profile_logs"] = access_system_profile_logs

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_job_run_attempts(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        job_run_id: "capo_emr_serverless.types.job_run_id.JobRunId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        next_token: Optional["capo_emr_serverless.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_emr_serverless.types.list_job_run_attempts_response.ListJobRunAttemptsResponse":
        """<p>Lists all attempt of a job run.</p>

        Args:
            application_id: <p>The ID of the application for which to list job runs.</p>
            job_run_id: <p>The ID of the job run to list.</p>
            next_token: <p>The token for the next set of job run attempt results.</p>
            max_results: <p>The maximum number of job run attempts to list.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.list_job_run_attempts_request.ListJobRunAttemptsRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.list_job_run_attempts_response.ListJobRunAttemptsResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.list_job_run_attempts

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.list_job_run_attempts.async_list_job_run_attempts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.list_job_run_attempts_request.ListJobRunAttemptsRequest = {
            "application_id": application_id,
            "job_run_id": job_run_id,
        }
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

    async def iter_list_job_run_attempts(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        job_run_id: "capo_emr_serverless.types.job_run_id.JobRunId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        next_token: Optional["capo_emr_serverless.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_emr_serverless.types.job_run_attempt_summary.JobRunAttemptSummary]":
        _token = next_token
        while True:
            _response = await self.list_job_run_attempts(
                application_id,
                job_run_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("job_run_attempts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_session(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        client_token: "capo_emr_serverless.types.client_token.ClientToken",
        execution_role_arn: "capo_emr_serverless.types.iam_role_arn.IAMRoleArn",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        configuration_overrides: Optional[
            "capo_emr_serverless.types.session_configuration_overrides.SessionConfigurationOverrides"
        ] = None,
        tags: Optional["capo_emr_serverless.types.tag_map.TagMap"] = None,
        idle_timeout_minutes: Optional[
            "capo_emr_serverless.types.duration.Duration"
        ] = None,
        name: Optional["capo_emr_serverless.types.string256.String256"] = None,
    ) -> "capo_emr_serverless.types.start_session_response.StartSessionResponse":
        """<p>Creates and starts a new session on the specified application. The application must be in the <code>STARTED</code> state or have <code>AutoStart</code> enabled, and have interactive sessions enabled. This operation is supported for EMR release 7.13.0 and later.</p>

        Args:
            application_id: <p>The ID of the application on which to start the session.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token, the server returns the successful response without performing the operation again.</p>
            execution_role_arn: <p>The execution role ARN for the session. Amazon EMR Serverless uses this role to access Amazon Web Services resources on your behalf during session execution.</p>
            configuration_overrides: <p>The configuration overrides for the session. Only runtime configuration overrides are supported.</p>
            tags: <p>The tags to assign to the session.</p>
            idle_timeout_minutes: <p>The idle timeout in minutes for the session. After the session remains idle for this duration, Amazon EMR Serverless automatically terminates it.</p>
            name: <p>The optional name for the session.</p>

        Raises:
            capo_emr_serverless.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The maximum number of resources per account has been reached.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.start_session_request.StartSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.start_session_response.StartSessionResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.start_session

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.start_session.async_start_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.start_session_request.StartSessionRequest = {
            "application_id": application_id,
            "client_token": client_token,
            "execution_role_arn": execution_role_arn,
        }
        if configuration_overrides is not None:
            input_["configuration_overrides"] = configuration_overrides
        if tags is not None:
            input_["tags"] = tags
        if idle_timeout_minutes is not None:
            input_["idle_timeout_minutes"] = idle_timeout_minutes
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_session(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        session_id: "capo_emr_serverless.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.get_session_response.GetSessionResponse":
        """<p>Displays detailed information about a session.</p>

        Args:
            application_id: <p>The ID of the application that the session belongs to.</p>
            session_id: <p>The ID of the session.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.get_session_request.GetSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.get_session_response.GetSessionResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.get_session

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.get_session.async_get_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.get_session_request.GetSessionRequest = {
            "application_id": application_id,
            "session_id": session_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def terminate_session(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        session_id: "capo_emr_serverless.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
    ) -> (
        "capo_emr_serverless.types.terminate_session_response.TerminateSessionResponse"
    ):
        """<p>Terminates the specified session. After you terminate a session, it enters the <code>TERMINATING</code> state and then the <code>TERMINATED</code> state. You can still access the Spark History Server for a terminated session through the <code>GetResourceDashboard</code> operation.</p>

        Args:
            application_id: <p>The ID of the application that the session belongs to.</p>
            session_id: <p>The ID of the session to terminate.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.terminate_session_request.TerminateSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.terminate_session_response.TerminateSessionResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.terminate_session

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.terminate_session.async_terminate_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.terminate_session_request.TerminateSessionRequest = {
            "application_id": application_id,
            "session_id": session_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_sessions(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        next_token: Optional["capo_emr_serverless.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
        states: Optional[
            "capo_emr_serverless.types.session_state_set.SessionStateSet"
        ] = None,
        created_at_after: Optional["capo_emr_serverless.types.date.Date"] = None,
        created_at_before: Optional["capo_emr_serverless.types.date.Date"] = None,
    ) -> "capo_emr_serverless.types.list_sessions_response.ListSessionsResponse":
        """<p>Lists sessions for the specified application. You can filter sessions by state and creation time.</p>

        Args:
            application_id: <p>The ID of the application to list sessions for.</p>
            next_token: <p>The token for the next set of session results.</p>
            max_results: <p>The maximum number of sessions to return in each page of results.</p>
            states: <p>An optional filter for session states. Note that if this filter contains multiple states, the resulting list will be grouped by the state.</p>
            created_at_after: <p>The lower bound of the option to filter by creation date and time.</p>
            created_at_before: <p>The upper bound of the option to filter by creation date and time.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.list_sessions_request.ListSessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.list_sessions_response.ListSessionsResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.list_sessions

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.list_sessions.async_list_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.list_sessions_request.ListSessionsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if states is not None:
            input_["states"] = states
        if created_at_after is not None:
            input_["created_at_after"] = created_at_after
        if created_at_before is not None:
            input_["created_at_before"] = created_at_before

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_sessions(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        next_token: Optional["capo_emr_serverless.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
        states: Optional[
            "capo_emr_serverless.types.session_state_set.SessionStateSet"
        ] = None,
        created_at_after: Optional["capo_emr_serverless.types.date.Date"] = None,
        created_at_before: Optional["capo_emr_serverless.types.date.Date"] = None,
    ) -> "AsyncIterator[capo_emr_serverless.types.session_summary.SessionSummary]":
        _token = next_token
        while True:
            _response = await self.list_sessions(
                application_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                states=states,
                created_at_after=created_at_after,
                created_at_before=created_at_before,
            )
            _page = _resolve_path(_response, ("sessions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_session_endpoint(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        session_id: "capo_emr_serverless.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.get_session_endpoint_response.GetSessionEndpointResponse":
        """<p>Returns the session endpoint URL and a time-limited authentication token for the specified session. Use the endpoint and token to connect a client to the session. Call this operation again when the authentication token expires to obtain a new token.</p>

        Args:
            application_id: <p>The ID of the application that the session belongs to.</p>
            session_id: <p>The ID of the session.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.get_session_endpoint_request.GetSessionEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.get_session_endpoint_response.GetSessionEndpointResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.get_session_endpoint

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.get_session_endpoint.async_get_session_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_emr_serverless.types.get_session_endpoint_request.GetSessionEndpointRequest = {
            "application_id": application_id,
            "session_id": session_id,
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
