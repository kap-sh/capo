from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_migrationhuborchestrator._auth._signers
import capo_migrationhuborchestrator._auth._sigv4
from capo_migrationhuborchestrator._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.client_token
    import capo_migrationhuborchestrator.types.create_template_request
    import capo_migrationhuborchestrator.types.create_template_response
    import capo_migrationhuborchestrator.types.delete_template_request
    import capo_migrationhuborchestrator.types.delete_template_response
    import capo_migrationhuborchestrator.types.get_migration_workflow_template_request
    import capo_migrationhuborchestrator.types.get_migration_workflow_template_response
    import capo_migrationhuborchestrator.types.list_migration_workflow_templates_request
    import capo_migrationhuborchestrator.types.list_migration_workflow_templates_response
    import capo_migrationhuborchestrator.types.max_results
    import capo_migrationhuborchestrator.types.next_token
    import capo_migrationhuborchestrator.types.tag_map
    import capo_migrationhuborchestrator.types.template_id
    import capo_migrationhuborchestrator.types.template_name
    import capo_migrationhuborchestrator.types.template_source
    import capo_migrationhuborchestrator.types.template_summary
    import capo_migrationhuborchestrator.types.update_template_request
    import capo_migrationhuborchestrator.types.update_template_response
    from capo_migrationhuborchestrator._services.async_migration_hub_orchestrator import (
        AsyncMigrationHubOrchestratorClient,
        AsyncMigrationHubOrchestratorClientConfig,
    )
    from capo_migrationhuborchestrator._services.migration_hub_orchestrator import (
        MigrationHubOrchestratorClient,
        MigrationHubOrchestratorClientConfig,
    )


class MigrationWorkflowTemplate:
    def __init__(self, service: MigrationHubOrchestratorClient) -> None:
        self._service = service

    def create(
        self,
        template_name: str,
        template_source: "capo_migrationhuborchestrator.types.template_source.TemplateSource",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.create_template_request.CreateTemplateRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.create_template_response.CreateTemplateResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_template

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_template.create_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        id: "capo_migrationhuborchestrator.types.template_id.TemplateId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.get_migration_workflow_template_request.GetMigrationWorkflowTemplateRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.get_migration_workflow_template_response.GetMigrationWorkflowTemplateResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_template

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_template.get_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.get_migration_workflow_template_request.GetMigrationWorkflowTemplateRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        id: "capo_migrationhuborchestrator.types.template_id.TemplateId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.update_template_request.UpdateTemplateRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.update_template_response.UpdateTemplateResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_template

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_template.update_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id: "capo_migrationhuborchestrator.types.template_id.TemplateId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.delete_template_request.DeleteTemplateRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.delete_template_response.DeleteTemplateResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_template

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_template.delete_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.delete_template_request.DeleteTemplateRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.list_migration_workflow_templates_request.ListMigrationWorkflowTemplatesRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.list_migration_workflow_templates_response.ListMigrationWorkflowTemplatesResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_templates

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_templates.list_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.list_migration_workflow_templates_request.ListMigrationWorkflowTemplatesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncMigrationWorkflowTemplate:
    def __init__(self, service: AsyncMigrationHubOrchestratorClient) -> None:
        self._service = service

    async def create(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def read(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def update(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def delete(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def list(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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
