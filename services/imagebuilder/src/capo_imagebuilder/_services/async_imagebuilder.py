"""Generated from Smithy shape ``com.amazonaws.imagebuilder#imagebuilder``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_imagebuilder._auth._signers
import capo_imagebuilder._auth._sigv4
from capo_imagebuilder._auth._identity import Credentials
from capo_imagebuilder._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_imagebuilder._auth._zapros_handler import AuthMiddleware
from capo_imagebuilder._pagination import resolve_path as _resolve_path
from capo_imagebuilder._services._aws_config import aaws_config
from capo_imagebuilder._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_imagebuilder.types.additional_instance_configuration
    import capo_imagebuilder.types.ami_watermarks_list
    import capo_imagebuilder.types.boolean
    import capo_imagebuilder.types.cancel_image_creation_request
    import capo_imagebuilder.types.cancel_image_creation_response
    import capo_imagebuilder.types.cancel_lifecycle_execution_request
    import capo_imagebuilder.types.cancel_lifecycle_execution_response
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.component_build_version_arn
    import capo_imagebuilder.types.component_configuration_list
    import capo_imagebuilder.types.component_format
    import capo_imagebuilder.types.component_summary
    import capo_imagebuilder.types.component_type
    import capo_imagebuilder.types.component_version
    import capo_imagebuilder.types.component_version_arn
    import capo_imagebuilder.types.component_version_arn_or_build_version_arn
    import capo_imagebuilder.types.container_recipe_arn
    import capo_imagebuilder.types.container_recipe_summary
    import capo_imagebuilder.types.container_type
    import capo_imagebuilder.types.create_component_request
    import capo_imagebuilder.types.create_component_response
    import capo_imagebuilder.types.create_container_recipe_request
    import capo_imagebuilder.types.create_container_recipe_response
    import capo_imagebuilder.types.create_distribution_configuration_request
    import capo_imagebuilder.types.create_distribution_configuration_response
    import capo_imagebuilder.types.create_image_pipeline_request
    import capo_imagebuilder.types.create_image_pipeline_response
    import capo_imagebuilder.types.create_image_recipe_request
    import capo_imagebuilder.types.create_image_recipe_response
    import capo_imagebuilder.types.create_image_request
    import capo_imagebuilder.types.create_image_response
    import capo_imagebuilder.types.create_infrastructure_configuration_request
    import capo_imagebuilder.types.create_infrastructure_configuration_response
    import capo_imagebuilder.types.create_lifecycle_policy_request
    import capo_imagebuilder.types.create_lifecycle_policy_response
    import capo_imagebuilder.types.create_workflow_request
    import capo_imagebuilder.types.create_workflow_response
    import capo_imagebuilder.types.date_time_timestamp
    import capo_imagebuilder.types.delete_component_request
    import capo_imagebuilder.types.delete_component_response
    import capo_imagebuilder.types.delete_container_recipe_request
    import capo_imagebuilder.types.delete_container_recipe_response
    import capo_imagebuilder.types.delete_distribution_configuration_request
    import capo_imagebuilder.types.delete_distribution_configuration_response
    import capo_imagebuilder.types.delete_image_pipeline_request
    import capo_imagebuilder.types.delete_image_pipeline_response
    import capo_imagebuilder.types.delete_image_recipe_request
    import capo_imagebuilder.types.delete_image_recipe_response
    import capo_imagebuilder.types.delete_image_request
    import capo_imagebuilder.types.delete_image_response
    import capo_imagebuilder.types.delete_infrastructure_configuration_request
    import capo_imagebuilder.types.delete_infrastructure_configuration_response
    import capo_imagebuilder.types.delete_lifecycle_policy_request
    import capo_imagebuilder.types.delete_lifecycle_policy_response
    import capo_imagebuilder.types.delete_workflow_request
    import capo_imagebuilder.types.delete_workflow_response
    import capo_imagebuilder.types.distribute_image_request
    import capo_imagebuilder.types.distribute_image_response
    import capo_imagebuilder.types.distribution_configuration_arn
    import capo_imagebuilder.types.distribution_configuration_summary
    import capo_imagebuilder.types.distribution_list
    import capo_imagebuilder.types.filter
    import capo_imagebuilder.types.filter_list
    import capo_imagebuilder.types.get_component_policy_request
    import capo_imagebuilder.types.get_component_policy_response
    import capo_imagebuilder.types.get_component_request
    import capo_imagebuilder.types.get_component_response
    import capo_imagebuilder.types.get_container_recipe_policy_request
    import capo_imagebuilder.types.get_container_recipe_policy_response
    import capo_imagebuilder.types.get_container_recipe_request
    import capo_imagebuilder.types.get_container_recipe_response
    import capo_imagebuilder.types.get_distribution_configuration_request
    import capo_imagebuilder.types.get_distribution_configuration_response
    import capo_imagebuilder.types.get_image_pipeline_request
    import capo_imagebuilder.types.get_image_pipeline_response
    import capo_imagebuilder.types.get_image_policy_request
    import capo_imagebuilder.types.get_image_policy_response
    import capo_imagebuilder.types.get_image_recipe_policy_request
    import capo_imagebuilder.types.get_image_recipe_policy_response
    import capo_imagebuilder.types.get_image_recipe_request
    import capo_imagebuilder.types.get_image_recipe_response
    import capo_imagebuilder.types.get_image_request
    import capo_imagebuilder.types.get_image_response
    import capo_imagebuilder.types.get_infrastructure_configuration_request
    import capo_imagebuilder.types.get_infrastructure_configuration_response
    import capo_imagebuilder.types.get_lifecycle_execution_request
    import capo_imagebuilder.types.get_lifecycle_execution_response
    import capo_imagebuilder.types.get_lifecycle_policy_request
    import capo_imagebuilder.types.get_lifecycle_policy_response
    import capo_imagebuilder.types.get_marketplace_resource_request
    import capo_imagebuilder.types.get_marketplace_resource_response
    import capo_imagebuilder.types.get_workflow_execution_request
    import capo_imagebuilder.types.get_workflow_execution_response
    import capo_imagebuilder.types.get_workflow_request
    import capo_imagebuilder.types.get_workflow_response
    import capo_imagebuilder.types.get_workflow_step_execution_request
    import capo_imagebuilder.types.get_workflow_step_execution_response
    import capo_imagebuilder.types.image_build_version_arn
    import capo_imagebuilder.types.image_builder_arn
    import capo_imagebuilder.types.image_logging_configuration
    import capo_imagebuilder.types.image_package
    import capo_imagebuilder.types.image_pipeline
    import capo_imagebuilder.types.image_pipeline_arn
    import capo_imagebuilder.types.image_recipe_arn
    import capo_imagebuilder.types.image_recipe_summary
    import capo_imagebuilder.types.image_scan_finding
    import capo_imagebuilder.types.image_scan_finding_aggregation
    import capo_imagebuilder.types.image_scan_findings_filter_list
    import capo_imagebuilder.types.image_scanning_configuration
    import capo_imagebuilder.types.image_summary
    import capo_imagebuilder.types.image_tests_configuration
    import capo_imagebuilder.types.image_version
    import capo_imagebuilder.types.image_version_arn
    import capo_imagebuilder.types.image_version_arn_or_build_version_arn
    import capo_imagebuilder.types.import_component_request
    import capo_imagebuilder.types.import_component_response
    import capo_imagebuilder.types.import_disk_image_request
    import capo_imagebuilder.types.import_disk_image_response
    import capo_imagebuilder.types.import_vm_image_request
    import capo_imagebuilder.types.import_vm_image_response
    import capo_imagebuilder.types.infrastructure_configuration_arn
    import capo_imagebuilder.types.infrastructure_configuration_summary
    import capo_imagebuilder.types.inline_component_data
    import capo_imagebuilder.types.inline_docker_file_template
    import capo_imagebuilder.types.inline_workflow_data
    import capo_imagebuilder.types.instance_block_device_mappings
    import capo_imagebuilder.types.instance_configuration
    import capo_imagebuilder.types.instance_metadata_options
    import capo_imagebuilder.types.instance_profile_name_type
    import capo_imagebuilder.types.instance_type_list
    import capo_imagebuilder.types.lifecycle_execution
    import capo_imagebuilder.types.lifecycle_execution_id
    import capo_imagebuilder.types.lifecycle_execution_resource
    import capo_imagebuilder.types.lifecycle_policy_arn
    import capo_imagebuilder.types.lifecycle_policy_details
    import capo_imagebuilder.types.lifecycle_policy_resource_selection
    import capo_imagebuilder.types.lifecycle_policy_resource_type
    import capo_imagebuilder.types.lifecycle_policy_status
    import capo_imagebuilder.types.lifecycle_policy_summary
    import capo_imagebuilder.types.list_component_build_versions_request
    import capo_imagebuilder.types.list_component_build_versions_response
    import capo_imagebuilder.types.list_components_request
    import capo_imagebuilder.types.list_components_response
    import capo_imagebuilder.types.list_container_recipes_request
    import capo_imagebuilder.types.list_container_recipes_response
    import capo_imagebuilder.types.list_distribution_configurations_request
    import capo_imagebuilder.types.list_distribution_configurations_response
    import capo_imagebuilder.types.list_image_build_versions_request
    import capo_imagebuilder.types.list_image_build_versions_response
    import capo_imagebuilder.types.list_image_packages_request
    import capo_imagebuilder.types.list_image_packages_response
    import capo_imagebuilder.types.list_image_pipeline_images_request
    import capo_imagebuilder.types.list_image_pipeline_images_response
    import capo_imagebuilder.types.list_image_pipelines_request
    import capo_imagebuilder.types.list_image_pipelines_response
    import capo_imagebuilder.types.list_image_recipes_request
    import capo_imagebuilder.types.list_image_recipes_response
    import capo_imagebuilder.types.list_image_scan_finding_aggregations_request
    import capo_imagebuilder.types.list_image_scan_finding_aggregations_response
    import capo_imagebuilder.types.list_image_scan_findings_request
    import capo_imagebuilder.types.list_image_scan_findings_response
    import capo_imagebuilder.types.list_images_request
    import capo_imagebuilder.types.list_images_response
    import capo_imagebuilder.types.list_infrastructure_configurations_request
    import capo_imagebuilder.types.list_infrastructure_configurations_response
    import capo_imagebuilder.types.list_lifecycle_execution_resources_request
    import capo_imagebuilder.types.list_lifecycle_execution_resources_response
    import capo_imagebuilder.types.list_lifecycle_executions_request
    import capo_imagebuilder.types.list_lifecycle_executions_response
    import capo_imagebuilder.types.list_lifecycle_policies_request
    import capo_imagebuilder.types.list_lifecycle_policies_response
    import capo_imagebuilder.types.list_tags_for_resource_request
    import capo_imagebuilder.types.list_tags_for_resource_response
    import capo_imagebuilder.types.list_waiting_workflow_steps_request
    import capo_imagebuilder.types.list_waiting_workflow_steps_response
    import capo_imagebuilder.types.list_workflow_build_versions_request
    import capo_imagebuilder.types.list_workflow_build_versions_response
    import capo_imagebuilder.types.list_workflow_executions_request
    import capo_imagebuilder.types.list_workflow_executions_response
    import capo_imagebuilder.types.list_workflow_step_executions_request
    import capo_imagebuilder.types.list_workflow_step_executions_response
    import capo_imagebuilder.types.list_workflows_request
    import capo_imagebuilder.types.list_workflows_response
    import capo_imagebuilder.types.logging
    import capo_imagebuilder.types.marketplace_resource_location
    import capo_imagebuilder.types.marketplace_resource_type
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.nullable_boolean
    import capo_imagebuilder.types.os_version
    import capo_imagebuilder.types.os_version_list
    import capo_imagebuilder.types.ownership
    import capo_imagebuilder.types.pagination_token
    import capo_imagebuilder.types.pipeline_logging_configuration
    import capo_imagebuilder.types.pipeline_status
    import capo_imagebuilder.types.placement
    import capo_imagebuilder.types.platform
    import capo_imagebuilder.types.put_component_policy_request
    import capo_imagebuilder.types.put_component_policy_response
    import capo_imagebuilder.types.put_container_recipe_policy_request
    import capo_imagebuilder.types.put_container_recipe_policy_response
    import capo_imagebuilder.types.put_image_policy_request
    import capo_imagebuilder.types.put_image_policy_response
    import capo_imagebuilder.types.put_image_recipe_policy_request
    import capo_imagebuilder.types.put_image_recipe_policy_response
    import capo_imagebuilder.types.register_image_options
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.resource_policy_document
    import capo_imagebuilder.types.resource_state
    import capo_imagebuilder.types.resource_state_update_exclusion_rules
    import capo_imagebuilder.types.resource_state_update_include_resources
    import capo_imagebuilder.types.resource_tag_map
    import capo_imagebuilder.types.restricted_integer
    import capo_imagebuilder.types.retry_image_request
    import capo_imagebuilder.types.retry_image_response
    import capo_imagebuilder.types.role_name_or_arn
    import capo_imagebuilder.types.schedule
    import capo_imagebuilder.types.security_group_ids
    import capo_imagebuilder.types.send_workflow_step_action_request
    import capo_imagebuilder.types.send_workflow_step_action_response
    import capo_imagebuilder.types.sns_topic_arn
    import capo_imagebuilder.types.start_image_pipeline_execution_request
    import capo_imagebuilder.types.start_image_pipeline_execution_response
    import capo_imagebuilder.types.start_resource_state_update_request
    import capo_imagebuilder.types.start_resource_state_update_response
    import capo_imagebuilder.types.tag_key_list
    import capo_imagebuilder.types.tag_map
    import capo_imagebuilder.types.tag_resource_request
    import capo_imagebuilder.types.tag_resource_response
    import capo_imagebuilder.types.target_container_repository
    import capo_imagebuilder.types.untag_resource_request
    import capo_imagebuilder.types.untag_resource_response
    import capo_imagebuilder.types.update_distribution_configuration_request
    import capo_imagebuilder.types.update_distribution_configuration_response
    import capo_imagebuilder.types.update_image_pipeline_request
    import capo_imagebuilder.types.update_image_pipeline_response
    import capo_imagebuilder.types.update_infrastructure_configuration_request
    import capo_imagebuilder.types.update_infrastructure_configuration_response
    import capo_imagebuilder.types.update_lifecycle_policy_request
    import capo_imagebuilder.types.update_lifecycle_policy_response
    import capo_imagebuilder.types.uri
    import capo_imagebuilder.types.version_number
    import capo_imagebuilder.types.wildcard_version_number
    import capo_imagebuilder.types.windows_configuration
    import capo_imagebuilder.types.workflow_build_version_arn
    import capo_imagebuilder.types.workflow_configuration_list
    import capo_imagebuilder.types.workflow_execution_id
    import capo_imagebuilder.types.workflow_execution_metadata
    import capo_imagebuilder.types.workflow_step_action_type
    import capo_imagebuilder.types.workflow_step_execution
    import capo_imagebuilder.types.workflow_step_execution_id
    import capo_imagebuilder.types.workflow_step_metadata
    import capo_imagebuilder.types.workflow_summary
    import capo_imagebuilder.types.workflow_type
    import capo_imagebuilder.types.workflow_version
    import capo_imagebuilder.types.workflow_version_arn_or_build_version_arn
    import capo_imagebuilder.types.workflow_wildcard_version_arn


class AsyncimagebuilderClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncimagebuilderClient:
    """A client for the ``imagebuilder`` service.

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
        self._config = AsyncimagebuilderClientConfig(
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
        self, config_overrides: Optional[AsyncimagebuilderClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncimagebuilderClientConfig = config_overrides or {}
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

    async def cancel_image_creation(
        self,
        image_build_version_arn: "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.cancel_image_creation_response.CancelImageCreationResponse":
        """<p>Cancels the creation of an image. This operation can only be used on images in a non-terminal state. Cancellation is asynchronous: the request returns immediately, then Image Builder stops the running build and moves the image to the <code>CANCELLED</code> state. Output resources that the build already created, such as AMIs and snapshots, aren't removed.</p>

        Args:
            image_build_version_arn: <p>The Amazon Resource Name (ARN) of the image that you want to cancel creation for.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Cancel an image build
            The following example cancels a build that is in progress for the specified image build version.

            >>> await client.cancel_image_creation(image_build_version_arn='arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1', client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE77777')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.cancel_image_creation_request.CancelImageCreationRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.cancel_image_creation_response.CancelImageCreationResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.cancel_image_creation

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.cancel_image_creation.async_cancel_image_creation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.cancel_image_creation_request.CancelImageCreationRequest = {
            "image_build_version_arn": image_build_version_arn,
            "client_token": client_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_lifecycle_execution(
        self,
        lifecycle_execution_id: "capo_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.cancel_lifecycle_execution_response.CancelLifecycleExecutionResponse":
        """<p>Cancels a lifecycle execution – a single run of lifecycle actions that a lifecycle policy or a <a>StartResourceStateUpdate</a> request started. You can only cancel an execution that hasn't reached a terminal state. Cancellation is asynchronous and doesn't undo completed lifecycle actions.</p>

        Args:
            lifecycle_execution_id: <p>Identifies the specific runtime instance of the image lifecycle to cancel.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Cancel a lifecycle execution
            The following example cancels the scheduled resource state update associated with the specified lifecycle execution ID before it runs.

            >>> await client.cancel_lifecycle_execution(lifecycle_execution_id='lce-401aefc3-a829-46f6-8fc2-91497988a503', client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE97531')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.cancel_lifecycle_execution_request.CancelLifecycleExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.cancel_lifecycle_execution_response.CancelLifecycleExecutionResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.cancel_lifecycle_execution

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.cancel_lifecycle_execution.async_cancel_lifecycle_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.cancel_lifecycle_execution_request.CancelLifecycleExecutionRequest = {
            "lifecycle_execution_id": lifecycle_execution_id,
            "client_token": client_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_component(
        self,
        name: "capo_imagebuilder.types.resource_name.ResourceName",
        semantic_version: "capo_imagebuilder.types.version_number.VersionNumber",
        platform: "capo_imagebuilder.types.platform.Platform",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        description: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        change_description: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        supported_os_versions: Optional[
            "capo_imagebuilder.types.os_version_list.OsVersionList"
        ] = None,
        data: Optional[
            "capo_imagebuilder.types.inline_component_data.InlineComponentData"
        ] = None,
        uri: Optional["capo_imagebuilder.types.uri.Uri"] = None,
        kms_key_id: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["capo_imagebuilder.types.tag_map.TagMap"] = None,
        dry_run: Optional["capo_imagebuilder.types.boolean.Boolean"] = None,
    ) -> "capo_imagebuilder.types.create_component_response.CreateComponentResponse":
        r"""<p>Creates a new component that can be used to build, validate, test, and assess your image. The component is based on a YAML document that you specify using exactly one of the following methods:</p> <ul> <li> <p>Inline, using the <code>data</code> property in the request body.</p> </li> <li> <p>A URL that points to a YAML document file stored in Amazon S3, using the <code>uri</code> property in the request body.</p> </li> </ul> <p>Image Builder determines the component type from the document. If the document contains a single phase named <code>test</code>, the component type is <code>TEST</code>. Otherwise, the component type is <code>BUILD</code>.</p>

        Args:
            name: <p>The name of the component. Image Builder generates the component ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name. If a component with the same name and semantic version already exists in your account in the same Amazon Web Services Region, the request creates a new build version for it. If the content is also identical to the latest build version, the request fails because the component already exists.</p>
            semantic_version: <p>The semantic version of the component. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>
            description: <p>Describes the contents of the component.</p>
            change_description: <p>The change description of the component. Describes what change has been made in this version, or what makes this version different from other versions of the component.</p>
            platform: <p>The operating system platform of the component.</p>
            supported_os_versions: <p>The operating system (OS) version supported by the component. If the OS information is available, a prefix match is performed against the base image OS version during image recipe creation.</p>
            data: <p>Component <code>data</code> contains inline YAML document content for the component. Alternatively, you can specify the <code>uri</code> of a YAML document file stored in Amazon S3. However, you cannot specify both properties.</p>
            uri: <p>The <code>uri</code> of a YAML component document file. This must be an S3 URL (<code>s3://bucket/key</code>), and you must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota for component size, which is 64 KB by default.</p> <p>Alternatively, you can specify the YAML document inline, using the component <code>data</code> property. You cannot specify both properties.</p>
            kms_key_id: <p>The Amazon Resource Name (ARN) that uniquely identifies the KMS key used to encrypt this component. This can be either the Key ARN or the Alias ARN. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>. If you don't specify a key, Image Builder encrypts the component data with a KMS key that Image Builder owns.</p>
            tags: <p>The tags that apply to the component.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            dry_run: <p>Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a <code>DryRunOperationException</code> error response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.dry_run_operation_exception.DryRunOperationException: <p>The dry run operation of the resource was successful, and no resources or mutations were actually performed due to the dry run flag in the request.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>You have specified a combination of parameters that isn't valid. For example, two mutually exclusive parameters, or a parameter without its required companion parameter. Review the error message for details.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.invalid_version_number_exception.InvalidVersionNumberException: <p>Your version number is out of bounds or does not follow the required syntax.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href="https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder">EC2 Image Builder endpoints and quotas</a>.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a component from a document stored in Amazon S3
            The following example creates a component from a YAML definition document that's stored in an Amazon S3 bucket. The definition document for this component includes an AppVersion parameter that recipes can set when they include the component.

            >>> await client.create_component(name='my-example-parameterized-component', semantic_version='1.0.0', description='Installs a configurable version of my application', platform='Linux', uri='s3://amzn-s3-demo-bucket/components/install-my-app.yaml', client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE10101')
            Create a component from an inline document
            The following example creates a build component from a YAML document provided inline in the request.

            >>> await client.create_component(name='my-example-component', semantic_version='1.0.0', description='Installs the latest version of my application', platform='Linux', data='name: InstallMyApp\ndescription: Installs my application\nschemaVersion: 1.0\nphases:\n  - name: build\n    steps:\n      - name: InstallApp\n        action: ExecuteBash\n        inputs:\n          commands:\n            - sudo yum -y install my-app\n', client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE11111')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.create_component_request.CreateComponentRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.create_component_response.CreateComponentResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.create_component

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.create_component.async_create_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.create_component_request.CreateComponentRequest = {
            "name": name,
            "semantic_version": semantic_version,
            "platform": platform,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
        if change_description is not None:
            input_["change_description"] = change_description
        if supported_os_versions is not None:
            input_["supported_os_versions"] = supported_os_versions
        if data is not None:
            input_["data"] = data
        if uri is not None:
            input_["uri"] = uri
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_container_recipe(
        self,
        container_type: "capo_imagebuilder.types.container_type.ContainerType",
        name: "capo_imagebuilder.types.resource_name.ResourceName",
        semantic_version: "capo_imagebuilder.types.wildcard_version_number.WildcardVersionNumber",
        parent_image: "capo_imagebuilder.types.non_empty_string.NonEmptyString",
        target_repository: "capo_imagebuilder.types.target_container_repository.TargetContainerRepository",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        description: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        components: Optional[
            "capo_imagebuilder.types.component_configuration_list.ComponentConfigurationList"
        ] = None,
        instance_configuration: Optional[
            "capo_imagebuilder.types.instance_configuration.InstanceConfiguration"
        ] = None,
        dockerfile_template_data: Optional[
            "capo_imagebuilder.types.inline_docker_file_template.InlineDockerFileTemplate"
        ] = None,
        dockerfile_template_uri: Optional["capo_imagebuilder.types.uri.Uri"] = None,
        platform_override: Optional["capo_imagebuilder.types.platform.Platform"] = None,
        image_os_version_override: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["capo_imagebuilder.types.tag_map.TagMap"] = None,
        working_directory: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        kms_key_id: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        dry_run: Optional["capo_imagebuilder.types.boolean.Boolean"] = None,
    ) -> "capo_imagebuilder.types.create_container_recipe_response.CreateContainerRecipeResponse":
        r"""<p>Creates a new container recipe. Container recipes define how images are configured, tested, and assessed.</p>

        Args:
            container_type: <p>The type of container to create.</p>
            name: <p>The name of the container recipe. The recipe name, combined with the semantic version, must be unique to your account in each Amazon Web Services Region. Image Builder generates the container recipe ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name.</p>
            description: <p>The description of the container recipe.</p>
            semantic_version: <p>The semantic version of the container recipe. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>
            components: <p>The components included in the container recipe. You can specify each component only one time in a recipe.</p>
            instance_configuration: <p>A group of options that can be used to configure an instance for building and testing container images.</p>
            dockerfile_template_data: <p>The Dockerfile template used to build your image, as an inline data blob. You must specify exactly one of the <code>dockerfileTemplateData</code> or <code>dockerfileTemplateUri</code> properties. For the contextual variables that the template can include, see <a href="https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-container-recipes.html">Create a new version of a container recipe</a> in the <i>EC2 Image Builder User Guide</i>.</p>
            dockerfile_template_uri: <p>The Amazon S3 URI for the Dockerfile template that is used to build your container image. You must have permission to read the object. Image Builder reads the object once, when it creates the recipe, and stores its content in the recipe. Later changes to the S3 object don't affect the recipe. You must specify exactly one of the <code>dockerfileTemplateData</code> or <code>dockerfileTemplateUri</code> properties.</p>
            platform_override: <p>Specifies the operating system platform when you use a custom base image. Container recipes support only the Linux and Windows platforms.</p>
            image_os_version_override: <p>Specifies the operating system version for the base image. Use this property only when the base image is a container image from a registry. When the base image is an Image Builder image, the operating system version comes from the parent image.</p>
            parent_image: <p>The base image for the container recipe. This can be an Image Builder image resource ARN or a container image URI from a registry, for example <code>amazonlinux:latest</code>.</p>
            tags: <p>Tags that are attached to the container recipe.</p>
            working_directory: <p>The working directory for use during build and test workflows.</p>
            target_repository: <p>The destination repository for the container image. The Amazon ECR repository must already exist in the Amazon Web Services Region where the build runs.</p>
            kms_key_id: <p>The Amazon Resource Name (ARN) that uniquely identifies which KMS key is used to encrypt the Dockerfile template. This can be either the Key ARN or the Alias ARN. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            dry_run: <p>Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a <code>DryRunOperationException</code> error response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.dry_run_operation_exception.DryRunOperationException: <p>The dry run operation of the resource was successful, and no resources or mutations were actually performed due to the dry run flag in the request.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.invalid_version_number_exception.InvalidVersionNumberException: <p>Your version number is out of bounds or does not follow the required syntax.</p>
            capo_imagebuilder.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource that you are trying to create already exists.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href="https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder">EC2 Image Builder endpoints and quotas</a>.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a container recipe with a custom build instance configuration
            The following example creates a container recipe that customizes the Amazon EC2 instance that builds the container image. The build instance launches from an Amazon ECS-optimized instance image and uses a 40 GiB gp3 volume.

            >>> await client.create_container_recipe(container_type='DOCKER', name='my-example-container-recipe', semantic_version='1.1.0', description='A container recipe that builds on an ECS-optimized instance image with a larger build volume', parent_image='amazonlinux:latest', components=[{'componentArn': 'arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-container-component/1.0.0/1'}], instance_configuration={'image': 'ami-1234567890abcdef0', 'blockDeviceMappings': [{'deviceName': '/dev/xvda', 'ebs': {'volumeSize': 40, 'volumeType': 'gp3', 'deleteOnTermination': True}}]}, dockerfile_template_data='FROM {{{ imagebuilder:parentImage }}}\n{{{ imagebuilder:environments }}}\n{{{ imagebuilder:components }}}\n', target_repository={'service': 'ECR', 'repositoryName': 'my-example-container-repo'}, client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE40404')
            Create a container recipe with an inline Dockerfile template
            The following example creates a Docker container recipe that applies one build component, using the latest Amazon Linux container image as the parent and an existing ECR repository as the target.

            >>> await client.create_container_recipe(container_type='DOCKER', name='my-example-container-recipe', semantic_version='1.0.0', parent_image='amazonlinux:latest', components=[{'componentArn': 'arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-container-component/1.0.0/1'}], dockerfile_template_data='FROM {{{ imagebuilder:parentImage }}}\n{{{ imagebuilder:environments }}}\n{{{ imagebuilder:components }}}\n', target_repository={'service': 'ECR', 'repositoryName': 'my-example-container-repo'}, client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE99999')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.create_container_recipe_request.CreateContainerRecipeRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.create_container_recipe_response.CreateContainerRecipeResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.create_container_recipe

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.create_container_recipe.async_create_container_recipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.create_container_recipe_request.CreateContainerRecipeRequest = {
            "container_type": container_type,
            "name": name,
            "semantic_version": semantic_version,
            "parent_image": parent_image,
            "target_repository": target_repository,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
        if components is not None:
            input_["components"] = components
        if instance_configuration is not None:
            input_["instance_configuration"] = instance_configuration
        if dockerfile_template_data is not None:
            input_["dockerfile_template_data"] = dockerfile_template_data
        if dockerfile_template_uri is not None:
            input_["dockerfile_template_uri"] = dockerfile_template_uri
        if platform_override is not None:
            input_["platform_override"] = platform_override
        if image_os_version_override is not None:
            input_["image_os_version_override"] = image_os_version_override
        if tags is not None:
            input_["tags"] = tags
        if working_directory is not None:
            input_["working_directory"] = working_directory
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_distribution_configuration(
        self,
        name: "capo_imagebuilder.types.resource_name.ResourceName",
        distributions: "capo_imagebuilder.types.distribution_list.DistributionList",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        description: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["capo_imagebuilder.types.tag_map.TagMap"] = None,
        dry_run: Optional["capo_imagebuilder.types.boolean.Boolean"] = None,
    ) -> "capo_imagebuilder.types.create_distribution_configuration_response.CreateDistributionConfigurationResponse":
        """<p>Creates a new distribution configuration. Distribution configurations define and configure the outputs for your images, including the target Regions, accounts, and settings for each Region.</p>

        Args:
            name: <p>The name of the distribution configuration. Distribution configuration names must be unique to your account in each Amazon Web Services Region. Image Builder generates the distribution configuration ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name.</p>
            description: <p>The description of the distribution configuration.</p>
            distributions: <p>The distribution settings for the configuration. Each entry defines how output images are distributed in one target Amazon Web Services Region. A Region can appear at most once in the list.</p>
            tags: <p>The tags of the distribution configuration.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            dry_run: <p>Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a <code>DryRunOperationException</code> error response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.dry_run_operation_exception.DryRunOperationException: <p>The dry run operation of the resource was successful, and no resources or mutations were actually performed due to the dry run flag in the request.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>You have specified a combination of parameters that isn't valid. For example, two mutually exclusive parameters, or a parameter without its required companion parameter. Review the error message for details.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource that you are trying to create already exists.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href="https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder">EC2 Image Builder endpoints and quotas</a>.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a distribution configuration
            The following example creates a distribution configuration that distributes the output AMI to two Regions. The AMI name includes the build date, so that repeated builds create unique AMI names.

            >>> await client.create_distribution_configuration(name='my-example-distribution', description='Copies the output AMI to a second Region', distributions=[{'region': 'us-west-2', 'amiDistributionConfiguration': {'name': 'my-example-image-{{ imagebuilder:buildDate }}'}}, {'region': 'us-east-1', 'amiDistributionConfiguration': {'name': 'my-example-image-{{ imagebuilder:buildDate }}'}}], client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE44444')
            Create a distribution configuration with launch permissions and a launch template update
            The following example creates a distribution configuration that distributes the output AMI to two Regions. In us-east-1, it shares the AMI with another AWS account. In us-west-2, it sets the new AMI as the default version of your launch template.

            >>> await client.create_distribution_configuration(name='my-example-distribution', description='Distributes the output AMI to two Regions and shares it with another account', distributions=[{'region': 'us-west-2', 'amiDistributionConfiguration': {'name': 'my-example-image-{{ imagebuilder:buildDate }}'}, 'launchTemplateConfigurations': [{'launchTemplateId': 'lt-1234567890abcdef0', 'setDefaultVersion': True}]}, {'region': 'us-east-1', 'amiDistributionConfiguration': {'name': 'my-example-image-{{ imagebuilder:buildDate }}', 'launchPermission': {'userIds': ['444455556666']}}}], client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE56789')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.create_distribution_configuration_request.CreateDistributionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.create_distribution_configuration_response.CreateDistributionConfigurationResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.create_distribution_configuration

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.create_distribution_configuration.async_create_distribution_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.create_distribution_configuration_request.CreateDistributionConfigurationRequest = {
            "name": name,
            "distributions": distributions,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_image(
        self,
        infrastructure_configuration_arn: "capo_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        image_recipe_arn: Optional[
            "capo_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
        ] = None,
        container_recipe_arn: Optional[
            "capo_imagebuilder.types.container_recipe_arn.ContainerRecipeArn"
        ] = None,
        distribution_configuration_arn: Optional[
            "capo_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn"
        ] = None,
        image_tests_configuration: Optional[
            "capo_imagebuilder.types.image_tests_configuration.ImageTestsConfiguration"
        ] = None,
        enhanced_image_metadata_enabled: Optional[
            "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
        ] = None,
        tags: Optional["capo_imagebuilder.types.tag_map.TagMap"] = None,
        image_scanning_configuration: Optional[
            "capo_imagebuilder.types.image_scanning_configuration.ImageScanningConfiguration"
        ] = None,
        workflows: Optional[
            "capo_imagebuilder.types.workflow_configuration_list.WorkflowConfigurationList"
        ] = None,
        execution_role: Optional[
            "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
        ] = None,
        logging_configuration: Optional[
            "capo_imagebuilder.types.image_logging_configuration.ImageLoggingConfiguration"
        ] = None,
    ) -> "capo_imagebuilder.types.create_image_response.CreateImageResponse":
        """<p>Creates a new image along with all configured output resources defined in the distribution configuration. You must specify exactly one recipe for your image, using either a <code>containerRecipeArn</code> or an <code>imageRecipeArn</code>.</p> <p>The response returns as soon as Image Builder creates the new image resource. The image build process runs asynchronously. To check its progress, call <a href="https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetImage.html">GetImage</a> and check the image status.</p>

        Args:
            image_recipe_arn: <p>The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed. You must specify either this property or <code>containerRecipeArn</code>, but not both.</p>
            container_recipe_arn: <p>The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested. You must specify either this property or <code>imageRecipeArn</code>, but not both.</p>
            distribution_configuration_arn: <p>The Amazon Resource Name (ARN) of the distribution configuration that defines and configures the outputs of the image build. If you don't specify a distribution configuration, Image Builder creates the output image only in the account and Amazon Web Services Region where the build runs.</p>
            infrastructure_configuration_arn: <p>The Amazon Resource Name (ARN) of the infrastructure configuration that defines the environment in which your image will be built and tested.</p>
            image_tests_configuration: <p>Settings that determine whether Image Builder runs tests on the image after building it. Image tests are enabled by default.</p>
            enhanced_image_metadata_enabled: <p>Specifies whether to collect additional information about the image being created, including the operating system (OS) version and package list. Defaults to <code>true</code>.</p>
            tags: <p>The tags of the image.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            image_scanning_configuration: <p>Settings for vulnerability scans that Amazon Inspector runs during image creation. For AMI output, Amazon Inspector scans the test instance. For container output, Amazon Inspector scans the container image that Image Builder pushes to the Amazon ECR repository specified in <code>ecrConfiguration</code>.</p>
            workflows: <p>The array of workflow configuration objects for the build. If you specify workflows, they replace the default workflows that Image Builder otherwise runs for the build, and you must also provide an <code>executionRole</code>.</p>
            execution_role: <p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions. This property is required if you specify <code>workflows</code>. If you don't provide a role, Image Builder uses the Image Builder service-linked role in your account, and creates it if it doesn't exist.</p>
            logging_configuration: <p>The CloudWatch Logs log group where Image Builder sends the image build logs. If you specify a log group name outside of the <code>/aws/imagebuilder/</code> namespace, you must also provide an <code>executionRole</code> that has permission to write to that log group.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href="https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder">EC2 Image Builder endpoints and quotas</a>.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create an image
            The following example creates a new image from the specified image recipe and infrastructure configuration.

            >>> await client.create_image(image_recipe_arn='arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.0.0', infrastructure_configuration_arn='arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure', client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLEeeeee')
            Create an image with custom build and parallel test workflows
            The following example creates an image that uses your custom build and test workflows. It uses the Image Builder service-linked role as the execution role. Both test workflows are in the same parallel group, so they can run at the same time after the build workflow completes.

            >>> await client.create_image(image_recipe_arn='arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.0.0', infrastructure_configuration_arn='arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure', workflows=[{'workflowArn': 'arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/1.0.0/1'}, {'workflowArn': 'arn:aws:imagebuilder:us-west-2:111122223333:workflow/test/my-example-integration-tests/1.0.0/1', 'parallelGroup': 'post-build-tests'}, {'workflowArn': 'arn:aws:imagebuilder:us-west-2:111122223333:workflow/test/my-example-compliance-tests/1.0.0/1', 'parallelGroup': 'post-build-tests'}], execution_role='arn:aws:iam::111122223333:role/aws-service-role/imagebuilder.amazonaws.com/AWSServiceRoleForImageBuilder', client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE01234')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.create_image_request.CreateImageRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.create_image_response.CreateImageResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.create_image

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.create_image.async_create_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.create_image_request.CreateImageRequest = {
            "infrastructure_configuration_arn": infrastructure_configuration_arn,
            "client_token": client_token,
        }
        if image_recipe_arn is not None:
            input_["image_recipe_arn"] = image_recipe_arn
        if container_recipe_arn is not None:
            input_["container_recipe_arn"] = container_recipe_arn
        if distribution_configuration_arn is not None:
            input_["distribution_configuration_arn"] = distribution_configuration_arn
        if image_tests_configuration is not None:
            input_["image_tests_configuration"] = image_tests_configuration
        if enhanced_image_metadata_enabled is not None:
            input_["enhanced_image_metadata_enabled"] = enhanced_image_metadata_enabled
        if tags is not None:
            input_["tags"] = tags
        if image_scanning_configuration is not None:
            input_["image_scanning_configuration"] = image_scanning_configuration
        if workflows is not None:
            input_["workflows"] = workflows
        if execution_role is not None:
            input_["execution_role"] = execution_role
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_image_pipeline(
        self,
        name: "capo_imagebuilder.types.resource_name.ResourceName",
        infrastructure_configuration_arn: "capo_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        description: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        image_recipe_arn: Optional[
            "capo_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
        ] = None,
        container_recipe_arn: Optional[
            "capo_imagebuilder.types.container_recipe_arn.ContainerRecipeArn"
        ] = None,
        distribution_configuration_arn: Optional[
            "capo_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn"
        ] = None,
        image_tests_configuration: Optional[
            "capo_imagebuilder.types.image_tests_configuration.ImageTestsConfiguration"
        ] = None,
        enhanced_image_metadata_enabled: Optional[
            "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
        ] = None,
        schedule: Optional["capo_imagebuilder.types.schedule.Schedule"] = None,
        status: Optional[
            "capo_imagebuilder.types.pipeline_status.PipelineStatus"
        ] = None,
        tags: Optional["capo_imagebuilder.types.tag_map.TagMap"] = None,
        image_tags: Optional["capo_imagebuilder.types.tag_map.TagMap"] = None,
        image_scanning_configuration: Optional[
            "capo_imagebuilder.types.image_scanning_configuration.ImageScanningConfiguration"
        ] = None,
        workflows: Optional[
            "capo_imagebuilder.types.workflow_configuration_list.WorkflowConfigurationList"
        ] = None,
        execution_role: Optional[
            "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
        ] = None,
        logging_configuration: Optional[
            "capo_imagebuilder.types.pipeline_logging_configuration.PipelineLoggingConfiguration"
        ] = None,
        dry_run: Optional["capo_imagebuilder.types.boolean.Boolean"] = None,
    ) -> "capo_imagebuilder.types.create_image_pipeline_response.CreateImagePipelineResponse":
        """<p>Creates a new image pipeline. Use image pipelines to automate the creation and distribution of images. You must specify exactly one recipe for the pipeline, using either a <code>containerRecipeArn</code> or an <code>imageRecipeArn</code>.</p>

        Args:
            name: <p>The name of the image pipeline. Pipeline names must be unique to your account in each Amazon Web Services Region. Image Builder generates the pipeline ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name.</p>
            description: <p>The description of the image pipeline.</p>
            image_recipe_arn: <p>The Amazon Resource Name (ARN) of the image recipe that configures images created by this image pipeline. You must specify either this property or <code>containerRecipeArn</code>, but not both.</p>
            container_recipe_arn: <p>The Amazon Resource Name (ARN) of the container recipe that is used to configure images created by this container pipeline. You must specify either this property or <code>imageRecipeArn</code>, but not both.</p>
            infrastructure_configuration_arn: <p>The Amazon Resource Name (ARN) of the infrastructure configuration that builds images created by this image pipeline.</p>
            distribution_configuration_arn: <p>The Amazon Resource Name (ARN) of the distribution configuration that configures and distributes images created by this image pipeline.</p>
            image_tests_configuration: <p>Specifies the test settings that Image Builder applies to images that this pipeline creates. If you don't provide test settings, Image Builder stores a default configuration with image tests enabled.</p>
            enhanced_image_metadata_enabled: <p>Specifies whether to collect additional information about the image being created, including the operating system (OS) version and package list. Defaults to <code>true</code>.</p>
            schedule: <p>The schedule of the image pipeline. If you don't provide a schedule, the pipeline runs only when you call <a>StartImagePipelineExecution</a>.</p>
            status: <p>The status of the image pipeline. If you don't specify a status, it defaults to <code>ENABLED</code>. A disabled pipeline doesn't run on its schedule, but you can still start builds manually.</p>
            tags: <p>The tags of the image pipeline.</p>
            image_tags: <p>The tags that Image Builder applies to the Image Builder image resource that this pipeline's scheduled executions create. These tags don't apply to the output AMI. To tag output AMIs, use <code>amiTags</code> in the pipeline's distribution configuration.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            image_scanning_configuration: <p>Contains settings for vulnerability scans that Amazon Inspector runs against the test instance during image creation.</p>
            workflows: <p>The array of workflow configuration objects for builds that this pipeline starts. You must also specify <code>executionRole</code> when you provide workflows.</p>
            execution_role: <p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.</p>
            logging_configuration: <p>Specifies the logging configuration for the image pipeline. Use this to define custom CloudWatch Logs log groups for your pipeline execution logs and image build logs. The service manages log groups with names starting with <code>/aws/imagebuilder/</code> using the service-linked role. For custom log group names outside of this prefix, you must also provide an <code>executionRole</code>.</p>
            dry_run: <p>Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a <code>DryRunOperationException</code> error response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.dry_run_operation_exception.DryRunOperationException: <p>The dry run operation of the resource was successful, and no resources or mutations were actually performed due to the dry run flag in the request.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource that you are trying to create already exists.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href="https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder">EC2 Image Builder endpoints and quotas</a>.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create an image pipeline
            The following example creates a pipeline that builds a new image version every Sunday at 9:00 AM UTC, if the base image or components have updates.

            >>> await client.create_image_pipeline(name='my-example-pipeline', description='Builds a new version of my image every Sunday', image_recipe_arn='arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.0.0', infrastructure_configuration_arn='arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure', distribution_configuration_arn='arn:aws:imagebuilder:us-west-2:111122223333:distribution-configuration/my-example-distribution', schedule={'scheduleExpression': 'cron(0 9 ? * SUN *)', 'pipelineExecutionStartCondition': 'EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE'}, status='ENABLED', client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE55555')
            Create an image pipeline with scanning, custom workflows, and an auto-disable policy
            The following example creates a pipeline that uses your custom build workflow and enables image scanning. The schedule evaluates its cron expression in the America/Los_Angeles time zone. The auto-disable policy disables the pipeline after 3 consecutive failed scheduled builds.

            >>> await client.create_image_pipeline(name='my-example-pipeline', description='Builds a scanned image with my custom build workflow on Sunday mornings when dependency updates are available', image_recipe_arn='arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.1.0', infrastructure_configuration_arn='arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure', distribution_configuration_arn='arn:aws:imagebuilder:us-west-2:111122223333:distribution-configuration/my-example-distribution', workflows=[{'workflowArn': 'arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/1.0.0/1'}], execution_role='arn:aws:iam::111122223333:role/aws-service-role/imagebuilder.amazonaws.com/AWSServiceRoleForImageBuilder', image_scanning_configuration={'imageScanningEnabled': True}, schedule={'scheduleExpression': 'cron(0 9 ? * SUN *)', 'timezone': 'America/Los_Angeles', 'pipelineExecutionStartCondition': 'EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE', 'autoDisablePolicy': {'failureCount': 3}}, status='ENABLED', client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE30303')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.create_image_pipeline_request.CreateImagePipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.create_image_pipeline_response.CreateImagePipelineResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.create_image_pipeline

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.create_image_pipeline.async_create_image_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.create_image_pipeline_request.CreateImagePipelineRequest = {
            "name": name,
            "infrastructure_configuration_arn": infrastructure_configuration_arn,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
        if image_recipe_arn is not None:
            input_["image_recipe_arn"] = image_recipe_arn
        if container_recipe_arn is not None:
            input_["container_recipe_arn"] = container_recipe_arn
        if distribution_configuration_arn is not None:
            input_["distribution_configuration_arn"] = distribution_configuration_arn
        if image_tests_configuration is not None:
            input_["image_tests_configuration"] = image_tests_configuration
        if enhanced_image_metadata_enabled is not None:
            input_["enhanced_image_metadata_enabled"] = enhanced_image_metadata_enabled
        if schedule is not None:
            input_["schedule"] = schedule
        if status is not None:
            input_["status"] = status
        if tags is not None:
            input_["tags"] = tags
        if image_tags is not None:
            input_["image_tags"] = image_tags
        if image_scanning_configuration is not None:
            input_["image_scanning_configuration"] = image_scanning_configuration
        if workflows is not None:
            input_["workflows"] = workflows
        if execution_role is not None:
            input_["execution_role"] = execution_role
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_image_recipe(
        self,
        name: "capo_imagebuilder.types.resource_name.ResourceName",
        semantic_version: "capo_imagebuilder.types.wildcard_version_number.WildcardVersionNumber",
        parent_image: "capo_imagebuilder.types.non_empty_string.NonEmptyString",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        description: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        components: Optional[
            "capo_imagebuilder.types.component_configuration_list.ComponentConfigurationList"
        ] = None,
        block_device_mappings: Optional[
            "capo_imagebuilder.types.instance_block_device_mappings.InstanceBlockDeviceMappings"
        ] = None,
        tags: Optional["capo_imagebuilder.types.tag_map.TagMap"] = None,
        working_directory: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        additional_instance_configuration: Optional[
            "capo_imagebuilder.types.additional_instance_configuration.AdditionalInstanceConfiguration"
        ] = None,
        ami_tags: Optional["capo_imagebuilder.types.tag_map.TagMap"] = None,
        ami_watermarks: Optional[
            "capo_imagebuilder.types.ami_watermarks_list.AmiWatermarksList"
        ] = None,
        dry_run: Optional["capo_imagebuilder.types.boolean.Boolean"] = None,
    ) -> (
        "capo_imagebuilder.types.create_image_recipe_response.CreateImageRecipeResponse"
    ):
        """<p>Creates a new image recipe. Image recipes define how images are configured, tested, and assessed.</p>

        Args:
            name: <p>The name of the image recipe. The recipe name, combined with the semantic version, must be unique to your account in each Amazon Web Services Region. Image Builder generates the image recipe ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name.</p>
            description: <p>The description of the image recipe.</p>
            semantic_version: <p>The semantic version of the image recipe. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>
            components: <p>The components included in the image recipe. Components are optional. A recipe with no components bakes the base image without additional customization. You can specify each component only one time in a recipe. Components with a status of <code>DEPRECATED</code> or <code>DISABLED</code> can't be added to new recipes.</p>
            parent_image: <p>The base image for customizations specified in the image recipe. You can specify the parent image using one of the following options:</p> <ul> <li> <p>AMI ID</p> </li> <li> <p>Image Builder image Amazon Resource Name (ARN)</p> </li> <li> <p>Amazon Web Services Systems Manager (SSM) Parameter Store Parameter, prefixed by <code>ssm:</code>, followed by the parameter name or ARN.</p> </li> <li> <p>Amazon Web Services Marketplace product ID</p> </li> </ul> <p>If you enter an AMI ID or an SSM parameter that contains the AMI ID, you must have access to the AMI. The AMI must also be in the Region where you're creating the recipe.</p>
            block_device_mappings: <p>The block device mappings that Image Builder applies to the build instance and the output AMI. For example, you can override the size of the base image's root volume or attach additional EBS volumes.</p>
            tags: <p>The tags of the image recipe.</p>
            working_directory: <p>The working directory used during build and test workflows. If you don't specify a working directory, Image Builder uses <code>/tmp</code> for Linux and macOS build instances, and <code>C:/</code> for Windows build instances.</p>
            additional_instance_configuration: <p>The additional settings and launch scripts for your build instances.</p>
            ami_tags: <p>Tags that are applied to the AMI that Image Builder creates during the Build phase prior to image distribution.</p>
            ami_watermarks: <p>The AMI watermark names to attach to the output AMI from this recipe. AMI watermarks are lineage markers. They automatically propagate to derivative AMIs when the source AMI is copied or distributed across Regions or accounts.</p> <note> <p>AMI watermarks are supported only for image recipes. AMIs with watermarks cannot be made public.</p> </note>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            dry_run: <p>Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a <code>DryRunOperationException</code> error response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.dry_run_operation_exception.DryRunOperationException: <p>The dry run operation of the resource was successful, and no resources or mutations were actually performed due to the dry run flag in the request.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.invalid_version_number_exception.InvalidVersionNumberException: <p>Your version number is out of bounds or does not follow the required syntax.</p>
            capo_imagebuilder.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource that you are trying to create already exists.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href="https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder">EC2 Image Builder endpoints and quotas</a>.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create an image recipe
            The following example creates an image recipe that applies a custom component on top of the latest Amazon Linux 2023 base image.

            >>> await client.create_image_recipe(name='my-example-recipe', semantic_version='1.0.0', description='An image recipe that installs my application on Amazon Linux 2023', parent_image='arn:aws:imagebuilder:us-west-2:aws:image/amazon-linux-2023-x86/x.x.x', components=[{'componentArn': 'arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/1.0.0/1'}], client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE22222')
            Create an image recipe with component parameters and block device mappings
            The following example creates an image recipe that configures its components and storage. The AppVersion component parameter selects the application version to install. The block device mapping increases the root volume to an encrypted 30 GiB gp3 volume.

            >>> await client.create_image_recipe(name='my-example-recipe', semantic_version='1.1.0', description='Installs a specific version of my application on Amazon Linux 2023 with a larger encrypted root volume', parent_image='arn:aws:imagebuilder:us-west-2:aws:image/amazon-linux-2023-x86/x.x.x', components=[{'componentArn': 'arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-parameterized-component/1.0.0/1', 'parameters': [{'name': 'AppVersion', 'value': ['2.5.0']}]}], block_device_mappings=[{'deviceName': '/dev/xvda', 'ebs': {'volumeSize': 30, 'volumeType': 'gp3', 'encrypted': True, 'deleteOnTermination': True}}], client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE20202')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.create_image_recipe_request.CreateImageRecipeRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.create_image_recipe_response.CreateImageRecipeResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.create_image_recipe

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.create_image_recipe.async_create_image_recipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.create_image_recipe_request.CreateImageRecipeRequest = {
            "name": name,
            "semantic_version": semantic_version,
            "parent_image": parent_image,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
        if components is not None:
            input_["components"] = components
        if block_device_mappings is not None:
            input_["block_device_mappings"] = block_device_mappings
        if tags is not None:
            input_["tags"] = tags
        if working_directory is not None:
            input_["working_directory"] = working_directory
        if additional_instance_configuration is not None:
            input_["additional_instance_configuration"] = (
                additional_instance_configuration
            )
        if ami_tags is not None:
            input_["ami_tags"] = ami_tags
        if ami_watermarks is not None:
            input_["ami_watermarks"] = ami_watermarks
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_infrastructure_configuration(
        self,
        name: "capo_imagebuilder.types.resource_name.ResourceName",
        instance_profile_name: "capo_imagebuilder.types.instance_profile_name_type.InstanceProfileNameType",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        description: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        instance_types: Optional[
            "capo_imagebuilder.types.instance_type_list.InstanceTypeList"
        ] = None,
        security_group_ids: Optional[
            "capo_imagebuilder.types.security_group_ids.SecurityGroupIds"
        ] = None,
        subnet_id: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        logging: Optional["capo_imagebuilder.types.logging.Logging"] = None,
        key_pair: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        terminate_instance_on_failure: Optional[
            "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
        ] = None,
        sns_topic_arn: Optional[
            "capo_imagebuilder.types.sns_topic_arn.SnsTopicArn"
        ] = None,
        resource_tags: Optional[
            "capo_imagebuilder.types.resource_tag_map.ResourceTagMap"
        ] = None,
        instance_metadata_options: Optional[
            "capo_imagebuilder.types.instance_metadata_options.InstanceMetadataOptions"
        ] = None,
        tags: Optional["capo_imagebuilder.types.tag_map.TagMap"] = None,
        placement: Optional["capo_imagebuilder.types.placement.Placement"] = None,
        dry_run: Optional["capo_imagebuilder.types.boolean.Boolean"] = None,
    ) -> "capo_imagebuilder.types.create_infrastructure_configuration_response.CreateInfrastructureConfigurationResponse":
        """<p>Creates a new infrastructure configuration. An infrastructure configuration defines the environment in which your image will be built and tested.</p>

        Args:
            name: <p>The name of the infrastructure configuration. Infrastructure configuration names must be unique to your account in each Amazon Web Services Region. Image Builder generates the infrastructure configuration ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name.</p>
            description: <p>The description of the infrastructure configuration.</p>
            instance_types: <p>The instance types of the infrastructure configuration. You can specify one or more instance types to use for this build. Image Builder picks one of these instance types based on availability. If you don't specify instance types, Image Builder selects compatible instance types automatically. If you specify a Dedicated Host, Image Builder uses only instance types that the host supports.</p>
            instance_profile_name: <p>The instance profile to associate with the instance used to customize your Amazon EC2 AMI. The instance profile must exist in your account.</p>
            security_group_ids: <p>The security group IDs to associate with the instance used to customize your Amazon EC2 AMI.</p>
            subnet_id: <p>The subnet ID in which to place the instance used to customize your Amazon EC2 AMI. If you specify <code>subnetId</code>, you must also specify one or more security group IDs in <code>securityGroupIds</code>. Otherwise, the request fails.</p>
            logging: <p>The logging configuration of the infrastructure configuration. When you configure S3 logs, Image Builder writes logs from the build and test process to the specified bucket under the key prefix.</p>
            key_pair: <p>The key pair of the infrastructure configuration. You can use this to log on to and debug the instance used to create your image.</p>
            terminate_instance_on_failure: <p>Specifies whether to terminate the instance on failure. Set to false if you want Image Builder to retain the instance used to configure your AMI if the build or test phase of your workflow fails. Defaults to <code>true</code>.</p>
            sns_topic_arn: <p>The Amazon Resource Name (ARN) of the SNS topic to which Image Builder sends image build event notifications. Specify a standard topic. Image Builder doesn't support FIFO topics. Image Builder validates the topic when you create or update the configuration. You must have permission to publish to the topic.</p> <note> <p>EC2 Image Builder can't send notifications to SNS topics that are encrypted using keys from other accounts. If your SNS topic is encrypted, the key must be owned by the same account that owns your Image Builder resources.</p> </note>
            resource_tags: <p>The metadata tags to assign to the Amazon EC2 instance that Image Builder launches during the build process. Tags are formatted as key value pairs. Tag keys can't begin with <code>aws:</code> or match one of the following reserved keys: <code>CreatedBy</code>, <code>Ec2ImageBuilderArn</code>, <code>Name</code>, or <code>Tags</code>.</p>
            instance_metadata_options: <p>The instance metadata service (IMDS) settings that Image Builder applies to the EC2 build and test instances it launches during image creation. If you don't set these options, the EC2 launch defaults for the instance apply. For more information about instance metadata options, see one of the following links:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html">Configure the instance metadata options</a> in the <i> <i>Amazon EC2 User Guide</i> </i> for Linux instances.</p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/configuring-instance-metadata-options.html">Configure the instance metadata options</a> in the <i> <i>Amazon EC2 Windows Guide</i> </i> for Windows instances.</p> </li> </ul>
            tags: <p>The metadata tags to assign to the infrastructure configuration resource that Image Builder creates as output. Tags are formatted as key value pairs.</p>
            placement: <p>The instance placement settings that define where the build and test instances that Image Builder launches during image creation run. These settings don't affect instances that you launch from the output image.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            dry_run: <p>Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a <code>DryRunOperationException</code> error response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.dry_run_operation_exception.DryRunOperationException: <p>The dry run operation of the resource was successful, and no resources or mutations were actually performed due to the dry run flag in the request.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource that you are trying to create already exists.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href="https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder">EC2 Image Builder endpoints and quotas</a>.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create an infrastructure configuration
            The following example creates an infrastructure configuration that gives Image Builder a choice of two instance types for its build and test instances.

            >>> await client.create_infrastructure_configuration(name='my-example-infrastructure', description='An infrastructure configuration for Amazon Linux builds', instance_profile_name='EC2InstanceProfileForImageBuilder', instance_types=['t3.medium', 't3.large'], terminate_instance_on_failure=True, client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE33333')
            Create an infrastructure configuration with instance placement and metadata options
            The following example creates an infrastructure configuration. It places your build and test instances in a single Availability Zone and requires IMDSv2 for instance metadata requests. It also applies resource tags to the resources that Image Builder creates during the build.

            >>> await client.create_infrastructure_configuration(name='my-example-infrastructure', description='An infrastructure configuration that pins build instances to one Availability Zone and requires IMDSv2', instance_profile_name='my-example-instance-role', placement={'availabilityZone': 'us-west-2a'}, instance_metadata_options={'httpTokens': 'required', 'httpPutResponseHopLimit': 2}, resource_tags={'CostCenter': '12345', 'Environment': 'test'}, terminate_instance_on_failure=True, client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE98765')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.create_infrastructure_configuration_request.CreateInfrastructureConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.create_infrastructure_configuration_response.CreateInfrastructureConfigurationResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.create_infrastructure_configuration

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.create_infrastructure_configuration.async_create_infrastructure_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.create_infrastructure_configuration_request.CreateInfrastructureConfigurationRequest = {
            "name": name,
            "instance_profile_name": instance_profile_name,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
        if instance_types is not None:
            input_["instance_types"] = instance_types
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if subnet_id is not None:
            input_["subnet_id"] = subnet_id
        if logging is not None:
            input_["logging"] = logging
        if key_pair is not None:
            input_["key_pair"] = key_pair
        if terminate_instance_on_failure is not None:
            input_["terminate_instance_on_failure"] = terminate_instance_on_failure
        if sns_topic_arn is not None:
            input_["sns_topic_arn"] = sns_topic_arn
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
        if instance_metadata_options is not None:
            input_["instance_metadata_options"] = instance_metadata_options
        if tags is not None:
            input_["tags"] = tags
        if placement is not None:
            input_["placement"] = placement
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_lifecycle_policy(
        self,
        name: "capo_imagebuilder.types.resource_name.ResourceName",
        execution_role: "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn",
        resource_type: "capo_imagebuilder.types.lifecycle_policy_resource_type.LifecyclePolicyResourceType",
        policy_details: "capo_imagebuilder.types.lifecycle_policy_details.LifecyclePolicyDetails",
        resource_selection: "capo_imagebuilder.types.lifecycle_policy_resource_selection.LifecyclePolicyResourceSelection",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        description: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        status: Optional[
            "capo_imagebuilder.types.lifecycle_policy_status.LifecyclePolicyStatus"
        ] = None,
        tags: Optional["capo_imagebuilder.types.tag_map.TagMap"] = None,
        dry_run: Optional["capo_imagebuilder.types.boolean.Boolean"] = None,
    ) -> "capo_imagebuilder.types.create_lifecycle_policy_response.CreateLifecyclePolicyResponse":
        """<p>Creates a lifecycle policy resource.</p>

        Args:
            name: <p>The name of the lifecycle policy to create. Policy names must be unique to your account in each Amazon Web Services Region. Image Builder generates the policy ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name. You can't change the name after creation.</p>
            description: <p>Optional description for the lifecycle policy.</p>
            status: <p>Indicates whether the lifecycle policy resource is enabled. If you don't specify a status, it defaults to <code>ENABLED</code>. Only enabled policies run on their schedule.</p>
            execution_role: <p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to run lifecycle actions. You must have permission to pass the role, and the role's trust policy must allow the Image Builder service principal to assume it.</p>
            resource_type: <p>The type of Image Builder resource that the lifecycle policy applies to. The resource type determines the allowed rule actions: policies for AMI-based Image Builder images support <code>DELETE</code>, <code>DEPRECATE</code>, and <code>DISABLE</code>, and policies for container-based Image Builder images support only <code>DELETE</code>. You can't change the resource type after creation.</p>
            policy_details: <p>Configuration details for the lifecycle policy rules. A policy can contain at most one rule per action type: one <code>DELETE</code>, one <code>DEPRECATE</code>, and one <code>DISABLE</code>.</p>
            resource_selection: <p>Selection criteria for the resources that the lifecycle policy applies to. You must specify exactly one selection criteria: either recipes or a tag map, not both.</p>
            tags: <p>Tags to apply to the lifecycle policy resource.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            dry_run: <p>Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a <code>DryRunOperationException</code> error response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.dry_run_operation_exception.DryRunOperationException: <p>The dry run operation of the resource was successful, and no resources or mutations were actually performed due to the dry run flag in the request.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource that you are trying to create already exists.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href="https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder">EC2 Image Builder endpoints and quotas</a>.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a lifecycle policy
            The following example creates a lifecycle policy that deletes AMI-based images six months after they were created, selecting the images that match the specified resource tags.

            >>> await client.create_lifecycle_policy(name='my-example-lifecycle-policy', execution_role='arn:aws:iam::111122223333:role/my-example-lifecycle-role', resource_type='AMI_IMAGE', policy_details=[{'action': {'type': 'DELETE'}, 'filter': {'type': 'AGE', 'value': 6, 'unit': 'MONTHS'}}], resource_selection={'tagMap': {'Environment': 'test'}}, client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE13579')
            Create a lifecycle policy with exclusion rules
            The following example creates a lifecycle policy that deletes images created from the specified recipe version after six months. The policy excludes images whose AMIs launched an instance within the last 30 days or are tagged to be retained.

            >>> await client.create_lifecycle_policy(name='my-example-lifecycle-policy', execution_role='arn:aws:iam::111122223333:role/my-example-lifecycle-role', resource_type='AMI_IMAGE', policy_details=[{'action': {'type': 'DELETE'}, 'filter': {'type': 'AGE', 'value': 6, 'unit': 'MONTHS'}, 'exclusionRules': {'amis': {'lastLaunched': {'value': 30, 'unit': 'DAYS'}, 'tagMap': {'Retention': 'keep'}}}}], resource_selection={'recipes': [{'name': 'my-example-recipe', 'semanticVersion': '1.0.0'}]}, client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE43210')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.create_lifecycle_policy_request.CreateLifecyclePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.create_lifecycle_policy_response.CreateLifecyclePolicyResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.create_lifecycle_policy

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.create_lifecycle_policy.async_create_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.create_lifecycle_policy_request.CreateLifecyclePolicyRequest = {
            "name": name,
            "execution_role": execution_role,
            "resource_type": resource_type,
            "policy_details": policy_details,
            "resource_selection": resource_selection,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if tags is not None:
            input_["tags"] = tags
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_workflow(
        self,
        name: "capo_imagebuilder.types.resource_name.ResourceName",
        semantic_version: "capo_imagebuilder.types.version_number.VersionNumber",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        type: "capo_imagebuilder.types.workflow_type.WorkflowType",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        description: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        change_description: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        data: Optional[
            "capo_imagebuilder.types.inline_workflow_data.InlineWorkflowData"
        ] = None,
        uri: Optional["capo_imagebuilder.types.uri.Uri"] = None,
        kms_key_id: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["capo_imagebuilder.types.tag_map.TagMap"] = None,
        dry_run: Optional["capo_imagebuilder.types.boolean.Boolean"] = None,
    ) -> "capo_imagebuilder.types.create_workflow_response.CreateWorkflowResponse":
        r"""<p>Creates a new workflow or a new version of an existing workflow. If a workflow with the same name and semantic version already exists, and your request changes its configuration, Image Builder creates a new build version. If the configuration is identical to the latest build version, the request fails because that workflow configuration already exists.</p>

        Args:
            name: <p>The name of the workflow to create. Image Builder generates the workflow ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name. If a workflow with the same name and semantic version already exists in your account in the same Amazon Web Services Region, the request creates a new build version for it. If the content is also identical to the latest build version, the request fails because the workflow already exists.</p>
            semantic_version: <p>The semantic version of this workflow resource. The semantic version syntax adheres to the following rules.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>
            description: <p>Describes the workflow.</p>
            change_description: <p>Describes what change has been made in this version of the workflow, or what makes this version different from other versions of the workflow.</p>
            data: <p>The UTF-8 encoded YAML document content for the workflow, up to 16,000 characters. For larger documents, store the document in Amazon S3 and specify the <code>uri</code> property instead. You must specify exactly one of the <code>data</code> or <code>uri</code> properties.</p>
            uri: <p>The <code>uri</code> of a YAML workflow document file stored in Amazon S3. This must be an S3 URL (<code>s3://bucket/key</code>), and you must have permission to access the S3 bucket it points to. A workflow document that you provide from Amazon S3 can be up to your service quota for workflow size.</p> <p>Alternatively, you can specify the YAML document inline, using the workflow <code>data</code> property. You must specify exactly one of the <code>data</code> or <code>uri</code> properties.</p>
            kms_key_id: <p>The Amazon Resource Name (ARN) that uniquely identifies the KMS key used to encrypt this workflow resource. This can be either the Key ARN or the Alias ARN. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>. If you don't specify a key, Image Builder encrypts the workflow document with a KMS key that Image Builder owns.</p>
            tags: <p>Tags that apply to the workflow resource.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            type: <p>The image creation stage that this workflow applies to. Image Builder validates the workflow document steps against the stage you specify.</p>
            dry_run: <p>Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a <code>DryRunOperationException</code> error response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.dry_run_operation_exception.DryRunOperationException: <p>The dry run operation of the resource was successful, and no resources or mutations were actually performed due to the dry run flag in the request.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>You have specified a combination of parameters that isn't valid. For example, two mutually exclusive parameters, or a parameter without its required companion parameter. Review the error message for details.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.invalid_version_number_exception.InvalidVersionNumberException: <p>Your version number is out of bounds or does not follow the required syntax.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href="https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder">EC2 Image Builder endpoints and quotas</a>.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a build workflow from an inline document
            The following example creates a build workflow from a YAML workflow document provided inline in the request.

            >>> await client.create_workflow(name='my-example-workflow', semantic_version='1.0.0', description='Workflow to build an AMI', type='BUILD', data='name: my-example-workflow\ndescription: Workflow to build an AMI\nschemaVersion: 1.0\nsteps:\n  - name: LaunchBuildInstance\n    action: LaunchInstance\n    onFailure: Abort\n    inputs:\n      waitFor: ssmAgent\n  - name: ApplyBuildComponents\n    action: ExecuteComponents\n    onFailure: Abort\n    inputs:\n      instanceId.$: $.stepOutputs.LaunchBuildInstance.instanceId\n  - name: CreateOutputAMI\n    action: CreateImage\n    onFailure: Abort\n    inputs:\n      instanceId.$: $.stepOutputs.LaunchBuildInstance.instanceId\n  - name: TerminateBuildInstance\n    action: TerminateInstance\n    onFailure: Continue\n    inputs:\n      instanceId.$: $.stepOutputs.LaunchBuildInstance.instanceId\n', client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE54321')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.create_workflow_request.CreateWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.create_workflow_response.CreateWorkflowResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.create_workflow

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.create_workflow.async_create_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.create_workflow_request.CreateWorkflowRequest = {
            "name": name,
            "semantic_version": semantic_version,
            "client_token": client_token,
            "type": type,
        }
        if description is not None:
            input_["description"] = description
        if change_description is not None:
            input_["change_description"] = change_description
        if data is not None:
            input_["data"] = data
        if uri is not None:
            input_["uri"] = uri
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_component(
        self,
        component_build_version_arn: "capo_imagebuilder.types.component_build_version_arn.ComponentBuildVersionArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.delete_component_response.DeleteComponentResponse":
        """<p>Deletes a component build version. The request fails with <code>ResourceDependencyException</code> if an image recipe or container recipe references this component version. It also fails if the component build version is shared with other accounts.</p>

        Args:
            component_build_version_arn: <p>The Amazon Resource Name (ARN) of the component build version to delete.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_dependency_exception.ResourceDependencyException: <p>You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a component build version
            The following example deletes the specified component build version.

            >>> await client.delete_component(component_build_version_arn='arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/1.0.0/1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.delete_component_request.DeleteComponentRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.delete_component_response.DeleteComponentResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.delete_component

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.delete_component.async_delete_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.delete_component_request.DeleteComponentRequest = {
            "component_build_version_arn": component_build_version_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_container_recipe(
        self,
        container_recipe_arn: "capo_imagebuilder.types.container_recipe_arn.ContainerRecipeArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.delete_container_recipe_response.DeleteContainerRecipeResponse":
        """<p>Deletes a container recipe. The request fails with <code>ResourceDependencyException</code> if the recipe is shared with other accounts, or if an image pipeline references it.</p>

        Args:
            container_recipe_arn: <p>The Amazon Resource Name (ARN) of the container recipe to delete.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_dependency_exception.ResourceDependencyException: <p>You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a container recipe
            The following example deletes the specified container recipe.

            >>> await client.delete_container_recipe(container_recipe_arn='arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe/1.0.0')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.delete_container_recipe_request.DeleteContainerRecipeRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.delete_container_recipe_response.DeleteContainerRecipeResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.delete_container_recipe

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.delete_container_recipe.async_delete_container_recipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.delete_container_recipe_request.DeleteContainerRecipeRequest = {
            "container_recipe_arn": container_recipe_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_distribution_configuration(
        self,
        distribution_configuration_arn: "capo_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.delete_distribution_configuration_response.DeleteDistributionConfigurationResponse":
        """<p>Deletes a distribution configuration. You can't delete a configuration that an image pipeline still references. The request fails with <code>ResourceDependencyException</code>. Update or delete the referencing pipelines first.</p>

        Args:
            distribution_configuration_arn: <p>The Amazon Resource Name (ARN) of the distribution configuration to delete.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_dependency_exception.ResourceDependencyException: <p>You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a distribution configuration
            The following example deletes the specified distribution configuration.

            >>> await client.delete_distribution_configuration(distribution_configuration_arn='arn:aws:imagebuilder:us-west-2:111122223333:distribution-configuration/my-example-distribution-configuration')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.delete_distribution_configuration_request.DeleteDistributionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.delete_distribution_configuration_response.DeleteDistributionConfigurationResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.delete_distribution_configuration

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.delete_distribution_configuration.async_delete_distribution_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.delete_distribution_configuration_request.DeleteDistributionConfigurationRequest = {
            "distribution_configuration_arn": distribution_configuration_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_image(
        self,
        image_build_version_arn: "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.delete_image_response.DeleteImageResponse":
        """<p>Deletes an Image Builder image resource. This does not delete any EC2 AMIs or ECR container images that are created during the image build process. You must clean those up separately, using the appropriate Amazon EC2 or Amazon ECR console actions, or API or CLI commands.</p> <p>The request fails with <code>ResourceDependencyException</code> if the image is shared with other accounts, or if other resources depend on it. It also fails while the image build is still running. Cancel an in-progress build with <a>CancelImageCreation</a> before you delete the image.</p> <ul> <li> <p>To deregister an EC2 Linux AMI, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/deregister-ami.html">Deregister your Linux AMI</a> in the <i> <i>Amazon EC2 User Guide</i> </i>.</p> </li> <li> <p>To deregister an EC2 Windows AMI, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/deregister-ami.html">Deregister your Windows AMI</a> in the <i> <i>Amazon EC2 Windows Guide</i> </i>.</p> </li> <li> <p>To delete a container image from Amazon ECR, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/delete_image.html">Deleting an image</a> in the <i>Amazon ECR User Guide</i>.</p> </li> </ul>

        Args:
            image_build_version_arn: <p>The Amazon Resource Name (ARN) of the Image Builder image resource to delete.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_dependency_exception.ResourceDependencyException: <p>You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an image build version
            The following example deletes the Image Builder image record for the specified build version - EC2 AMIs or ECR container images that the build created aren't removed.

            >>> await client.delete_image(image_build_version_arn='arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.delete_image_request.DeleteImageRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.delete_image_response.DeleteImageResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.delete_image

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.delete_image.async_delete_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.delete_image_request.DeleteImageRequest = {
            "image_build_version_arn": image_build_version_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_image_pipeline(
        self,
        image_pipeline_arn: "capo_imagebuilder.types.image_pipeline_arn.ImagePipelineArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.delete_image_pipeline_response.DeleteImagePipelineResponse":
        """<p>Deletes an image pipeline. Images that the pipeline created aren't deleted - remove those separately with <a>DeleteImage</a>. You can delete a pipeline while a build that it started is still running. The build continues independently.</p>

        Args:
            image_pipeline_arn: <p>The Amazon Resource Name (ARN) of the image pipeline to delete.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_dependency_exception.ResourceDependencyException: <p>You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an image pipeline
            The following example deletes an image pipeline.

            >>> await client.delete_image_pipeline(image_pipeline_arn='arn:aws:imagebuilder:us-west-2:111122223333:image-pipeline/my-example-pipeline')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.delete_image_pipeline_request.DeleteImagePipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.delete_image_pipeline_response.DeleteImagePipelineResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.delete_image_pipeline

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.delete_image_pipeline.async_delete_image_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.delete_image_pipeline_request.DeleteImagePipelineRequest = {
            "image_pipeline_arn": image_pipeline_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_image_recipe(
        self,
        image_recipe_arn: "capo_imagebuilder.types.image_recipe_arn.ImageRecipeArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> (
        "capo_imagebuilder.types.delete_image_recipe_response.DeleteImageRecipeResponse"
    ):
        """<p>Deletes an image recipe.</p>

        Args:
            image_recipe_arn: <p>The Amazon Resource Name (ARN) of the image recipe to delete.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_dependency_exception.ResourceDependencyException: <p>You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an image recipe
            The following example deletes the specified image recipe version.

            >>> await client.delete_image_recipe(image_recipe_arn='arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.0.0')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.delete_image_recipe_request.DeleteImageRecipeRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.delete_image_recipe_response.DeleteImageRecipeResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.delete_image_recipe

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.delete_image_recipe.async_delete_image_recipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.delete_image_recipe_request.DeleteImageRecipeRequest = {
            "image_recipe_arn": image_recipe_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_infrastructure_configuration(
        self,
        infrastructure_configuration_arn: "capo_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.delete_infrastructure_configuration_response.DeleteInfrastructureConfigurationResponse":
        """<p>Deletes an infrastructure configuration. You can't delete a configuration that an image pipeline still references. The request fails with <code>ResourceDependencyException</code>. Update or delete the referencing pipelines first.</p>

        Args:
            infrastructure_configuration_arn: <p>The Amazon Resource Name (ARN) of the infrastructure configuration to delete.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_dependency_exception.ResourceDependencyException: <p>You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an infrastructure configuration
            The following example deletes the infrastructure configuration with the specified ARN.

            >>> await client.delete_infrastructure_configuration(infrastructure_configuration_arn='arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.delete_infrastructure_configuration_request.DeleteInfrastructureConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.delete_infrastructure_configuration_response.DeleteInfrastructureConfigurationResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.delete_infrastructure_configuration

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.delete_infrastructure_configuration.async_delete_infrastructure_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.delete_infrastructure_configuration_request.DeleteInfrastructureConfigurationRequest = {
            "infrastructure_configuration_arn": infrastructure_configuration_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_lifecycle_policy(
        self,
        lifecycle_policy_arn: "capo_imagebuilder.types.lifecycle_policy_arn.LifecyclePolicyArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.delete_lifecycle_policy_response.DeleteLifecyclePolicyResponse":
        """<p>Deletes the specified lifecycle policy resource. Deleting the policy removes its schedule, so no further lifecycle runs occur for that policy. If a lifecycle execution is in progress for the policy, Image Builder cancels it. Deletion doesn't revert actions that the policy already applied to your resources.</p>

        Args:
            lifecycle_policy_arn: <p>The Amazon Resource Name (ARN) of the lifecycle policy resource to delete.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_dependency_exception.ResourceDependencyException: <p>You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a lifecycle policy
            The following example deletes the specified lifecycle policy.

            >>> await client.delete_lifecycle_policy(lifecycle_policy_arn='arn:aws:imagebuilder:us-west-2:111122223333:lifecycle-policy/my-example-lifecycle-policy')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.delete_lifecycle_policy_request.DeleteLifecyclePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.delete_lifecycle_policy_response.DeleteLifecyclePolicyResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.delete_lifecycle_policy

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.delete_lifecycle_policy.async_delete_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.delete_lifecycle_policy_request.DeleteLifecyclePolicyRequest = {
            "lifecycle_policy_arn": lifecycle_policy_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_workflow(
        self,
        workflow_build_version_arn: "capo_imagebuilder.types.workflow_build_version_arn.WorkflowBuildVersionArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.delete_workflow_response.DeleteWorkflowResponse":
        """<p>Deletes a specific workflow resource. You can't delete a workflow build version while an image pipeline references it. The request fails with <code>ResourceDependencyException</code>.</p>

        Args:
            workflow_build_version_arn: <p>The Amazon Resource Name (ARN) of the workflow resource to delete.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_dependency_exception.ResourceDependencyException: <p>You have attempted to mutate or delete a resource with a dependency that prohibits this action. See the error message for more details.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a workflow build version
            The following example deletes the workflow build version that the ARN specifies.

            >>> await client.delete_workflow(workflow_build_version_arn='arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/1.0.0/1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.delete_workflow_request.DeleteWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.delete_workflow_response.DeleteWorkflowResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.delete_workflow

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.delete_workflow.async_delete_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.delete_workflow_request.DeleteWorkflowRequest = {
            "workflow_build_version_arn": workflow_build_version_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def distribute_image(
        self,
        source_image: "capo_imagebuilder.types.non_empty_string.NonEmptyString",
        distribution_configuration_arn: "capo_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn",
        execution_role: "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        tags: Optional["capo_imagebuilder.types.tag_map.TagMap"] = None,
        logging_configuration: Optional[
            "capo_imagebuilder.types.image_logging_configuration.ImageLoggingConfiguration"
        ] = None,
    ) -> "capo_imagebuilder.types.distribute_image_response.DistributeImageResponse":
        """<p>Distributes an existing AMI to target Regions and accounts without running the full image build process. This operation only runs the distribution phase on an image that has already been built.</p>

        Args:
            source_image: <p>The source image to distribute. You can specify the source in any of the following formats:</p> <ul> <li> <p>An AMI ID.</p> </li> <li> <p>An Amazon Web Services Systems Manager Parameter Store reference, prefixed by <code>ssm:</code>, followed by the parameter name or ARN.</p> </li> <li> <p>An Image Builder image Amazon Resource Name (ARN). An image version ARN resolves to the latest available build version.</p> </li> </ul> <p>Whichever format you use, the source must resolve to an AMI in the current Amazon Web Services Region.</p>
            distribution_configuration_arn: <p>The Amazon Resource Name (ARN) of the distribution configuration. The configuration defines target Regions, accounts, and AMI settings. The distribution configuration must be in the same Region as this operation.</p>
            execution_role: <p>The name or Amazon Resource Name (ARN) of the IAM role that Image Builder assumes to distribute the image.</p>
            tags: <p>The tags to apply to the new Image Builder image resource that this operation creates. To tag the output AMIs, use <code>amiTags</code> in the distribution configuration.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            logging_configuration: <p>The logging configuration for the distribution.</p>

        Raises:
            capo_imagebuilder.errors.access_denied_exception.AccessDeniedException: <p>You do not have permissions to perform the requested operation.</p>
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the number of permitted resources or operations for this service. For service quotas, see <a href="https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder">EC2 Image Builder endpoints and quotas</a>.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.too_many_requests_exception.TooManyRequestsException: <p>You have attempted too many requests for the specific operation.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Distribute an existing AMI
            The following example distributes an AMI that you own to the targets defined in the specified distribution configuration. It returns the ARN of a new Image Builder image resource that you can use with GetImage to monitor distribution progress.

            >>> await client.distribute_image(source_image='ami-1234567890abcdef0', distribution_configuration_arn='arn:aws:imagebuilder:us-west-2:111122223333:distribution-configuration/my-example-distribution-configuration', execution_role='arn:aws:iam::111122223333:role/aws-service-role/imagebuilder.amazonaws.com/AWSServiceRoleForImageBuilder', client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE86420')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.distribute_image_request.DistributeImageRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.distribute_image_response.DistributeImageResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.distribute_image

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.distribute_image.async_distribute_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.distribute_image_request.DistributeImageRequest = {
            "source_image": source_image,
            "distribution_configuration_arn": distribution_configuration_arn,
            "execution_role": execution_role,
            "client_token": client_token,
        }
        if tags is not None:
            input_["tags"] = tags
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_component(
        self,
        component_build_version_arn: "capo_imagebuilder.types.component_version_arn_or_build_version_arn.ComponentVersionArnOrBuildVersionArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.get_component_response.GetComponentResponse":
        """<p>Retrieves a component object.</p>

        Args:
            component_build_version_arn: <p>The Amazon Resource Name (ARN) of the component that you want to get. You can specify a build version ARN, or a component version ARN. The version can use the <code>x</code> wildcard in trailing positions, for example <code>1.0.x</code> or <code>1.x.x</code>. Version ARNs resolve to the latest available matching component build version.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the details of a component build version
            The following example retrieves a component build version. The data field in the response contains the YAML document that defines the component.

            >>> await client.get_component(component_build_version_arn='arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/1.0.0/1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.get_component_request.GetComponentRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.get_component_response.GetComponentResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.get_component

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.get_component.async_get_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.get_component_request.GetComponentRequest = {
            "component_build_version_arn": component_build_version_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_component_policy(
        self,
        component_arn: "capo_imagebuilder.types.component_build_version_arn.ComponentBuildVersionArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.get_component_policy_response.GetComponentPolicyResponse":
        """<p>Retrieves a component policy.</p>

        Args:
            component_arn: <p>The Amazon Resource Name (ARN) of the component whose policy you want to retrieve.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the resource policy for a component
            The following example retrieves the resource policy that's applied to a component that the owner shared with another account.

            >>> await client.get_component_policy(component_arn='arn:aws:imagebuilder:us-west-2:111122223333:component/my-shared-component/1.0.0/1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.get_component_policy_request.GetComponentPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.get_component_policy_response.GetComponentPolicyResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.get_component_policy

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.get_component_policy.async_get_component_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.get_component_policy_request.GetComponentPolicyRequest = {
            "component_arn": component_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_container_recipe(
        self,
        container_recipe_arn: "capo_imagebuilder.types.container_recipe_arn.ContainerRecipeArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.get_container_recipe_response.GetContainerRecipeResponse":
        """<p>Retrieves a container recipe.</p>

        Args:
            container_recipe_arn: <p>The Amazon Resource Name (ARN) of the container recipe to retrieve.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the details of a container recipe
            The following example retrieves the details of the specified container recipe.

            >>> await client.get_container_recipe(container_recipe_arn='arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe/1.0.0')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.get_container_recipe_request.GetContainerRecipeRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.get_container_recipe_response.GetContainerRecipeResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.get_container_recipe

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.get_container_recipe.async_get_container_recipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.get_container_recipe_request.GetContainerRecipeRequest = {
            "container_recipe_arn": container_recipe_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_container_recipe_policy(
        self,
        container_recipe_arn: "capo_imagebuilder.types.container_recipe_arn.ContainerRecipeArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.get_container_recipe_policy_response.GetContainerRecipePolicyResponse":
        """<p>Retrieves the policy for a container recipe.</p>

        Args:
            container_recipe_arn: <p>The Amazon Resource Name (ARN) of the container recipe for the policy being requested.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the policy attached to a container recipe
            The following example retrieves the resource policy for a container recipe that you shared with another AWS account. The policy property contains the resource-based policy document as a JSON-encoded string.

            >>> await client.get_container_recipe_policy(container_recipe_arn='arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe-shared/1.0.0')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.get_container_recipe_policy_request.GetContainerRecipePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.get_container_recipe_policy_response.GetContainerRecipePolicyResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.get_container_recipe_policy

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.get_container_recipe_policy.async_get_container_recipe_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.get_container_recipe_policy_request.GetContainerRecipePolicyRequest = {
            "container_recipe_arn": container_recipe_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_distribution_configuration(
        self,
        distribution_configuration_arn: "capo_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.get_distribution_configuration_response.GetDistributionConfigurationResponse":
        """<p>Retrieves a distribution configuration.</p>

        Args:
            distribution_configuration_arn: <p>The Amazon Resource Name (ARN) of the distribution configuration that you want to retrieve.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the details of a distribution configuration
            The following example retrieves a distribution configuration that distributes the output AMI to two Regions.

            >>> await client.get_distribution_configuration(distribution_configuration_arn='arn:aws:imagebuilder:us-west-2:111122223333:distribution-configuration/my-example-distribution')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.get_distribution_configuration_request.GetDistributionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.get_distribution_configuration_response.GetDistributionConfigurationResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.get_distribution_configuration

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.get_distribution_configuration.async_get_distribution_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.get_distribution_configuration_request.GetDistributionConfigurationRequest = {
            "distribution_configuration_arn": distribution_configuration_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_image(
        self,
        image_build_version_arn: "capo_imagebuilder.types.image_version_arn_or_build_version_arn.ImageVersionArnOrBuildVersionArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.get_image_response.GetImageResponse":
        """<p>Retrieves an image.</p>

        Args:
            image_build_version_arn: <p>The Amazon Resource Name (ARN) of the image that you want to get. You can specify a full build version ARN, or a version ARN with or without wildcards (<code>x.x.x</code>, <code>1.x.x</code>, or <code>1.0.x</code>). A version or wildcard ARN resolves to the latest matching build version that has reached <code>AVAILABLE</code> status. Builds that were later deprecated, disabled, or deleted don't resolve. To get an image in any other state, such as a failed or in-progress build, specify the full build version ARN.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Check the status of an image build
            The following example retrieves an image build version to check its status while the build is running. The response is shortened to show a subset of the fields that Image Builder returns.

            >>> await client.get_image(image_build_version_arn='arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.get_image_request.GetImageRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.get_image_response.GetImageResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.get_image

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.get_image.async_get_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.get_image_request.GetImageRequest = {
            "image_build_version_arn": image_build_version_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_image_pipeline(
        self,
        image_pipeline_arn: "capo_imagebuilder.types.image_pipeline_arn.ImagePipelineArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.get_image_pipeline_response.GetImagePipelineResponse":
        """<p>Retrieves an image pipeline.</p>

        Args:
            image_pipeline_arn: <p>The Amazon Resource Name (ARN) of the image pipeline that you want to retrieve.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the details of an image pipeline
            The following example retrieves an image pipeline that builds a new image every Sunday, including the image tests configuration and schedule start condition defaults that Image Builder applied at creation.

            >>> await client.get_image_pipeline(image_pipeline_arn='arn:aws:imagebuilder:us-west-2:111122223333:image-pipeline/my-example-pipeline')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.get_image_pipeline_request.GetImagePipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.get_image_pipeline_response.GetImagePipelineResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.get_image_pipeline

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.get_image_pipeline.async_get_image_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.get_image_pipeline_request.GetImagePipelineRequest = {
            "image_pipeline_arn": image_pipeline_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_image_policy(
        self,
        image_arn: "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.get_image_policy_response.GetImagePolicyResponse":
        """<p>Retrieves an image policy.</p>

        Args:
            image_arn: <p>The Amazon Resource Name (ARN) of the image whose policy you want to retrieve.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieve the resource policy for an image
            The following example retrieves the resource policy for an image build version that was shared with account 444455556666.

            >>> await client.get_image_policy(image_arn='arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.get_image_policy_request.GetImagePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.get_image_policy_response.GetImagePolicyResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.get_image_policy

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.get_image_policy.async_get_image_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.get_image_policy_request.GetImagePolicyRequest = {
            "image_arn": image_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_image_recipe(
        self,
        image_recipe_arn: "capo_imagebuilder.types.image_recipe_arn.ImageRecipeArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.get_image_recipe_response.GetImageRecipeResponse":
        """<p>Retrieves an image recipe.</p>

        Args:
            image_recipe_arn: <p>The Amazon Resource Name (ARN) of the image recipe that you want to retrieve. You can use the <code>x</code> wildcard in trailing version positions to retrieve the latest matching version, for example <code>x.x.x</code> or <code>1.x.x</code>.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the details of an image recipe
            The following example retrieves the full definition of an image recipe, including the components it applies and the base image it builds on.

            >>> await client.get_image_recipe(image_recipe_arn='arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-app-recipe/1.0.0')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.get_image_recipe_request.GetImageRecipeRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.get_image_recipe_response.GetImageRecipeResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.get_image_recipe

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.get_image_recipe.async_get_image_recipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.get_image_recipe_request.GetImageRecipeRequest = {
            "image_recipe_arn": image_recipe_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_image_recipe_policy(
        self,
        image_recipe_arn: "capo_imagebuilder.types.image_recipe_arn.ImageRecipeArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.get_image_recipe_policy_response.GetImageRecipePolicyResponse":
        """<p>Retrieves an image recipe policy.</p>

        Args:
            image_recipe_arn: <p>The Amazon Resource Name (ARN) of the image recipe whose policy you want to retrieve.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the resource policy for an image recipe
            The following example retrieves the resource policy that's applied to the specified image recipe.

            >>> await client.get_image_recipe_policy(image_recipe_arn='arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.0.0')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.get_image_recipe_policy_request.GetImageRecipePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.get_image_recipe_policy_response.GetImageRecipePolicyResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.get_image_recipe_policy

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.get_image_recipe_policy.async_get_image_recipe_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.get_image_recipe_policy_request.GetImageRecipePolicyRequest = {
            "image_recipe_arn": image_recipe_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_infrastructure_configuration(
        self,
        infrastructure_configuration_arn: "capo_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.get_infrastructure_configuration_response.GetInfrastructureConfigurationResponse":
        """<p>Retrieves an infrastructure configuration.</p>

        Args:
            infrastructure_configuration_arn: <p>The Amazon Resource Name (ARN) of the infrastructure configuration that you want to retrieve.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the details of an infrastructure configuration
            The following example retrieves an infrastructure configuration that specifies the instance types, instance profile, and instance metadata options that Image Builder uses for build and test instances.

            >>> await client.get_infrastructure_configuration(infrastructure_configuration_arn='arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure-configuration')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.get_infrastructure_configuration_request.GetInfrastructureConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.get_infrastructure_configuration_response.GetInfrastructureConfigurationResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.get_infrastructure_configuration

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.get_infrastructure_configuration.async_get_infrastructure_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.get_infrastructure_configuration_request.GetInfrastructureConfigurationRequest = {
            "infrastructure_configuration_arn": infrastructure_configuration_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_lifecycle_execution(
        self,
        lifecycle_execution_id: "capo_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.get_lifecycle_execution_response.GetLifecycleExecutionResponse":
        """<p>Retrieves runtime information for a lifecycle execution – a single run of lifecycle actions that a lifecycle policy or a <a>StartResourceStateUpdate</a> request started.</p>

        Args:
            lifecycle_execution_id: <p>The unique identifier for a runtime instance of the lifecycle policy.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the details of a lifecycle execution
            The following example retrieves the runtime status of the specified lifecycle execution. If the execution was started by StartResourceStateUpdate rather than a lifecycle policy run, the response doesn't include the lifecyclePolicyArn field.

            >>> await client.get_lifecycle_execution(lifecycle_execution_id='lce-401aefc3-a829-46f6-8fc2-91497988a503')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.get_lifecycle_execution_request.GetLifecycleExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.get_lifecycle_execution_response.GetLifecycleExecutionResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.get_lifecycle_execution

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.get_lifecycle_execution.async_get_lifecycle_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.get_lifecycle_execution_request.GetLifecycleExecutionRequest = {
            "lifecycle_execution_id": lifecycle_execution_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_lifecycle_policy(
        self,
        lifecycle_policy_arn: "capo_imagebuilder.types.lifecycle_policy_arn.LifecyclePolicyArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.get_lifecycle_policy_response.GetLifecyclePolicyResponse":
        """<p>Retrieves details for the specified image lifecycle policy.</p>

        Args:
            lifecycle_policy_arn: <p>Specifies the Amazon Resource Name (ARN) of the image lifecycle policy resource to get.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the details of a lifecycle policy
            The following example retrieves the full definition of the specified lifecycle policy.

            >>> await client.get_lifecycle_policy(lifecycle_policy_arn='arn:aws:imagebuilder:us-west-2:111122223333:lifecycle-policy/my-example-lifecycle-policy')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.get_lifecycle_policy_request.GetLifecyclePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.get_lifecycle_policy_response.GetLifecyclePolicyResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.get_lifecycle_policy

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.get_lifecycle_policy.async_get_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.get_lifecycle_policy_request.GetLifecyclePolicyRequest = {
            "lifecycle_policy_arn": lifecycle_policy_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_marketplace_resource(
        self,
        resource_type: "capo_imagebuilder.types.marketplace_resource_type.MarketplaceResourceType",
        resource_arn: "capo_imagebuilder.types.image_builder_arn.ImageBuilderArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        resource_location: Optional[
            "capo_imagebuilder.types.marketplace_resource_location.MarketplaceResourceLocation"
        ] = None,
    ) -> "capo_imagebuilder.types.get_marketplace_resource_response.GetMarketplaceResourceResponse":
        """<p>Verifies the subscription and performs resource dependency checks on the requested Amazon Web Services Marketplace resource. The caller must be entitled to the resource. For Amazon Web Services Marketplace components, the response contains fields to download the components and their artifacts.</p>

        Args:
            resource_type: <p>Specifies which type of Amazon Web Services Marketplace resource Image Builder retrieves.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies an Amazon Web Services Marketplace resource.</p>
            resource_location: <p>The Amazon S3 location of the component artifact to retrieve, in <code>s3://bucket/key</code> form.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.get_marketplace_resource_request.GetMarketplaceResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.get_marketplace_resource_response.GetMarketplaceResourceResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.get_marketplace_resource

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.get_marketplace_resource.async_get_marketplace_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.get_marketplace_resource_request.GetMarketplaceResourceRequest = {
            "resource_type": resource_type,
            "resource_arn": resource_arn,
        }
        if resource_location is not None:
            input_["resource_location"] = resource_location

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_workflow(
        self,
        workflow_build_version_arn: "capo_imagebuilder.types.workflow_version_arn_or_build_version_arn.WorkflowVersionArnOrBuildVersionArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.get_workflow_response.GetWorkflowResponse":
        """<p>Retrieves a workflow resource object.</p>

        Args:
            workflow_build_version_arn: <p>The Amazon Resource Name (ARN) of the workflow resource that you want to get. You can specify a build version ARN, or a version ARN with or without wildcards (<code>x</code>) in its version segments. Image Builder resolves version and wildcard ARNs to the most recent matching build version.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the details of a workflow build version
            The following example retrieves a workflow build version. The response includes the YAML workflow document in the data field and the parameters that Image Builder extracted from it when the workflow was created.

            >>> await client.get_workflow(workflow_build_version_arn='arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/1.0.0/1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.get_workflow_request.GetWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.get_workflow_response.GetWorkflowResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.get_workflow

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.get_workflow.async_get_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.get_workflow_request.GetWorkflowRequest = {
            "workflow_build_version_arn": workflow_build_version_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_workflow_execution(
        self,
        workflow_execution_id: "capo_imagebuilder.types.workflow_execution_id.WorkflowExecutionId",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.get_workflow_execution_response.GetWorkflowExecutionResponse":
        """<p>Retrieves runtime information for a specific runtime instance of the workflow.</p>

        Args:
            workflow_execution_id: <p>Use the unique identifier for a runtime instance of the workflow to get runtime details.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the runtime details for a workflow execution
            The following example retrieves runtime status and step counts for the build workflow that ran for an image build version, using the workflow execution ID returned by ListWorkflowExecutions.

            >>> await client.get_workflow_execution(workflow_execution_id='wf-165b1cb6-3a62-4618-a021-94ddcbe32908')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.get_workflow_execution_request.GetWorkflowExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.get_workflow_execution_response.GetWorkflowExecutionResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.get_workflow_execution

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.get_workflow_execution.async_get_workflow_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.get_workflow_execution_request.GetWorkflowExecutionRequest = {
            "workflow_execution_id": workflow_execution_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_workflow_step_execution(
        self,
        step_execution_id: "capo_imagebuilder.types.workflow_step_execution_id.WorkflowStepExecutionId",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.get_workflow_step_execution_response.GetWorkflowStepExecutionResponse":
        """<p>Retrieves runtime information for a specific runtime instance of the workflow step.</p>

        Args:
            step_execution_id: <p>The unique identifier for the runtime instance of the workflow step that you want to get runtime details for. To get the identifiers for the steps that ran in a workflow, call <a>ListWorkflowStepExecutions</a>.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the runtime details of a workflow step
            The following example retrieves runtime details for the step that launched the build instance during an image build, with the step's input parameters and output values returned as JSON-encoded strings.

            >>> await client.get_workflow_step_execution(step_execution_id='step-2e6fef0d-657c-4b7e-8706-ff24da9afa01')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.get_workflow_step_execution_request.GetWorkflowStepExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.get_workflow_step_execution_response.GetWorkflowStepExecutionResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.get_workflow_step_execution

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.get_workflow_step_execution.async_get_workflow_step_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.get_workflow_step_execution_request.GetWorkflowStepExecutionRequest = {
            "step_execution_id": step_execution_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_component(
        self,
        name: "capo_imagebuilder.types.resource_name.ResourceName",
        semantic_version: "capo_imagebuilder.types.version_number.VersionNumber",
        type: "capo_imagebuilder.types.component_type.ComponentType",
        format: "capo_imagebuilder.types.component_format.ComponentFormat",
        platform: "capo_imagebuilder.types.platform.Platform",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        description: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        change_description: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        data: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        uri: Optional["capo_imagebuilder.types.uri.Uri"] = None,
        kms_key_id: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["capo_imagebuilder.types.tag_map.TagMap"] = None,
    ) -> "capo_imagebuilder.types.import_component_response.ImportComponentResponse":
        r"""<p>Imports a component and transforms its data into a component document. For the <code>SHELL</code> format, Image Builder wraps your script in a component document with a single step that runs the script.</p>

        Args:
            name: <p>The name of the component. Image Builder generates the component ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name. If a component with the same name and semantic version already exists in your account in the same Amazon Web Services Region, the request creates a new build version for it. If the content is also identical to the latest build version, the request fails because the component already exists.</p>
            semantic_version: <p>The semantic version of the component. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>
            description: <p>The description of the component. Describes the contents of the component.</p>
            change_description: <p>The change description of the component. This description indicates the change that has been made in this version, or what makes this version different from other versions of the component.</p>
            type: <p>The type of the component denotes whether the component is used to build the image, or only to test it.</p>
            format: <p>The format of the resource that you want to import as a component.</p>
            platform: <p>The platform of the component.</p>
            data: <p>The data of the component. For the <code>SHELL</code> format, this is the plain script content. You must specify exactly one of the <code>data</code> or <code>uri</code> properties. For scripts that exceed the inline length constraint, use the <code>uri</code> property.</p>
            uri: <p>The uri of the component. Must be an Amazon S3 URL and you must have permission to access the Amazon S3 bucket. If you use Amazon S3, you can specify component content up to your service quota. Either <code>data</code> or <code>uri</code> can be used to specify the data within the component.</p>
            kms_key_id: <p>The Amazon Resource Name (ARN) of the KMS key that is used to encrypt this component. This can be either the Key ARN or the Alias ARN. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>. If you don't specify a key, Image Builder encrypts the component data with a KMS key that Image Builder owns.</p>
            tags: <p>The tags of the component.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>You have specified a combination of parameters that isn't valid. For example, two mutually exclusive parameters, or a parameter without its required companion parameter. Review the error message for details.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.invalid_version_number_exception.InvalidVersionNumberException: <p>Your version number is out of bounds or does not follow the required syntax.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Import a component from a shell script
            The following example imports a plain shell script as a Linux build component.

            >>> await client.import_component(name='my-example-imported-component', semantic_version='1.0.0', description='Installs my application from an imported shell script', type='BUILD', format='SHELL', platform='Linux', data='sudo yum update -y\nsudo yum -y install my-app\n', client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE88888')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.import_component_request.ImportComponentRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.import_component_response.ImportComponentResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.import_component

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.import_component.async_import_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.import_component_request.ImportComponentRequest = {
            "name": name,
            "semantic_version": semantic_version,
            "type": type,
            "format": format,
            "platform": platform,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
        if change_description is not None:
            input_["change_description"] = change_description
        if data is not None:
            input_["data"] = data
        if uri is not None:
            input_["uri"] = uri
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_disk_image(
        self,
        name: "capo_imagebuilder.types.resource_name.ResourceName",
        semantic_version: "capo_imagebuilder.types.version_number.VersionNumber",
        platform: "capo_imagebuilder.types.non_empty_string.NonEmptyString",
        os_version: "capo_imagebuilder.types.os_version.OsVersion",
        infrastructure_configuration_arn: "capo_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn",
        uri: "capo_imagebuilder.types.uri.Uri",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        description: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        execution_role: Optional[
            "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
        ] = None,
        logging_configuration: Optional[
            "capo_imagebuilder.types.image_logging_configuration.ImageLoggingConfiguration"
        ] = None,
        tags: Optional["capo_imagebuilder.types.tag_map.TagMap"] = None,
        register_image_options: Optional[
            "capo_imagebuilder.types.register_image_options.RegisterImageOptions"
        ] = None,
        windows_configuration: Optional[
            "capo_imagebuilder.types.windows_configuration.WindowsConfiguration"
        ] = None,
    ) -> "capo_imagebuilder.types.import_disk_image_response.ImportDiskImageResponse":
        """<p>Imports a Windows operating system image from a verified Microsoft ISO disk file. The following disk images are supported:</p> <ul> <li> <p>Windows 11 Enterprise</p> </li> </ul> <p>The response returns as soon as Image Builder creates the new image resource in the <code>PENDING</code> state. The conversion from ISO file to AMI then runs asynchronously on an EC2 instance that Image Builder launches with the specified infrastructure configuration.</p>

        Args:
            name: <p>The name of the image resource that's created from the import. Image Builder generates the image ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name. If an image with the same name and semantic version already exists in your account in the same Amazon Web Services Region, the import creates a new build version for it.</p>
            semantic_version: <p>The semantic version to attach to the image that's created during the import process. This version follows the semantic version syntax.</p>
            description: <p>The description for your disk image import.</p>
            platform: <p>The operating system platform for the imported image. Allowed values include the following: <code>Windows</code>.</p>
            os_version: <p>The operating system version for the imported image. The only supported value is <code>Microsoft Windows 11</code>.</p>
            execution_role: <p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions to import an image from a Microsoft ISO file. If you don't provide a role, Image Builder uses the Image Builder service-linked role in your account, and creates it if it doesn't exist.</p>
            infrastructure_configuration_arn: <p>The Amazon Resource Name (ARN) of the infrastructure configuration resource that's used for launching the EC2 instance on which the ISO image is built.</p>
            uri: <p>The <code>uri</code> of the ISO disk file that's stored in Amazon S3, in <code>s3://bucket/key</code> format. The key must end with the <code>.iso</code>, <code>.ISO</code>, or <code>.Iso</code> extension, and the bucket must be owned by the account that makes the request.</p>
            logging_configuration: <p>The CloudWatch Logs log group where Image Builder sends the import logs. If you specify a log group name outside of the <code>/aws/imagebuilder/</code> namespace, you must also provide an <code>executionRole</code> that has permission to write to that log group.</p>
            tags: <p>Tags that are attached to image resources created from the import.</p>
            register_image_options: <p>Configures Secure Boot and UEFI settings for the imported image.</p>
            windows_configuration: <p>Specifies Windows settings for ISO imports.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            capo_imagebuilder.errors.access_denied_exception.AccessDeniedException: <p>You do not have permissions to perform the requested operation.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.too_many_requests_exception.TooManyRequestsException: <p>You have attempted too many requests for the specific operation.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Import a Windows 11 ISO disk image
            The following example starts an image build that converts a Windows 11 ISO disk file stored in Amazon S3 into an AMI; the imageBuildVersionArn in the response identifies the Image Builder image resource that tracks the build, not the output AMI.

            >>> await client.import_disk_image(name='my-example-imported-image', semantic_version='1.0.0', platform='Windows', os_version='Microsoft Windows 11', uri='s3://amzn-s3-demo-bucket/Win11_23H2_English_x64.iso', infrastructure_configuration_arn='arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure', client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE12345')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.import_disk_image_request.ImportDiskImageRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.import_disk_image_response.ImportDiskImageResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.import_disk_image

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.import_disk_image.async_import_disk_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.import_disk_image_request.ImportDiskImageRequest = {
            "name": name,
            "semantic_version": semantic_version,
            "platform": platform,
            "os_version": os_version,
            "infrastructure_configuration_arn": infrastructure_configuration_arn,
            "uri": uri,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
        if execution_role is not None:
            input_["execution_role"] = execution_role
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if tags is not None:
            input_["tags"] = tags
        if register_image_options is not None:
            input_["register_image_options"] = register_image_options
        if windows_configuration is not None:
            input_["windows_configuration"] = windows_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_vm_image(
        self,
        name: "capo_imagebuilder.types.non_empty_string.NonEmptyString",
        semantic_version: "capo_imagebuilder.types.version_number.VersionNumber",
        platform: "capo_imagebuilder.types.platform.Platform",
        vm_import_task_id: "capo_imagebuilder.types.non_empty_string.NonEmptyString",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        description: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        os_version: Optional["capo_imagebuilder.types.os_version.OsVersion"] = None,
        logging_configuration: Optional[
            "capo_imagebuilder.types.image_logging_configuration.ImageLoggingConfiguration"
        ] = None,
        tags: Optional["capo_imagebuilder.types.tag_map.TagMap"] = None,
    ) -> "capo_imagebuilder.types.import_vm_image_response.ImportVmImageResponse":
        """<p>Creates an Image Builder image resource from an Amazon EC2 VM import task. The response returns as soon as Image Builder creates the image resource in the <code>PENDING</code> state. Image Builder then monitors the import task asynchronously. When the task completes, Image Builder records the AMI that it produced as the new image's output resource and marks the image <code>AVAILABLE</code>. You can then use the imported image as the base image for your recipes.</p> <p>To create the VM import task, use the Amazon EC2 API <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportImage.html">ImportImage</a> operation, or the <a href="https://docs.aws.amazon.com/cli/latest/reference/ec2/import-image.html">import-image</a> CLI command.</p>

        Args:
            name: <p>The name of the base image that is created by the import process. Image Builder generates the image ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name. If an image with the same name and semantic version already exists in your account in the same Amazon Web Services Region, the import creates a new build version for it.</p>
            semantic_version: <p>The semantic version to attach to the base image that was created during the import process. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>
            description: <p>The description for the base image that is created by the import process.</p>
            platform: <p>The operating system platform for the imported VM.</p>
            os_version: <p>The operating system version for the imported VM.</p>
            vm_import_task_id: <p>The <code>importTaskId</code> (API) or <code>ImportTaskId</code> (CLI) from the Amazon EC2 VM import process. The import task doesn't need to be complete when you call ImportVmImage - Image Builder monitors the task and finishes creating the image when the task completes.</p>
            logging_configuration: <p>The CloudWatch Logs log group where Image Builder sends the import logs. For ImportVmImage, the log group name must be within the <code>/aws/imagebuilder/</code> namespace.</p>
            tags: <p>Tags that are attached to the import resources.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Import a virtual machine as an Image Builder image
            The following example registers the output of an EC2 VM Import/Export task (import-ami) as a new Image Builder image, so you can use the imported virtual machine as a base image.

            >>> await client.import_vm_image(name='my-example-imported-image', semantic_version='1.0.0', platform='Linux', os_version='Amazon Linux 2', vm_import_task_id='import-ami-1234567890abcdef0', client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE00000')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.import_vm_image_request.ImportVmImageRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.import_vm_image_response.ImportVmImageResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.import_vm_image

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.import_vm_image.async_import_vm_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.import_vm_image_request.ImportVmImageRequest = {
            "name": name,
            "semantic_version": semantic_version,
            "platform": platform,
            "vm_import_task_id": vm_import_task_id,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
        if os_version is not None:
            input_["os_version"] = os_version
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_component_build_versions(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        component_version_arn: Optional[
            "capo_imagebuilder.types.component_version_arn.ComponentVersionArn"
        ] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_component_build_versions_response.ListComponentBuildVersionsResponse":
        """<p>Returns a list of component build versions for the specified component version ARN. You can only list build versions for components that your account owns. Deprecated build versions aren't included in the results.</p>

        Args:
            component_version_arn: <p>The component version ARN whose build versions you want to list. The ARN must specify an exact version, without a build number suffix. If you don't specify an ARN, Image Builder returns build versions for the components that your account owns.</p>
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the build versions of a component
            The following example lists the build versions that exist for version 1.0.0 of the specified component. The list returns the most recent build version first.

            >>> await client.list_component_build_versions(component_version_arn='arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/1.0.0')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_component_build_versions_request.ListComponentBuildVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_component_build_versions_response.ListComponentBuildVersionsResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_component_build_versions

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_component_build_versions.async_list_component_build_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_component_build_versions_request.ListComponentBuildVersionsRequest = {}
        if component_version_arn is not None:
            input_["component_version_arn"] = component_version_arn
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

    async def iter_list_component_build_versions(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        component_version_arn: Optional[
            "capo_imagebuilder.types.component_version_arn.ComponentVersionArn"
        ] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.component_summary.ComponentSummary]":
        _token = next_token
        while True:
            _response = await self.list_component_build_versions(
                config_overrides=config_overrides,
                component_version_arn=component_version_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("component_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_components(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        owner: Optional["capo_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        by_name: Optional["capo_imagebuilder.types.boolean.Boolean"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_components_response.ListComponentsResponse":
        """<p>Returns the list of components that you have access to. By default, the response doesn't include components in the <code>DEPRECATED</code> state. To list deprecated components, use the <code>status</code> filter with the value <code>DEPRECATED</code>.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Filtering:</b> You can use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.</p> </note>

        Args:
            owner: <p>Filters results based on the type of owner for the component. By default, this request returns a list of components that your account owns. To see results for other types of owners, you can specify components that Amazon manages, components from the Amazon Web Services Marketplace, third party components, or components that other accounts have shared with you.</p>
            filters: <p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>description</code> </p> </li> <li> <p> <code>name</code> </p> </li> <li> <p> <code>platform</code> </p> </li> <li> <p> <code>productCodes</code> </p> </li> <li> <p> <code>status</code> </p> </li> <li> <p> <code>supportedOsVersion</code> </p> </li> <li> <p> <code>type</code> </p> </li> <li> <p> <code>version</code> </p> </li> </ul>
            by_name: <p>Specifies whether to return one entry per component name, with all versions of each component aggregated. Defaults to <code>false</code>, which returns one entry per component version. You can't combine this option with the <code>version</code> filter.</p>
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List components that you own
            The following example lists the component versions that your account owns, filtered to components for the Linux platform.

            >>> await client.list_components(owner='Self', filters=[{'name': 'platform', 'values': ['Linux']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_components_request.ListComponentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_components_response.ListComponentsResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_components

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_components.async_list_components(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_components_request.ListComponentsRequest = {}
        if owner is not None:
            input_["owner"] = owner
        if filters is not None:
            input_["filters"] = filters
        if by_name is not None:
            input_["by_name"] = by_name
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

    async def iter_list_components(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        owner: Optional["capo_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        by_name: Optional["capo_imagebuilder.types.boolean.Boolean"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.component_version.ComponentVersion]":
        _token = next_token
        while True:
            _response = await self.list_components(
                config_overrides=config_overrides,
                owner=owner,
                filters=filters,
                by_name=by_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("component_version_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_container_recipes(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        owner: Optional["capo_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_container_recipes_response.ListContainerRecipesResponse":
        """<p>Returns a list of container recipes.</p>

        Args:
            owner: <p>Returns container recipes belonging to the specified owner, that have been shared with you. You can omit this field to return container recipes belonging to your account. For container recipes, the valid owner values are <code>Self</code>, <code>Shared</code>, and <code>Amazon</code>.</p>
            filters: <p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>containerType</code> </p> </li> <li> <p> <code>name</code> </p> </li> <li> <p> <code>parentImage</code> </p> </li> <li> <p> <code>platform</code> </p> </li> </ul>
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the container recipes you own
            The following example lists the container recipes that you own.

            >>> await client.list_container_recipes(owner='Self')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_container_recipes_request.ListContainerRecipesRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_container_recipes_response.ListContainerRecipesResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_container_recipes

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_container_recipes.async_list_container_recipes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_container_recipes_request.ListContainerRecipesRequest = {}
        if owner is not None:
            input_["owner"] = owner
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_container_recipes(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        owner: Optional["capo_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.container_recipe_summary.ContainerRecipeSummary]":
        _token = next_token
        while True:
            _response = await self.list_container_recipes(
                config_overrides=config_overrides,
                owner=owner,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("container_recipe_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_distribution_configurations(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_distribution_configurations_response.ListDistributionConfigurationsResponse":
        """<p>Returns a list of distribution configurations.</p>

        Args:
            filters: <p>You can filter on <code>name</code> to streamline results.</p>
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List distribution configurations that match a name filter
            The following example lists the distribution configurations whose name matches the filter value.

            >>> await client.list_distribution_configurations(filters=[{'name': 'name', 'values': ['my-example-distribution-configuration']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_distribution_configurations_request.ListDistributionConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_distribution_configurations_response.ListDistributionConfigurationsResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_distribution_configurations

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_distribution_configurations.async_list_distribution_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_distribution_configurations_request.ListDistributionConfigurationsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_distribution_configurations(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.distribution_configuration_summary.DistributionConfigurationSummary]":
        _token = next_token
        while True:
            _response = await self.list_distribution_configurations(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(
                _response, ("distribution_configuration_summary_list",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_image_build_versions(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        image_version_arn: Optional[
            "capo_imagebuilder.types.image_version_arn.ImageVersionArn"
        ] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_image_build_versions_response.ListImageBuildVersionsResponse":
        """<p>Returns a list of image build versions.</p>

        Args:
            image_version_arn: <p>The Amazon Resource Name (ARN) of the image version whose build versions you want to retrieve. The ARN must specify an exact version (<code><major>.<minor>.<patch></code>) - wildcards aren't allowed. This parameter is optional. If you don't specify it, Image Builder returns build versions for all of the images in your account.</p>
            filters: <p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>name</code> </p> </li> <li> <p> <code>osVersion</code> </p> </li> <li> <p> <code>platform</code> </p> </li> <li> <p> <code>type</code> </p> </li> <li> <p> <code>version</code> </p> </li> </ul>
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the build versions of an image
            The following example lists the build versions that exist for version 1.0.0 of the specified image, with the output AMI that each build produced.

            >>> await client.list_image_build_versions(image_version_arn='arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_image_build_versions_request.ListImageBuildVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_image_build_versions_response.ListImageBuildVersionsResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_image_build_versions

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_image_build_versions.async_list_image_build_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_image_build_versions_request.ListImageBuildVersionsRequest = {}
        if image_version_arn is not None:
            input_["image_version_arn"] = image_version_arn
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_image_build_versions(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        image_version_arn: Optional[
            "capo_imagebuilder.types.image_version_arn.ImageVersionArn"
        ] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.image_summary.ImageSummary]":
        _token = next_token
        while True:
            _response = await self.list_image_build_versions(
                config_overrides=config_overrides,
                image_version_arn=image_version_arn,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("image_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_image_packages(
        self,
        image_build_version_arn: "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "capo_imagebuilder.types.list_image_packages_response.ListImagePackagesResponse"
    ):
        """<p>Lists the packages that are associated with an image build version, as determined by Amazon Web Services Systems Manager Inventory at build time.</p>

        Args:
            image_build_version_arn: <p>The Amazon Resource Name (ARN) of the image build version whose packages you want to list. The value must be a full build version ARN.</p>
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the packages in an image build version
            The following example lists the operating system packages that Image Builder detected in the specified image build version.

            >>> await client.list_image_packages(image_build_version_arn='arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_image_packages_request.ListImagePackagesRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_image_packages_response.ListImagePackagesResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_image_packages

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_image_packages.async_list_image_packages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_image_packages_request.ListImagePackagesRequest = {
            "image_build_version_arn": image_build_version_arn
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

    async def iter_list_image_packages(
        self,
        image_build_version_arn: "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.image_package.ImagePackage]":
        _token = next_token
        while True:
            _response = await self.list_image_packages(
                image_build_version_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("image_package_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_image_pipeline_images(
        self,
        image_pipeline_arn: "capo_imagebuilder.types.image_pipeline_arn.ImagePipelineArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_image_pipeline_images_response.ListImagePipelineImagesResponse":
        """<p>Returns a list of images created by the specified pipeline.</p>

        Args:
            image_pipeline_arn: <p>The Amazon Resource Name (ARN) of the image pipeline whose images you want to view.</p>
            filters: <p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>name</code> </p> </li> <li> <p> <code>version</code> </p> </li> </ul>
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the images that an image pipeline created
            The following example lists the images that the specified pipeline created, including a build that is still in progress.

            >>> await client.list_image_pipeline_images(image_pipeline_arn='arn:aws:imagebuilder:us-west-2:111122223333:image-pipeline/my-example-pipeline')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_image_pipeline_images_request.ListImagePipelineImagesRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_image_pipeline_images_response.ListImagePipelineImagesResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_image_pipeline_images

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_image_pipeline_images.async_list_image_pipeline_images(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_image_pipeline_images_request.ListImagePipelineImagesRequest = {
            "image_pipeline_arn": image_pipeline_arn
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_image_pipeline_images(
        self,
        image_pipeline_arn: "capo_imagebuilder.types.image_pipeline_arn.ImagePipelineArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.image_summary.ImageSummary]":
        _token = next_token
        while True:
            _response = await self.list_image_pipeline_images(
                image_pipeline_arn,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("image_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_image_pipelines(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_image_pipelines_response.ListImagePipelinesResponse":
        """<p>Returns a list of image pipelines.</p>

        Args:
            filters: <p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>description</code> </p> </li> <li> <p> <code>distributionConfigurationArn</code> </p> </li> <li> <p> <code>imageRecipeArn</code> </p> </li> <li> <p> <code>infrastructureConfigurationArn</code> </p> </li> <li> <p> <code>name</code> </p> </li> <li> <p> <code>status</code> </p> </li> </ul>
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List image pipelines filtered by name
            The following example lists the image pipelines in your account, using a filter to match a specific pipeline name.

            >>> await client.list_image_pipelines(filters=[{'name': 'name', 'values': ['my-example-pipeline']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_image_pipelines_request.ListImagePipelinesRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_image_pipelines_response.ListImagePipelinesResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_image_pipelines

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_image_pipelines.async_list_image_pipelines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_image_pipelines_request.ListImagePipelinesRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_image_pipelines(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.image_pipeline.ImagePipeline]":
        _token = next_token
        while True:
            _response = await self.list_image_pipelines(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("image_pipeline_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_image_recipes(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        owner: Optional["capo_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_image_recipes_response.ListImageRecipesResponse":
        """<p>Returns a list of image recipes.</p>

        Args:
            owner: <p>You can specify the recipe owner to filter results by that owner. By default, this request will only show image recipes owned by your account. To filter by a different owner, specify one of the <code>Valid Values</code> that are listed for this parameter.</p>
            filters: <p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>name</code> </p> </li> <li> <p> <code>parentImage</code> </p> </li> <li> <p> <code>platform</code> </p> </li> </ul>
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the image recipes that you own
            The following example lists the image recipes that you own.

            >>> await client.list_image_recipes(owner='Self')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_image_recipes_request.ListImageRecipesRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_image_recipes_response.ListImageRecipesResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_image_recipes

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_image_recipes.async_list_image_recipes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_image_recipes_request.ListImageRecipesRequest = {}
        if owner is not None:
            input_["owner"] = owner
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_image_recipes(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        owner: Optional["capo_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "AsyncIterator[capo_imagebuilder.types.image_recipe_summary.ImageRecipeSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_image_recipes(
                config_overrides=config_overrides,
                owner=owner,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("image_recipe_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_images(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        owner: Optional["capo_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        by_name: Optional["capo_imagebuilder.types.boolean.Boolean"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
        include_deprecated: Optional[
            "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "capo_imagebuilder.types.list_images_response.ListImagesResponse":
        """<p>Returns the list of images that you have access to.</p>

        Args:
            owner: <p>Filters the list to images owned by you, by Amazon, or shared with you by other accounts. By default, only your account's images are returned.</p>
            filters: <p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>name</code> </p> </li> <li> <p> <code>osVersion</code> </p> </li> <li> <p> <code>platform</code> </p> </li> <li> <p> <code>type</code> </p> </li> <li> <p> <code>version</code> </p> </li> </ul>
            by_name: <p>Specifies whether to return one entry per image name, with all versions of each image aggregated. Defaults to <code>false</code>, which returns one entry per image version. You can't combine this option with the <code>version</code> filter.</p>
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>
            include_deprecated: <p>Specifies whether to include deprecated Amazon-managed images in the results. Deprecated images that you own are always returned. Defaults to <code>false</code>.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List images that you own
            The following example lists the image versions that you own. Setting byName to false returns each image version as its own entry, instead of grouping build versions under their image name.

            >>> await client.list_images(owner='Self', by_name=False)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_images_request.ListImagesRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_images_response.ListImagesResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_images

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_images.async_list_images(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_images_request.ListImagesRequest = {}
        if owner is not None:
            input_["owner"] = owner
        if filters is not None:
            input_["filters"] = filters
        if by_name is not None:
            input_["by_name"] = by_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if include_deprecated is not None:
            input_["include_deprecated"] = include_deprecated

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_images(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        owner: Optional["capo_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        by_name: Optional["capo_imagebuilder.types.boolean.Boolean"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
        include_deprecated: Optional[
            "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.image_version.ImageVersion]":
        _token = next_token
        while True:
            _response = await self.list_images(
                config_overrides=config_overrides,
                owner=owner,
                filters=filters,
                by_name=by_name,
                max_results=max_results,
                next_token=_token,
                include_deprecated=include_deprecated,
            )
            _page = _resolve_path(_response, ("image_version_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_image_scan_finding_aggregations(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        filter: Optional["capo_imagebuilder.types.filter.Filter"] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_image_scan_finding_aggregations_response.ListImageScanFindingAggregationsResponse":
        """<p>Returns a list of image scan aggregations for your account. You can filter by the type of key that Image Builder uses to group results. For example, if you want to get a list of findings by severity level for one of your pipelines, you might specify your pipeline with the <code>imagePipelineArn</code> filter. If you don't specify a filter, Image Builder returns an aggregation for your account.</p> <p>To streamline results, you can use the following filters in your request:</p> <ul> <li> <p> <code>imageBuildVersionArn</code> </p> </li> <li> <p> <code>imagePipelineArn</code> </p> </li> <li> <p> <code>vulnerabilityId</code> </p> </li> </ul>

        Args:
            filter: <p>A filter name and value pair that determines the type of aggregation that Image Builder returns. Use one of the following filter names:</p> <ul> <li> <p> <code>imageBuildVersionArn</code> </p> </li> <li> <p> <code>imagePipelineArn</code> </p> </li> <li> <p> <code>vulnerabilityId</code> </p> </li> </ul> <p>If you don't specify a filter, Image Builder returns an aggregation for your account.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List image scan finding aggregations for an image pipeline
            The following example aggregates vulnerability findings for images that the specified pipeline created, with counts grouped by severity level.

            >>> await client.list_image_scan_finding_aggregations(filter={'name': 'imagePipelineArn', 'values': ['arn:aws:imagebuilder:us-west-2:111122223333:image-pipeline/my-example-pipeline']})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_image_scan_finding_aggregations_request.ListImageScanFindingAggregationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_image_scan_finding_aggregations_response.ListImageScanFindingAggregationsResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_image_scan_finding_aggregations

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_image_scan_finding_aggregations.async_list_image_scan_finding_aggregations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_image_scan_finding_aggregations_request.ListImageScanFindingAggregationsRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_image_scan_finding_aggregations(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        filter: Optional["capo_imagebuilder.types.filter.Filter"] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.image_scan_finding_aggregation.ImageScanFindingAggregation]":
        _token = next_token
        while True:
            _response = await self.list_image_scan_finding_aggregations(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("responses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_image_scan_findings(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        filters: Optional[
            "capo_imagebuilder.types.image_scan_findings_filter_list.ImageScanFindingsFilterList"
        ] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_image_scan_findings_response.ListImageScanFindingsResponse":
        """<p>Returns a list of image scan findings for your account. Amazon Inspector generates the findings when it scans images that have scanning enabled.</p>

        Args:
            filters: <p>An array of name value pairs that you can use to filter your results. You can use the following filters to streamline results:</p> <ul> <li> <p> <code>imageBuildVersionArn</code> – Filters findings by the image build version that was scanned.</p> </li> <li> <p> <code>imagePipelineArn</code> – Filters findings by the pipeline that created the scanned image.</p> </li> <li> <p> <code>vulnerabilityId</code> – Filters findings by vulnerability ID, for example a CVE ID.</p> </li> <li> <p> <code>severity</code> – Filters findings by severity level.</p> </li> </ul> <p>If you don't request a filter, then all findings in your account are listed.</p>
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List vulnerability findings for an image build
            The following example lists the vulnerability findings that Amazon Inspector detected for the specified image build version.

            >>> await client.list_image_scan_findings(filters=[{'name': 'imageBuildVersionArn', 'values': ['arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_image_scan_findings_request.ListImageScanFindingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_image_scan_findings_response.ListImageScanFindingsResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_image_scan_findings

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_image_scan_findings.async_list_image_scan_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_image_scan_findings_request.ListImageScanFindingsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_image_scan_findings(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        filters: Optional[
            "capo_imagebuilder.types.image_scan_findings_filter_list.ImageScanFindingsFilterList"
        ] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.image_scan_finding.ImageScanFinding]":
        _token = next_token
        while True:
            _response = await self.list_image_scan_findings(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("findings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_infrastructure_configurations(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_infrastructure_configurations_response.ListInfrastructureConfigurationsResponse":
        """<p>Returns a list of infrastructure configurations.</p>

        Args:
            filters: <p>You can filter on <code>name</code> to streamline results.</p>
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List infrastructure configurations by name
            The following example lists your infrastructure configurations, filtered to a specific resource name.

            >>> await client.list_infrastructure_configurations(filters=[{'name': 'name', 'values': ['my-example-infrastructure-configuration']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_infrastructure_configurations_request.ListInfrastructureConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_infrastructure_configurations_response.ListInfrastructureConfigurationsResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_infrastructure_configurations

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_infrastructure_configurations.async_list_infrastructure_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_infrastructure_configurations_request.ListInfrastructureConfigurationsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_infrastructure_configurations(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.infrastructure_configuration_summary.InfrastructureConfigurationSummary]":
        _token = next_token
        while True:
            _response = await self.list_infrastructure_configurations(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(
                _response, ("infrastructure_configuration_summary_list",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_lifecycle_execution_resources(
        self,
        lifecycle_execution_id: "capo_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        parent_resource_id: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_lifecycle_execution_resources_response.ListLifecycleExecutionResourcesResponse":
        """<p>Lists resources that the runtime instance of the image lifecycle identified for lifecycle actions.</p>

        Args:
            lifecycle_execution_id: <p>The unique identifier for a runtime instance of the lifecycle policy.</p>
            parent_resource_id: <p>The Amazon Resource Name (ARN) of an image build version to get the output resources for, such as AMIs or container images in Amazon ECR. You can get this value from the <code>resourceId</code> in the top-level response. If you leave this property empty, the response lists the Image Builder resources that the lifecycle execution identified for lifecycle actions. If the image build version that you specify in <code>parentResourceId</code> wasn't part of this lifecycle execution, the response contains an empty list.</p>
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the resources that a lifecycle execution acted on
            The following example lists the resources that the specified lifecycle execution acted on. For a scheduled resource state update that hasn't started to apply changes yet, the resources list is empty.

            >>> await client.list_lifecycle_execution_resources(lifecycle_execution_id='lce-401aefc3-a829-46f6-8fc2-91497988a503')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_lifecycle_execution_resources_request.ListLifecycleExecutionResourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_lifecycle_execution_resources_response.ListLifecycleExecutionResourcesResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_lifecycle_execution_resources

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_lifecycle_execution_resources.async_list_lifecycle_execution_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_lifecycle_execution_resources_request.ListLifecycleExecutionResourcesRequest = {
            "lifecycle_execution_id": lifecycle_execution_id
        }
        if parent_resource_id is not None:
            input_["parent_resource_id"] = parent_resource_id
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

    async def iter_list_lifecycle_execution_resources(
        self,
        lifecycle_execution_id: "capo_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        parent_resource_id: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.lifecycle_execution_resource.LifecycleExecutionResource]":
        _token = next_token
        while True:
            _response = await self.list_lifecycle_execution_resources(
                lifecycle_execution_id,
                config_overrides=config_overrides,
                parent_resource_id=parent_resource_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_lifecycle_executions(
        self,
        resource_arn: "capo_imagebuilder.types.image_builder_arn.ImageBuilderArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_lifecycle_executions_response.ListLifecycleExecutionsResponse":
        """<p>Retrieves the lifecycle runtime history for the specified resource.</p>

        Args:
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to list lifecycle executions. Specify a lifecycle policy ARN to list its executions, or an image build version ARN to list the executions that <a>StartResourceStateUpdate</a> started for that image. Other ARN types aren't valid for this request.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List lifecycle executions for an image build version
            The following example lists the lifecycle executions that have run against the specified image build version. The execution shown was started with StartResourceStateUpdate rather than a lifecycle policy, so it has no lifecyclePolicyArn.

            >>> await client.list_lifecycle_executions(resource_arn='arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_lifecycle_executions_request.ListLifecycleExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_lifecycle_executions_response.ListLifecycleExecutionsResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_lifecycle_executions

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_lifecycle_executions.async_list_lifecycle_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_lifecycle_executions_request.ListLifecycleExecutionsRequest = {
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

    async def iter_list_lifecycle_executions(
        self,
        resource_arn: "capo_imagebuilder.types.image_builder_arn.ImageBuilderArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "AsyncIterator[capo_imagebuilder.types.lifecycle_execution.LifecycleExecution]"
    ):
        _token = next_token
        while True:
            _response = await self.list_lifecycle_executions(
                resource_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("lifecycle_executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_lifecycle_policies(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_lifecycle_policies_response.ListLifecyclePoliciesResponse":
        """<p>Retrieves a list of lifecycle policies in your Amazon Web Services account.</p>

        Args:
            filters: <p>Use the following filters to streamline results: <code>name</code>, <code>resourceType</code>, and <code>status</code>. Filter names are matched exactly as shown.</p>
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List enabled lifecycle policies
            The following example lists the lifecycle policies in your account that have ENABLED status.

            >>> await client.list_lifecycle_policies(filters=[{'name': 'status', 'values': ['ENABLED']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_lifecycle_policies_request.ListLifecyclePoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_lifecycle_policies_response.ListLifecyclePoliciesResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_lifecycle_policies

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_lifecycle_policies.async_list_lifecycle_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_lifecycle_policies_request.ListLifecyclePoliciesRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_lifecycle_policies(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.lifecycle_policy_summary.LifecyclePolicySummary]":
        _token = next_token
        while True:
            _response = await self.list_lifecycle_policies(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("lifecycle_policy_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_imagebuilder.types.image_builder_arn.ImageBuilderArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns the list of tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.</p>

        Raises:
            capo_imagebuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the tags for a resource
            The following example lists the tags that are assigned to an existing component build version.

            >>> await client.list_tags_for_resource(resource_arn='arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/1.0.0/1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_waiting_workflow_steps(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_waiting_workflow_steps_response.ListWaitingWorkflowStepsResponse":
        """<p>Lists the workflow steps in your Amazon Web Services account that have paused at a <code>WaitForAction</code> step, and are waiting for you to respond. To send a response, call <a>SendWorkflowStepAction</a>.</p>

        Args:
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List workflow steps that are waiting for an action
            The following example lists the workflow steps in your account that are paused at a WaitForAction step, waiting for you to resume or stop the workflow with SendWorkflowStepAction.

            >>> await client.list_waiting_workflow_steps(max_results=25)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_waiting_workflow_steps_request.ListWaitingWorkflowStepsRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_waiting_workflow_steps_response.ListWaitingWorkflowStepsResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_waiting_workflow_steps

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_waiting_workflow_steps.async_list_waiting_workflow_steps(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_waiting_workflow_steps_request.ListWaitingWorkflowStepsRequest = {}
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

    async def iter_list_waiting_workflow_steps(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.workflow_step_execution.WorkflowStepExecution]":
        _token = next_token
        while True:
            _response = await self.list_waiting_workflow_steps(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("steps",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_workflow_build_versions(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        workflow_version_arn: Optional[
            "capo_imagebuilder.types.workflow_wildcard_version_arn.WorkflowWildcardVersionArn"
        ] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_workflow_build_versions_response.ListWorkflowBuildVersionsResponse":
        """<p>Returns a list of build versions for a specific workflow resource.</p>

        Args:
            workflow_version_arn: <p>The Amazon Resource Name (ARN) of the workflow resource for which to get a list of build versions. The version segments can contain wildcards (<code>x</code>) to match multiple versions of the workflow. If you don't specify an ARN, the response lists build versions for all of the workflows in your account.</p>
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the build versions of a workflow
            The following example lists the build versions that exist for version 1.0.0 of the specified workflow, with the most recent build version first and the change description for each build version showing what changed.

            >>> await client.list_workflow_build_versions(workflow_version_arn='arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/1.0.0')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_workflow_build_versions_request.ListWorkflowBuildVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_workflow_build_versions_response.ListWorkflowBuildVersionsResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_workflow_build_versions

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_workflow_build_versions.async_list_workflow_build_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_workflow_build_versions_request.ListWorkflowBuildVersionsRequest = {}
        if workflow_version_arn is not None:
            input_["workflow_version_arn"] = workflow_version_arn
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

    async def iter_list_workflow_build_versions(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        workflow_version_arn: Optional[
            "capo_imagebuilder.types.workflow_wildcard_version_arn.WorkflowWildcardVersionArn"
        ] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.workflow_summary.WorkflowSummary]":
        _token = next_token
        while True:
            _response = await self.list_workflow_build_versions(
                config_overrides=config_overrides,
                workflow_version_arn=workflow_version_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("workflow_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_workflow_executions(
        self,
        image_build_version_arn: "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_workflow_executions_response.ListWorkflowExecutionsResponse":
        """<p>Returns a list of workflow runtime instance metadata objects for a specific image build version.</p>

        Args:
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>
            image_build_version_arn: <p>List all workflow runtime instances for the specified image build version resource ARN.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the workflow runtime instances for an image build version
            The following example lists the workflow runtime instances that ran for the specified image build version, which was built with the Image Builder default build and test workflows.

            >>> await client.list_workflow_executions(image_build_version_arn='arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_workflow_executions_request.ListWorkflowExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_workflow_executions_response.ListWorkflowExecutionsResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_workflow_executions

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_workflow_executions.async_list_workflow_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_workflow_executions_request.ListWorkflowExecutionsRequest = {
            "image_build_version_arn": image_build_version_arn
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

    async def iter_list_workflow_executions(
        self,
        image_build_version_arn: "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.workflow_execution_metadata.WorkflowExecutionMetadata]":
        _token = next_token
        while True:
            _response = await self.list_workflow_executions(
                image_build_version_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("workflow_executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_workflows(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        owner: Optional["capo_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        by_name: Optional["capo_imagebuilder.types.boolean.Boolean"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_workflows_response.ListWorkflowsResponse":
        """<p>Lists workflow versions based on filtering parameters. To list the build versions of a specific workflow version, call <a>ListWorkflowBuildVersions</a>.</p>

        Args:
            owner: <p>Filters results based on the workflow owner. By default, this request returns the workflows that your account owns (<code>Self</code>). Specify <code>Amazon</code> to list the workflows that Image Builder manages. Image Builder rejects the <code>Shared</code> and <code>ThirdParty</code> owner values for workflows, and <code>AWSMarketplace</code> returns no results.</p>
            filters: <p>Filters to narrow the list of workflows. You can filter on <code>name</code>, <code>version</code>, <code>description</code>, and <code>type</code>.</p>
            by_name: <p>Specifies whether to return one entry per workflow name, with all versions of each workflow aggregated. Defaults to <code>false</code>, which returns one entry per workflow version. You can't combine this option with the <code>version</code> filter.</p>
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List workflows that you own
            The following example lists the workflow versions that you own.

            >>> await client.list_workflows(owner='Self')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_workflows_request.ListWorkflowsRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_workflows_response.ListWorkflowsResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_workflows

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_workflows.async_list_workflows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_workflows_request.ListWorkflowsRequest = {}
        if owner is not None:
            input_["owner"] = owner
        if filters is not None:
            input_["filters"] = filters
        if by_name is not None:
            input_["by_name"] = by_name
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

    async def iter_list_workflows(
        self,
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        owner: Optional["capo_imagebuilder.types.ownership.Ownership"] = None,
        filters: Optional["capo_imagebuilder.types.filter_list.FilterList"] = None,
        by_name: Optional["capo_imagebuilder.types.boolean.Boolean"] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.workflow_version.WorkflowVersion]":
        _token = next_token
        while True:
            _response = await self.list_workflows(
                config_overrides=config_overrides,
                owner=owner,
                filters=filters,
                by_name=by_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("workflow_version_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_workflow_step_executions(
        self,
        workflow_execution_id: "capo_imagebuilder.types.workflow_execution_id.WorkflowExecutionId",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_imagebuilder.types.list_workflow_step_executions_response.ListWorkflowStepExecutionsResponse":
        """<p>Returns runtime data for each step in a runtime instance of the workflow that you specify in the request.</p>

        Args:
            max_results: <p>The maximum number of items to return in a single request.</p>
            next_token: <p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>
            workflow_execution_id: <p>The unique identifier that Image Builder assigned to keep track of runtime details when it ran the workflow.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>You have provided an invalid pagination token in your request.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the steps that ran in a workflow execution
            The following example lists runtime details for each step in the specified runtime instance of a workflow, in this case the build workflow from an image build.

            >>> await client.list_workflow_step_executions(workflow_execution_id='wf-165b1cb6-3a62-4618-a021-94ddcbe32908')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.list_workflow_step_executions_request.ListWorkflowStepExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.list_workflow_step_executions_response.ListWorkflowStepExecutionsResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.list_workflow_step_executions

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.list_workflow_step_executions.async_list_workflow_step_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.list_workflow_step_executions_request.ListWorkflowStepExecutionsRequest = {
            "workflow_execution_id": workflow_execution_id
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

    async def iter_list_workflow_step_executions(
        self,
        workflow_execution_id: "capo_imagebuilder.types.workflow_execution_id.WorkflowExecutionId",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        max_results: Optional[
            "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
        ] = None,
        next_token: Optional[
            "capo_imagebuilder.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_imagebuilder.types.workflow_step_metadata.WorkflowStepMetadata]":
        _token = next_token
        while True:
            _response = await self.list_workflow_step_executions(
                workflow_execution_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("steps",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_component_policy(
        self,
        component_arn: "capo_imagebuilder.types.component_build_version_arn.ComponentBuildVersionArn",
        policy: "capo_imagebuilder.types.resource_policy_document.ResourcePolicyDocument",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.put_component_policy_response.PutComponentPolicyResponse":
        """<p>Applies a policy to a component. The preferred way to share resources is with the RAM API <a href="https://docs.aws.amazon.com/ram/latest/APIReference/API_CreateResourceShare.html">CreateResourceShare</a>. If you use the PutComponentPolicy operation instead, you must also call the RAM API <a href="https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html">PromoteResourceShareCreatedFromPolicy</a>. Otherwise, the resource isn't visible to the principals that it's shared with.</p>

        Args:
            component_arn: <p>The Amazon Resource Name (ARN) of the component that this policy should be applied to.</p>
            policy: <p>The policy to apply.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value that you provided for the specified parameter is invalid.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Share a component with another account
            The following example applies a resource policy that grants another account permission to get and list the component.

            >>> await client.put_component_policy(component_arn='arn:aws:imagebuilder:us-west-2:111122223333:component/my-shared-component/1.0.0/1', policy='{"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Principal": {"AWS": "arn:aws:iam::444455556666:root"}, "Action": ["imagebuilder:GetComponent", "imagebuilder:ListComponents"], "Resource": ["arn:aws:imagebuilder:us-west-2:111122223333:component/my-shared-component/1.0.0/1"]}]}')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.put_component_policy_request.PutComponentPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.put_component_policy_response.PutComponentPolicyResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.put_component_policy

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.put_component_policy.async_put_component_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.put_component_policy_request.PutComponentPolicyRequest = {
            "component_arn": component_arn,
            "policy": policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_container_recipe_policy(
        self,
        container_recipe_arn: "capo_imagebuilder.types.container_recipe_arn.ContainerRecipeArn",
        policy: "capo_imagebuilder.types.resource_policy_document.ResourcePolicyDocument",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.put_container_recipe_policy_response.PutContainerRecipePolicyResponse":
        """<p>Applies a policy to a container recipe. The preferred way to share resources is with the RAM API <a href="https://docs.aws.amazon.com/ram/latest/APIReference/API_CreateResourceShare.html">CreateResourceShare</a>. If you use the PutContainerRecipePolicy operation instead, you must also call the RAM API <a href="https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html">PromoteResourceShareCreatedFromPolicy</a>. Otherwise, the resource isn't visible to the principals that it's shared with.</p>

        Args:
            container_recipe_arn: <p>The Amazon Resource Name (ARN) of the container recipe that this policy should be applied to.</p>
            policy: <p>The policy to apply to the container recipe.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value that you provided for the specified parameter is invalid.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Share a container recipe with another account
            The following example applies a resource policy that grants another AWS account permission to view and use the specified container recipe.

            >>> await client.put_container_recipe_policy(container_recipe_arn='arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe-shared/1.0.0', policy='{"Version": "2012-10-17", "Statement": [{"Sid": "AllowSharedAccountContainerRecipeAccess", "Effect": "Allow", "Principal": {"AWS": "arn:aws:iam::444455556666:root"}, "Action": ["imagebuilder:GetContainerRecipe", "imagebuilder:ListContainerRecipes"], "Resource": "arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe-shared/1.0.0"}]}')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.put_container_recipe_policy_request.PutContainerRecipePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.put_container_recipe_policy_response.PutContainerRecipePolicyResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.put_container_recipe_policy

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.put_container_recipe_policy.async_put_container_recipe_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.put_container_recipe_policy_request.PutContainerRecipePolicyRequest = {
            "container_recipe_arn": container_recipe_arn,
            "policy": policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_image_policy(
        self,
        image_arn: "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        policy: "capo_imagebuilder.types.resource_policy_document.ResourcePolicyDocument",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.put_image_policy_response.PutImagePolicyResponse":
        """<p>Applies a policy to an image. The preferred way to share resources is with the RAM API <a href="https://docs.aws.amazon.com/ram/latest/APIReference/API_CreateResourceShare.html">CreateResourceShare</a>. If you use the PutImagePolicy operation instead, you must also call the RAM API <a href="https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html">PromoteResourceShareCreatedFromPolicy</a>. Otherwise, the resource isn't visible to the principals that it's shared with.</p>

        Args:
            image_arn: <p>The Amazon Resource Name (ARN) of the image that this policy should be applied to.</p>
            policy: <p>The resource policy to apply to the image, as a JSON policy document. Image Builder validates the policy with Amazon Web Services RAM before applying it, and rejects invalid policies with <code>InvalidParameterValueException</code>.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value that you provided for the specified parameter is invalid.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Share an image with another AWS account
            The following example applies a resource policy to an image build version that grants another AWS account permission to view the image.

            >>> await client.put_image_policy(image_arn='arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1', policy='{"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Principal": {"AWS": "arn:aws:iam::444455556666:root"}, "Action": ["imagebuilder:GetImage", "imagebuilder:ListImages"], "Resource": ["arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1"]}]}')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.put_image_policy_request.PutImagePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.put_image_policy_response.PutImagePolicyResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.put_image_policy

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.put_image_policy.async_put_image_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.put_image_policy_request.PutImagePolicyRequest = {
            "image_arn": image_arn,
            "policy": policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_image_recipe_policy(
        self,
        image_recipe_arn: "capo_imagebuilder.types.image_recipe_arn.ImageRecipeArn",
        policy: "capo_imagebuilder.types.resource_policy_document.ResourcePolicyDocument",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.put_image_recipe_policy_response.PutImageRecipePolicyResponse":
        """<p>Applies a policy to an image recipe. The preferred way to share resources is with the RAM API <a href="https://docs.aws.amazon.com/ram/latest/APIReference/API_CreateResourceShare.html">CreateResourceShare</a>. If you use the PutImageRecipePolicy operation instead, you must also call the RAM API <a href="https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html">PromoteResourceShareCreatedFromPolicy</a>. Otherwise, the resource isn't visible to the principals that it's shared with.</p>

        Args:
            image_recipe_arn: <p>The Amazon Resource Name (ARN) of the image recipe that this policy should be applied to.</p>
            policy: <p>The policy to apply.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value that you provided for the specified parameter is invalid.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Share an image recipe with another account
            The following example applies a resource policy that grants another AWS account permission to view the specified image recipe.

            >>> await client.put_image_recipe_policy(image_recipe_arn='arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.0.0', policy='{"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Principal": {"AWS": "arn:aws:iam::444455556666:root"}, "Action": ["imagebuilder:GetImageRecipe", "imagebuilder:ListImageRecipes"], "Resource": "arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.0.0"}]}')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.put_image_recipe_policy_request.PutImageRecipePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.put_image_recipe_policy_response.PutImageRecipePolicyResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.put_image_recipe_policy

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.put_image_recipe_policy.async_put_image_recipe_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.put_image_recipe_policy_request.PutImageRecipePolicyRequest = {
            "image_recipe_arn": image_recipe_arn,
            "policy": policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def retry_image(
        self,
        image_build_version_arn: "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.retry_image_response.RetryImageResponse":
        """<p>Retries a failed or canceled image build without rebuilding the phases that already completed. The image re-runs asynchronously in place: the same build version returns to the test or distribution phase where it failed and continues from there. No new image build version is created. Retry is only supported for AMI-based images.</p>

        Args:
            image_build_version_arn: <p>The Amazon Resource Name (ARN) of the image build version that you want to retry. The image must be in the <code>FAILED</code> or <code>CANCELLED</code> state.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retry an image build
            The following example retries a cancelled image build, which resumes in place from the phase where it stopped.

            >>> await client.retry_image(image_build_version_arn='arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1', client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLEfffff')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.retry_image_request.RetryImageRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.retry_image_response.RetryImageResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.retry_image

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.retry_image.async_retry_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.retry_image_request.RetryImageRequest = {
            "image_build_version_arn": image_build_version_arn,
            "client_token": client_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_workflow_step_action(
        self,
        step_execution_id: "capo_imagebuilder.types.workflow_step_execution_id.WorkflowStepExecutionId",
        image_build_version_arn: "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        action: "capo_imagebuilder.types.workflow_step_action_type.WorkflowStepActionType",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        reason: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_imagebuilder.types.send_workflow_step_action_response.SendWorkflowStepActionResponse":
        """<p>Sends an action to a workflow step that has paused at a <code>WaitForAction</code> step, so that image creation can continue. To find the steps that are waiting for an action, call <a>ListWaitingWorkflowSteps</a>.</p>

        Args:
            step_execution_id: <p>Uniquely identifies the waiting workflow step that you send the action to. To get this identifier, call <a>ListWaitingWorkflowSteps</a>.</p>
            image_build_version_arn: <p>The Amazon Resource Name (ARN) of the image build version associated with the workflow step execution. This value must match the image that owns the waiting step. If the ARN does not correspond to the image running the workflow, then the request fails with a validation error.</p>
            action: <p>The action to perform on the paused workflow step. <code>RESUME</code> completes the waiting step, and the workflow continues. <code>STOP</code> fails the step, and the step's <code>onFailure</code> setting determines whether the workflow continues or aborts. The workflow step must be in a waiting state to accept an action. The request fails if the step has already timed out or been actioned.</p>
            reason: <p>The reason for the action. This value is stored with the step execution record and is accessible in subsequent workflow steps via step output references.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value that you provided for the specified parameter is invalid.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Stop a workflow step that is waiting for action
            The following example sends the STOP action to a workflow step that has paused the image build, identified by the step execution ID that ListWaitingWorkflowSteps returns.

            >>> await client.send_workflow_step_action(step_execution_id='step-8eb24d7a-036e-46b5-94a3-90a5d8b5ac4a', image_build_version_arn='arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-wait-recipe/1.0.0/1', action='STOP', client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE67890')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.send_workflow_step_action_request.SendWorkflowStepActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.send_workflow_step_action_response.SendWorkflowStepActionResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.send_workflow_step_action

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.send_workflow_step_action.async_send_workflow_step_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.send_workflow_step_action_request.SendWorkflowStepActionRequest = {
            "step_execution_id": step_execution_id,
            "image_build_version_arn": image_build_version_arn,
            "action": action,
            "client_token": client_token,
        }
        if reason is not None:
            input_["reason"] = reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_image_pipeline_execution(
        self,
        image_pipeline_arn: "capo_imagebuilder.types.image_pipeline_arn.ImagePipelineArn",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        tags: Optional["capo_imagebuilder.types.tag_map.TagMap"] = None,
    ) -> "capo_imagebuilder.types.start_image_pipeline_execution_response.StartImagePipelineExecutionResponse":
        """<p>Manually triggers a pipeline to create an image. You can start a build this way whether the pipeline is enabled or disabled. The response returns as soon as Image Builder creates the new image resource and queues the build. Use the returned <code>imageBuildVersionArn</code> with <a>GetImage</a> to track build progress.</p>

        Args:
            image_pipeline_arn: <p>The Amazon Resource Name (ARN) of the image pipeline that you want to manually invoke.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            tags: <p>The tags for Image Builder to apply to the image resource that's created when pipeline execution starts.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Start a pipeline build manually
            The following example starts a build for the specified pipeline. The response returns the ARN of the new image build version.

            >>> await client.start_image_pipeline_execution(image_pipeline_arn='arn:aws:imagebuilder:us-west-2:111122223333:image-pipeline/my-example-pipeline', client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE66666')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.start_image_pipeline_execution_request.StartImagePipelineExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.start_image_pipeline_execution_response.StartImagePipelineExecutionResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.start_image_pipeline_execution

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.start_image_pipeline_execution.async_start_image_pipeline_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.start_image_pipeline_execution_request.StartImagePipelineExecutionRequest = {
            "image_pipeline_arn": image_pipeline_arn,
            "client_token": client_token,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_resource_state_update(
        self,
        resource_arn: "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn",
        state: "capo_imagebuilder.types.resource_state.ResourceState",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        execution_role: Optional[
            "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
        ] = None,
        include_resources: Optional[
            "capo_imagebuilder.types.resource_state_update_include_resources.ResourceStateUpdateIncludeResources"
        ] = None,
        exclusion_rules: Optional[
            "capo_imagebuilder.types.resource_state_update_exclusion_rules.ResourceStateUpdateExclusionRules"
        ] = None,
        update_at: Optional[
            "capo_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
        ] = None,
    ) -> "capo_imagebuilder.types.start_resource_state_update_response.StartResourceStateUpdateResponse":
        """<p>Begins an ad-hoc state change for the specified image build version. This is a one-time operation - if you schedule the update, it runs only once. If the request includes underlying resources, or schedules the update far enough in the future, Image Builder runs the update as an asynchronous lifecycle execution and returns its identifier. Otherwise, for target states other than <code>DELETED</code>, the state change applies immediately. If a request that starts a lifecycle execution arrives while the image already has one in progress, Image Builder rejects it.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the image build version to update. The image must be in one of these terminal states: <code>AVAILABLE</code>, <code>DEPRECATED</code>, <code>DISABLED</code>, <code>FAILED</code>, or <code>CANCELLED</code>. Images with <code>FAILED</code> or <code>CANCELLED</code> status can transition only to <code>DELETED</code>.</p>
            state: <p>Specifies the lifecycle action to take for this request. For AMI-based images, valid values are <code>AVAILABLE</code>, <code>DEPRECATED</code>, <code>DISABLED</code>, and <code>DELETED</code>. For container-based images, only <code>DELETED</code> is supported.</p>
            execution_role: <p>The name or Amazon Resource Name (ARN) of the IAM role that's used to update image state. You must provide this property together with <code>includeResources</code>. Neither is valid without the other.</p>
            include_resources: <p>Specifies which underlying resources to update, in addition to the Image Builder image resource itself. Snapshots and containers are only valid for the <code>DELETED</code> state. To set an image to <code>DELETED</code>, you must include its underlying resources. To delete only the Image Builder image record, use the <a>DeleteImage</a> operation instead.</p>
            exclusion_rules: <p>Rules that Image Builder evaluates against each of the image's AMIs. Matching AMIs and their snapshots are skipped. Exclusion rules only take effect when the request includes AMIs. If the target state is <code>DELETED</code> and any resource was skipped, the Image Builder image resource itself is also retained. For the <code>DEPRECATED</code> and <code>DISABLED</code> target states, Image Builder updates the image resource's state regardless of exclusions.</p>
            update_at: <p>The timestamp that indicates when resources are updated by a lifecycle action. This property is valid only when the target status is <code>DEPRECATED</code>, and the value must be a future time. If you don't specify a value, Image Builder begins the state update right away. For a scheduled deprecation, included AMIs get their EC2 deprecation time set immediately, and Image Builder schedules the image resource to transition to <code>DEPRECATED</code> at that time.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Schedule an image build version for deprecation
            The following example schedules the specified image build version and its AMI to move to the DEPRECATED state at the requested future time. It returns the ID of the lifecycle execution that applies the update.

            >>> await client.start_resource_state_update(resource_arn='arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1', state={'status': 'DEPRECATED'}, execution_role='arn:aws:iam::111122223333:role/my-example-state-update-role', include_resources={'amis': True}, update_at='2026-09-11T21:20:00Z', client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLE24680')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.start_resource_state_update_request.StartResourceStateUpdateRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.start_resource_state_update_response.StartResourceStateUpdateResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.start_resource_state_update

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.start_resource_state_update.async_start_resource_state_update(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.start_resource_state_update_request.StartResourceStateUpdateRequest = {
            "resource_arn": resource_arn,
            "state": state,
            "client_token": client_token,
        }
        if execution_role is not None:
            input_["execution_role"] = execution_role
        if include_resources is not None:
            input_["include_resources"] = include_resources
        if exclusion_rules is not None:
            input_["exclusion_rules"] = exclusion_rules
        if update_at is not None:
            input_["update_at"] = update_at

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_imagebuilder.types.image_builder_arn.ImageBuilderArn",
        tags: "capo_imagebuilder.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.tag_resource_response.TagResourceResponse":
        """<p>Adds a tag to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>
            tags: <p>The tags to apply to the resource.</p>

        Raises:
            capo_imagebuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Add tags to a component build version
            The following example adds two tags to a component build version.

            >>> await client.tag_resource(resource_arn='arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-tagged-component/1.0.0/1', tags={'Environment': 'Production', 'CostCenter': '12345'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.tag_resource

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_imagebuilder.types.image_builder_arn.ImageBuilderArn",
        tag_keys: "capo_imagebuilder.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
    ) -> "capo_imagebuilder.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to untag.</p>
            tag_keys: <p>The tag keys to remove from the resource.</p>

        Raises:
            capo_imagebuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>At least one of the resources referenced by your request does not exist.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Remove a tag from a resource
            The following example removes the CostCenter tag key from the specified component build version.

            >>> await client.untag_resource(resource_arn='arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-tagged-component/1.0.0/1', tag_keys=['CostCenter'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.untag_resource

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_distribution_configuration(
        self,
        distribution_configuration_arn: "capo_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn",
        distributions: "capo_imagebuilder.types.distribution_list.DistributionList",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        description: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_imagebuilder.types.update_distribution_configuration_response.UpdateDistributionConfigurationResponse":
        """<p>Updates a distribution configuration. Distribution configurations define and configure the outputs for your images, including the target Regions, accounts, and settings for each Region.</p> <note> <p>This operation doesn't support selective updates. The request replaces the stored configuration, so include every setting that you want to keep.</p> </note>

        Args:
            distribution_configuration_arn: <p>The Amazon Resource Name (ARN) of the distribution configuration that you want to update.</p>
            description: <p>The description of the distribution configuration.</p>
            distributions: <p>The distribution settings for the configuration. Each entry defines how output images are distributed in one target Amazon Web Services Region. A Region can appear at most once in the list. This list replaces the configuration's existing distributions entirely.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>You have specified a combination of parameters that isn't valid. For example, two mutually exclusive parameters, or a parameter without its required companion parameter. Review the error message for details.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a distribution configuration
            The following example replaces the distribution settings for the specified configuration with a single distribution that names the output AMI with the build date.

            >>> await client.update_distribution_configuration(distribution_configuration_arn='arn:aws:imagebuilder:us-west-2:111122223333:distribution-configuration/my-example-distribution', distributions=[{'region': 'us-west-2', 'amiDistributionConfiguration': {'name': 'my-example-image-{{ imagebuilder:buildDate }}'}}], client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLEccccc')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.update_distribution_configuration_request.UpdateDistributionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.update_distribution_configuration_response.UpdateDistributionConfigurationResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.update_distribution_configuration

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.update_distribution_configuration.async_update_distribution_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.update_distribution_configuration_request.UpdateDistributionConfigurationRequest = {
            "distribution_configuration_arn": distribution_configuration_arn,
            "distributions": distributions,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_image_pipeline(
        self,
        image_pipeline_arn: "capo_imagebuilder.types.image_pipeline_arn.ImagePipelineArn",
        infrastructure_configuration_arn: "capo_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        description: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        image_recipe_arn: Optional[
            "capo_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
        ] = None,
        container_recipe_arn: Optional[
            "capo_imagebuilder.types.container_recipe_arn.ContainerRecipeArn"
        ] = None,
        distribution_configuration_arn: Optional[
            "capo_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn"
        ] = None,
        image_tests_configuration: Optional[
            "capo_imagebuilder.types.image_tests_configuration.ImageTestsConfiguration"
        ] = None,
        enhanced_image_metadata_enabled: Optional[
            "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
        ] = None,
        schedule: Optional["capo_imagebuilder.types.schedule.Schedule"] = None,
        status: Optional[
            "capo_imagebuilder.types.pipeline_status.PipelineStatus"
        ] = None,
        image_scanning_configuration: Optional[
            "capo_imagebuilder.types.image_scanning_configuration.ImageScanningConfiguration"
        ] = None,
        workflows: Optional[
            "capo_imagebuilder.types.workflow_configuration_list.WorkflowConfigurationList"
        ] = None,
        logging_configuration: Optional[
            "capo_imagebuilder.types.pipeline_logging_configuration.PipelineLoggingConfiguration"
        ] = None,
        execution_role: Optional[
            "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
        ] = None,
        image_tags: Optional["capo_imagebuilder.types.tag_map.TagMap"] = None,
    ) -> "capo_imagebuilder.types.update_image_pipeline_response.UpdateImagePipelineResponse":
        """<p>Updates an image pipeline. Use image pipelines to automate the creation and distribution of images. You must specify exactly one recipe for your image, using either a <code>containerRecipeArn</code> or an <code>imageRecipeArn</code>. The recipe must be the same type, image or container, as the pipeline's current recipe.</p> <note> <p>UpdateImagePipeline does not support selective updates. The request replaces the pipeline's entire configuration, so include every setting that you want to keep. Any optional property that you omit is removed or reset to its default.</p> </note>

        Args:
            image_pipeline_arn: <p>The Amazon Resource Name (ARN) of the image pipeline that you want to update.</p>
            description: <p>The description of the image pipeline.</p>
            image_recipe_arn: <p>The Amazon Resource Name (ARN) of the image recipe that configures images created by this image pipeline. You must specify either this property or <code>containerRecipeArn</code>, but not both.</p>
            container_recipe_arn: <p>The Amazon Resource Name (ARN) of the container recipe that is used to configure images created by this container pipeline. You must specify either this property or <code>imageRecipeArn</code>, but not both.</p>
            infrastructure_configuration_arn: <p>The Amazon Resource Name (ARN) of the infrastructure configuration that Image Builder uses to build images created by this image pipeline.</p>
            distribution_configuration_arn: <p>The Amazon Resource Name (ARN) of the distribution configuration that Image Builder uses to configure and distribute images created by this image pipeline.</p>
            image_tests_configuration: <p>Specifies the test settings that Image Builder applies to images that this pipeline creates. If you don't provide test settings, Image Builder stores a default configuration with image tests enabled.</p>
            enhanced_image_metadata_enabled: <p>Specifies whether to collect additional information about the image being created, including the operating system (OS) version and package list. Defaults to <code>true</code>.</p>
            schedule: <p>The schedule of the image pipeline. Because the update replaces the entire configuration, omitting this property removes any existing schedule. The pipeline then runs only when you call <a>StartImagePipelineExecution</a>.</p>
            status: <p>The status of the image pipeline. Defaults to <code>ENABLED</code> when omitted. To keep a pipeline disabled, include this property set to <code>DISABLED</code> in your update request.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>
            image_scanning_configuration: <p>Contains settings for vulnerability scans that Amazon Inspector runs against the test instance during image creation.</p>
            workflows: <p>The array of workflow configuration objects for builds that this pipeline starts. You must also specify <code>executionRole</code> when you provide workflows.</p>
            logging_configuration: <p>Specifies the logging configuration for the image pipeline. Use this to define custom CloudWatch Logs log groups for your pipeline execution logs and image build logs. The service manages log groups with names starting with <code>/aws/imagebuilder/</code> using the service-linked role. For custom log group names outside of this prefix, you must also provide an <code>executionRole</code>.</p>
            execution_role: <p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions. If you omit this property, the pipeline reverts to the Image Builder service-linked role.</p>
            image_tags: <p>The tags that Image Builder applies to the Image Builder image resource that this pipeline's scheduled executions create. These tags don't apply to the output AMI. To tag output AMIs, use <code>amiTags</code> in the pipeline's distribution configuration.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update an image pipeline
            The following example changes the pipeline's schedule to build every day at 6:00 AM UTC.

            >>> await client.update_image_pipeline(image_pipeline_arn='arn:aws:imagebuilder:us-west-2:111122223333:image-pipeline/my-example-pipeline', image_recipe_arn='arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.0.0', infrastructure_configuration_arn='arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure', schedule={'scheduleExpression': 'cron(0 6 * * ? *)', 'pipelineExecutionStartCondition': 'EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE'}, status='ENABLED', client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLEddddd')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.update_image_pipeline_request.UpdateImagePipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.update_image_pipeline_response.UpdateImagePipelineResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.update_image_pipeline

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.update_image_pipeline.async_update_image_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.update_image_pipeline_request.UpdateImagePipelineRequest = {
            "image_pipeline_arn": image_pipeline_arn,
            "infrastructure_configuration_arn": infrastructure_configuration_arn,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
        if image_recipe_arn is not None:
            input_["image_recipe_arn"] = image_recipe_arn
        if container_recipe_arn is not None:
            input_["container_recipe_arn"] = container_recipe_arn
        if distribution_configuration_arn is not None:
            input_["distribution_configuration_arn"] = distribution_configuration_arn
        if image_tests_configuration is not None:
            input_["image_tests_configuration"] = image_tests_configuration
        if enhanced_image_metadata_enabled is not None:
            input_["enhanced_image_metadata_enabled"] = enhanced_image_metadata_enabled
        if schedule is not None:
            input_["schedule"] = schedule
        if status is not None:
            input_["status"] = status
        if image_scanning_configuration is not None:
            input_["image_scanning_configuration"] = image_scanning_configuration
        if workflows is not None:
            input_["workflows"] = workflows
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if execution_role is not None:
            input_["execution_role"] = execution_role
        if image_tags is not None:
            input_["image_tags"] = image_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_infrastructure_configuration(
        self,
        infrastructure_configuration_arn: "capo_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn",
        instance_profile_name: "capo_imagebuilder.types.instance_profile_name_type.InstanceProfileNameType",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        description: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        instance_types: Optional[
            "capo_imagebuilder.types.instance_type_list.InstanceTypeList"
        ] = None,
        security_group_ids: Optional[
            "capo_imagebuilder.types.security_group_ids.SecurityGroupIds"
        ] = None,
        subnet_id: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        logging: Optional["capo_imagebuilder.types.logging.Logging"] = None,
        key_pair: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        terminate_instance_on_failure: Optional[
            "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
        ] = None,
        sns_topic_arn: Optional[
            "capo_imagebuilder.types.sns_topic_arn.SnsTopicArn"
        ] = None,
        resource_tags: Optional[
            "capo_imagebuilder.types.resource_tag_map.ResourceTagMap"
        ] = None,
        instance_metadata_options: Optional[
            "capo_imagebuilder.types.instance_metadata_options.InstanceMetadataOptions"
        ] = None,
        placement: Optional["capo_imagebuilder.types.placement.Placement"] = None,
    ) -> "capo_imagebuilder.types.update_infrastructure_configuration_response.UpdateInfrastructureConfigurationResponse":
        """<p>Updates an infrastructure configuration. An infrastructure configuration defines the environment in which Image Builder builds and tests your image.</p> <note> <p>This operation doesn't support selective updates. The request replaces the configuration, so include every setting that you want to keep. Omitted optional properties are cleared.</p> </note>

        Args:
            infrastructure_configuration_arn: <p>The Amazon Resource Name (ARN) of the infrastructure configuration that you want to update.</p>
            description: <p>The description of the infrastructure configuration.</p>
            instance_types: <p>The instance types of the infrastructure configuration. You can specify one or more instance types to use for this build. Image Builder picks one of these instance types based on availability. If you don't specify instance types, Image Builder selects compatible instance types automatically. If you specify a Dedicated Host, Image Builder uses only instance types that the host supports.</p>
            instance_profile_name: <p>The instance profile to associate with the instance used to customize your Amazon EC2 AMI. The instance profile must exist in your account.</p>
            security_group_ids: <p>The security group IDs to associate with the instance used to customize your Amazon EC2 AMI.</p>
            subnet_id: <p>The subnet ID in which to place the instance used to customize your Amazon EC2 AMI. If you specify <code>subnetId</code>, you must also specify one or more security group IDs in <code>securityGroupIds</code>. Otherwise, the request fails.</p>
            logging: <p>The logging configuration of the infrastructure configuration. When you configure S3 logs, Image Builder writes logs from the build and test process to the specified bucket under the key prefix.</p>
            key_pair: <p>The key pair of the infrastructure configuration. You can use this to log on to and debug the instance used to create your image.</p>
            terminate_instance_on_failure: <p>Specifies whether to terminate the instance on failure. Set to false if you want Image Builder to retain the instance used to configure your AMI if the build or test phase of your workflow fails. Defaults to <code>true</code>.</p>
            sns_topic_arn: <p>The Amazon Resource Name (ARN) of the SNS topic to which Image Builder sends image build event notifications. Specify a standard topic. Image Builder doesn't support FIFO topics. Image Builder validates the topic when you create or update the configuration. You must have permission to publish to the topic.</p> <note> <p>EC2 Image Builder can't send notifications to SNS topics that are encrypted using keys from other accounts. If your SNS topic is encrypted, the key must be owned by the same account that owns your Image Builder resources.</p> </note>
            resource_tags: <p>The metadata tags to assign to the Amazon EC2 instance that Image Builder launches during the build process. Tags are formatted as key value pairs. Tag keys can't begin with <code>aws:</code> or match one of the following reserved keys: <code>CreatedBy</code>, <code>Ec2ImageBuilderArn</code>, <code>Name</code>, or <code>Tags</code>.</p>
            instance_metadata_options: <p>The instance metadata service (IMDS) settings that Image Builder applies to the EC2 build and test instances it launches during image creation. If you don't set these options, the EC2 launch defaults for the instance apply. For more information about instance metadata options, see one of the following links:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html">Configure the instance metadata options</a> in the <i> <i>Amazon EC2 User Guide</i> </i> for Linux instances.</p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/configuring-instance-metadata-options.html">Configure the instance metadata options</a> in the <i> <i>Amazon EC2 Windows Guide</i> </i> for Windows instances.</p> </li> </ul>
            placement: <p>The instance placement settings that define where the build and test instances that Image Builder launches during image creation run. These settings don't affect instances that you launch from the output image.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update an infrastructure configuration
            The following example updates an infrastructure configuration to use larger instance types and to keep the build instance running when the image build fails.

            >>> await client.update_infrastructure_configuration(infrastructure_configuration_arn='arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure', description='An infrastructure configuration for Amazon Linux builds', instance_profile_name='EC2InstanceProfileForImageBuilder', instance_types=['t3.large', 't3.xlarge'], terminate_instance_on_failure=False, client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.update_infrastructure_configuration_request.UpdateInfrastructureConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.update_infrastructure_configuration_response.UpdateInfrastructureConfigurationResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.update_infrastructure_configuration

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.update_infrastructure_configuration.async_update_infrastructure_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.update_infrastructure_configuration_request.UpdateInfrastructureConfigurationRequest = {
            "infrastructure_configuration_arn": infrastructure_configuration_arn,
            "instance_profile_name": instance_profile_name,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
        if instance_types is not None:
            input_["instance_types"] = instance_types
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if subnet_id is not None:
            input_["subnet_id"] = subnet_id
        if logging is not None:
            input_["logging"] = logging
        if key_pair is not None:
            input_["key_pair"] = key_pair
        if terminate_instance_on_failure is not None:
            input_["terminate_instance_on_failure"] = terminate_instance_on_failure
        if sns_topic_arn is not None:
            input_["sns_topic_arn"] = sns_topic_arn
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
        if instance_metadata_options is not None:
            input_["instance_metadata_options"] = instance_metadata_options
        if placement is not None:
            input_["placement"] = placement

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_lifecycle_policy(
        self,
        lifecycle_policy_arn: "capo_imagebuilder.types.lifecycle_policy_arn.LifecyclePolicyArn",
        execution_role: "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn",
        resource_type: "capo_imagebuilder.types.lifecycle_policy_resource_type.LifecyclePolicyResourceType",
        policy_details: "capo_imagebuilder.types.lifecycle_policy_details.LifecyclePolicyDetails",
        resource_selection: "capo_imagebuilder.types.lifecycle_policy_resource_selection.LifecyclePolicyResourceSelection",
        client_token: "capo_imagebuilder.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncimagebuilderClientConfig] = None,
        description: Optional[
            "capo_imagebuilder.types.non_empty_string.NonEmptyString"
        ] = None,
        status: Optional[
            "capo_imagebuilder.types.lifecycle_policy_status.LifecyclePolicyStatus"
        ] = None,
    ) -> "capo_imagebuilder.types.update_lifecycle_policy_response.UpdateLifecyclePolicyResponse":
        """<p>Updates the specified lifecycle policy. The request replaces the existing policy configuration rather than merging changes, so re-specify every setting that you want to keep. The <code>resourceType</code> must match the existing policy's value.</p>

        Args:
            lifecycle_policy_arn: <p>The Amazon Resource Name (ARN) of the lifecycle policy resource.</p>
            description: <p>Optional description for the lifecycle policy. Because the update replaces the entire configuration, omitting this property removes any existing description.</p>
            status: <p>Indicates whether the lifecycle policy resource is enabled. Defaults to <code>ENABLED</code> when omitted, so updating a disabled policy without setting this property re-enables it.</p>
            execution_role: <p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to run lifecycle actions.</p>
            resource_type: <p>The type of image resource that the lifecycle policy applies to. The value must match the policy's existing resource type. You can't change the resource type of an existing lifecycle policy.</p>
            policy_details: <p>The configuration details for a lifecycle policy resource.</p>
            resource_selection: <p>Selection criteria for resources that the lifecycle policy applies to. You must specify exactly one selection criteria: either recipes or a tag map, not both.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>

        Raises:
            capo_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException: <p>You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.</p>
            capo_imagebuilder.errors.client_exception.ClientException: <p>A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.</p>
            capo_imagebuilder.errors.forbidden_exception.ForbiddenException: <p>You are not authorized to perform the requested operation.</p>
            capo_imagebuilder.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.</p>
            capo_imagebuilder.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>You have specified a combination of parameters that isn't valid. For example, two mutually exclusive parameters, or a parameter without its required companion parameter. Review the error message for details.</p>
            capo_imagebuilder.errors.invalid_request_exception.InvalidRequestException: <p>The request is malformed or otherwise invalid. Verify the request and try again.</p>
            capo_imagebuilder.errors.resource_in_use_exception.ResourceInUseException: <p>The resource that you are trying to operate on is currently in use. Review the message details and retry later.</p>
            capo_imagebuilder.errors.service_exception.ServiceException: <p>An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.</p>
            capo_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unable to process your request at this time.</p>
            capo_imagebuilder.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a lifecycle policy
            The following example updates a lifecycle policy to delete AMI images and their associated snapshots after 12 months, retaining the 3 most recent images.

            >>> await client.update_lifecycle_policy(lifecycle_policy_arn='arn:aws:imagebuilder:us-west-2:111122223333:lifecycle-policy/my-example-policy', description='Deletes AMI images and their snapshots after 12 months, retaining the 3 most recent', status='ENABLED', execution_role='arn:aws:iam::111122223333:role/my-example-lifecycle-role', resource_type='AMI_IMAGE', policy_details=[{'action': {'type': 'DELETE', 'includeResources': {'amis': True, 'snapshots': True}}, 'filter': {'type': 'AGE', 'value': 12, 'unit': 'MONTHS', 'retainAtLeast': 3}}], resource_selection={'tagMap': {'environment': 'production'}}, client_token='a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_imagebuilder.types.update_lifecycle_policy_request.UpdateLifecyclePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_imagebuilder.types.update_lifecycle_policy_response.UpdateLifecyclePolicyResponse"
        ]:
            import capo_imagebuilder._operations.imagebuilder.update_lifecycle_policy

            (
                output,
                http_response,
            ) = await capo_imagebuilder._operations.imagebuilder.update_lifecycle_policy.async_update_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_imagebuilder.types.update_lifecycle_policy_request.UpdateLifecyclePolicyRequest = {
            "lifecycle_policy_arn": lifecycle_policy_arn,
            "execution_role": execution_role,
            "resource_type": resource_type,
            "policy_details": policy_details,
            "resource_selection": resource_selection,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status

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
