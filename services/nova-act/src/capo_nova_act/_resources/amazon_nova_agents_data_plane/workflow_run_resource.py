from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_nova_act._auth._signers
import capo_nova_act._auth._sigv4
from capo_nova_act._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_nova_act.types.client_info
    import capo_nova_act.types.client_token
    import capo_nova_act.types.cloud_watch_log_group_name
    import capo_nova_act.types.create_workflow_run_request
    import capo_nova_act.types.create_workflow_run_response
    import capo_nova_act.types.delete_workflow_run_request
    import capo_nova_act.types.delete_workflow_run_response
    import capo_nova_act.types.get_workflow_run_request
    import capo_nova_act.types.get_workflow_run_response
    import capo_nova_act.types.list_workflow_runs_request
    import capo_nova_act.types.list_workflow_runs_response
    import capo_nova_act.types.max_results
    import capo_nova_act.types.model_id
    import capo_nova_act.types.next_token
    import capo_nova_act.types.sort_order
    import capo_nova_act.types.update_workflow_run_request
    import capo_nova_act.types.update_workflow_run_response
    import capo_nova_act.types.uuid_string
    import capo_nova_act.types.workflow_definition_name
    import capo_nova_act.types.workflow_run_status
    import capo_nova_act.types.workflow_run_summary
    from capo_nova_act._services.async_nova_act import (
        AsyncNovaActClient,
        AsyncNovaActClientConfig,
    )
    from capo_nova_act._services.nova_act import NovaActClient, NovaActClientConfig


class WorkflowRunResource:
    def __init__(self, service: NovaActClient) -> None:
        self._service = service

    def create(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        model_id: "capo_nova_act.types.model_id.ModelId",
        client_info: "capo_nova_act.types.client_info.ClientInfo",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        client_token: Optional["capo_nova_act.types.client_token.ClientToken"] = None,
        log_group_name: Optional[
            "capo_nova_act.types.cloud_watch_log_group_name.CloudWatchLogGroupName"
        ] = None,
    ) -> "capo_nova_act.types.create_workflow_run_response.CreateWorkflowRunResponse":
        """<p>Creates a new execution instance of a workflow definition with specified parameters.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to execute.</p>
            model_id: <p>The ID of the AI model to use for workflow execution.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            log_group_name: <p>The CloudWatch log group name for storing workflow execution logs.</p>
            client_info: <p>Information about the client making the request, including compatibility version and SDK version.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.create_workflow_run_request.CreateWorkflowRunRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.create_workflow_run_response.CreateWorkflowRunResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_run

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_run.create_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateWorkflowRun")
        )
        input_: capo_nova_act.types.create_workflow_run_request.CreateWorkflowRunRequest = {
            "workflow_definition_name": workflow_definition_name,
            "model_id": model_id,
            "client_info": client_info,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if log_group_name is not None:
            input_["log_group_name"] = log_group_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
    ) -> "capo_nova_act.types.get_workflow_run_response.GetWorkflowRunResponse":
        """<p>Retrieves the current state, configuration, and execution details of a workflow run.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to retrieve.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.get_workflow_run_request.GetWorkflowRunRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.get_workflow_run_response.GetWorkflowRunResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_run

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_run.get_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetWorkflowRun")
        )
        input_: capo_nova_act.types.get_workflow_run_request.GetWorkflowRunRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
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
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        status: "capo_nova_act.types.workflow_run_status.WorkflowRunStatus",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
    ) -> "capo_nova_act.types.update_workflow_run_response.UpdateWorkflowRunResponse":
        """<p>Updates the configuration or state of an active workflow run.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to update.</p>
            status: <p>The new status to set for the workflow run.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.update_workflow_run_request.UpdateWorkflowRunRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.update_workflow_run_response.UpdateWorkflowRunResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.update_workflow_run

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.update_workflow_run.update_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateWorkflowRun")
        )
        input_: capo_nova_act.types.update_workflow_run_request.UpdateWorkflowRunRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
            "status": status,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
    ) -> "capo_nova_act.types.delete_workflow_run_response.DeleteWorkflowRunResponse":
        """<p>Terminates and cleans up a workflow run, stopping all associated acts and sessions.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to delete.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.delete_workflow_run_request.DeleteWorkflowRunRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.delete_workflow_run_response.DeleteWorkflowRunResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_run

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_run.delete_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWorkflowRun")
        )
        input_: capo_nova_act.types.delete_workflow_run_request.DeleteWorkflowRunRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
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
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        max_results: Optional["capo_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["capo_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "capo_nova_act.types.list_workflow_runs_response.ListWorkflowRunsResponse":
        """<p>Lists all workflow runs for a specific workflow definition with optional filtering and pagination.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to list workflow runs for.</p>
            max_results: <p>The maximum number of workflow runs to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned workflow runs (ascending or descending).</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.list_workflow_runs_request.ListWorkflowRunsRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.list_workflow_runs_response.ListWorkflowRunsResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_runs

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_runs.list_workflow_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWorkflowRuns")
        )
        input_: capo_nova_act.types.list_workflow_runs_request.ListWorkflowRunsRequest = {
            "workflow_definition_name": workflow_definition_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncWorkflowRunResource:
    def __init__(self, service: AsyncNovaActClient) -> None:
        self._service = service

    async def create(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        model_id: "capo_nova_act.types.model_id.ModelId",
        client_info: "capo_nova_act.types.client_info.ClientInfo",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        client_token: Optional["capo_nova_act.types.client_token.ClientToken"] = None,
        log_group_name: Optional[
            "capo_nova_act.types.cloud_watch_log_group_name.CloudWatchLogGroupName"
        ] = None,
    ) -> "capo_nova_act.types.create_workflow_run_response.CreateWorkflowRunResponse":
        """<p>Creates a new execution instance of a workflow definition with specified parameters.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to execute.</p>
            model_id: <p>The ID of the AI model to use for workflow execution.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            log_group_name: <p>The CloudWatch log group name for storing workflow execution logs.</p>
            client_info: <p>Information about the client making the request, including compatibility version and SDK version.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_nova_act.types.create_workflow_run_request.CreateWorkflowRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_nova_act.types.create_workflow_run_response.CreateWorkflowRunResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_run

            (
                output,
                http_response,
            ) = await capo_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_run.async_create_workflow_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateWorkflowRun")
        )
        input_: capo_nova_act.types.create_workflow_run_request.CreateWorkflowRunRequest = {
            "workflow_definition_name": workflow_definition_name,
            "model_id": model_id,
            "client_info": client_info,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if log_group_name is not None:
            input_["log_group_name"] = log_group_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
    ) -> "capo_nova_act.types.get_workflow_run_response.GetWorkflowRunResponse":
        """<p>Retrieves the current state, configuration, and execution details of a workflow run.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to retrieve.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_nova_act.types.get_workflow_run_request.GetWorkflowRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_nova_act.types.get_workflow_run_response.GetWorkflowRunResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_run

            (
                output,
                http_response,
            ) = await capo_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_run.async_get_workflow_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetWorkflowRun")
        )
        input_: capo_nova_act.types.get_workflow_run_request.GetWorkflowRunRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
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
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        status: "capo_nova_act.types.workflow_run_status.WorkflowRunStatus",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
    ) -> "capo_nova_act.types.update_workflow_run_response.UpdateWorkflowRunResponse":
        """<p>Updates the configuration or state of an active workflow run.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to update.</p>
            status: <p>The new status to set for the workflow run.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_nova_act.types.update_workflow_run_request.UpdateWorkflowRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_nova_act.types.update_workflow_run_response.UpdateWorkflowRunResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.update_workflow_run

            (
                output,
                http_response,
            ) = await capo_nova_act._operations.amazon_nova_agents_data_plane.update_workflow_run.async_update_workflow_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateWorkflowRun")
        )
        input_: capo_nova_act.types.update_workflow_run_request.UpdateWorkflowRunRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
            "status": status,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
    ) -> "capo_nova_act.types.delete_workflow_run_response.DeleteWorkflowRunResponse":
        """<p>Terminates and cleans up a workflow run, stopping all associated acts and sessions.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to delete.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_nova_act.types.delete_workflow_run_request.DeleteWorkflowRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_nova_act.types.delete_workflow_run_response.DeleteWorkflowRunResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_run

            (
                output,
                http_response,
            ) = await capo_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_run.async_delete_workflow_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWorkflowRun")
        )
        input_: capo_nova_act.types.delete_workflow_run_request.DeleteWorkflowRunRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
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
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        max_results: Optional["capo_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["capo_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "capo_nova_act.types.list_workflow_runs_response.ListWorkflowRunsResponse":
        """<p>Lists all workflow runs for a specific workflow definition with optional filtering and pagination.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to list workflow runs for.</p>
            max_results: <p>The maximum number of workflow runs to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned workflow runs (ascending or descending).</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_nova_act.types.list_workflow_runs_request.ListWorkflowRunsRequest]",
        ) -> AsyncOperationResponse[
            "capo_nova_act.types.list_workflow_runs_response.ListWorkflowRunsResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_runs

            (
                output,
                http_response,
            ) = await capo_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_runs.async_list_workflow_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWorkflowRuns")
        )
        input_: capo_nova_act.types.list_workflow_runs_request.ListWorkflowRunsRequest = {
            "workflow_definition_name": workflow_definition_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
