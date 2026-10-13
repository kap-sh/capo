from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_bedrock_agent_runtime._auth._signers
import capo_bedrock_agent_runtime._auth._sigv4
from capo_bedrock_agent_runtime._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agent_alias_id
    import capo_bedrock_agent_runtime.types.agent_id
    import capo_bedrock_agent_runtime.types.delete_agent_memory_request
    import capo_bedrock_agent_runtime.types.delete_agent_memory_response
    import capo_bedrock_agent_runtime.types.get_agent_memory_request
    import capo_bedrock_agent_runtime.types.get_agent_memory_response
    import capo_bedrock_agent_runtime.types.max_results
    import capo_bedrock_agent_runtime.types.memory
    import capo_bedrock_agent_runtime.types.memory_id
    import capo_bedrock_agent_runtime.types.memory_type
    import capo_bedrock_agent_runtime.types.next_token
    import capo_bedrock_agent_runtime.types.session_id
    from capo_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from capo_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class MemoryResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    def delete_agent_memory(
        self,
        agent_id: "capo_bedrock_agent_runtime.types.agent_id.AgentId",
        agent_alias_id: "capo_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        memory_id: Optional[
            "capo_bedrock_agent_runtime.types.memory_id.MemoryId"
        ] = None,
        session_id: Optional[
            "capo_bedrock_agent_runtime.types.session_id.SessionId"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.delete_agent_memory_response.DeleteAgentMemoryResponse":
        """<p>Deletes memory from the specified memory identifier.</p>

        Args:
            agent_id: <p>The unique identifier of the agent to which the alias belongs.</p>
            agent_alias_id: <p>The unique identifier of an alias of an agent.</p>
            memory_id: <p>The unique identifier of the memory.</p>
            session_id: <p>The unique session identifier of the memory.</p>

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
            req: "OperationRequest[capo_bedrock_agent_runtime.types.delete_agent_memory_request.DeleteAgentMemoryRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.delete_agent_memory_response.DeleteAgentMemoryResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.delete_agent_memory

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.delete_agent_memory.delete_agent_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAgentMemory")
        )
        input_: capo_bedrock_agent_runtime.types.delete_agent_memory_request.DeleteAgentMemoryRequest = {
            "agent_id": agent_id,
            "agent_alias_id": agent_alias_id,
        }
        if memory_id is not None:
            input_["memory_id"] = memory_id
        if session_id is not None:
            input_["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_agent_memory(
        self,
        agent_id: "capo_bedrock_agent_runtime.types.agent_id.AgentId",
        agent_alias_id: "capo_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId",
        memory_type: "capo_bedrock_agent_runtime.types.memory_type.MemoryType",
        memory_id: "capo_bedrock_agent_runtime.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
        max_items: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_agent_memory_response.GetAgentMemoryResponse":
        """<p>Gets the sessions stored in the memory of the agent.</p>

        Args:
            next_token: <p>If the total number of results is greater than the maxItems value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            max_items: <p>The maximum number of items to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            agent_id: <p>The unique identifier of the agent to which the alias belongs.</p>
            agent_alias_id: <p>The unique identifier of an alias of an agent.</p>
            memory_type: <p>The type of memory.</p>
            memory_id: <p>The unique identifier of the memory. </p>

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
            req: "OperationRequest[capo_bedrock_agent_runtime.types.get_agent_memory_request.GetAgentMemoryRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.get_agent_memory_response.GetAgentMemoryResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_agent_memory

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_agent_memory.get_agent_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAgentMemory")
        )
        input_: capo_bedrock_agent_runtime.types.get_agent_memory_request.GetAgentMemoryRequest = {
            "agent_id": agent_id,
            "agent_alias_id": agent_alias_id,
            "memory_type": memory_type,
            "memory_id": memory_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncMemoryResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    async def delete_agent_memory(
        self,
        agent_id: "capo_bedrock_agent_runtime.types.agent_id.AgentId",
        agent_alias_id: "capo_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        memory_id: Optional[
            "capo_bedrock_agent_runtime.types.memory_id.MemoryId"
        ] = None,
        session_id: Optional[
            "capo_bedrock_agent_runtime.types.session_id.SessionId"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.delete_agent_memory_response.DeleteAgentMemoryResponse":
        """<p>Deletes memory from the specified memory identifier.</p>

        Args:
            agent_id: <p>The unique identifier of the agent to which the alias belongs.</p>
            agent_alias_id: <p>The unique identifier of an alias of an agent.</p>
            memory_id: <p>The unique identifier of the memory.</p>
            session_id: <p>The unique session identifier of the memory.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.delete_agent_memory_request.DeleteAgentMemoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.delete_agent_memory_response.DeleteAgentMemoryResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.delete_agent_memory

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.delete_agent_memory.async_delete_agent_memory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAgentMemory")
        )
        input_: capo_bedrock_agent_runtime.types.delete_agent_memory_request.DeleteAgentMemoryRequest = {
            "agent_id": agent_id,
            "agent_alias_id": agent_alias_id,
        }
        if memory_id is not None:
            input_["memory_id"] = memory_id
        if session_id is not None:
            input_["session_id"] = session_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_agent_memory(
        self,
        agent_id: "capo_bedrock_agent_runtime.types.agent_id.AgentId",
        agent_alias_id: "capo_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId",
        memory_type: "capo_bedrock_agent_runtime.types.memory_type.MemoryType",
        memory_id: "capo_bedrock_agent_runtime.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
        max_items: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_agent_memory_response.GetAgentMemoryResponse":
        """<p>Gets the sessions stored in the memory of the agent.</p>

        Args:
            next_token: <p>If the total number of results is greater than the maxItems value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            max_items: <p>The maximum number of items to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            agent_id: <p>The unique identifier of the agent to which the alias belongs.</p>
            agent_alias_id: <p>The unique identifier of an alias of an agent.</p>
            memory_type: <p>The type of memory.</p>
            memory_id: <p>The unique identifier of the memory. </p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.get_agent_memory_request.GetAgentMemoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.get_agent_memory_response.GetAgentMemoryResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_agent_memory

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_agent_memory.async_get_agent_memory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAgentMemory")
        )
        input_: capo_bedrock_agent_runtime.types.get_agent_memory_request.GetAgentMemoryRequest = {
            "agent_id": agent_id,
            "agent_alias_id": agent_alias_id,
            "memory_type": memory_type,
            "memory_id": memory_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
