from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_bedrock_agentcore._auth._signers
import capo_bedrock_agentcore._auth._sigv4
from capo_bedrock_agentcore._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.certificates
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.code_interpreter_session_id
    import capo_bedrock_agentcore.types.code_interpreter_session_status
    import capo_bedrock_agentcore.types.code_interpreter_session_timeout
    import capo_bedrock_agentcore.types.get_code_interpreter_session_request
    import capo_bedrock_agentcore.types.get_code_interpreter_session_response
    import capo_bedrock_agentcore.types.list_code_interpreter_sessions_request
    import capo_bedrock_agentcore.types.list_code_interpreter_sessions_response
    import capo_bedrock_agentcore.types.max_results
    import capo_bedrock_agentcore.types.name
    import capo_bedrock_agentcore.types.next_token
    import capo_bedrock_agentcore.types.start_code_interpreter_session_request
    import capo_bedrock_agentcore.types.start_code_interpreter_session_response
    import capo_bedrock_agentcore.types.stop_code_interpreter_session_request
    import capo_bedrock_agentcore.types.stop_code_interpreter_session_response
    import capo_bedrock_agentcore.types.tools_file_system_configurations
    from capo_bedrock_agentcore._services.async_bedrock_agent_core import (
        AsyncBedrockAgentCoreClient,
        AsyncBedrockAgentCoreClientConfig,
    )
    from capo_bedrock_agentcore._services.bedrock_agent_core import (
        BedrockAgentCoreClient,
        BedrockAgentCoreClientConfig,
    )


class CodeInterpreterSessionResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service

    def read(
        self,
        code_interpreter_identifier: str,
        session_id: "capo_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_code_interpreter_session_response.GetCodeInterpreterSessionResponse":
        """<p>Retrieves detailed information about a specific code interpreter session in Amazon Bedrock AgentCore. This operation returns the session's configuration, current status, and metadata.</p> <p>To get a code interpreter session, you must specify both the code interpreter identifier and the session ID. The response includes information about the session's timeout settings and current status.</p> <p>The following operations are related to <code>GetCodeInterpreterSession</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html">StartCodeInterpreterSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListCodeInterpreterSessions.html">ListCodeInterpreterSessions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopCodeInterpreterSession.html">StopCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            code_interpreter_identifier: <p>The unique identifier of the code interpreter associated with the session.</p>
            session_id: <p>The unique identifier of the code interpreter session to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_code_interpreter_session_request.GetCodeInterpreterSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_code_interpreter_session_response.GetCodeInterpreterSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_code_interpreter_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_code_interpreter_session.get_code_interpreter_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_code_interpreter_session_request.GetCodeInterpreterSessionRequest = {
            "code_interpreter_identifier": code_interpreter_identifier,
            "session_id": session_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_code_interpreter_sessions(
        self,
        code_interpreter_identifier: str,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_bedrock_agentcore.types.code_interpreter_session_status.CodeInterpreterSessionStatus"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_code_interpreter_sessions_response.ListCodeInterpreterSessionsResponse":
        """<p>Retrieves a list of code interpreter sessions in Amazon Bedrock AgentCore that match the specified criteria. This operation returns summary information about each session, including identifiers, status, and timestamps.</p> <p>You can filter the results by code interpreter identifier and session status. The operation supports pagination to handle large result sets efficiently.</p> <p>We recommend using pagination to ensure that the operation returns quickly and successfully when retrieving large numbers of sessions.</p> <p>The following operations are related to <code>ListCodeInterpreterSessions</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html">StartCodeInterpreterSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html">GetCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            code_interpreter_identifier: <p>The unique identifier of the code interpreter to list sessions for. If specified, only sessions for this code interpreter are returned. If not specified, sessions for all code interpreters are returned.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 10. Valid values range from 1 to 100. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. If not specified, Amazon Bedrock AgentCore returns the first page of results.</p>
            status: <p>The status of the code interpreter sessions to list. Valid values include ACTIVE, STOPPING, and STOPPED. If not specified, sessions with any status are returned.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_code_interpreter_sessions_request.ListCodeInterpreterSessionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_code_interpreter_sessions_response.ListCodeInterpreterSessionsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_code_interpreter_sessions

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_code_interpreter_sessions.list_code_interpreter_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.list_code_interpreter_sessions_request.ListCodeInterpreterSessionsRequest = {
            "code_interpreter_identifier": code_interpreter_identifier
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_code_interpreter_session(
        self,
        code_interpreter_identifier: str,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        name: Optional["capo_bedrock_agentcore.types.name.Name"] = None,
        session_timeout_seconds: Optional[
            "capo_bedrock_agentcore.types.code_interpreter_session_timeout.CodeInterpreterSessionTimeout"
        ] = None,
        certificates: Optional[
            "capo_bedrock_agentcore.types.certificates.Certificates"
        ] = None,
        filesystem_configurations: Optional[
            "capo_bedrock_agentcore.types.tools_file_system_configurations.ToolsFileSystemConfigurations"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.start_code_interpreter_session_response.StartCodeInterpreterSessionResponse":
        """<p>Creates and initializes a code interpreter session in Amazon Bedrock AgentCore. The session enables agents to execute code as part of their response generation, supporting programming languages such as Python for data analysis, visualization, and computation tasks.</p> <p>To create a session, you must specify a code interpreter identifier and a name. The session remains active until it times out or you explicitly stop it using the <code>StopCodeInterpreterSession</code> operation.</p> <p>The following operations are related to <code>StartCodeInterpreterSession</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeCodeInterpreter.html">InvokeCodeInterpreter</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html">GetCodeInterpreterSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopCodeInterpreterSession.html">StopCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            code_interpreter_identifier: <p>The unique identifier of the code interpreter to use for this session. This identifier specifies which code interpreter environment to initialize for the session.</p>
            name: <p>The name of the code interpreter session. This name helps you identify and manage the session. The name does not need to be unique.</p>
            session_timeout_seconds: <p>The duration in seconds (time-to-live) after which the session automatically terminates, regardless of ongoing activity. Defaults to 900 seconds (15 minutes). Recommended minimum: 60 seconds. Maximum allowed: 28,800 seconds (8 hours).</p>
            certificates: <p>A list of certificates to install in the code interpreter session.</p>
            filesystem_configurations: <p>The file system configurations to mount into the code interpreter session. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your session can then read and write your data. If you don't specify this field, no additional file systems are mounted.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error. This parameter helps prevent the creation of duplicate sessions if there are temporary network issues.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.start_code_interpreter_session_request.StartCodeInterpreterSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.start_code_interpreter_session_response.StartCodeInterpreterSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_code_interpreter_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_code_interpreter_session.start_code_interpreter_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.start_code_interpreter_session_request.StartCodeInterpreterSessionRequest = {
            "code_interpreter_identifier": code_interpreter_identifier
        }
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
        if name is not None:
            input_["name"] = name
        if session_timeout_seconds is not None:
            input_["session_timeout_seconds"] = session_timeout_seconds
        if certificates is not None:
            input_["certificates"] = certificates
        if filesystem_configurations is not None:
            input_["filesystem_configurations"] = filesystem_configurations
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

    def stop_code_interpreter_session(
        self,
        code_interpreter_identifier: str,
        session_id: "capo_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.stop_code_interpreter_session_response.StopCodeInterpreterSessionResponse":
        """<p>Terminates an active code interpreter session in Amazon Bedrock AgentCore. This operation stops the session, releases associated resources, and makes the session unavailable for further use.</p> <p>To stop a code interpreter session, you must specify both the code interpreter identifier and the session ID. Once stopped, a session cannot be restarted; you must create a new session using <code>StartCodeInterpreterSession</code>.</p> <p>The following operations are related to <code>StopCodeInterpreterSession</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html">StartCodeInterpreterSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html">GetCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            code_interpreter_identifier: <p>The unique identifier of the code interpreter associated with the session.</p>
            session_id: <p>The unique identifier of the code interpreter session to stop.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.stop_code_interpreter_session_request.StopCodeInterpreterSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.stop_code_interpreter_session_response.StopCodeInterpreterSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_code_interpreter_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_code_interpreter_session.stop_code_interpreter_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.stop_code_interpreter_session_request.StopCodeInterpreterSessionRequest = {
            "code_interpreter_identifier": code_interpreter_identifier,
            "session_id": session_id,
        }
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
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


class AsyncCodeInterpreterSessionResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service

    async def read(
        self,
        code_interpreter_identifier: str,
        session_id: "capo_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_code_interpreter_session_response.GetCodeInterpreterSessionResponse":
        """<p>Retrieves detailed information about a specific code interpreter session in Amazon Bedrock AgentCore. This operation returns the session's configuration, current status, and metadata.</p> <p>To get a code interpreter session, you must specify both the code interpreter identifier and the session ID. The response includes information about the session's timeout settings and current status.</p> <p>The following operations are related to <code>GetCodeInterpreterSession</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html">StartCodeInterpreterSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListCodeInterpreterSessions.html">ListCodeInterpreterSessions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopCodeInterpreterSession.html">StopCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            code_interpreter_identifier: <p>The unique identifier of the code interpreter associated with the session.</p>
            session_id: <p>The unique identifier of the code interpreter session to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.get_code_interpreter_session_request.GetCodeInterpreterSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.get_code_interpreter_session_response.GetCodeInterpreterSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_code_interpreter_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_code_interpreter_session.async_get_code_interpreter_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_code_interpreter_session_request.GetCodeInterpreterSessionRequest = {
            "code_interpreter_identifier": code_interpreter_identifier,
            "session_id": session_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_code_interpreter_sessions(
        self,
        code_interpreter_identifier: str,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_bedrock_agentcore.types.code_interpreter_session_status.CodeInterpreterSessionStatus"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_code_interpreter_sessions_response.ListCodeInterpreterSessionsResponse":
        """<p>Retrieves a list of code interpreter sessions in Amazon Bedrock AgentCore that match the specified criteria. This operation returns summary information about each session, including identifiers, status, and timestamps.</p> <p>You can filter the results by code interpreter identifier and session status. The operation supports pagination to handle large result sets efficiently.</p> <p>We recommend using pagination to ensure that the operation returns quickly and successfully when retrieving large numbers of sessions.</p> <p>The following operations are related to <code>ListCodeInterpreterSessions</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html">StartCodeInterpreterSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html">GetCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            code_interpreter_identifier: <p>The unique identifier of the code interpreter to list sessions for. If specified, only sessions for this code interpreter are returned. If not specified, sessions for all code interpreters are returned.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 10. Valid values range from 1 to 100. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. If not specified, Amazon Bedrock AgentCore returns the first page of results.</p>
            status: <p>The status of the code interpreter sessions to list. Valid values include ACTIVE, STOPPING, and STOPPED. If not specified, sessions with any status are returned.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.list_code_interpreter_sessions_request.ListCodeInterpreterSessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.list_code_interpreter_sessions_response.ListCodeInterpreterSessionsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_code_interpreter_sessions

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_code_interpreter_sessions.async_list_code_interpreter_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.list_code_interpreter_sessions_request.ListCodeInterpreterSessionsRequest = {
            "code_interpreter_identifier": code_interpreter_identifier
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_code_interpreter_session(
        self,
        code_interpreter_identifier: str,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        name: Optional["capo_bedrock_agentcore.types.name.Name"] = None,
        session_timeout_seconds: Optional[
            "capo_bedrock_agentcore.types.code_interpreter_session_timeout.CodeInterpreterSessionTimeout"
        ] = None,
        certificates: Optional[
            "capo_bedrock_agentcore.types.certificates.Certificates"
        ] = None,
        filesystem_configurations: Optional[
            "capo_bedrock_agentcore.types.tools_file_system_configurations.ToolsFileSystemConfigurations"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.start_code_interpreter_session_response.StartCodeInterpreterSessionResponse":
        """<p>Creates and initializes a code interpreter session in Amazon Bedrock AgentCore. The session enables agents to execute code as part of their response generation, supporting programming languages such as Python for data analysis, visualization, and computation tasks.</p> <p>To create a session, you must specify a code interpreter identifier and a name. The session remains active until it times out or you explicitly stop it using the <code>StopCodeInterpreterSession</code> operation.</p> <p>The following operations are related to <code>StartCodeInterpreterSession</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeCodeInterpreter.html">InvokeCodeInterpreter</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html">GetCodeInterpreterSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopCodeInterpreterSession.html">StopCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            code_interpreter_identifier: <p>The unique identifier of the code interpreter to use for this session. This identifier specifies which code interpreter environment to initialize for the session.</p>
            name: <p>The name of the code interpreter session. This name helps you identify and manage the session. The name does not need to be unique.</p>
            session_timeout_seconds: <p>The duration in seconds (time-to-live) after which the session automatically terminates, regardless of ongoing activity. Defaults to 900 seconds (15 minutes). Recommended minimum: 60 seconds. Maximum allowed: 28,800 seconds (8 hours).</p>
            certificates: <p>A list of certificates to install in the code interpreter session.</p>
            filesystem_configurations: <p>The file system configurations to mount into the code interpreter session. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your session can then read and write your data. If you don't specify this field, no additional file systems are mounted.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error. This parameter helps prevent the creation of duplicate sessions if there are temporary network issues.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.start_code_interpreter_session_request.StartCodeInterpreterSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.start_code_interpreter_session_response.StartCodeInterpreterSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_code_interpreter_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_code_interpreter_session.async_start_code_interpreter_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.start_code_interpreter_session_request.StartCodeInterpreterSessionRequest = {
            "code_interpreter_identifier": code_interpreter_identifier
        }
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
        if name is not None:
            input_["name"] = name
        if session_timeout_seconds is not None:
            input_["session_timeout_seconds"] = session_timeout_seconds
        if certificates is not None:
            input_["certificates"] = certificates
        if filesystem_configurations is not None:
            input_["filesystem_configurations"] = filesystem_configurations
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

    async def stop_code_interpreter_session(
        self,
        code_interpreter_identifier: str,
        session_id: "capo_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.stop_code_interpreter_session_response.StopCodeInterpreterSessionResponse":
        """<p>Terminates an active code interpreter session in Amazon Bedrock AgentCore. This operation stops the session, releases associated resources, and makes the session unavailable for further use.</p> <p>To stop a code interpreter session, you must specify both the code interpreter identifier and the session ID. Once stopped, a session cannot be restarted; you must create a new session using <code>StartCodeInterpreterSession</code>.</p> <p>The following operations are related to <code>StopCodeInterpreterSession</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html">StartCodeInterpreterSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html">GetCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            code_interpreter_identifier: <p>The unique identifier of the code interpreter associated with the session.</p>
            session_id: <p>The unique identifier of the code interpreter session to stop.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.stop_code_interpreter_session_request.StopCodeInterpreterSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.stop_code_interpreter_session_response.StopCodeInterpreterSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_code_interpreter_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_code_interpreter_session.async_stop_code_interpreter_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.stop_code_interpreter_session_request.StopCodeInterpreterSessionRequest = {
            "code_interpreter_identifier": code_interpreter_identifier,
            "session_id": session_id,
        }
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
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
