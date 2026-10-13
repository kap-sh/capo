from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_migrationhuborchestrator._auth._signers
import capo_migrationhuborchestrator._auth._sigv4
from capo_migrationhuborchestrator._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.get_template_step_group_request
    import capo_migrationhuborchestrator.types.get_template_step_group_response
    import capo_migrationhuborchestrator.types.step_group_id
    import capo_migrationhuborchestrator.types.template_id
    from capo_migrationhuborchestrator._services.async_migration_hub_orchestrator import (
        AsyncMigrationHubOrchestratorClient,
        AsyncMigrationHubOrchestratorClientConfig,
    )
    from capo_migrationhuborchestrator._services.migration_hub_orchestrator import (
        MigrationHubOrchestratorClient,
        MigrationHubOrchestratorClientConfig,
    )


class TemplateStepGroup:
    def __init__(self, service: MigrationHubOrchestratorClient) -> None:
        self._service = service

    def read(
        self,
        template_id: "capo_migrationhuborchestrator.types.template_id.TemplateId",
        id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.get_template_step_group_request.GetTemplateStepGroupRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.get_template_step_group_response.GetTemplateStepGroupResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_template_step_group

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_template_step_group.get_template_step_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTemplateStepGroup")
        )
        input_: capo_migrationhuborchestrator.types.get_template_step_group_request.GetTemplateStepGroupRequest = {
            "template_id": template_id,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncTemplateStepGroup:
    def __init__(self, service: AsyncMigrationHubOrchestratorClient) -> None:
        self._service = service

    async def read(
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTemplateStepGroup")
        )
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
