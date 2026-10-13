from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

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
    import capo_nova_act.types.act_error
    import capo_nova_act.types.act_status
    import capo_nova_act.types.act_summary
    import capo_nova_act.types.call_results
    import capo_nova_act.types.client_token
    import capo_nova_act.types.create_act_request
    import capo_nova_act.types.create_act_response
    import capo_nova_act.types.invoke_act_step_request
    import capo_nova_act.types.invoke_act_step_response
    import capo_nova_act.types.list_acts_request
    import capo_nova_act.types.list_acts_response
    import capo_nova_act.types.max_results
    import capo_nova_act.types.next_token
    import capo_nova_act.types.sort_order
    import capo_nova_act.types.task
    import capo_nova_act.types.tool_specs
    import capo_nova_act.types.update_act_request
    import capo_nova_act.types.update_act_response
    import capo_nova_act.types.uuid_string
    import capo_nova_act.types.workflow_definition_name
    from capo_nova_act._services.async_nova_act import (
        AsyncNovaActClient,
        AsyncNovaActClientConfig,
    )
    from capo_nova_act._services.nova_act import NovaActClient, NovaActClientConfig


class ActResource:
    def __init__(self, service: NovaActClient) -> None:
        self._service = service

    def create(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        session_id: "capo_nova_act.types.uuid_string.UuidString",
        task: "capo_nova_act.types.task.Task",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        tool_specs: Optional["capo_nova_act.types.tool_specs.ToolSpecs"] = None,
        client_token: Optional["capo_nova_act.types.client_token.ClientToken"] = None,
    ) -> "capo_nova_act.types.create_act_response.CreateActResponse":
        """<p>Creates a new AI task (act) within a session that can interact with tools and perform specific actions.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the session.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the session.</p>
            session_id: <p>The unique identifier of the session to create the act in.</p>
            task: <p>The task description that defines what the act should accomplish.</p>
            tool_specs: <p>A list of tool specifications that the act can invoke to complete its task.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.create_act_request.CreateActRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.create_act_response.CreateActResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.create_act

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.create_act.create_act(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_nova_act.types.create_act_request.CreateActRequest",
        ) -> dict[str, Any]:
            import capo_nova_act.types.create_act_request

            return capo_nova_act.types.create_act_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateAct", redact_input=_redact_input)
        )
        input_: capo_nova_act.types.create_act_request.CreateActRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
            "session_id": session_id,
            "task": task,
        }
        if tool_specs is not None:
            input_["tool_specs"] = tool_specs
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

    def list(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        workflow_run_id: Optional["capo_nova_act.types.uuid_string.UuidString"] = None,
        session_id: Optional["capo_nova_act.types.uuid_string.UuidString"] = None,
        max_results: Optional["capo_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["capo_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "capo_nova_act.types.list_acts_response.ListActsResponse":
        """<p>Lists all acts within a specific session with their current status and execution details.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the session.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the session.</p>
            session_id: <p>The unique identifier of the session to list acts for.</p>
            max_results: <p>The maximum number of acts to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned acts (ascending or descending).</p>

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
            req: "OperationRequest[capo_nova_act.types.list_acts_request.ListActsRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.list_acts_response.ListActsResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.list_acts

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.list_acts.list_acts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListActs")
        )
        input_: capo_nova_act.types.list_acts_request.ListActsRequest = {
            "workflow_definition_name": workflow_definition_name
        }
        if workflow_run_id is not None:
            input_["workflow_run_id"] = workflow_run_id
        if session_id is not None:
            input_["session_id"] = session_id
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

    def invoke_act_step(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        session_id: "capo_nova_act.types.uuid_string.UuidString",
        act_id: "capo_nova_act.types.uuid_string.UuidString",
        call_results: "capo_nova_act.types.call_results.CallResults",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        previous_step_id: Optional["capo_nova_act.types.uuid_string.UuidString"] = None,
    ) -> "capo_nova_act.types.invoke_act_step_response.InvokeActStepResponse":
        """<p>Executes the next step of an act, processing tool call results and returning new tool calls if needed.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the act.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the act.</p>
            session_id: <p>The unique identifier of the session containing the act.</p>
            act_id: <p>The unique identifier of the act to invoke the next step for.</p>
            call_results: <p>The results from previous tool calls that the act requested.</p>
            previous_step_id: <p>The identifier of the previous step, used for tracking execution flow.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.invoke_act_step_request.InvokeActStepRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.invoke_act_step_response.InvokeActStepResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.invoke_act_step

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.invoke_act_step.invoke_act_step(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_nova_act.types.invoke_act_step_request.InvokeActStepRequest",
        ) -> dict[str, Any]:
            import capo_nova_act.types.invoke_act_step_request

            return capo_nova_act.types.invoke_act_step_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_nova_act.types.invoke_act_step_response.InvokeActStepResponse",
        ) -> dict[str, Any]:
            import capo_nova_act.types.invoke_act_step_response

            return capo_nova_act.types.invoke_act_step_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "InvokeActStep",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_nova_act.types.invoke_act_step_request.InvokeActStepRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
            "session_id": session_id,
            "act_id": act_id,
            "call_results": call_results,
        }
        if previous_step_id is not None:
            input_["previous_step_id"] = previous_step_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_act(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        session_id: "capo_nova_act.types.uuid_string.UuidString",
        act_id: "capo_nova_act.types.uuid_string.UuidString",
        status: "capo_nova_act.types.act_status.ActStatus",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        error: Optional["capo_nova_act.types.act_error.ActError"] = None,
    ) -> "capo_nova_act.types.update_act_response.UpdateActResponse":
        """<p>Updates an existing act's configuration, status, or error information.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the act.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the act.</p>
            session_id: <p>The unique identifier of the session containing the act.</p>
            act_id: <p>The unique identifier of the act to update.</p>
            status: <p>The new status to set for the act.</p>
            error: <p>Error information to associate with the act, if applicable.</p>

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
            req: "OperationRequest[capo_nova_act.types.update_act_request.UpdateActRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.update_act_response.UpdateActResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.update_act

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.update_act.update_act(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_nova_act.types.update_act_request.UpdateActRequest",
        ) -> dict[str, Any]:
            import capo_nova_act.types.update_act_request

            return capo_nova_act.types.update_act_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateAct", redact_input=_redact_input)
        )
        input_: capo_nova_act.types.update_act_request.UpdateActRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
            "session_id": session_id,
            "act_id": act_id,
            "status": status,
        }
        if error is not None:
            input_["error"] = error

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncActResource:
    def __init__(self, service: AsyncNovaActClient) -> None:
        self._service = service

    async def create(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        session_id: "capo_nova_act.types.uuid_string.UuidString",
        task: "capo_nova_act.types.task.Task",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        tool_specs: Optional["capo_nova_act.types.tool_specs.ToolSpecs"] = None,
        client_token: Optional["capo_nova_act.types.client_token.ClientToken"] = None,
    ) -> "capo_nova_act.types.create_act_response.CreateActResponse":
        """<p>Creates a new AI task (act) within a session that can interact with tools and perform specific actions.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the session.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the session.</p>
            session_id: <p>The unique identifier of the session to create the act in.</p>
            task: <p>The task description that defines what the act should accomplish.</p>
            tool_specs: <p>A list of tool specifications that the act can invoke to complete its task.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_nova_act.types.create_act_request.CreateActRequest]",
        ) -> AsyncOperationResponse[
            "capo_nova_act.types.create_act_response.CreateActResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.create_act

            (
                output,
                http_response,
            ) = await capo_nova_act._operations.amazon_nova_agents_data_plane.create_act.async_create_act(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_nova_act.types.create_act_request.CreateActRequest",
        ) -> dict[str, Any]:
            import capo_nova_act.types.create_act_request

            return capo_nova_act.types.create_act_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateAct", redact_input=_redact_input)
        )
        input_: capo_nova_act.types.create_act_request.CreateActRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
            "session_id": session_id,
            "task": task,
        }
        if tool_specs is not None:
            input_["tool_specs"] = tool_specs
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

    async def list(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        workflow_run_id: Optional["capo_nova_act.types.uuid_string.UuidString"] = None,
        session_id: Optional["capo_nova_act.types.uuid_string.UuidString"] = None,
        max_results: Optional["capo_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["capo_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "capo_nova_act.types.list_acts_response.ListActsResponse":
        """<p>Lists all acts within a specific session with their current status and execution details.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the session.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the session.</p>
            session_id: <p>The unique identifier of the session to list acts for.</p>
            max_results: <p>The maximum number of acts to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned acts (ascending or descending).</p>

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
            req: "AsyncOperationRequest[capo_nova_act.types.list_acts_request.ListActsRequest]",
        ) -> AsyncOperationResponse[
            "capo_nova_act.types.list_acts_response.ListActsResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.list_acts

            (
                output,
                http_response,
            ) = await capo_nova_act._operations.amazon_nova_agents_data_plane.list_acts.async_list_acts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListActs")
        )
        input_: capo_nova_act.types.list_acts_request.ListActsRequest = {
            "workflow_definition_name": workflow_definition_name
        }
        if workflow_run_id is not None:
            input_["workflow_run_id"] = workflow_run_id
        if session_id is not None:
            input_["session_id"] = session_id
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

    async def invoke_act_step(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        session_id: "capo_nova_act.types.uuid_string.UuidString",
        act_id: "capo_nova_act.types.uuid_string.UuidString",
        call_results: "capo_nova_act.types.call_results.CallResults",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        previous_step_id: Optional["capo_nova_act.types.uuid_string.UuidString"] = None,
    ) -> "capo_nova_act.types.invoke_act_step_response.InvokeActStepResponse":
        """<p>Executes the next step of an act, processing tool call results and returning new tool calls if needed.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the act.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the act.</p>
            session_id: <p>The unique identifier of the session containing the act.</p>
            act_id: <p>The unique identifier of the act to invoke the next step for.</p>
            call_results: <p>The results from previous tool calls that the act requested.</p>
            previous_step_id: <p>The identifier of the previous step, used for tracking execution flow.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_nova_act.types.invoke_act_step_request.InvokeActStepRequest]",
        ) -> AsyncOperationResponse[
            "capo_nova_act.types.invoke_act_step_response.InvokeActStepResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.invoke_act_step

            (
                output,
                http_response,
            ) = await capo_nova_act._operations.amazon_nova_agents_data_plane.invoke_act_step.async_invoke_act_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_nova_act.types.invoke_act_step_request.InvokeActStepRequest",
        ) -> dict[str, Any]:
            import capo_nova_act.types.invoke_act_step_request

            return capo_nova_act.types.invoke_act_step_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_nova_act.types.invoke_act_step_response.InvokeActStepResponse",
        ) -> dict[str, Any]:
            import capo_nova_act.types.invoke_act_step_response

            return capo_nova_act.types.invoke_act_step_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "InvokeActStep",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_nova_act.types.invoke_act_step_request.InvokeActStepRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
            "session_id": session_id,
            "act_id": act_id,
            "call_results": call_results,
        }
        if previous_step_id is not None:
            input_["previous_step_id"] = previous_step_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_act(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        session_id: "capo_nova_act.types.uuid_string.UuidString",
        act_id: "capo_nova_act.types.uuid_string.UuidString",
        status: "capo_nova_act.types.act_status.ActStatus",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        error: Optional["capo_nova_act.types.act_error.ActError"] = None,
    ) -> "capo_nova_act.types.update_act_response.UpdateActResponse":
        """<p>Updates an existing act's configuration, status, or error information.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the act.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the act.</p>
            session_id: <p>The unique identifier of the session containing the act.</p>
            act_id: <p>The unique identifier of the act to update.</p>
            status: <p>The new status to set for the act.</p>
            error: <p>Error information to associate with the act, if applicable.</p>

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
            req: "AsyncOperationRequest[capo_nova_act.types.update_act_request.UpdateActRequest]",
        ) -> AsyncOperationResponse[
            "capo_nova_act.types.update_act_response.UpdateActResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.update_act

            (
                output,
                http_response,
            ) = await capo_nova_act._operations.amazon_nova_agents_data_plane.update_act.async_update_act(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_nova_act.types.update_act_request.UpdateActRequest",
        ) -> dict[str, Any]:
            import capo_nova_act.types.update_act_request

            return capo_nova_act.types.update_act_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateAct", redact_input=_redact_input)
        )
        input_: capo_nova_act.types.update_act_request.UpdateActRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
            "session_id": session_id,
            "act_id": act_id,
            "status": status,
        }
        if error is not None:
            input_["error"] = error

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
