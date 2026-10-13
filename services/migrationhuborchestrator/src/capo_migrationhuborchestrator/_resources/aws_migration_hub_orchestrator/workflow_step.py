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
    import capo_migrationhuborchestrator.types.create_workflow_step_request
    import capo_migrationhuborchestrator.types.create_workflow_step_response
    import capo_migrationhuborchestrator.types.delete_workflow_step_request
    import capo_migrationhuborchestrator.types.delete_workflow_step_response
    import capo_migrationhuborchestrator.types.get_workflow_step_request
    import capo_migrationhuborchestrator.types.get_workflow_step_response
    import capo_migrationhuborchestrator.types.list_workflow_steps_request
    import capo_migrationhuborchestrator.types.list_workflow_steps_response
    import capo_migrationhuborchestrator.types.max_results
    import capo_migrationhuborchestrator.types.migration_workflow_description
    import capo_migrationhuborchestrator.types.migration_workflow_id
    import capo_migrationhuborchestrator.types.migration_workflow_name
    import capo_migrationhuborchestrator.types.next_token
    import capo_migrationhuborchestrator.types.retry_workflow_step_request
    import capo_migrationhuborchestrator.types.retry_workflow_step_response
    import capo_migrationhuborchestrator.types.step_action_type
    import capo_migrationhuborchestrator.types.step_description
    import capo_migrationhuborchestrator.types.step_group_id
    import capo_migrationhuborchestrator.types.step_id
    import capo_migrationhuborchestrator.types.step_name
    import capo_migrationhuborchestrator.types.step_status
    import capo_migrationhuborchestrator.types.string_list
    import capo_migrationhuborchestrator.types.update_workflow_step_request
    import capo_migrationhuborchestrator.types.update_workflow_step_response
    import capo_migrationhuborchestrator.types.workflow_step_automation_configuration
    import capo_migrationhuborchestrator.types.workflow_step_output_list
    import capo_migrationhuborchestrator.types.workflow_step_summary
    from capo_migrationhuborchestrator._services.async_migration_hub_orchestrator import (
        AsyncMigrationHubOrchestratorClient,
        AsyncMigrationHubOrchestratorClientConfig,
    )
    from capo_migrationhuborchestrator._services.migration_hub_orchestrator import (
        MigrationHubOrchestratorClient,
        MigrationHubOrchestratorClientConfig,
    )


class WorkflowStep:
    def __init__(self, service: MigrationHubOrchestratorClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_migrationhuborchestrator.types.migration_workflow_name.MigrationWorkflowName",
        step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        step_action_type: "capo_migrationhuborchestrator.types.step_action_type.StepActionType",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.create_workflow_step_request.CreateWorkflowStepRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.create_workflow_step_response.CreateWorkflowStepResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow_step

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow_step.create_workflow_step(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateWorkflowStep")
        )
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        id: "capo_migrationhuborchestrator.types.step_id.StepId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.get_workflow_step_request.GetWorkflowStepRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.get_workflow_step_response.GetWorkflowStepResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow_step

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow_step.get_workflow_step(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetWorkflowStep")
        )
        input_: capo_migrationhuborchestrator.types.get_workflow_step_request.GetWorkflowStepRequest = {
            "workflow_id": workflow_id,
            "step_group_id": step_group_id,
            "id": id,
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
        id: "capo_migrationhuborchestrator.types.step_id.StepId",
        step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.update_workflow_step_request.UpdateWorkflowStepRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.update_workflow_step_response.UpdateWorkflowStepResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow_step

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow_step.update_workflow_step(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateWorkflowStep")
        )
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id: "capo_migrationhuborchestrator.types.step_id.StepId",
        step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.delete_workflow_step_request.DeleteWorkflowStepRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.delete_workflow_step_response.DeleteWorkflowStepResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow_step

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow_step.delete_workflow_step(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWorkflowStep")
        )
        input_: capo_migrationhuborchestrator.types.delete_workflow_step_request.DeleteWorkflowStepRequest = {
            "id": id,
            "step_group_id": step_group_id,
            "workflow_id": workflow_id,
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
        step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.list_workflow_steps_request.ListWorkflowStepsRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.list_workflow_steps_response.ListWorkflowStepsResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflow_steps

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflow_steps.list_workflow_steps(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWorkflowSteps")
        )
        input_: capo_migrationhuborchestrator.types.list_workflow_steps_request.ListWorkflowStepsRequest = {
            "workflow_id": workflow_id,
            "step_group_id": step_group_id,
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

    def retry_workflow_step(
        self,
        workflow_id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId",
        id: "capo_migrationhuborchestrator.types.step_id.StepId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.retry_workflow_step_request.RetryWorkflowStepRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.retry_workflow_step_response.RetryWorkflowStepResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.retry_workflow_step

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.retry_workflow_step.retry_workflow_step(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RetryWorkflowStep")
        )
        input_: capo_migrationhuborchestrator.types.retry_workflow_step_request.RetryWorkflowStepRequest = {
            "workflow_id": workflow_id,
            "step_group_id": step_group_id,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncWorkflowStep:
    def __init__(self, service: AsyncMigrationHubOrchestratorClient) -> None:
        self._service = service

    async def create(
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateWorkflowStep")
        )
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

    async def read(
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetWorkflowStep")
        )
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

    async def update(
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateWorkflowStep")
        )
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

    async def delete(
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWorkflowStep")
        )
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

    async def list(
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWorkflowSteps")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RetryWorkflowStep")
        )
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
