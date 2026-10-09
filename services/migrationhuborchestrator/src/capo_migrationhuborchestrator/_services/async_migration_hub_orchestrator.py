"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#AWSMigrationHubOrchestrator``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_migrationhuborchestrator._auth._signers
import capo_migrationhuborchestrator._auth._sigv4
from capo_migrationhuborchestrator._auth._identity import Credentials
from capo_migrationhuborchestrator._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_migrationhuborchestrator._auth._zapros_handler import AuthMiddleware
from capo_migrationhuborchestrator._pagination import resolve_path as _resolve_path
from capo_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.migration_workflow import (
    AsyncMigrationWorkflow,
)
from capo_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.migration_workflow_template import (
    AsyncMigrationWorkflowTemplate,
)
from capo_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.plugin import (
    AsyncPlugin,
)
from capo_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.template_step import (
    AsyncTemplateStep,
)
from capo_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.template_step_group import (
    AsyncTemplateStepGroup,
)
from capo_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.template_step_groups import (
    AsyncTemplateStepGroups,
)
from capo_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.workflow_step import (
    AsyncWorkflowStep,
)
from capo_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.workflow_step_group import (
    AsyncWorkflowStepGroup,
)
from capo_migrationhuborchestrator._services._aws_config import aaws_config
from capo_migrationhuborchestrator._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.application_configuration_name
    import capo_migrationhuborchestrator.types.client_token
    import capo_migrationhuborchestrator.types.create_migration_workflow_request
    import capo_migrationhuborchestrator.types.create_migration_workflow_response
    import capo_migrationhuborchestrator.types.create_template_request
    import capo_migrationhuborchestrator.types.create_template_response
    import capo_migrationhuborchestrator.types.create_workflow_step_group_request
    import capo_migrationhuborchestrator.types.create_workflow_step_group_response
    import capo_migrationhuborchestrator.types.create_workflow_step_request
    import capo_migrationhuborchestrator.types.create_workflow_step_response
    import capo_migrationhuborchestrator.types.delete_migration_workflow_request
    import capo_migrationhuborchestrator.types.delete_migration_workflow_response
    import capo_migrationhuborchestrator.types.delete_template_request
    import capo_migrationhuborchestrator.types.delete_template_response
    import capo_migrationhuborchestrator.types.delete_workflow_step_group_request
    import capo_migrationhuborchestrator.types.delete_workflow_step_group_response
    import capo_migrationhuborchestrator.types.delete_workflow_step_request
    import capo_migrationhuborchestrator.types.delete_workflow_step_response
    import capo_migrationhuborchestrator.types.get_migration_workflow_request
    import capo_migrationhuborchestrator.types.get_migration_workflow_response
    import capo_migrationhuborchestrator.types.get_migration_workflow_template_request
    import capo_migrationhuborchestrator.types.get_migration_workflow_template_response
    import capo_migrationhuborchestrator.types.get_template_step_group_request
    import capo_migrationhuborchestrator.types.get_template_step_group_response
    import capo_migrationhuborchestrator.types.get_template_step_request
    import capo_migrationhuborchestrator.types.get_template_step_response
    import capo_migrationhuborchestrator.types.get_workflow_step_group_request
    import capo_migrationhuborchestrator.types.get_workflow_step_group_response
    import capo_migrationhuborchestrator.types.get_workflow_step_request
    import capo_migrationhuborchestrator.types.get_workflow_step_response
    import capo_migrationhuborchestrator.types.list_migration_workflow_templates_request
    import capo_migrationhuborchestrator.types.list_migration_workflow_templates_response
    import capo_migrationhuborchestrator.types.list_migration_workflows_request
    import capo_migrationhuborchestrator.types.list_migration_workflows_response
    import capo_migrationhuborchestrator.types.list_plugins_request
    import capo_migrationhuborchestrator.types.list_plugins_response
    import capo_migrationhuborchestrator.types.list_tags_for_resource_request
    import capo_migrationhuborchestrator.types.list_tags_for_resource_response
    import capo_migrationhuborchestrator.types.list_template_step_groups_request
    import capo_migrationhuborchestrator.types.list_template_step_groups_response
    import capo_migrationhuborchestrator.types.list_template_steps_request
    import capo_migrationhuborchestrator.types.list_template_steps_response
    import capo_migrationhuborchestrator.types.list_workflow_step_groups_request
    import capo_migrationhuborchestrator.types.list_workflow_step_groups_response
    import capo_migrationhuborchestrator.types.list_workflow_steps_request
    import capo_migrationhuborchestrator.types.list_workflow_steps_response
    import capo_migrationhuborchestrator.types.max_results
    import capo_migrationhuborchestrator.types.migration_workflow_description
    import capo_migrationhuborchestrator.types.migration_workflow_id
    import capo_migrationhuborchestrator.types.migration_workflow_name
    import capo_migrationhuborchestrator.types.migration_workflow_status_enum
    import capo_migrationhuborchestrator.types.migration_workflow_summary
    import capo_migrationhuborchestrator.types.next_token
    import capo_migrationhuborchestrator.types.plugin_summary
    import capo_migrationhuborchestrator.types.resource_arn
    import capo_migrationhuborchestrator.types.retry_workflow_step_request
    import capo_migrationhuborchestrator.types.retry_workflow_step_response
    import capo_migrationhuborchestrator.types.start_migration_workflow_request
    import capo_migrationhuborchestrator.types.start_migration_workflow_response
    import capo_migrationhuborchestrator.types.step_action_type
    import capo_migrationhuborchestrator.types.step_description
    import capo_migrationhuborchestrator.types.step_group_description
    import capo_migrationhuborchestrator.types.step_group_id
    import capo_migrationhuborchestrator.types.step_group_name
    import capo_migrationhuborchestrator.types.step_id
    import capo_migrationhuborchestrator.types.step_input_parameters
    import capo_migrationhuborchestrator.types.step_name
    import capo_migrationhuborchestrator.types.step_status
    import capo_migrationhuborchestrator.types.stop_migration_workflow_request
    import capo_migrationhuborchestrator.types.stop_migration_workflow_response
    import capo_migrationhuborchestrator.types.string_list
    import capo_migrationhuborchestrator.types.string_map
    import capo_migrationhuborchestrator.types.tag_key_list
    import capo_migrationhuborchestrator.types.tag_map
    import capo_migrationhuborchestrator.types.tag_resource_request
    import capo_migrationhuborchestrator.types.tag_resource_response
    import capo_migrationhuborchestrator.types.template_id
    import capo_migrationhuborchestrator.types.template_name
    import capo_migrationhuborchestrator.types.template_source
    import capo_migrationhuborchestrator.types.template_step_group_summary
    import capo_migrationhuborchestrator.types.template_step_summary
    import capo_migrationhuborchestrator.types.template_summary
    import capo_migrationhuborchestrator.types.untag_resource_request
    import capo_migrationhuborchestrator.types.untag_resource_response
    import capo_migrationhuborchestrator.types.update_migration_workflow_request
    import capo_migrationhuborchestrator.types.update_migration_workflow_response
    import capo_migrationhuborchestrator.types.update_template_request
    import capo_migrationhuborchestrator.types.update_template_response
    import capo_migrationhuborchestrator.types.update_workflow_step_group_request
    import capo_migrationhuborchestrator.types.update_workflow_step_group_response
    import capo_migrationhuborchestrator.types.update_workflow_step_request
    import capo_migrationhuborchestrator.types.update_workflow_step_response
    import capo_migrationhuborchestrator.types.workflow_step_automation_configuration
    import capo_migrationhuborchestrator.types.workflow_step_group_summary
    import capo_migrationhuborchestrator.types.workflow_step_output_list
    import capo_migrationhuborchestrator.types.workflow_step_summary


class AsyncMigrationHubOrchestratorClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncMigrationHubOrchestratorClient:
    """A client for the ``MigrationHubOrchestrator`` service.

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
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
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
        anonymous: bool | None = None,
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
        self._config = AsyncMigrationHubOrchestratorClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.migration_workflow = AsyncMigrationWorkflow(self)
        self.migration_workflow_template = AsyncMigrationWorkflowTemplate(self)
        self.plugin = AsyncPlugin(self)
        self.template_step = AsyncTemplateStep(self)
        self.template_step_group = AsyncTemplateStepGroup(self)
        self.template_step_groups = AsyncTemplateStepGroups(self)
        self.workflow_step = AsyncWorkflowStep(self)
        self.workflow_step_group = AsyncWorkflowStepGroup(self)

    def operation_options(
        self,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMigrationHubOrchestratorClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_migrationhuborchestrator.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "capo_migrationhuborchestrator.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List the tags added to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_migrationhuborchestrator.types.resource_arn.ResourceArn",
        tags: "capo_migrationhuborchestrator.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> (
        "capo_migrationhuborchestrator.types.tag_resource_response.TagResourceResponse"
    ):
        """<p>Tag a resource by specifying its Amazon Resource Name (ARN).</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which you want to add tags.</p>
            tags: <p>A collection of labels, in the form of key:value pairs, that apply to this resource.</p>

        Raises:
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.tag_resource

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_migrationhuborchestrator.types.resource_arn.ResourceArn",
        tag_keys: "capo_migrationhuborchestrator.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "capo_migrationhuborchestrator.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes the tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which you want to remove tags.</p>
            tag_keys: <p>One or more tag keys. Specify only the tag keys, not the tag values.</p>

        Raises:
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.untag_resource

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_workflow(
        self,
        name: str,
        template_id: str,
        input_parameters: "capo_migrationhuborchestrator.types.step_input_parameters.StepInputParameters",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        description: Optional[str] = None,
        application_configuration_id: Optional[str] = None,
        step_targets: Optional[
            "capo_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        tags: Optional[
            "capo_migrationhuborchestrator.types.string_map.StringMap"
        ] = None,
    ) -> "capo_migrationhuborchestrator.types.create_migration_workflow_response.CreateMigrationWorkflowResponse":
        """<p>Create a workflow to orchestrate your migrations.</p>

        Args:
            name: <p>The name of the migration workflow.</p>
            description: <p>The description of the migration workflow.</p>
            template_id: <p>The ID of the template.</p>
            application_configuration_id: <p>The configuration ID of the application configured in Application Discovery Service.</p>
            input_parameters: <p>The input parameters required to create a migration workflow.</p>
            step_targets: <p>The servers on which a step will be run.</p>
            tags: <p>The tags to add on a migration workflow.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.create_migration_workflow_request.CreateMigrationWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.create_migration_workflow_response.CreateMigrationWorkflowResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow.async_create_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.create_migration_workflow_request.CreateMigrationWorkflowRequest = {
            "name": name,
            "template_id": template_id,
            "input_parameters": input_parameters,
        }
        if description is not None:
            input_["description"] = description
        if application_configuration_id is not None:
            input_["application_configuration_id"] = application_configuration_id
        if step_targets is not None:
            input_["step_targets"] = step_targets
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_workflow(
        self,
        id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "capo_migrationhuborchestrator.types.get_migration_workflow_response.GetMigrationWorkflowResponse":
        """<p>Get migration workflow.</p>

        Args:
            id: <p>The ID of the migration workflow.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.get_migration_workflow_request.GetMigrationWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.get_migration_workflow_response.GetMigrationWorkflowResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow.async_get_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.get_migration_workflow_request.GetMigrationWorkflowRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_workflow(
        self,
        id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        input_parameters: Optional[
            "capo_migrationhuborchestrator.types.step_input_parameters.StepInputParameters"
        ] = None,
        step_targets: Optional[
            "capo_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
    ) -> "capo_migrationhuborchestrator.types.update_migration_workflow_response.UpdateMigrationWorkflowResponse":
        """<p>Update a migration workflow.</p>

        Args:
            id: <p>The ID of the migration workflow.</p>
            name: <p>The name of the migration workflow.</p>
            description: <p>The description of the migration workflow.</p>
            input_parameters: <p>The input parameters required to update a migration workflow.</p>
            step_targets: <p>The servers on which a step will be run.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.update_migration_workflow_request.UpdateMigrationWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.update_migration_workflow_response.UpdateMigrationWorkflowResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow.async_update_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.update_migration_workflow_request.UpdateMigrationWorkflowRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if input_parameters is not None:
            input_["input_parameters"] = input_parameters
        if step_targets is not None:
            input_["step_targets"] = step_targets

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_workflow(
        self,
        id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "capo_migrationhuborchestrator.types.delete_migration_workflow_response.DeleteMigrationWorkflowResponse":
        """<p>Delete a migration workflow. You must pause a running workflow in Migration Hub Orchestrator console to delete it.</p>

        Args:
            id: <p>The ID of the migration workflow you want to delete.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.delete_migration_workflow_request.DeleteMigrationWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.delete_migration_workflow_response.DeleteMigrationWorkflowResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow.async_delete_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.delete_migration_workflow_request.DeleteMigrationWorkflowRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_workflows(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        max_results: Optional[
            "capo_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
        template_id: Optional[
            "capo_migrationhuborchestrator.types.template_id.TemplateId"
        ] = None,
        ads_application_configuration_name: Optional[
            "capo_migrationhuborchestrator.types.application_configuration_name.ApplicationConfigurationName"
        ] = None,
        status: Optional[
            "capo_migrationhuborchestrator.types.migration_workflow_status_enum.MigrationWorkflowStatusEnum"
        ] = None,
        name: Optional[str] = None,
    ) -> "capo_migrationhuborchestrator.types.list_migration_workflows_response.ListMigrationWorkflowsResponse":
        """<p>List the migration workflows.</p>

        Args:
            max_results: <p>The maximum number of results that can be returned.</p>
            next_token: <p>The pagination token.</p>
            template_id: <p>The ID of the template.</p>
            ads_application_configuration_name: <p>The name of the application configured in Application Discovery Service.</p>
            status: <p>The status of the migration workflow.</p>
            name: <p>The name of the migration workflow.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.list_migration_workflows_request.ListMigrationWorkflowsRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.list_migration_workflows_response.ListMigrationWorkflowsResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflows

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflows.async_list_workflows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.list_migration_workflows_request.ListMigrationWorkflowsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if template_id is not None:
            input_["template_id"] = template_id
        if ads_application_configuration_name is not None:
            input_["ads_application_configuration_name"] = (
                ads_application_configuration_name
            )
        if status is not None:
            input_["status"] = status
        if name is not None:
            input_["name"] = name

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
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        max_results: Optional[
            "capo_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
        template_id: Optional[
            "capo_migrationhuborchestrator.types.template_id.TemplateId"
        ] = None,
        ads_application_configuration_name: Optional[
            "capo_migrationhuborchestrator.types.application_configuration_name.ApplicationConfigurationName"
        ] = None,
        status: Optional[
            "capo_migrationhuborchestrator.types.migration_workflow_status_enum.MigrationWorkflowStatusEnum"
        ] = None,
        name: Optional[str] = None,
    ) -> "AsyncIterator[capo_migrationhuborchestrator.types.migration_workflow_summary.MigrationWorkflowSummary]":
        _token = next_token
        while True:
            _response = await self.list_workflows(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                template_id=template_id,
                ads_application_configuration_name=ads_application_configuration_name,
                status=status,
                name=name,
            )
            _page = _resolve_path(_response, ("migration_workflow_summary",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_workflow(
        self,
        id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "capo_migrationhuborchestrator.types.start_migration_workflow_response.StartMigrationWorkflowResponse":
        """<p>Start a migration workflow.</p>

        Args:
            id: <p>The ID of the migration workflow.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.start_migration_workflow_request.StartMigrationWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.start_migration_workflow_response.StartMigrationWorkflowResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.start_workflow

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.start_workflow.async_start_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.start_migration_workflow_request.StartMigrationWorkflowRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_workflow(
        self,
        id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "capo_migrationhuborchestrator.types.stop_migration_workflow_response.StopMigrationWorkflowResponse":
        """<p>Stop an ongoing migration workflow.</p>

        Args:
            id: <p>The ID of the migration workflow.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.stop_migration_workflow_request.StopMigrationWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.stop_migration_workflow_response.StopMigrationWorkflowResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.stop_workflow

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.stop_workflow.async_stop_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.stop_migration_workflow_request.StopMigrationWorkflowRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_template(
        self,
        template_name: str,
        template_source: "capo_migrationhuborchestrator.types.template_source.TemplateSource",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        template_description: Optional[str] = None,
        client_token: Optional[
            "capo_migrationhuborchestrator.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_migrationhuborchestrator.types.tag_map.TagMap"] = None,
    ) -> "capo_migrationhuborchestrator.types.create_template_response.CreateTemplateResponse":
        """<p>Creates a migration workflow template.</p>

        Args:
            template_name: <p>The name of the migration workflow template.</p>
            template_description: <p>A description of the migration workflow template.</p>
            template_source: <p>The source of the migration workflow template.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://smithy.io/2.0/spec/behavior-traits.html#idempotencytoken-trait">Idempotency</a> in the Smithy documentation.</p>
            tags: <p>The tags to add to the migration workflow template.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.conflict_exception.ConflictException: <p>This exception is thrown when an attempt to update or delete a resource would cause an inconsistent state.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.create_template_request.CreateTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.create_template_response.CreateTemplateResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_template

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_template.async_create_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.create_template_request.CreateTemplateRequest = {
            "template_name": template_name,
            "template_source": template_source,
        }
        if template_description is not None:
            input_["template_description"] = template_description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_template(
        self,
        id: "capo_migrationhuborchestrator.types.template_id.TemplateId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "capo_migrationhuborchestrator.types.get_migration_workflow_template_response.GetMigrationWorkflowTemplateResponse":
        """<p>Get the template you want to use for creating a migration workflow.</p>

        Args:
            id: <p>The ID of the template.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.get_migration_workflow_template_request.GetMigrationWorkflowTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.get_migration_workflow_template_response.GetMigrationWorkflowTemplateResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_template

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_template.async_get_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.get_migration_workflow_template_request.GetMigrationWorkflowTemplateRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_template(
        self,
        id: "capo_migrationhuborchestrator.types.template_id.TemplateId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        template_name: Optional[str] = None,
        template_description: Optional[str] = None,
        client_token: Optional[
            "capo_migrationhuborchestrator.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_migrationhuborchestrator.types.update_template_response.UpdateTemplateResponse":
        """<p>Updates a migration workflow template.</p>

        Args:
            id: <p>The ID of the request to update a migration workflow template.</p>
            template_name: <p>The name of the migration workflow template to update.</p>
            template_description: <p>The description of the migration workflow template to update.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.update_template_request.UpdateTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.update_template_response.UpdateTemplateResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_template

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_template.async_update_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.update_template_request.UpdateTemplateRequest = {
            "id": id
        }
        if template_name is not None:
            input_["template_name"] = template_name
        if template_description is not None:
            input_["template_description"] = template_description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_template(
        self,
        id: "capo_migrationhuborchestrator.types.template_id.TemplateId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "capo_migrationhuborchestrator.types.delete_template_response.DeleteTemplateResponse":
        """<p>Deletes a migration workflow template.</p>

        Args:
            id: <p>The ID of the request to delete a migration workflow template.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.delete_template_request.DeleteTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.delete_template_response.DeleteTemplateResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_template

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_template.async_delete_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.delete_template_request.DeleteTemplateRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_templates(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        max_results: Optional[
            "capo_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
        name: Optional[
            "capo_migrationhuborchestrator.types.template_name.TemplateName"
        ] = None,
    ) -> "capo_migrationhuborchestrator.types.list_migration_workflow_templates_response.ListMigrationWorkflowTemplatesResponse":
        """<p>List the templates available in Migration Hub Orchestrator to create a migration workflow.</p>

        Args:
            max_results: <p>The maximum number of results that can be returned.</p>
            next_token: <p>The pagination token.</p>
            name: <p>The name of the template.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.list_migration_workflow_templates_request.ListMigrationWorkflowTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.list_migration_workflow_templates_response.ListMigrationWorkflowTemplatesResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_templates

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_templates.async_list_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.list_migration_workflow_templates_request.ListMigrationWorkflowTemplatesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_templates(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        max_results: Optional[
            "capo_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
        name: Optional[
            "capo_migrationhuborchestrator.types.template_name.TemplateName"
        ] = None,
    ) -> "AsyncIterator[capo_migrationhuborchestrator.types.template_summary.TemplateSummary]":
        _token = next_token
        while True:
            _response = await self.list_templates(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                name=name,
            )
            _page = _resolve_path(_response, ("template_summary",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_plugins(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        max_results: Optional[
            "capo_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
    ) -> (
        "capo_migrationhuborchestrator.types.list_plugins_response.ListPluginsResponse"
    ):
        """<p>List AWS Migration Hub Orchestrator plugins.</p>

        Args:
            max_results: <p>The maximum number of plugins that can be returned.</p>
            next_token: <p>The pagination token.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.list_plugins_request.ListPluginsRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.list_plugins_response.ListPluginsResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_plugins

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_plugins.async_list_plugins(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.list_plugins_request.ListPluginsRequest = {}
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

    async def iter_list_plugins(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        max_results: Optional[
            "capo_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_migrationhuborchestrator.types.plugin_summary.PluginSummary]":
        _token = next_token
        while True:
            _response = await self.list_plugins(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("plugins",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_template_step(
        self,
        id: "capo_migrationhuborchestrator.types.step_id.StepId",
        template_id: "capo_migrationhuborchestrator.types.template_id.TemplateId",
        step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "capo_migrationhuborchestrator.types.get_template_step_response.GetTemplateStepResponse":
        """<p>Get a specific step in a template.</p>

        Args:
            id: <p>The ID of the step.</p>
            template_id: <p>The ID of the template.</p>
            step_group_id: <p>The ID of the step group.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.get_template_step_request.GetTemplateStepRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.get_template_step_response.GetTemplateStepResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_template_step

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_template_step.async_get_template_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.get_template_step_request.GetTemplateStepRequest = {
            "id": id,
            "template_id": template_id,
            "step_group_id": step_group_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_template_steps(
        self,
        template_id: "capo_migrationhuborchestrator.types.template_id.TemplateId",
        step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        max_results: Optional[
            "capo_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
    ) -> "capo_migrationhuborchestrator.types.list_template_steps_response.ListTemplateStepsResponse":
        """<p>List the steps in a template.</p>

        Args:
            max_results: <p>The maximum number of results that can be returned.</p>
            next_token: <p>The pagination token.</p>
            template_id: <p>The ID of the template.</p>
            step_group_id: <p>The ID of the step group.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.list_template_steps_request.ListTemplateStepsRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.list_template_steps_response.ListTemplateStepsResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_template_steps

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_template_steps.async_list_template_steps(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.list_template_steps_request.ListTemplateStepsRequest = {
            "template_id": template_id,
            "step_group_id": step_group_id,
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

    async def iter_list_template_steps(
        self,
        template_id: "capo_migrationhuborchestrator.types.template_id.TemplateId",
        step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        max_results: Optional[
            "capo_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_migrationhuborchestrator.types.template_step_summary.TemplateStepSummary]":
        _token = next_token
        while True:
            _response = await self.list_template_steps(
                template_id,
                step_group_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("template_step_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_template_step_group(
        self,
        template_id: "capo_migrationhuborchestrator.types.template_id.TemplateId",
        id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "capo_migrationhuborchestrator.types.get_template_step_group_response.GetTemplateStepGroupResponse":
        """<p>Get a step group in a template.</p>

        Args:
            template_id: <p>The ID of the template.</p>
            id: <p>The ID of the step group.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.get_template_step_group_request.GetTemplateStepGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.get_template_step_group_response.GetTemplateStepGroupResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_template_step_group

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_template_step_group.async_get_template_step_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.get_template_step_group_request.GetTemplateStepGroupRequest = {
            "template_id": template_id,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_template_step_groups(
        self,
        template_id: "capo_migrationhuborchestrator.types.template_id.TemplateId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        max_results: Optional[
            "capo_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
    ) -> "capo_migrationhuborchestrator.types.list_template_step_groups_response.ListTemplateStepGroupsResponse":
        """<p>List the step groups in a template.</p>

        Args:
            max_results: <p>The maximum number of results that can be returned.</p>
            next_token: <p>The pagination token.</p>
            template_id: <p>The ID of the template.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.list_template_step_groups_request.ListTemplateStepGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.list_template_step_groups_response.ListTemplateStepGroupsResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_template_step_groups

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_template_step_groups.async_list_template_step_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.list_template_step_groups_request.ListTemplateStepGroupsRequest = {
            "template_id": template_id
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

    async def iter_list_template_step_groups(
        self,
        template_id: "capo_migrationhuborchestrator.types.template_id.TemplateId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        max_results: Optional[
            "capo_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_migrationhuborchestrator.types.template_step_group_summary.TemplateStepGroupSummary]":
        _token = next_token
        while True:
            _response = await self.list_template_step_groups(
                template_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("template_step_group_summary",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_workflow_step(
        self,
        name: "capo_migrationhuborchestrator.types.migration_workflow_name.MigrationWorkflowName",
        step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        step_action_type: "capo_migrationhuborchestrator.types.step_action_type.StepActionType",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        description: Optional[
            "capo_migrationhuborchestrator.types.migration_workflow_description.MigrationWorkflowDescription"
        ] = None,
        workflow_step_automation_configuration: Optional[
            "capo_migrationhuborchestrator.types.workflow_step_automation_configuration.WorkflowStepAutomationConfiguration"
        ] = None,
        step_target: Optional[
            "capo_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        outputs: Optional[
            "capo_migrationhuborchestrator.types.workflow_step_output_list.WorkflowStepOutputList"
        ] = None,
        previous: Optional[
            "capo_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        next: Optional[
            "capo_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
    ) -> "capo_migrationhuborchestrator.types.create_workflow_step_response.CreateWorkflowStepResponse":
        """<p>Create a step in the migration workflow.</p>

        Args:
            name: <p>The name of the step.</p>
            step_group_id: <p>The ID of the step group.</p>
            workflow_id: <p>The ID of the migration workflow.</p>
            step_action_type: <p>The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.</p>
            description: <p>The description of the step.</p>
            workflow_step_automation_configuration: <p>The custom script to run tests on source or target environments.</p>
            step_target: <p>The servers on which a step will be run.</p>
            outputs: <p>The key value pairs added for the expected output.</p>
            previous: <p>The previous step.</p>
            next: <p>The next step.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.create_workflow_step_request.CreateWorkflowStepRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.create_workflow_step_response.CreateWorkflowStepResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow_step

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow_step.async_create_workflow_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.create_workflow_step_request.CreateWorkflowStepRequest = {
            "name": name,
            "step_group_id": step_group_id,
            "workflow_id": workflow_id,
            "step_action_type": step_action_type,
        }
        if description is not None:
            input_["description"] = description
        if workflow_step_automation_configuration is not None:
            input_["workflow_step_automation_configuration"] = (
                workflow_step_automation_configuration
            )
        if step_target is not None:
            input_["step_target"] = step_target
        if outputs is not None:
            input_["outputs"] = outputs
        if previous is not None:
            input_["previous"] = previous
        if next is not None:
            input_["next"] = next

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_workflow_step(
        self,
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        id: "capo_migrationhuborchestrator.types.step_id.StepId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "capo_migrationhuborchestrator.types.get_workflow_step_response.GetWorkflowStepResponse":
        """<p>Get a step in the migration workflow.</p>

        Args:
            workflow_id: <p>The ID of the migration workflow.</p>
            step_group_id: <p>The ID of the step group.</p>
            id: <p>The ID of the step.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.get_workflow_step_request.GetWorkflowStepRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.get_workflow_step_response.GetWorkflowStepResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow_step

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow_step.async_get_workflow_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.get_workflow_step_request.GetWorkflowStepRequest = {
            "workflow_id": workflow_id,
            "step_group_id": step_group_id,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_workflow_step(
        self,
        id: "capo_migrationhuborchestrator.types.step_id.StepId",
        step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        name: Optional["capo_migrationhuborchestrator.types.step_name.StepName"] = None,
        description: Optional[
            "capo_migrationhuborchestrator.types.step_description.StepDescription"
        ] = None,
        step_action_type: Optional[
            "capo_migrationhuborchestrator.types.step_action_type.StepActionType"
        ] = None,
        workflow_step_automation_configuration: Optional[
            "capo_migrationhuborchestrator.types.workflow_step_automation_configuration.WorkflowStepAutomationConfiguration"
        ] = None,
        step_target: Optional[
            "capo_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        outputs: Optional[
            "capo_migrationhuborchestrator.types.workflow_step_output_list.WorkflowStepOutputList"
        ] = None,
        previous: Optional[
            "capo_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        next: Optional[
            "capo_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        status: Optional[
            "capo_migrationhuborchestrator.types.step_status.StepStatus"
        ] = None,
    ) -> "capo_migrationhuborchestrator.types.update_workflow_step_response.UpdateWorkflowStepResponse":
        """<p>Update a step in a migration workflow.</p>

        Args:
            id: <p>The ID of the step.</p>
            step_group_id: <p>The ID of the step group.</p>
            workflow_id: <p>The ID of the migration workflow.</p>
            name: <p>The name of the step.</p>
            description: <p>The description of the step.</p>
            step_action_type: <p>The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.</p>
            workflow_step_automation_configuration: <p>The custom script to run tests on the source and target environments.</p>
            step_target: <p>The servers on which a step will be run.</p>
            outputs: <p>The outputs of a step.</p>
            previous: <p>The previous step.</p>
            next: <p>The next step.</p>
            status: <p>The status of the step.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.update_workflow_step_request.UpdateWorkflowStepRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.update_workflow_step_response.UpdateWorkflowStepResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow_step

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow_step.async_update_workflow_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.update_workflow_step_request.UpdateWorkflowStepRequest = {
            "id": id,
            "step_group_id": step_group_id,
            "workflow_id": workflow_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if step_action_type is not None:
            input_["step_action_type"] = step_action_type
        if workflow_step_automation_configuration is not None:
            input_["workflow_step_automation_configuration"] = (
                workflow_step_automation_configuration
            )
        if step_target is not None:
            input_["step_target"] = step_target
        if outputs is not None:
            input_["outputs"] = outputs
        if previous is not None:
            input_["previous"] = previous
        if next is not None:
            input_["next"] = next
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_workflow_step(
        self,
        id: "capo_migrationhuborchestrator.types.step_id.StepId",
        step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "capo_migrationhuborchestrator.types.delete_workflow_step_response.DeleteWorkflowStepResponse":
        """<p>Delete a step in a migration workflow. Pause the workflow to delete a running step.</p>

        Args:
            id: <p>The ID of the step you want to delete.</p>
            step_group_id: <p>The ID of the step group that contains the step you want to delete.</p>
            workflow_id: <p>The ID of the migration workflow.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.delete_workflow_step_request.DeleteWorkflowStepRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.delete_workflow_step_response.DeleteWorkflowStepResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow_step

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow_step.async_delete_workflow_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.delete_workflow_step_request.DeleteWorkflowStepRequest = {
            "id": id,
            "step_group_id": step_group_id,
            "workflow_id": workflow_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_workflow_steps(
        self,
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        next_token: Optional[
            "capo_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_migrationhuborchestrator.types.list_workflow_steps_response.ListWorkflowStepsResponse":
        """<p>List the steps in a workflow.</p>

        Args:
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of results that can be returned.</p>
            workflow_id: <p>The ID of the migration workflow.</p>
            step_group_id: <p>The ID of the step group.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.list_workflow_steps_request.ListWorkflowStepsRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.list_workflow_steps_response.ListWorkflowStepsResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflow_steps

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflow_steps.async_list_workflow_steps(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.list_workflow_steps_request.ListWorkflowStepsRequest = {
            "workflow_id": workflow_id,
            "step_group_id": step_group_id,
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

    async def iter_list_workflow_steps(
        self,
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        next_token: Optional[
            "capo_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_migrationhuborchestrator.types.workflow_step_summary.WorkflowStepSummary]":
        _token = next_token
        while True:
            _response = await self.list_workflow_steps(
                workflow_id,
                step_group_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("workflow_steps_summary",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def retry_workflow_step(
        self,
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        id: "capo_migrationhuborchestrator.types.step_id.StepId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "capo_migrationhuborchestrator.types.retry_workflow_step_response.RetryWorkflowStepResponse":
        """<p>Retry a failed step in a migration workflow.</p>

        Args:
            workflow_id: <p>The ID of the migration workflow.</p>
            step_group_id: <p>The ID of the step group.</p>
            id: <p>The ID of the step.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.retry_workflow_step_request.RetryWorkflowStepRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.retry_workflow_step_response.RetryWorkflowStepResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.retry_workflow_step

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.retry_workflow_step.async_retry_workflow_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.retry_workflow_step_request.RetryWorkflowStepRequest = {
            "workflow_id": workflow_id,
            "step_group_id": step_group_id,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_workflow_step_group(
        self,
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        name: "capo_migrationhuborchestrator.types.step_group_name.StepGroupName",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        description: Optional[
            "capo_migrationhuborchestrator.types.step_group_description.StepGroupDescription"
        ] = None,
        next: Optional[
            "capo_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        previous: Optional[
            "capo_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
    ) -> "capo_migrationhuborchestrator.types.create_workflow_step_group_response.CreateWorkflowStepGroupResponse":
        """<p>Create a step group in a migration workflow.</p>

        Args:
            workflow_id: <p>The ID of the migration workflow that will contain the step group.</p>
            name: <p>The name of the step group.</p>
            description: <p>The description of the step group.</p>
            next: <p>The next step group.</p>
            previous: <p>The previous step group.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.create_workflow_step_group_request.CreateWorkflowStepGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.create_workflow_step_group_response.CreateWorkflowStepGroupResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow_step_group

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow_step_group.async_create_workflow_step_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.create_workflow_step_group_request.CreateWorkflowStepGroupRequest = {
            "workflow_id": workflow_id,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if next is not None:
            input_["next"] = next
        if previous is not None:
            input_["previous"] = previous

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_workflow_step_group(
        self,
        id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "capo_migrationhuborchestrator.types.get_workflow_step_group_response.GetWorkflowStepGroupResponse":
        """<p>Get the step group of a migration workflow.</p>

        Args:
            id: <p>The ID of the step group.</p>
            workflow_id: <p>The ID of the migration workflow.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.get_workflow_step_group_request.GetWorkflowStepGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.get_workflow_step_group_response.GetWorkflowStepGroupResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow_step_group

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow_step_group.async_get_workflow_step_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.get_workflow_step_group_request.GetWorkflowStepGroupRequest = {
            "id": id,
            "workflow_id": workflow_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_workflow_step_group(
        self,
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        name: Optional[
            "capo_migrationhuborchestrator.types.step_group_name.StepGroupName"
        ] = None,
        description: Optional[
            "capo_migrationhuborchestrator.types.step_group_description.StepGroupDescription"
        ] = None,
        next: Optional[
            "capo_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        previous: Optional[
            "capo_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
    ) -> "capo_migrationhuborchestrator.types.update_workflow_step_group_response.UpdateWorkflowStepGroupResponse":
        """<p>Update the step group in a migration workflow.</p>

        Args:
            workflow_id: <p>The ID of the migration workflow.</p>
            id: <p>The ID of the step group.</p>
            name: <p>The name of the step group.</p>
            description: <p>The description of the step group.</p>
            next: <p>The next step group.</p>
            previous: <p>The previous step group.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.update_workflow_step_group_request.UpdateWorkflowStepGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.update_workflow_step_group_response.UpdateWorkflowStepGroupResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow_step_group

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow_step_group.async_update_workflow_step_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.update_workflow_step_group_request.UpdateWorkflowStepGroupRequest = {
            "workflow_id": workflow_id,
            "id": id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if next is not None:
            input_["next"] = next
        if previous is not None:
            input_["previous"] = previous

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_workflow_step_group(
        self,
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "capo_migrationhuborchestrator.types.delete_workflow_step_group_response.DeleteWorkflowStepGroupResponse":
        """<p>Delete a step group in a migration workflow.</p>

        Args:
            workflow_id: <p>The ID of the migration workflow.</p>
            id: <p>The ID of the step group you want to delete.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.delete_workflow_step_group_request.DeleteWorkflowStepGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.delete_workflow_step_group_response.DeleteWorkflowStepGroupResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow_step_group

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow_step_group.async_delete_workflow_step_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.delete_workflow_step_group_request.DeleteWorkflowStepGroupRequest = {
            "workflow_id": workflow_id,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_workflow_step_groups(
        self,
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        next_token: Optional[
            "capo_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_migrationhuborchestrator.types.list_workflow_step_groups_response.ListWorkflowStepGroupsResponse":
        """<p>List the step groups in a migration workflow.</p>

        Args:
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of results that can be returned.</p>
            workflow_id: <p>The ID of the migration workflow.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.list_workflow_step_groups_request.ListWorkflowStepGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.list_workflow_step_groups_response.ListWorkflowStepGroupsResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflow_step_groups

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflow_step_groups.async_list_workflow_step_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.list_workflow_step_groups_request.ListWorkflowStepGroupsRequest = {
            "workflow_id": workflow_id
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

    async def iter_list_workflow_step_groups(
        self,
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        next_token: Optional[
            "capo_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_migrationhuborchestrator.types.workflow_step_group_summary.WorkflowStepGroupSummary]":
        _token = next_token
        while True:
            _response = await self.list_workflow_step_groups(
                workflow_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("workflow_step_groups_summary",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
