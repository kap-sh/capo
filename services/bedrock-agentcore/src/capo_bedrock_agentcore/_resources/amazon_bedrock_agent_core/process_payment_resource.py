from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

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
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.payment_agent_name
    import capo_bedrock_agentcore.types.payment_input
    import capo_bedrock_agentcore.types.payment_instrument_id
    import capo_bedrock_agentcore.types.payment_manager_arn
    import capo_bedrock_agentcore.types.payment_session_id
    import capo_bedrock_agentcore.types.payment_type
    import capo_bedrock_agentcore.types.process_payment_request
    import capo_bedrock_agentcore.types.process_payment_response
    import capo_bedrock_agentcore.types.user_id
    from capo_bedrock_agentcore._services.async_bedrock_agent_core import (
        AsyncBedrockAgentCoreClient,
        AsyncBedrockAgentCoreClientConfig,
    )
    from capo_bedrock_agentcore._services.bedrock_agent_core import (
        BedrockAgentCoreClient,
        BedrockAgentCoreClientConfig,
    )


class ProcessPaymentResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service

    def create(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_session_id: "capo_bedrock_agentcore.types.payment_session_id.PaymentSessionId",
        payment_instrument_id: "capo_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        payment_type: "capo_bedrock_agentcore.types.payment_type.PaymentType",
        payment_input: "capo_bedrock_agentcore.types.payment_input.PaymentInput",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.process_payment_response.ProcessPaymentResponse":
        """<p>Processes a payment using a payment instrument within a payment session.</p>

        Args:
            user_id: <p>The user ID associated with this payment.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager.</p>
            payment_session_id: <p>The ID of the payment session.</p>
            payment_instrument_id: <p>The ID of the payment instrument to use.</p>
            payment_type: <p>The type of payment to process.</p>
            payment_input: <p>The payment input details specific to the payment type.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.subscription_required_exception.SubscriptionRequiredException: <p>Returned when you attempt a wallet operation against a Coinbase Marketplace connector whose account does not hold an active Marketplace subscription and is not within the legacy exception period. Subscribe to the Marketplace listing before you retry the operation.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.process_payment_request.ProcessPaymentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.process_payment_response.ProcessPaymentResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.process_payment

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.process_payment.process_payment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore.types.process_payment_request.ProcessPaymentRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.process_payment_request

            return (
                capo_bedrock_agentcore.types.process_payment_request.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_bedrock_agentcore.types.process_payment_response.ProcessPaymentResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.process_payment_response

            return (
                capo_bedrock_agentcore.types.process_payment_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ProcessPayment",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore.types.process_payment_request.ProcessPaymentRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_session_id": payment_session_id,
            "payment_instrument_id": payment_instrument_id,
            "payment_type": payment_type,
            "payment_input": payment_input,
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
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


class AsyncProcessPaymentResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service

    async def create(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_session_id: "capo_bedrock_agentcore.types.payment_session_id.PaymentSessionId",
        payment_instrument_id: "capo_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        payment_type: "capo_bedrock_agentcore.types.payment_type.PaymentType",
        payment_input: "capo_bedrock_agentcore.types.payment_input.PaymentInput",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.process_payment_response.ProcessPaymentResponse":
        """<p>Processes a payment using a payment instrument within a payment session.</p>

        Args:
            user_id: <p>The user ID associated with this payment.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager.</p>
            payment_session_id: <p>The ID of the payment session.</p>
            payment_instrument_id: <p>The ID of the payment instrument to use.</p>
            payment_type: <p>The type of payment to process.</p>
            payment_input: <p>The payment input details specific to the payment type.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.subscription_required_exception.SubscriptionRequiredException: <p>Returned when you attempt a wallet operation against a Coinbase Marketplace connector whose account does not hold an active Marketplace subscription and is not within the legacy exception period. Subscribe to the Marketplace listing before you retry the operation.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.process_payment_request.ProcessPaymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.process_payment_response.ProcessPaymentResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.process_payment

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.process_payment.async_process_payment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore.types.process_payment_request.ProcessPaymentRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.process_payment_request

            return (
                capo_bedrock_agentcore.types.process_payment_request.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_bedrock_agentcore.types.process_payment_response.ProcessPaymentResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.process_payment_response

            return (
                capo_bedrock_agentcore.types.process_payment_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ProcessPayment",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore.types.process_payment_request.ProcessPaymentRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_session_id": payment_session_id,
            "payment_instrument_id": payment_instrument_id,
            "payment_type": payment_type,
            "payment_input": payment_input,
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
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
