from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

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
    import capo_migrationhuborchestrator.types.application_configuration_name
    import capo_migrationhuborchestrator.types.create_migration_workflow_request
    import capo_migrationhuborchestrator.types.create_migration_workflow_response
    import capo_migrationhuborchestrator.types.delete_migration_workflow_request
    import capo_migrationhuborchestrator.types.delete_migration_workflow_response
    import capo_migrationhuborchestrator.types.get_migration_workflow_request
    import capo_migrationhuborchestrator.types.get_migration_workflow_response
    import capo_migrationhuborchestrator.types.list_migration_workflows_request
    import capo_migrationhuborchestrator.types.list_migration_workflows_response
    import capo_migrationhuborchestrator.types.max_results
    import capo_migrationhuborchestrator.types.migration_workflow_id
    import capo_migrationhuborchestrator.types.migration_workflow_status_enum
    import capo_migrationhuborchestrator.types.migration_workflow_summary
    import capo_migrationhuborchestrator.types.next_token
    import capo_migrationhuborchestrator.types.start_migration_workflow_request
    import capo_migrationhuborchestrator.types.start_migration_workflow_response
    import capo_migrationhuborchestrator.types.step_input_parameters
    import capo_migrationhuborchestrator.types.stop_migration_workflow_request
    import capo_migrationhuborchestrator.types.stop_migration_workflow_response
    import capo_migrationhuborchestrator.types.string_list
    import capo_migrationhuborchestrator.types.string_map
    import capo_migrationhuborchestrator.types.template_id
    import capo_migrationhuborchestrator.types.update_migration_workflow_request
    import capo_migrationhuborchestrator.types.update_migration_workflow_response
    from capo_migrationhuborchestrator._services.async_migration_hub_orchestrator import (
        AsyncMigrationHubOrchestratorClient,
        AsyncMigrationHubOrchestratorClientConfig,
    )
    from capo_migrationhuborchestrator._services.migration_hub_orchestrator import (
        MigrationHubOrchestratorClient,
        MigrationHubOrchestratorClientConfig,
    )


class MigrationWorkflow:
    def __init__(self, service: MigrationHubOrchestratorClient) -> None:
        self._service = service

    def create(
        self,
        name: str,
        template_id: str,
        input_parameters: "capo_migrationhuborchestrator.types.step_input_parameters.StepInputParameters",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.create_migration_workflow_request.CreateMigrationWorkflowRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.create_migration_workflow_response.CreateMigrationWorkflowResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow.create_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_migrationhuborchestrator.types.create_migration_workflow_request.CreateMigrationWorkflowRequest",
        ) -> dict[str, Any]:
            import capo_migrationhuborchestrator.types.create_migration_workflow_request

            return capo_migrationhuborchestrator.types.create_migration_workflow_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_migrationhuborchestrator.types.create_migration_workflow_response.CreateMigrationWorkflowResponse",
        ) -> dict[str, Any]:
            import capo_migrationhuborchestrator.types.create_migration_workflow_response

            return capo_migrationhuborchestrator.types.create_migration_workflow_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateWorkflow",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.get_migration_workflow_request.GetMigrationWorkflowRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.get_migration_workflow_response.GetMigrationWorkflowResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow.get_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_migrationhuborchestrator.types.get_migration_workflow_response.GetMigrationWorkflowResponse",
        ) -> dict[str, Any]:
            import capo_migrationhuborchestrator.types.get_migration_workflow_response

            return capo_migrationhuborchestrator.types.get_migration_workflow_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetWorkflow", redact_output=_redact_output),
        )
        input_: capo_migrationhuborchestrator.types.get_migration_workflow_request.GetMigrationWorkflowRequest = {
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
        id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.update_migration_workflow_request.UpdateMigrationWorkflowRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.update_migration_workflow_response.UpdateMigrationWorkflowResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow.update_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_migrationhuborchestrator.types.update_migration_workflow_request.UpdateMigrationWorkflowRequest",
        ) -> dict[str, Any]:
            import capo_migrationhuborchestrator.types.update_migration_workflow_request

            return capo_migrationhuborchestrator.types.update_migration_workflow_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_migrationhuborchestrator.types.update_migration_workflow_response.UpdateMigrationWorkflowResponse",
        ) -> dict[str, Any]:
            import capo_migrationhuborchestrator.types.update_migration_workflow_response

            return capo_migrationhuborchestrator.types.update_migration_workflow_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateWorkflow",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.delete_migration_workflow_request.DeleteMigrationWorkflowRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.delete_migration_workflow_response.DeleteMigrationWorkflowResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow.delete_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWorkflow")
        )
        input_: capo_migrationhuborchestrator.types.delete_migration_workflow_request.DeleteMigrationWorkflowRequest = {
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.list_migration_workflows_request.ListMigrationWorkflowsRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.list_migration_workflows_response.ListMigrationWorkflowsResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflows

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflows.list_workflows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWorkflows")
        )
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_workflow(
        self,
        id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.start_migration_workflow_request.StartMigrationWorkflowRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.start_migration_workflow_response.StartMigrationWorkflowResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.start_workflow

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.start_workflow.start_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartWorkflow")
        )
        input_: capo_migrationhuborchestrator.types.start_migration_workflow_request.StartMigrationWorkflowRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_workflow(
        self,
        id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.stop_migration_workflow_request.StopMigrationWorkflowRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.stop_migration_workflow_response.StopMigrationWorkflowResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.stop_workflow

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.stop_workflow.stop_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopWorkflow")
        )
        input_: capo_migrationhuborchestrator.types.stop_migration_workflow_request.StopMigrationWorkflowRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncMigrationWorkflow:
    def __init__(self, service: AsyncMigrationHubOrchestratorClient) -> None:
        self._service = service

    async def create(
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

        def _redact_input(
            input_: "capo_migrationhuborchestrator.types.create_migration_workflow_request.CreateMigrationWorkflowRequest",
        ) -> dict[str, Any]:
            import capo_migrationhuborchestrator.types.create_migration_workflow_request

            return capo_migrationhuborchestrator.types.create_migration_workflow_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_migrationhuborchestrator.types.create_migration_workflow_response.CreateMigrationWorkflowResponse",
        ) -> dict[str, Any]:
            import capo_migrationhuborchestrator.types.create_migration_workflow_response

            return capo_migrationhuborchestrator.types.create_migration_workflow_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateWorkflow",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
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

    async def read(
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

        def _redact_output(
            output: "capo_migrationhuborchestrator.types.get_migration_workflow_response.GetMigrationWorkflowResponse",
        ) -> dict[str, Any]:
            import capo_migrationhuborchestrator.types.get_migration_workflow_response

            return capo_migrationhuborchestrator.types.get_migration_workflow_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetWorkflow", redact_output=_redact_output),
        )
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

    async def update(
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

        def _redact_input(
            input_: "capo_migrationhuborchestrator.types.update_migration_workflow_request.UpdateMigrationWorkflowRequest",
        ) -> dict[str, Any]:
            import capo_migrationhuborchestrator.types.update_migration_workflow_request

            return capo_migrationhuborchestrator.types.update_migration_workflow_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_migrationhuborchestrator.types.update_migration_workflow_response.UpdateMigrationWorkflowResponse",
        ) -> dict[str, Any]:
            import capo_migrationhuborchestrator.types.update_migration_workflow_response

            return capo_migrationhuborchestrator.types.update_migration_workflow_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateWorkflow",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
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

    async def delete(
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWorkflow")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWorkflows")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartWorkflow")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopWorkflow")
        )
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
