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
    import capo_bedrock_agentcore.types.blockchain_chain_id
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.create_payment_instrument_request
    import capo_bedrock_agentcore.types.create_payment_instrument_response
    import capo_bedrock_agentcore.types.delete_payment_instrument_request
    import capo_bedrock_agentcore.types.delete_payment_instrument_response
    import capo_bedrock_agentcore.types.get_payment_instrument_balance_request
    import capo_bedrock_agentcore.types.get_payment_instrument_balance_response
    import capo_bedrock_agentcore.types.get_payment_instrument_request
    import capo_bedrock_agentcore.types.get_payment_instrument_response
    import capo_bedrock_agentcore.types.instrument_balance_token
    import capo_bedrock_agentcore.types.list_payment_instruments_request
    import capo_bedrock_agentcore.types.list_payment_instruments_response
    import capo_bedrock_agentcore.types.next_token
    import capo_bedrock_agentcore.types.payment_agent_name
    import capo_bedrock_agentcore.types.payment_connector_id
    import capo_bedrock_agentcore.types.payment_instrument_details
    import capo_bedrock_agentcore.types.payment_instrument_id
    import capo_bedrock_agentcore.types.payment_instrument_summary
    import capo_bedrock_agentcore.types.payment_instrument_type
    import capo_bedrock_agentcore.types.payment_manager_arn
    import capo_bedrock_agentcore.types.user_id
    from capo_bedrock_agentcore._services.async_bedrock_agent_core import (
        AsyncBedrockAgentCoreClient,
        AsyncBedrockAgentCoreClientConfig,
    )
    from capo_bedrock_agentcore._services.bedrock_agent_core import (
        BedrockAgentCoreClient,
        BedrockAgentCoreClientConfig,
    )


class PaymentInstrumentResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service

    def create(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_connector_id: "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId",
        payment_instrument_type: "capo_bedrock_agentcore.types.payment_instrument_type.PaymentInstrumentType",
        payment_instrument_details: "capo_bedrock_agentcore.types.payment_instrument_details.PaymentInstrumentDetails",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.create_payment_instrument_response.CreatePaymentInstrumentResponse":
        """<p>Create a new payment instrument for a connector.</p>

        Args:
            user_id: <p>The user ID associated with this payment instrument.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this payment instrument.</p>
            payment_connector_id: <p>The ID of the payment connector to use for this instrument.</p>
            payment_instrument_type: <p>The type of payment instrument being created.</p>
            payment_instrument_details: <p>The details of the payment instrument.</p>
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
            req: "OperationRequest[capo_bedrock_agentcore.types.create_payment_instrument_request.CreatePaymentInstrumentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.create_payment_instrument_response.CreatePaymentInstrumentResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_instrument

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_instrument.create_payment_instrument(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore.types.create_payment_instrument_request.CreatePaymentInstrumentRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.create_payment_instrument_request

            return capo_bedrock_agentcore.types.create_payment_instrument_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore.types.create_payment_instrument_response.CreatePaymentInstrumentResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.create_payment_instrument_response

            return capo_bedrock_agentcore.types.create_payment_instrument_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreatePaymentInstrument",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore.types.create_payment_instrument_request.CreatePaymentInstrumentRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_connector_id": payment_connector_id,
            "payment_instrument_type": payment_instrument_type,
            "payment_instrument_details": payment_instrument_details,
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

    def read(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_instrument_id: "capo_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        payment_connector_id: Optional[
            "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.get_payment_instrument_response.GetPaymentInstrumentResponse":
        """<p>Get a payment instrument by ID.</p>

        Args:
            user_id: <p>The user ID associated with this payment instrument.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this payment instrument.</p>
            payment_connector_id: <p>The ID of the payment connector.</p>
            payment_instrument_id: <p>The ID of the payment instrument to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_payment_instrument_request.GetPaymentInstrumentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_payment_instrument_response.GetPaymentInstrumentResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument.get_payment_instrument(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore.types.get_payment_instrument_response.GetPaymentInstrumentResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.get_payment_instrument_response

            return capo_bedrock_agentcore.types.get_payment_instrument_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetPaymentInstrument", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore.types.get_payment_instrument_request.GetPaymentInstrumentRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_instrument_id": payment_instrument_id,
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        if payment_connector_id is not None:
            input_["payment_connector_id"] = payment_connector_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_connector_id: "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId",
        payment_instrument_id: "capo_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
    ) -> "capo_bedrock_agentcore.types.delete_payment_instrument_response.DeletePaymentInstrumentResponse":
        """<p>Deletes a payment instrument. This is a soft delete operation that preserves the record for audit and compliance purposes.</p>

        Args:
            user_id: <p>The user ID making the delete request. Must match the instrument's userId.</p>
            payment_manager_arn: <p>The payment manager ARN. Must match the instrument's paymentManagerArn.</p>
            payment_connector_id: <p>The payment connector ID. Must match the instrument's paymentConnectorId.</p>
            payment_instrument_id: <p>The payment instrument ID to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.delete_payment_instrument_request.DeletePaymentInstrumentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.delete_payment_instrument_response.DeletePaymentInstrumentResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_instrument

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_instrument.delete_payment_instrument(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePaymentInstrument")
        )
        input_: capo_bedrock_agentcore.types.delete_payment_instrument_request.DeletePaymentInstrumentRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_connector_id": payment_connector_id,
            "payment_instrument_id": payment_instrument_id,
        }
        if user_id is not None:
            input_["user_id"] = user_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        payment_connector_id: Optional[
            "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore.types.list_payment_instruments_response.ListPaymentInstrumentsResponse":
        """<p>List payment instruments for a manager.</p>

        Args:
            user_id: <p>The user ID associated with the payment instruments.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns the payment instruments.</p>
            payment_connector_id: <p>The ID of the payment connector to filter by.</p>
            next_token: <p>Token for pagination to retrieve the next set of results.</p>
            max_results: <p>Maximum number of results to return in a single response.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_payment_instruments_request.ListPaymentInstrumentsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_payment_instruments_response.ListPaymentInstrumentsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_instruments

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_instruments.list_payment_instruments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPaymentInstruments")
        )
        input_: capo_bedrock_agentcore.types.list_payment_instruments_request.ListPaymentInstrumentsRequest = {
            "payment_manager_arn": payment_manager_arn
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        if payment_connector_id is not None:
            input_["payment_connector_id"] = payment_connector_id
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

    def get_payment_instrument_balance(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_connector_id: "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId",
        payment_instrument_id: "capo_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        chain: "capo_bedrock_agentcore.types.blockchain_chain_id.BlockchainChainId",
        token: "capo_bedrock_agentcore.types.instrument_balance_token.InstrumentBalanceToken",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.get_payment_instrument_balance_response.GetPaymentInstrumentBalanceResponse":
        """<p>Get the balance of a payment instrument.</p>

        Args:
            user_id: <p>The user ID associated with this payment instrument.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this payment instrument.</p>
            payment_connector_id: <p>The ID of the payment connector associated with this instrument.</p>
            payment_instrument_id: <p>The ID of the payment instrument to query balance for.</p>
            chain: <p>The specific blockchain chain to query balance on. Required because balances are chain-specific.</p>
            token: <p>The token to query balance for. Only tokens supported for X402 payments are returned.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_payment_instrument_balance_request.GetPaymentInstrumentBalanceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_payment_instrument_balance_response.GetPaymentInstrumentBalanceResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument_balance

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument_balance.get_payment_instrument_balance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetPaymentInstrumentBalance")
        )
        input_: capo_bedrock_agentcore.types.get_payment_instrument_balance_request.GetPaymentInstrumentBalanceRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_connector_id": payment_connector_id,
            "payment_instrument_id": payment_instrument_id,
            "chain": chain,
            "token": token,
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncPaymentInstrumentResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service

    async def create(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_connector_id: "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId",
        payment_instrument_type: "capo_bedrock_agentcore.types.payment_instrument_type.PaymentInstrumentType",
        payment_instrument_details: "capo_bedrock_agentcore.types.payment_instrument_details.PaymentInstrumentDetails",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.create_payment_instrument_response.CreatePaymentInstrumentResponse":
        """<p>Create a new payment instrument for a connector.</p>

        Args:
            user_id: <p>The user ID associated with this payment instrument.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this payment instrument.</p>
            payment_connector_id: <p>The ID of the payment connector to use for this instrument.</p>
            payment_instrument_type: <p>The type of payment instrument being created.</p>
            payment_instrument_details: <p>The details of the payment instrument.</p>
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
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.create_payment_instrument_request.CreatePaymentInstrumentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.create_payment_instrument_response.CreatePaymentInstrumentResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_instrument

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_instrument.async_create_payment_instrument(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore.types.create_payment_instrument_request.CreatePaymentInstrumentRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.create_payment_instrument_request

            return capo_bedrock_agentcore.types.create_payment_instrument_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore.types.create_payment_instrument_response.CreatePaymentInstrumentResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.create_payment_instrument_response

            return capo_bedrock_agentcore.types.create_payment_instrument_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreatePaymentInstrument",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore.types.create_payment_instrument_request.CreatePaymentInstrumentRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_connector_id": payment_connector_id,
            "payment_instrument_type": payment_instrument_type,
            "payment_instrument_details": payment_instrument_details,
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

    async def read(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_instrument_id: "capo_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        payment_connector_id: Optional[
            "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.get_payment_instrument_response.GetPaymentInstrumentResponse":
        """<p>Get a payment instrument by ID.</p>

        Args:
            user_id: <p>The user ID associated with this payment instrument.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this payment instrument.</p>
            payment_connector_id: <p>The ID of the payment connector.</p>
            payment_instrument_id: <p>The ID of the payment instrument to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.get_payment_instrument_request.GetPaymentInstrumentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.get_payment_instrument_response.GetPaymentInstrumentResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument.async_get_payment_instrument(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore.types.get_payment_instrument_response.GetPaymentInstrumentResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.get_payment_instrument_response

            return capo_bedrock_agentcore.types.get_payment_instrument_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetPaymentInstrument", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore.types.get_payment_instrument_request.GetPaymentInstrumentRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_instrument_id": payment_instrument_id,
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        if payment_connector_id is not None:
            input_["payment_connector_id"] = payment_connector_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_connector_id: "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId",
        payment_instrument_id: "capo_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
    ) -> "capo_bedrock_agentcore.types.delete_payment_instrument_response.DeletePaymentInstrumentResponse":
        """<p>Deletes a payment instrument. This is a soft delete operation that preserves the record for audit and compliance purposes.</p>

        Args:
            user_id: <p>The user ID making the delete request. Must match the instrument's userId.</p>
            payment_manager_arn: <p>The payment manager ARN. Must match the instrument's paymentManagerArn.</p>
            payment_connector_id: <p>The payment connector ID. Must match the instrument's paymentConnectorId.</p>
            payment_instrument_id: <p>The payment instrument ID to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.delete_payment_instrument_request.DeletePaymentInstrumentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.delete_payment_instrument_response.DeletePaymentInstrumentResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_instrument

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_instrument.async_delete_payment_instrument(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePaymentInstrument")
        )
        input_: capo_bedrock_agentcore.types.delete_payment_instrument_request.DeletePaymentInstrumentRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_connector_id": payment_connector_id,
            "payment_instrument_id": payment_instrument_id,
        }
        if user_id is not None:
            input_["user_id"] = user_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        payment_connector_id: Optional[
            "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore.types.list_payment_instruments_response.ListPaymentInstrumentsResponse":
        """<p>List payment instruments for a manager.</p>

        Args:
            user_id: <p>The user ID associated with the payment instruments.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns the payment instruments.</p>
            payment_connector_id: <p>The ID of the payment connector to filter by.</p>
            next_token: <p>Token for pagination to retrieve the next set of results.</p>
            max_results: <p>Maximum number of results to return in a single response.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.list_payment_instruments_request.ListPaymentInstrumentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.list_payment_instruments_response.ListPaymentInstrumentsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_instruments

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_instruments.async_list_payment_instruments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPaymentInstruments")
        )
        input_: capo_bedrock_agentcore.types.list_payment_instruments_request.ListPaymentInstrumentsRequest = {
            "payment_manager_arn": payment_manager_arn
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        if payment_connector_id is not None:
            input_["payment_connector_id"] = payment_connector_id
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

    async def get_payment_instrument_balance(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_connector_id: "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId",
        payment_instrument_id: "capo_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        chain: "capo_bedrock_agentcore.types.blockchain_chain_id.BlockchainChainId",
        token: "capo_bedrock_agentcore.types.instrument_balance_token.InstrumentBalanceToken",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.get_payment_instrument_balance_response.GetPaymentInstrumentBalanceResponse":
        """<p>Get the balance of a payment instrument.</p>

        Args:
            user_id: <p>The user ID associated with this payment instrument.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this payment instrument.</p>
            payment_connector_id: <p>The ID of the payment connector associated with this instrument.</p>
            payment_instrument_id: <p>The ID of the payment instrument to query balance for.</p>
            chain: <p>The specific blockchain chain to query balance on. Required because balances are chain-specific.</p>
            token: <p>The token to query balance for. Only tokens supported for X402 payments are returned.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.get_payment_instrument_balance_request.GetPaymentInstrumentBalanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.get_payment_instrument_balance_response.GetPaymentInstrumentBalanceResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument_balance

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument_balance.async_get_payment_instrument_balance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetPaymentInstrumentBalance")
        )
        input_: capo_bedrock_agentcore.types.get_payment_instrument_balance_request.GetPaymentInstrumentBalanceRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_connector_id": payment_connector_id,
            "payment_instrument_id": payment_instrument_id,
            "chain": chain,
            "token": token,
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
