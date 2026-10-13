from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_bedrock_agentcore_control._auth._signers
import capo_bedrock_agentcore_control._auth._sigv4
from capo_bedrock_agentcore_control._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_endpoint_description
    import capo_bedrock_agentcore_control.types.agent_runtime_endpoint
    import capo_bedrock_agentcore_control.types.agent_runtime_id
    import capo_bedrock_agentcore_control.types.agent_runtime_version
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request
    import capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response
    import capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request
    import capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response
    import capo_bedrock_agentcore_control.types.endpoint_name
    import capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request
    import capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response
    import capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_request
    import capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response
    import capo_bedrock_agentcore_control.types.max_results
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.tags_map
    import capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request
    import capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_response
    from capo_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from capo_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class AgentEndpointResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def create(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        name: "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        agent_runtime_version: Optional[
            "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.agent_endpoint_description.AgentEndpointDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response.CreateAgentRuntimeEndpointResponse":
        """<p>Creates an AgentCore Runtime endpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to create an endpoint for.</p>
            name: <p>The name of the AgentCore Runtime endpoint.</p>
            agent_runtime_version: <p>The version of the AgentCore Runtime to use for the endpoint.</p>
            description: <p>The description of the AgentCore Runtime endpoint.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>A map of tag keys and values to assign to the agent runtime endpoint. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request.CreateAgentRuntimeEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response.CreateAgentRuntimeEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime_endpoint

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime_endpoint.create_agent_runtime_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request.CreateAgentRuntimeEndpointRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request

            return capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response.CreateAgentRuntimeEndpointResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response

            return capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateAgentRuntimeEndpoint",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request.CreateAgentRuntimeEndpointRequest = {
            "agent_runtime_id": agent_runtime_id,
            "name": name,
        }
        if agent_runtime_version is not None:
            input_["agent_runtime_version"] = agent_runtime_version
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        endpoint_name: "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response.GetAgentRuntimeEndpointResponse":
        """<p>Gets information about an Amazon Secure AgentEndpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>
            endpoint_name: <p>The name of the AgentCore Runtime endpoint to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request.GetAgentRuntimeEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response.GetAgentRuntimeEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime_endpoint

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime_endpoint.get_agent_runtime_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request.GetAgentRuntimeEndpointRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request

            return capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response.GetAgentRuntimeEndpointResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response

            return capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetAgentRuntimeEndpoint",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request.GetAgentRuntimeEndpointRequest = {
            "agent_runtime_id": agent_runtime_id,
            "endpoint_name": endpoint_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        endpoint_name: "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        agent_runtime_version: Optional[
            "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.agent_endpoint_description.AgentEndpointDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_response.UpdateAgentRuntimeEndpointResponse":
        """<p>Updates an existing Amazon Bedrock AgentCore Runtime endpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>
            endpoint_name: <p>The name of the AgentCore Runtime endpoint to update.</p>
            agent_runtime_version: <p>The updated version of the AgentCore Runtime for the endpoint.</p>
            description: <p>The updated description of the AgentCore Runtime endpoint.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request.UpdateAgentRuntimeEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_response.UpdateAgentRuntimeEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime_endpoint

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime_endpoint.update_agent_runtime_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request.UpdateAgentRuntimeEndpointRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request

            return capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateAgentRuntimeEndpoint", redact_input=_redact_input),
        )
        input_: capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request.UpdateAgentRuntimeEndpointRequest = {
            "agent_runtime_id": agent_runtime_id,
            "endpoint_name": endpoint_name,
        }
        if agent_runtime_version is not None:
            input_["agent_runtime_version"] = agent_runtime_version
        if description is not None:
            input_["description"] = description
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

    def delete(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        endpoint_name: "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response.DeleteAgentRuntimeEndpointResponse":
        """<p>Deletes an AgentCore Runtime endpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>
            endpoint_name: <p>The name of the AgentCore Runtime endpoint to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request.DeleteAgentRuntimeEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response.DeleteAgentRuntimeEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime_endpoint

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime_endpoint.delete_agent_runtime_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request.DeleteAgentRuntimeEndpointRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request

            return capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response.DeleteAgentRuntimeEndpointResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response

            return capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "DeleteAgentRuntimeEndpoint",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request.DeleteAgentRuntimeEndpointRequest = {
            "agent_runtime_id": agent_runtime_id,
            "endpoint_name": endpoint_name,
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
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response.ListAgentRuntimeEndpointsResponse":
        """<p>Lists all endpoints for a specific Amazon Secure Agent.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to list endpoints for.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_request.ListAgentRuntimeEndpointsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response.ListAgentRuntimeEndpointsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_endpoints

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_endpoints.list_agent_runtime_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response.ListAgentRuntimeEndpointsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response

            return capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListAgentRuntimeEndpoints", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_request.ListAgentRuntimeEndpointsRequest = {
            "agent_runtime_id": agent_runtime_id
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


class AsyncAgentEndpointResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def create(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        name: "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        agent_runtime_version: Optional[
            "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.agent_endpoint_description.AgentEndpointDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response.CreateAgentRuntimeEndpointResponse":
        """<p>Creates an AgentCore Runtime endpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to create an endpoint for.</p>
            name: <p>The name of the AgentCore Runtime endpoint.</p>
            agent_runtime_version: <p>The version of the AgentCore Runtime to use for the endpoint.</p>
            description: <p>The description of the AgentCore Runtime endpoint.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>A map of tag keys and values to assign to the agent runtime endpoint. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request.CreateAgentRuntimeEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response.CreateAgentRuntimeEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime_endpoint.async_create_agent_runtime_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request.CreateAgentRuntimeEndpointRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request

            return capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response.CreateAgentRuntimeEndpointResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response

            return capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateAgentRuntimeEndpoint",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request.CreateAgentRuntimeEndpointRequest = {
            "agent_runtime_id": agent_runtime_id,
            "name": name,
        }
        if agent_runtime_version is not None:
            input_["agent_runtime_version"] = agent_runtime_version
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        endpoint_name: "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response.GetAgentRuntimeEndpointResponse":
        """<p>Gets information about an Amazon Secure AgentEndpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>
            endpoint_name: <p>The name of the AgentCore Runtime endpoint to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request.GetAgentRuntimeEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response.GetAgentRuntimeEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime_endpoint.async_get_agent_runtime_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request.GetAgentRuntimeEndpointRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request

            return capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response.GetAgentRuntimeEndpointResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response

            return capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetAgentRuntimeEndpoint",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request.GetAgentRuntimeEndpointRequest = {
            "agent_runtime_id": agent_runtime_id,
            "endpoint_name": endpoint_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        endpoint_name: "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        agent_runtime_version: Optional[
            "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.agent_endpoint_description.AgentEndpointDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_response.UpdateAgentRuntimeEndpointResponse":
        """<p>Updates an existing Amazon Bedrock AgentCore Runtime endpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>
            endpoint_name: <p>The name of the AgentCore Runtime endpoint to update.</p>
            agent_runtime_version: <p>The updated version of the AgentCore Runtime for the endpoint.</p>
            description: <p>The updated description of the AgentCore Runtime endpoint.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request.UpdateAgentRuntimeEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_response.UpdateAgentRuntimeEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime_endpoint.async_update_agent_runtime_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request.UpdateAgentRuntimeEndpointRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request

            return capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateAgentRuntimeEndpoint", redact_input=_redact_input),
        )
        input_: capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request.UpdateAgentRuntimeEndpointRequest = {
            "agent_runtime_id": agent_runtime_id,
            "endpoint_name": endpoint_name,
        }
        if agent_runtime_version is not None:
            input_["agent_runtime_version"] = agent_runtime_version
        if description is not None:
            input_["description"] = description
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

    async def delete(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        endpoint_name: "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response.DeleteAgentRuntimeEndpointResponse":
        """<p>Deletes an AgentCore Runtime endpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>
            endpoint_name: <p>The name of the AgentCore Runtime endpoint to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request.DeleteAgentRuntimeEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response.DeleteAgentRuntimeEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime_endpoint.async_delete_agent_runtime_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request.DeleteAgentRuntimeEndpointRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request

            return capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response.DeleteAgentRuntimeEndpointResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response

            return capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "DeleteAgentRuntimeEndpoint",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request.DeleteAgentRuntimeEndpointRequest = {
            "agent_runtime_id": agent_runtime_id,
            "endpoint_name": endpoint_name,
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
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response.ListAgentRuntimeEndpointsResponse":
        """<p>Lists all endpoints for a specific Amazon Secure Agent.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to list endpoints for.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_request.ListAgentRuntimeEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response.ListAgentRuntimeEndpointsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_endpoints

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_endpoints.async_list_agent_runtime_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response.ListAgentRuntimeEndpointsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response

            return capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListAgentRuntimeEndpoints", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_request.ListAgentRuntimeEndpointsRequest = {
            "agent_runtime_id": agent_runtime_id
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
