from __future__ import annotations

import uuid
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
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.create_payment_session_request
    import capo_bedrock_agentcore.types.create_payment_session_response
    import capo_bedrock_agentcore.types.delete_payment_session_request
    import capo_bedrock_agentcore.types.delete_payment_session_response
    import capo_bedrock_agentcore.types.get_payment_session_request
    import capo_bedrock_agentcore.types.get_payment_session_response
    import capo_bedrock_agentcore.types.list_payment_sessions_request
    import capo_bedrock_agentcore.types.list_payment_sessions_response
    import capo_bedrock_agentcore.types.next_token
    import capo_bedrock_agentcore.types.payment_agent_name
    import capo_bedrock_agentcore.types.payment_manager_arn
    import capo_bedrock_agentcore.types.payment_session_id
    import capo_bedrock_agentcore.types.payment_session_summary
    import capo_bedrock_agentcore.types.session_limits
    import capo_bedrock_agentcore.types.user_id
    from capo_bedrock_agentcore._services.async_bedrock_agent_core import (
        AsyncBedrockAgentCoreClient,
        AsyncBedrockAgentCoreClientConfig,
    )
    from capo_bedrock_agentcore._services.bedrock_agent_core import (
        BedrockAgentCoreClient,
        BedrockAgentCoreClientConfig,
    )


class PaymentSessionResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service

    def create(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        expiry_time_in_minutes: int,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        limits: Optional[
            "capo_bedrock_agentcore.types.session_limits.SessionLimits"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.create_payment_session_response.CreatePaymentSessionResponse":
        """<p>Create a new payment session.</p>

        Args:
            user_id: <p>The user ID associated with this payment session.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this session.</p>
            limits: <p>The spending limits for this payment session.</p>
            expiry_time_in_minutes: <p>The session expiry time in minutes. Must be between 15 and 480 minutes.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.subscription_required_exception.SubscriptionRequiredException: <p>Returned when you attempt a wallet operation against a Coinbase Marketplace connector whose account does not hold an active Marketplace subscription and is not within the legacy exception period. Subscribe to the Marketplace listing before you retry the operation.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.create_payment_session_request.CreatePaymentSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.create_payment_session_response.CreatePaymentSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_session.create_payment_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreatePaymentSession")
        )
        input_: capo_bedrock_agentcore.types.create_payment_session_request.CreatePaymentSessionRequest = {
            "payment_manager_arn": payment_manager_arn,
            "expiry_time_in_minutes": expiry_time_in_minutes,
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        if limits is not None:
            input_["limits"] = limits
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
        payment_session_id: "capo_bedrock_agentcore.types.payment_session_id.PaymentSessionId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.get_payment_session_response.GetPaymentSessionResponse":
        """<p>Get a payment session.</p>

        Args:
            user_id: <p>The user ID associated with this payment session.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this session.</p>
            payment_session_id: <p>The ID of the payment session to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_payment_session_request.GetPaymentSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_payment_session_response.GetPaymentSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_session.get_payment_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetPaymentSession")
        )
        input_: capo_bedrock_agentcore.types.get_payment_session_request.GetPaymentSessionRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_session_id": payment_session_id,
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

    def delete(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_session_id: "capo_bedrock_agentcore.types.payment_session_id.PaymentSessionId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
    ) -> "capo_bedrock_agentcore.types.delete_payment_session_response.DeletePaymentSessionResponse":
        """<p>Deletes a payment session. This permanently removes the payment session record.</p>

        Args:
            user_id: <p>The user ID making the delete request. Must match the session's userId.</p>
            payment_manager_arn: <p>The payment manager ARN. Must match the session's paymentManagerArn.</p>
            payment_session_id: <p>The payment session ID to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.delete_payment_session_request.DeletePaymentSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.delete_payment_session_response.DeletePaymentSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_session.delete_payment_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePaymentSession")
        )
        input_: capo_bedrock_agentcore.types.delete_payment_session_request.DeletePaymentSessionRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_session_id": payment_session_id,
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
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore.types.list_payment_sessions_response.ListPaymentSessionsResponse":
        """<p>List payment sessions.</p>

        Args:
            user_id: <p>The user ID associated with the payment sessions.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns the sessions.</p>
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
            req: "OperationRequest[capo_bedrock_agentcore.types.list_payment_sessions_request.ListPaymentSessionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_payment_sessions_response.ListPaymentSessionsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_sessions

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_sessions.list_payment_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPaymentSessions")
        )
        input_: capo_bedrock_agentcore.types.list_payment_sessions_request.ListPaymentSessionsRequest = {
            "payment_manager_arn": payment_manager_arn
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
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


class AsyncPaymentSessionResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service

    async def create(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        expiry_time_in_minutes: int,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        limits: Optional[
            "capo_bedrock_agentcore.types.session_limits.SessionLimits"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.create_payment_session_response.CreatePaymentSessionResponse":
        """<p>Create a new payment session.</p>

        Args:
            user_id: <p>The user ID associated with this payment session.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this session.</p>
            limits: <p>The spending limits for this payment session.</p>
            expiry_time_in_minutes: <p>The session expiry time in minutes. Must be between 15 and 480 minutes.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.subscription_required_exception.SubscriptionRequiredException: <p>Returned when you attempt a wallet operation against a Coinbase Marketplace connector whose account does not hold an active Marketplace subscription and is not within the legacy exception period. Subscribe to the Marketplace listing before you retry the operation.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.create_payment_session_request.CreatePaymentSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.create_payment_session_response.CreatePaymentSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_session.async_create_payment_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreatePaymentSession")
        )
        input_: capo_bedrock_agentcore.types.create_payment_session_request.CreatePaymentSessionRequest = {
            "payment_manager_arn": payment_manager_arn,
            "expiry_time_in_minutes": expiry_time_in_minutes,
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        if limits is not None:
            input_["limits"] = limits
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
        payment_session_id: "capo_bedrock_agentcore.types.payment_session_id.PaymentSessionId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.get_payment_session_response.GetPaymentSessionResponse":
        """<p>Get a payment session.</p>

        Args:
            user_id: <p>The user ID associated with this payment session.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this session.</p>
            payment_session_id: <p>The ID of the payment session to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.get_payment_session_request.GetPaymentSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.get_payment_session_response.GetPaymentSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_session.async_get_payment_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetPaymentSession")
        )
        input_: capo_bedrock_agentcore.types.get_payment_session_request.GetPaymentSessionRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_session_id": payment_session_id,
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

    async def delete(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_session_id: "capo_bedrock_agentcore.types.payment_session_id.PaymentSessionId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
    ) -> "capo_bedrock_agentcore.types.delete_payment_session_response.DeletePaymentSessionResponse":
        """<p>Deletes a payment session. This permanently removes the payment session record.</p>

        Args:
            user_id: <p>The user ID making the delete request. Must match the session's userId.</p>
            payment_manager_arn: <p>The payment manager ARN. Must match the session's paymentManagerArn.</p>
            payment_session_id: <p>The payment session ID to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.delete_payment_session_request.DeletePaymentSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.delete_payment_session_response.DeletePaymentSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_session.async_delete_payment_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePaymentSession")
        )
        input_: capo_bedrock_agentcore.types.delete_payment_session_request.DeletePaymentSessionRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_session_id": payment_session_id,
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
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore.types.list_payment_sessions_response.ListPaymentSessionsResponse":
        """<p>List payment sessions.</p>

        Args:
            user_id: <p>The user ID associated with the payment sessions.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns the sessions.</p>
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
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.list_payment_sessions_request.ListPaymentSessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.list_payment_sessions_response.ListPaymentSessionsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_sessions

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_sessions.async_list_payment_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPaymentSessions")
        )
        input_: capo_bedrock_agentcore.types.list_payment_sessions_request.ListPaymentSessionsRequest = {
            "payment_manager_arn": payment_manager_arn
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
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
