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
    import capo_bedrock_agent.types.action_group_executor
    import capo_bedrock_agent.types.action_group_signature
    import capo_bedrock_agent.types.action_group_signature_params
    import capo_bedrock_agent.types.action_group_state
    import capo_bedrock_agent.types.action_group_summary
    import capo_bedrock_agent.types.api_schema
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.create_agent_action_group_request
    import capo_bedrock_agent.types.create_agent_action_group_response
    import capo_bedrock_agent.types.delete_agent_action_group_request
    import capo_bedrock_agent.types.delete_agent_action_group_response
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.draft_version
    import capo_bedrock_agent.types.function_schema
    import capo_bedrock_agent.types.get_agent_action_group_request
    import capo_bedrock_agent.types.get_agent_action_group_response
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.list_agent_action_groups_request
    import capo_bedrock_agent.types.list_agent_action_groups_response
    import capo_bedrock_agent.types.max_results
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.update_agent_action_group_request
    import capo_bedrock_agent.types.update_agent_action_group_response
    import capo_bedrock_agent.types.version
    from capo_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from capo_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class ActionGroupResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def create_agent_action_group(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        action_group_name: "capo_bedrock_agent.types.name.Name",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        parent_action_group_signature: Optional[
            "capo_bedrock_agent.types.action_group_signature.ActionGroupSignature"
        ] = None,
        parent_action_group_signature_params: Optional[
            "capo_bedrock_agent.types.action_group_signature_params.ActionGroupSignatureParams"
        ] = None,
        action_group_executor: Optional[
            "capo_bedrock_agent.types.action_group_executor.ActionGroupExecutor"
        ] = None,
        api_schema: Optional["capo_bedrock_agent.types.api_schema.APISchema"] = None,
        action_group_state: Optional[
            "capo_bedrock_agent.types.action_group_state.ActionGroupState"
        ] = None,
        function_schema: Optional[
            "capo_bedrock_agent.types.function_schema.FunctionSchema"
        ] = None,
    ) -> "capo_bedrock_agent.types.create_agent_action_group_response.CreateAgentActionGroupResponse":
        """<p>Creates an action group for an agent. An action group represents the actions that an agent can carry out for the customer by defining the APIs that an agent can call and the logic for calling them.</p> <p>To allow your agent to request the user for additional information when trying to complete a task, add an action group with the <code>parentActionGroupSignature</code> field set to <code>AMAZON.UserInput</code>. </p> <p>To allow your agent to generate, run, and troubleshoot code when trying to complete a task, add an action group with the <code>parentActionGroupSignature</code> field set to <code>AMAZON.CodeInterpreter</code>. </p> <p>You must leave the <code>description</code>, <code>apiSchema</code>, and <code>actionGroupExecutor</code> fields blank for this action group. During orchestration, if your agent determines that it needs to invoke an API in an action group, but doesn't have enough information to complete the API request, it will invoke this action group instead and return an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Observation.html">Observation</a> reprompting the user for more information.</p>

        Args:
            agent_id: <p>The unique identifier of the agent for which to create the action group.</p>
            agent_version: <p>The version of the agent for which to create the action group.</p>
            action_group_name: <p>The name to give the action group.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            description: <p>A description of the action group.</p>
            parent_action_group_signature: <p>Specify a built-in or computer use action for this action group. If you specify a value, you must leave the <code>description</code>, <code>apiSchema</code>, and <code>actionGroupExecutor</code> fields empty for this action group. </p> <ul> <li> <p>To allow your agent to request the user for additional information when trying to complete a task, set this field to <code>AMAZON.UserInput</code>. </p> </li> <li> <p>To allow your agent to generate, run, and troubleshoot code when trying to complete a task, set this field to <code>AMAZON.CodeInterpreter</code>.</p> </li> <li> <p>To allow your agent to use an Anthropic computer use tool, specify one of the following values. </p> <important> <p> Computer use is a new Anthropic Claude model capability (in beta) available with Anthropic Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. When operating computer use functionality, we recommend taking additional security precautions, such as executing computer actions in virtual environments with restricted data access and limited internet connectivity. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p> </important> <ul> <li> <p> <code>ANTHROPIC.Computer</code> - Gives the agent permission to use the mouse and keyboard and take screenshots.</p> </li> <li> <p> <code>ANTHROPIC.TextEditor</code> - Gives the agent permission to view, create and edit files.</p> </li> <li> <p> <code>ANTHROPIC.Bash</code> - Gives the agent permission to run commands in a bash shell.</p> </li> </ul> </li> </ul>
            parent_action_group_signature_params: <p>The configuration settings for a computer use action.</p> <important> <p> Computer use is a new Anthropic Claude model capability (in beta) available with Anthropic Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p> </important>
            action_group_executor: <p>The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking the action or the custom control method for handling the information elicited from the user.</p>
            api_schema: <p>Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html">Action group OpenAPI schemas</a>.</p>
            action_group_state: <p>Specifies whether the action group is available for the agent to invoke or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>
            function_schema: <p>Contains details about the function schema for the action group or the JSON or YAML-formatted payload defining the schema.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.create_agent_action_group_request.CreateAgentActionGroupRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_agent_action_group_response.CreateAgentActionGroupResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent_action_group

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent_action_group.create_agent_action_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_agent_action_group_request.CreateAgentActionGroupRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "action_group_name": action_group_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if parent_action_group_signature is not None:
            input_["parent_action_group_signature"] = parent_action_group_signature
        if parent_action_group_signature_params is not None:
            input_["parent_action_group_signature_params"] = (
                parent_action_group_signature_params
            )
        if action_group_executor is not None:
            input_["action_group_executor"] = action_group_executor
        if api_schema is not None:
            input_["api_schema"] = api_schema
        if action_group_state is not None:
            input_["action_group_state"] = action_group_state
        if function_schema is not None:
            input_["function_schema"] = function_schema

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_agent_action_group(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        action_group_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        skip_resource_in_use_check: Optional[bool] = None,
    ) -> "capo_bedrock_agent.types.delete_agent_action_group_response.DeleteAgentActionGroupResponse":
        """<p>Deletes an action group in an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent that the action group belongs to.</p>
            agent_version: <p>The version of the agent that the action group belongs to.</p>
            action_group_id: <p>The unique identifier of the action group to delete.</p>
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
            req: "OperationRequest[capo_bedrock_agent.types.delete_agent_action_group_request.DeleteAgentActionGroupRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_agent_action_group_response.DeleteAgentActionGroupResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_action_group

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_action_group.delete_agent_action_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_agent_action_group_request.DeleteAgentActionGroupRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "action_group_id": action_group_id,
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

    def get_agent_action_group(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        action_group_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_agent_action_group_response.GetAgentActionGroupResponse":
        """<p>Gets information about an action group for an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent that the action group belongs to.</p>
            agent_version: <p>The version of the agent that the action group belongs to.</p>
            action_group_id: <p>The unique identifier of the action group for which to get information.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_agent_action_group_request.GetAgentActionGroupRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_agent_action_group_response.GetAgentActionGroupResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_action_group

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_action_group.get_agent_action_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_agent_action_group_request.GetAgentActionGroupRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "action_group_id": action_group_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_agent_action_groups(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_agent_action_groups_response.ListAgentActionGroupsResponse":
        """<p>Lists the action groups for an agent and information about each one.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_version: <p>The version of the agent.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_agent_action_groups_request.ListAgentActionGroupsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_agent_action_groups_response.ListAgentActionGroupsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_action_groups

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_action_groups.list_agent_action_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_agent_action_groups_request.ListAgentActionGroupsRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
        }
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

    def update_agent_action_group(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        action_group_id: "capo_bedrock_agent.types.id.Id",
        action_group_name: "capo_bedrock_agent.types.name.Name",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        parent_action_group_signature: Optional[
            "capo_bedrock_agent.types.action_group_signature.ActionGroupSignature"
        ] = None,
        parent_action_group_signature_params: Optional[
            "capo_bedrock_agent.types.action_group_signature_params.ActionGroupSignatureParams"
        ] = None,
        action_group_executor: Optional[
            "capo_bedrock_agent.types.action_group_executor.ActionGroupExecutor"
        ] = None,
        action_group_state: Optional[
            "capo_bedrock_agent.types.action_group_state.ActionGroupState"
        ] = None,
        api_schema: Optional["capo_bedrock_agent.types.api_schema.APISchema"] = None,
        function_schema: Optional[
            "capo_bedrock_agent.types.function_schema.FunctionSchema"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_agent_action_group_response.UpdateAgentActionGroupResponse":
        """<p>Updates the configuration for an action group for an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent for which to update the action group.</p>
            agent_version: <p>The unique identifier of the agent version for which to update the action group.</p>
            action_group_id: <p>The unique identifier of the action group.</p>
            action_group_name: <p>Specifies a new name for the action group.</p>
            description: <p>Specifies a new name for the action group.</p>
            parent_action_group_signature: <p>Update the built-in or computer use action for this action group. If you specify a value, you must leave the <code>description</code>, <code>apiSchema</code>, and <code>actionGroupExecutor</code> fields empty for this action group. </p> <ul> <li> <p>To allow your agent to request the user for additional information when trying to complete a task, set this field to <code>AMAZON.UserInput</code>. </p> </li> <li> <p>To allow your agent to generate, run, and troubleshoot code when trying to complete a task, set this field to <code>AMAZON.CodeInterpreter</code>.</p> </li> <li> <p>To allow your agent to use an Anthropic computer use tool, specify one of the following values. </p> <important> <p> Computer use is a new Anthropic Claude model capability (in beta) available with Anthropic Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. When operating computer use functionality, we recommend taking additional security precautions, such as executing computer actions in virtual environments with restricted data access and limited internet connectivity. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p> </important> <ul> <li> <p> <code>ANTHROPIC.Computer</code> - Gives the agent permission to use the mouse and keyboard and take screenshots.</p> </li> <li> <p> <code>ANTHROPIC.TextEditor</code> - Gives the agent permission to view, create and edit files.</p> </li> <li> <p> <code>ANTHROPIC.Bash</code> - Gives the agent permission to run commands in a bash shell.</p> </li> </ul> </li> </ul> <p>During orchestration, if your agent determines that it needs to invoke an API in an action group, but doesn't have enough information to complete the API request, it will invoke this action group instead and return an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Observation.html">Observation</a> reprompting the user for more information.</p>
            parent_action_group_signature_params: <p>The configuration settings for a computer use action.</p> <important> <p> Computer use is a new Anthropic Claude model capability (in beta) available with Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p> </important>
            action_group_executor: <p>The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking the action.</p>
            action_group_state: <p>Specifies whether the action group is available for the agent to invoke or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>
            api_schema: <p>Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html">Action group OpenAPI schemas</a>.</p>
            function_schema: <p>Contains details about the function schema for the action group or the JSON or YAML-formatted payload defining the schema.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.update_agent_action_group_request.UpdateAgentActionGroupRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_agent_action_group_response.UpdateAgentActionGroupResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_action_group

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_action_group.update_agent_action_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_agent_action_group_request.UpdateAgentActionGroupRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "action_group_id": action_group_id,
            "action_group_name": action_group_name,
        }
        if description is not None:
            input_["description"] = description
        if parent_action_group_signature is not None:
            input_["parent_action_group_signature"] = parent_action_group_signature
        if parent_action_group_signature_params is not None:
            input_["parent_action_group_signature_params"] = (
                parent_action_group_signature_params
            )
        if action_group_executor is not None:
            input_["action_group_executor"] = action_group_executor
        if action_group_state is not None:
            input_["action_group_state"] = action_group_state
        if api_schema is not None:
            input_["api_schema"] = api_schema
        if function_schema is not None:
            input_["function_schema"] = function_schema

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncActionGroupResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def create_agent_action_group(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        action_group_name: "capo_bedrock_agent.types.name.Name",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        parent_action_group_signature: Optional[
            "capo_bedrock_agent.types.action_group_signature.ActionGroupSignature"
        ] = None,
        parent_action_group_signature_params: Optional[
            "capo_bedrock_agent.types.action_group_signature_params.ActionGroupSignatureParams"
        ] = None,
        action_group_executor: Optional[
            "capo_bedrock_agent.types.action_group_executor.ActionGroupExecutor"
        ] = None,
        api_schema: Optional["capo_bedrock_agent.types.api_schema.APISchema"] = None,
        action_group_state: Optional[
            "capo_bedrock_agent.types.action_group_state.ActionGroupState"
        ] = None,
        function_schema: Optional[
            "capo_bedrock_agent.types.function_schema.FunctionSchema"
        ] = None,
    ) -> "capo_bedrock_agent.types.create_agent_action_group_response.CreateAgentActionGroupResponse":
        """<p>Creates an action group for an agent. An action group represents the actions that an agent can carry out for the customer by defining the APIs that an agent can call and the logic for calling them.</p> <p>To allow your agent to request the user for additional information when trying to complete a task, add an action group with the <code>parentActionGroupSignature</code> field set to <code>AMAZON.UserInput</code>. </p> <p>To allow your agent to generate, run, and troubleshoot code when trying to complete a task, add an action group with the <code>parentActionGroupSignature</code> field set to <code>AMAZON.CodeInterpreter</code>. </p> <p>You must leave the <code>description</code>, <code>apiSchema</code>, and <code>actionGroupExecutor</code> fields blank for this action group. During orchestration, if your agent determines that it needs to invoke an API in an action group, but doesn't have enough information to complete the API request, it will invoke this action group instead and return an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Observation.html">Observation</a> reprompting the user for more information.</p>

        Args:
            agent_id: <p>The unique identifier of the agent for which to create the action group.</p>
            agent_version: <p>The version of the agent for which to create the action group.</p>
            action_group_name: <p>The name to give the action group.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            description: <p>A description of the action group.</p>
            parent_action_group_signature: <p>Specify a built-in or computer use action for this action group. If you specify a value, you must leave the <code>description</code>, <code>apiSchema</code>, and <code>actionGroupExecutor</code> fields empty for this action group. </p> <ul> <li> <p>To allow your agent to request the user for additional information when trying to complete a task, set this field to <code>AMAZON.UserInput</code>. </p> </li> <li> <p>To allow your agent to generate, run, and troubleshoot code when trying to complete a task, set this field to <code>AMAZON.CodeInterpreter</code>.</p> </li> <li> <p>To allow your agent to use an Anthropic computer use tool, specify one of the following values. </p> <important> <p> Computer use is a new Anthropic Claude model capability (in beta) available with Anthropic Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. When operating computer use functionality, we recommend taking additional security precautions, such as executing computer actions in virtual environments with restricted data access and limited internet connectivity. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p> </important> <ul> <li> <p> <code>ANTHROPIC.Computer</code> - Gives the agent permission to use the mouse and keyboard and take screenshots.</p> </li> <li> <p> <code>ANTHROPIC.TextEditor</code> - Gives the agent permission to view, create and edit files.</p> </li> <li> <p> <code>ANTHROPIC.Bash</code> - Gives the agent permission to run commands in a bash shell.</p> </li> </ul> </li> </ul>
            parent_action_group_signature_params: <p>The configuration settings for a computer use action.</p> <important> <p> Computer use is a new Anthropic Claude model capability (in beta) available with Anthropic Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p> </important>
            action_group_executor: <p>The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking the action or the custom control method for handling the information elicited from the user.</p>
            api_schema: <p>Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html">Action group OpenAPI schemas</a>.</p>
            action_group_state: <p>Specifies whether the action group is available for the agent to invoke or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>
            function_schema: <p>Contains details about the function schema for the action group or the JSON or YAML-formatted payload defining the schema.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.create_agent_action_group_request.CreateAgentActionGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.create_agent_action_group_response.CreateAgentActionGroupResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent_action_group

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent_action_group.async_create_agent_action_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_agent_action_group_request.CreateAgentActionGroupRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "action_group_name": action_group_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if parent_action_group_signature is not None:
            input_["parent_action_group_signature"] = parent_action_group_signature
        if parent_action_group_signature_params is not None:
            input_["parent_action_group_signature_params"] = (
                parent_action_group_signature_params
            )
        if action_group_executor is not None:
            input_["action_group_executor"] = action_group_executor
        if api_schema is not None:
            input_["api_schema"] = api_schema
        if action_group_state is not None:
            input_["action_group_state"] = action_group_state
        if function_schema is not None:
            input_["function_schema"] = function_schema

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_agent_action_group(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        action_group_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        skip_resource_in_use_check: Optional[bool] = None,
    ) -> "capo_bedrock_agent.types.delete_agent_action_group_response.DeleteAgentActionGroupResponse":
        """<p>Deletes an action group in an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent that the action group belongs to.</p>
            agent_version: <p>The version of the agent that the action group belongs to.</p>
            action_group_id: <p>The unique identifier of the action group to delete.</p>
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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.delete_agent_action_group_request.DeleteAgentActionGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.delete_agent_action_group_response.DeleteAgentActionGroupResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_action_group

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_action_group.async_delete_agent_action_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_agent_action_group_request.DeleteAgentActionGroupRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "action_group_id": action_group_id,
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

    async def get_agent_action_group(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        action_group_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_agent_action_group_response.GetAgentActionGroupResponse":
        """<p>Gets information about an action group for an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent that the action group belongs to.</p>
            agent_version: <p>The version of the agent that the action group belongs to.</p>
            action_group_id: <p>The unique identifier of the action group for which to get information.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.get_agent_action_group_request.GetAgentActionGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.get_agent_action_group_response.GetAgentActionGroupResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_action_group

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_action_group.async_get_agent_action_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_agent_action_group_request.GetAgentActionGroupRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "action_group_id": action_group_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_agent_action_groups(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_agent_action_groups_response.ListAgentActionGroupsResponse":
        """<p>Lists the action groups for an agent and information about each one.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_version: <p>The version of the agent.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.list_agent_action_groups_request.ListAgentActionGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.list_agent_action_groups_response.ListAgentActionGroupsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_action_groups

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_action_groups.async_list_agent_action_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_agent_action_groups_request.ListAgentActionGroupsRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
        }
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

    async def update_agent_action_group(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        action_group_id: "capo_bedrock_agent.types.id.Id",
        action_group_name: "capo_bedrock_agent.types.name.Name",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        parent_action_group_signature: Optional[
            "capo_bedrock_agent.types.action_group_signature.ActionGroupSignature"
        ] = None,
        parent_action_group_signature_params: Optional[
            "capo_bedrock_agent.types.action_group_signature_params.ActionGroupSignatureParams"
        ] = None,
        action_group_executor: Optional[
            "capo_bedrock_agent.types.action_group_executor.ActionGroupExecutor"
        ] = None,
        action_group_state: Optional[
            "capo_bedrock_agent.types.action_group_state.ActionGroupState"
        ] = None,
        api_schema: Optional["capo_bedrock_agent.types.api_schema.APISchema"] = None,
        function_schema: Optional[
            "capo_bedrock_agent.types.function_schema.FunctionSchema"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_agent_action_group_response.UpdateAgentActionGroupResponse":
        """<p>Updates the configuration for an action group for an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent for which to update the action group.</p>
            agent_version: <p>The unique identifier of the agent version for which to update the action group.</p>
            action_group_id: <p>The unique identifier of the action group.</p>
            action_group_name: <p>Specifies a new name for the action group.</p>
            description: <p>Specifies a new name for the action group.</p>
            parent_action_group_signature: <p>Update the built-in or computer use action for this action group. If you specify a value, you must leave the <code>description</code>, <code>apiSchema</code>, and <code>actionGroupExecutor</code> fields empty for this action group. </p> <ul> <li> <p>To allow your agent to request the user for additional information when trying to complete a task, set this field to <code>AMAZON.UserInput</code>. </p> </li> <li> <p>To allow your agent to generate, run, and troubleshoot code when trying to complete a task, set this field to <code>AMAZON.CodeInterpreter</code>.</p> </li> <li> <p>To allow your agent to use an Anthropic computer use tool, specify one of the following values. </p> <important> <p> Computer use is a new Anthropic Claude model capability (in beta) available with Anthropic Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. When operating computer use functionality, we recommend taking additional security precautions, such as executing computer actions in virtual environments with restricted data access and limited internet connectivity. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p> </important> <ul> <li> <p> <code>ANTHROPIC.Computer</code> - Gives the agent permission to use the mouse and keyboard and take screenshots.</p> </li> <li> <p> <code>ANTHROPIC.TextEditor</code> - Gives the agent permission to view, create and edit files.</p> </li> <li> <p> <code>ANTHROPIC.Bash</code> - Gives the agent permission to run commands in a bash shell.</p> </li> </ul> </li> </ul> <p>During orchestration, if your agent determines that it needs to invoke an API in an action group, but doesn't have enough information to complete the API request, it will invoke this action group instead and return an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Observation.html">Observation</a> reprompting the user for more information.</p>
            parent_action_group_signature_params: <p>The configuration settings for a computer use action.</p> <important> <p> Computer use is a new Anthropic Claude model capability (in beta) available with Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p> </important>
            action_group_executor: <p>The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking the action.</p>
            action_group_state: <p>Specifies whether the action group is available for the agent to invoke or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>
            api_schema: <p>Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html">Action group OpenAPI schemas</a>.</p>
            function_schema: <p>Contains details about the function schema for the action group or the JSON or YAML-formatted payload defining the schema.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.update_agent_action_group_request.UpdateAgentActionGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.update_agent_action_group_response.UpdateAgentActionGroupResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_action_group

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_action_group.async_update_agent_action_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_agent_action_group_request.UpdateAgentActionGroupRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "action_group_id": action_group_id,
            "action_group_name": action_group_name,
        }
        if description is not None:
            input_["description"] = description
        if parent_action_group_signature is not None:
            input_["parent_action_group_signature"] = parent_action_group_signature
        if parent_action_group_signature_params is not None:
            input_["parent_action_group_signature_params"] = (
                parent_action_group_signature_params
            )
        if action_group_executor is not None:
            input_["action_group_executor"] = action_group_executor
        if action_group_state is not None:
            input_["action_group_state"] = action_group_state
        if api_schema is not None:
            input_["api_schema"] = api_schema
        if function_schema is not None:
            input_["function_schema"] = function_schema

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
