"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AWSMPCommerceService_v20200301``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_marketplace_agreement._auth._signers
import capo_marketplace_agreement._auth._sigv4
from capo_marketplace_agreement._auth._identity import Credentials
from capo_marketplace_agreement._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_marketplace_agreement._auth._zapros_handler import AuthMiddleware
from capo_marketplace_agreement._pagination import resolve_path as _resolve_path
from capo_marketplace_agreement._services._aws_config import aaws_config
from capo_marketplace_agreement._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.accept_agreement_cancellation_request_input
    import capo_marketplace_agreement.types.accept_agreement_cancellation_request_output
    import capo_marketplace_agreement.types.accept_agreement_payment_request_input
    import capo_marketplace_agreement.types.accept_agreement_payment_request_output
    import capo_marketplace_agreement.types.accept_agreement_request_input
    import capo_marketplace_agreement.types.accept_agreement_request_output
    import capo_marketplace_agreement.types.accepted_term
    import capo_marketplace_agreement.types.agreement_cancellation_request_cancellation_reason
    import capo_marketplace_agreement.types.agreement_cancellation_request_description
    import capo_marketplace_agreement.types.agreement_cancellation_request_id
    import capo_marketplace_agreement.types.agreement_cancellation_request_reason_code
    import capo_marketplace_agreement.types.agreement_cancellation_request_rejection_reason
    import capo_marketplace_agreement.types.agreement_cancellation_request_status
    import capo_marketplace_agreement.types.agreement_cancellation_request_summary
    import capo_marketplace_agreement.types.agreement_entitlement
    import capo_marketplace_agreement.types.agreement_id
    import capo_marketplace_agreement.types.agreement_invoice_line_item_group_summary
    import capo_marketplace_agreement.types.agreement_proposal_id
    import capo_marketplace_agreement.types.agreement_request_id
    import capo_marketplace_agreement.types.agreement_type
    import capo_marketplace_agreement.types.agreement_view_summary
    import capo_marketplace_agreement.types.batch_create_billing_adjustment_request_entry_list
    import capo_marketplace_agreement.types.batch_create_billing_adjustment_request_input
    import capo_marketplace_agreement.types.batch_create_billing_adjustment_request_output
    import capo_marketplace_agreement.types.billing_adjustment_request_id
    import capo_marketplace_agreement.types.billing_adjustment_status
    import capo_marketplace_agreement.types.billing_adjustment_summary
    import capo_marketplace_agreement.types.cancel_agreement_cancellation_request_input
    import capo_marketplace_agreement.types.cancel_agreement_cancellation_request_output
    import capo_marketplace_agreement.types.cancel_agreement_input
    import capo_marketplace_agreement.types.cancel_agreement_output
    import capo_marketplace_agreement.types.cancel_agreement_payment_request_input
    import capo_marketplace_agreement.types.cancel_agreement_payment_request_output
    import capo_marketplace_agreement.types.catalog
    import capo_marketplace_agreement.types.charge
    import capo_marketplace_agreement.types.client_token
    import capo_marketplace_agreement.types.create_agreement_request_input
    import capo_marketplace_agreement.types.create_agreement_request_output
    import capo_marketplace_agreement.types.describe_agreement_input
    import capo_marketplace_agreement.types.describe_agreement_output
    import capo_marketplace_agreement.types.filter_list
    import capo_marketplace_agreement.types.get_agreement_cancellation_request_input
    import capo_marketplace_agreement.types.get_agreement_cancellation_request_output
    import capo_marketplace_agreement.types.get_agreement_entitlements_input
    import capo_marketplace_agreement.types.get_agreement_entitlements_output
    import capo_marketplace_agreement.types.get_agreement_payment_request_input
    import capo_marketplace_agreement.types.get_agreement_payment_request_output
    import capo_marketplace_agreement.types.get_agreement_terms_input
    import capo_marketplace_agreement.types.get_agreement_terms_output
    import capo_marketplace_agreement.types.get_billing_adjustment_request_input
    import capo_marketplace_agreement.types.get_billing_adjustment_request_output
    import capo_marketplace_agreement.types.intent
    import capo_marketplace_agreement.types.invoice_billing_period
    import capo_marketplace_agreement.types.invoice_type
    import capo_marketplace_agreement.types.line_item_group_by
    import capo_marketplace_agreement.types.list_agreement_cancellation_requests_input
    import capo_marketplace_agreement.types.list_agreement_cancellation_requests_output
    import capo_marketplace_agreement.types.list_agreement_charges_input
    import capo_marketplace_agreement.types.list_agreement_charges_output
    import capo_marketplace_agreement.types.list_agreement_invoice_line_items_input
    import capo_marketplace_agreement.types.list_agreement_invoice_line_items_output
    import capo_marketplace_agreement.types.list_agreement_payment_requests_input
    import capo_marketplace_agreement.types.list_agreement_payment_requests_output
    import capo_marketplace_agreement.types.list_billing_adjustment_requests_input
    import capo_marketplace_agreement.types.list_billing_adjustment_requests_output
    import capo_marketplace_agreement.types.max_results
    import capo_marketplace_agreement.types.next_token
    import capo_marketplace_agreement.types.party_type
    import capo_marketplace_agreement.types.payment_request_description
    import capo_marketplace_agreement.types.payment_request_id
    import capo_marketplace_agreement.types.payment_request_name
    import capo_marketplace_agreement.types.payment_request_rejection_reason
    import capo_marketplace_agreement.types.payment_request_status
    import capo_marketplace_agreement.types.payment_request_summary
    import capo_marketplace_agreement.types.positive_amount_upto8_decimals
    import capo_marketplace_agreement.types.purchase_order_reference
    import capo_marketplace_agreement.types.purchase_orders
    import capo_marketplace_agreement.types.reject_agreement_cancellation_request_input
    import capo_marketplace_agreement.types.reject_agreement_cancellation_request_output
    import capo_marketplace_agreement.types.reject_agreement_payment_request_input
    import capo_marketplace_agreement.types.reject_agreement_payment_request_output
    import capo_marketplace_agreement.types.requested_term_list
    import capo_marketplace_agreement.types.resource_id
    import capo_marketplace_agreement.types.search_agreements_input
    import capo_marketplace_agreement.types.search_agreements_output
    import capo_marketplace_agreement.types.send_agreement_cancellation_request_input
    import capo_marketplace_agreement.types.send_agreement_cancellation_request_output
    import capo_marketplace_agreement.types.send_agreement_payment_request_input
    import capo_marketplace_agreement.types.send_agreement_payment_request_output
    import capo_marketplace_agreement.types.sort
    import capo_marketplace_agreement.types.tax_configuration
    import capo_marketplace_agreement.types.term_id
    import capo_marketplace_agreement.types.timestamp
    import capo_marketplace_agreement.types.update_purchase_orders_input
    import capo_marketplace_agreement.types.update_purchase_orders_output


class AsyncMarketplaceAgreementClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncMarketplaceAgreementClient:
    """A client for the ``MarketplaceAgreement`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncMarketplaceAgreementClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMarketplaceAgreementClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def accept_agreement_cancellation_request(
        self,
        agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId",
        agreement_cancellation_request_id: "capo_marketplace_agreement.types.agreement_cancellation_request_id.AgreementCancellationRequestId",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
    ) -> "capo_marketplace_agreement.types.accept_agreement_cancellation_request_output.AcceptAgreementCancellationRequestOutput":
        """<p>Allows buyers (acceptors) to accept a cancellation request that is in <code>PENDING_APPROVAL</code> status. Once accepted, the cancellation request transitions to <code>APPROVED</code> status and the agreement cancellation will be processed.</p> <note> <p>Only cancellation requests in <code>PENDING_APPROVAL</code> status can be accepted. A <code>ConflictException</code> is thrown if the cancellation request is in any other status.</p> </note>

        Args:
            agreement_id: <p>The unique identifier of the agreement associated with the cancellation request.</p>
            agreement_cancellation_request_id: <p>The unique identifier of the cancellation request to accept.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.conflict_exception.ConflictException: <p>Request was denied due to a resource conflict.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.accept_agreement_cancellation_request_input.AcceptAgreementCancellationRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.accept_agreement_cancellation_request_output.AcceptAgreementCancellationRequestOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.accept_agreement_cancellation_request

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.accept_agreement_cancellation_request.async_accept_agreement_cancellation_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.accept_agreement_cancellation_request_input.AcceptAgreementCancellationRequestInput = {
            "agreement_id": agreement_id,
            "agreement_cancellation_request_id": agreement_cancellation_request_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def accept_agreement_payment_request(
        self,
        payment_request_id: "capo_marketplace_agreement.types.payment_request_id.PaymentRequestId",
        agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        purchase_order_reference: Optional[
            "capo_marketplace_agreement.types.purchase_order_reference.PurchaseOrderReference"
        ] = None,
    ) -> "capo_marketplace_agreement.types.accept_agreement_payment_request_output.AcceptAgreementPaymentRequestOutput":
        """<p>Allows buyers (acceptors) to accept a payment request that is in <code>PENDING_APPROVAL</code> status. Once accepted, the payment request transitions to <code>APPROVED</code> status and the charge will be processed. Buyers can optionally provide a purchase order reference for their internal tracking.</p> <note> <p>Only payment requests in <code>PENDING_APPROVAL</code> status can be accepted. A <code>ConflictException</code> is thrown if the payment request is in any other status.</p> </note>

        Args:
            payment_request_id: <p>The unique identifier of the payment request to accept.</p>
            agreement_id: <p>The unique identifier of the agreement associated with the payment request.</p>
            purchase_order_reference: <p>An optional purchase order reference that buyers can provide to associate the payment request with their internal purchase order system.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.conflict_exception.ConflictException: <p>Request was denied due to a resource conflict.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.accept_agreement_payment_request_input.AcceptAgreementPaymentRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.accept_agreement_payment_request_output.AcceptAgreementPaymentRequestOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.accept_agreement_payment_request

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.accept_agreement_payment_request.async_accept_agreement_payment_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.accept_agreement_payment_request_input.AcceptAgreementPaymentRequestInput = {
            "payment_request_id": payment_request_id,
            "agreement_id": agreement_id,
        }
        if purchase_order_reference is not None:
            input_["purchase_order_reference"] = purchase_order_reference

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def accept_agreement_request(
        self,
        agreement_request_id: "capo_marketplace_agreement.types.agreement_request_id.AgreementRequestId",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        purchase_orders: Optional[
            "capo_marketplace_agreement.types.purchase_orders.PurchaseOrders"
        ] = None,
    ) -> "capo_marketplace_agreement.types.accept_agreement_request_output.AcceptAgreementRequestOutput":
        """<p>Accepts an agreement request to finalize the agreement. The acceptor can optionally provide purchase orders to associate with the agreement charges.</p>

        Args:
            agreement_request_id: <p>The unique identifier of the agreement request.</p>
            purchase_orders: <p>A list of purchase orders associated with accepting a marketplace agreement request.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.conflict_exception.ConflictException: <p>Request was denied due to a resource conflict.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.accept_agreement_request_input.AcceptAgreementRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.accept_agreement_request_output.AcceptAgreementRequestOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.accept_agreement_request

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.accept_agreement_request.async_accept_agreement_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.accept_agreement_request_input.AcceptAgreementRequestInput = {
            "agreement_request_id": agreement_request_id
        }
        if purchase_orders is not None:
            input_["purchase_orders"] = purchase_orders

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_create_billing_adjustment_request(
        self,
        billing_adjustment_request_entries: "capo_marketplace_agreement.types.batch_create_billing_adjustment_request_entry_list.BatchCreateBillingAdjustmentRequestEntryList",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
    ) -> "capo_marketplace_agreement.types.batch_create_billing_adjustment_request_output.BatchCreateBillingAdjustmentRequestOutput":
        """<p>Allows sellers (proposers) to submit billing adjustment requests for one or more invoices within an agreement. Each entry in the batch specifies an invoice and the adjustment amount. The operation returns successfully created adjustment request IDs and any errors for entries that failed to process.</p> <note> <p>Each entry requires a unique <code>clientToken</code> for idempotency.</p> </note>

        Args:
            billing_adjustment_request_entries: <p>A list of billing adjustment request entries. Each entry specifies the invoice and adjustment details.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.conflict_exception.ConflictException: <p>Request was denied due to a resource conflict.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create billing adjustment requests

            >>> await client.batch_create_billing_adjustment_request(billing_adjustment_request_entries=[{'originalInvoiceId': 'E2E20230929a108cfae', 'agreementId': 'agmt-SvIzsqYMyQwI3GWgJAe17URx', 'adjustmentAmount': '500.00', 'currencyCode': 'USD', 'clientToken': '71a5e82e-a49b-4075-8c7f-52df1d294379', 'adjustmentReasonCode': 'OTHER', 'description': 'Customer requested adjustment due to service outage during critical business period.'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.batch_create_billing_adjustment_request_input.BatchCreateBillingAdjustmentRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.batch_create_billing_adjustment_request_output.BatchCreateBillingAdjustmentRequestOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.batch_create_billing_adjustment_request

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.batch_create_billing_adjustment_request.async_batch_create_billing_adjustment_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.batch_create_billing_adjustment_request_input.BatchCreateBillingAdjustmentRequestInput = {
            "billing_adjustment_request_entries": billing_adjustment_request_entries
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_agreement(
        self,
        agreement_id: "capo_marketplace_agreement.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
    ) -> (
        "capo_marketplace_agreement.types.cancel_agreement_output.CancelAgreementOutput"
    ):
        """<p>Allows an acceptor to cancel an active agreement. Not all agreements are eligible for cancellation. Use the error response to determine why a cancellation request was rejected.</p>

        Args:
            agreement_id: <p>The unique identifier of the agreement.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.conflict_exception.ConflictException: <p>Request was denied due to a resource conflict.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.cancel_agreement_input.CancelAgreementInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.cancel_agreement_output.CancelAgreementOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.cancel_agreement

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.cancel_agreement.async_cancel_agreement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.cancel_agreement_input.CancelAgreementInput = {
            "agreement_id": agreement_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_agreement_cancellation_request(
        self,
        agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId",
        agreement_cancellation_request_id: "capo_marketplace_agreement.types.agreement_cancellation_request_id.AgreementCancellationRequestId",
        cancellation_reason: "capo_marketplace_agreement.types.agreement_cancellation_request_cancellation_reason.AgreementCancellationRequestCancellationReason",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
    ) -> "capo_marketplace_agreement.types.cancel_agreement_cancellation_request_output.CancelAgreementCancellationRequestOutput":
        """<p>Allows sellers (proposers) to withdraw an existing agreement cancellation request that is in a pending state. Once cancelled, the cancellation request transitions to <code>CANCELLED</code> status and can no longer be approved or rejected by the buyer.</p> <note> <p>Only cancellation requests in <code>PENDING_APPROVAL</code> status can be cancelled. A <code>ConflictException</code> is thrown if the cancellation request is in any other status.</p> </note>

        Args:
            agreement_id: <p>The unique identifier of the agreement associated with the cancellation request.</p>
            agreement_cancellation_request_id: <p>The unique identifier of the cancellation request to cancel.</p>
            cancellation_reason: <p>A required message explaining why the cancellation request is being withdrawn (1-2000 characters).</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.conflict_exception.ConflictException: <p>Request was denied due to a resource conflict.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Cancel a cancellation request

            >>> await client.cancel_agreement_cancellation_request(agreement_cancellation_request_id='acr-752jqvg74yo7k4h56cakk6396', agreement_id='agmt-752jqvg74yo7k4h56cakk6396', cancellation_reason='Requested agreement cancellation by mistake')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.cancel_agreement_cancellation_request_input.CancelAgreementCancellationRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.cancel_agreement_cancellation_request_output.CancelAgreementCancellationRequestOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.cancel_agreement_cancellation_request

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.cancel_agreement_cancellation_request.async_cancel_agreement_cancellation_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.cancel_agreement_cancellation_request_input.CancelAgreementCancellationRequestInput = {
            "agreement_id": agreement_id,
            "agreement_cancellation_request_id": agreement_cancellation_request_id,
            "cancellation_reason": cancellation_reason,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_agreement_payment_request(
        self,
        payment_request_id: "capo_marketplace_agreement.types.payment_request_id.PaymentRequestId",
        agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
    ) -> "capo_marketplace_agreement.types.cancel_agreement_payment_request_output.CancelAgreementPaymentRequestOutput":
        """<p>Allows sellers (proposers) to cancel a payment request that is in <code>PENDING_APPROVAL</code> status. Once cancelled, the payment request transitions to <code>CANCELLED</code> status and can no longer be accepted or rejected by the buyer.</p> <note> <p>Only payment requests in <code>PENDING_APPROVAL</code> status can be cancelled. A <code>ConflictException</code> is thrown if the payment request is in any other status.</p> </note>

        Args:
            payment_request_id: <p>The unique identifier of the payment request to cancel.</p>
            agreement_id: <p>The unique identifier of the agreement associated with the payment request.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.conflict_exception.ConflictException: <p>Request was denied due to a resource conflict.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.cancel_agreement_payment_request_input.CancelAgreementPaymentRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.cancel_agreement_payment_request_output.CancelAgreementPaymentRequestOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.cancel_agreement_payment_request

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.cancel_agreement_payment_request.async_cancel_agreement_payment_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.cancel_agreement_payment_request_input.CancelAgreementPaymentRequestInput = {
            "payment_request_id": payment_request_id,
            "agreement_id": agreement_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_agreement_request(
        self,
        intent: "capo_marketplace_agreement.types.intent.Intent",
        requested_terms: "capo_marketplace_agreement.types.requested_term_list.RequestedTermList",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        client_token: Optional[
            "capo_marketplace_agreement.types.client_token.ClientToken"
        ] = None,
        source_agreement_identifier: Optional[
            "capo_marketplace_agreement.types.resource_id.ResourceId"
        ] = None,
        agreement_proposal_identifier: Optional[
            "capo_marketplace_agreement.types.agreement_proposal_id.AgreementProposalId"
        ] = None,
        tax_configuration: Optional[
            "capo_marketplace_agreement.types.tax_configuration.TaxConfiguration"
        ] = None,
    ) -> "capo_marketplace_agreement.types.create_agreement_request_output.CreateAgreementRequestOutput":
        """<p>Creates an agreement request that acts as a quote for the terms you want to accept. The agreement request captures the requested terms, calculates charges, and returns a summary. Use <code>AcceptAgreementRequest</code> with the returned <code>agreementRequestId</code> to finalize the agreement.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            intent: <p>The purpose and desired outcome of the agreement request. This is a required parameter that determines how the agreement request is processed.</p> <ul> <li> <p> <code>NEW</code> – Creates a new agreement for terms in the request.</p> </li> <li> <p> <code>AMEND</code> – Modifies an existing agreement with terms that are accepted in the request.</p> </li> <li> <p> <code>REPLACE</code> – Creates a new agreement with accepted terms and replaces the existing agreement.</p> </li> </ul>
            requested_terms: <p>A list of terms that define what is being accepted as part of the agreement. Some terms require configuration.</p>
            source_agreement_identifier: <p>The agreement's identifier that the request acts upon.</p> <important> <p> This parameter is required for all non-<code>NEW</code> intents (i.e., <code>AMEND</code> or <code>REPLACE</code>). Don't provide this parameter if the intent is <code>NEW</code>. </p> </important>
            agreement_proposal_identifier: <p>The agreement proposal signed by the proposer. The proposal includes the requested resources and the terms that outline an agreement outcome.</p> <important> <p> This parameter is required if the intent is not <code>AMEND</code>.</p> </important>
            tax_configuration: <p>Configuration for tax estimation in the agreement request response.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.conflict_exception.ConflictException: <p>Request was denied due to a resource conflict.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request exceeded the maximum allowed limit (quota) for a specific resource or API operation.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.create_agreement_request_input.CreateAgreementRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.create_agreement_request_output.CreateAgreementRequestOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.create_agreement_request

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.create_agreement_request.async_create_agreement_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.create_agreement_request_input.CreateAgreementRequestInput = {
            "intent": intent,
            "requested_terms": requested_terms,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if source_agreement_identifier is not None:
            input_["source_agreement_identifier"] = source_agreement_identifier
        if agreement_proposal_identifier is not None:
            input_["agreement_proposal_identifier"] = agreement_proposal_identifier
        if tax_configuration is not None:
            input_["tax_configuration"] = tax_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_agreement(
        self,
        agreement_id: "capo_marketplace_agreement.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
    ) -> "capo_marketplace_agreement.types.describe_agreement_output.DescribeAgreementOutput":
        """<p>Provides details about an agreement, such as the proposer, acceptor, start date, and end date.</p>

        Args:
            agreement_id: <p>The unique identifier of the agreement.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.describe_agreement_input.DescribeAgreementInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.describe_agreement_output.DescribeAgreementOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.describe_agreement

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.describe_agreement.async_describe_agreement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.describe_agreement_input.DescribeAgreementInput = {
            "agreement_id": agreement_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_agreement_cancellation_request(
        self,
        agreement_cancellation_request_id: "capo_marketplace_agreement.types.agreement_cancellation_request_id.AgreementCancellationRequestId",
        agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
    ) -> "capo_marketplace_agreement.types.get_agreement_cancellation_request_output.GetAgreementCancellationRequestOutput":
        """<p>Retrieves detailed information about a specific agreement cancellation request. Both sellers (proposers) and buyers (acceptors) can use this operation to view cancellation requests associated with their agreements.</p>

        Args:
            agreement_cancellation_request_id: <p>The unique identifier of the cancellation request.</p>
            agreement_id: <p>The unique identifier of the agreement associated with the cancellation request.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a cancellation request

            >>> await client.get_agreement_cancellation_request(agreement_id='agmt-752jqvg74yo7k', agreement_cancellation_request_id='acr-sgew33rhsds')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.get_agreement_cancellation_request_input.GetAgreementCancellationRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.get_agreement_cancellation_request_output.GetAgreementCancellationRequestOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.get_agreement_cancellation_request

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.get_agreement_cancellation_request.async_get_agreement_cancellation_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.get_agreement_cancellation_request_input.GetAgreementCancellationRequestInput = {
            "agreement_cancellation_request_id": agreement_cancellation_request_id,
            "agreement_id": agreement_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_agreement_entitlements(
        self,
        agreement_id: "capo_marketplace_agreement.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        max_results: Optional[
            "capo_marketplace_agreement.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_marketplace_agreement.types.next_token.NextToken"
        ] = None,
    ) -> "capo_marketplace_agreement.types.get_agreement_entitlements_output.GetAgreementEntitlementsOutput":
        """<p>Obtains details about the entitlements of an agreement.</p>

        Args:
            agreement_id: <p>The unique identifier of the agreement.</p>
            max_results: <p>The maximum number of agreement entitlements to return in the response.</p>
            next_token: <p>A token to specify where to start pagination.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.get_agreement_entitlements_input.GetAgreementEntitlementsInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.get_agreement_entitlements_output.GetAgreementEntitlementsOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.get_agreement_entitlements

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.get_agreement_entitlements.async_get_agreement_entitlements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.get_agreement_entitlements_input.GetAgreementEntitlementsInput = {
            "agreement_id": agreement_id
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

    async def iter_get_agreement_entitlements(
        self,
        agreement_id: "capo_marketplace_agreement.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        max_results: Optional[
            "capo_marketplace_agreement.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_marketplace_agreement.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_marketplace_agreement.types.agreement_entitlement.AgreementEntitlement]":
        _token = next_token
        while True:
            _response = await self.get_agreement_entitlements(
                agreement_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("agreement_entitlements",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_agreement_payment_request(
        self,
        payment_request_id: "capo_marketplace_agreement.types.payment_request_id.PaymentRequestId",
        agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
    ) -> "capo_marketplace_agreement.types.get_agreement_payment_request_output.GetAgreementPaymentRequestOutput":
        """<p>Retrieves detailed information about a specific payment request. Both sellers (proposers) and buyers (acceptors) can use this operation to view payment requests associated with their agreements. The response includes the current status, charge details, timestamps, and the charge ID if the request has been approved.</p> <note> <p>The calling identity must be either the acceptor or proposer of the payment request. A <code>ResourceNotFoundException</code> is returned if the payment request does not exist.</p> </note>

        Args:
            payment_request_id: <p>The identifier of the payment request.</p>
            agreement_id: <p>The unique identifier of the agreement associated with the payment request.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.get_agreement_payment_request_input.GetAgreementPaymentRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.get_agreement_payment_request_output.GetAgreementPaymentRequestOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.get_agreement_payment_request

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.get_agreement_payment_request.async_get_agreement_payment_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.get_agreement_payment_request_input.GetAgreementPaymentRequestInput = {
            "payment_request_id": payment_request_id,
            "agreement_id": agreement_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_agreement_terms(
        self,
        agreement_id: "capo_marketplace_agreement.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        max_results: Optional[
            "capo_marketplace_agreement.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_marketplace_agreement.types.next_token.NextToken"
        ] = None,
    ) -> "capo_marketplace_agreement.types.get_agreement_terms_output.GetAgreementTermsOutput":
        """<p>Obtains details about the terms in an agreement that you participated in as proposer or acceptor.</p> <p>The details include:</p> <ul> <li> <p> <code>TermType</code> – The type of term, such as <code>LegalTerm</code>, <code>RenewalTerm</code>, or <code>ConfigurableUpfrontPricingTerm</code>.</p> </li> <li> <p> <code>TermID</code> – The ID of the particular term, which is common between offer and agreement.</p> </li> <li> <p> <code>TermPayload</code> – The key information contained in the term, such as the EULA for <code>LegalTerm</code> or pricing and dimensions for various pricing terms, such as <code>ConfigurableUpfrontPricingTerm</code> or <code>UsageBasedPricingTerm</code>.</p> </li> </ul> <ul> <li> <p> <code>Configuration</code> – The buyer/acceptor's selection at the time of agreement creation, such as the number of units purchased for a dimension or setting the <code>EnableAutoRenew</code> flag.</p> </li> </ul>

        Args:
            agreement_id: <p>The unique identifier of the agreement.</p>
            max_results: <p>The maximum number of agreements to return in the response.</p>
            next_token: <p>A token to specify where to start pagination.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.get_agreement_terms_input.GetAgreementTermsInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.get_agreement_terms_output.GetAgreementTermsOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.get_agreement_terms

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.get_agreement_terms.async_get_agreement_terms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.get_agreement_terms_input.GetAgreementTermsInput = {
            "agreement_id": agreement_id
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

    async def iter_get_agreement_terms(
        self,
        agreement_id: "capo_marketplace_agreement.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        max_results: Optional[
            "capo_marketplace_agreement.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_marketplace_agreement.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_marketplace_agreement.types.accepted_term.AcceptedTerm]":
        _token = next_token
        while True:
            _response = await self.get_agreement_terms(
                agreement_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("accepted_terms",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_billing_adjustment_request(
        self,
        agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId",
        billing_adjustment_request_id: "capo_marketplace_agreement.types.billing_adjustment_request_id.BillingAdjustmentRequestId",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
    ) -> "capo_marketplace_agreement.types.get_billing_adjustment_request_output.GetBillingAdjustmentRequestOutput":
        """<p>Retrieves detailed information about a specific billing adjustment request. Sellers (proposers) can use this operation to view the status and details of a billing adjustment request they submitted.</p>

        Args:
            agreement_id: <p>The unique identifier of the agreement associated with the billing adjustment request.</p>
            billing_adjustment_request_id: <p>The unique identifier of the billing adjustment request.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a billing adjustment request

            >>> await client.get_billing_adjustment_request(billing_adjustment_request_id='ba-1a2b3c4d5e6f7g', agreement_id='agmt-SvIzsqYMyQwI3GWgJAe17URx')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.get_billing_adjustment_request_input.GetBillingAdjustmentRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.get_billing_adjustment_request_output.GetBillingAdjustmentRequestOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.get_billing_adjustment_request

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.get_billing_adjustment_request.async_get_billing_adjustment_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.get_billing_adjustment_request_input.GetBillingAdjustmentRequestInput = {
            "agreement_id": agreement_id,
            "billing_adjustment_request_id": billing_adjustment_request_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_agreement_cancellation_requests(
        self,
        party_type: "capo_marketplace_agreement.types.party_type.PartyType",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        agreement_id: Optional[
            "capo_marketplace_agreement.types.agreement_id.AgreementId"
        ] = None,
        status: Optional[
            "capo_marketplace_agreement.types.agreement_cancellation_request_status.AgreementCancellationRequestStatus"
        ] = None,
        agreement_type: Optional[
            "capo_marketplace_agreement.types.agreement_type.AgreementType"
        ] = None,
        catalog: Optional["capo_marketplace_agreement.types.catalog.Catalog"] = None,
        max_results: Optional[
            "capo_marketplace_agreement.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_marketplace_agreement.types.next_token.NextToken"
        ] = None,
    ) -> "capo_marketplace_agreement.types.list_agreement_cancellation_requests_output.ListAgreementCancellationRequestsOutput":
        """<p>Lists agreement cancellation requests available to you as a seller or buyer. Both sellers (proposers) and buyers (acceptors) can use this operation to find cancellation requests by specifying their party type and applying optional filters.</p> <note> <p> <code>PartyType</code> is a required parameter. A <code>ValidationException</code> is returned if <code>PartyType</code> is not provided.</p> </note>

        Args:
            party_type: <p>The party type for the cancellation requests. Required parameter. Use <code>Proposer</code> to list cancellation requests where you are the seller, or <code>Acceptor</code> to list cancellation requests where you are the buyer.</p>
            agreement_id: <p>An optional parameter to filter cancellation requests for a specific agreement.</p>
            status: <p>An optional parameter to filter cancellation requests by status.</p>
            agreement_type: <p>An optional parameter to filter cancellation requests by agreement type (e.g., <code>PurchaseAgreement</code>).</p>
            catalog: <p>An optional parameter to filter cancellation requests by catalog (e.g., <code>AWSMarketplace</code>).</p>
            max_results: <p>The maximum number of cancellation requests to return in the response.</p>
            next_token: <p>A token to specify where to start pagination.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List cancellation requests

            >>> await client.list_agreement_cancellation_requests(party_type='Proposer', max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.list_agreement_cancellation_requests_input.ListAgreementCancellationRequestsInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.list_agreement_cancellation_requests_output.ListAgreementCancellationRequestsOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.list_agreement_cancellation_requests

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.list_agreement_cancellation_requests.async_list_agreement_cancellation_requests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.list_agreement_cancellation_requests_input.ListAgreementCancellationRequestsInput = {
            "party_type": party_type
        }
        if agreement_id is not None:
            input_["agreement_id"] = agreement_id
        if status is not None:
            input_["status"] = status
        if agreement_type is not None:
            input_["agreement_type"] = agreement_type
        if catalog is not None:
            input_["catalog"] = catalog
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

    async def iter_list_agreement_cancellation_requests(
        self,
        party_type: "capo_marketplace_agreement.types.party_type.PartyType",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        agreement_id: Optional[
            "capo_marketplace_agreement.types.agreement_id.AgreementId"
        ] = None,
        status: Optional[
            "capo_marketplace_agreement.types.agreement_cancellation_request_status.AgreementCancellationRequestStatus"
        ] = None,
        agreement_type: Optional[
            "capo_marketplace_agreement.types.agreement_type.AgreementType"
        ] = None,
        catalog: Optional["capo_marketplace_agreement.types.catalog.Catalog"] = None,
        max_results: Optional[
            "capo_marketplace_agreement.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_marketplace_agreement.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_marketplace_agreement.types.agreement_cancellation_request_summary.AgreementCancellationRequestSummary]":
        _token = next_token
        while True:
            _response = await self.list_agreement_cancellation_requests(
                party_type,
                config_overrides=config_overrides,
                agreement_id=agreement_id,
                status=status,
                agreement_type=agreement_type,
                catalog=catalog,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_agreement_charges(
        self,
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        catalog: Optional["capo_marketplace_agreement.types.catalog.Catalog"] = None,
        agreement_id: Optional[
            "capo_marketplace_agreement.types.resource_id.ResourceId"
        ] = None,
        agreement_type: Optional[
            "capo_marketplace_agreement.types.agreement_type.AgreementType"
        ] = None,
        max_results: Optional[
            "capo_marketplace_agreement.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_marketplace_agreement.types.next_token.NextToken"
        ] = None,
    ) -> "capo_marketplace_agreement.types.list_agreement_charges_output.ListAgreementChargesOutput":
        """<p>Allows acceptors to view charges and purchase orders that are associated with an agreement. The response includes details about all charges regardless of whether a purchase order is linked to each charge.</p>

        Args:
            catalog: <p>The catalog in which the charges were created.</p>
            agreement_id: <p>The unique identifier of the agreement.</p>
            agreement_type: <p>Filter to retrieve charges of a specific agreement type (for example, <code>PurchaseAgreement</code>).</p>
            max_results: <p>The maximum number of charges to return in the response.</p>
            next_token: <p>A token to specify where to start pagination.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.list_agreement_charges_input.ListAgreementChargesInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.list_agreement_charges_output.ListAgreementChargesOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.list_agreement_charges

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.list_agreement_charges.async_list_agreement_charges(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.list_agreement_charges_input.ListAgreementChargesInput = {}
        if catalog is not None:
            input_["catalog"] = catalog
        if agreement_id is not None:
            input_["agreement_id"] = agreement_id
        if agreement_type is not None:
            input_["agreement_type"] = agreement_type
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

    async def iter_list_agreement_charges(
        self,
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        catalog: Optional["capo_marketplace_agreement.types.catalog.Catalog"] = None,
        agreement_id: Optional[
            "capo_marketplace_agreement.types.resource_id.ResourceId"
        ] = None,
        agreement_type: Optional[
            "capo_marketplace_agreement.types.agreement_type.AgreementType"
        ] = None,
        max_results: Optional[
            "capo_marketplace_agreement.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_marketplace_agreement.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_marketplace_agreement.types.charge.Charge]":
        _token = next_token
        while True:
            _response = await self.list_agreement_charges(
                config_overrides=config_overrides,
                catalog=catalog,
                agreement_id=agreement_id,
                agreement_type=agreement_type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_agreement_invoice_line_items(
        self,
        agreement_id: "capo_marketplace_agreement.types.resource_id.ResourceId",
        group_by: "capo_marketplace_agreement.types.line_item_group_by.LineItemGroupBy",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        invoice_id: Optional[
            "capo_marketplace_agreement.types.resource_id.ResourceId"
        ] = None,
        invoice_type: Optional[
            "capo_marketplace_agreement.types.invoice_type.InvoiceType"
        ] = None,
        invoice_billing_period: Optional[
            "capo_marketplace_agreement.types.invoice_billing_period.InvoiceBillingPeriod"
        ] = None,
        before_issued_time: Optional[
            "capo_marketplace_agreement.types.timestamp.Timestamp"
        ] = None,
        after_issued_time: Optional[
            "capo_marketplace_agreement.types.timestamp.Timestamp"
        ] = None,
        max_results: Optional[
            "capo_marketplace_agreement.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_marketplace_agreement.types.next_token.NextToken"
        ] = None,
    ) -> "capo_marketplace_agreement.types.list_agreement_invoice_line_items_output.ListAgreementInvoiceLineItemsOutput":
        """<p>Allows sellers (proposers) to retrieve aggregated billing data from AWS Marketplace agreements using flexible grouping. Supports invoice-level aggregation with filtering by billing period, invoice type, and issued date.</p> <note> <p>The <code>groupBy</code> parameter is required and supports only <code>INVOICE_ID</code> as a value. The <code>agreementId</code> parameter is required.</p> </note>

        Args:
            agreement_id: <p>The unique identifier of the agreement.</p>
            group_by: <p>Specifies a grouping strategy for line items. Currently supports <code>INVOICE_ID</code>.</p>
            invoice_id: <p>An optional filter to retrieve invoice information for a specific invoice.</p>
            invoice_type: <p>An optional filter for the type of invoice. Valid values are <code>INVOICE</code> and <code>CREDIT_MEMO</code>.</p>
            invoice_billing_period: <p>An optional filter for the billing period associated with the invoice.</p>
            before_issued_time: <p>An optional filter for invoices issued before the specified timestamp.</p>
            after_issued_time: <p>An optional filter for invoices issued after the specified timestamp.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to specify where to start pagination.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List agreement invoice line items

            >>> await client.list_agreement_invoice_line_items(agreement_id='agmt-EXAMPLESvIzsqYMyQwI3', group_by='INVOICE_ID')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.list_agreement_invoice_line_items_input.ListAgreementInvoiceLineItemsInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.list_agreement_invoice_line_items_output.ListAgreementInvoiceLineItemsOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.list_agreement_invoice_line_items

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.list_agreement_invoice_line_items.async_list_agreement_invoice_line_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.list_agreement_invoice_line_items_input.ListAgreementInvoiceLineItemsInput = {
            "agreement_id": agreement_id,
            "group_by": group_by,
        }
        if invoice_id is not None:
            input_["invoice_id"] = invoice_id
        if invoice_type is not None:
            input_["invoice_type"] = invoice_type
        if invoice_billing_period is not None:
            input_["invoice_billing_period"] = invoice_billing_period
        if before_issued_time is not None:
            input_["before_issued_time"] = before_issued_time
        if after_issued_time is not None:
            input_["after_issued_time"] = after_issued_time
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

    async def iter_list_agreement_invoice_line_items(
        self,
        agreement_id: "capo_marketplace_agreement.types.resource_id.ResourceId",
        group_by: "capo_marketplace_agreement.types.line_item_group_by.LineItemGroupBy",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        invoice_id: Optional[
            "capo_marketplace_agreement.types.resource_id.ResourceId"
        ] = None,
        invoice_type: Optional[
            "capo_marketplace_agreement.types.invoice_type.InvoiceType"
        ] = None,
        invoice_billing_period: Optional[
            "capo_marketplace_agreement.types.invoice_billing_period.InvoiceBillingPeriod"
        ] = None,
        before_issued_time: Optional[
            "capo_marketplace_agreement.types.timestamp.Timestamp"
        ] = None,
        after_issued_time: Optional[
            "capo_marketplace_agreement.types.timestamp.Timestamp"
        ] = None,
        max_results: Optional[
            "capo_marketplace_agreement.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_marketplace_agreement.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_marketplace_agreement.types.agreement_invoice_line_item_group_summary.AgreementInvoiceLineItemGroupSummary]":
        _token = next_token
        while True:
            _response = await self.list_agreement_invoice_line_items(
                agreement_id,
                group_by,
                config_overrides=config_overrides,
                invoice_id=invoice_id,
                invoice_type=invoice_type,
                invoice_billing_period=invoice_billing_period,
                before_issued_time=before_issued_time,
                after_issued_time=after_issued_time,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(
                _response, ("agreement_invoice_line_item_group_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_agreement_payment_requests(
        self,
        party_type: "capo_marketplace_agreement.types.party_type.PartyType",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        agreement_type: Optional[
            "capo_marketplace_agreement.types.agreement_type.AgreementType"
        ] = None,
        catalog: Optional["capo_marketplace_agreement.types.catalog.Catalog"] = None,
        agreement_id: Optional[
            "capo_marketplace_agreement.types.agreement_id.AgreementId"
        ] = None,
        status: Optional[
            "capo_marketplace_agreement.types.payment_request_status.PaymentRequestStatus"
        ] = None,
        max_results: Optional[
            "capo_marketplace_agreement.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_marketplace_agreement.types.next_token.NextToken"
        ] = None,
    ) -> "capo_marketplace_agreement.types.list_agreement_payment_requests_output.ListAgreementPaymentRequestsOutput":
        """<p>Lists payment requests available to you as a seller or buyer. Both sellers (proposers) and buyers (acceptors) can use this operation to find payment requests by specifying their party type and applying optional parameters.</p> <note> <p> <code>PartyType</code> is a required parameter. A <code>ValidationException</code> is returned if <code>PartyType</code> is not provided. Pagination is supported through <code>maxResults</code> (1-50, default 50) and <code>nextToken</code> parameters.</p> </note>

        Args:
            party_type: <p>The party type for the payment requests. Required parameter. Use <code>Proposer</code> to list payment requests where you are the seller, or <code>Acceptor</code> to list payment requests where you are the buyer.</p>
            agreement_type: <p>An optional parameter to list payment requests by agreement type (e.g., <code>PurchaseAgreement</code>).</p>
            catalog: <p>An optional parameter to list payment requests by catalog (e.g., <code>AWSMarketplace</code>).</p>
            agreement_id: <p>An optional parameter to list payment requests for a specific agreement.</p>
            status: <p>An optional parameter to list payment requests by status. Valid values include <code>VALIDATING</code>, <code>VALIDATION_FAILED</code>, <code>PENDING_APPROVAL</code>, <code>APPROVED</code>, <code>REJECTED</code>, and <code>CANCELLED</code>.</p>
            max_results: <p>The maximum number of payment requests to return in a single response (1-50). Default is 50.</p>
            next_token: <p>A token to specify where to start pagination.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.list_agreement_payment_requests_input.ListAgreementPaymentRequestsInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.list_agreement_payment_requests_output.ListAgreementPaymentRequestsOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.list_agreement_payment_requests

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.list_agreement_payment_requests.async_list_agreement_payment_requests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.list_agreement_payment_requests_input.ListAgreementPaymentRequestsInput = {
            "party_type": party_type
        }
        if agreement_type is not None:
            input_["agreement_type"] = agreement_type
        if catalog is not None:
            input_["catalog"] = catalog
        if agreement_id is not None:
            input_["agreement_id"] = agreement_id
        if status is not None:
            input_["status"] = status
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

    async def iter_list_agreement_payment_requests(
        self,
        party_type: "capo_marketplace_agreement.types.party_type.PartyType",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        agreement_type: Optional[
            "capo_marketplace_agreement.types.agreement_type.AgreementType"
        ] = None,
        catalog: Optional["capo_marketplace_agreement.types.catalog.Catalog"] = None,
        agreement_id: Optional[
            "capo_marketplace_agreement.types.agreement_id.AgreementId"
        ] = None,
        status: Optional[
            "capo_marketplace_agreement.types.payment_request_status.PaymentRequestStatus"
        ] = None,
        max_results: Optional[
            "capo_marketplace_agreement.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_marketplace_agreement.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_marketplace_agreement.types.payment_request_summary.PaymentRequestSummary]":
        _token = next_token
        while True:
            _response = await self.list_agreement_payment_requests(
                party_type,
                config_overrides=config_overrides,
                agreement_type=agreement_type,
                catalog=catalog,
                agreement_id=agreement_id,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_billing_adjustment_requests(
        self,
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        agreement_id: Optional[
            "capo_marketplace_agreement.types.agreement_id.AgreementId"
        ] = None,
        status: Optional[
            "capo_marketplace_agreement.types.billing_adjustment_status.BillingAdjustmentStatus"
        ] = None,
        created_after: Optional[
            "capo_marketplace_agreement.types.timestamp.Timestamp"
        ] = None,
        created_before: Optional[
            "capo_marketplace_agreement.types.timestamp.Timestamp"
        ] = None,
        max_results: Optional[
            "capo_marketplace_agreement.types.max_results.MaxResults"
        ] = None,
        catalog: Optional["capo_marketplace_agreement.types.catalog.Catalog"] = None,
        agreement_type: Optional[
            "capo_marketplace_agreement.types.agreement_type.AgreementType"
        ] = None,
        next_token: Optional[
            "capo_marketplace_agreement.types.next_token.NextToken"
        ] = None,
    ) -> "capo_marketplace_agreement.types.list_billing_adjustment_requests_output.ListBillingAdjustmentRequestsOutput":
        """<p>Lists billing adjustment requests for a specific agreement. Sellers (proposers) can use this operation to view all billing adjustment requests associated with an agreement.</p>

        Args:
            agreement_id: <p>The unique identifier of the agreement to list billing adjustment requests for.</p>
            status: <p>An optional filter to return billing adjustment requests with the specified status.</p>
            created_after: <p>An optional filter to return billing adjustment requests created after the specified timestamp.</p>
            created_before: <p>An optional filter to return billing adjustment requests created before the specified timestamp.</p>
            max_results: <p>The maximum number of billing adjustment requests to return in the response.</p>
            catalog: <p>An optional filter to return billing adjustment requests by catalog (e.g., <code>AWSMarketplace</code>).</p>
            agreement_type: <p>An optional filter to return billing adjustment requests by agreement type (e.g., <code>PurchaseAgreement</code>).</p>
            next_token: <p>A token to specify where to start pagination.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List billing adjustment requests

            >>> await client.list_billing_adjustment_requests(agreement_id='agmt-SvIzsqYMyQwI3GWgJAe17URx')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.list_billing_adjustment_requests_input.ListBillingAdjustmentRequestsInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.list_billing_adjustment_requests_output.ListBillingAdjustmentRequestsOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.list_billing_adjustment_requests

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.list_billing_adjustment_requests.async_list_billing_adjustment_requests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.list_billing_adjustment_requests_input.ListBillingAdjustmentRequestsInput = {}
        if agreement_id is not None:
            input_["agreement_id"] = agreement_id
        if status is not None:
            input_["status"] = status
        if created_after is not None:
            input_["created_after"] = created_after
        if created_before is not None:
            input_["created_before"] = created_before
        if max_results is not None:
            input_["max_results"] = max_results
        if catalog is not None:
            input_["catalog"] = catalog
        if agreement_type is not None:
            input_["agreement_type"] = agreement_type
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_billing_adjustment_requests(
        self,
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        agreement_id: Optional[
            "capo_marketplace_agreement.types.agreement_id.AgreementId"
        ] = None,
        status: Optional[
            "capo_marketplace_agreement.types.billing_adjustment_status.BillingAdjustmentStatus"
        ] = None,
        created_after: Optional[
            "capo_marketplace_agreement.types.timestamp.Timestamp"
        ] = None,
        created_before: Optional[
            "capo_marketplace_agreement.types.timestamp.Timestamp"
        ] = None,
        max_results: Optional[
            "capo_marketplace_agreement.types.max_results.MaxResults"
        ] = None,
        catalog: Optional["capo_marketplace_agreement.types.catalog.Catalog"] = None,
        agreement_type: Optional[
            "capo_marketplace_agreement.types.agreement_type.AgreementType"
        ] = None,
        next_token: Optional[
            "capo_marketplace_agreement.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_marketplace_agreement.types.billing_adjustment_summary.BillingAdjustmentSummary]":
        _token = next_token
        while True:
            _response = await self.list_billing_adjustment_requests(
                config_overrides=config_overrides,
                agreement_id=agreement_id,
                status=status,
                created_after=created_after,
                created_before=created_before,
                max_results=max_results,
                catalog=catalog,
                agreement_type=agreement_type,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def reject_agreement_cancellation_request(
        self,
        agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId",
        agreement_cancellation_request_id: "capo_marketplace_agreement.types.agreement_cancellation_request_id.AgreementCancellationRequestId",
        rejection_reason: "capo_marketplace_agreement.types.agreement_cancellation_request_rejection_reason.AgreementCancellationRequestRejectionReason",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
    ) -> "capo_marketplace_agreement.types.reject_agreement_cancellation_request_output.RejectAgreementCancellationRequestOutput":
        """<p>Allows buyers (acceptors) to reject a cancellation request that is in <code>PENDING_APPROVAL</code> status. Once rejected, the cancellation request transitions to <code>REJECTED</code> status and the agreement remains active. Buyers must provide a reason for the rejection.</p> <note> <p>Only cancellation requests in <code>PENDING_APPROVAL</code> status can be rejected. A <code>ConflictException</code> is thrown if the cancellation request is in any other status.</p> </note>

        Args:
            agreement_id: <p>The unique identifier of the agreement associated with the cancellation request.</p>
            agreement_cancellation_request_id: <p>The unique identifier of the cancellation request to reject.</p>
            rejection_reason: <p>The reason for rejecting the cancellation request (1-2000 characters). This message is visible to the seller.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.conflict_exception.ConflictException: <p>Request was denied due to a resource conflict.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.reject_agreement_cancellation_request_input.RejectAgreementCancellationRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.reject_agreement_cancellation_request_output.RejectAgreementCancellationRequestOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.reject_agreement_cancellation_request

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.reject_agreement_cancellation_request.async_reject_agreement_cancellation_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.reject_agreement_cancellation_request_input.RejectAgreementCancellationRequestInput = {
            "agreement_id": agreement_id,
            "agreement_cancellation_request_id": agreement_cancellation_request_id,
            "rejection_reason": rejection_reason,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reject_agreement_payment_request(
        self,
        payment_request_id: "capo_marketplace_agreement.types.payment_request_id.PaymentRequestId",
        agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        rejection_reason: Optional[
            "capo_marketplace_agreement.types.payment_request_rejection_reason.PaymentRequestRejectionReason"
        ] = None,
    ) -> "capo_marketplace_agreement.types.reject_agreement_payment_request_output.RejectAgreementPaymentRequestOutput":
        """<p>Allows buyers (acceptors) to reject a payment request that is in <code>PENDING_APPROVAL</code> status. Once rejected, the payment request transitions to <code>REJECTED</code> status and cannot be accepted. Buyers can optionally provide a reason for the rejection.</p> <note> <p>Only payment requests in <code>PENDING_APPROVAL</code> status can be rejected. A <code>ConflictException</code> is thrown if the payment request is in any other status.</p> </note>

        Args:
            payment_request_id: <p>The unique identifier of the payment request to reject.</p>
            agreement_id: <p>The unique identifier of the agreement associated with the payment request.</p>
            rejection_reason: <p>An optional reason for rejecting the payment request (1-250 characters). This message is visible to the seller.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.conflict_exception.ConflictException: <p>Request was denied due to a resource conflict.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.reject_agreement_payment_request_input.RejectAgreementPaymentRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.reject_agreement_payment_request_output.RejectAgreementPaymentRequestOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.reject_agreement_payment_request

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.reject_agreement_payment_request.async_reject_agreement_payment_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.reject_agreement_payment_request_input.RejectAgreementPaymentRequestInput = {
            "payment_request_id": payment_request_id,
            "agreement_id": agreement_id,
        }
        if rejection_reason is not None:
            input_["rejection_reason"] = rejection_reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_agreements(
        self,
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        catalog: Optional["capo_marketplace_agreement.types.catalog.Catalog"] = None,
        filters: Optional[
            "capo_marketplace_agreement.types.filter_list.FilterList"
        ] = None,
        sort: Optional["capo_marketplace_agreement.types.sort.Sort"] = None,
        max_results: Optional[
            "capo_marketplace_agreement.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_marketplace_agreement.types.next_token.NextToken"
        ] = None,
    ) -> "capo_marketplace_agreement.types.search_agreements_output.SearchAgreementsOutput":
        """<p>Searches across all agreements that a proposer or an acceptor has in AWS Marketplace. The search returns a list of agreements with basic agreement information.</p>

        Args:
            catalog: <p>The catalog in which the agreement was created.</p>
            filters: <p>The filter name and value pair used to return a specific list of results.</p> <p>The following filters are supported:</p> <ul> <li> <p> <code>ResourceIdentifier</code> – The unique identifier of the resource.</p> </li> <li> <p> <code>ResourceType</code> – Type of the resource, which is the product (<code>AmiProduct</code>, <code>ContainerProduct</code>, <code>SaaSProduct</code>, <code>ProfessionalServicesProduct</code>, or <code>MachineLearningProduct</code>).</p> </li> <li> <p> <code>PartyType</code> – The party type of the caller. Use <code>Proposer</code> or <code>Acceptor</code>.</p> </li> <li> <p> <code>AcceptorAccountId</code> – The AWS account ID of the party accepting the agreement terms.</p> </li> <li> <p> <code>OfferId</code> – The unique identifier of the offer in which the terms are registered in the agreement token.</p> </li> <li> <p> <code>Status</code> – The current status of the agreement. Values include <code>ACTIVE</code>, <code>CANCELLED</code>, <code>EXPIRED</code>, <code>RENEWED</code>, <code>REPLACED</code>, and <code>TERMINATED</code>.</p> </li> <li> <p> <code>BeforeEndTime</code> – A date used to filter agreements with a date before the <code>endTime</code> of an agreement.</p> </li> <li> <p> <code>AfterEndTime</code> – A date used to filter agreements with a date after the <code>endTime</code> of an agreement.</p> </li> <li> <p> <code>BeforeStartTime</code> – A date used to filter agreements with a date before the <code>startTime</code> of an agreement.</p> </li> <li> <p> <code>AfterStartTime</code> – A date used to filter agreements with a date after the <code>startTime</code> of an agreement.</p> </li> <li> <p> <code>BeforeLastUpdateTime</code> – A date used to filter agreements with a date before the <code>lastUpdateTime</code> of an agreement.</p> </li> <li> <p> <code>AfterLastUpdateTime</code> – A date used to filter agreements with a date after the <code>lastUpdateTime</code> of an agreement.</p> </li> <li> <p> <code>AgreementType</code> – The type of agreement. Supported value includes <code>PurchaseAgreement</code>.</p> </li> <li> <p> <code>OfferSetId</code> – A unique identifier for the offer set containing this offer. All agreements created from offers in this set include this identifier as context.</p> </li> <li> <p> <code>EndTimeBehaviorType</code> – What happens to the agreement when it reaches its end date. Values include <code>RENEW</code>, <code>REPLACE</code>, and <code>EXPIRE</code>.</p> </li> <li> <p> <code>EndTimeBehaviorReasonCode</code> – The reason why the agreement doesn't renew at its end date. Values include <code>PROPOSER_RENEW_OPTED_OUT</code>, <code>ACCEPTOR_RENEW_OPTED_OUT</code>, <code>NO_RENEWAL_TERM</code>, and <code>RENEWAL_LIMIT_EXHAUSTED</code>.</p> </li> <li> <p> <code>InitialAgreementId</code> – The unique identifier of the very first agreement in a chain of related agreements. Use this filter to return every agreement in the same chain.</p> </li> <li> <p> <code>LicenseArn</code> – The Amazon Resource Name (ARN) of the AWS License Manager license associated with an entitlement granted by the agreement.</p> </li> </ul> <p>A proposer can use any combination of the preceding filters along with <code>AgreementType</code>, which is required.</p> <p>The following filter combinations are supported when the <code>PartyType</code> is <code>Acceptor</code>:</p> <ul> <li> <p> <code>AgreementType</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>Status</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>EndTime</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>Status</code> + <code>EndTime</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>ResourceIdentifier</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>ResourceIdentifier</code> + <code>EndTime</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>ResourceIdentifier</code> + <code>Status</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>ResourceIdentifier</code> + <code>Status</code> + <code>EndTime</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>ResourceType</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>ResourceType</code> + <code>EndTime</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>OfferId</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>OfferId</code> + <code>EndTime</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>OfferId</code> + <code>Status</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>OfferId</code> + <code>Status</code> + <code>EndTime</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>OfferSetId</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>OfferSetId</code> + <code>EndTime</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>OfferSetId</code> + <code>Status</code> </p> </li> <li> <p> <code>AgreementType</code> + <code>OfferSetId</code> + <code>Status</code> + <code>EndTime</code> </p> </li> </ul> <note> <p>To filter by <code>EndTime</code>, you can use <code>BeforeEndTime</code>, <code>AfterEndTime</code>, or both.</p> </note>
            sort: <p>An object that contains the <code>SortBy</code> and <code>SortOrder</code> attributes. For <code>SearchAgreements</code>, <code>SortBy</code> supports <code>EndTime</code> for both party types, and <code>StartTime</code> and <code>LastUpdateTime</code> only when <code>PartyType</code> is <code>Proposer</code>. The default <code>SortBy</code> value is <code>EndTime</code>.</p>
            max_results: <p>The maximum number of agreements to return in the response.</p>
            next_token: <p>A token to specify where to start pagination.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.search_agreements_input.SearchAgreementsInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.search_agreements_output.SearchAgreementsOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.search_agreements

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.search_agreements.async_search_agreements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.search_agreements_input.SearchAgreementsInput = {}
        if catalog is not None:
            input_["catalog"] = catalog
        if filters is not None:
            input_["filters"] = filters
        if sort is not None:
            input_["sort"] = sort
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

    async def iter_search_agreements(
        self,
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        catalog: Optional["capo_marketplace_agreement.types.catalog.Catalog"] = None,
        filters: Optional[
            "capo_marketplace_agreement.types.filter_list.FilterList"
        ] = None,
        sort: Optional["capo_marketplace_agreement.types.sort.Sort"] = None,
        max_results: Optional[
            "capo_marketplace_agreement.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_marketplace_agreement.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_marketplace_agreement.types.agreement_view_summary.AgreementViewSummary]":
        _token = next_token
        while True:
            _response = await self.search_agreements(
                config_overrides=config_overrides,
                catalog=catalog,
                filters=filters,
                sort=sort,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("agreement_view_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def send_agreement_cancellation_request(
        self,
        agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId",
        reason_code: "capo_marketplace_agreement.types.agreement_cancellation_request_reason_code.AgreementCancellationRequestReasonCode",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        client_token: Optional[
            "capo_marketplace_agreement.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_marketplace_agreement.types.agreement_cancellation_request_description.AgreementCancellationRequestDescription"
        ] = None,
    ) -> "capo_marketplace_agreement.types.send_agreement_cancellation_request_output.SendAgreementCancellationRequestOutput":
        """<p>Allows sellers (proposers) to submit a cancellation request for an active agreement. The cancellation request is created in <code>PENDING_APPROVAL</code> status, at which point the buyer can review it.</p>

        Args:
            agreement_id: <p>The unique identifier of the agreement for which the cancellation request is being submitted.</p>
            reason_code: <p>The reason code for the cancellation request.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            description: <p>An optional detailed description of the cancellation reason (1-2000 characters).</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.conflict_exception.ConflictException: <p>Request was denied due to a resource conflict.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Send a cancellation request

            >>> await client.send_agreement_cancellation_request(agreement_id='agmt-752jqvg74yo7k4h56cakk6396', reason_code='OTHER', description='Due to budget constraints, we are unable to continue with our current subscription', client_token='53nQSKWt6AjrsiZPhzQyZT')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.send_agreement_cancellation_request_input.SendAgreementCancellationRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.send_agreement_cancellation_request_output.SendAgreementCancellationRequestOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.send_agreement_cancellation_request

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.send_agreement_cancellation_request.async_send_agreement_cancellation_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.send_agreement_cancellation_request_input.SendAgreementCancellationRequestInput = {
            "agreement_id": agreement_id,
            "reason_code": reason_code,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_agreement_payment_request(
        self,
        agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId",
        term_id: "capo_marketplace_agreement.types.term_id.TermId",
        name: "capo_marketplace_agreement.types.payment_request_name.PaymentRequestName",
        charge_amount: "capo_marketplace_agreement.types.positive_amount_upto8_decimals.PositiveAmountUpto8Decimals",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
        client_token: Optional[
            "capo_marketplace_agreement.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_marketplace_agreement.types.payment_request_description.PaymentRequestDescription"
        ] = None,
    ) -> "capo_marketplace_agreement.types.send_agreement_payment_request_output.SendAgreementPaymentRequestOutput":
        """<p>Allows sellers (proposers) to submit a payment request to buyers (acceptors) for a specific charge amount for an agreement that includes a <code>VariablePaymentTerm</code>. The payment request is created in <code>PENDING_APPROVAL</code> status, at which point the buyer can accept or reject it.</p> <note> <p>The agreement must be active and have a <code>VariablePaymentTerm</code> to support payment requests. The <code>chargeAmount</code> must not exceed the remaining available balance under the <code>VariablePaymentTerm</code> <code>maxTotalChargeAmount</code>.</p> </note>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            agreement_id: <p>The unique identifier of the agreement for which the payment request is being submitted. Use <code>GetAgreementTerms</code> to retrieve agreement term details.</p>
            term_id: <p>The unique identifier of the <code>VariablePaymentTerm</code> for the agreement that the payment request is being sent for.</p>
            name: <p>A descriptive name for the payment request (5-64 characters).</p>
            charge_amount: <p>The amount requested to be charged to the buyer, positive decimal value in the currency of the accepted term.</p> <note> <p>A <code>ValidationException</code> is returned if the <code>chargeAmount</code> exceeds the available balance, if the agreement doesn't have an active <code>VariablePaymentTerm</code>, or if the <code>termId</code> is invalid.</p> </note>
            description: <p>An optional detailed description of the payment request (1-2000 characters).</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.conflict_exception.ConflictException: <p>Request was denied due to a resource conflict.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.send_agreement_payment_request_input.SendAgreementPaymentRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.send_agreement_payment_request_output.SendAgreementPaymentRequestOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.send_agreement_payment_request

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.send_agreement_payment_request.async_send_agreement_payment_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.send_agreement_payment_request_input.SendAgreementPaymentRequestInput = {
            "agreement_id": agreement_id,
            "term_id": term_id,
            "name": name,
            "charge_amount": charge_amount,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_purchase_orders(
        self,
        purchase_orders: "capo_marketplace_agreement.types.purchase_orders.PurchaseOrders",
        *,
        config_overrides: Optional[AsyncMarketplaceAgreementClientConfig] = None,
    ) -> "capo_marketplace_agreement.types.update_purchase_orders_output.UpdatePurchaseOrdersOutput":
        """<p>Allows acceptors to associate purchase orders with agreement charges after an agreement is created.</p>

        Args:
            purchase_orders: <p>Contains information about purchase order associations.</p>

        Raises:
            capo_marketplace_agreement.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_marketplace_agreement.errors.conflict_exception.ConflictException: <p>Request was denied due to a resource conflict.</p>
            capo_marketplace_agreement.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_marketplace_agreement.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_marketplace_agreement.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_marketplace_agreement.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_agreement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_agreement.types.update_purchase_orders_input.UpdatePurchaseOrdersInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_agreement.types.update_purchase_orders_output.UpdatePurchaseOrdersOutput"
        ]:
            import capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.update_purchase_orders

            (
                output,
                http_response,
            ) = await capo_marketplace_agreement._operations.awsmp_commerce_service_v20200301.update_purchase_orders.async_update_purchase_orders(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_agreement.types.update_purchase_orders_input.UpdatePurchaseOrdersInput = {
            "purchase_orders": purchase_orders
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
