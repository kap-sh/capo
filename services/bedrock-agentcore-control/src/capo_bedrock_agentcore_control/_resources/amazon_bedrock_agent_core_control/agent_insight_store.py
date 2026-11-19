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
    import capo_bedrock_agentcore_control.types.agent_insight_store_enablement_status
    import capo_bedrock_agentcore_control.types.agent_insight_store_encryption_configuration
    import capo_bedrock_agentcore_control.types.agent_insight_store_id
    import capo_bedrock_agentcore_control.types.agent_insight_store_summary
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.get_agent_insight_store_request
    import capo_bedrock_agentcore_control.types.get_agent_insight_store_response
    import capo_bedrock_agentcore_control.types.list_agent_insight_stores_request
    import capo_bedrock_agentcore_control.types.list_agent_insight_stores_response
    import capo_bedrock_agentcore_control.types.update_agent_insight_store_request
    import capo_bedrock_agentcore_control.types.update_agent_insight_store_response
    from capo_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from capo_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class AgentInsightStore:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def read(
        self,
        agent_insight_store_id: "capo_bedrock_agentcore_control.types.agent_insight_store_id.AgentInsightStoreId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_agent_insight_store_response.GetAgentInsightStoreResponse":
        """Returns the account's service-defined default Agent Insight Store. The logical default exists for every enrolled account; its backing state may be initialized on first access.

        Args:
            agent_insight_store_id: <p>Specifies the unique identifier of the Agent Insight Store to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_agent_insight_store_request.GetAgentInsightStoreRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_agent_insight_store_response.GetAgentInsightStoreResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_insight_store

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_insight_store.get_agent_insight_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.get_agent_insight_store_response.GetAgentInsightStoreResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.get_agent_insight_store_response

            return capo_bedrock_agentcore_control.types.get_agent_insight_store_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAgentInsightStore", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.get_agent_insight_store_request.GetAgentInsightStoreRequest = {
            "agent_insight_store_id": agent_insight_store_id
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
        agent_insight_store_id: "capo_bedrock_agentcore_control.types.agent_insight_store_id.AgentInsightStoreId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        enablement_status: Optional[
            "capo_bedrock_agentcore_control.types.agent_insight_store_enablement_status.AgentInsightStoreEnablementStatus"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_agentcore_control.types.agent_insight_store_encryption_configuration.AgentInsightStoreEncryptionConfiguration"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_agent_insight_store_response.UpdateAgentInsightStoreResponse":
        """<p>Updates the enablement status or encryption configuration of an Agent Insight Store.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            agent_insight_store_id: <p>Specifies the unique identifier of the Agent Insight Store to update.</p>
            enablement_status: <p>Specifies whether the Agent Insight Store accepts new Agent Insights. If you don't specify this parameter, the store's current enablement setting remains unchanged.</p>
            encryption_configuration: <p>Specifies the encryption mode and key configuration to use for new Agent Insights. If you don't specify this parameter, the store's current encryption configuration remains unchanged.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_agent_insight_store_request.UpdateAgentInsightStoreRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_agent_insight_store_response.UpdateAgentInsightStoreResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_insight_store

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_insight_store.update_agent_insight_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.update_agent_insight_store_response.UpdateAgentInsightStoreResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_agent_insight_store_response

            return capo_bedrock_agentcore_control.types.update_agent_insight_store_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateAgentInsightStore", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.update_agent_insight_store_request.UpdateAgentInsightStoreRequest = {
            "agent_insight_store_id": agent_insight_store_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if enablement_status is not None:
            input_["enablement_status"] = enablement_status
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_agent_insight_stores_response.ListAgentInsightStoresResponse":
        """Lists the account's service-defined default Agent Insight Store. The singleton backing state may be initialized on first access.

        Args:
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_agent_insight_stores_request.ListAgentInsightStoresRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_agent_insight_stores_response.ListAgentInsightStoresResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_insight_stores

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_insight_stores.list_agent_insight_stores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAgentInsightStores")
        )
        input_: capo_bedrock_agentcore_control.types.list_agent_insight_stores_request.ListAgentInsightStoresRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAgentInsightStore:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def read(
        self,
        agent_insight_store_id: "capo_bedrock_agentcore_control.types.agent_insight_store_id.AgentInsightStoreId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_agent_insight_store_response.GetAgentInsightStoreResponse":
        """Returns the account's service-defined default Agent Insight Store. The logical default exists for every enrolled account; its backing state may be initialized on first access.

        Args:
            agent_insight_store_id: <p>Specifies the unique identifier of the Agent Insight Store to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.get_agent_insight_store_request.GetAgentInsightStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.get_agent_insight_store_response.GetAgentInsightStoreResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_insight_store

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_insight_store.async_get_agent_insight_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.get_agent_insight_store_response.GetAgentInsightStoreResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.get_agent_insight_store_response

            return capo_bedrock_agentcore_control.types.get_agent_insight_store_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAgentInsightStore", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.get_agent_insight_store_request.GetAgentInsightStoreRequest = {
            "agent_insight_store_id": agent_insight_store_id
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
        agent_insight_store_id: "capo_bedrock_agentcore_control.types.agent_insight_store_id.AgentInsightStoreId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        enablement_status: Optional[
            "capo_bedrock_agentcore_control.types.agent_insight_store_enablement_status.AgentInsightStoreEnablementStatus"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_agentcore_control.types.agent_insight_store_encryption_configuration.AgentInsightStoreEncryptionConfiguration"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_agent_insight_store_response.UpdateAgentInsightStoreResponse":
        """<p>Updates the enablement status or encryption configuration of an Agent Insight Store.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            agent_insight_store_id: <p>Specifies the unique identifier of the Agent Insight Store to update.</p>
            enablement_status: <p>Specifies whether the Agent Insight Store accepts new Agent Insights. If you don't specify this parameter, the store's current enablement setting remains unchanged.</p>
            encryption_configuration: <p>Specifies the encryption mode and key configuration to use for new Agent Insights. If you don't specify this parameter, the store's current encryption configuration remains unchanged.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.update_agent_insight_store_request.UpdateAgentInsightStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.update_agent_insight_store_response.UpdateAgentInsightStoreResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_insight_store

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_insight_store.async_update_agent_insight_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.update_agent_insight_store_response.UpdateAgentInsightStoreResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_agent_insight_store_response

            return capo_bedrock_agentcore_control.types.update_agent_insight_store_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateAgentInsightStore", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.update_agent_insight_store_request.UpdateAgentInsightStoreRequest = {
            "agent_insight_store_id": agent_insight_store_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if enablement_status is not None:
            input_["enablement_status"] = enablement_status
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_agent_insight_stores_response.ListAgentInsightStoresResponse":
        """Lists the account's service-defined default Agent Insight Store. The singleton backing state may be initialized on first access.

        Args:
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_agent_insight_stores_request.ListAgentInsightStoresRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_agent_insight_stores_response.ListAgentInsightStoresResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_insight_stores

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_insight_stores.async_list_agent_insight_stores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAgentInsightStores")
        )
        input_: capo_bedrock_agentcore_control.types.list_agent_insight_stores_request.ListAgentInsightStoresRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
