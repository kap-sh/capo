"""Generated from Smithy shape ``com.amazonaws.invoicing#Invoicing``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_invoicing._auth._signers
import capo_invoicing._auth._sigv4
from capo_invoicing._auth._identity import Credentials
from capo_invoicing._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_invoicing._auth._zapros_handler import AuthMiddleware
from capo_invoicing._pagination import resolve_path as _resolve_path
from capo_invoicing._services._aws_config import aaws_config
from capo_invoicing._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_invoicing.types.account_id_list
    import capo_invoicing.types.account_id_string
    import capo_invoicing.types.as_of_timestamp
    import capo_invoicing.types.basic_string
    import capo_invoicing.types.basic_string_without_space
    import capo_invoicing.types.batch_get_invoice_profile_request
    import capo_invoicing.types.batch_get_invoice_profile_response
    import capo_invoicing.types.buyer_domain
    import capo_invoicing.types.contacts
    import capo_invoicing.types.create_invoice_unit_request
    import capo_invoicing.types.create_invoice_unit_response
    import capo_invoicing.types.create_procurement_portal_preference_request
    import capo_invoicing.types.create_procurement_portal_preference_response
    import capo_invoicing.types.delete_invoice_unit_request
    import capo_invoicing.types.delete_invoice_unit_response
    import capo_invoicing.types.delete_procurement_portal_preference_request
    import capo_invoicing.types.delete_procurement_portal_preference_response
    import capo_invoicing.types.description_string
    import capo_invoicing.types.einvoice_delivery_preference
    import capo_invoicing.types.filters
    import capo_invoicing.types.get_invoice_pdf_request
    import capo_invoicing.types.get_invoice_pdf_response
    import capo_invoicing.types.get_invoice_unit_request
    import capo_invoicing.types.get_invoice_unit_response
    import capo_invoicing.types.get_procurement_portal_preference_request
    import capo_invoicing.types.get_procurement_portal_preference_response
    import capo_invoicing.types.invoice_summaries_filter
    import capo_invoicing.types.invoice_summaries_max_results
    import capo_invoicing.types.invoice_summaries_selector
    import capo_invoicing.types.invoice_summary
    import capo_invoicing.types.invoice_unit
    import capo_invoicing.types.invoice_unit_arn_string
    import capo_invoicing.types.invoice_unit_name
    import capo_invoicing.types.invoice_unit_rule
    import capo_invoicing.types.list_invoice_summaries_request
    import capo_invoicing.types.list_invoice_summaries_response
    import capo_invoicing.types.list_invoice_units_request
    import capo_invoicing.types.list_invoice_units_response
    import capo_invoicing.types.list_procurement_portal_preferences_request
    import capo_invoicing.types.list_procurement_portal_preferences_response
    import capo_invoicing.types.list_procurement_portal_suppliers_request
    import capo_invoicing.types.list_procurement_portal_suppliers_response
    import capo_invoicing.types.list_procurement_portals_request
    import capo_invoicing.types.list_procurement_portals_response
    import capo_invoicing.types.list_tags_for_resource_request
    import capo_invoicing.types.list_tags_for_resource_response
    import capo_invoicing.types.marketplace_punch_out_preference
    import capo_invoicing.types.max_results
    import capo_invoicing.types.max_results_integer
    import capo_invoicing.types.next_token_string
    import capo_invoicing.types.procurement_portal
    import capo_invoicing.types.procurement_portal_id_string
    import capo_invoicing.types.procurement_portal_name
    import capo_invoicing.types.procurement_portal_preference_arn_string
    import capo_invoicing.types.procurement_portal_preference_selector
    import capo_invoicing.types.procurement_portal_preference_status
    import capo_invoicing.types.procurement_portal_preference_summary
    import capo_invoicing.types.procurement_portal_supplier
    import capo_invoicing.types.put_procurement_portal_preference_request
    import capo_invoicing.types.put_procurement_portal_preference_response
    import capo_invoicing.types.resource_tag_key_list
    import capo_invoicing.types.resource_tag_list
    import capo_invoicing.types.send_procurement_portal_validation_request
    import capo_invoicing.types.send_procurement_portal_validation_response
    import capo_invoicing.types.sensitive_basic_string_without_space
    import capo_invoicing.types.string_without_new_line
    import capo_invoicing.types.supplier_domain
    import capo_invoicing.types.tag_resource_request
    import capo_invoicing.types.tag_resource_response
    import capo_invoicing.types.tagris_arn
    import capo_invoicing.types.tax_inheritance_disabled_flag
    import capo_invoicing.types.test_env_preference_input
    import capo_invoicing.types.untag_resource_request
    import capo_invoicing.types.untag_resource_response
    import capo_invoicing.types.update_invoice_unit_request
    import capo_invoicing.types.update_invoice_unit_response
    import capo_invoicing.types.update_procurement_portal_preference_status_request
    import capo_invoicing.types.update_procurement_portal_preference_status_response
    import capo_invoicing.types.verify_procurement_portal_validation_request
    import capo_invoicing.types.verify_procurement_portal_validation_response


class AsyncInvoicingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncInvoicingClient:
    """A client for the ``Invoicing`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = AsyncInvoicingClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncInvoicingClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncInvoicingClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def batch_get_invoice_profile(
        self,
        account_ids: "capo_invoicing.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
    ) -> "capo_invoicing.types.batch_get_invoice_profile_response.BatchGetInvoiceProfileResponse":
        """<p>This gets the invoice profile associated with a set of accounts. The accounts must be linked accounts under the requester management account organization.</p>

        Args:
            account_ids: <p>Retrieves the corresponding invoice profile data for these account IDs. </p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            BatchGetInvoiceProfile

            >>> await client.batch_get_invoice_profile(account_ids=['111111111111'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.batch_get_invoice_profile_request.BatchGetInvoiceProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.batch_get_invoice_profile_response.BatchGetInvoiceProfileResponse"
        ]:
            import capo_invoicing._operations.invoicing.batch_get_invoice_profile

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.batch_get_invoice_profile.async_batch_get_invoice_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.batch_get_invoice_profile_request.BatchGetInvoiceProfileRequest = {
            "account_ids": account_ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_invoice_unit(
        self,
        name: "capo_invoicing.types.invoice_unit_name.InvoiceUnitName",
        invoice_receiver: "capo_invoicing.types.account_id_string.AccountIdString",
        rule: "capo_invoicing.types.invoice_unit_rule.InvoiceUnitRule",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        description: Optional[
            "capo_invoicing.types.description_string.DescriptionString"
        ] = None,
        tax_inheritance_disabled: Optional[
            "capo_invoicing.types.tax_inheritance_disabled_flag.TaxInheritanceDisabledFlag"
        ] = None,
        resource_tags: Optional[
            "capo_invoicing.types.resource_tag_list.ResourceTagList"
        ] = None,
        client_token: Optional[
            "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
        ] = None,
    ) -> "capo_invoicing.types.create_invoice_unit_response.CreateInvoiceUnitResponse":
        """<p>This creates a new invoice unit with the provided definition.</p>

        Args:
            name: <p> The unique name of the invoice unit that is shown on the generated invoice. This can't be changed once it is set. To change this name, you must delete the invoice unit recreate. </p>
            invoice_receiver: <p> The Amazon Web Services account ID chosen to be the receiver of an invoice unit. All invoices generated for that invoice unit will be sent to this account ID. </p>
            description: <p> The invoice unit's description. This can be changed at a later time. </p>
            tax_inheritance_disabled: <p>Whether the invoice unit based tax inheritance is/ should be enabled or disabled. </p>
            rule: <p>The <code>InvoiceUnitRule</code> object used to create invoice units. </p>
            resource_tags: <p> The tag structure that contains a tag key and value. </p>
            client_token: <p> A unique, case-sensitive identifier that you provide to ensure idempotency of the request. </p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateInvoiceUnit

            >>> await client.create_invoice_unit(name='Example Invoice Unit', invoice_receiver='111111111111', description='Example Invoice Unit Description', tax_inheritance_disabled=False, rule={'LinkedAccounts': ['222222222222']}, resource_tags=[{'Key': 'TagKey', 'Value': 'TagValue'}], client_token='e362c68e-4e74-48d7-9228-0bc5aa447b42')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.create_invoice_unit_request.CreateInvoiceUnitRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.create_invoice_unit_response.CreateInvoiceUnitResponse"
        ]:
            import capo_invoicing._operations.invoicing.create_invoice_unit

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.create_invoice_unit.async_create_invoice_unit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.create_invoice_unit_request.CreateInvoiceUnitRequest = {
            "name": name,
            "invoice_receiver": invoice_receiver,
            "rule": rule,
        }
        if description is not None:
            input_["description"] = description
        if tax_inheritance_disabled is not None:
            input_["tax_inheritance_disabled"] = tax_inheritance_disabled
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
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

    async def create_procurement_portal_preference(
        self,
        procurement_portal_name: "capo_invoicing.types.procurement_portal_name.ProcurementPortalName",
        buyer_domain: "capo_invoicing.types.buyer_domain.BuyerDomain",
        buyer_identifier: "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace",
        supplier_domain: "capo_invoicing.types.supplier_domain.SupplierDomain",
        supplier_identifier: "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace",
        einvoice_delivery_enabled: bool,
        purchase_order_retrieval_enabled: bool,
        contacts: "capo_invoicing.types.contacts.Contacts",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        selector: Optional[
            "capo_invoicing.types.procurement_portal_preference_selector.ProcurementPortalPreferenceSelector"
        ] = None,
        procurement_portal_shared_secret: Optional[
            "capo_invoicing.types.sensitive_basic_string_without_space.SensitiveBasicStringWithoutSpace"
        ] = None,
        procurement_portal_instance_endpoint: Optional[
            "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
        ] = None,
        test_env_preference: Optional[
            "capo_invoicing.types.test_env_preference_input.TestEnvPreferenceInput"
        ] = None,
        einvoice_delivery_preference: Optional[
            "capo_invoicing.types.einvoice_delivery_preference.EinvoiceDeliveryPreference"
        ] = None,
        marketplace_punch_out_enabled: Optional[bool] = None,
        marketplace_punch_out_preference: Optional[
            "capo_invoicing.types.marketplace_punch_out_preference.MarketplacePunchOutPreference"
        ] = None,
        resource_tags: Optional[
            "capo_invoicing.types.resource_tag_list.ResourceTagList"
        ] = None,
        client_token: Optional[
            "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
        ] = None,
    ) -> "capo_invoicing.types.create_procurement_portal_preference_response.CreateProcurementPortalPreferenceResponse":
        """<p> <i> <b>This feature API is subject to changing at any time. For more information, see the <a href="https://aws.amazon.com/service-terms/">Amazon Web Services Service Terms</a> (Betas and Previews).</b> </i> </p> <p>Creates a procurement portal preference configuration for e-invoice delivery and purchase order retrieval. This preference defines how invoices are delivered to a procurement portal and how purchase orders are retrieved.</p>

        Args:
            procurement_portal_name: <p>The name of the procurement portal.</p>
            buyer_domain: <p>The domain identifier for the buyer in the procurement portal.</p>
            buyer_identifier: <p>The unique identifier for the buyer in the procurement portal. </p>
            supplier_domain: <p>The domain identifier for the supplier in the procurement portal.</p>
            supplier_identifier: <p>The unique identifier for the supplier in the procurement portal.</p>
            procurement_portal_shared_secret: <p>The shared secret or authentication credential used to establish secure communication with the procurement portal. This value must be encrypted at rest.</p>
            procurement_portal_instance_endpoint: <p>The endpoint URL where e-invoices will be delivered to the procurement portal. Must be a valid HTTPS URL.</p>
            test_env_preference: <p>Configuration settings for the test environment of the procurement portal. Includes test credentials and endpoints that are used for validation before production deployment.</p>
            einvoice_delivery_enabled: <p>Indicates whether e-invoice delivery is enabled for this procurement portal preference. Set to true to enable e-invoice delivery, false to disable.</p>
            einvoice_delivery_preference: <p>Specifies the e-invoice delivery configuration including document types, attachment types, and customization settings for the portal.</p>
            purchase_order_retrieval_enabled: <p>Indicates whether purchase order retrieval is enabled for this procurement portal preference. Set to true to enable PO retrieval, false to disable.</p>
            marketplace_punch_out_enabled: Defaults to false if not provided.
            marketplace_punch_out_preference: Required for Coupa when MarketplacePunchOutEnabled is true.
            contacts: <p>List of contact information for portal administrators and technical contacts responsible for the e-invoice integration.</p>
            resource_tags: <p>The tags to apply to this procurement portal preference resource. Each tag consists of a key and an optional value.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure idempotency of the request.</p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This exception occurs when a concurrent modification is detected during an update operation, or when attempting to create a resource that already exists.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateProcurementPortalPreference for Coupa

            >>> await client.create_procurement_portal_preference(procurement_portal_name='COUPA', buyer_domain='NetworkID', buyer_identifier='BuyerId_1', supplier_domain='NetworkID', supplier_identifier='SupplierId_1', selector={'InvoiceUnitArns': ['arn:aws:invoicing::111111111111:invoice-unit/12345678', 'arn:aws:invoicing::111111111111:invoice-unit/12345679'], 'SellerOfRecords': ['AWS_INC', 'AWS_EUROPE']}, procurement_portal_shared_secret='Coupa_Secret', procurement_portal_instance_endpoint='https://www.placeholder-domain.test', test_env_preference={'BuyerDomain': 'NetworkID', 'BuyerIdentifier': 'BuyerId_1_Test', 'SupplierDomain': 'NetworkID', 'SupplierIdentifier': 'SupplierId_1_Test', 'ProcurementPortalSharedSecret': 'Coupa_Secret_test', 'ProcurementPortalInstanceEndpoint': 'https://www.placeholder-domain.test'}, einvoice_delivery_enabled=True, einvoice_delivery_preference={'EinvoiceDeliveryDocumentTypes': ['AWS_CLOUD_INVOICE'], 'EinvoiceDeliveryAttachmentTypes': ['INVOICE_PDF'], 'Protocol': 'CXML', 'PurchaseOrderDataSources': [{'EinvoiceDeliveryDocumentType': 'AWS_CLOUD_INVOICE', 'PurchaseOrderDataSourceType': 'ASSOCIATED_PURCHASE_ORDER_REQUIRED'}], 'ConnectionTestingMethod': 'PROD_ENV_DOLLAR_TEST', 'EinvoiceDeliveryActivationDate': 1750279280.091}, purchase_order_retrieval_enabled=True, marketplace_punch_out_enabled=True, marketplace_punch_out_preference={'ApprovalRequestRedirectUrl': 'https://www.placeholder-domain.test/approvals'}, contacts=[{'Name': 'John Doe', 'Email': 'example-placeholder@amazon.com'}], resource_tags=[{'Key': 'testKey', 'Value': 'testValue'}], client_token='e362c68e-4e74-48d7-9228-0bc5aa447b42')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.create_procurement_portal_preference_request.CreateProcurementPortalPreferenceRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.create_procurement_portal_preference_response.CreateProcurementPortalPreferenceResponse"
        ]:
            import capo_invoicing._operations.invoicing.create_procurement_portal_preference

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.create_procurement_portal_preference.async_create_procurement_portal_preference(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.create_procurement_portal_preference_request.CreateProcurementPortalPreferenceRequest = {
            "procurement_portal_name": procurement_portal_name,
            "buyer_domain": buyer_domain,
            "buyer_identifier": buyer_identifier,
            "supplier_domain": supplier_domain,
            "supplier_identifier": supplier_identifier,
            "einvoice_delivery_enabled": einvoice_delivery_enabled,
            "purchase_order_retrieval_enabled": purchase_order_retrieval_enabled,
            "contacts": contacts,
        }
        if selector is not None:
            input_["selector"] = selector
        if procurement_portal_shared_secret is not None:
            input_["procurement_portal_shared_secret"] = (
                procurement_portal_shared_secret
            )
        if procurement_portal_instance_endpoint is not None:
            input_["procurement_portal_instance_endpoint"] = (
                procurement_portal_instance_endpoint
            )
        if test_env_preference is not None:
            input_["test_env_preference"] = test_env_preference
        if einvoice_delivery_preference is not None:
            input_["einvoice_delivery_preference"] = einvoice_delivery_preference
        if marketplace_punch_out_enabled is not None:
            input_["marketplace_punch_out_enabled"] = marketplace_punch_out_enabled
        if marketplace_punch_out_preference is not None:
            input_["marketplace_punch_out_preference"] = (
                marketplace_punch_out_preference
            )
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
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

    async def delete_invoice_unit(
        self,
        invoice_unit_arn: "capo_invoicing.types.invoice_unit_arn_string.InvoiceUnitArnString",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        client_token: Optional[
            "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
        ] = None,
    ) -> "capo_invoicing.types.delete_invoice_unit_response.DeleteInvoiceUnitResponse":
        """<p>This deletes an invoice unit with the provided invoice unit ARN. </p>

        Args:
            invoice_unit_arn: <p> The ARN to identify an invoice unit. This information can't be modified or deleted. </p>
            client_token: <p> A unique, case-sensitive identifier that you provide to ensure idempotency of the request. </p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteInvoiceUnit

            >>> await client.delete_invoice_unit(invoice_unit_arn='arn:aws:invoicing::000000000000:invoice-unit/12345678', client_token='e362c68e-4e74-48d7-9228-0bc5aa447b44')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.delete_invoice_unit_request.DeleteInvoiceUnitRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.delete_invoice_unit_response.DeleteInvoiceUnitResponse"
        ]:
            import capo_invoicing._operations.invoicing.delete_invoice_unit

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.delete_invoice_unit.async_delete_invoice_unit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.delete_invoice_unit_request.DeleteInvoiceUnitRequest = {
            "invoice_unit_arn": invoice_unit_arn
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

    async def delete_procurement_portal_preference(
        self,
        procurement_portal_preference_arn: "capo_invoicing.types.procurement_portal_preference_arn_string.ProcurementPortalPreferenceArnString",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        client_token: Optional[
            "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
        ] = None,
    ) -> "capo_invoicing.types.delete_procurement_portal_preference_response.DeleteProcurementPortalPreferenceResponse":
        """<p> <i> <b>This feature API is subject to changing at any time. For more information, see the <a href="https://aws.amazon.com/service-terms/">Amazon Web Services Service Terms</a> (Betas and Previews).</b> </i> </p> <p>Deletes an existing procurement portal preference. This action cannot be undone. Active e-invoice delivery and PO retrieval configurations will be terminated.</p>

        Args:
            procurement_portal_preference_arn: <p>The Amazon Resource Name (ARN) of the procurement portal preference to delete.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure idempotency of the request.</p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This exception occurs when a concurrent modification is detected during an update operation, or when attempting to create a resource that already exists.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found. </p>
            capo_invoicing.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteProcurementPortalPreference call

            >>> await client.delete_procurement_portal_preference(procurement_portal_preference_arn='arn:aws:invoicing::111111111111:procurement-portal-preference/f71dd02e-f855-4b13-b793-0fd25c0b3ecd', client_token='e362c68e-4e74-48d7-9228-0bc5aa447b47')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.delete_procurement_portal_preference_request.DeleteProcurementPortalPreferenceRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.delete_procurement_portal_preference_response.DeleteProcurementPortalPreferenceResponse"
        ]:
            import capo_invoicing._operations.invoicing.delete_procurement_portal_preference

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.delete_procurement_portal_preference.async_delete_procurement_portal_preference(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.delete_procurement_portal_preference_request.DeleteProcurementPortalPreferenceRequest = {
            "procurement_portal_preference_arn": procurement_portal_preference_arn
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

    async def get_invoice_pdf(
        self,
        invoice_id: "capo_invoicing.types.string_without_new_line.StringWithoutNewLine",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
    ) -> "capo_invoicing.types.get_invoice_pdf_response.GetInvoicePDFResponse":
        """<p>Returns a URL to download the invoice document and supplemental documents associated with an invoice. The URLs are pre-signed and have expiration time. For special cases like Brazil, where Amazon Web Services generated invoice identifiers and government provided identifiers do not match, use the Amazon Web Services generated invoice identifier when making API requests. To grant IAM permission to use this operation, the caller needs the <code>invoicing:GetInvoicePDF</code> policy action.</p>

        Args:
            invoice_id: <p> Your unique invoice ID. </p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetInvoicePDF without supplemental documents

            >>> await client.get_invoice_pdf(invoice_id='abc123')
            GetInvoicePDF with supplemental documents

            >>> await client.get_invoice_pdf(invoice_id='abc123')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.get_invoice_pdf_request.GetInvoicePDFRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.get_invoice_pdf_response.GetInvoicePDFResponse"
        ]:
            import capo_invoicing._operations.invoicing.get_invoice_pdf

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.get_invoice_pdf.async_get_invoice_pdf(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.get_invoice_pdf_request.GetInvoicePDFRequest = {
            "invoice_id": invoice_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_invoice_unit(
        self,
        invoice_unit_arn: "capo_invoicing.types.invoice_unit_arn_string.InvoiceUnitArnString",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        as_of: Optional["capo_invoicing.types.as_of_timestamp.AsOfTimestamp"] = None,
    ) -> "capo_invoicing.types.get_invoice_unit_response.GetInvoiceUnitResponse":
        """<p>This retrieves the invoice unit definition.</p>

        Args:
            invoice_unit_arn: <p> The ARN to identify an invoice unit. This information can't be modified or deleted. </p>
            as_of: <p> The state of an invoice unit at a specified time. You can see legacy invoice units that are currently deleted if the <code>AsOf</code> time is set to before it was deleted. If an <code>AsOf</code> is not provided, the default value is the current time. </p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetInvoiceUnit as of current time

            >>> await client.get_invoice_unit(invoice_unit_arn='arn:aws:invoicing::000000000000:invoice-unit/12345678')
            GetInvoiceUnit as of specified time

            >>> await client.get_invoice_unit(invoice_unit_arn='arn:aws:invoicing::000000000000:invoice-unit/87654321', as_of=1733097600)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.get_invoice_unit_request.GetInvoiceUnitRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.get_invoice_unit_response.GetInvoiceUnitResponse"
        ]:
            import capo_invoicing._operations.invoicing.get_invoice_unit

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.get_invoice_unit.async_get_invoice_unit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.get_invoice_unit_request.GetInvoiceUnitRequest = {
            "invoice_unit_arn": invoice_unit_arn
        }
        if as_of is not None:
            input_["as_of"] = as_of

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_procurement_portal_preference(
        self,
        procurement_portal_preference_arn: "capo_invoicing.types.procurement_portal_preference_arn_string.ProcurementPortalPreferenceArnString",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
    ) -> "capo_invoicing.types.get_procurement_portal_preference_response.GetProcurementPortalPreferenceResponse":
        """<p> <i> <b>This feature API is subject to changing at any time. For more information, see the <a href="https://aws.amazon.com/service-terms/">Amazon Web Services Service Terms</a> (Betas and Previews).</b> </i> </p> <p>Retrieves the details of a specific procurement portal preference configuration.</p>

        Args:
            procurement_portal_preference_arn: <p>The Amazon Resource Name (ARN) of the procurement portal preference to retrieve.</p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This exception occurs when a concurrent modification is detected during an update operation, or when attempting to create a resource that already exists.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found. </p>
            capo_invoicing.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetProcurementPortalPreference for Coupa pref

            >>> await client.get_procurement_portal_preference(procurement_portal_preference_arn='arn:aws:invoicing::111111111111:procurement-portal-preference/a34fd666-7810-4414-9360-aaa4bcab0abd')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.get_procurement_portal_preference_request.GetProcurementPortalPreferenceRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.get_procurement_portal_preference_response.GetProcurementPortalPreferenceResponse"
        ]:
            import capo_invoicing._operations.invoicing.get_procurement_portal_preference

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.get_procurement_portal_preference.async_get_procurement_portal_preference(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.get_procurement_portal_preference_request.GetProcurementPortalPreferenceRequest = {
            "procurement_portal_preference_arn": procurement_portal_preference_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_invoice_summaries(
        self,
        selector: "capo_invoicing.types.invoice_summaries_selector.InvoiceSummariesSelector",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        filter: Optional[
            "capo_invoicing.types.invoice_summaries_filter.InvoiceSummariesFilter"
        ] = None,
        next_token: Optional[
            "capo_invoicing.types.next_token_string.NextTokenString"
        ] = None,
        max_results: Optional[
            "capo_invoicing.types.invoice_summaries_max_results.InvoiceSummariesMaxResults"
        ] = None,
    ) -> "capo_invoicing.types.list_invoice_summaries_response.ListInvoiceSummariesResponse":
        """<p>Retrieves your invoice details programmatically, without line item details.</p>

        Args:
            selector: <p>The option to retrieve details for a specific invoice by providing its unique ID. Alternatively, access information for all invoices linked to the account by providing an account ID.</p>
            filter: <p>Filters you can use to customize your invoice summary.</p>
            next_token: <p>The token for the next set of results. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of invoice summaries a paginated response can contain.</p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListInvoiceSummaries with InvoiceId as selector

            >>> await client.list_invoice_summaries(selector={'ResourceType': 'INVOICE_ID', 'Value': '1111111111'})
            ListInvoiceSummaries with AccountId as selector and billing period

            >>> await client.list_invoice_summaries(selector={'ResourceType': 'ACCOUNT_ID', 'Value': '111111111111'}, filter={'BillingPeriod': {'Month': 1, 'Year': 2025}})
            ListInvoiceSummaries with AccountId as selector and time interval

            >>> await client.list_invoice_summaries(selector={'ResourceType': 'ACCOUNT_ID', 'Value': '111111111111'}, filter={'TimeInterval': {'StartDate': 1590997407, 'EndDate': 1592639007}})
            ListInvoiceSummaries filtered by ReceiverRole

            >>> await client.list_invoice_summaries(selector={'ResourceType': 'ACCOUNT_ID', 'Value': '111111111111'}, filter={'TimeInterval': {'StartDate': 1748736000, 'EndDate': 1751328000}, 'ReceiverRole': 'SELLER'})
            ListInvoiceSummaries with AccountId as selector and a billing period and max results

            >>> await client.list_invoice_summaries(selector={'ResourceType': 'ACCOUNT_ID', 'Value': '111111111111'}, filter={'BillingPeriod': {'Month': 1, 'Year': 2025}}, max_results=1)
            ListInvoiceSummaries with AccountId as selector and a billing period and next token

            >>> await client.list_invoice_summaries(selector={'ResourceType': 'ACCOUNT_ID', 'Value': '111111111111'}, filter={'BillingPeriod': {'Month': 1, 'Year': 2025}}, next_token='abcde12345')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.list_invoice_summaries_request.ListInvoiceSummariesRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.list_invoice_summaries_response.ListInvoiceSummariesResponse"
        ]:
            import capo_invoicing._operations.invoicing.list_invoice_summaries

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.list_invoice_summaries.async_list_invoice_summaries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.list_invoice_summaries_request.ListInvoiceSummariesRequest = {
            "selector": selector
        }
        if filter is not None:
            input_["filter"] = filter
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

    async def iter_list_invoice_summaries(
        self,
        selector: "capo_invoicing.types.invoice_summaries_selector.InvoiceSummariesSelector",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        filter: Optional[
            "capo_invoicing.types.invoice_summaries_filter.InvoiceSummariesFilter"
        ] = None,
        next_token: Optional[
            "capo_invoicing.types.next_token_string.NextTokenString"
        ] = None,
        max_results: Optional[
            "capo_invoicing.types.invoice_summaries_max_results.InvoiceSummariesMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_invoicing.types.invoice_summary.InvoiceSummary]":
        _token = next_token
        while True:
            _response = await self.list_invoice_summaries(
                selector,
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("invoice_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_invoice_units(
        self,
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        filters: Optional["capo_invoicing.types.filters.Filters"] = None,
        next_token: Optional[
            "capo_invoicing.types.next_token_string.NextTokenString"
        ] = None,
        max_results: Optional[
            "capo_invoicing.types.max_results_integer.MaxResultsInteger"
        ] = None,
        as_of: Optional["capo_invoicing.types.as_of_timestamp.AsOfTimestamp"] = None,
    ) -> "capo_invoicing.types.list_invoice_units_response.ListInvoiceUnitsResponse":
        """<p>This fetches a list of all invoice unit definitions for a given account, as of the provided <code>AsOf</code> date.</p>

        Args:
            filters: <p> An optional input to the list API. If multiple filters are specified, the returned list will be a configuration that match all of the provided filters. Supported filter types are <code>InvoiceReceivers</code>, <code>Names</code>, and <code>Accounts</code>. </p>
            next_token: <p>The next token used to indicate where the returned list should start from. </p>
            max_results: <p>The maximum number of invoice units that can be returned. </p>
            as_of: <p> The state of an invoice unit at a specified time. You can see legacy invoice units that are currently deleted if the <code>AsOf</code> time is set to before it was deleted. If an <code>AsOf</code> is not provided, the default value is the current time. </p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListInvoiceUnits without filters as of current time

            >>> await client.list_invoice_units()
            ListInvoiceUnits with filters as of specified time

            >>> await client.list_invoice_units(as_of=1733097600, filters={'InvoiceReceivers': ['333333333333']})
            ListInvoiceUnits with pagination - first page

            >>> await client.list_invoice_units(max_results=1)
            ListInvoiceUnits with pagination - second page

            >>> await client.list_invoice_units(max_results=1, next_token='nextTokenExample')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.list_invoice_units_request.ListInvoiceUnitsRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.list_invoice_units_response.ListInvoiceUnitsResponse"
        ]:
            import capo_invoicing._operations.invoicing.list_invoice_units

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.list_invoice_units.async_list_invoice_units(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.list_invoice_units_request.ListInvoiceUnitsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if as_of is not None:
            input_["as_of"] = as_of

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_invoice_units(
        self,
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        filters: Optional["capo_invoicing.types.filters.Filters"] = None,
        next_token: Optional[
            "capo_invoicing.types.next_token_string.NextTokenString"
        ] = None,
        max_results: Optional[
            "capo_invoicing.types.max_results_integer.MaxResultsInteger"
        ] = None,
        as_of: Optional["capo_invoicing.types.as_of_timestamp.AsOfTimestamp"] = None,
    ) -> "AsyncIterator[capo_invoicing.types.invoice_unit.InvoiceUnit]":
        _token = next_token
        while True:
            _response = await self.list_invoice_units(
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
                as_of=as_of,
            )
            _page = _resolve_path(_response, ("invoice_units",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_procurement_portal_preferences(
        self,
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        next_token: Optional[
            "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
        ] = None,
        max_results: Optional["capo_invoicing.types.max_results.MaxResults"] = None,
    ) -> "capo_invoicing.types.list_procurement_portal_preferences_response.ListProcurementPortalPreferencesResponse":
        """<p> <i> <b>This feature API is subject to changing at any time. For more information, see the <a href="https://aws.amazon.com/service-terms/">Amazon Web Services Service Terms</a> (Betas and Previews).</b> </i> </p> <p>Retrieves a list of procurement portal preferences associated with the Amazon Web Services account.</p>

        Args:
            next_token: <p>The token for the next set of results. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.</p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This exception occurs when a concurrent modification is detected during an update operation, or when attempting to create a resource that already exists.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListProcurementPortalPreferences for Coupa prefs. First Call with following pages

            >>> await client.list_procurement_portal_preferences(max_results=2)
            ListProcurementPortalPreferences for Coupa prefs. Second Call with the last page

            >>> await client.list_procurement_portal_preferences(next_token='AAQA-EFRSURBSGpkVFU5MVNUVWNXTzNoUEptWEFGcEt0QzBBeHZaZmRUU2w3L0hRQmdDeEx3R0NuSnF2NjM5NGNmM1I5KzNIQzNnT0FBQUFmakI4QmdrcWhraUc5dzBCQndhZ2J6QnRBZ0VBTUdnR0NTcUdTSWIzRFFFSEFUQWVCZ2xnaGtnQlpRTUVBUzR3RVFRTVhPSnhEQ04rWk1idnAyb1RBZ0VRZ0RzbFJBeFlXMk9RRGFtTU8vdFc0MUJlTFFNU2hPR1E5bDM3MHcyS05mSjIzbU93MG1aVXk1MzBiWWVsZ3FaZzhjMndhTjZtNzNYTWd3bnpsZz09E8JRNUKK1r2-b9X8Qd1RAOSKHZOCy-UCpOQjJdSfZHcUefTH0YmlIW8ykllegYUWB1D1NjDjC3u2z2e4cLBTmQhrQewSBW-I_i8okXup9RWN60eMOnB6dl5jUiinJ-FjY_jGjbOkiWuJhXteDKP16RfVRW7mxp2-v1-B8gPPxGLolXHBHrb8gt18P8eWs8RcvRRmmbGUy5qa6nFH5WiCq9Bx2fTUTy9Iz_xZooNuiqC6y119EGQqJ9WsWsIUa8MbWHFXtn9-Uriz7osYocbFm1Evv_NCn3YK-wFy9rUlUskcM2n9AqvPYhOyf0reV7E8cErZFR_Ev8l008QcxQfaqK19-gKR9clddwoDzMVfVuyiW3vbzUXz7fzQLr-UMLCGdE3yHf1oz2SEbcxhHZ2eh7-9wEYDv0v92wXg7m7xaYvaKuVBPKqBaq66GdpS1HTfakkjRGvsoBStXWVgPahISglPO__-Ym5NnXOw2wENBVXZ7RsVe6nJ1X15bB1RDkqLV8xJD0L83snuCEBtM9pyUUQOPvfGHzC4yRusMgBav_y1kq0wjqsbJV5EhHV_SIwf-WZa_A==', max_results=2)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.list_procurement_portal_preferences_request.ListProcurementPortalPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.list_procurement_portal_preferences_response.ListProcurementPortalPreferencesResponse"
        ]:
            import capo_invoicing._operations.invoicing.list_procurement_portal_preferences

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.list_procurement_portal_preferences.async_list_procurement_portal_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.list_procurement_portal_preferences_request.ListProcurementPortalPreferencesRequest = {}
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

    async def iter_list_procurement_portal_preferences(
        self,
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        next_token: Optional[
            "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
        ] = None,
        max_results: Optional["capo_invoicing.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_invoicing.types.procurement_portal_preference_summary.ProcurementPortalPreferenceSummary]":
        _token = next_token
        while True:
            _response = await self.list_procurement_portal_preferences(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("procurement_portal_preferences",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_procurement_portals(
        self,
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        next_token: Optional[
            "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
        ] = None,
        max_results: Optional["capo_invoicing.types.max_results.MaxResults"] = None,
    ) -> "capo_invoicing.types.list_procurement_portals_response.ListProcurementPortalsResponse":
        """<p>Returns the Amazon Web Services-supported procurement portals for e-invoice delivery and purchase order retrieval. Each entry includes the portal identifier, name, and default feature configurations, which define the supported document and attachment types. For faster, more reliable responses, use pagination.</p>

        Args:
            next_token: <p>The token for the next set of results. You received this token from a previous call.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value. Default is 100.</p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListProcurementPortals

            >>> await client.list_procurement_portals()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.list_procurement_portals_request.ListProcurementPortalsRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.list_procurement_portals_response.ListProcurementPortalsResponse"
        ]:
            import capo_invoicing._operations.invoicing.list_procurement_portals

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.list_procurement_portals.async_list_procurement_portals(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.list_procurement_portals_request.ListProcurementPortalsRequest = {}
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

    async def iter_list_procurement_portals(
        self,
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        next_token: Optional[
            "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
        ] = None,
        max_results: Optional["capo_invoicing.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_invoicing.types.procurement_portal.ProcurementPortal]":
        _token = next_token
        while True:
            _response = await self.list_procurement_portals(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("procurement_portals",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_procurement_portal_suppliers(
        self,
        portal_identifier: "capo_invoicing.types.procurement_portal_id_string.ProcurementPortalIdString",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        next_token: Optional[
            "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
        ] = None,
        max_results: Optional["capo_invoicing.types.max_results.MaxResults"] = None,
    ) -> "capo_invoicing.types.list_procurement_portal_suppliers_response.ListProcurementPortalSuppliersResponse":
        """<p>Returns the suppliers configured for a specified procurement portal, including supplier identifiers and associated metadata. For faster, more reliable responses, use pagination.</p>

        Args:
            portal_identifier: <p>The unique identifier of the procurement portal for which to list suppliers. Use the <code>PortalIdentifier</code> value returned by <code>ListProcurementPortals</code>.</p>
            next_token: <p>The token for the next set of results. You received this token from a previous call.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value. Default is 100.</p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListProcurementPortalSuppliers

            >>> await client.list_procurement_portal_suppliers(portal_identifier='KXMJQWBRNP')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.list_procurement_portal_suppliers_request.ListProcurementPortalSuppliersRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.list_procurement_portal_suppliers_response.ListProcurementPortalSuppliersResponse"
        ]:
            import capo_invoicing._operations.invoicing.list_procurement_portal_suppliers

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.list_procurement_portal_suppliers.async_list_procurement_portal_suppliers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.list_procurement_portal_suppliers_request.ListProcurementPortalSuppliersRequest = {
            "portal_identifier": portal_identifier
        }
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

    async def iter_list_procurement_portal_suppliers(
        self,
        portal_identifier: "capo_invoicing.types.procurement_portal_id_string.ProcurementPortalIdString",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        next_token: Optional[
            "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
        ] = None,
        max_results: Optional["capo_invoicing.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_invoicing.types.procurement_portal_supplier.ProcurementPortalSupplier]":
        _token = next_token
        while True:
            _response = await self.list_procurement_portal_suppliers(
                portal_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("procurement_portal_suppliers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_invoicing.types.tagris_arn.TagrisArn",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
    ) -> "capo_invoicing.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for a resource. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of tags to list. </p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListTagsForResource

            >>> await client.list_tags_for_resource(resource_arn='arn:aws:invoicing::000000000000:invoice-unit/12345678')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_invoicing._operations.invoicing.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_procurement_portal_preference(
        self,
        procurement_portal_preference_arn: "capo_invoicing.types.procurement_portal_preference_arn_string.ProcurementPortalPreferenceArnString",
        einvoice_delivery_enabled: bool,
        purchase_order_retrieval_enabled: bool,
        contacts: "capo_invoicing.types.contacts.Contacts",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        selector: Optional[
            "capo_invoicing.types.procurement_portal_preference_selector.ProcurementPortalPreferenceSelector"
        ] = None,
        procurement_portal_shared_secret: Optional[
            "capo_invoicing.types.sensitive_basic_string_without_space.SensitiveBasicStringWithoutSpace"
        ] = None,
        procurement_portal_instance_endpoint: Optional[
            "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
        ] = None,
        test_env_preference: Optional[
            "capo_invoicing.types.test_env_preference_input.TestEnvPreferenceInput"
        ] = None,
        einvoice_delivery_preference: Optional[
            "capo_invoicing.types.einvoice_delivery_preference.EinvoiceDeliveryPreference"
        ] = None,
        marketplace_punch_out_enabled: Optional[bool] = None,
        marketplace_punch_out_preference: Optional[
            "capo_invoicing.types.marketplace_punch_out_preference.MarketplacePunchOutPreference"
        ] = None,
        client_token: Optional[
            "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
        ] = None,
    ) -> "capo_invoicing.types.put_procurement_portal_preference_response.PutProcurementPortalPreferenceResponse":
        """<p> <i> <b>This feature API is subject to changing at any time. For more information, see the <a href="https://aws.amazon.com/service-terms/">Amazon Web Services Service Terms</a> (Betas and Previews).</b> </i> </p> <p>Updates an existing procurement portal preference configuration. This operation can modify settings for e-invoice delivery and purchase order retrieval.</p>

        Args:
            procurement_portal_preference_arn: <p>The Amazon Resource Name (ARN) of the procurement portal preference to update.</p>
            procurement_portal_shared_secret: <p>The updated shared secret or authentication credential for the procurement portal. This value must be encrypted at rest.</p>
            procurement_portal_instance_endpoint: <p>The updated endpoint URL where e-invoices will be delivered to the procurement portal. Must be a valid HTTPS URL.</p>
            test_env_preference: <p>Updated configuration settings for the test environment of the procurement portal.</p>
            einvoice_delivery_enabled: <p>Updated flag indicating whether e-invoice delivery is enabled for this procurement portal preference.</p>
            einvoice_delivery_preference: <p>Updated e-invoice delivery configuration including document types, attachment types, and customization settings for the portal.</p>
            purchase_order_retrieval_enabled: <p>Updated flag indicating whether purchase order retrieval is enabled for this procurement portal preference.</p>
            marketplace_punch_out_enabled: Whether Marketplace PunchOut is enabled for this connection. Defaults to false if not provided.
            marketplace_punch_out_preference: Configuration for Marketplace PunchOut. Required when MarketplacePunchOutEnabled is true.
            contacts: <p>Updated list of contact information for portal administrators and technical contacts.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure idempotency of the request.</p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This exception occurs when a concurrent modification is detected during an update operation, or when attempting to create a resource that already exists.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found. </p>
            capo_invoicing.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            PutProcurementPortalPreference for Coupa pref

            >>> await client.put_procurement_portal_preference(procurement_portal_preference_arn='arn:aws:invoicing::111111111111:procurement-portal-preference/f71dd02e-f855-4b13-b793-0fd25c0b3ecd', procurement_portal_shared_secret='Coupa_Secret_2', procurement_portal_instance_endpoint='https://www.placeholder-domain.test', selector={'InvoiceUnitArns': ['arn:aws:invoicing::111111111111:invoice-unit/12345679'], 'SellerOfRecords': ['AWS_INC']}, test_env_preference={'BuyerDomain': 'NetworkID', 'BuyerIdentifier': 'BuyerId_1_Test', 'SupplierDomain': 'NetworkID', 'SupplierIdentifier': 'SupplierId_1_Test', 'ProcurementPortalSharedSecret': 'Coupa_Secret_test_2', 'ProcurementPortalInstanceEndpoint': 'https://www.placeholder-domain.test'}, einvoice_delivery_enabled=True, einvoice_delivery_preference={'EinvoiceDeliveryDocumentTypes': ['AWS_CLOUD_INVOICE'], 'EinvoiceDeliveryAttachmentTypes': ['INVOICE_PDF'], 'Protocol': 'CXML', 'PurchaseOrderDataSources': [{'EinvoiceDeliveryDocumentType': 'AWS_CLOUD_INVOICE', 'PurchaseOrderDataSourceType': 'ASSOCIATED_PURCHASE_ORDER_REQUIRED'}], 'ConnectionTestingMethod': 'PROD_ENV_DOLLAR_TEST', 'EinvoiceDeliveryActivationDate': 1750279280.091}, purchase_order_retrieval_enabled=True, marketplace_punch_out_enabled=True, contacts=[{'Name': 'John Doe2', 'Email': 'example-placeholder2@amazon.com'}], client_token='e362c68e-4e74-48d7-9228-0bc5aa447b45')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.put_procurement_portal_preference_request.PutProcurementPortalPreferenceRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.put_procurement_portal_preference_response.PutProcurementPortalPreferenceResponse"
        ]:
            import capo_invoicing._operations.invoicing.put_procurement_portal_preference

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.put_procurement_portal_preference.async_put_procurement_portal_preference(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.put_procurement_portal_preference_request.PutProcurementPortalPreferenceRequest = {
            "procurement_portal_preference_arn": procurement_portal_preference_arn,
            "einvoice_delivery_enabled": einvoice_delivery_enabled,
            "purchase_order_retrieval_enabled": purchase_order_retrieval_enabled,
            "contacts": contacts,
        }
        if selector is not None:
            input_["selector"] = selector
        if procurement_portal_shared_secret is not None:
            input_["procurement_portal_shared_secret"] = (
                procurement_portal_shared_secret
            )
        if procurement_portal_instance_endpoint is not None:
            input_["procurement_portal_instance_endpoint"] = (
                procurement_portal_instance_endpoint
            )
        if test_env_preference is not None:
            input_["test_env_preference"] = test_env_preference
        if einvoice_delivery_preference is not None:
            input_["einvoice_delivery_preference"] = einvoice_delivery_preference
        if marketplace_punch_out_enabled is not None:
            input_["marketplace_punch_out_enabled"] = marketplace_punch_out_enabled
        if marketplace_punch_out_preference is not None:
            input_["marketplace_punch_out_preference"] = (
                marketplace_punch_out_preference
            )
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

    async def send_procurement_portal_validation(
        self,
        procurement_portal_preference_arn: "capo_invoicing.types.procurement_portal_preference_arn_string.ProcurementPortalPreferenceArnString",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        client_token: Optional[
            "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
        ] = None,
    ) -> "capo_invoicing.types.send_procurement_portal_validation_response.SendProcurementPortalValidationResponse":
        """<p> <i> <b>This feature API is subject to changing at any time. For more information, see the <a href="https://aws.amazon.com/service-terms/">Amazon Web Services Service Terms</a> (Betas and Previews).</b> </i> </p> <p>Sends a validation request for a procurement portal preference. This operation initiates the validation process by issuing a validation code that confirms ownership and connectivity of the configured procurement portal endpoint. Use <code>VerifyProcurementPortalValidation</code> to submit the received code and complete validation.</p>

        Args:
            procurement_portal_preference_arn: <p>The Amazon Resource Name (ARN) of the procurement portal preference to validate.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure idempotency of the request.</p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            SendProcurementPortalValidation call

            >>> await client.send_procurement_portal_validation(procurement_portal_preference_arn='arn:aws:invoicing::111111111111:procurement-portal-preference/f71dd02e-f855-4b13-b793-0fd25c0b3ecd')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.send_procurement_portal_validation_request.SendProcurementPortalValidationRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.send_procurement_portal_validation_response.SendProcurementPortalValidationResponse"
        ]:
            import capo_invoicing._operations.invoicing.send_procurement_portal_validation

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.send_procurement_portal_validation.async_send_procurement_portal_validation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.send_procurement_portal_validation_request.SendProcurementPortalValidationRequest = {
            "procurement_portal_preference_arn": procurement_portal_preference_arn
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

    async def tag_resource(
        self,
        resource_arn: "capo_invoicing.types.tagris_arn.TagrisArn",
        resource_tags: "capo_invoicing.types.resource_tag_list.ResourceTagList",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
    ) -> "capo_invoicing.types.tag_resource_response.TagResourceResponse":
        """<p>Adds a tag to a resource. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the tags. </p>
            resource_tags: <p> Adds a tag to a resource. </p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found. </p>
            capo_invoicing.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            TagResource

            >>> await client.tag_resource(resource_arn='arn:aws:invoicing::000000000000:invoice-unit/12345678', resource_tags=[{'Key': 'TagKey', 'Value': 'TagValue'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_invoicing._operations.invoicing.tag_resource

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "resource_tags": resource_tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_invoicing.types.tagris_arn.TagrisArn",
        resource_tag_keys: "capo_invoicing.types.resource_tag_key_list.ResourceTagKeyList",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
    ) -> "capo_invoicing.types.untag_resource_response.UntagResourceResponse":
        """<p> Removes a tag from a resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) to untag. </p>
            resource_tag_keys: <p> Keys for the tags to be removed. </p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UntagResource

            >>> await client.untag_resource(resource_arn='arn:aws:invoicing::000000000000:invoice-unit/12345678', resource_tag_keys=['TagKey'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_invoicing._operations.invoicing.untag_resource

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "resource_tag_keys": resource_tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_invoice_unit(
        self,
        invoice_unit_arn: "capo_invoicing.types.invoice_unit_arn_string.InvoiceUnitArnString",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        description: Optional[
            "capo_invoicing.types.description_string.DescriptionString"
        ] = None,
        tax_inheritance_disabled: Optional[
            "capo_invoicing.types.tax_inheritance_disabled_flag.TaxInheritanceDisabledFlag"
        ] = None,
        rule: Optional["capo_invoicing.types.invoice_unit_rule.InvoiceUnitRule"] = None,
        client_token: Optional[
            "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
        ] = None,
    ) -> "capo_invoicing.types.update_invoice_unit_response.UpdateInvoiceUnitResponse":
        """<p>You can update the invoice unit configuration at any time, and Amazon Web Services will use the latest configuration at the end of the month.</p>

        Args:
            invoice_unit_arn: <p>The ARN to identify an invoice unit. This information can't be modified or deleted. </p>
            description: <p>The assigned description for an invoice unit. This information can't be modified or deleted. </p>
            tax_inheritance_disabled: <p>Whether the invoice unit based tax inheritance is/ should be enabled or disabled. </p>
            rule: <p>The <code>InvoiceUnitRule</code> object used to update invoice units. </p>
            client_token: <p> A unique, case-sensitive identifier that you provide to ensure idempotency of the request. </p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UpdateInvoiceUnit with all updatable fields

            >>> await client.update_invoice_unit(invoice_unit_arn='arn:aws:invoicing::000000000000:invoice-unit/12345678', description='Updated IU description', tax_inheritance_disabled=False, rule={'LinkedAccounts': ['111111111111', '222222222222']}, client_token='e362c68e-4e74-48d7-9228-0bc5aa447b42')
            UpdateInvoiceUnit with specific fields

            >>> await client.update_invoice_unit(invoice_unit_arn='arn:aws:invoicing::000000000000:invoice-unit/12345678', description='Updated IU description. All other fields remain unchanged', client_token='e362c68e-4e74-48d7-9228-0bc5aa447b43')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.update_invoice_unit_request.UpdateInvoiceUnitRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.update_invoice_unit_response.UpdateInvoiceUnitResponse"
        ]:
            import capo_invoicing._operations.invoicing.update_invoice_unit

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.update_invoice_unit.async_update_invoice_unit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.update_invoice_unit_request.UpdateInvoiceUnitRequest = {
            "invoice_unit_arn": invoice_unit_arn
        }
        if description is not None:
            input_["description"] = description
        if tax_inheritance_disabled is not None:
            input_["tax_inheritance_disabled"] = tax_inheritance_disabled
        if rule is not None:
            input_["rule"] = rule
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

    async def update_procurement_portal_preference_status(
        self,
        procurement_portal_preference_arn: "capo_invoicing.types.procurement_portal_preference_arn_string.ProcurementPortalPreferenceArnString",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        einvoice_delivery_preference_status: Optional[
            "capo_invoicing.types.procurement_portal_preference_status.ProcurementPortalPreferenceStatus"
        ] = None,
        einvoice_delivery_preference_status_reason: Optional[
            "capo_invoicing.types.basic_string.BasicString"
        ] = None,
        purchase_order_retrieval_preference_status: Optional[
            "capo_invoicing.types.procurement_portal_preference_status.ProcurementPortalPreferenceStatus"
        ] = None,
        purchase_order_retrieval_preference_status_reason: Optional[
            "capo_invoicing.types.basic_string.BasicString"
        ] = None,
        client_token: Optional[
            "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
        ] = None,
    ) -> "capo_invoicing.types.update_procurement_portal_preference_status_response.UpdateProcurementPortalPreferenceStatusResponse":
        """<p> <i> <b>This feature API is subject to changing at any time. For more information, see the <a href="https://aws.amazon.com/service-terms/">Amazon Web Services Service Terms</a> (Betas and Previews).</b> </i> </p> <p>Updates the status of a procurement portal preference, including the activation state of e-invoice delivery and purchase order retrieval features.</p>

        Args:
            procurement_portal_preference_arn: <p>The Amazon Resource Name (ARN) of the procurement portal preference to update.</p>
            einvoice_delivery_preference_status: <p>The updated status of the e-invoice delivery preference.</p>
            einvoice_delivery_preference_status_reason: <p>The reason for the e-invoice delivery preference status update, providing context for the change.</p>
            purchase_order_retrieval_preference_status: <p>The updated status of the purchase order retrieval preference.</p>
            purchase_order_retrieval_preference_status_reason: <p>The reason for the purchase order retrieval preference status update, providing context for the change.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure idempotency of the request.</p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This exception occurs when a concurrent modification is detected during an update operation, or when attempting to create a resource that already exists.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found. </p>
            capo_invoicing.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UpdateProcurementPortalPreference for EinvoiceDeliveryPreferenceStatus and PurchaseOrderRetrievalPreferenceStatus

            >>> await client.update_procurement_portal_preference_status(procurement_portal_preference_arn='arn:aws:invoicing::111111111111:procurement-portal-preference/f71dd02e-f855-4b13-b793-0fd25c0b3ecd', einvoice_delivery_preference_status='SUSPENDED', einvoice_delivery_preference_status_reason='suspended example reason', purchase_order_retrieval_preference_status='SUSPENDED', purchase_order_retrieval_preference_status_reason='suspended example reason', client_token='e362c68e-4e74-48d7-9228-0bc5aa447b46')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.update_procurement_portal_preference_status_request.UpdateProcurementPortalPreferenceStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.update_procurement_portal_preference_status_response.UpdateProcurementPortalPreferenceStatusResponse"
        ]:
            import capo_invoicing._operations.invoicing.update_procurement_portal_preference_status

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.update_procurement_portal_preference_status.async_update_procurement_portal_preference_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.update_procurement_portal_preference_status_request.UpdateProcurementPortalPreferenceStatusRequest = {
            "procurement_portal_preference_arn": procurement_portal_preference_arn
        }
        if einvoice_delivery_preference_status is not None:
            input_["einvoice_delivery_preference_status"] = (
                einvoice_delivery_preference_status
            )
        if einvoice_delivery_preference_status_reason is not None:
            input_["einvoice_delivery_preference_status_reason"] = (
                einvoice_delivery_preference_status_reason
            )
        if purchase_order_retrieval_preference_status is not None:
            input_["purchase_order_retrieval_preference_status"] = (
                purchase_order_retrieval_preference_status
            )
        if purchase_order_retrieval_preference_status_reason is not None:
            input_["purchase_order_retrieval_preference_status_reason"] = (
                purchase_order_retrieval_preference_status_reason
            )
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

    async def verify_procurement_portal_validation(
        self,
        procurement_portal_preference_arn: "capo_invoicing.types.procurement_portal_preference_arn_string.ProcurementPortalPreferenceArnString",
        code: "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace",
        *,
        config_overrides: Optional[AsyncInvoicingClientConfig] = None,
        client_token: Optional[
            "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
        ] = None,
    ) -> "capo_invoicing.types.verify_procurement_portal_validation_response.VerifyProcurementPortalValidationResponse":
        """<p> <i> <b>This feature API is subject to changing at any time. For more information, see the <a href="https://aws.amazon.com/service-terms/">Amazon Web Services Service Terms</a> (Betas and Previews).</b> </i> </p> <p>Submits a validation code to complete the validation of a procurement portal preference. Use this operation after calling <code>SendProcurementPortalValidation</code> to confirm ownership and connectivity of the configured procurement portal endpoint.</p>

        Args:
            procurement_portal_preference_arn: <p>The Amazon Resource Name (ARN) of the procurement portal preference to validate.</p>
            code: <p>The validation code received from the procurement portal in response to a previous <code>SendProcurementPortalValidation</code> request.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure idempotency of the request.</p>

        Raises:
            capo_invoicing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_invoicing.errors.internal_server_exception.InternalServerException: <p>The processing request failed because of an unknown error, exception, or failure. </p>
            capo_invoicing.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found. </p>
            capo_invoicing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_invoicing.errors.validation_exception.ValidationException: <p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_invoicing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            VerifyProcurementPortalValidation call

            >>> await client.verify_procurement_portal_validation(procurement_portal_preference_arn='arn:aws:invoicing::111111111111:procurement-portal-preference/f71dd02e-f855-4b13-b793-0fd25c0b3ecd', code='validation-code-123')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_invoicing.types.verify_procurement_portal_validation_request.VerifyProcurementPortalValidationRequest]",
        ) -> AsyncOperationResponse[
            "capo_invoicing.types.verify_procurement_portal_validation_response.VerifyProcurementPortalValidationResponse"
        ]:
            import capo_invoicing._operations.invoicing.verify_procurement_portal_validation

            (
                output,
                http_response,
            ) = await capo_invoicing._operations.invoicing.verify_procurement_portal_validation.async_verify_procurement_portal_validation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_invoicing.types.verify_procurement_portal_validation_request.VerifyProcurementPortalValidationRequest = {
            "procurement_portal_preference_arn": procurement_portal_preference_arn,
            "code": code,
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
