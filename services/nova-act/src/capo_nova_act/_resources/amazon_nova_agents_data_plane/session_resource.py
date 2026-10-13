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
    import capo_nova_act.types.client_token
    import capo_nova_act.types.create_session_request
    import capo_nova_act.types.create_session_response
    import capo_nova_act.types.list_sessions_request
    import capo_nova_act.types.list_sessions_response
    import capo_nova_act.types.max_results
    import capo_nova_act.types.next_token
    import capo_nova_act.types.session_summary
    import capo_nova_act.types.sort_order
    import capo_nova_act.types.uuid_string
    import capo_nova_act.types.workflow_definition_name
    from capo_nova_act._services.async_nova_act import (
        AsyncNovaActClient,
        AsyncNovaActClientConfig,
    )
    from capo_nova_act._services.nova_act import NovaActClient, NovaActClientConfig


class SessionResource:
    def __init__(self, service: NovaActClient) -> None:
        self._service = service

    def create(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        client_token: Optional["capo_nova_act.types.client_token.ClientToken"] = None,
    ) -> "capo_nova_act.types.create_session_response.CreateSessionResponse":
        """<p>Creates a new session context within a workflow run to manage conversation state and acts.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to create the session in.</p>
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
            req: "OperationRequest[capo_nova_act.types.create_session_request.CreateSessionRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.create_session_response.CreateSessionResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.create_session

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.create_session.create_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateSession")
        )
        input_: capo_nova_act.types.create_session_request.CreateSessionRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
        }
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
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        max_results: Optional["capo_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["capo_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "capo_nova_act.types.list_sessions_response.ListSessionsResponse":
        """<p>Lists all sessions within a specific workflow run.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to list sessions for.</p>
            max_results: <p>The maximum number of sessions to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned sessions (ascending or descending).</p>

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
            req: "OperationRequest[capo_nova_act.types.list_sessions_request.ListSessionsRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.list_sessions_response.ListSessionsResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.list_sessions

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.list_sessions.list_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSessions")
        )
        input_: capo_nova_act.types.list_sessions_request.ListSessionsRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
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


class AsyncSessionResource:
    def __init__(self, service: AsyncNovaActClient) -> None:
        self._service = service

    async def create(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        client_token: Optional["capo_nova_act.types.client_token.ClientToken"] = None,
    ) -> "capo_nova_act.types.create_session_response.CreateSessionResponse":
        """<p>Creates a new session context within a workflow run to manage conversation state and acts.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to create the session in.</p>
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
            req: "AsyncOperationRequest[capo_nova_act.types.create_session_request.CreateSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_nova_act.types.create_session_response.CreateSessionResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.create_session

            (
                output,
                http_response,
            ) = await capo_nova_act._operations.amazon_nova_agents_data_plane.create_session.async_create_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateSession")
        )
        input_: capo_nova_act.types.create_session_request.CreateSessionRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
        }
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
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        max_results: Optional["capo_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["capo_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "capo_nova_act.types.list_sessions_response.ListSessionsResponse":
        """<p>Lists all sessions within a specific workflow run.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to list sessions for.</p>
            max_results: <p>The maximum number of sessions to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned sessions (ascending or descending).</p>

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
            req: "AsyncOperationRequest[capo_nova_act.types.list_sessions_request.ListSessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_nova_act.types.list_sessions_response.ListSessionsResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.list_sessions

            (
                output,
                http_response,
            ) = await capo_nova_act._operations.amazon_nova_agents_data_plane.list_sessions.async_list_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSessions")
        )
        input_: capo_nova_act.types.list_sessions_request.ListSessionsRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
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
