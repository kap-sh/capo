"""Generated from Smithy shape ``com.amazonaws.route53domains#Route53Domains_v20140515``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_route_53_domains._auth._signers
import capo_route_53_domains._auth._sigv4
from capo_route_53_domains._auth._identity import Credentials
from capo_route_53_domains._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_route_53_domains._auth._zapros_handler import AuthMiddleware
from capo_route_53_domains._pagination import resolve_path as _resolve_path
from capo_route_53_domains._services._aws_config import aaws_config
from capo_route_53_domains._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_route_53_domains.types.accept_domain_transfer_from_another_aws_account_request
    import capo_route_53_domains.types.accept_domain_transfer_from_another_aws_account_response
    import capo_route_53_domains.types.account_id
    import capo_route_53_domains.types.associate_delegation_signer_to_domain_request
    import capo_route_53_domains.types.associate_delegation_signer_to_domain_response
    import capo_route_53_domains.types.billing_record
    import capo_route_53_domains.types.boolean
    import capo_route_53_domains.types.cancel_domain_transfer_to_another_aws_account_request
    import capo_route_53_domains.types.cancel_domain_transfer_to_another_aws_account_response
    import capo_route_53_domains.types.check_domain_availability_request
    import capo_route_53_domains.types.check_domain_availability_response
    import capo_route_53_domains.types.check_domain_transferability_request
    import capo_route_53_domains.types.check_domain_transferability_response
    import capo_route_53_domains.types.consent
    import capo_route_53_domains.types.contact_detail
    import capo_route_53_domains.types.current_expiry_year
    import capo_route_53_domains.types.delete_domain_request
    import capo_route_53_domains.types.delete_domain_response
    import capo_route_53_domains.types.delete_tags_for_domain_request
    import capo_route_53_domains.types.delete_tags_for_domain_response
    import capo_route_53_domains.types.disable_domain_auto_renew_request
    import capo_route_53_domains.types.disable_domain_auto_renew_response
    import capo_route_53_domains.types.disable_domain_transfer_lock_request
    import capo_route_53_domains.types.disable_domain_transfer_lock_response
    import capo_route_53_domains.types.disassociate_delegation_signer_from_domain_request
    import capo_route_53_domains.types.disassociate_delegation_signer_from_domain_response
    import capo_route_53_domains.types.dnssec_signing_attributes
    import capo_route_53_domains.types.domain_auth_code
    import capo_route_53_domains.types.domain_name
    import capo_route_53_domains.types.domain_price
    import capo_route_53_domains.types.domain_summary
    import capo_route_53_domains.types.duration_in_years
    import capo_route_53_domains.types.enable_domain_auto_renew_request
    import capo_route_53_domains.types.enable_domain_auto_renew_response
    import capo_route_53_domains.types.enable_domain_transfer_lock_request
    import capo_route_53_domains.types.enable_domain_transfer_lock_response
    import capo_route_53_domains.types.fi_auth_key
    import capo_route_53_domains.types.filter_conditions
    import capo_route_53_domains.types.get_contact_reachability_status_request
    import capo_route_53_domains.types.get_contact_reachability_status_response
    import capo_route_53_domains.types.get_domain_detail_request
    import capo_route_53_domains.types.get_domain_detail_response
    import capo_route_53_domains.types.get_domain_suggestions_request
    import capo_route_53_domains.types.get_domain_suggestions_response
    import capo_route_53_domains.types.get_operation_detail_request
    import capo_route_53_domains.types.get_operation_detail_response
    import capo_route_53_domains.types.integer
    import capo_route_53_domains.types.label
    import capo_route_53_domains.types.lang_code
    import capo_route_53_domains.types.list_domains_request
    import capo_route_53_domains.types.list_domains_response
    import capo_route_53_domains.types.list_operations_request
    import capo_route_53_domains.types.list_operations_response
    import capo_route_53_domains.types.list_operations_sort_attribute_name
    import capo_route_53_domains.types.list_prices_page_max_items
    import capo_route_53_domains.types.list_prices_request
    import capo_route_53_domains.types.list_prices_response
    import capo_route_53_domains.types.list_tags_for_domain_request
    import capo_route_53_domains.types.list_tags_for_domain_response
    import capo_route_53_domains.types.nameserver_list
    import capo_route_53_domains.types.operation_id
    import capo_route_53_domains.types.operation_status_list
    import capo_route_53_domains.types.operation_summary
    import capo_route_53_domains.types.operation_type_list
    import capo_route_53_domains.types.page_marker
    import capo_route_53_domains.types.page_max_items
    import capo_route_53_domains.types.password
    import capo_route_53_domains.types.push_domain_request
    import capo_route_53_domains.types.register_domain_request
    import capo_route_53_domains.types.register_domain_response
    import capo_route_53_domains.types.reject_domain_transfer_from_another_aws_account_request
    import capo_route_53_domains.types.reject_domain_transfer_from_another_aws_account_response
    import capo_route_53_domains.types.renew_domain_request
    import capo_route_53_domains.types.renew_domain_response
    import capo_route_53_domains.types.resend_contact_reachability_email_request
    import capo_route_53_domains.types.resend_contact_reachability_email_response
    import capo_route_53_domains.types.resend_operation_authorization_request
    import capo_route_53_domains.types.retrieve_domain_auth_code_request
    import capo_route_53_domains.types.retrieve_domain_auth_code_response
    import capo_route_53_domains.types.sort_condition
    import capo_route_53_domains.types.sort_order
    import capo_route_53_domains.types.string
    import capo_route_53_domains.types.tag_key_list
    import capo_route_53_domains.types.tag_list
    import capo_route_53_domains.types.timestamp
    import capo_route_53_domains.types.tld_name
    import capo_route_53_domains.types.transfer_domain_request
    import capo_route_53_domains.types.transfer_domain_response
    import capo_route_53_domains.types.transfer_domain_to_another_aws_account_request
    import capo_route_53_domains.types.transfer_domain_to_another_aws_account_response
    import capo_route_53_domains.types.update_domain_contact_privacy_request
    import capo_route_53_domains.types.update_domain_contact_privacy_response
    import capo_route_53_domains.types.update_domain_contact_request
    import capo_route_53_domains.types.update_domain_contact_response
    import capo_route_53_domains.types.update_domain_nameservers_request
    import capo_route_53_domains.types.update_domain_nameservers_response
    import capo_route_53_domains.types.update_tags_for_domain_request
    import capo_route_53_domains.types.update_tags_for_domain_response
    import capo_route_53_domains.types.view_billing_request
    import capo_route_53_domains.types.view_billing_response


class AsyncRoute53DomainsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncRoute53DomainsClient:
    """A client for the ``Route53Domains`` service.

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
        self._config = AsyncRoute53DomainsClientConfig(
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
        self, config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncRoute53DomainsClientConfig = config_overrides or {}
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

    async def accept_domain_transfer_from_another_aws_account(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        password: "capo_route_53_domains.types.password.Password",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> "capo_route_53_domains.types.accept_domain_transfer_from_another_aws_account_response.AcceptDomainTransferFromAnotherAwsAccountResponse":
        """<p>Accepts the transfer of a domain from another Amazon Web Services account to the currentAmazon Web Services account. You initiate a transfer between Amazon Web Services accounts using <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomainToAnotherAwsAccount.html">TransferDomainToAnotherAwsAccount</a>.</p> <p>If you use the CLI command at <a href="https://docs.aws.amazon.com/cli/latest/reference/route53domains/accept-domain-transfer-from-another-aws-account.html">accept-domain-transfer-from-another-aws-account</a>, use JSON format as input instead of text because otherwise CLI will throw an error from domain transfer input that includes single quotes.</p> <p>Use either <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListOperations.html">ListOperations</a> or <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html">GetOperationDetail</a> to determine whether the operation succeeded. <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html">GetOperationDetail</a> provides additional information, for example, <code>Domain Transfer from Aws Account 111122223333 has been cancelled</code>. </p>

        Args:
            domain_name: <p>The name of the domain that was specified when another Amazon Web Services account submitted a <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomainToAnotherAwsAccount.html">TransferDomainToAnotherAwsAccount</a> request. </p>
            password: <p>The password that was returned by the <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomainToAnotherAwsAccount.html">TransferDomainToAnotherAwsAccount</a> request. </p>

        Raises:
            capo_route_53_domains.errors.domain_limit_exceeded.DomainLimitExceeded: <p>The number of domains has exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.accept_domain_transfer_from_another_aws_account_request.AcceptDomainTransferFromAnotherAwsAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.accept_domain_transfer_from_another_aws_account_response.AcceptDomainTransferFromAnotherAwsAccountResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.accept_domain_transfer_from_another_aws_account

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.accept_domain_transfer_from_another_aws_account.async_accept_domain_transfer_from_another_aws_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.accept_domain_transfer_from_another_aws_account_request.AcceptDomainTransferFromAnotherAwsAccountRequest = {
            "domain_name": domain_name,
            "password": password,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_delegation_signer_to_domain(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        signing_attributes: "capo_route_53_domains.types.dnssec_signing_attributes.DnssecSigningAttributes",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> "capo_route_53_domains.types.associate_delegation_signer_to_domain_response.AssociateDelegationSignerToDomainResponse":
        """<p> Creates a delegation signer (DS) record in the registry zone for this domain name.</p> <p>Note that creating DS record at the registry impacts DNSSEC validation of your DNS records. This action may render your domain name unavailable on the internet if the steps are completed in the wrong order, or with incorrect timing. For more information about DNSSEC signing, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec.html">Configuring DNSSEC signing</a> in the <i>Route 53 developer guide</i>.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
            signing_attributes: <p>The information about a key, including the algorithm, public key-value, and flags.</p>

        Raises:
            capo_route_53_domains.errors.dnssec_limit_exceeded.DnssecLimitExceeded: <p> This error is returned if you call <code>AssociateDelegationSignerToDomain</code> when the specified domain has reached the maximum number of DS records. You can't add any additional DS records unless you delete an existing one first. </p>
            capo_route_53_domains.errors.duplicate_request.DuplicateRequest: <p>The request is already in progress for the domain.</p>
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.tld_rules_violation.TLDRulesViolation: <p>The top-level domain does not support this operation.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.associate_delegation_signer_to_domain_request.AssociateDelegationSignerToDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.associate_delegation_signer_to_domain_response.AssociateDelegationSignerToDomainResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.associate_delegation_signer_to_domain

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.associate_delegation_signer_to_domain.async_associate_delegation_signer_to_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.associate_delegation_signer_to_domain_request.AssociateDelegationSignerToDomainRequest = {
            "domain_name": domain_name,
            "signing_attributes": signing_attributes,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_domain_transfer_to_another_aws_account(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> "capo_route_53_domains.types.cancel_domain_transfer_to_another_aws_account_response.CancelDomainTransferToAnotherAwsAccountResponse":
        """<p>Cancels the transfer of a domain from the current Amazon Web Services account to another Amazon Web Services account. You initiate a transfer betweenAmazon Web Services accounts using <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomainToAnotherAwsAccount.html">TransferDomainToAnotherAwsAccount</a>. </p> <important> <p>You must cancel the transfer before the other Amazon Web Services account accepts the transfer using <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AcceptDomainTransferFromAnotherAwsAccount.html">AcceptDomainTransferFromAnotherAwsAccount</a>.</p> </important> <p>Use either <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListOperations.html">ListOperations</a> or <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html">GetOperationDetail</a> to determine whether the operation succeeded. <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html">GetOperationDetail</a> provides additional information, for example, <code>Domain Transfer from Aws Account 111122223333 has been cancelled</code>. </p>

        Args:
            domain_name: <p>The name of the domain for which you want to cancel the transfer to another Amazon Web Services account.</p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.cancel_domain_transfer_to_another_aws_account_request.CancelDomainTransferToAnotherAwsAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.cancel_domain_transfer_to_another_aws_account_response.CancelDomainTransferToAnotherAwsAccountResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.cancel_domain_transfer_to_another_aws_account

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.cancel_domain_transfer_to_another_aws_account.async_cancel_domain_transfer_to_another_aws_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.cancel_domain_transfer_to_another_aws_account_request.CancelDomainTransferToAnotherAwsAccountRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def check_domain_availability(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        idn_lang_code: Optional[
            "capo_route_53_domains.types.lang_code.LangCode"
        ] = None,
    ) -> "capo_route_53_domains.types.check_domain_availability_response.CheckDomainAvailabilityResponse":
        """<p>This operation checks the availability of one domain name. Note that if the availability status of a domain is pending, you must submit another request to determine the availability of the domain name.</p>

        Args:
            domain_name: <p>The name of the domain that you want to get availability for. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html">Domains that You Can Register with Amazon Route 53</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>The domain name can contain only the following characters:</p> <ul> <li> <p>Letters a through z. Domain names are not case sensitive.</p> </li> <li> <p>Numbers 0 through 9.</p> </li> <li> <p>Hyphen (-). You can't specify a hyphen at the beginning or end of a label. </p> </li> <li> <p>Period (.) to separate the labels in the name, such as the <code>.</code> in <code>example.com</code>.</p> </li> </ul> <p>Internationalized domain names are not supported for some top-level domains. To determine whether the TLD that you want to use supports internationalized domain names, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html">Domains that You Can Register with Amazon Route 53</a>. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html#domain-name-format-idns">Formatting Internationalized Domain Names</a>. </p>
            idn_lang_code: <p>Reserved for future use.</p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.tld_in_maintenance.TLDInMaintenance: <p>The top-level domain is currently undergoing maintenance and the request cannot be processed. Try again later.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.check_domain_availability_request.CheckDomainAvailabilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.check_domain_availability_response.CheckDomainAvailabilityResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.check_domain_availability

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.check_domain_availability.async_check_domain_availability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.check_domain_availability_request.CheckDomainAvailabilityRequest = {
            "domain_name": domain_name
        }
        if idn_lang_code is not None:
            input_["idn_lang_code"] = idn_lang_code

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def check_domain_transferability(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        auth_code: Optional[
            "capo_route_53_domains.types.domain_auth_code.DomainAuthCode"
        ] = None,
    ) -> "capo_route_53_domains.types.check_domain_transferability_response.CheckDomainTransferabilityResponse":
        """<p>Checks whether a domain name can be transferred to Amazon Route 53. </p>

        Args:
            domain_name: <p>The name of the domain that you want to transfer to Route 53. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html">Domains that You Can Register with Amazon Route 53</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>The domain name can contain only the following characters:</p> <ul> <li> <p>Letters a through z. Domain names are not case sensitive.</p> </li> <li> <p>Numbers 0 through 9.</p> </li> <li> <p>Hyphen (-). You can't specify a hyphen at the beginning or end of a label. </p> </li> <li> <p>Period (.) to separate the labels in the name, such as the <code>.</code> in <code>example.com</code>.</p> </li> </ul>
            auth_code: <p>If the registrar for the top-level domain (TLD) requires an authorization code to transfer the domain, the code that you got from the current registrar for the domain.</p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.tld_in_maintenance.TLDInMaintenance: <p>The top-level domain is currently undergoing maintenance and the request cannot be processed. Try again later.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.check_domain_transferability_request.CheckDomainTransferabilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.check_domain_transferability_response.CheckDomainTransferabilityResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.check_domain_transferability

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.check_domain_transferability.async_check_domain_transferability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.check_domain_transferability_request.CheckDomainTransferabilityRequest = {
            "domain_name": domain_name
        }
        if auth_code is not None:
            input_["auth_code"] = auth_code

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_domain(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> "capo_route_53_domains.types.delete_domain_response.DeleteDomainResponse":
        """<p>This operation deletes the specified domain. This action is permanent. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-delete.html">Deleting a domain name registration</a>.</p> <p>To transfer the domain registration to another registrar, use the transfer process that’s provided by the registrar to which you want to transfer the registration. Otherwise, the following apply:</p> <ol> <li> <p>You can’t get a refund for the cost of a deleted domain registration.</p> </li> <li> <p>The registry for the top-level domain might hold the domain name for a brief time before releasing it for other users to register (varies by registry). </p> </li> <li> <p>When the registration has been deleted, we'll send you a confirmation to the registrant contact. The email will come from <code>noreply@domainnameverification.net</code> or <code>noreply@emailverification.info</code> or <code>noreply@registrar.amazon</code>.</p> </li> </ol>

        Args:
            domain_name: <p>Name of the domain to be deleted.</p>

        Raises:
            capo_route_53_domains.errors.duplicate_request.DuplicateRequest: <p>The request is already in progress for the domain.</p>
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.tld_rules_violation.TLDRulesViolation: <p>The top-level domain does not support this operation.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.delete_domain_request.DeleteDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.delete_domain_response.DeleteDomainResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.delete_domain

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.delete_domain.async_delete_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.delete_domain_request.DeleteDomainRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_tags_for_domain(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        tags_to_delete: "capo_route_53_domains.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> "capo_route_53_domains.types.delete_tags_for_domain_response.DeleteTagsForDomainResponse":
        """<p>This operation deletes the specified tags for a domain.</p> <p>All tag operations are eventually consistent; subsequent operations might not immediately represent all issued operations.</p>

        Args:
            domain_name: <p>The domain for which you want to delete one or more tags.</p>
            tags_to_delete: <p>A list of tag keys to delete.</p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.delete_tags_for_domain_request.DeleteTagsForDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.delete_tags_for_domain_response.DeleteTagsForDomainResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.delete_tags_for_domain

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.delete_tags_for_domain.async_delete_tags_for_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.delete_tags_for_domain_request.DeleteTagsForDomainRequest = {
            "domain_name": domain_name,
            "tags_to_delete": tags_to_delete,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_domain_auto_renew(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> "capo_route_53_domains.types.disable_domain_auto_renew_response.DisableDomainAutoRenewResponse":
        """<p>This operation disables automatic renewal of domain registration for the specified domain.</p>

        Args:
            domain_name: <p>The name of the domain that you want to disable automatic renewal for.</p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.disable_domain_auto_renew_request.DisableDomainAutoRenewRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.disable_domain_auto_renew_response.DisableDomainAutoRenewResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.disable_domain_auto_renew

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.disable_domain_auto_renew.async_disable_domain_auto_renew(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.disable_domain_auto_renew_request.DisableDomainAutoRenewRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_domain_transfer_lock(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> "capo_route_53_domains.types.disable_domain_transfer_lock_response.DisableDomainTransferLockResponse":
        """<p>This operation removes the transfer lock on the domain (specifically the <code>clientTransferProhibited</code> status) to allow domain transfers. We recommend you refrain from performing this action unless you intend to transfer the domain to a different registrar. Successful submission returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant will be notified by email.</p>

        Args:
            domain_name: <p>The name of the domain that you want to remove the transfer lock for.</p>

        Raises:
            capo_route_53_domains.errors.duplicate_request.DuplicateRequest: <p>The request is already in progress for the domain.</p>
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.tld_rules_violation.TLDRulesViolation: <p>The top-level domain does not support this operation.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.disable_domain_transfer_lock_request.DisableDomainTransferLockRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.disable_domain_transfer_lock_response.DisableDomainTransferLockResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.disable_domain_transfer_lock

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.disable_domain_transfer_lock.async_disable_domain_transfer_lock(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.disable_domain_transfer_lock_request.DisableDomainTransferLockRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_delegation_signer_from_domain(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        id: "capo_route_53_domains.types.string.String",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> "capo_route_53_domains.types.disassociate_delegation_signer_from_domain_response.DisassociateDelegationSignerFromDomainResponse":
        """<p>Deletes a delegation signer (DS) record in the registry zone for this domain name.</p>

        Args:
            domain_name: <p>Name of the domain.</p>
            id: <p>An internal identification number assigned to each DS record after it’s created. You can retrieve it as part of DNSSEC information returned by <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetDomainDetail.html">GetDomainDetail</a>.</p>

        Raises:
            capo_route_53_domains.errors.duplicate_request.DuplicateRequest: <p>The request is already in progress for the domain.</p>
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.tld_rules_violation.TLDRulesViolation: <p>The top-level domain does not support this operation.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.disassociate_delegation_signer_from_domain_request.DisassociateDelegationSignerFromDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.disassociate_delegation_signer_from_domain_response.DisassociateDelegationSignerFromDomainResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.disassociate_delegation_signer_from_domain

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.disassociate_delegation_signer_from_domain.async_disassociate_delegation_signer_from_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.disassociate_delegation_signer_from_domain_request.DisassociateDelegationSignerFromDomainRequest = {
            "domain_name": domain_name,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_domain_auto_renew(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> "capo_route_53_domains.types.enable_domain_auto_renew_response.EnableDomainAutoRenewResponse":
        """<p>This operation configures Amazon Route 53 to automatically renew the specified domain before the domain registration expires. The cost of renewing your domain registration is billed to your Amazon Web Services account.</p> <p>The period during which you can renew a domain name varies by TLD. For a list of TLDs and their renewal policies, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html">Domains That You Can Register with Amazon Route 53</a> in the <i>Amazon Route 53 Developer Guide</i>. Route 53 requires that you renew before the end of the renewal period so we can complete processing before the deadline.</p>

        Args:
            domain_name: <p>The name of the domain that you want to enable automatic renewal for.</p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.tld_rules_violation.TLDRulesViolation: <p>The top-level domain does not support this operation.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.enable_domain_auto_renew_request.EnableDomainAutoRenewRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.enable_domain_auto_renew_response.EnableDomainAutoRenewResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.enable_domain_auto_renew

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.enable_domain_auto_renew.async_enable_domain_auto_renew(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.enable_domain_auto_renew_request.EnableDomainAutoRenewRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_domain_transfer_lock(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> "capo_route_53_domains.types.enable_domain_transfer_lock_response.EnableDomainTransferLockResponse":
        """<p>This operation sets the transfer lock on the domain (specifically the <code>clientTransferProhibited</code> status) to prevent domain transfers. Successful submission returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant will be notified by email.</p>

        Args:
            domain_name: <p>The name of the domain that you want to set the transfer lock for.</p>

        Raises:
            capo_route_53_domains.errors.duplicate_request.DuplicateRequest: <p>The request is already in progress for the domain.</p>
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.tld_rules_violation.TLDRulesViolation: <p>The top-level domain does not support this operation.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.enable_domain_transfer_lock_request.EnableDomainTransferLockRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.enable_domain_transfer_lock_response.EnableDomainTransferLockResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.enable_domain_transfer_lock

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.enable_domain_transfer_lock.async_enable_domain_transfer_lock(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.enable_domain_transfer_lock_request.EnableDomainTransferLockRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_contact_reachability_status(
        self,
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        domain_name: Optional[
            "capo_route_53_domains.types.domain_name.DomainName"
        ] = None,
    ) -> "capo_route_53_domains.types.get_contact_reachability_status_response.GetContactReachabilityStatusResponse":
        """<p>For operations that require confirmation that the email address for the registrant contact is valid, such as registering a new domain, this operation returns information about whether the registrant contact has responded.</p> <p>If you want us to resend the email, use the <code>ResendContactReachabilityEmail</code> operation.</p>

        Args:
            domain_name: <p>The name of the domain for which you want to know whether the registrant contact has confirmed that the email address is valid.</p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.get_contact_reachability_status_request.GetContactReachabilityStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.get_contact_reachability_status_response.GetContactReachabilityStatusResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.get_contact_reachability_status

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.get_contact_reachability_status.async_get_contact_reachability_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.get_contact_reachability_status_request.GetContactReachabilityStatusRequest = {}
        if domain_name is not None:
            input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_domain_detail(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> (
        "capo_route_53_domains.types.get_domain_detail_response.GetDomainDetailResponse"
    ):
        """<p>This operation returns detailed information about a specified domain that is associated with the current Amazon Web Services account. Contact information for the domain is also returned as part of the output.</p>

        Args:
            domain_name: <p>The name of the domain that you want to get detailed information about.</p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.get_domain_detail_request.GetDomainDetailRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.get_domain_detail_response.GetDomainDetailResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.get_domain_detail

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.get_domain_detail.async_get_domain_detail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.get_domain_detail_request.GetDomainDetailRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_domain_suggestions(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        suggestion_count: "capo_route_53_domains.types.integer.Integer",
        only_available: "capo_route_53_domains.types.boolean.Boolean",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> "capo_route_53_domains.types.get_domain_suggestions_response.GetDomainSuggestionsResponse":
        """<p>The GetDomainSuggestions operation returns a list of suggested domain names.</p>

        Args:
            domain_name: <p>A domain name that you want to use as the basis for a list of possible domain names. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html">Domains that You Can Register with Amazon Route 53</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>The domain name can contain only the following characters:</p> <ul> <li> <p>Letters a through z. Domain names are not case sensitive.</p> </li> <li> <p>Numbers 0 through 9.</p> </li> <li> <p>Hyphen (-). You can't specify a hyphen at the beginning or end of a label. </p> </li> <li> <p>Period (.) to separate the labels in the name, such as the <code>.</code> in <code>example.com</code>.</p> </li> </ul> <p>Internationalized domain names are not supported for some top-level domains. To determine whether the TLD that you want to use supports internationalized domain names, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html">Domains that You Can Register with Amazon Route 53</a>. </p>
            suggestion_count: <p>The number of suggested domain names that you want Route 53 to return. Specify a value between 1 and 50. Note that fewer than the requested number might be returned.</p>
            only_available: <p>If <code>OnlyAvailable</code> is <code>true</code>, Route 53 returns only domain names that are available. If <code>OnlyAvailable</code> is <code>false</code>, Route 53 returns domain names without checking whether they're available to be registered. To determine whether the domain is available, you can call <code>checkDomainAvailability</code> for each suggestion.</p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.tld_in_maintenance.TLDInMaintenance: <p>The top-level domain is currently undergoing maintenance and the request cannot be processed. Try again later.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.get_domain_suggestions_request.GetDomainSuggestionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.get_domain_suggestions_response.GetDomainSuggestionsResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.get_domain_suggestions

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.get_domain_suggestions.async_get_domain_suggestions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.get_domain_suggestions_request.GetDomainSuggestionsRequest = {
            "domain_name": domain_name,
            "suggestion_count": suggestion_count,
            "only_available": only_available,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_operation_detail(
        self,
        operation_id: "capo_route_53_domains.types.operation_id.OperationId",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> "capo_route_53_domains.types.get_operation_detail_response.GetOperationDetailResponse":
        """<p>This operation returns the current status of an operation that is not completed.</p>

        Args:
            operation_id: <p>The identifier for the operation for which you want to get the status. Route 53 returned the identifier in the response to the original request.</p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.get_operation_detail_request.GetOperationDetailRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.get_operation_detail_response.GetOperationDetailResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.get_operation_detail

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.get_operation_detail.async_get_operation_detail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.get_operation_detail_request.GetOperationDetailRequest = {
            "operation_id": operation_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_domains(
        self,
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        filter_conditions: Optional[
            "capo_route_53_domains.types.filter_conditions.FilterConditions"
        ] = None,
        sort_condition: Optional[
            "capo_route_53_domains.types.sort_condition.SortCondition"
        ] = None,
        marker: Optional["capo_route_53_domains.types.page_marker.PageMarker"] = None,
        max_items: Optional[
            "capo_route_53_domains.types.page_max_items.PageMaxItems"
        ] = None,
    ) -> "capo_route_53_domains.types.list_domains_response.ListDomainsResponse":
        """<p>This operation returns all the domain names registered with Amazon Route 53 for the current Amazon Web Services account if no filtering conditions are used.</p>

        Args:
            filter_conditions: <p>A complex type that contains information about the filters applied during the <code>ListDomains</code> request. The filter conditions can include domain name and domain expiration.</p>
            sort_condition: <p>A complex type that contains information about the requested ordering of domains in the returned list.</p>
            marker: <p>For an initial request for a list of domains, omit this element. If the number of domains that are associated with the current Amazon Web Services account is greater than the value that you specified for <code>MaxItems</code>, you can use <code>Marker</code> to return additional domains. Get the value of <code>NextPageMarker</code> from the previous response, and submit another request that includes the value of <code>NextPageMarker</code> in the <code>Marker</code> element.</p> <p>Constraints: The marker must match the value specified in the previous request.</p>
            max_items: <p>Number of domains to be returned.</p> <p>Default: 20</p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.list_domains_request.ListDomainsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.list_domains_response.ListDomainsResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.list_domains

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.list_domains.async_list_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.list_domains_request.ListDomainsRequest = {}
        if filter_conditions is not None:
            input_["filter_conditions"] = filter_conditions
        if sort_condition is not None:
            input_["sort_condition"] = sort_condition
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_domains(
        self,
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        filter_conditions: Optional[
            "capo_route_53_domains.types.filter_conditions.FilterConditions"
        ] = None,
        sort_condition: Optional[
            "capo_route_53_domains.types.sort_condition.SortCondition"
        ] = None,
        marker: Optional["capo_route_53_domains.types.page_marker.PageMarker"] = None,
        max_items: Optional[
            "capo_route_53_domains.types.page_max_items.PageMaxItems"
        ] = None,
    ) -> "AsyncIterator[capo_route_53_domains.types.domain_summary.DomainSummary]":
        _token = marker
        while True:
            _response = await self.list_domains(
                config_overrides=config_overrides,
                filter_conditions=filter_conditions,
                sort_condition=sort_condition,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("domains",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_marker",))
            if not _token:
                break

    async def list_operations(
        self,
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        submitted_since: Optional[
            "capo_route_53_domains.types.timestamp.Timestamp"
        ] = None,
        marker: Optional["capo_route_53_domains.types.page_marker.PageMarker"] = None,
        max_items: Optional[
            "capo_route_53_domains.types.page_max_items.PageMaxItems"
        ] = None,
        status: Optional[
            "capo_route_53_domains.types.operation_status_list.OperationStatusList"
        ] = None,
        type: Optional[
            "capo_route_53_domains.types.operation_type_list.OperationTypeList"
        ] = None,
        sort_by: Optional[
            "capo_route_53_domains.types.list_operations_sort_attribute_name.ListOperationsSortAttributeName"
        ] = None,
        sort_order: Optional["capo_route_53_domains.types.sort_order.SortOrder"] = None,
    ) -> "capo_route_53_domains.types.list_operations_response.ListOperationsResponse":
        """<p>Returns information about all of the operations that return an operation ID and that have ever been performed on domains that were registered by the current account. </p> <p>This command runs only in the us-east-1 Region.</p>

        Args:
            submitted_since: <p>An optional parameter that lets you get information about all the operations that you submitted after a specified date and time. Specify the date and time in Unix time format and Coordinated Universal time (UTC).</p>
            marker: <p>For an initial request for a list of operations, omit this element. If the number of operations that are not yet complete is greater than the value that you specified for <code>MaxItems</code>, you can use <code>Marker</code> to return additional operations. Get the value of <code>NextPageMarker</code> from the previous response, and submit another request that includes the value of <code>NextPageMarker</code> in the <code>Marker</code> element.</p>
            max_items: <p>Number of domains to be returned.</p> <p>Default: 20</p>
            status: <p> The status of the operations. </p>
            type: <p> An arrays of the domains operation types. </p>
            sort_by: <p> The sort type for returned values. </p>
            sort_order: <p> The sort order for returned values, either ascending or descending. </p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.list_operations_request.ListOperationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.list_operations_response.ListOperationsResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.list_operations

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.list_operations.async_list_operations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.list_operations_request.ListOperationsRequest = {}
        if submitted_since is not None:
            input_["submitted_since"] = submitted_since
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        if status is not None:
            input_["status"] = status
        if type is not None:
            input_["type"] = type
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_operations(
        self,
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        submitted_since: Optional[
            "capo_route_53_domains.types.timestamp.Timestamp"
        ] = None,
        marker: Optional["capo_route_53_domains.types.page_marker.PageMarker"] = None,
        max_items: Optional[
            "capo_route_53_domains.types.page_max_items.PageMaxItems"
        ] = None,
        status: Optional[
            "capo_route_53_domains.types.operation_status_list.OperationStatusList"
        ] = None,
        type: Optional[
            "capo_route_53_domains.types.operation_type_list.OperationTypeList"
        ] = None,
        sort_by: Optional[
            "capo_route_53_domains.types.list_operations_sort_attribute_name.ListOperationsSortAttributeName"
        ] = None,
        sort_order: Optional["capo_route_53_domains.types.sort_order.SortOrder"] = None,
    ) -> (
        "AsyncIterator[capo_route_53_domains.types.operation_summary.OperationSummary]"
    ):
        _token = marker
        while True:
            _response = await self.list_operations(
                config_overrides=config_overrides,
                submitted_since=submitted_since,
                marker=_token,
                max_items=max_items,
                status=status,
                type=type,
                sort_by=sort_by,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("operations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_marker",))
            if not _token:
                break

    async def list_prices(
        self,
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        tld: Optional["capo_route_53_domains.types.tld_name.TldName"] = None,
        marker: Optional["capo_route_53_domains.types.page_marker.PageMarker"] = None,
        max_items: Optional[
            "capo_route_53_domains.types.list_prices_page_max_items.ListPricesPageMaxItems"
        ] = None,
    ) -> "capo_route_53_domains.types.list_prices_response.ListPricesResponse":
        """<p>Lists the following prices for either all the TLDs supported by Route 53, or the specified TLD:</p> <ul> <li> <p>Registration</p> </li> <li> <p>Transfer</p> </li> <li> <p>Owner change</p> </li> <li> <p>Domain renewal</p> </li> <li> <p>Domain restoration</p> </li> </ul>

        Args:
            tld: <p>The TLD for which you want to receive the pricing information. For example. <code>.net</code>.</p> <p>If a <code>Tld</code> value is not provided, a list of prices for all TLDs supported by Route 53 is returned.</p>
            marker: <p>For an initial request for a list of prices, omit this element. If the number of prices that are not yet complete is greater than the value that you specified for <code>MaxItems</code>, you can use <code>Marker</code> to return additional prices. Get the value of <code>NextPageMarker</code> from the previous response, and submit another request that includes the value of <code>NextPageMarker</code> in the <code>Marker</code> element. </p> <p>Used only for all TLDs. If you specify a TLD, don't specify a <code>Marker</code>.</p>
            max_items: <p>Number of <code>Prices</code> to be returned.</p> <p>Used only for all TLDs. If you specify a TLD, don't specify a <code>MaxItems</code>.</p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.list_prices_request.ListPricesRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.list_prices_response.ListPricesResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.list_prices

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.list_prices.async_list_prices(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.list_prices_request.ListPricesRequest = {}
        if tld is not None:
            input_["tld"] = tld
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_prices(
        self,
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        tld: Optional["capo_route_53_domains.types.tld_name.TldName"] = None,
        marker: Optional["capo_route_53_domains.types.page_marker.PageMarker"] = None,
        max_items: Optional[
            "capo_route_53_domains.types.list_prices_page_max_items.ListPricesPageMaxItems"
        ] = None,
    ) -> "AsyncIterator[capo_route_53_domains.types.domain_price.DomainPrice]":
        _token = marker
        while True:
            _response = await self.list_prices(
                config_overrides=config_overrides,
                tld=tld,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("prices",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_marker",))
            if not _token:
                break

    async def list_tags_for_domain(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> "capo_route_53_domains.types.list_tags_for_domain_response.ListTagsForDomainResponse":
        """<p>This operation returns all of the tags that are associated with the specified domain.</p> <p>All tag operations are eventually consistent; subsequent operations might not immediately represent all issued operations.</p>

        Args:
            domain_name: <p>The domain for which you want to get a list of tags.</p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.list_tags_for_domain_request.ListTagsForDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.list_tags_for_domain_response.ListTagsForDomainResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.list_tags_for_domain

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.list_tags_for_domain.async_list_tags_for_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.list_tags_for_domain_request.ListTagsForDomainRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def push_domain(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        target: "capo_route_53_domains.types.label.Label",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> None:
        """<p> Moves a domain from Amazon Web Services to another registrar. </p> <p>Supported actions:</p> <ul> <li> <p>Changes the IPS tags of a .uk domain, and pushes it to transit. Transit means that the domain is ready to be transferred to another registrar.</p> </li> </ul>

        Args:
            domain_name: <p> Name of the domain. </p>
            target: <p> New IPS tag for the domain. </p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.tld_in_maintenance.TLDInMaintenance: <p>The top-level domain is currently undergoing maintenance and the request cannot be processed. Try again later.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.push_domain_request.PushDomainRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_route_53_domains._operations.route53_domains_v20140515.push_domain

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.push_domain.async_push_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.push_domain_request.PushDomainRequest = {
            "domain_name": domain_name,
            "target": target,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_domain(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        duration_in_years: "capo_route_53_domains.types.duration_in_years.DurationInYears",
        admin_contact: "capo_route_53_domains.types.contact_detail.ContactDetail",
        registrant_contact: "capo_route_53_domains.types.contact_detail.ContactDetail",
        tech_contact: "capo_route_53_domains.types.contact_detail.ContactDetail",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        idn_lang_code: Optional[
            "capo_route_53_domains.types.lang_code.LangCode"
        ] = None,
        auto_renew: Optional["capo_route_53_domains.types.boolean.Boolean"] = None,
        privacy_protect_admin_contact: Optional[
            "capo_route_53_domains.types.boolean.Boolean"
        ] = None,
        privacy_protect_registrant_contact: Optional[
            "capo_route_53_domains.types.boolean.Boolean"
        ] = None,
        privacy_protect_tech_contact: Optional[
            "capo_route_53_domains.types.boolean.Boolean"
        ] = None,
        billing_contact: Optional[
            "capo_route_53_domains.types.contact_detail.ContactDetail"
        ] = None,
        privacy_protect_billing_contact: Optional[
            "capo_route_53_domains.types.boolean.Boolean"
        ] = None,
    ) -> "capo_route_53_domains.types.register_domain_response.RegisterDomainResponse":
        """<p>This operation registers a domain. For some top-level domains (TLDs), this operation requires extra parameters.</p> <p>When you register a domain, Amazon Route 53 does the following:</p> <ul> <li> <p>Creates a Route 53 hosted zone that has the same name as the domain. Route 53 assigns four name servers to your hosted zone and automatically updates your domain registration with the names of these name servers.</p> </li> <li> <p>Enables auto renew, so your domain registration will renew automatically each year. We'll notify you in advance of the renewal date so you can choose whether to renew the registration.</p> </li> <li> <p>Optionally enables privacy protection, so WHOIS queries return contact for the registrar or the phrase "REDACTED FOR PRIVACY", or "On behalf of <domain name> owner." If you don't enable privacy protection, WHOIS queries return the information that you entered for the administrative, registrant, and technical contacts.</p> <note> <p>While some domains may allow different privacy settings per contact, we recommend specifying the same privacy setting for all contacts.</p> </note> </li> <li> <p>If registration is successful, returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant is notified by email.</p> </li> <li> <p>Charges your Amazon Web Services account an amount based on the top-level domain. For more information, see <a href="http://aws.amazon.com/route53/pricing/">Amazon Route 53 Pricing</a>.</p> </li> </ul>

        Args:
            domain_name: <p>The domain name that you want to register. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html">Domains that You Can Register with Amazon Route 53</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>The domain name can contain only the following characters:</p> <ul> <li> <p>Letters a through z. Domain names are not case sensitive.</p> </li> <li> <p>Numbers 0 through 9.</p> </li> <li> <p>Hyphen (-). You can't specify a hyphen at the beginning or end of a label. </p> </li> <li> <p>Period (.) to separate the labels in the name, such as the <code>.</code> in <code>example.com</code>.</p> </li> </ul> <p>Internationalized domain names are not supported for some top-level domains. To determine whether the TLD that you want to use supports internationalized domain names, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html">Domains that You Can Register with Amazon Route 53</a>. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html#domain-name-format-idns">Formatting Internationalized Domain Names</a>. </p>
            idn_lang_code: <p>Reserved for future use.</p>
            duration_in_years: <p>The number of years that you want to register the domain for. Domains are registered for a minimum of one year. The maximum period depends on the top-level domain. For the range of valid values for your domain, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html">Domains that You Can Register with Amazon Route 53</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>Default: 1</p>
            auto_renew: <p>Indicates whether the domain will be automatically renewed (<code>true</code>) or not (<code>false</code>). Auto renewal only takes effect after the account is charged.</p> <p>Default: <code>true</code> </p>
            admin_contact: <p>Provides detailed contact information. For information about the values that you specify for each element, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html">ContactDetail</a>.</p>
            registrant_contact: <p>Provides detailed contact information. For information about the values that you specify for each element, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html">ContactDetail</a>.</p>
            tech_contact: <p>Provides detailed contact information. For information about the values that you specify for each element, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html">ContactDetail</a>.</p>
            privacy_protect_admin_contact: <p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the admin contact.</p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note> <p>Default: <code>true</code> </p>
            privacy_protect_registrant_contact: <p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the registrant contact (the domain owner).</p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note> <p>Default: <code>true</code> </p>
            privacy_protect_tech_contact: <p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the technical contact.</p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note> <p>Default: <code>true</code> </p>
            billing_contact: <p>Provides detailed contact information. For information about the values that you specify for each element, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html">ContactDetail</a>.</p>
            privacy_protect_billing_contact: <p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the billing contact.</p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note>

        Raises:
            capo_route_53_domains.errors.domain_limit_exceeded.DomainLimitExceeded: <p>The number of domains has exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.duplicate_request.DuplicateRequest: <p>The request is already in progress for the domain.</p>
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.tld_rules_violation.TLDRulesViolation: <p>The top-level domain does not support this operation.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.register_domain_request.RegisterDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.register_domain_response.RegisterDomainResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.register_domain

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.register_domain.async_register_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.register_domain_request.RegisterDomainRequest = {
            "domain_name": domain_name,
            "duration_in_years": duration_in_years,
            "admin_contact": admin_contact,
            "registrant_contact": registrant_contact,
            "tech_contact": tech_contact,
        }
        if idn_lang_code is not None:
            input_["idn_lang_code"] = idn_lang_code
        if auto_renew is not None:
            input_["auto_renew"] = auto_renew
        if privacy_protect_admin_contact is not None:
            input_["privacy_protect_admin_contact"] = privacy_protect_admin_contact
        if privacy_protect_registrant_contact is not None:
            input_["privacy_protect_registrant_contact"] = (
                privacy_protect_registrant_contact
            )
        if privacy_protect_tech_contact is not None:
            input_["privacy_protect_tech_contact"] = privacy_protect_tech_contact
        if billing_contact is not None:
            input_["billing_contact"] = billing_contact
        if privacy_protect_billing_contact is not None:
            input_["privacy_protect_billing_contact"] = privacy_protect_billing_contact

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reject_domain_transfer_from_another_aws_account(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> "capo_route_53_domains.types.reject_domain_transfer_from_another_aws_account_response.RejectDomainTransferFromAnotherAwsAccountResponse":
        """<p>Rejects the transfer of a domain from another Amazon Web Services account to the current Amazon Web Services account. You initiate a transfer betweenAmazon Web Services accounts using <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomainToAnotherAwsAccount.html">TransferDomainToAnotherAwsAccount</a>. </p> <p>Use either <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListOperations.html">ListOperations</a> or <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html">GetOperationDetail</a> to determine whether the operation succeeded. <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html">GetOperationDetail</a> provides additional information, for example, <code>Domain Transfer from Aws Account 111122223333 has been cancelled</code>. </p>

        Args:
            domain_name: <p>The name of the domain that was specified when another Amazon Web Services account submitted a <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomainToAnotherAwsAccount.html">TransferDomainToAnotherAwsAccount</a> request. </p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.reject_domain_transfer_from_another_aws_account_request.RejectDomainTransferFromAnotherAwsAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.reject_domain_transfer_from_another_aws_account_response.RejectDomainTransferFromAnotherAwsAccountResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.reject_domain_transfer_from_another_aws_account

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.reject_domain_transfer_from_another_aws_account.async_reject_domain_transfer_from_another_aws_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.reject_domain_transfer_from_another_aws_account_request.RejectDomainTransferFromAnotherAwsAccountRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def renew_domain(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        current_expiry_year: "capo_route_53_domains.types.current_expiry_year.CurrentExpiryYear",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        duration_in_years: Optional[
            "capo_route_53_domains.types.duration_in_years.DurationInYears"
        ] = None,
    ) -> "capo_route_53_domains.types.renew_domain_response.RenewDomainResponse":
        """<p>This operation renews a domain for the specified number of years. The cost of renewing your domain is billed to your Amazon Web Services account.</p> <p>We recommend that you renew your domain several weeks before the expiration date. Some TLD registries delete domains before the expiration date if you haven't renewed far enough in advance. For more information about renewing domain registration, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-renew.html">Renewing Registration for a Domain</a> in the <i>Amazon Route 53 Developer Guide</i>.</p>

        Args:
            domain_name: <p>The name of the domain that you want to renew.</p>
            duration_in_years: <p>The number of years that you want to renew the domain for. The maximum number of years depends on the top-level domain. For the range of valid values for your domain, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html">Domains that You Can Register with Amazon Route 53</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>Default: 1</p>
            current_expiry_year: <p>The year when the registration for the domain is set to expire. This value must match the current expiration date for the domain.</p>

        Raises:
            capo_route_53_domains.errors.duplicate_request.DuplicateRequest: <p>The request is already in progress for the domain.</p>
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.tld_rules_violation.TLDRulesViolation: <p>The top-level domain does not support this operation.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.renew_domain_request.RenewDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.renew_domain_response.RenewDomainResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.renew_domain

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.renew_domain.async_renew_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.renew_domain_request.RenewDomainRequest = {
            "domain_name": domain_name,
            "current_expiry_year": current_expiry_year,
        }
        if duration_in_years is not None:
            input_["duration_in_years"] = duration_in_years

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def resend_contact_reachability_email(
        self,
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        domain_name: Optional[
            "capo_route_53_domains.types.domain_name.DomainName"
        ] = None,
    ) -> "capo_route_53_domains.types.resend_contact_reachability_email_response.ResendContactReachabilityEmailResponse":
        """<p>For operations that require confirmation that the email address for the registrant contact is valid, such as registering a new domain, this operation resends the confirmation email to the current email address for the registrant contact.</p>

        Args:
            domain_name: <p>The name of the domain for which you want Route 53 to resend a confirmation email to the registrant contact.</p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.tld_in_maintenance.TLDInMaintenance: <p>The top-level domain is currently undergoing maintenance and the request cannot be processed. Try again later.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.resend_contact_reachability_email_request.ResendContactReachabilityEmailRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.resend_contact_reachability_email_response.ResendContactReachabilityEmailResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.resend_contact_reachability_email

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.resend_contact_reachability_email.async_resend_contact_reachability_email(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.resend_contact_reachability_email_request.ResendContactReachabilityEmailRequest = {}
        if domain_name is not None:
            input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def resend_operation_authorization(
        self,
        operation_id: "capo_route_53_domains.types.operation_id.OperationId",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> None:
        """<p> Resend the form of authorization email for this operation. </p>

        Args:
            operation_id: <p> Operation ID. </p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.tld_in_maintenance.TLDInMaintenance: <p>The top-level domain is currently undergoing maintenance and the request cannot be processed. Try again later.</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.resend_operation_authorization_request.ResendOperationAuthorizationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_route_53_domains._operations.route53_domains_v20140515.resend_operation_authorization

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.resend_operation_authorization.async_resend_operation_authorization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.resend_operation_authorization_request.ResendOperationAuthorizationRequest = {
            "operation_id": operation_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def retrieve_domain_auth_code(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> "capo_route_53_domains.types.retrieve_domain_auth_code_response.RetrieveDomainAuthCodeResponse":
        """<p>This operation returns the authorization code for the domain. To transfer a domain to another registrar, you provide this value to the new registrar.</p>

        Args:
            domain_name: <p>The name of the domain that you want to get an authorization code for.</p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.tld_in_maintenance.TLDInMaintenance: <p>The top-level domain is currently undergoing maintenance and the request cannot be processed. Try again later.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.retrieve_domain_auth_code_request.RetrieveDomainAuthCodeRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.retrieve_domain_auth_code_response.RetrieveDomainAuthCodeResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.retrieve_domain_auth_code

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.retrieve_domain_auth_code.async_retrieve_domain_auth_code(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.retrieve_domain_auth_code_request.RetrieveDomainAuthCodeRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def transfer_domain(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        admin_contact: "capo_route_53_domains.types.contact_detail.ContactDetail",
        registrant_contact: "capo_route_53_domains.types.contact_detail.ContactDetail",
        tech_contact: "capo_route_53_domains.types.contact_detail.ContactDetail",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        idn_lang_code: Optional[
            "capo_route_53_domains.types.lang_code.LangCode"
        ] = None,
        duration_in_years: Optional[
            "capo_route_53_domains.types.duration_in_years.DurationInYears"
        ] = None,
        nameservers: Optional[
            "capo_route_53_domains.types.nameserver_list.NameserverList"
        ] = None,
        auth_code: Optional[
            "capo_route_53_domains.types.domain_auth_code.DomainAuthCode"
        ] = None,
        auto_renew: Optional["capo_route_53_domains.types.boolean.Boolean"] = None,
        privacy_protect_admin_contact: Optional[
            "capo_route_53_domains.types.boolean.Boolean"
        ] = None,
        privacy_protect_registrant_contact: Optional[
            "capo_route_53_domains.types.boolean.Boolean"
        ] = None,
        privacy_protect_tech_contact: Optional[
            "capo_route_53_domains.types.boolean.Boolean"
        ] = None,
        billing_contact: Optional[
            "capo_route_53_domains.types.contact_detail.ContactDetail"
        ] = None,
        privacy_protect_billing_contact: Optional[
            "capo_route_53_domains.types.boolean.Boolean"
        ] = None,
    ) -> "capo_route_53_domains.types.transfer_domain_response.TransferDomainResponse":
        """<p>Transfers a domain from another registrar to Amazon Route 53. </p> <p>For more information about transferring domains, see the following topics:</p> <ul> <li> <p>For transfer requirements, a detailed procedure, and information about viewing the status of a domain that you're transferring to Route 53, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-to-route-53.html">Transferring Registration for a Domain to Amazon Route 53</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> </li> <li> <p>For information about how to transfer a domain from one Amazon Web Services account to another, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomainToAnotherAwsAccount.html">TransferDomainToAnotherAwsAccount</a>. </p> </li> <li> <p>For information about how to transfer a domain to another domain registrar, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-from-route-53.html">Transferring a Domain from Amazon Route 53 to Another Registrar</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> </li> </ul> <important> <p>During the transfer of any country code top-level domains (ccTLDs) to Route 53, except for .cc and .tv, updates to the owner contact are ignored and the owner contact data from the registry is used. You can update the owner contact after the transfer is complete. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateDomainContact.html">UpdateDomainContact</a>.</p> </important> <p>If the registrar for your domain is also the DNS service provider for the domain, we highly recommend that you transfer your DNS service to Route 53 or to another DNS service provider before you transfer your registration. Some registrars provide free DNS service when you purchase a domain registration. When you transfer the registration, the previous registrar will not renew your domain registration and could end your DNS service at any time.</p> <important> <p>If the registrar for your domain is also the DNS service provider for the domain and you don't transfer DNS service to another provider, your website, email, and the web applications associated with the domain might become unavailable.</p> </important> <p>If the transfer is successful, this method returns an operation ID that you can use to track the progress and completion of the action. If the transfer doesn't complete successfully, the domain registrant will be notified by email.</p>

        Args:
            domain_name: <p>The name of the domain that you want to transfer to Route 53. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html">Domains that You Can Register with Amazon Route 53</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>The domain name can contain only the following characters:</p> <ul> <li> <p>Letters a through z. Domain names are not case sensitive.</p> </li> <li> <p>Numbers 0 through 9.</p> </li> <li> <p>Hyphen (-). You can't specify a hyphen at the beginning or end of a label. </p> </li> <li> <p>Period (.) to separate the labels in the name, such as the <code>.</code> in <code>example.com</code>.</p> </li> </ul>
            idn_lang_code: <p>Reserved for future use.</p>
            duration_in_years: <p>Reserved for future use.</p> <p>Currently, the effect of a domain transfer on the registration period varies by TLD. For information about how transferring a domain affects the expiration date, see the Transfer Term column in the pricing information at <a href="http://aws.amazon.com/route53/pricing/">Amazon Route 53 Pricing</a>.</p> <p>Default: 1</p>
            nameservers: <p>Contains details for the host and glue IP addresses.</p>
            auth_code: <p>The authorization code for the domain. You get this value from the current registrar.</p>
            auto_renew: <p>Indicates whether the domain will be automatically renewed (true) or not (false). Auto renewal only takes effect after the account is charged.</p> <p>Default: true</p>
            admin_contact: <p>Provides detailed contact information.</p>
            registrant_contact: <p>Provides detailed contact information.</p>
            tech_contact: <p>Provides detailed contact information.</p>
            privacy_protect_admin_contact: <p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS ("who is") queries return contact information for the registrar, the phrase "REDACTED FOR PRIVACY", or "On behalf of <domain name> owner.".</p> <note> <p>While some domains may allow different privacy settings per contact, we recommend specifying the same privacy setting for all contacts.</p> </note> <p>Default: <code>true</code> </p>
            privacy_protect_registrant_contact: <p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the registrant contact (domain owner).</p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note> <p>Default: <code>true</code> </p>
            privacy_protect_tech_contact: <p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the technical contact.</p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note> <p>Default: <code>true</code> </p>
            billing_contact: <p>Provides detailed contact information.</p>
            privacy_protect_billing_contact: <p> Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the billing contact. </p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note>

        Raises:
            capo_route_53_domains.errors.domain_limit_exceeded.DomainLimitExceeded: <p>The number of domains has exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.duplicate_request.DuplicateRequest: <p>The request is already in progress for the domain.</p>
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.tld_rules_violation.TLDRulesViolation: <p>The top-level domain does not support this operation.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.transfer_domain_request.TransferDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.transfer_domain_response.TransferDomainResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.transfer_domain

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.transfer_domain.async_transfer_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.transfer_domain_request.TransferDomainRequest = {
            "domain_name": domain_name,
            "admin_contact": admin_contact,
            "registrant_contact": registrant_contact,
            "tech_contact": tech_contact,
        }
        if idn_lang_code is not None:
            input_["idn_lang_code"] = idn_lang_code
        if duration_in_years is not None:
            input_["duration_in_years"] = duration_in_years
        if nameservers is not None:
            input_["nameservers"] = nameservers
        if auth_code is not None:
            input_["auth_code"] = auth_code
        if auto_renew is not None:
            input_["auto_renew"] = auto_renew
        if privacy_protect_admin_contact is not None:
            input_["privacy_protect_admin_contact"] = privacy_protect_admin_contact
        if privacy_protect_registrant_contact is not None:
            input_["privacy_protect_registrant_contact"] = (
                privacy_protect_registrant_contact
            )
        if privacy_protect_tech_contact is not None:
            input_["privacy_protect_tech_contact"] = privacy_protect_tech_contact
        if billing_contact is not None:
            input_["billing_contact"] = billing_contact
        if privacy_protect_billing_contact is not None:
            input_["privacy_protect_billing_contact"] = privacy_protect_billing_contact

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def transfer_domain_to_another_aws_account(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        account_id: "capo_route_53_domains.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
    ) -> "capo_route_53_domains.types.transfer_domain_to_another_aws_account_response.TransferDomainToAnotherAwsAccountResponse":
        """<p>Transfers a domain from the current Amazon Web Services account to another Amazon Web Services account. Note the following:</p> <ul> <li> <p>The Amazon Web Services account that you're transferring the domain to must accept the transfer. If the other account doesn't accept the transfer within 3 days, we cancel the transfer. See <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AcceptDomainTransferFromAnotherAwsAccount.html">AcceptDomainTransferFromAnotherAwsAccount</a>. </p> </li> <li> <p>You can cancel the transfer before the other account accepts it. See <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_CancelDomainTransferToAnotherAwsAccount.html">CancelDomainTransferToAnotherAwsAccount</a>. </p> </li> <li> <p>The other account can reject the transfer. See <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RejectDomainTransferFromAnotherAwsAccount.html">RejectDomainTransferFromAnotherAwsAccount</a>. </p> </li> </ul> <important> <p>When you transfer a domain from one Amazon Web Services account to another, Route 53 doesn't transfer the hosted zone that is associated with the domain. DNS resolution isn't affected if the domain and the hosted zone are owned by separate accounts, so transferring the hosted zone is optional. For information about transferring the hosted zone to another Amazon Web Services account, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-migrating.html">Migrating a Hosted Zone to a Different Amazon Web Services Account</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> </important> <p>Use either <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListOperations.html">ListOperations</a> or <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html">GetOperationDetail</a> to determine whether the operation succeeded. <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html">GetOperationDetail</a> provides additional information, for example, <code>Domain Transfer from Aws Account 111122223333 has been cancelled</code>. </p>

        Args:
            domain_name: <p>The name of the domain that you want to transfer from the current Amazon Web Services account to another account.</p>
            account_id: <p>The account ID of the Amazon Web Services account that you want to transfer the domain to, for example, <code>111122223333</code>.</p>

        Raises:
            capo_route_53_domains.errors.duplicate_request.DuplicateRequest: <p>The request is already in progress for the domain.</p>
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.transfer_domain_to_another_aws_account_request.TransferDomainToAnotherAwsAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.transfer_domain_to_another_aws_account_response.TransferDomainToAnotherAwsAccountResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.transfer_domain_to_another_aws_account

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.transfer_domain_to_another_aws_account.async_transfer_domain_to_another_aws_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.transfer_domain_to_another_aws_account_request.TransferDomainToAnotherAwsAccountRequest = {
            "domain_name": domain_name,
            "account_id": account_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_domain_contact(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        admin_contact: Optional[
            "capo_route_53_domains.types.contact_detail.ContactDetail"
        ] = None,
        registrant_contact: Optional[
            "capo_route_53_domains.types.contact_detail.ContactDetail"
        ] = None,
        tech_contact: Optional[
            "capo_route_53_domains.types.contact_detail.ContactDetail"
        ] = None,
        consent: Optional["capo_route_53_domains.types.consent.Consent"] = None,
        billing_contact: Optional[
            "capo_route_53_domains.types.contact_detail.ContactDetail"
        ] = None,
    ) -> "capo_route_53_domains.types.update_domain_contact_response.UpdateDomainContactResponse":
        """<p>This operation updates the contact information for a particular domain. You must specify information for at least one contact: registrant, administrator, or technical.</p> <p>If the update is successful, this method returns an operation ID that you can use to track the progress and completion of the operation. If the request is not completed successfully, the domain registrant will be notified by email.</p>

        Args:
            domain_name: <p>The name of the domain that you want to update contact information for.</p>
            admin_contact: <p>Provides detailed contact information.</p>
            registrant_contact: <p>Provides detailed contact information.</p>
            tech_contact: <p>Provides detailed contact information.</p>
            consent: <p> Customer's consent for the owner change request. Required if the domain is not free (consent price is more than $0.00).</p>
            billing_contact: <p>Provides detailed contact information.</p>

        Raises:
            capo_route_53_domains.errors.duplicate_request.DuplicateRequest: <p>The request is already in progress for the domain.</p>
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.tld_rules_violation.TLDRulesViolation: <p>The top-level domain does not support this operation.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.update_domain_contact_request.UpdateDomainContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.update_domain_contact_response.UpdateDomainContactResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.update_domain_contact

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.update_domain_contact.async_update_domain_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.update_domain_contact_request.UpdateDomainContactRequest = {
            "domain_name": domain_name
        }
        if admin_contact is not None:
            input_["admin_contact"] = admin_contact
        if registrant_contact is not None:
            input_["registrant_contact"] = registrant_contact
        if tech_contact is not None:
            input_["tech_contact"] = tech_contact
        if consent is not None:
            input_["consent"] = consent
        if billing_contact is not None:
            input_["billing_contact"] = billing_contact

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_domain_contact_privacy(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        admin_privacy: Optional["capo_route_53_domains.types.boolean.Boolean"] = None,
        registrant_privacy: Optional[
            "capo_route_53_domains.types.boolean.Boolean"
        ] = None,
        tech_privacy: Optional["capo_route_53_domains.types.boolean.Boolean"] = None,
        billing_privacy: Optional["capo_route_53_domains.types.boolean.Boolean"] = None,
    ) -> "capo_route_53_domains.types.update_domain_contact_privacy_response.UpdateDomainContactPrivacyResponse":
        """<p>This operation updates the specified domain contact's privacy setting. When privacy protection is enabled, your contact information is replaced with contact information for the registrar or with the phrase "REDACTED FOR PRIVACY", or "On behalf of <domain name> owner."</p> <note> <p>While some domains may allow different privacy settings per contact, we recommend specifying the same privacy setting for all contacts.</p> </note> <p>This operation affects only the contact information for the specified contact type (administrative, registrant, or technical). If the request succeeds, Amazon Route 53 returns an operation ID that you can use with <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html">GetOperationDetail</a> to track the progress and completion of the action. If the request doesn't complete successfully, the domain registrant will be notified by email.</p> <important> <p>By disabling the privacy service via API, you consent to the publication of the contact information provided for this domain via the public WHOIS database. You certify that you are the registrant of this domain name and have the authority to make this decision. You may withdraw your consent at any time by enabling privacy protection using either <code>UpdateDomainContactPrivacy</code> or the Route 53 console. Enabling privacy protection removes the contact information provided for this domain from the WHOIS database. For more information on our privacy practices, see <a href="https://aws.amazon.com/privacy/">https://aws.amazon.com/privacy/</a>.</p> </important>

        Args:
            domain_name: <p>The name of the domain that you want to update the privacy setting for.</p>
            admin_privacy: <p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the admin contact.</p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note>
            registrant_privacy: <p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the registrant contact (domain owner).</p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note>
            tech_privacy: <p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the technical contact.</p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note>
            billing_privacy: <p> Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the billing contact. </p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note>

        Raises:
            capo_route_53_domains.errors.duplicate_request.DuplicateRequest: <p>The request is already in progress for the domain.</p>
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.tld_rules_violation.TLDRulesViolation: <p>The top-level domain does not support this operation.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.update_domain_contact_privacy_request.UpdateDomainContactPrivacyRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.update_domain_contact_privacy_response.UpdateDomainContactPrivacyResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.update_domain_contact_privacy

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.update_domain_contact_privacy.async_update_domain_contact_privacy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.update_domain_contact_privacy_request.UpdateDomainContactPrivacyRequest = {
            "domain_name": domain_name
        }
        if admin_privacy is not None:
            input_["admin_privacy"] = admin_privacy
        if registrant_privacy is not None:
            input_["registrant_privacy"] = registrant_privacy
        if tech_privacy is not None:
            input_["tech_privacy"] = tech_privacy
        if billing_privacy is not None:
            input_["billing_privacy"] = billing_privacy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_domain_nameservers(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        nameservers: "capo_route_53_domains.types.nameserver_list.NameserverList",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        fi_auth_key: Optional[
            "capo_route_53_domains.types.fi_auth_key.FIAuthKey"
        ] = None,
    ) -> "capo_route_53_domains.types.update_domain_nameservers_response.UpdateDomainNameserversResponse":
        """<p>This operation replaces the current set of name servers for the domain with the specified set of name servers. If you use Amazon Route 53 as your DNS service, specify the four name servers in the delegation set for the hosted zone for the domain.</p> <p>If successful, this operation returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant will be notified by email.</p>

        Args:
            domain_name: <p>The name of the domain that you want to change name servers for.</p>
            fi_auth_key: <p>The authorization key for .fi domains</p>
            nameservers: <p>A list of new name servers for the domain.</p>

        Raises:
            capo_route_53_domains.errors.duplicate_request.DuplicateRequest: <p>The request is already in progress for the domain.</p>
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.tld_rules_violation.TLDRulesViolation: <p>The top-level domain does not support this operation.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.update_domain_nameservers_request.UpdateDomainNameserversRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.update_domain_nameservers_response.UpdateDomainNameserversResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.update_domain_nameservers

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.update_domain_nameservers.async_update_domain_nameservers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.update_domain_nameservers_request.UpdateDomainNameserversRequest = {
            "domain_name": domain_name,
            "nameservers": nameservers,
        }
        if fi_auth_key is not None:
            input_["fi_auth_key"] = fi_auth_key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_tags_for_domain(
        self,
        domain_name: "capo_route_53_domains.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        tags_to_update: Optional["capo_route_53_domains.types.tag_list.TagList"] = None,
    ) -> "capo_route_53_domains.types.update_tags_for_domain_response.UpdateTagsForDomainResponse":
        """<p>This operation adds or updates tags for a specified domain.</p> <p>All tag operations are eventually consistent; subsequent operations might not immediately represent all issued operations.</p>

        Args:
            domain_name: <p>The domain for which you want to add or update tags.</p>
            tags_to_update: <p>A list of the tag keys and values that you want to add or update. If you specify a key that already exists, the corresponding value will be replaced.</p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded: <p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>
            capo_route_53_domains.errors.unsupported_tld.UnsupportedTLD: <p>Amazon Route 53 does not support this top-level domain (TLD).</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.update_tags_for_domain_request.UpdateTagsForDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.update_tags_for_domain_response.UpdateTagsForDomainResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.update_tags_for_domain

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.update_tags_for_domain.async_update_tags_for_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.update_tags_for_domain_request.UpdateTagsForDomainRequest = {
            "domain_name": domain_name
        }
        if tags_to_update is not None:
            input_["tags_to_update"] = tags_to_update

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def view_billing(
        self,
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        start: Optional["capo_route_53_domains.types.timestamp.Timestamp"] = None,
        end: Optional["capo_route_53_domains.types.timestamp.Timestamp"] = None,
        marker: Optional["capo_route_53_domains.types.page_marker.PageMarker"] = None,
        max_items: Optional[
            "capo_route_53_domains.types.page_max_items.PageMaxItems"
        ] = None,
    ) -> "capo_route_53_domains.types.view_billing_response.ViewBillingResponse":
        """<p>Returns all the domain-related billing records for the current Amazon Web Services account for a specified period</p>

        Args:
            start: <p>The beginning date and time for the time period for which you want a list of billing records. Specify the date and time in Unix time format and Coordinated Universal time (UTC).</p>
            end: <p>The end date and time for the time period for which you want a list of billing records. Specify the date and time in Unix time format and Coordinated Universal time (UTC).</p>
            marker: <p>For an initial request for a list of billing records, omit this element. If the number of billing records that are associated with the current Amazon Web Services account during the specified period is greater than the value that you specified for <code>MaxItems</code>, you can use <code>Marker</code> to return additional billing records. Get the value of <code>NextPageMarker</code> from the previous response, and submit another request that includes the value of <code>NextPageMarker</code> in the <code>Marker</code> element. </p> <p>Constraints: The marker must match the value of <code>NextPageMarker</code> that was returned in the previous response.</p>
            max_items: <p>The number of billing records to be returned.</p> <p>Default: 20</p>

        Raises:
            capo_route_53_domains.errors.invalid_input.InvalidInput: <p>The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For <code>AcceptDomainTransferFromAnotherAwsAccount</code>, the password might be invalid.</p>
            capo_route_53_domains.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route_53_domains.types.view_billing_request.ViewBillingRequest]",
        ) -> AsyncOperationResponse[
            "capo_route_53_domains.types.view_billing_response.ViewBillingResponse"
        ]:
            import capo_route_53_domains._operations.route53_domains_v20140515.view_billing

            (
                output,
                http_response,
            ) = await capo_route_53_domains._operations.route53_domains_v20140515.view_billing.async_view_billing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53_domains.types.view_billing_request.ViewBillingRequest = {}
        if start is not None:
            input_["start"] = start
        if end is not None:
            input_["end"] = end
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_view_billing(
        self,
        *,
        config_overrides: Optional[AsyncRoute53DomainsClientConfig] = None,
        start: Optional["capo_route_53_domains.types.timestamp.Timestamp"] = None,
        end: Optional["capo_route_53_domains.types.timestamp.Timestamp"] = None,
        marker: Optional["capo_route_53_domains.types.page_marker.PageMarker"] = None,
        max_items: Optional[
            "capo_route_53_domains.types.page_max_items.PageMaxItems"
        ] = None,
    ) -> "AsyncIterator[capo_route_53_domains.types.billing_record.BillingRecord]":
        _token = marker
        while True:
            _response = await self.view_billing(
                config_overrides=config_overrides,
                start=start,
                end=end,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("billing_records",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_marker",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
