from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_bedrock_agentcore._auth._signers
import capo_bedrock_agentcore._auth._sigv4
from capo_bedrock_agentcore._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.capacity_provider_id
    import capo_bedrock_agentcore.types.delete_capacity_provider_session_request
    import capo_bedrock_agentcore.types.delete_capacity_provider_session_response
    import capo_bedrock_agentcore.types.session_id
    from capo_bedrock_agentcore._services.async_bedrock_agent_core import (
        AsyncBedrockAgentCoreClient,
        AsyncBedrockAgentCoreClientConfig,
    )
    from capo_bedrock_agentcore._services.bedrock_agent_core import (
        BedrockAgentCoreClient,
        BedrockAgentCoreClientConfig,
    )


class CapacityProviderResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service

    def delete_capacity_provider_session(
        self,
        capacity_provider_id: "capo_bedrock_agentcore.types.capacity_provider_id.CapacityProviderId",
        session_id: "capo_bedrock_agentcore.types.session_id.SessionId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.delete_capacity_provider_session_response.DeleteCapacityProviderSessionResponse":
        """<p>Deletes a session associated with a capacity provider in Amazon Bedrock AgentCore and makes the session unavailable for further use. To delete a capacity provider session, specify both the capacity provider identifier and the session ID. After you delete a session, you cannot restart it.</p>

        Args:
            capacity_provider_id: <p>The unique identifier of the capacity provider associated with the session.</p>
            session_id: <p>The unique identifier of the capacity provider session to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.delete_capacity_provider_session_request.DeleteCapacityProviderSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.delete_capacity_provider_session_response.DeleteCapacityProviderSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_capacity_provider_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_capacity_provider_session.delete_capacity_provider_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCapacityProviderSession")
        )
        input_: capo_bedrock_agentcore.types.delete_capacity_provider_session_request.DeleteCapacityProviderSessionRequest = {
            "capacity_provider_id": capacity_provider_id,
            "session_id": session_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncCapacityProviderResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service

    async def delete_capacity_provider_session(
        self,
        capacity_provider_id: "capo_bedrock_agentcore.types.capacity_provider_id.CapacityProviderId",
        session_id: "capo_bedrock_agentcore.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.delete_capacity_provider_session_response.DeleteCapacityProviderSessionResponse":
        """<p>Deletes a session associated with a capacity provider in Amazon Bedrock AgentCore and makes the session unavailable for further use. To delete a capacity provider session, specify both the capacity provider identifier and the session ID. After you delete a session, you cannot restart it.</p>

        Args:
            capacity_provider_id: <p>The unique identifier of the capacity provider associated with the session.</p>
            session_id: <p>The unique identifier of the capacity provider session to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.delete_capacity_provider_session_request.DeleteCapacityProviderSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.delete_capacity_provider_session_response.DeleteCapacityProviderSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_capacity_provider_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_capacity_provider_session.async_delete_capacity_provider_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCapacityProviderSession")
        )
        input_: capo_bedrock_agentcore.types.delete_capacity_provider_session_request.DeleteCapacityProviderSessionRequest = {
            "capacity_provider_id": capacity_provider_id,
            "session_id": session_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
