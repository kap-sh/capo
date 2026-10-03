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
    import capo_bedrock_agent_runtime.types.agent_action_groups
    import capo_bedrock_agent_runtime.types.agent_collaboration
    import capo_bedrock_agent_runtime.types.collaborator_configurations
    import capo_bedrock_agent_runtime.types.collaborators
    import capo_bedrock_agent_runtime.types.custom_orchestration
    import capo_bedrock_agent_runtime.types.guardrail_configuration_with_arn
    import capo_bedrock_agent_runtime.types.inline_bedrock_model_configurations
    import capo_bedrock_agent_runtime.types.inline_session_state
    import capo_bedrock_agent_runtime.types.input_text
    import capo_bedrock_agent_runtime.types.instruction
    import capo_bedrock_agent_runtime.types.invoke_inline_agent_request
    import capo_bedrock_agent_runtime.types.invoke_inline_agent_response
    import capo_bedrock_agent_runtime.types.kms_key_arn
    import capo_bedrock_agent_runtime.types.knowledge_bases
    import capo_bedrock_agent_runtime.types.model_identifier
    import capo_bedrock_agent_runtime.types.name
    import capo_bedrock_agent_runtime.types.orchestration_type
    import capo_bedrock_agent_runtime.types.prompt_creation_configurations
    import capo_bedrock_agent_runtime.types.prompt_override_configuration
    import capo_bedrock_agent_runtime.types.session_id
    import capo_bedrock_agent_runtime.types.session_ttl
    import capo_bedrock_agent_runtime.types.streaming_configurations
    from capo_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from capo_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class InlineAgentResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    @contextmanager
    def invoke_inline_agent(
        self,
        foundation_model: "capo_bedrock_agent_runtime.types.model_identifier.ModelIdentifier",
        instruction: "capo_bedrock_agent_runtime.types.instruction.Instruction",
        session_id: "capo_bedrock_agent_runtime.types.session_id.SessionId",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent_runtime.types.kms_key_arn.KmsKeyArn"
        ] = None,
        idle_session_ttl_in_seconds: Optional[
            "capo_bedrock_agent_runtime.types.session_ttl.SessionTTL"
        ] = None,
        action_groups: Optional[
            "capo_bedrock_agent_runtime.types.agent_action_groups.AgentActionGroups"
        ] = None,
        knowledge_bases: Optional[
            "capo_bedrock_agent_runtime.types.knowledge_bases.KnowledgeBases"
        ] = None,
        guardrail_configuration: Optional[
            "capo_bedrock_agent_runtime.types.guardrail_configuration_with_arn.GuardrailConfigurationWithArn"
        ] = None,
        prompt_override_configuration: Optional[
            "capo_bedrock_agent_runtime.types.prompt_override_configuration.PromptOverrideConfiguration"
        ] = None,
        agent_collaboration: Optional[
            "capo_bedrock_agent_runtime.types.agent_collaboration.AgentCollaboration"
        ] = None,
        collaborator_configurations: Optional[
            "capo_bedrock_agent_runtime.types.collaborator_configurations.CollaboratorConfigurations"
        ] = None,
        agent_name: Optional["capo_bedrock_agent_runtime.types.name.Name"] = None,
        end_session: Optional[bool] = None,
        enable_trace: Optional[bool] = None,
        input_text: Optional[
            "capo_bedrock_agent_runtime.types.input_text.InputText"
        ] = None,
        streaming_configurations: Optional[
            "capo_bedrock_agent_runtime.types.streaming_configurations.StreamingConfigurations"
        ] = None,
        prompt_creation_configurations: Optional[
            "capo_bedrock_agent_runtime.types.prompt_creation_configurations.PromptCreationConfigurations"
        ] = None,
        inline_session_state: Optional[
            "capo_bedrock_agent_runtime.types.inline_session_state.InlineSessionState"
        ] = None,
        collaborators: Optional[
            "capo_bedrock_agent_runtime.types.collaborators.Collaborators"
        ] = None,
        bedrock_model_configurations: Optional[
            "capo_bedrock_agent_runtime.types.inline_bedrock_model_configurations.InlineBedrockModelConfigurations"
        ] = None,
        orchestration_type: Optional[
            "capo_bedrock_agent_runtime.types.orchestration_type.OrchestrationType"
        ] = None,
        custom_orchestration: Optional[
            "capo_bedrock_agent_runtime.types.custom_orchestration.CustomOrchestration"
        ] = None,
    ) -> "Generator[capo_bedrock_agent_runtime.types.invoke_inline_agent_response.InvokeInlineAgentResponse]":
        """<p> Invokes an inline Amazon Bedrock agent using the configurations you provide with the request. </p> <ul> <li> <p>Specify the following fields for security purposes.</p> <ul> <li> <p>(Optional) <code>customerEncryptionKeyArn</code> – The Amazon Resource Name (ARN) of a KMS key to encrypt the creation of the agent.</p> </li> <li> <p>(Optional) <code>idleSessionTTLinSeconds</code> – Specify the number of seconds for which the agent should maintain session information. After this time expires, the subsequent <code>InvokeInlineAgent</code> request begins a new session.</p> </li> </ul> </li> <li> <p>To override the default prompt behavior for agent orchestration and to use advanced prompts, include a <code>promptOverrideConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html">Advanced prompts</a>.</p> </li> <li> <p>The agent instructions will not be honored if your agent has only one knowledge base, uses default prompts, has no action group, and user input is disabled.</p> </li> </ul> <note> </note>

        Args:
            customer_encryption_key_arn: <p> The Amazon Resource Name (ARN) of the Amazon Web Services KMS key to use to encrypt your inline agent. </p>
            foundation_model: <p> The <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">model identifier (ID)</a> of the model to use for orchestration by the inline agent. For example, <code>meta.llama3-1-70b-instruct-v1:0</code>. </p>
            instruction: <p> The instructions that tell the inline agent what it should do and how it should interact with users. </p>
            idle_session_ttl_in_seconds: <p> The number of seconds for which the inline agent should maintain session information. After this time expires, the subsequent <code>InvokeInlineAgent</code> request begins a new session. </p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and the data provided before the timeout is deleted.</p>
            action_groups: <p> A list of action groups with each action group defining the action the inline agent needs to carry out. </p>
            knowledge_bases: <p> Contains information of the knowledge bases to associate with. </p>
            guardrail_configuration: <p> The <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html">guardrails</a> to assign to the inline agent. </p>
            prompt_override_configuration: <p> Configurations for advanced prompts used to override the default prompts to enhance the accuracy of the inline agent. </p>
            agent_collaboration: <p> Defines how the inline collaborator agent handles information across multiple collaborator agents to coordinate a final response. The inline collaborator agent can also be the supervisor. </p>
            collaborator_configurations: <p> Settings for an inline agent collaborator called with <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeInlineAgent.html">InvokeInlineAgent</a>. </p>
            agent_name: <p>The name for the agent.</p>
            session_id: <p> The unique identifier of the session. Use the same value across requests to continue the same conversation. </p>
            end_session: <p> Specifies whether to end the session with the inline agent or not. </p>
            enable_trace: <p> Specifies whether to turn on the trace or not to track the agent's reasoning process. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html">Using trace</a>. </p>
            input_text: <p> The prompt text to send to the agent. </p> <note> <p>If you include <code>returnControlInvocationResults</code> in the <code>sessionState</code> field, the <code>inputText</code> field will be ignored.</p> </note>
            streaming_configurations: <p> Specifies the configurations for streaming. </p> <note> <p>To use agent streaming, you need permissions to perform the <code>bedrock:InvokeModelWithResponseStream</code> action.</p> </note>
            prompt_creation_configurations: <p>Specifies parameters that control how the service populates the agent prompt for an <code>InvokeInlineAgent</code> request. You can control which aspects of previous invocations in the same agent session the service uses to populate the agent prompt. This gives you more granular control over the contextual history that is used to process the current request.</p>
            inline_session_state: <p> Parameters that specify the various attributes of a sessions. You can include attributes for the session or prompt or, if you configured an action group to return control, results from invocation of the action group. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html">Control session context</a>. </p> <note> <p>If you include <code>returnControlInvocationResults</code> in the <code>sessionState</code> field, the <code>inputText</code> field will be ignored.</p> </note>
            collaborators: <p> List of collaborator inline agents. </p>
            bedrock_model_configurations: <p>Model settings for the request.</p>
            orchestration_type: <p>Specifies the type of orchestration strategy for the agent. This is set to DEFAULT orchestration type, by default. </p>
            custom_orchestration: <p>Contains details of the custom orchestration configured for the agent. </p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent_runtime.types.invoke_inline_agent_request.InvokeInlineAgentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.invoke_inline_agent_response.InvokeInlineAgentResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_inline_agent

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_inline_agent.invoke_inline_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.invoke_inline_agent_request.InvokeInlineAgentRequest = {
            "foundation_model": foundation_model,
            "instruction": instruction,
            "session_id": session_id,
        }
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if idle_session_ttl_in_seconds is not None:
            input_["idle_session_ttl_in_seconds"] = idle_session_ttl_in_seconds
        if action_groups is not None:
            input_["action_groups"] = action_groups
        if knowledge_bases is not None:
            input_["knowledge_bases"] = knowledge_bases
        if guardrail_configuration is not None:
            input_["guardrail_configuration"] = guardrail_configuration
        if prompt_override_configuration is not None:
            input_["prompt_override_configuration"] = prompt_override_configuration
        if agent_collaboration is not None:
            input_["agent_collaboration"] = agent_collaboration
        if collaborator_configurations is not None:
            input_["collaborator_configurations"] = collaborator_configurations
        if agent_name is not None:
            input_["agent_name"] = agent_name
        if end_session is not None:
            input_["end_session"] = end_session
        if enable_trace is not None:
            input_["enable_trace"] = enable_trace
        if input_text is not None:
            input_["input_text"] = input_text
        if streaming_configurations is not None:
            input_["streaming_configurations"] = streaming_configurations
        if prompt_creation_configurations is not None:
            input_["prompt_creation_configurations"] = prompt_creation_configurations
        if inline_session_state is not None:
            input_["inline_session_state"] = inline_session_state
        if collaborators is not None:
            input_["collaborators"] = collaborators
        if bedrock_model_configurations is not None:
            input_["bedrock_model_configurations"] = bedrock_model_configurations
        if orchestration_type is not None:
            input_["orchestration_type"] = orchestration_type
        if custom_orchestration is not None:
            input_["custom_orchestration"] = custom_orchestration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()


class AsyncInlineAgentResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    @asynccontextmanager
    async def invoke_inline_agent(
        self,
        foundation_model: "capo_bedrock_agent_runtime.types.model_identifier.ModelIdentifier",
        instruction: "capo_bedrock_agent_runtime.types.instruction.Instruction",
        session_id: "capo_bedrock_agent_runtime.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent_runtime.types.kms_key_arn.KmsKeyArn"
        ] = None,
        idle_session_ttl_in_seconds: Optional[
            "capo_bedrock_agent_runtime.types.session_ttl.SessionTTL"
        ] = None,
        action_groups: Optional[
            "capo_bedrock_agent_runtime.types.agent_action_groups.AgentActionGroups"
        ] = None,
        knowledge_bases: Optional[
            "capo_bedrock_agent_runtime.types.knowledge_bases.KnowledgeBases"
        ] = None,
        guardrail_configuration: Optional[
            "capo_bedrock_agent_runtime.types.guardrail_configuration_with_arn.GuardrailConfigurationWithArn"
        ] = None,
        prompt_override_configuration: Optional[
            "capo_bedrock_agent_runtime.types.prompt_override_configuration.PromptOverrideConfiguration"
        ] = None,
        agent_collaboration: Optional[
            "capo_bedrock_agent_runtime.types.agent_collaboration.AgentCollaboration"
        ] = None,
        collaborator_configurations: Optional[
            "capo_bedrock_agent_runtime.types.collaborator_configurations.CollaboratorConfigurations"
        ] = None,
        agent_name: Optional["capo_bedrock_agent_runtime.types.name.Name"] = None,
        end_session: Optional[bool] = None,
        enable_trace: Optional[bool] = None,
        input_text: Optional[
            "capo_bedrock_agent_runtime.types.input_text.InputText"
        ] = None,
        streaming_configurations: Optional[
            "capo_bedrock_agent_runtime.types.streaming_configurations.StreamingConfigurations"
        ] = None,
        prompt_creation_configurations: Optional[
            "capo_bedrock_agent_runtime.types.prompt_creation_configurations.PromptCreationConfigurations"
        ] = None,
        inline_session_state: Optional[
            "capo_bedrock_agent_runtime.types.inline_session_state.InlineSessionState"
        ] = None,
        collaborators: Optional[
            "capo_bedrock_agent_runtime.types.collaborators.Collaborators"
        ] = None,
        bedrock_model_configurations: Optional[
            "capo_bedrock_agent_runtime.types.inline_bedrock_model_configurations.InlineBedrockModelConfigurations"
        ] = None,
        orchestration_type: Optional[
            "capo_bedrock_agent_runtime.types.orchestration_type.OrchestrationType"
        ] = None,
        custom_orchestration: Optional[
            "capo_bedrock_agent_runtime.types.custom_orchestration.CustomOrchestration"
        ] = None,
    ) -> "AsyncGenerator[capo_bedrock_agent_runtime.types.invoke_inline_agent_response.InvokeInlineAgentResponse]":
        """<p> Invokes an inline Amazon Bedrock agent using the configurations you provide with the request. </p> <ul> <li> <p>Specify the following fields for security purposes.</p> <ul> <li> <p>(Optional) <code>customerEncryptionKeyArn</code> – The Amazon Resource Name (ARN) of a KMS key to encrypt the creation of the agent.</p> </li> <li> <p>(Optional) <code>idleSessionTTLinSeconds</code> – Specify the number of seconds for which the agent should maintain session information. After this time expires, the subsequent <code>InvokeInlineAgent</code> request begins a new session.</p> </li> </ul> </li> <li> <p>To override the default prompt behavior for agent orchestration and to use advanced prompts, include a <code>promptOverrideConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html">Advanced prompts</a>.</p> </li> <li> <p>The agent instructions will not be honored if your agent has only one knowledge base, uses default prompts, has no action group, and user input is disabled.</p> </li> </ul> <note> </note>

        Args:
            customer_encryption_key_arn: <p> The Amazon Resource Name (ARN) of the Amazon Web Services KMS key to use to encrypt your inline agent. </p>
            foundation_model: <p> The <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">model identifier (ID)</a> of the model to use for orchestration by the inline agent. For example, <code>meta.llama3-1-70b-instruct-v1:0</code>. </p>
            instruction: <p> The instructions that tell the inline agent what it should do and how it should interact with users. </p>
            idle_session_ttl_in_seconds: <p> The number of seconds for which the inline agent should maintain session information. After this time expires, the subsequent <code>InvokeInlineAgent</code> request begins a new session. </p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and the data provided before the timeout is deleted.</p>
            action_groups: <p> A list of action groups with each action group defining the action the inline agent needs to carry out. </p>
            knowledge_bases: <p> Contains information of the knowledge bases to associate with. </p>
            guardrail_configuration: <p> The <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html">guardrails</a> to assign to the inline agent. </p>
            prompt_override_configuration: <p> Configurations for advanced prompts used to override the default prompts to enhance the accuracy of the inline agent. </p>
            agent_collaboration: <p> Defines how the inline collaborator agent handles information across multiple collaborator agents to coordinate a final response. The inline collaborator agent can also be the supervisor. </p>
            collaborator_configurations: <p> Settings for an inline agent collaborator called with <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeInlineAgent.html">InvokeInlineAgent</a>. </p>
            agent_name: <p>The name for the agent.</p>
            session_id: <p> The unique identifier of the session. Use the same value across requests to continue the same conversation. </p>
            end_session: <p> Specifies whether to end the session with the inline agent or not. </p>
            enable_trace: <p> Specifies whether to turn on the trace or not to track the agent's reasoning process. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html">Using trace</a>. </p>
            input_text: <p> The prompt text to send to the agent. </p> <note> <p>If you include <code>returnControlInvocationResults</code> in the <code>sessionState</code> field, the <code>inputText</code> field will be ignored.</p> </note>
            streaming_configurations: <p> Specifies the configurations for streaming. </p> <note> <p>To use agent streaming, you need permissions to perform the <code>bedrock:InvokeModelWithResponseStream</code> action.</p> </note>
            prompt_creation_configurations: <p>Specifies parameters that control how the service populates the agent prompt for an <code>InvokeInlineAgent</code> request. You can control which aspects of previous invocations in the same agent session the service uses to populate the agent prompt. This gives you more granular control over the contextual history that is used to process the current request.</p>
            inline_session_state: <p> Parameters that specify the various attributes of a sessions. You can include attributes for the session or prompt or, if you configured an action group to return control, results from invocation of the action group. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html">Control session context</a>. </p> <note> <p>If you include <code>returnControlInvocationResults</code> in the <code>sessionState</code> field, the <code>inputText</code> field will be ignored.</p> </note>
            collaborators: <p> List of collaborator inline agents. </p>
            bedrock_model_configurations: <p>Model settings for the request.</p>
            orchestration_type: <p>Specifies the type of orchestration strategy for the agent. This is set to DEFAULT orchestration type, by default. </p>
            custom_orchestration: <p>Contains details of the custom orchestration configured for the agent. </p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.invoke_inline_agent_request.InvokeInlineAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.invoke_inline_agent_response.InvokeInlineAgentResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_inline_agent

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_inline_agent.async_invoke_inline_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.invoke_inline_agent_request.InvokeInlineAgentRequest = {
            "foundation_model": foundation_model,
            "instruction": instruction,
            "session_id": session_id,
        }
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if idle_session_ttl_in_seconds is not None:
            input_["idle_session_ttl_in_seconds"] = idle_session_ttl_in_seconds
        if action_groups is not None:
            input_["action_groups"] = action_groups
        if knowledge_bases is not None:
            input_["knowledge_bases"] = knowledge_bases
        if guardrail_configuration is not None:
            input_["guardrail_configuration"] = guardrail_configuration
        if prompt_override_configuration is not None:
            input_["prompt_override_configuration"] = prompt_override_configuration
        if agent_collaboration is not None:
            input_["agent_collaboration"] = agent_collaboration
        if collaborator_configurations is not None:
            input_["collaborator_configurations"] = collaborator_configurations
        if agent_name is not None:
            input_["agent_name"] = agent_name
        if end_session is not None:
            input_["end_session"] = end_session
        if enable_trace is not None:
            input_["enable_trace"] = enable_trace
        if input_text is not None:
            input_["input_text"] = input_text
        if streaming_configurations is not None:
            input_["streaming_configurations"] = streaming_configurations
        if prompt_creation_configurations is not None:
            input_["prompt_creation_configurations"] = prompt_creation_configurations
        if inline_session_state is not None:
            input_["inline_session_state"] = inline_session_state
        if collaborators is not None:
            input_["collaborators"] = collaborators
        if bedrock_model_configurations is not None:
            input_["bedrock_model_configurations"] = bedrock_model_configurations
        if orchestration_type is not None:
            input_["orchestration_type"] = orchestration_type
        if custom_orchestration is not None:
            input_["custom_orchestration"] = custom_orchestration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()
