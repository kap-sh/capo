from __future__ import annotations

import uuid
from collections.abc import AsyncGenerator, Generator
from contextlib import asynccontextmanager, contextmanager
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
    import capo_bedrock_agentcore.types.body
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.get_agent_card_request
    import capo_bedrock_agentcore.types.get_agent_card_response
    import capo_bedrock_agentcore.types.invoke_agent_runtime_command_request
    import capo_bedrock_agentcore.types.invoke_agent_runtime_command_request_body
    import capo_bedrock_agentcore.types.invoke_agent_runtime_command_response
    import capo_bedrock_agentcore.types.invoke_agent_runtime_request
    import capo_bedrock_agentcore.types.invoke_agent_runtime_response
    import capo_bedrock_agentcore.types.mime_type
    import capo_bedrock_agentcore.types.session_type
    import capo_bedrock_agentcore.types.stop_runtime_session_request
    import capo_bedrock_agentcore.types.stop_runtime_session_response
    import capo_bedrock_agentcore.types.string_type
    from capo_bedrock_agentcore._services.async_bedrock_agent_core import (
        AsyncBedrockAgentCoreClient,
        AsyncBedrockAgentCoreClientConfig,
    )
    from capo_bedrock_agentcore._services.bedrock_agent_core import (
        BedrockAgentCoreClient,
        BedrockAgentCoreClientConfig,
    )


class AgenticResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service

    def get_agent_card(
        self,
        agent_runtime_arn: str,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        runtime_session_id: Optional[
            "capo_bedrock_agentcore.types.session_type.SessionType"
        ] = None,
        qualifier: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.get_agent_card_response.GetAgentCardResponse":
        """<p>Retrieves the A2A agent card associated with an AgentCore Runtime agent.</p>

        Args:
            runtime_session_id: <p>The session ID that the AgentCore Runtime agent is using. </p>
            agent_runtime_arn: <p>The ARN of the AgentCore Runtime agent for which you want to get the A2A agent card.</p>
            qualifier: <p>Optional qualifier to specify an agent alias, such as <code>prod</code>code&gt; or <code>dev</code>. If you don't provide a value, the DEFAULT alias is used. </p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.retryable_conflict_exception.RetryableConflictException: <p>The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError: <p>The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_agent_card_request.GetAgentCardRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_agent_card_response.GetAgentCardResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_agent_card

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_agent_card.get_agent_card(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_agent_card_request.GetAgentCardRequest = {
            "agent_runtime_arn": agent_runtime_arn
        }
        if runtime_session_id is None:
            runtime_session_id = str(uuid.uuid4())
        input_["runtime_session_id"] = runtime_session_id
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def invoke_agent_runtime(
        self,
        agent_runtime_arn: str,
        payload: "capo_bedrock_agentcore.types.body.Body",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        content_type: Optional[
            "capo_bedrock_agentcore.types.mime_type.MimeType"
        ] = None,
        accept: Optional["capo_bedrock_agentcore.types.mime_type.MimeType"] = None,
        mcp_session_id: Optional[
            "capo_bedrock_agentcore.types.string_type.StringType"
        ] = None,
        runtime_session_id: Optional[
            "capo_bedrock_agentcore.types.session_type.SessionType"
        ] = None,
        mcp_protocol_version: Optional[
            "capo_bedrock_agentcore.types.string_type.StringType"
        ] = None,
        mcp_method: Optional[
            "capo_bedrock_agentcore.types.string_type.StringType"
        ] = None,
        mcp_name: Optional[
            "capo_bedrock_agentcore.types.string_type.StringType"
        ] = None,
        runtime_user_id: Optional[
            "capo_bedrock_agentcore.types.string_type.StringType"
        ] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        trace_state: Optional[str] = None,
        baggage: Optional[str] = None,
        qualifier: Optional[str] = None,
        account_id: Optional[str] = None,
    ) -> "Generator[capo_bedrock_agentcore.types.invoke_agent_runtime_response.InvokeAgentRuntimeResponse]":
        """<p>Sends a request to an agent or tool hosted in an Amazon Bedrock AgentCore Runtime and receives responses in real-time. </p> <p>To invoke an agent, you can specify either the AgentCore Runtime ARN or the agent ID with an account ID, and provide a payload containing your request. When you use the agent ID instead of the full ARN, you don't need to URL-encode the identifier. You can optionally specify a qualifier to target a specific endpoint of the agent.</p> <p>This operation supports streaming responses, allowing you to receive partial responses as they become available. We recommend using pagination to ensure that the operation returns quickly and successfully when processing large responses.</p> <p>For example code, see <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-invoke-agent.html">Invoke an AgentCore Runtime agent</a>. </p> <p>If you're integrating your agent with OAuth, you can't use the Amazon Web Services SDK to call <code>InvokeAgentRuntime</code>. Instead, make a HTTPS request to <code>InvokeAgentRuntime</code>. For an example, see <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html">Authenticate and authorize with Inbound Auth and Outbound Auth</a>.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:InvokeAgentRuntime</code> permission. If you are making a call to <code>InvokeAgentRuntime</code> on behalf of a user ID with the <code>X-Amzn-Bedrock-AgentCore-Runtime-User-Id</code> header, You require permissions to both actions (<code>bedrock-agentcore:InvokeAgentRuntime</code> and <code>bedrock-agentcore:InvokeAgentRuntimeForUser</code>). </p>

        Args:
            content_type: <p>The MIME type of the input data in the payload. This tells the agent runtime how to interpret the payload data. Common values include application/json for JSON data.</p>
            accept: <p>The desired MIME type for the response from the agent runtime. This tells the agent runtime what format to use for the response data. Common values include application/json for JSON data.</p>
            mcp_session_id: <p>The identifier of the MCP session.</p>
            runtime_session_id: <p>The identifier of the runtime session.</p>
            mcp_protocol_version: <p>The version of the MCP protocol being used.</p>
            mcp_method: <p>The MCP method being invoked. For example, <code>tools/call</code>, <code>resources/read</code>, or <code>prompts/get</code>.</p>
            mcp_name: <p>The name of the MCP resource, tool, or prompt being accessed. The value depends on the method:</p> <ul> <li> <p> <code>tools/call</code> – The tool name.</p> </li> <li> <p> <code>resources/read</code> – The resource URI.</p> </li> <li> <p> <code>prompts/get</code> – The prompt name.</p> </li> </ul>
            runtime_user_id: <p>The identifier of the runtime user.</p>
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            trace_state: <p>The trace state information for distributed tracing.</p>
            baggage: <p>Additional context information for distributed tracing.</p>
            agent_runtime_arn: <p>The identifier of the agent runtime to invoke. You can specify either the full Amazon Web Services Resource Name (ARN) or the agent ID. If you use the agent ID, you must also provide the <code>accountId</code> query parameter.</p>
            qualifier: <p>The qualifier to use for the agent runtime. This is an endpoint name that points to a specific version. If not specified, Amazon Bedrock AgentCore uses the default endpoint of the agent runtime.</p>
            account_id: <p>The identifier of the Amazon Web Services account for the agent runtime resource. This parameter is required when you specify an agent ID instead of the full ARN for <code>agentRuntimeArn</code>.</p>
            payload: <p>The input data to send to the agent runtime. The format of this data depends on the specific agent configuration and must match the specified content type. For most agents, this is a JSON object containing the user's request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.retryable_conflict_exception.RetryableConflictException: <p>The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError: <p>The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.invoke_agent_runtime_request.InvokeAgentRuntimeRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.invoke_agent_runtime_response.InvokeAgentRuntimeResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_agent_runtime

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_agent_runtime.invoke_agent_runtime(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.invoke_agent_runtime_request.InvokeAgentRuntimeRequest = {
            "agent_runtime_arn": agent_runtime_arn,
            "payload": payload,
        }
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if mcp_session_id is not None:
            input_["mcp_session_id"] = mcp_session_id
        if runtime_session_id is None:
            runtime_session_id = str(uuid.uuid4())
        input_["runtime_session_id"] = runtime_session_id
        if mcp_protocol_version is not None:
            input_["mcp_protocol_version"] = mcp_protocol_version
        if mcp_method is not None:
            input_["mcp_method"] = mcp_method
        if mcp_name is not None:
            input_["mcp_name"] = mcp_name
        if runtime_user_id is not None:
            input_["runtime_user_id"] = runtime_user_id
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
        if trace_state is not None:
            input_["trace_state"] = trace_state
        if baggage is not None:
            input_["baggage"] = baggage
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    @contextmanager
    def invoke_agent_runtime_command(
        self,
        agent_runtime_arn: str,
        body: "capo_bedrock_agentcore.types.invoke_agent_runtime_command_request_body.InvokeAgentRuntimeCommandRequestBody",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        content_type: Optional[
            "capo_bedrock_agentcore.types.mime_type.MimeType"
        ] = None,
        accept: Optional["capo_bedrock_agentcore.types.mime_type.MimeType"] = None,
        runtime_session_id: Optional[
            "capo_bedrock_agentcore.types.session_type.SessionType"
        ] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        trace_state: Optional[str] = None,
        baggage: Optional[str] = None,
        qualifier: Optional[str] = None,
        account_id: Optional[str] = None,
    ) -> "Generator[capo_bedrock_agentcore.types.invoke_agent_runtime_command_response.InvokeAgentRuntimeCommandResponse]":
        """<p>Executes a command in a runtime session container and streams the output back to the caller. This operation allows you to run shell commands within the agent runtime environment and receive real-time streaming responses including standard output and standard error.</p> <p>To invoke a command, you must specify the agent runtime ARN and a runtime session ID. The command execution supports streaming responses, allowing you to receive output as it becomes available through <code>contentStart</code>, <code>contentDelta</code>, and <code>contentStop</code> events.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:InvokeAgentRuntimeCommand</code> permission.</p>

        Args:
            content_type: <p>The MIME type of the input data in the request payload. This tells the agent runtime how to interpret the payload data. Common values include application/json for JSON data.</p>
            accept: <p>The desired MIME type for the response from the agent runtime command. This tells the agent runtime what format to use for the response data. Common values include application/json for JSON data.</p>
            runtime_session_id: <p>The unique identifier of the runtime session in which to execute the command. This session ID is used to maintain state and context across multiple command invocations.</p>
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            trace_state: <p>The trace state information for distributed tracing.</p>
            baggage: <p>Additional context information for distributed tracing.</p>
            agent_runtime_arn: <p>The Amazon Resource Name (ARN) of the agent runtime on which to execute the command. This identifies the specific agent runtime environment where the command will run.</p>
            qualifier: <p>The qualifier to use for the agent runtime. This is an endpoint name that points to a specific version. If not specified, Amazon Bedrock AgentCore uses the default endpoint of the agent runtime.</p>
            account_id: <p>The identifier of the Amazon Web Services account for the agent runtime resource. This parameter is required when you specify an agent ID instead of the full ARN for <code>agentRuntimeArn</code>.</p>
            body: <p>The request body containing the command to execute and optional configuration parameters such as timeout settings.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.retryable_conflict_exception.RetryableConflictException: <p>The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError: <p>The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.invoke_agent_runtime_command_request.InvokeAgentRuntimeCommandRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.invoke_agent_runtime_command_response.InvokeAgentRuntimeCommandResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_agent_runtime_command

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_agent_runtime_command.invoke_agent_runtime_command(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.invoke_agent_runtime_command_request.InvokeAgentRuntimeCommandRequest = {
            "agent_runtime_arn": agent_runtime_arn,
            "body": body,
        }
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if runtime_session_id is None:
            runtime_session_id = str(uuid.uuid4())
        input_["runtime_session_id"] = runtime_session_id
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
        if trace_state is not None:
            input_["trace_state"] = trace_state
        if baggage is not None:
            input_["baggage"] = baggage
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def stop_runtime_session(
        self,
        runtime_session_id: "capo_bedrock_agentcore.types.session_type.SessionType",
        agent_runtime_arn: str,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        qualifier: Optional[str] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.stop_runtime_session_response.StopRuntimeSessionResponse":
        """<p>Stops a session that is running in an running AgentCore Runtime agent.</p>

        Args:
            runtime_session_id: <p>The ID of the session that you want to stop.</p>
            agent_runtime_arn: <p>The ARN of the agent that contains the session that you want to stop.</p>
            qualifier: <p>Optional qualifier to specify an agent alias, such as <code>prod</code>code&gt; or <code>dev</code>. If you don't provide a value, the DEFAULT alias is used. </p>
            client_token: <p>Idempotent token used to identify the request. If you use the same token with multiple requests, the same response is returned. Use ClientToken to prevent the same request from being processed more than once.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.retryable_conflict_exception.RetryableConflictException: <p>The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError: <p>The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.stop_runtime_session_request.StopRuntimeSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.stop_runtime_session_response.StopRuntimeSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_runtime_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_runtime_session.stop_runtime_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.stop_runtime_session_request.StopRuntimeSessionRequest = {
            "runtime_session_id": runtime_session_id,
            "agent_runtime_arn": agent_runtime_arn,
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
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


class AsyncAgenticResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service

    async def get_agent_card(
        self,
        agent_runtime_arn: str,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        runtime_session_id: Optional[
            "capo_bedrock_agentcore.types.session_type.SessionType"
        ] = None,
        qualifier: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.get_agent_card_response.GetAgentCardResponse":
        """<p>Retrieves the A2A agent card associated with an AgentCore Runtime agent.</p>

        Args:
            runtime_session_id: <p>The session ID that the AgentCore Runtime agent is using. </p>
            agent_runtime_arn: <p>The ARN of the AgentCore Runtime agent for which you want to get the A2A agent card.</p>
            qualifier: <p>Optional qualifier to specify an agent alias, such as <code>prod</code>code&gt; or <code>dev</code>. If you don't provide a value, the DEFAULT alias is used. </p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.retryable_conflict_exception.RetryableConflictException: <p>The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError: <p>The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.get_agent_card_request.GetAgentCardRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.get_agent_card_response.GetAgentCardResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_agent_card

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_agent_card.async_get_agent_card(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_agent_card_request.GetAgentCardRequest = {
            "agent_runtime_arn": agent_runtime_arn
        }
        if runtime_session_id is None:
            runtime_session_id = str(uuid.uuid4())
        input_["runtime_session_id"] = runtime_session_id
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    @asynccontextmanager
    async def invoke_agent_runtime(
        self,
        agent_runtime_arn: str,
        payload: "capo_bedrock_agentcore.types.body.Body",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        content_type: Optional[
            "capo_bedrock_agentcore.types.mime_type.MimeType"
        ] = None,
        accept: Optional["capo_bedrock_agentcore.types.mime_type.MimeType"] = None,
        mcp_session_id: Optional[
            "capo_bedrock_agentcore.types.string_type.StringType"
        ] = None,
        runtime_session_id: Optional[
            "capo_bedrock_agentcore.types.session_type.SessionType"
        ] = None,
        mcp_protocol_version: Optional[
            "capo_bedrock_agentcore.types.string_type.StringType"
        ] = None,
        mcp_method: Optional[
            "capo_bedrock_agentcore.types.string_type.StringType"
        ] = None,
        mcp_name: Optional[
            "capo_bedrock_agentcore.types.string_type.StringType"
        ] = None,
        runtime_user_id: Optional[
            "capo_bedrock_agentcore.types.string_type.StringType"
        ] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        trace_state: Optional[str] = None,
        baggage: Optional[str] = None,
        qualifier: Optional[str] = None,
        account_id: Optional[str] = None,
    ) -> "AsyncGenerator[capo_bedrock_agentcore.types.invoke_agent_runtime_response.InvokeAgentRuntimeResponse]":
        """<p>Sends a request to an agent or tool hosted in an Amazon Bedrock AgentCore Runtime and receives responses in real-time. </p> <p>To invoke an agent, you can specify either the AgentCore Runtime ARN or the agent ID with an account ID, and provide a payload containing your request. When you use the agent ID instead of the full ARN, you don't need to URL-encode the identifier. You can optionally specify a qualifier to target a specific endpoint of the agent.</p> <p>This operation supports streaming responses, allowing you to receive partial responses as they become available. We recommend using pagination to ensure that the operation returns quickly and successfully when processing large responses.</p> <p>For example code, see <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-invoke-agent.html">Invoke an AgentCore Runtime agent</a>. </p> <p>If you're integrating your agent with OAuth, you can't use the Amazon Web Services SDK to call <code>InvokeAgentRuntime</code>. Instead, make a HTTPS request to <code>InvokeAgentRuntime</code>. For an example, see <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html">Authenticate and authorize with Inbound Auth and Outbound Auth</a>.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:InvokeAgentRuntime</code> permission. If you are making a call to <code>InvokeAgentRuntime</code> on behalf of a user ID with the <code>X-Amzn-Bedrock-AgentCore-Runtime-User-Id</code> header, You require permissions to both actions (<code>bedrock-agentcore:InvokeAgentRuntime</code> and <code>bedrock-agentcore:InvokeAgentRuntimeForUser</code>). </p>

        Args:
            content_type: <p>The MIME type of the input data in the payload. This tells the agent runtime how to interpret the payload data. Common values include application/json for JSON data.</p>
            accept: <p>The desired MIME type for the response from the agent runtime. This tells the agent runtime what format to use for the response data. Common values include application/json for JSON data.</p>
            mcp_session_id: <p>The identifier of the MCP session.</p>
            runtime_session_id: <p>The identifier of the runtime session.</p>
            mcp_protocol_version: <p>The version of the MCP protocol being used.</p>
            mcp_method: <p>The MCP method being invoked. For example, <code>tools/call</code>, <code>resources/read</code>, or <code>prompts/get</code>.</p>
            mcp_name: <p>The name of the MCP resource, tool, or prompt being accessed. The value depends on the method:</p> <ul> <li> <p> <code>tools/call</code> – The tool name.</p> </li> <li> <p> <code>resources/read</code> – The resource URI.</p> </li> <li> <p> <code>prompts/get</code> – The prompt name.</p> </li> </ul>
            runtime_user_id: <p>The identifier of the runtime user.</p>
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            trace_state: <p>The trace state information for distributed tracing.</p>
            baggage: <p>Additional context information for distributed tracing.</p>
            agent_runtime_arn: <p>The identifier of the agent runtime to invoke. You can specify either the full Amazon Web Services Resource Name (ARN) or the agent ID. If you use the agent ID, you must also provide the <code>accountId</code> query parameter.</p>
            qualifier: <p>The qualifier to use for the agent runtime. This is an endpoint name that points to a specific version. If not specified, Amazon Bedrock AgentCore uses the default endpoint of the agent runtime.</p>
            account_id: <p>The identifier of the Amazon Web Services account for the agent runtime resource. This parameter is required when you specify an agent ID instead of the full ARN for <code>agentRuntimeArn</code>.</p>
            payload: <p>The input data to send to the agent runtime. The format of this data depends on the specific agent configuration and must match the specified content type. For most agents, this is a JSON object containing the user's request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.retryable_conflict_exception.RetryableConflictException: <p>The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError: <p>The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.invoke_agent_runtime_request.InvokeAgentRuntimeRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.invoke_agent_runtime_response.InvokeAgentRuntimeResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_agent_runtime

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_agent_runtime.async_invoke_agent_runtime(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.invoke_agent_runtime_request.InvokeAgentRuntimeRequest = {
            "agent_runtime_arn": agent_runtime_arn,
            "payload": payload,
        }
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if mcp_session_id is not None:
            input_["mcp_session_id"] = mcp_session_id
        if runtime_session_id is None:
            runtime_session_id = str(uuid.uuid4())
        input_["runtime_session_id"] = runtime_session_id
        if mcp_protocol_version is not None:
            input_["mcp_protocol_version"] = mcp_protocol_version
        if mcp_method is not None:
            input_["mcp_method"] = mcp_method
        if mcp_name is not None:
            input_["mcp_name"] = mcp_name
        if runtime_user_id is not None:
            input_["runtime_user_id"] = runtime_user_id
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
        if trace_state is not None:
            input_["trace_state"] = trace_state
        if baggage is not None:
            input_["baggage"] = baggage
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    @asynccontextmanager
    async def invoke_agent_runtime_command(
        self,
        agent_runtime_arn: str,
        body: "capo_bedrock_agentcore.types.invoke_agent_runtime_command_request_body.InvokeAgentRuntimeCommandRequestBody",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        content_type: Optional[
            "capo_bedrock_agentcore.types.mime_type.MimeType"
        ] = None,
        accept: Optional["capo_bedrock_agentcore.types.mime_type.MimeType"] = None,
        runtime_session_id: Optional[
            "capo_bedrock_agentcore.types.session_type.SessionType"
        ] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        trace_state: Optional[str] = None,
        baggage: Optional[str] = None,
        qualifier: Optional[str] = None,
        account_id: Optional[str] = None,
    ) -> "AsyncGenerator[capo_bedrock_agentcore.types.invoke_agent_runtime_command_response.InvokeAgentRuntimeCommandResponse]":
        """<p>Executes a command in a runtime session container and streams the output back to the caller. This operation allows you to run shell commands within the agent runtime environment and receive real-time streaming responses including standard output and standard error.</p> <p>To invoke a command, you must specify the agent runtime ARN and a runtime session ID. The command execution supports streaming responses, allowing you to receive output as it becomes available through <code>contentStart</code>, <code>contentDelta</code>, and <code>contentStop</code> events.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:InvokeAgentRuntimeCommand</code> permission.</p>

        Args:
            content_type: <p>The MIME type of the input data in the request payload. This tells the agent runtime how to interpret the payload data. Common values include application/json for JSON data.</p>
            accept: <p>The desired MIME type for the response from the agent runtime command. This tells the agent runtime what format to use for the response data. Common values include application/json for JSON data.</p>
            runtime_session_id: <p>The unique identifier of the runtime session in which to execute the command. This session ID is used to maintain state and context across multiple command invocations.</p>
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            trace_state: <p>The trace state information for distributed tracing.</p>
            baggage: <p>Additional context information for distributed tracing.</p>
            agent_runtime_arn: <p>The Amazon Resource Name (ARN) of the agent runtime on which to execute the command. This identifies the specific agent runtime environment where the command will run.</p>
            qualifier: <p>The qualifier to use for the agent runtime. This is an endpoint name that points to a specific version. If not specified, Amazon Bedrock AgentCore uses the default endpoint of the agent runtime.</p>
            account_id: <p>The identifier of the Amazon Web Services account for the agent runtime resource. This parameter is required when you specify an agent ID instead of the full ARN for <code>agentRuntimeArn</code>.</p>
            body: <p>The request body containing the command to execute and optional configuration parameters such as timeout settings.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.retryable_conflict_exception.RetryableConflictException: <p>The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError: <p>The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.invoke_agent_runtime_command_request.InvokeAgentRuntimeCommandRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.invoke_agent_runtime_command_response.InvokeAgentRuntimeCommandResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_agent_runtime_command

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_agent_runtime_command.async_invoke_agent_runtime_command(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.invoke_agent_runtime_command_request.InvokeAgentRuntimeCommandRequest = {
            "agent_runtime_arn": agent_runtime_arn,
            "body": body,
        }
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if runtime_session_id is None:
            runtime_session_id = str(uuid.uuid4())
        input_["runtime_session_id"] = runtime_session_id
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
        if trace_state is not None:
            input_["trace_state"] = trace_state
        if baggage is not None:
            input_["baggage"] = baggage
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def stop_runtime_session(
        self,
        runtime_session_id: "capo_bedrock_agentcore.types.session_type.SessionType",
        agent_runtime_arn: str,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        qualifier: Optional[str] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.stop_runtime_session_response.StopRuntimeSessionResponse":
        """<p>Stops a session that is running in an running AgentCore Runtime agent.</p>

        Args:
            runtime_session_id: <p>The ID of the session that you want to stop.</p>
            agent_runtime_arn: <p>The ARN of the agent that contains the session that you want to stop.</p>
            qualifier: <p>Optional qualifier to specify an agent alias, such as <code>prod</code>code&gt; or <code>dev</code>. If you don't provide a value, the DEFAULT alias is used. </p>
            client_token: <p>Idempotent token used to identify the request. If you use the same token with multiple requests, the same response is returned. Use ClientToken to prevent the same request from being processed more than once.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.retryable_conflict_exception.RetryableConflictException: <p>The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError: <p>The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.stop_runtime_session_request.StopRuntimeSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.stop_runtime_session_response.StopRuntimeSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_runtime_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_runtime_session.async_stop_runtime_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.stop_runtime_session_request.StopRuntimeSessionRequest = {
            "runtime_session_id": runtime_session_id,
            "agent_runtime_arn": agent_runtime_arn,
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
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
