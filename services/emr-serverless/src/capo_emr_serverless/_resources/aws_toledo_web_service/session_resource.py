from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_emr_serverless._auth._signers
import capo_emr_serverless._auth._sigv4
from capo_emr_serverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_id
    import capo_emr_serverless.types.client_token
    import capo_emr_serverless.types.date
    import capo_emr_serverless.types.duration
    import capo_emr_serverless.types.get_session_endpoint_request
    import capo_emr_serverless.types.get_session_endpoint_response
    import capo_emr_serverless.types.get_session_request
    import capo_emr_serverless.types.get_session_response
    import capo_emr_serverless.types.iam_role_arn
    import capo_emr_serverless.types.list_sessions_request
    import capo_emr_serverless.types.list_sessions_response
    import capo_emr_serverless.types.next_token
    import capo_emr_serverless.types.session_configuration_overrides
    import capo_emr_serverless.types.session_id
    import capo_emr_serverless.types.session_state_set
    import capo_emr_serverless.types.session_summary
    import capo_emr_serverless.types.start_session_request
    import capo_emr_serverless.types.start_session_response
    import capo_emr_serverless.types.string256
    import capo_emr_serverless.types.tag_map
    import capo_emr_serverless.types.terminate_session_request
    import capo_emr_serverless.types.terminate_session_response
    from capo_emr_serverless._services.async_emr_serverless import (
        AsyncEMRServerlessClient,
        AsyncEMRServerlessClientConfig,
    )
    from capo_emr_serverless._services.emr_serverless import (
        EMRServerlessClient,
        EMRServerlessClientConfig,
    )


class SessionResource:
    def __init__(self, service: EMRServerlessClient) -> None:
        self._service = service

    def create(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        client_token: "capo_emr_serverless.types.client_token.ClientToken",
        execution_role_arn: "capo_emr_serverless.types.iam_role_arn.IAMRoleArn",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
        configuration_overrides: Optional[
            "capo_emr_serverless.types.session_configuration_overrides.SessionConfigurationOverrides"
        ] = None,
        tags: Optional["capo_emr_serverless.types.tag_map.TagMap"] = None,
        idle_timeout_minutes: Optional[
            "capo_emr_serverless.types.duration.Duration"
        ] = None,
        name: Optional["capo_emr_serverless.types.string256.String256"] = None,
    ) -> "capo_emr_serverless.types.start_session_response.StartSessionResponse":
        """<p>Creates and starts a new session on the specified application. The application must be in the <code>STARTED</code> state or have <code>AutoStart</code> enabled, and have interactive sessions enabled. This operation is supported for EMR release 7.13.0 and later.</p>

        Args:
            application_id: <p>The ID of the application on which to start the session.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token, the server returns the successful response without performing the operation again.</p>
            execution_role_arn: <p>The execution role ARN for the session. Amazon EMR Serverless uses this role to access Amazon Web Services resources on your behalf during session execution.</p>
            configuration_overrides: <p>The configuration overrides for the session. Only runtime configuration overrides are supported.</p>
            tags: <p>The tags to assign to the session.</p>
            idle_timeout_minutes: <p>The idle timeout in minutes for the session. After the session remains idle for this duration, Amazon EMR Serverless automatically terminates it.</p>
            name: <p>The optional name for the session.</p>

        Raises:
            capo_emr_serverless.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The maximum number of resources per account has been reached.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.start_session_request.StartSessionRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.start_session_response.StartSessionResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.start_session

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.start_session.start_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_emr_serverless.types.start_session_request.StartSessionRequest",
        ) -> dict[str, Any]:
            import capo_emr_serverless.types.start_session_request

            return capo_emr_serverless.types.start_session_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StartSession", redact_input=_redact_input),
        )
        input_: capo_emr_serverless.types.start_session_request.StartSessionRequest = {
            "application_id": application_id,
            "client_token": client_token,
            "execution_role_arn": execution_role_arn,
        }
        if configuration_overrides is not None:
            input_["configuration_overrides"] = configuration_overrides
        if tags is not None:
            input_["tags"] = tags
        if idle_timeout_minutes is not None:
            input_["idle_timeout_minutes"] = idle_timeout_minutes
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        session_id: "capo_emr_serverless.types.session_id.SessionId",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.get_session_response.GetSessionResponse":
        """<p>Displays detailed information about a session.</p>

        Args:
            application_id: <p>The ID of the application that the session belongs to.</p>
            session_id: <p>The ID of the session.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.get_session_request.GetSessionRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.get_session_response.GetSessionResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.get_session

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.get_session.get_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_emr_serverless.types.get_session_response.GetSessionResponse",
        ) -> dict[str, Any]:
            import capo_emr_serverless.types.get_session_response

            return capo_emr_serverless.types.get_session_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetSession", redact_output=_redact_output),
        )
        input_: capo_emr_serverless.types.get_session_request.GetSessionRequest = {
            "application_id": application_id,
            "session_id": session_id,
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
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        session_id: "capo_emr_serverless.types.session_id.SessionId",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
    ) -> (
        "capo_emr_serverless.types.terminate_session_response.TerminateSessionResponse"
    ):
        """<p>Terminates the specified session. After you terminate a session, it enters the <code>TERMINATING</code> state and then the <code>TERMINATED</code> state. You can still access the Spark History Server for a terminated session through the <code>GetResourceDashboard</code> operation.</p>

        Args:
            application_id: <p>The ID of the application that the session belongs to.</p>
            session_id: <p>The ID of the session to terminate.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.terminate_session_request.TerminateSessionRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.terminate_session_response.TerminateSessionResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.terminate_session

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.terminate_session.terminate_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("TerminateSession")
        )
        input_: capo_emr_serverless.types.terminate_session_request.TerminateSessionRequest = {
            "application_id": application_id,
            "session_id": session_id,
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
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
        next_token: Optional["capo_emr_serverless.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
        states: Optional[
            "capo_emr_serverless.types.session_state_set.SessionStateSet"
        ] = None,
        created_at_after: Optional["capo_emr_serverless.types.date.Date"] = None,
        created_at_before: Optional["capo_emr_serverless.types.date.Date"] = None,
    ) -> "capo_emr_serverless.types.list_sessions_response.ListSessionsResponse":
        """<p>Lists sessions for the specified application. You can filter sessions by state and creation time.</p>

        Args:
            application_id: <p>The ID of the application to list sessions for.</p>
            next_token: <p>The token for the next set of session results.</p>
            max_results: <p>The maximum number of sessions to return in each page of results.</p>
            states: <p>An optional filter for session states. Note that if this filter contains multiple states, the resulting list will be grouped by the state.</p>
            created_at_after: <p>The lower bound of the option to filter by creation date and time.</p>
            created_at_before: <p>The upper bound of the option to filter by creation date and time.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.list_sessions_request.ListSessionsRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.list_sessions_response.ListSessionsResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.list_sessions

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.list_sessions.list_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSessions")
        )
        input_: capo_emr_serverless.types.list_sessions_request.ListSessionsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if states is not None:
            input_["states"] = states
        if created_at_after is not None:
            input_["created_at_after"] = created_at_after
        if created_at_before is not None:
            input_["created_at_before"] = created_at_before

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_session_endpoint(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        session_id: "capo_emr_serverless.types.session_id.SessionId",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.get_session_endpoint_response.GetSessionEndpointResponse":
        """<p>Returns the session endpoint URL and a time-limited authentication token for the specified session. Use the endpoint and token to connect a client to the session. Call this operation again when the authentication token expires to obtain a new token.</p>

        Args:
            application_id: <p>The ID of the application that the session belongs to.</p>
            session_id: <p>The ID of the session.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.get_session_endpoint_request.GetSessionEndpointRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.get_session_endpoint_response.GetSessionEndpointResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.get_session_endpoint

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.get_session_endpoint.get_session_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_emr_serverless.types.get_session_endpoint_response.GetSessionEndpointResponse",
        ) -> dict[str, Any]:
            import capo_emr_serverless.types.get_session_endpoint_response

            return capo_emr_serverless.types.get_session_endpoint_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetSessionEndpoint", redact_output=_redact_output),
        )
        input_: capo_emr_serverless.types.get_session_endpoint_request.GetSessionEndpointRequest = {
            "application_id": application_id,
            "session_id": session_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncSessionResource:
    def __init__(self, service: AsyncEMRServerlessClient) -> None:
        self._service = service

    async def create(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        client_token: "capo_emr_serverless.types.client_token.ClientToken",
        execution_role_arn: "capo_emr_serverless.types.iam_role_arn.IAMRoleArn",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        configuration_overrides: Optional[
            "capo_emr_serverless.types.session_configuration_overrides.SessionConfigurationOverrides"
        ] = None,
        tags: Optional["capo_emr_serverless.types.tag_map.TagMap"] = None,
        idle_timeout_minutes: Optional[
            "capo_emr_serverless.types.duration.Duration"
        ] = None,
        name: Optional["capo_emr_serverless.types.string256.String256"] = None,
    ) -> "capo_emr_serverless.types.start_session_response.StartSessionResponse":
        """<p>Creates and starts a new session on the specified application. The application must be in the <code>STARTED</code> state or have <code>AutoStart</code> enabled, and have interactive sessions enabled. This operation is supported for EMR release 7.13.0 and later.</p>

        Args:
            application_id: <p>The ID of the application on which to start the session.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token, the server returns the successful response without performing the operation again.</p>
            execution_role_arn: <p>The execution role ARN for the session. Amazon EMR Serverless uses this role to access Amazon Web Services resources on your behalf during session execution.</p>
            configuration_overrides: <p>The configuration overrides for the session. Only runtime configuration overrides are supported.</p>
            tags: <p>The tags to assign to the session.</p>
            idle_timeout_minutes: <p>The idle timeout in minutes for the session. After the session remains idle for this duration, Amazon EMR Serverless automatically terminates it.</p>
            name: <p>The optional name for the session.</p>

        Raises:
            capo_emr_serverless.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The maximum number of resources per account has been reached.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.start_session_request.StartSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.start_session_response.StartSessionResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.start_session

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.start_session.async_start_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_emr_serverless.types.start_session_request.StartSessionRequest",
        ) -> dict[str, Any]:
            import capo_emr_serverless.types.start_session_request

            return capo_emr_serverless.types.start_session_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StartSession", redact_input=_redact_input),
        )
        input_: capo_emr_serverless.types.start_session_request.StartSessionRequest = {
            "application_id": application_id,
            "client_token": client_token,
            "execution_role_arn": execution_role_arn,
        }
        if configuration_overrides is not None:
            input_["configuration_overrides"] = configuration_overrides
        if tags is not None:
            input_["tags"] = tags
        if idle_timeout_minutes is not None:
            input_["idle_timeout_minutes"] = idle_timeout_minutes
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        session_id: "capo_emr_serverless.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.get_session_response.GetSessionResponse":
        """<p>Displays detailed information about a session.</p>

        Args:
            application_id: <p>The ID of the application that the session belongs to.</p>
            session_id: <p>The ID of the session.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.get_session_request.GetSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.get_session_response.GetSessionResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.get_session

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.get_session.async_get_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_emr_serverless.types.get_session_response.GetSessionResponse",
        ) -> dict[str, Any]:
            import capo_emr_serverless.types.get_session_response

            return capo_emr_serverless.types.get_session_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetSession", redact_output=_redact_output),
        )
        input_: capo_emr_serverless.types.get_session_request.GetSessionRequest = {
            "application_id": application_id,
            "session_id": session_id,
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
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        session_id: "capo_emr_serverless.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
    ) -> (
        "capo_emr_serverless.types.terminate_session_response.TerminateSessionResponse"
    ):
        """<p>Terminates the specified session. After you terminate a session, it enters the <code>TERMINATING</code> state and then the <code>TERMINATED</code> state. You can still access the Spark History Server for a terminated session through the <code>GetResourceDashboard</code> operation.</p>

        Args:
            application_id: <p>The ID of the application that the session belongs to.</p>
            session_id: <p>The ID of the session to terminate.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.terminate_session_request.TerminateSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.terminate_session_response.TerminateSessionResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.terminate_session

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.terminate_session.async_terminate_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("TerminateSession")
        )
        input_: capo_emr_serverless.types.terminate_session_request.TerminateSessionRequest = {
            "application_id": application_id,
            "session_id": session_id,
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
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        next_token: Optional["capo_emr_serverless.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
        states: Optional[
            "capo_emr_serverless.types.session_state_set.SessionStateSet"
        ] = None,
        created_at_after: Optional["capo_emr_serverless.types.date.Date"] = None,
        created_at_before: Optional["capo_emr_serverless.types.date.Date"] = None,
    ) -> "capo_emr_serverless.types.list_sessions_response.ListSessionsResponse":
        """<p>Lists sessions for the specified application. You can filter sessions by state and creation time.</p>

        Args:
            application_id: <p>The ID of the application to list sessions for.</p>
            next_token: <p>The token for the next set of session results.</p>
            max_results: <p>The maximum number of sessions to return in each page of results.</p>
            states: <p>An optional filter for session states. Note that if this filter contains multiple states, the resulting list will be grouped by the state.</p>
            created_at_after: <p>The lower bound of the option to filter by creation date and time.</p>
            created_at_before: <p>The upper bound of the option to filter by creation date and time.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.list_sessions_request.ListSessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.list_sessions_response.ListSessionsResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.list_sessions

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.list_sessions.async_list_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSessions")
        )
        input_: capo_emr_serverless.types.list_sessions_request.ListSessionsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if states is not None:
            input_["states"] = states
        if created_at_after is not None:
            input_["created_at_after"] = created_at_after
        if created_at_before is not None:
            input_["created_at_before"] = created_at_before

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_session_endpoint(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        session_id: "capo_emr_serverless.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
    ) -> "capo_emr_serverless.types.get_session_endpoint_response.GetSessionEndpointResponse":
        """<p>Returns the session endpoint URL and a time-limited authentication token for the specified session. Use the endpoint and token to connect a client to the session. Call this operation again when the authentication token expires to obtain a new token.</p>

        Args:
            application_id: <p>The ID of the application that the session belongs to.</p>
            session_id: <p>The ID of the session.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.get_session_endpoint_request.GetSessionEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.get_session_endpoint_response.GetSessionEndpointResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.get_session_endpoint

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.get_session_endpoint.async_get_session_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_emr_serverless.types.get_session_endpoint_response.GetSessionEndpointResponse",
        ) -> dict[str, Any]:
            import capo_emr_serverless.types.get_session_endpoint_response

            return capo_emr_serverless.types.get_session_endpoint_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetSessionEndpoint", redact_output=_redact_output),
        )
        input_: capo_emr_serverless.types.get_session_endpoint_request.GetSessionEndpointRequest = {
            "application_id": application_id,
            "session_id": session_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
