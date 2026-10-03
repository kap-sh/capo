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
    import capo_bedrock_agent.types.agent_alias_id
    import capo_bedrock_agent.types.agent_alias_routing_configuration
    import capo_bedrock_agent.types.agent_alias_summary
    import capo_bedrock_agent.types.alias_invocation_state
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.create_agent_alias_request
    import capo_bedrock_agent.types.create_agent_alias_response
    import capo_bedrock_agent.types.delete_agent_alias_request
    import capo_bedrock_agent.types.delete_agent_alias_response
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.get_agent_alias_request
    import capo_bedrock_agent.types.get_agent_alias_response
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.list_agent_aliases_request
    import capo_bedrock_agent.types.list_agent_aliases_response
    import capo_bedrock_agent.types.max_results
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.tags_map
    import capo_bedrock_agent.types.update_agent_alias_request
    import capo_bedrock_agent.types.update_agent_alias_response
    from capo_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from capo_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class AliasResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def create_agent_alias(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_alias_name: "capo_bedrock_agent.types.name.Name",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        routing_configuration: Optional[
            "capo_bedrock_agent.types.agent_alias_routing_configuration.AgentAliasRoutingConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> (
        "capo_bedrock_agent.types.create_agent_alias_response.CreateAgentAliasResponse"
    ):
        """<p>Creates an alias of an agent that can be used to deploy the agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_alias_name: <p>The name of the alias.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            description: <p>A description of the alias of the agent.</p>
            routing_configuration: <p>Contains details about the routing configuration of the alias.</p>
            tags: <p>Any tags that you want to attach to the alias of the agent.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.create_agent_alias_request.CreateAgentAliasRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_agent_alias_response.CreateAgentAliasResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent_alias

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent_alias.create_agent_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_agent_alias_request.CreateAgentAliasRequest = {
            "agent_id": agent_id,
            "agent_alias_name": agent_alias_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if routing_configuration is not None:
            input_["routing_configuration"] = routing_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_agent_alias(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_alias_id: "capo_bedrock_agent.types.agent_alias_id.AgentAliasId",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> (
        "capo_bedrock_agent.types.delete_agent_alias_response.DeleteAgentAliasResponse"
    ):
        """<p>Deletes an alias of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent that the alias belongs to.</p>
            agent_alias_id: <p>The unique identifier of the alias to delete.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_agent_alias_request.DeleteAgentAliasRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_agent_alias_response.DeleteAgentAliasResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_alias

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_alias.delete_agent_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_agent_alias_request.DeleteAgentAliasRequest = {
            "agent_id": agent_id,
            "agent_alias_id": agent_alias_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_agent_alias(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_alias_id: "capo_bedrock_agent.types.agent_alias_id.AgentAliasId",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_agent_alias_response.GetAgentAliasResponse":
        """<p>Gets information about an alias of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent to which the alias to get information belongs.</p>
            agent_alias_id: <p>The unique identifier of the alias for which to get information.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_agent_alias_request.GetAgentAliasRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_agent_alias_response.GetAgentAliasResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_alias

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_alias.get_agent_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_agent_alias_request.GetAgentAliasRequest = {
            "agent_id": agent_id,
            "agent_alias_id": agent_alias_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_agent_aliases(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> (
        "capo_bedrock_agent.types.list_agent_aliases_response.ListAgentAliasesResponse"
    ):
        """<p>Lists the aliases of an agent and information about each one.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
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
            req: "OperationRequest[capo_bedrock_agent.types.list_agent_aliases_request.ListAgentAliasesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_agent_aliases_response.ListAgentAliasesResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_aliases

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_aliases.list_agent_aliases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_agent_aliases_request.ListAgentAliasesRequest = {
            "agent_id": agent_id
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

    def update_agent_alias(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_alias_id: "capo_bedrock_agent.types.agent_alias_id.AgentAliasId",
        agent_alias_name: "capo_bedrock_agent.types.name.Name",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        routing_configuration: Optional[
            "capo_bedrock_agent.types.agent_alias_routing_configuration.AgentAliasRoutingConfiguration"
        ] = None,
        alias_invocation_state: Optional[
            "capo_bedrock_agent.types.alias_invocation_state.AliasInvocationState"
        ] = None,
    ) -> (
        "capo_bedrock_agent.types.update_agent_alias_response.UpdateAgentAliasResponse"
    ):
        """<p>Updates configurations for an alias of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_alias_id: <p>The unique identifier of the alias.</p>
            agent_alias_name: <p>Specifies a new name for the alias.</p>
            description: <p>Specifies a new description for the alias.</p>
            routing_configuration: <p>Contains details about the routing configuration of the alias.</p>
            alias_invocation_state: <p>The invocation state for the agent alias. To pause the agent alias, set the value to <code>REJECT_INVOCATIONS</code>. To start the agent alias running again, set the value to <code>ACCEPT_INVOCATIONS</code>. Use the <code>GetAgentAlias</code>, or <code>ListAgentAliases</code>, operation to get the invocation state of an agent alias.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.update_agent_alias_request.UpdateAgentAliasRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_agent_alias_response.UpdateAgentAliasResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_alias

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_alias.update_agent_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_agent_alias_request.UpdateAgentAliasRequest = {
            "agent_id": agent_id,
            "agent_alias_id": agent_alias_id,
            "agent_alias_name": agent_alias_name,
        }
        if description is not None:
            input_["description"] = description
        if routing_configuration is not None:
            input_["routing_configuration"] = routing_configuration
        if alias_invocation_state is not None:
            input_["alias_invocation_state"] = alias_invocation_state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAliasResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def create_agent_alias(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_alias_name: "capo_bedrock_agent.types.name.Name",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        routing_configuration: Optional[
            "capo_bedrock_agent.types.agent_alias_routing_configuration.AgentAliasRoutingConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> (
        "capo_bedrock_agent.types.create_agent_alias_response.CreateAgentAliasResponse"
    ):
        """<p>Creates an alias of an agent that can be used to deploy the agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_alias_name: <p>The name of the alias.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            description: <p>A description of the alias of the agent.</p>
            routing_configuration: <p>Contains details about the routing configuration of the alias.</p>
            tags: <p>Any tags that you want to attach to the alias of the agent.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.create_agent_alias_request.CreateAgentAliasRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.create_agent_alias_response.CreateAgentAliasResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent_alias

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent_alias.async_create_agent_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_agent_alias_request.CreateAgentAliasRequest = {
            "agent_id": agent_id,
            "agent_alias_name": agent_alias_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if routing_configuration is not None:
            input_["routing_configuration"] = routing_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_agent_alias(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_alias_id: "capo_bedrock_agent.types.agent_alias_id.AgentAliasId",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> (
        "capo_bedrock_agent.types.delete_agent_alias_response.DeleteAgentAliasResponse"
    ):
        """<p>Deletes an alias of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent that the alias belongs to.</p>
            agent_alias_id: <p>The unique identifier of the alias to delete.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.delete_agent_alias_request.DeleteAgentAliasRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.delete_agent_alias_response.DeleteAgentAliasResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_alias

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_alias.async_delete_agent_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_agent_alias_request.DeleteAgentAliasRequest = {
            "agent_id": agent_id,
            "agent_alias_id": agent_alias_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_agent_alias(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_alias_id: "capo_bedrock_agent.types.agent_alias_id.AgentAliasId",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_agent_alias_response.GetAgentAliasResponse":
        """<p>Gets information about an alias of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent to which the alias to get information belongs.</p>
            agent_alias_id: <p>The unique identifier of the alias for which to get information.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.get_agent_alias_request.GetAgentAliasRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.get_agent_alias_response.GetAgentAliasResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_alias

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_alias.async_get_agent_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_agent_alias_request.GetAgentAliasRequest = {
            "agent_id": agent_id,
            "agent_alias_id": agent_alias_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_agent_aliases(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> (
        "capo_bedrock_agent.types.list_agent_aliases_response.ListAgentAliasesResponse"
    ):
        """<p>Lists the aliases of an agent and information about each one.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.list_agent_aliases_request.ListAgentAliasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.list_agent_aliases_response.ListAgentAliasesResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_aliases

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_aliases.async_list_agent_aliases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_agent_aliases_request.ListAgentAliasesRequest = {
            "agent_id": agent_id
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

    async def update_agent_alias(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_alias_id: "capo_bedrock_agent.types.agent_alias_id.AgentAliasId",
        agent_alias_name: "capo_bedrock_agent.types.name.Name",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        routing_configuration: Optional[
            "capo_bedrock_agent.types.agent_alias_routing_configuration.AgentAliasRoutingConfiguration"
        ] = None,
        alias_invocation_state: Optional[
            "capo_bedrock_agent.types.alias_invocation_state.AliasInvocationState"
        ] = None,
    ) -> (
        "capo_bedrock_agent.types.update_agent_alias_response.UpdateAgentAliasResponse"
    ):
        """<p>Updates configurations for an alias of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_alias_id: <p>The unique identifier of the alias.</p>
            agent_alias_name: <p>Specifies a new name for the alias.</p>
            description: <p>Specifies a new description for the alias.</p>
            routing_configuration: <p>Contains details about the routing configuration of the alias.</p>
            alias_invocation_state: <p>The invocation state for the agent alias. To pause the agent alias, set the value to <code>REJECT_INVOCATIONS</code>. To start the agent alias running again, set the value to <code>ACCEPT_INVOCATIONS</code>. Use the <code>GetAgentAlias</code>, or <code>ListAgentAliases</code>, operation to get the invocation state of an agent alias.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.update_agent_alias_request.UpdateAgentAliasRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.update_agent_alias_response.UpdateAgentAliasResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_alias

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_alias.async_update_agent_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_agent_alias_request.UpdateAgentAliasRequest = {
            "agent_id": agent_id,
            "agent_alias_id": agent_alias_id,
            "agent_alias_name": agent_alias_name,
        }
        if description is not None:
            input_["description"] = description
        if routing_configuration is not None:
            input_["routing_configuration"] = routing_configuration
        if alias_invocation_state is not None:
            input_["alias_invocation_state"] = alias_invocation_state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
