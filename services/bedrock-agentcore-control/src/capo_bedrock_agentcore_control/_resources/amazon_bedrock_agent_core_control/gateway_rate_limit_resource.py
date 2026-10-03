from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_bedrock_agentcore_control._auth._signers
import capo_bedrock_agentcore_control._auth._sigv4
from capo_bedrock_agentcore_control._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.batch_put_gateway_rate_limits_request
    import capo_bedrock_agentcore_control.types.batch_put_gateway_rate_limits_response
    import capo_bedrock_agentcore_control.types.batch_put_limit_entries
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.create_gateway_rate_limit_request
    import capo_bedrock_agentcore_control.types.create_gateway_rate_limit_response
    import capo_bedrock_agentcore_control.types.delete_gateway_rate_limit_request
    import capo_bedrock_agentcore_control.types.delete_gateway_rate_limit_response
    import capo_bedrock_agentcore_control.types.dimension_keys
    import capo_bedrock_agentcore_control.types.gateway_identifier
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_description
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_detail
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_id
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_max_results
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_next_token
    import capo_bedrock_agentcore_control.types.get_gateway_rate_limit_request
    import capo_bedrock_agentcore_control.types.get_gateway_rate_limit_response
    import capo_bedrock_agentcore_control.types.limit_entries
    import capo_bedrock_agentcore_control.types.list_gateway_rate_limits_request
    import capo_bedrock_agentcore_control.types.list_gateway_rate_limits_response
    import capo_bedrock_agentcore_control.types.update_gateway_rate_limit_request
    import capo_bedrock_agentcore_control.types.update_gateway_rate_limit_response
    from capo_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from capo_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class GatewayRateLimitResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def batch_put_gateway_rate_limits(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rate_limits: "capo_bedrock_agentcore_control.types.batch_put_limit_entries.BatchPutLimitEntries",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.batch_put_gateway_rate_limits_response.BatchPutGatewayRateLimitsResponse":
        """<p>Atomically creates or updates multiple rate limits for a gateway. The operation updates existing limits with matching keys and creates new limits for new keys. If the operation fails, the service applies no changes. Retry the request after resolving the issue.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            rate_limits: <p>The complete set of rate limits for this gateway. This operation replaces all existing rate limits in a single request. If the operation fails, no rate limits are changed.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.batch_put_gateway_rate_limits_request.BatchPutGatewayRateLimitsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.batch_put_gateway_rate_limits_response.BatchPutGatewayRateLimitsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.batch_put_gateway_rate_limits

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.batch_put_gateway_rate_limits.batch_put_gateway_rate_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.batch_put_gateway_rate_limits_request.BatchPutGatewayRateLimitsRequest = {
            "gateway_identifier": gateway_identifier,
            "rate_limits": rate_limits,
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

    def create_gateway_rate_limit(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        dimension_keys: "capo_bedrock_agentcore_control.types.dimension_keys.DimensionKeys",
        entries: "capo_bedrock_agentcore_control.types.limit_entries.LimitEntries",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        rate_limit_id: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_description.GatewayRateLimitDescription"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_gateway_rate_limit_response.CreateGatewayRateLimitResponse":
        """<p>Creates a rate limit for a gateway. Rate limits define throttling rules for each dimension that control request rates, token consumption rates, and concurrent connections through the gateway.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway to create the rate limit for.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            rate_limit_id: <p>An optional customer-defined identifier for the rate limit. If not provided, the system generates one.</p>
            description: <p>An optional human-readable description for this rate limit. If not provided, the rate limit is created without a description.</p>
            dimension_keys: <p>The ordered list of dimension key names that define the scope of this rate limit. Must be unique per gateway—no two rate limits can share the same dimension keys.</p>
            entries: <p>The rule entries that map dimension values to rate configurations.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_gateway_rate_limit_request.CreateGatewayRateLimitRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_gateway_rate_limit_response.CreateGatewayRateLimitResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway_rate_limit

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway_rate_limit.create_gateway_rate_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_gateway_rate_limit_request.CreateGatewayRateLimitRequest = {
            "gateway_identifier": gateway_identifier,
            "dimension_keys": dimension_keys,
            "entries": entries,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if rate_limit_id is not None:
            input_["rate_limit_id"] = rate_limit_id
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_gateway_rate_limit(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rate_limit_id: "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_gateway_rate_limit_response.DeleteGatewayRateLimitResponse":
        """<p>Deletes a gateway rate limit.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway.</p>
            rate_limit_id: <p>The unique identifier of the rate limit to delete.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_gateway_rate_limit_request.DeleteGatewayRateLimitRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_gateway_rate_limit_response.DeleteGatewayRateLimitResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway_rate_limit

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway_rate_limit.delete_gateway_rate_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_gateway_rate_limit_request.DeleteGatewayRateLimitRequest = {
            "gateway_identifier": gateway_identifier,
            "rate_limit_id": rate_limit_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_gateway_rate_limit(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rate_limit_id: "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_gateway_rate_limit_response.GetGatewayRateLimitResponse":
        """<p>Retrieves information about a gateway rate limit.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway.</p>
            rate_limit_id: <p>The unique identifier of the rate limit to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_gateway_rate_limit_request.GetGatewayRateLimitRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_gateway_rate_limit_response.GetGatewayRateLimitResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway_rate_limit

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway_rate_limit.get_gateway_rate_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_gateway_rate_limit_request.GetGatewayRateLimitRequest = {
            "gateway_identifier": gateway_identifier,
            "rate_limit_id": rate_limit_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_gateway_rate_limits(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_max_results.GatewayRateLimitMaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_next_token.GatewayRateLimitNextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_gateway_rate_limits_response.ListGatewayRateLimitsResponse":
        """<p>Lists all rate limits for a gateway. Results are paginated. Use the <code>nextToken</code> parameter to retrieve additional results.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>The token to use to retrieve the next page of results. Use the value returned in a previous <code>ListGatewayRateLimits</code> response.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_gateway_rate_limits_request.ListGatewayRateLimitsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_gateway_rate_limits_response.ListGatewayRateLimitsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateway_rate_limits

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateway_rate_limits.list_gateway_rate_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_gateway_rate_limits_request.ListGatewayRateLimitsRequest = {
            "gateway_identifier": gateway_identifier
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

    def update_gateway_rate_limit(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rate_limit_id: "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId",
        entries: "capo_bedrock_agentcore_control.types.limit_entries.LimitEntries",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_description.GatewayRateLimitDescription"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_gateway_rate_limit_response.UpdateGatewayRateLimitResponse":
        """<p>Updates the entries of a gateway rate limit. The dimension keys are immutable after creation.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway.</p>
            rate_limit_id: <p>The unique identifier of the rate limit to update.</p>
            description: <p>The updated human-readable description for this rate limit.</p>
            entries: <p>The updated rule entries. The dimension keys are immutable after creation and cannot be changed.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_gateway_rate_limit_request.UpdateGatewayRateLimitRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_gateway_rate_limit_response.UpdateGatewayRateLimitResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway_rate_limit

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway_rate_limit.update_gateway_rate_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_gateway_rate_limit_request.UpdateGatewayRateLimitRequest = {
            "gateway_identifier": gateway_identifier,
            "rate_limit_id": rate_limit_id,
            "entries": entries,
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncGatewayRateLimitResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def batch_put_gateway_rate_limits(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rate_limits: "capo_bedrock_agentcore_control.types.batch_put_limit_entries.BatchPutLimitEntries",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.batch_put_gateway_rate_limits_response.BatchPutGatewayRateLimitsResponse":
        """<p>Atomically creates or updates multiple rate limits for a gateway. The operation updates existing limits with matching keys and creates new limits for new keys. If the operation fails, the service applies no changes. Retry the request after resolving the issue.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            rate_limits: <p>The complete set of rate limits for this gateway. This operation replaces all existing rate limits in a single request. If the operation fails, no rate limits are changed.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.batch_put_gateway_rate_limits_request.BatchPutGatewayRateLimitsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.batch_put_gateway_rate_limits_response.BatchPutGatewayRateLimitsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.batch_put_gateway_rate_limits

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.batch_put_gateway_rate_limits.async_batch_put_gateway_rate_limits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.batch_put_gateway_rate_limits_request.BatchPutGatewayRateLimitsRequest = {
            "gateway_identifier": gateway_identifier,
            "rate_limits": rate_limits,
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

    async def create_gateway_rate_limit(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        dimension_keys: "capo_bedrock_agentcore_control.types.dimension_keys.DimensionKeys",
        entries: "capo_bedrock_agentcore_control.types.limit_entries.LimitEntries",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        rate_limit_id: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_description.GatewayRateLimitDescription"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_gateway_rate_limit_response.CreateGatewayRateLimitResponse":
        """<p>Creates a rate limit for a gateway. Rate limits define throttling rules for each dimension that control request rates, token consumption rates, and concurrent connections through the gateway.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway to create the rate limit for.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            rate_limit_id: <p>An optional customer-defined identifier for the rate limit. If not provided, the system generates one.</p>
            description: <p>An optional human-readable description for this rate limit. If not provided, the rate limit is created without a description.</p>
            dimension_keys: <p>The ordered list of dimension key names that define the scope of this rate limit. Must be unique per gateway—no two rate limits can share the same dimension keys.</p>
            entries: <p>The rule entries that map dimension values to rate configurations.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.create_gateway_rate_limit_request.CreateGatewayRateLimitRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.create_gateway_rate_limit_response.CreateGatewayRateLimitResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway_rate_limit

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway_rate_limit.async_create_gateway_rate_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_gateway_rate_limit_request.CreateGatewayRateLimitRequest = {
            "gateway_identifier": gateway_identifier,
            "dimension_keys": dimension_keys,
            "entries": entries,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if rate_limit_id is not None:
            input_["rate_limit_id"] = rate_limit_id
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_gateway_rate_limit(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rate_limit_id: "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_gateway_rate_limit_response.DeleteGatewayRateLimitResponse":
        """<p>Deletes a gateway rate limit.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway.</p>
            rate_limit_id: <p>The unique identifier of the rate limit to delete.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.delete_gateway_rate_limit_request.DeleteGatewayRateLimitRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.delete_gateway_rate_limit_response.DeleteGatewayRateLimitResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway_rate_limit

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway_rate_limit.async_delete_gateway_rate_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_gateway_rate_limit_request.DeleteGatewayRateLimitRequest = {
            "gateway_identifier": gateway_identifier,
            "rate_limit_id": rate_limit_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_gateway_rate_limit(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rate_limit_id: "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_gateway_rate_limit_response.GetGatewayRateLimitResponse":
        """<p>Retrieves information about a gateway rate limit.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway.</p>
            rate_limit_id: <p>The unique identifier of the rate limit to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.get_gateway_rate_limit_request.GetGatewayRateLimitRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.get_gateway_rate_limit_response.GetGatewayRateLimitResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway_rate_limit

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway_rate_limit.async_get_gateway_rate_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_gateway_rate_limit_request.GetGatewayRateLimitRequest = {
            "gateway_identifier": gateway_identifier,
            "rate_limit_id": rate_limit_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_gateway_rate_limits(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_max_results.GatewayRateLimitMaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_next_token.GatewayRateLimitNextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_gateway_rate_limits_response.ListGatewayRateLimitsResponse":
        """<p>Lists all rate limits for a gateway. Results are paginated. Use the <code>nextToken</code> parameter to retrieve additional results.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>The token to use to retrieve the next page of results. Use the value returned in a previous <code>ListGatewayRateLimits</code> response.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_gateway_rate_limits_request.ListGatewayRateLimitsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_gateway_rate_limits_response.ListGatewayRateLimitsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateway_rate_limits

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateway_rate_limits.async_list_gateway_rate_limits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_gateway_rate_limits_request.ListGatewayRateLimitsRequest = {
            "gateway_identifier": gateway_identifier
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

    async def update_gateway_rate_limit(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rate_limit_id: "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId",
        entries: "capo_bedrock_agentcore_control.types.limit_entries.LimitEntries",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_description.GatewayRateLimitDescription"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_gateway_rate_limit_response.UpdateGatewayRateLimitResponse":
        """<p>Updates the entries of a gateway rate limit. The dimension keys are immutable after creation.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway.</p>
            rate_limit_id: <p>The unique identifier of the rate limit to update.</p>
            description: <p>The updated human-readable description for this rate limit.</p>
            entries: <p>The updated rule entries. The dimension keys are immutable after creation and cannot be changed.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.update_gateway_rate_limit_request.UpdateGatewayRateLimitRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.update_gateway_rate_limit_response.UpdateGatewayRateLimitResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway_rate_limit

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway_rate_limit.async_update_gateway_rate_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_gateway_rate_limit_request.UpdateGatewayRateLimitRequest = {
            "gateway_identifier": gateway_identifier,
            "rate_limit_id": rate_limit_id,
            "entries": entries,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
