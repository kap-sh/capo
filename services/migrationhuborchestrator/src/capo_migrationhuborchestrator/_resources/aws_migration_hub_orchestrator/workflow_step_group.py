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
    import capo_migrationhuborchestrator.types.create_workflow_step_group_request
    import capo_migrationhuborchestrator.types.create_workflow_step_group_response
    import capo_migrationhuborchestrator.types.delete_workflow_step_group_request
    import capo_migrationhuborchestrator.types.delete_workflow_step_group_response
    import capo_migrationhuborchestrator.types.get_workflow_step_group_request
    import capo_migrationhuborchestrator.types.get_workflow_step_group_response
    import capo_migrationhuborchestrator.types.list_workflow_step_groups_request
    import capo_migrationhuborchestrator.types.list_workflow_step_groups_response
    import capo_migrationhuborchestrator.types.max_results
    import capo_migrationhuborchestrator.types.migration_workflow_id
    import capo_migrationhuborchestrator.types.next_token
    import capo_migrationhuborchestrator.types.step_group_description
    import capo_migrationhuborchestrator.types.step_group_id
    import capo_migrationhuborchestrator.types.step_group_name
    import capo_migrationhuborchestrator.types.string_list
    import capo_migrationhuborchestrator.types.update_workflow_step_group_request
    import capo_migrationhuborchestrator.types.update_workflow_step_group_response
    import capo_migrationhuborchestrator.types.workflow_step_group_summary
    from capo_migrationhuborchestrator._services.async_migration_hub_orchestrator import (
        AsyncMigrationHubOrchestratorClient,
        AsyncMigrationHubOrchestratorClientConfig,
    )
    from capo_migrationhuborchestrator._services.migration_hub_orchestrator import (
        MigrationHubOrchestratorClient,
        MigrationHubOrchestratorClientConfig,
    )


class WorkflowStepGroup:
    def __init__(self, service: MigrationHubOrchestratorClient) -> None:
        self._service = service

    def create(
        self,
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        name: "capo_migrationhuborchestrator.types.step_group_name.StepGroupName",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.create_workflow_step_group_request.CreateWorkflowStepGroupRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.create_workflow_step_group_response.CreateWorkflowStepGroupResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow_step_group

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow_step_group.create_workflow_step_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateWorkflowStepGroup")
        )
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.get_workflow_step_group_request.GetWorkflowStepGroupRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.get_workflow_step_group_response.GetWorkflowStepGroupResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow_step_group

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow_step_group.get_workflow_step_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetWorkflowStepGroup")
        )
        input_: capo_migrationhuborchestrator.types.get_workflow_step_group_request.GetWorkflowStepGroupRequest = {
            "id": id,
            "workflow_id": workflow_id,
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
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.update_workflow_step_group_request.UpdateWorkflowStepGroupRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.update_workflow_step_group_response.UpdateWorkflowStepGroupResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow_step_group

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow_step_group.update_workflow_step_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateWorkflowStepGroup")
        )
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.delete_workflow_step_group_request.DeleteWorkflowStepGroupRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.delete_workflow_step_group_response.DeleteWorkflowStepGroupResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow_step_group

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow_step_group.delete_workflow_step_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWorkflowStepGroup")
        )
        input_: capo_migrationhuborchestrator.types.delete_workflow_step_group_request.DeleteWorkflowStepGroupRequest = {
            "workflow_id": workflow_id,
            "id": id,
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
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.list_workflow_step_groups_request.ListWorkflowStepGroupsRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.list_workflow_step_groups_response.ListWorkflowStepGroupsResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflow_step_groups

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflow_step_groups.list_workflow_step_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWorkflowStepGroups")
        )
        input_: capo_migrationhuborchestrator.types.list_workflow_step_groups_request.ListWorkflowStepGroupsRequest = {
            "workflow_id": workflow_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncWorkflowStepGroup:
    def __init__(self, service: AsyncMigrationHubOrchestratorClient) -> None:
        self._service = service

    async def create(
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateWorkflowStepGroup")
        )
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

    async def read(
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetWorkflowStepGroup")
        )
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

    async def update(
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateWorkflowStepGroup")
        )
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

    async def delete(
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWorkflowStepGroup")
        )
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

    async def list(
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWorkflowStepGroups")
        )
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
