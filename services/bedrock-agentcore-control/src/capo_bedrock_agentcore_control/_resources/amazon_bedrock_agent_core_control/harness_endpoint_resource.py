from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

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
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.create_harness_endpoint_request
    import capo_bedrock_agentcore_control.types.create_harness_endpoint_response
    import capo_bedrock_agentcore_control.types.delete_harness_endpoint_request
    import capo_bedrock_agentcore_control.types.delete_harness_endpoint_response
    import capo_bedrock_agentcore_control.types.get_harness_endpoint_request
    import capo_bedrock_agentcore_control.types.get_harness_endpoint_response
    import capo_bedrock_agentcore_control.types.harness_endpoint
    import capo_bedrock_agentcore_control.types.harness_endpoint_description
    import capo_bedrock_agentcore_control.types.harness_endpoint_name
    import capo_bedrock_agentcore_control.types.harness_id
    import capo_bedrock_agentcore_control.types.harness_version
    import capo_bedrock_agentcore_control.types.list_harness_endpoints_request
    import capo_bedrock_agentcore_control.types.list_harness_endpoints_response
    import capo_bedrock_agentcore_control.types.max_results
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.tags_map
    import capo_bedrock_agentcore_control.types.update_harness_endpoint_request
    import capo_bedrock_agentcore_control.types.update_harness_endpoint_response
    from capo_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from capo_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class HarnessEndpointResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def create_harness_endpoint(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        endpoint_name: "capo_bedrock_agentcore_control.types.harness_endpoint_name.HarnessEndpointName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        target_version: Optional[
            "capo_bedrock_agentcore_control.types.harness_version.HarnessVersion"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.harness_endpoint_description.HarnessEndpointDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_harness_endpoint_response.CreateHarnessEndpointResponse":
        """<p>Operation to create a harness endpoint.</p>

        Args:
            harness_id: <p>The ID of the harness to create an endpoint for.</p>
            endpoint_name: <p>The name of the endpoint. Must start with a letter and contain only alphanumeric characters and underscores.</p>
            target_version: <p>The harness version that the endpoint points to and serves invocations from.</p>
            description: <p>A description of the endpoint.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>Tags to apply to the endpoint resource.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_harness_endpoint_request.CreateHarnessEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_harness_endpoint_response.CreateHarnessEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_harness_endpoint

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_harness_endpoint.create_harness_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateHarnessEndpoint")
        )
        input_: capo_bedrock_agentcore_control.types.create_harness_endpoint_request.CreateHarnessEndpointRequest = {
            "harness_id": harness_id,
            "endpoint_name": endpoint_name,
        }
        if target_version is not None:
            input_["target_version"] = target_version
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

    def delete_harness_endpoint(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        endpoint_name: "capo_bedrock_agentcore_control.types.harness_endpoint_name.HarnessEndpointName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_harness_endpoint_response.DeleteHarnessEndpointResponse":
        """<p>Operation to delete a harness endpoint.</p>

        Args:
            harness_id: <p>The ID of the harness that the endpoint belongs to.</p>
            endpoint_name: <p>The name of the endpoint to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_harness_endpoint_request.DeleteHarnessEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_harness_endpoint_response.DeleteHarnessEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_harness_endpoint

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_harness_endpoint.delete_harness_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteHarnessEndpoint")
        )
        input_: capo_bedrock_agentcore_control.types.delete_harness_endpoint_request.DeleteHarnessEndpointRequest = {
            "harness_id": harness_id,
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

    def get_harness_endpoint(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        endpoint_name: "capo_bedrock_agentcore_control.types.harness_endpoint_name.HarnessEndpointName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_harness_endpoint_response.GetHarnessEndpointResponse":
        """<p>Operation to get a single harness endpoint.</p>

        Args:
            harness_id: <p>The ID of the harness that the endpoint belongs to.</p>
            endpoint_name: <p>The name of the endpoint to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_harness_endpoint_request.GetHarnessEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_harness_endpoint_response.GetHarnessEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_harness_endpoint

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_harness_endpoint.get_harness_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetHarnessEndpoint")
        )
        input_: capo_bedrock_agentcore_control.types.get_harness_endpoint_request.GetHarnessEndpointRequest = {
            "harness_id": harness_id,
            "endpoint_name": endpoint_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_harness_endpoints(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_harness_endpoints_response.ListHarnessEndpointsResponse":
        """<p>Operation to list the endpoints of a harness.</p>

        Args:
            harness_id: <p>The ID of the harness whose endpoints are listed.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_harness_endpoints_request.ListHarnessEndpointsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_harness_endpoints_response.ListHarnessEndpointsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_harness_endpoints

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_harness_endpoints.list_harness_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListHarnessEndpoints")
        )
        input_: capo_bedrock_agentcore_control.types.list_harness_endpoints_request.ListHarnessEndpointsRequest = {
            "harness_id": harness_id
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

    def update_harness_endpoint(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        endpoint_name: "capo_bedrock_agentcore_control.types.harness_endpoint_name.HarnessEndpointName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        target_version: Optional[
            "capo_bedrock_agentcore_control.types.harness_version.HarnessVersion"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.harness_endpoint_description.HarnessEndpointDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_harness_endpoint_response.UpdateHarnessEndpointResponse":
        """<p>Operation to update a harness endpoint.</p>

        Args:
            harness_id: <p>The ID of the harness that the endpoint belongs to.</p>
            endpoint_name: <p>The name of the endpoint to update.</p>
            target_version: <p>The harness version that the endpoint points to. If not specified, the existing value is retained.</p>
            description: <p>A description of the endpoint. If not specified, the existing value is retained.</p>
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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_harness_endpoint_request.UpdateHarnessEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_harness_endpoint_response.UpdateHarnessEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_harness_endpoint

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_harness_endpoint.update_harness_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateHarnessEndpoint")
        )
        input_: capo_bedrock_agentcore_control.types.update_harness_endpoint_request.UpdateHarnessEndpointRequest = {
            "harness_id": harness_id,
            "endpoint_name": endpoint_name,
        }
        if target_version is not None:
            input_["target_version"] = target_version
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


class AsyncHarnessEndpointResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def create_harness_endpoint(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        endpoint_name: "capo_bedrock_agentcore_control.types.harness_endpoint_name.HarnessEndpointName",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        target_version: Optional[
            "capo_bedrock_agentcore_control.types.harness_version.HarnessVersion"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.harness_endpoint_description.HarnessEndpointDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_harness_endpoint_response.CreateHarnessEndpointResponse":
        """<p>Operation to create a harness endpoint.</p>

        Args:
            harness_id: <p>The ID of the harness to create an endpoint for.</p>
            endpoint_name: <p>The name of the endpoint. Must start with a letter and contain only alphanumeric characters and underscores.</p>
            target_version: <p>The harness version that the endpoint points to and serves invocations from.</p>
            description: <p>A description of the endpoint.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>Tags to apply to the endpoint resource.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.create_harness_endpoint_request.CreateHarnessEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.create_harness_endpoint_response.CreateHarnessEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_harness_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_harness_endpoint.async_create_harness_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateHarnessEndpoint")
        )
        input_: capo_bedrock_agentcore_control.types.create_harness_endpoint_request.CreateHarnessEndpointRequest = {
            "harness_id": harness_id,
            "endpoint_name": endpoint_name,
        }
        if target_version is not None:
            input_["target_version"] = target_version
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

    async def delete_harness_endpoint(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        endpoint_name: "capo_bedrock_agentcore_control.types.harness_endpoint_name.HarnessEndpointName",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_harness_endpoint_response.DeleteHarnessEndpointResponse":
        """<p>Operation to delete a harness endpoint.</p>

        Args:
            harness_id: <p>The ID of the harness that the endpoint belongs to.</p>
            endpoint_name: <p>The name of the endpoint to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.delete_harness_endpoint_request.DeleteHarnessEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.delete_harness_endpoint_response.DeleteHarnessEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_harness_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_harness_endpoint.async_delete_harness_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteHarnessEndpoint")
        )
        input_: capo_bedrock_agentcore_control.types.delete_harness_endpoint_request.DeleteHarnessEndpointRequest = {
            "harness_id": harness_id,
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

    async def get_harness_endpoint(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        endpoint_name: "capo_bedrock_agentcore_control.types.harness_endpoint_name.HarnessEndpointName",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_harness_endpoint_response.GetHarnessEndpointResponse":
        """<p>Operation to get a single harness endpoint.</p>

        Args:
            harness_id: <p>The ID of the harness that the endpoint belongs to.</p>
            endpoint_name: <p>The name of the endpoint to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.get_harness_endpoint_request.GetHarnessEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.get_harness_endpoint_response.GetHarnessEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_harness_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_harness_endpoint.async_get_harness_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetHarnessEndpoint")
        )
        input_: capo_bedrock_agentcore_control.types.get_harness_endpoint_request.GetHarnessEndpointRequest = {
            "harness_id": harness_id,
            "endpoint_name": endpoint_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_harness_endpoints(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_harness_endpoints_response.ListHarnessEndpointsResponse":
        """<p>Operation to list the endpoints of a harness.</p>

        Args:
            harness_id: <p>The ID of the harness whose endpoints are listed.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_harness_endpoints_request.ListHarnessEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_harness_endpoints_response.ListHarnessEndpointsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_harness_endpoints

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_harness_endpoints.async_list_harness_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListHarnessEndpoints")
        )
        input_: capo_bedrock_agentcore_control.types.list_harness_endpoints_request.ListHarnessEndpointsRequest = {
            "harness_id": harness_id
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

    async def update_harness_endpoint(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        endpoint_name: "capo_bedrock_agentcore_control.types.harness_endpoint_name.HarnessEndpointName",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        target_version: Optional[
            "capo_bedrock_agentcore_control.types.harness_version.HarnessVersion"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.harness_endpoint_description.HarnessEndpointDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_harness_endpoint_response.UpdateHarnessEndpointResponse":
        """<p>Operation to update a harness endpoint.</p>

        Args:
            harness_id: <p>The ID of the harness that the endpoint belongs to.</p>
            endpoint_name: <p>The name of the endpoint to update.</p>
            target_version: <p>The harness version that the endpoint points to. If not specified, the existing value is retained.</p>
            description: <p>A description of the endpoint. If not specified, the existing value is retained.</p>
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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.update_harness_endpoint_request.UpdateHarnessEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.update_harness_endpoint_response.UpdateHarnessEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_harness_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_harness_endpoint.async_update_harness_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateHarnessEndpoint")
        )
        input_: capo_bedrock_agentcore_control.types.update_harness_endpoint_request.UpdateHarnessEndpointRequest = {
            "harness_id": harness_id,
            "endpoint_name": endpoint_name,
        }
        if target_version is not None:
            input_["target_version"] = target_version
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
