from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_bedrock_agent._auth._signers
import capo_bedrock_agent._auth._sigv4
from capo_bedrock_agent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_collaboration
    import capo_bedrock_agent.types.agent_role_arn
    import capo_bedrock_agent.types.agent_summary
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.create_agent_request
    import capo_bedrock_agent.types.create_agent_response
    import capo_bedrock_agent.types.custom_orchestration
    import capo_bedrock_agent.types.delete_agent_request
    import capo_bedrock_agent.types.delete_agent_response
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.get_agent_request
    import capo_bedrock_agent.types.get_agent_response
    import capo_bedrock_agent.types.guardrail_configuration
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.instruction
    import capo_bedrock_agent.types.kms_key_arn
    import capo_bedrock_agent.types.list_agents_request
    import capo_bedrock_agent.types.list_agents_response
    import capo_bedrock_agent.types.max_results
    import capo_bedrock_agent.types.memory_configuration
    import capo_bedrock_agent.types.model_identifier
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.orchestration_type
    import capo_bedrock_agent.types.prepare_agent_request
    import capo_bedrock_agent.types.prepare_agent_response
    import capo_bedrock_agent.types.prompt_override_configuration
    import capo_bedrock_agent.types.session_ttl
    import capo_bedrock_agent.types.tags_map
    import capo_bedrock_agent.types.update_agent_request
    import capo_bedrock_agent.types.update_agent_response
    from capo_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from capo_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class AgentResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def create_agent(
        self,
        agent_name: "capo_bedrock_agent.types.name.Name",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        instruction: Optional[
            "capo_bedrock_agent.types.instruction.Instruction"
        ] = None,
        foundation_model: Optional[
            "capo_bedrock_agent.types.model_identifier.ModelIdentifier"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        orchestration_type: Optional[
            "capo_bedrock_agent.types.orchestration_type.OrchestrationType"
        ] = None,
        custom_orchestration: Optional[
            "capo_bedrock_agent.types.custom_orchestration.CustomOrchestration"
        ] = None,
        idle_session_ttl_in_seconds: Optional[
            "capo_bedrock_agent.types.session_ttl.SessionTTL"
        ] = None,
        agent_resource_role_arn: Optional[
            "capo_bedrock_agent.types.agent_role_arn.AgentRoleArn"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
        prompt_override_configuration: Optional[
            "capo_bedrock_agent.types.prompt_override_configuration.PromptOverrideConfiguration"
        ] = None,
        guardrail_configuration: Optional[
            "capo_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
        ] = None,
        memory_configuration: Optional[
            "capo_bedrock_agent.types.memory_configuration.MemoryConfiguration"
        ] = None,
        agent_collaboration: Optional[
            "capo_bedrock_agent.types.agent_collaboration.AgentCollaboration"
        ] = None,
    ) -> "capo_bedrock_agent.types.create_agent_response.CreateAgentResponse":
        """<note> <p>Amazon Bedrock Agents (now Amazon Bedrock Agents Classic) is no longer open to new customers. For capabilities similar to Bedrock Agents Classic, explore Amazon Bedrock AgentCore. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html">Amazon Bedrock Agents Classic availability change</a>.</p> </note> <p>Creates an agent that orchestrates interactions between foundation models, data sources, software applications, user conversations, and APIs to carry out tasks to help customers.</p> <ul> <li> <p>Specify the following fields for security purposes.</p> <ul> <li> <p> <code>agentResourceRoleArn</code> – The Amazon Resource Name (ARN) of the role with permissions to invoke API operations on an agent.</p> </li> <li> <p>(Optional) <code>customerEncryptionKeyArn</code> – The Amazon Resource Name (ARN) of a KMS key to encrypt the creation of the agent.</p> </li> <li> <p>(Optional) <code>idleSessionTTLinSeconds</code> – Specify the number of seconds for which the agent should maintain session information. After this time expires, the subsequent <code>InvokeAgent</code> request begins a new session.</p> </li> </ul> </li> <li> <p>To enable your agent to retain conversational context across multiple sessions, include a <code>memoryConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-configure-memory.html">Configure memory</a>.</p> </li> <li> <p>To override the default prompt behavior for agent orchestration and to use advanced prompts, include a <code>promptOverrideConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html">Advanced prompts</a>.</p> </li> <li> <p>If your agent fails to be created, the response returns a list of <code>failureReasons</code> alongside a list of <code>recommendedActions</code> for you to troubleshoot.</p> </li> <li> <p>The agent instructions will not be honored if your agent has only one knowledge base, uses default prompts, has no action group, and user input is disabled.</p> </li> </ul>

        Args:
            agent_name: <p>A name for the agent that you create.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            instruction: <p>Instructions that tell the agent what it should do and how it should interact with users.</p>
            foundation_model: <p>The identifier for the model that you want to be used for orchestration by the agent you create.</p> <p>The <code>modelId</code> to provide depends on the type of model or throughput that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported model</a>, specify the ARN of the imported model. You can get the model ARN from a successful call to <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html">CreateModelImportJob</a> or from the Imported models page in the Amazon Bedrock console.</p> </li> </ul>
            description: <p>A description of the agent.</p>
            orchestration_type: <p> Specifies the type of orchestration strategy for the agent. This is set to <code>DEFAULT</code> orchestration type, by default. </p>
            custom_orchestration: <p> Contains details of the custom orchestration configured for the agent. </p>
            idle_session_ttl_in_seconds: <p>The number of seconds for which Amazon Bedrock keeps information about a user's conversation with the agent.</p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.</p>
            agent_resource_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the agent.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key with which to encrypt the agent.</p>
            tags: <p>Any tags that you want to attach to the agent.</p>
            prompt_override_configuration: <p>Contains configurations to override prompts in different parts of an agent sequence. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html">Advanced prompts</a>.</p>
            guardrail_configuration: <p>The unique Guardrail configuration assigned to the agent when it is created.</p>
            memory_configuration: <p> Contains the details of the memory configured for the agent.</p>
            agent_collaboration: <p>The agent's collaboration role.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.create_agent_request.CreateAgentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_agent_response.CreateAgentResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent.create_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_agent_request.CreateAgentRequest = {
            "agent_name": agent_name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if instruction is not None:
            input_["instruction"] = instruction
        if foundation_model is not None:
            input_["foundation_model"] = foundation_model
        if description is not None:
            input_["description"] = description
        if orchestration_type is not None:
            input_["orchestration_type"] = orchestration_type
        if custom_orchestration is not None:
            input_["custom_orchestration"] = custom_orchestration
        if idle_session_ttl_in_seconds is not None:
            input_["idle_session_ttl_in_seconds"] = idle_session_ttl_in_seconds
        if agent_resource_role_arn is not None:
            input_["agent_resource_role_arn"] = agent_resource_role_arn
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if tags is not None:
            input_["tags"] = tags
        if prompt_override_configuration is not None:
            input_["prompt_override_configuration"] = prompt_override_configuration
        if guardrail_configuration is not None:
            input_["guardrail_configuration"] = guardrail_configuration
        if memory_configuration is not None:
            input_["memory_configuration"] = memory_configuration
        if agent_collaboration is not None:
            input_["agent_collaboration"] = agent_collaboration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_agent(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        skip_resource_in_use_check: Optional[bool] = None,
    ) -> "capo_bedrock_agent.types.delete_agent_response.DeleteAgentResponse":
        """<p>Deletes an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent to delete.</p>
            skip_resource_in_use_check: <p>By default, this value is <code>false</code> and deletion is stopped if the resource is in use. If you set it to <code>true</code>, the resource will be deleted even if the resource is in use.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_agent_request.DeleteAgentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_agent_response.DeleteAgentResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent.delete_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_agent_request.DeleteAgentRequest = {
            "agent_id": agent_id
        }
        if skip_resource_in_use_check is not None:
            input_["skip_resource_in_use_check"] = skip_resource_in_use_check

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_agent(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_agent_response.GetAgentResponse":
        """<p>Gets information about an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_agent_request.GetAgentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_agent_response.GetAgentResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent.get_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_agent_request.GetAgentRequest = {
            "agent_id": agent_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_agents(
        self,
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_agents_response.ListAgentsResponse":
        """<p>Lists the agents belonging to an account and information about each agent.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_agents_request.ListAgentsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_agents_response.ListAgentsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agents

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agents.list_agents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_agents_request.ListAgentsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def prepare_agent(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.prepare_agent_response.PrepareAgentResponse":
        """<p>Creates a <code>DRAFT</code> version of the agent that can be used for internal testing.</p>

        Args:
            agent_id: <p>The unique identifier of the agent for which to create a <code>DRAFT</code> version.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.prepare_agent_request.PrepareAgentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.prepare_agent_response.PrepareAgentResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.prepare_agent

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.prepare_agent.prepare_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.prepare_agent_request.PrepareAgentRequest = {
            "agent_id": agent_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_agent(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_name: "capo_bedrock_agent.types.name.Name",
        agent_resource_role_arn: "capo_bedrock_agent.types.agent_role_arn.AgentRoleArn",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        instruction: Optional[
            "capo_bedrock_agent.types.instruction.Instruction"
        ] = None,
        foundation_model: Optional[
            "capo_bedrock_agent.types.model_identifier.ModelIdentifier"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        orchestration_type: Optional[
            "capo_bedrock_agent.types.orchestration_type.OrchestrationType"
        ] = None,
        custom_orchestration: Optional[
            "capo_bedrock_agent.types.custom_orchestration.CustomOrchestration"
        ] = None,
        idle_session_ttl_in_seconds: Optional[
            "capo_bedrock_agent.types.session_ttl.SessionTTL"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        prompt_override_configuration: Optional[
            "capo_bedrock_agent.types.prompt_override_configuration.PromptOverrideConfiguration"
        ] = None,
        guardrail_configuration: Optional[
            "capo_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
        ] = None,
        memory_configuration: Optional[
            "capo_bedrock_agent.types.memory_configuration.MemoryConfiguration"
        ] = None,
        agent_collaboration: Optional[
            "capo_bedrock_agent.types.agent_collaboration.AgentCollaboration"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_agent_response.UpdateAgentResponse":
        """<p>Updates the configuration of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_name: <p>Specifies a new name for the agent.</p>
            instruction: <p>Specifies new instructions that tell the agent what it should do and how it should interact with users.</p>
            foundation_model: <p>The identifier for the model that you want to be used for orchestration by the agent you create.</p> <p>The <code>modelId</code> to provide depends on the type of model or throughput that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported model</a>, specify the ARN of the imported model. You can get the model ARN from a successful call to <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html">CreateModelImportJob</a> or from the Imported models page in the Amazon Bedrock console.</p> </li> </ul>
            description: <p>Specifies a new description of the agent.</p>
            orchestration_type: <p> Specifies the type of orchestration strategy for the agent. This is set to <code>DEFAULT</code> orchestration type, by default. </p>
            custom_orchestration: <p> Contains details of the custom orchestration configured for the agent. </p>
            idle_session_ttl_in_seconds: <p>The number of seconds for which Amazon Bedrock keeps information about a user's conversation with the agent.</p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.</p>
            agent_resource_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the agent.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key with which to encrypt the agent.</p>
            prompt_override_configuration: <p>Contains configurations to override prompts in different parts of an agent sequence. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html">Advanced prompts</a>.</p>
            guardrail_configuration: <p>The unique Guardrail configuration assigned to the agent when it is updated.</p>
            memory_configuration: <p>Specifies the new memory configuration for the agent. </p>
            agent_collaboration: <p>The agent's collaboration role.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.update_agent_request.UpdateAgentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_agent_response.UpdateAgentResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent.update_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_agent_request.UpdateAgentRequest = {
            "agent_id": agent_id,
            "agent_name": agent_name,
            "agent_resource_role_arn": agent_resource_role_arn,
        }
        if instruction is not None:
            input_["instruction"] = instruction
        if foundation_model is not None:
            input_["foundation_model"] = foundation_model
        if description is not None:
            input_["description"] = description
        if orchestration_type is not None:
            input_["orchestration_type"] = orchestration_type
        if custom_orchestration is not None:
            input_["custom_orchestration"] = custom_orchestration
        if idle_session_ttl_in_seconds is not None:
            input_["idle_session_ttl_in_seconds"] = idle_session_ttl_in_seconds
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if prompt_override_configuration is not None:
            input_["prompt_override_configuration"] = prompt_override_configuration
        if guardrail_configuration is not None:
            input_["guardrail_configuration"] = guardrail_configuration
        if memory_configuration is not None:
            input_["memory_configuration"] = memory_configuration
        if agent_collaboration is not None:
            input_["agent_collaboration"] = agent_collaboration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAgentResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def create_agent(
        self,
        agent_name: "capo_bedrock_agent.types.name.Name",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        instruction: Optional[
            "capo_bedrock_agent.types.instruction.Instruction"
        ] = None,
        foundation_model: Optional[
            "capo_bedrock_agent.types.model_identifier.ModelIdentifier"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        orchestration_type: Optional[
            "capo_bedrock_agent.types.orchestration_type.OrchestrationType"
        ] = None,
        custom_orchestration: Optional[
            "capo_bedrock_agent.types.custom_orchestration.CustomOrchestration"
        ] = None,
        idle_session_ttl_in_seconds: Optional[
            "capo_bedrock_agent.types.session_ttl.SessionTTL"
        ] = None,
        agent_resource_role_arn: Optional[
            "capo_bedrock_agent.types.agent_role_arn.AgentRoleArn"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
        prompt_override_configuration: Optional[
            "capo_bedrock_agent.types.prompt_override_configuration.PromptOverrideConfiguration"
        ] = None,
        guardrail_configuration: Optional[
            "capo_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
        ] = None,
        memory_configuration: Optional[
            "capo_bedrock_agent.types.memory_configuration.MemoryConfiguration"
        ] = None,
        agent_collaboration: Optional[
            "capo_bedrock_agent.types.agent_collaboration.AgentCollaboration"
        ] = None,
    ) -> "capo_bedrock_agent.types.create_agent_response.CreateAgentResponse":
        """<note> <p>Amazon Bedrock Agents (now Amazon Bedrock Agents Classic) is no longer open to new customers. For capabilities similar to Bedrock Agents Classic, explore Amazon Bedrock AgentCore. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html">Amazon Bedrock Agents Classic availability change</a>.</p> </note> <p>Creates an agent that orchestrates interactions between foundation models, data sources, software applications, user conversations, and APIs to carry out tasks to help customers.</p> <ul> <li> <p>Specify the following fields for security purposes.</p> <ul> <li> <p> <code>agentResourceRoleArn</code> – The Amazon Resource Name (ARN) of the role with permissions to invoke API operations on an agent.</p> </li> <li> <p>(Optional) <code>customerEncryptionKeyArn</code> – The Amazon Resource Name (ARN) of a KMS key to encrypt the creation of the agent.</p> </li> <li> <p>(Optional) <code>idleSessionTTLinSeconds</code> – Specify the number of seconds for which the agent should maintain session information. After this time expires, the subsequent <code>InvokeAgent</code> request begins a new session.</p> </li> </ul> </li> <li> <p>To enable your agent to retain conversational context across multiple sessions, include a <code>memoryConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-configure-memory.html">Configure memory</a>.</p> </li> <li> <p>To override the default prompt behavior for agent orchestration and to use advanced prompts, include a <code>promptOverrideConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html">Advanced prompts</a>.</p> </li> <li> <p>If your agent fails to be created, the response returns a list of <code>failureReasons</code> alongside a list of <code>recommendedActions</code> for you to troubleshoot.</p> </li> <li> <p>The agent instructions will not be honored if your agent has only one knowledge base, uses default prompts, has no action group, and user input is disabled.</p> </li> </ul>

        Args:
            agent_name: <p>A name for the agent that you create.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            instruction: <p>Instructions that tell the agent what it should do and how it should interact with users.</p>
            foundation_model: <p>The identifier for the model that you want to be used for orchestration by the agent you create.</p> <p>The <code>modelId</code> to provide depends on the type of model or throughput that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported model</a>, specify the ARN of the imported model. You can get the model ARN from a successful call to <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html">CreateModelImportJob</a> or from the Imported models page in the Amazon Bedrock console.</p> </li> </ul>
            description: <p>A description of the agent.</p>
            orchestration_type: <p> Specifies the type of orchestration strategy for the agent. This is set to <code>DEFAULT</code> orchestration type, by default. </p>
            custom_orchestration: <p> Contains details of the custom orchestration configured for the agent. </p>
            idle_session_ttl_in_seconds: <p>The number of seconds for which Amazon Bedrock keeps information about a user's conversation with the agent.</p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.</p>
            agent_resource_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the agent.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key with which to encrypt the agent.</p>
            tags: <p>Any tags that you want to attach to the agent.</p>
            prompt_override_configuration: <p>Contains configurations to override prompts in different parts of an agent sequence. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html">Advanced prompts</a>.</p>
            guardrail_configuration: <p>The unique Guardrail configuration assigned to the agent when it is created.</p>
            memory_configuration: <p> Contains the details of the memory configured for the agent.</p>
            agent_collaboration: <p>The agent's collaboration role.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.create_agent_request.CreateAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.create_agent_response.CreateAgentResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent.async_create_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_agent_request.CreateAgentRequest = {
            "agent_name": agent_name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if instruction is not None:
            input_["instruction"] = instruction
        if foundation_model is not None:
            input_["foundation_model"] = foundation_model
        if description is not None:
            input_["description"] = description
        if orchestration_type is not None:
            input_["orchestration_type"] = orchestration_type
        if custom_orchestration is not None:
            input_["custom_orchestration"] = custom_orchestration
        if idle_session_ttl_in_seconds is not None:
            input_["idle_session_ttl_in_seconds"] = idle_session_ttl_in_seconds
        if agent_resource_role_arn is not None:
            input_["agent_resource_role_arn"] = agent_resource_role_arn
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if tags is not None:
            input_["tags"] = tags
        if prompt_override_configuration is not None:
            input_["prompt_override_configuration"] = prompt_override_configuration
        if guardrail_configuration is not None:
            input_["guardrail_configuration"] = guardrail_configuration
        if memory_configuration is not None:
            input_["memory_configuration"] = memory_configuration
        if agent_collaboration is not None:
            input_["agent_collaboration"] = agent_collaboration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_agent(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        skip_resource_in_use_check: Optional[bool] = None,
    ) -> "capo_bedrock_agent.types.delete_agent_response.DeleteAgentResponse":
        """<p>Deletes an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent to delete.</p>
            skip_resource_in_use_check: <p>By default, this value is <code>false</code> and deletion is stopped if the resource is in use. If you set it to <code>true</code>, the resource will be deleted even if the resource is in use.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.delete_agent_request.DeleteAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.delete_agent_response.DeleteAgentResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent.async_delete_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_agent_request.DeleteAgentRequest = {
            "agent_id": agent_id
        }
        if skip_resource_in_use_check is not None:
            input_["skip_resource_in_use_check"] = skip_resource_in_use_check

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_agent(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_agent_response.GetAgentResponse":
        """<p>Gets information about an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.get_agent_request.GetAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.get_agent_response.GetAgentResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent.async_get_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_agent_request.GetAgentRequest = {
            "agent_id": agent_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_agents(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_agents_response.ListAgentsResponse":
        """<p>Lists the agents belonging to an account and information about each agent.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.list_agents_request.ListAgentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.list_agents_response.ListAgentsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agents

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agents.async_list_agents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_agents_request.ListAgentsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def prepare_agent(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.prepare_agent_response.PrepareAgentResponse":
        """<p>Creates a <code>DRAFT</code> version of the agent that can be used for internal testing.</p>

        Args:
            agent_id: <p>The unique identifier of the agent for which to create a <code>DRAFT</code> version.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.prepare_agent_request.PrepareAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.prepare_agent_response.PrepareAgentResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.prepare_agent

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.prepare_agent.async_prepare_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.prepare_agent_request.PrepareAgentRequest = {
            "agent_id": agent_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_agent(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_name: "capo_bedrock_agent.types.name.Name",
        agent_resource_role_arn: "capo_bedrock_agent.types.agent_role_arn.AgentRoleArn",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        instruction: Optional[
            "capo_bedrock_agent.types.instruction.Instruction"
        ] = None,
        foundation_model: Optional[
            "capo_bedrock_agent.types.model_identifier.ModelIdentifier"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        orchestration_type: Optional[
            "capo_bedrock_agent.types.orchestration_type.OrchestrationType"
        ] = None,
        custom_orchestration: Optional[
            "capo_bedrock_agent.types.custom_orchestration.CustomOrchestration"
        ] = None,
        idle_session_ttl_in_seconds: Optional[
            "capo_bedrock_agent.types.session_ttl.SessionTTL"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        prompt_override_configuration: Optional[
            "capo_bedrock_agent.types.prompt_override_configuration.PromptOverrideConfiguration"
        ] = None,
        guardrail_configuration: Optional[
            "capo_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
        ] = None,
        memory_configuration: Optional[
            "capo_bedrock_agent.types.memory_configuration.MemoryConfiguration"
        ] = None,
        agent_collaboration: Optional[
            "capo_bedrock_agent.types.agent_collaboration.AgentCollaboration"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_agent_response.UpdateAgentResponse":
        """<p>Updates the configuration of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_name: <p>Specifies a new name for the agent.</p>
            instruction: <p>Specifies new instructions that tell the agent what it should do and how it should interact with users.</p>
            foundation_model: <p>The identifier for the model that you want to be used for orchestration by the agent you create.</p> <p>The <code>modelId</code> to provide depends on the type of model or throughput that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported model</a>, specify the ARN of the imported model. You can get the model ARN from a successful call to <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html">CreateModelImportJob</a> or from the Imported models page in the Amazon Bedrock console.</p> </li> </ul>
            description: <p>Specifies a new description of the agent.</p>
            orchestration_type: <p> Specifies the type of orchestration strategy for the agent. This is set to <code>DEFAULT</code> orchestration type, by default. </p>
            custom_orchestration: <p> Contains details of the custom orchestration configured for the agent. </p>
            idle_session_ttl_in_seconds: <p>The number of seconds for which Amazon Bedrock keeps information about a user's conversation with the agent.</p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.</p>
            agent_resource_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the agent.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key with which to encrypt the agent.</p>
            prompt_override_configuration: <p>Contains configurations to override prompts in different parts of an agent sequence. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html">Advanced prompts</a>.</p>
            guardrail_configuration: <p>The unique Guardrail configuration assigned to the agent when it is updated.</p>
            memory_configuration: <p>Specifies the new memory configuration for the agent. </p>
            agent_collaboration: <p>The agent's collaboration role.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.update_agent_request.UpdateAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.update_agent_response.UpdateAgentResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent.async_update_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_agent_request.UpdateAgentRequest = {
            "agent_id": agent_id,
            "agent_name": agent_name,
            "agent_resource_role_arn": agent_resource_role_arn,
        }
        if instruction is not None:
            input_["instruction"] = instruction
        if foundation_model is not None:
            input_["foundation_model"] = foundation_model
        if description is not None:
            input_["description"] = description
        if orchestration_type is not None:
            input_["orchestration_type"] = orchestration_type
        if custom_orchestration is not None:
            input_["custom_orchestration"] = custom_orchestration
        if idle_session_ttl_in_seconds is not None:
            input_["idle_session_ttl_in_seconds"] = idle_session_ttl_in_seconds
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if prompt_override_configuration is not None:
            input_["prompt_override_configuration"] = prompt_override_configuration
        if guardrail_configuration is not None:
            input_["guardrail_configuration"] = guardrail_configuration
        if memory_configuration is not None:
            input_["memory_configuration"] = memory_configuration
        if agent_collaboration is not None:
            input_["agent_collaboration"] = agent_collaboration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
