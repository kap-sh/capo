from __future__ import annotations

from collections.abc import AsyncGenerator, Generator
from contextlib import asynccontextmanager, contextmanager
from typing import TYPE_CHECKING, Optional

import capo_bedrock_agent_runtime._auth._signers
import capo_bedrock_agent_runtime._auth._sigv4
from capo_bedrock_agent_runtime._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agent_alias_id
    import capo_bedrock_agent_runtime.types.agent_id
    import capo_bedrock_agent_runtime.types.aws_resource_arn
    import capo_bedrock_agent_runtime.types.bedrock_model_configurations
    import capo_bedrock_agent_runtime.types.input_text
    import capo_bedrock_agent_runtime.types.invoke_agent_request
    import capo_bedrock_agent_runtime.types.invoke_agent_response
    import capo_bedrock_agent_runtime.types.memory_id
    import capo_bedrock_agent_runtime.types.prompt_creation_configurations
    import capo_bedrock_agent_runtime.types.session_id
    import capo_bedrock_agent_runtime.types.session_state
    import capo_bedrock_agent_runtime.types.streaming_configurations
    from capo_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from capo_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class InferenceResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    @contextmanager
    def invoke_agent(
        self,
        agent_id: "capo_bedrock_agent_runtime.types.agent_id.AgentId",
        agent_alias_id: "capo_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId",
        session_id: "capo_bedrock_agent_runtime.types.session_id.SessionId",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        session_state: Optional[
            "capo_bedrock_agent_runtime.types.session_state.SessionState"
        ] = None,
        end_session: Optional[bool] = None,
        enable_trace: Optional[bool] = None,
        input_text: Optional[
            "capo_bedrock_agent_runtime.types.input_text.InputText"
        ] = None,
        memory_id: Optional[
            "capo_bedrock_agent_runtime.types.memory_id.MemoryId"
        ] = None,
        bedrock_model_configurations: Optional[
            "capo_bedrock_agent_runtime.types.bedrock_model_configurations.BedrockModelConfigurations"
        ] = None,
        streaming_configurations: Optional[
            "capo_bedrock_agent_runtime.types.streaming_configurations.StreamingConfigurations"
        ] = None,
        prompt_creation_configurations: Optional[
            "capo_bedrock_agent_runtime.types.prompt_creation_configurations.PromptCreationConfigurations"
        ] = None,
        source_arn: Optional[
            "capo_bedrock_agent_runtime.types.aws_resource_arn.AWSResourceARN"
        ] = None,
    ) -> "Generator[capo_bedrock_agent_runtime.types.invoke_agent_response.InvokeAgentResponse]":
        """<note> <p>Amazon Bedrock Agents (now Amazon Bedrock Agents Classic) is no longer open to new customers. For capabilities similar to Bedrock Agents Classic, explore Amazon Bedrock AgentCore. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html">Amazon Bedrock Agents Classic availability change</a>.</p> </note> <note> </note> <p>Sends a prompt for the agent to process and respond to. Note the following fields for the request:</p> <ul> <li> <p>To continue the same conversation with an agent, use the same <code>sessionId</code> value in the request.</p> </li> <li> <p>To activate trace enablement, turn <code>enableTrace</code> to <code>true</code>. Trace enablement helps you follow the agent's reasoning process that led it to the information it processed, the actions it took, and the final result it yielded. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html#trace-events">Trace enablement</a>.</p> </li> <li> <p>End a conversation by setting <code>endSession</code> to <code>true</code>.</p> </li> <li> <p>In the <code>sessionState</code> object, you can include attributes for the session or prompt or, if you configured an action group to return control, results from invocation of the action group.</p> </li> </ul> <p>The response contains both <b>chunk</b> and <b>trace</b> attributes.</p> <p>The final response is returned in the <code>bytes</code> field of the <code>chunk</code> object. The <code>InvokeAgent</code> returns one chunk for the entire interaction.</p> <ul> <li> <p>The <code>attribution</code> object contains citations for parts of the response.</p> </li> <li> <p>If you set <code>enableTrace</code> to <code>true</code> in the request, you can trace the agent's steps and reasoning process that led it to the response.</p> </li> <li> <p>If the action predicted was configured to return control, the response returns parameters for the action, elicited from the user, in the <code>returnControl</code> field.</p> </li> <li> <p>Errors are also surfaced in the response.</p> </li> </ul>

        Args:
            session_state: <p>Contains parameters that specify various attributes of the session. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html">Control session context</a>.</p> <note> <p>If you include <code>returnControlInvocationResults</code> in the <code>sessionState</code> field, the <code>inputText</code> field will be ignored.</p> </note>
            agent_id: <p>The unique identifier of the agent to use.</p>
            agent_alias_id: <p>The alias of the agent to use.</p>
            session_id: <p>The unique identifier of the session. Use the same value across requests to continue the same conversation.</p>
            end_session: <p>Specifies whether to end the session with the agent or not.</p>
            enable_trace: <p>Specifies whether to turn on the trace or not to track the agent's reasoning process. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html#trace-events">Trace enablement</a>.</p>
            input_text: <p>The prompt text to send the agent.</p> <note> <p>If you include <code>returnControlInvocationResults</code> in the <code>sessionState</code> field, the <code>inputText</code> field will be ignored.</p> </note>
            memory_id: <p>The unique identifier of the agent memory.</p>
            bedrock_model_configurations: <p>Model performance settings for the request.</p>
            streaming_configurations: <p> Specifies the configurations for streaming. </p> <note> <p>To use agent streaming, you need permissions to perform the <code>bedrock:InvokeModelWithResponseStream</code> action.</p> </note>
            prompt_creation_configurations: <p>Specifies parameters that control how the service populates the agent prompt for an <code>InvokeAgent</code> request. You can control which aspects of previous invocations in the same agent session the service uses to populate the agent prompt. This gives you more granular control over the contextual history that is used to process the current request.</p>
            source_arn: <p>The ARN of the resource making the request.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p> The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see <a href="https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html">Retry behavior</a> in the <i>AWS SDKs and Tools</i> reference guide. </p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent_runtime.types.invoke_agent_request.InvokeAgentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.invoke_agent_response.InvokeAgentResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_agent

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_agent.invoke_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.invoke_agent_request.InvokeAgentRequest = {
            "agent_id": agent_id,
            "agent_alias_id": agent_alias_id,
            "session_id": session_id,
        }
        if session_state is not None:
            input_["session_state"] = session_state
        if end_session is not None:
            input_["end_session"] = end_session
        if enable_trace is not None:
            input_["enable_trace"] = enable_trace
        if input_text is not None:
            input_["input_text"] = input_text
        if memory_id is not None:
            input_["memory_id"] = memory_id
        if bedrock_model_configurations is not None:
            input_["bedrock_model_configurations"] = bedrock_model_configurations
        if streaming_configurations is not None:
            input_["streaming_configurations"] = streaming_configurations
        if prompt_creation_configurations is not None:
            input_["prompt_creation_configurations"] = prompt_creation_configurations
        if source_arn is not None:
            input_["source_arn"] = source_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()


class AsyncInferenceResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    @asynccontextmanager
    async def invoke_agent(
        self,
        agent_id: "capo_bedrock_agent_runtime.types.agent_id.AgentId",
        agent_alias_id: "capo_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId",
        session_id: "capo_bedrock_agent_runtime.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        session_state: Optional[
            "capo_bedrock_agent_runtime.types.session_state.SessionState"
        ] = None,
        end_session: Optional[bool] = None,
        enable_trace: Optional[bool] = None,
        input_text: Optional[
            "capo_bedrock_agent_runtime.types.input_text.InputText"
        ] = None,
        memory_id: Optional[
            "capo_bedrock_agent_runtime.types.memory_id.MemoryId"
        ] = None,
        bedrock_model_configurations: Optional[
            "capo_bedrock_agent_runtime.types.bedrock_model_configurations.BedrockModelConfigurations"
        ] = None,
        streaming_configurations: Optional[
            "capo_bedrock_agent_runtime.types.streaming_configurations.StreamingConfigurations"
        ] = None,
        prompt_creation_configurations: Optional[
            "capo_bedrock_agent_runtime.types.prompt_creation_configurations.PromptCreationConfigurations"
        ] = None,
        source_arn: Optional[
            "capo_bedrock_agent_runtime.types.aws_resource_arn.AWSResourceARN"
        ] = None,
    ) -> "AsyncGenerator[capo_bedrock_agent_runtime.types.invoke_agent_response.InvokeAgentResponse]":
        """<note> <p>Amazon Bedrock Agents (now Amazon Bedrock Agents Classic) is no longer open to new customers. For capabilities similar to Bedrock Agents Classic, explore Amazon Bedrock AgentCore. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html">Amazon Bedrock Agents Classic availability change</a>.</p> </note> <note> </note> <p>Sends a prompt for the agent to process and respond to. Note the following fields for the request:</p> <ul> <li> <p>To continue the same conversation with an agent, use the same <code>sessionId</code> value in the request.</p> </li> <li> <p>To activate trace enablement, turn <code>enableTrace</code> to <code>true</code>. Trace enablement helps you follow the agent's reasoning process that led it to the information it processed, the actions it took, and the final result it yielded. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html#trace-events">Trace enablement</a>.</p> </li> <li> <p>End a conversation by setting <code>endSession</code> to <code>true</code>.</p> </li> <li> <p>In the <code>sessionState</code> object, you can include attributes for the session or prompt or, if you configured an action group to return control, results from invocation of the action group.</p> </li> </ul> <p>The response contains both <b>chunk</b> and <b>trace</b> attributes.</p> <p>The final response is returned in the <code>bytes</code> field of the <code>chunk</code> object. The <code>InvokeAgent</code> returns one chunk for the entire interaction.</p> <ul> <li> <p>The <code>attribution</code> object contains citations for parts of the response.</p> </li> <li> <p>If you set <code>enableTrace</code> to <code>true</code> in the request, you can trace the agent's steps and reasoning process that led it to the response.</p> </li> <li> <p>If the action predicted was configured to return control, the response returns parameters for the action, elicited from the user, in the <code>returnControl</code> field.</p> </li> <li> <p>Errors are also surfaced in the response.</p> </li> </ul>

        Args:
            session_state: <p>Contains parameters that specify various attributes of the session. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html">Control session context</a>.</p> <note> <p>If you include <code>returnControlInvocationResults</code> in the <code>sessionState</code> field, the <code>inputText</code> field will be ignored.</p> </note>
            agent_id: <p>The unique identifier of the agent to use.</p>
            agent_alias_id: <p>The alias of the agent to use.</p>
            session_id: <p>The unique identifier of the session. Use the same value across requests to continue the same conversation.</p>
            end_session: <p>Specifies whether to end the session with the agent or not.</p>
            enable_trace: <p>Specifies whether to turn on the trace or not to track the agent's reasoning process. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html#trace-events">Trace enablement</a>.</p>
            input_text: <p>The prompt text to send the agent.</p> <note> <p>If you include <code>returnControlInvocationResults</code> in the <code>sessionState</code> field, the <code>inputText</code> field will be ignored.</p> </note>
            memory_id: <p>The unique identifier of the agent memory.</p>
            bedrock_model_configurations: <p>Model performance settings for the request.</p>
            streaming_configurations: <p> Specifies the configurations for streaming. </p> <note> <p>To use agent streaming, you need permissions to perform the <code>bedrock:InvokeModelWithResponseStream</code> action.</p> </note>
            prompt_creation_configurations: <p>Specifies parameters that control how the service populates the agent prompt for an <code>InvokeAgent</code> request. You can control which aspects of previous invocations in the same agent session the service uses to populate the agent prompt. This gives you more granular control over the contextual history that is used to process the current request.</p>
            source_arn: <p>The ARN of the resource making the request.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p> The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see <a href="https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html">Retry behavior</a> in the <i>AWS SDKs and Tools</i> reference guide. </p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.invoke_agent_request.InvokeAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.invoke_agent_response.InvokeAgentResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_agent

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_agent.async_invoke_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.invoke_agent_request.InvokeAgentRequest = {
            "agent_id": agent_id,
            "agent_alias_id": agent_alias_id,
            "session_id": session_id,
        }
        if session_state is not None:
            input_["session_state"] = session_state
        if end_session is not None:
            input_["end_session"] = end_session
        if enable_trace is not None:
            input_["enable_trace"] = enable_trace
        if input_text is not None:
            input_["input_text"] = input_text
        if memory_id is not None:
            input_["memory_id"] = memory_id
        if bedrock_model_configurations is not None:
            input_["bedrock_model_configurations"] = bedrock_model_configurations
        if streaming_configurations is not None:
            input_["streaming_configurations"] = streaming_configurations
        if prompt_creation_configurations is not None:
            input_["prompt_creation_configurations"] = prompt_creation_configurations
        if source_arn is not None:
            input_["source_arn"] = source_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()
