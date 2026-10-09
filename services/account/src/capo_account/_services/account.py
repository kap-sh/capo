"""Generated from Smithy shape ``com.amazonaws.account#Account``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_account._auth._signers
import capo_account._auth._sigv4
from capo_account._auth._identity import Credentials
from capo_account._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_account._auth._zapros_handler import AuthMiddleware
from capo_account._pagination import resolve_path as _resolve_path
from capo_account._resources.account.account_name_resource import AccountNameResource
from capo_account._resources.account.alternate_contact_resource import (
    AlternateContactResource,
)
from capo_account._resources.account.commercial_to_gov_cloud_gateway_resource import (
    CommercialToGovCloudGatewayResource,
)
from capo_account._resources.account.contact_information_resource import (
    ContactInformationResource,
)
from capo_account._resources.account.phone_number_verification_resource import (
    PhoneNumberVerificationResource,
)
from capo_account._resources.account.primary_email_resource import PrimaryEmailResource
from capo_account._resources.account.region_opt_resource import RegionOptResource
from capo_account._services._aws_config import aws_config
from capo_account._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_account.types.accept_primary_email_update_request
    import capo_account.types.accept_primary_email_update_response
    import capo_account.types.account_id
    import capo_account.types.account_name
    import capo_account.types.alternate_contact_type
    import capo_account.types.contact_information
    import capo_account.types.delete_alternate_contact_request
    import capo_account.types.disable_region_request
    import capo_account.types.email_address
    import capo_account.types.enable_region_request
    import capo_account.types.get_account_information_request
    import capo_account.types.get_account_information_response
    import capo_account.types.get_alternate_contact_request
    import capo_account.types.get_alternate_contact_response
    import capo_account.types.get_contact_information_request
    import capo_account.types.get_contact_information_response
    import capo_account.types.get_gov_cloud_account_information_request
    import capo_account.types.get_gov_cloud_account_information_response
    import capo_account.types.get_primary_email_request
    import capo_account.types.get_primary_email_response
    import capo_account.types.get_primary_email_update_status_request
    import capo_account.types.get_primary_email_update_status_response
    import capo_account.types.get_region_opt_status_request
    import capo_account.types.get_region_opt_status_response
    import capo_account.types.list_regions_request
    import capo_account.types.list_regions_response
    import capo_account.types.name
    import capo_account.types.otp
    import capo_account.types.phone_number
    import capo_account.types.primary_email_address
    import capo_account.types.put_account_name_request
    import capo_account.types.put_alternate_contact_request
    import capo_account.types.put_contact_information_request
    import capo_account.types.region
    import capo_account.types.region_name
    import capo_account.types.region_opt_status_list
    import capo_account.types.send_phone_number_verification_request
    import capo_account.types.send_phone_number_verification_response
    import capo_account.types.start_primary_email_update_request
    import capo_account.types.start_primary_email_update_response
    import capo_account.types.title
    import capo_account.types.verify_phone_number_request
    import capo_account.types.verify_phone_number_response


class AccountClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AccountClient:
    """A client for the ``Account`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
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
                Client(http_handler)
            )
        self._config = AccountClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.account_name_resource = AccountNameResource(self)
        self.alternate_contact_resource = AlternateContactResource(self)
        self.commercial_to_gov_cloud_gateway_resource = (
            CommercialToGovCloudGatewayResource(self)
        )
        self.contact_information_resource = ContactInformationResource(self)
        self.phone_number_verification_resource = PhoneNumberVerificationResource(self)
        self.primary_email_resource = PrimaryEmailResource(self)
        self.region_opt_resource = RegionOptResource(self)

    def operation_options(
        self, config_overrides: Optional[AccountClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: AccountClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
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

    def put_account_name(
        self,
        account_name: "capo_account.types.account_name.AccountName",
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["capo_account.types.account_id.AccountId"] = None,
    ) -> None:
        """<p>Updates the account name of the specified account. To use this API, IAM principals must have the <code>account:PutAccountName</code> IAM permission. </p>

        Args:
            account_name: <p>The name of the account.</p>
            account_id: <p>Specifies the 12 digit account ID number of the Amazon Web Services account that you want to access or modify with this operation.</p> <p>If you do not specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation.</p> <p>To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated administrator</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>; it must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>

        Raises:
            capo_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            capo_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            capo_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            capo_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            capo_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account.types.put_account_name_request.PutAccountNameRequest]",
        ) -> OperationResponse[None]:
            import capo_account._operations.account.put_account_name

            output, http_response = (
                capo_account._operations.account.put_account_name.put_account_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account.types.put_account_name_request.PutAccountNameRequest = {
            "account_name": account_name
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_account_information(
        self,
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["capo_account.types.account_id.AccountId"] = None,
    ) -> "capo_account.types.get_account_information_response.GetAccountInformationResponse":
        """<p>Retrieves information about the specified account including its account name, account ID, account creation date and time, and account state. To use this API, an IAM user or role must have the <code>account:GetAccountInformation</code> IAM permission. </p>

        Args:
            account_id: <p>Specifies the 12 digit account ID number of the Amazon Web Services account that you want to access or modify with this operation.</p> <p>If you do not specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation.</p> <p>To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated administrator</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>; it must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>

        Raises:
            capo_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            capo_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            capo_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            capo_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            capo_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account.types.get_account_information_request.GetAccountInformationRequest]",
        ) -> OperationResponse[
            "capo_account.types.get_account_information_response.GetAccountInformationResponse"
        ]:
            import capo_account._operations.account.get_account_information

            output, http_response = (
                capo_account._operations.account.get_account_information.get_account_information(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account.types.get_account_information_request.GetAccountInformationRequest = {}
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_alternate_contact(
        self,
        name: "capo_account.types.name.Name",
        title: "capo_account.types.title.Title",
        email_address: "capo_account.types.email_address.EmailAddress",
        phone_number: "capo_account.types.phone_number.PhoneNumber",
        alternate_contact_type: "capo_account.types.alternate_contact_type.AlternateContactType",
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["capo_account.types.account_id.AccountId"] = None,
    ) -> None:
        """<p>Modifies the specified alternate contact attached to an Amazon Web Services account.</p> <p>For complete details about how to use the alternate contact operations, see <a href="https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html">Update the alternate contacts for your Amazon Web Services account</a>.</p> <note> <p>Before you can update the alternate contact information for an Amazon Web Services account that is managed by Organizations, you must first enable integration between Amazon Web Services Account Management and Organizations. For more information, see <a href="https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-trusted-access.html">Enable trusted access for Amazon Web Services Account Management</a>.</p> </note>

        Args:
            name: <p>Specifies a name for the alternate contact.</p>
            title: <p>Specifies a title for the alternate contact.</p>
            email_address: <p>Specifies an email address for the alternate contact. </p>
            phone_number: <p>Specifies a phone number for the alternate contact.</p>
            alternate_contact_type: <p>Specifies which alternate contact you want to create or update.</p>
            account_id: <p>Specifies the 12 digit account ID number of the Amazon Web Services account that you want to access or modify with this operation.</p> <p>If you do not specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation.</p> <p>To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated administrator</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>; it must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>

        Raises:
            capo_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            capo_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            capo_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            capo_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            capo_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account.types.put_alternate_contact_request.PutAlternateContactRequest]",
        ) -> OperationResponse[None]:
            import capo_account._operations.account.put_alternate_contact

            output, http_response = (
                capo_account._operations.account.put_alternate_contact.put_alternate_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account.types.put_alternate_contact_request.PutAlternateContactRequest = {
            "name": name,
            "title": title,
            "email_address": email_address,
            "phone_number": phone_number,
            "alternate_contact_type": alternate_contact_type,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_alternate_contact(
        self,
        alternate_contact_type: "capo_account.types.alternate_contact_type.AlternateContactType",
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["capo_account.types.account_id.AccountId"] = None,
    ) -> (
        "capo_account.types.get_alternate_contact_response.GetAlternateContactResponse"
    ):
        """<p>Retrieves the specified alternate contact attached to an Amazon Web Services account.</p> <p>For complete details about how to use the alternate contact operations, see <a href="https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html">Update the alternate contacts for your Amazon Web Services account</a>.</p> <note> <p>Before you can update the alternate contact information for an Amazon Web Services account that is managed by Organizations, you must first enable integration between Amazon Web Services Account Management and Organizations. For more information, see <a href="https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-trusted-access.html">Enable trusted access for Amazon Web Services Account Management</a>.</p> </note>

        Args:
            alternate_contact_type: <p>Specifies which alternate contact you want to retrieve.</p>
            account_id: <p>Specifies the 12 digit account ID number of the Amazon Web Services account that you want to access or modify with this operation.</p> <p>If you do not specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation.</p> <p>To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated administrator</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>; it must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>

        Raises:
            capo_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            capo_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            capo_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation failed because it specified a resource that can't be found.</p>
            capo_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            capo_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            capo_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account.types.get_alternate_contact_request.GetAlternateContactRequest]",
        ) -> OperationResponse[
            "capo_account.types.get_alternate_contact_response.GetAlternateContactResponse"
        ]:
            import capo_account._operations.account.get_alternate_contact

            output, http_response = (
                capo_account._operations.account.get_alternate_contact.get_alternate_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account.types.get_alternate_contact_request.GetAlternateContactRequest = {
            "alternate_contact_type": alternate_contact_type
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_alternate_contact(
        self,
        alternate_contact_type: "capo_account.types.alternate_contact_type.AlternateContactType",
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["capo_account.types.account_id.AccountId"] = None,
    ) -> None:
        """<p>Deletes the specified alternate contact from an Amazon Web Services account.</p> <p>For complete details about how to use the alternate contact operations, see <a href="https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html">Update the alternate contacts for your Amazon Web Services account</a>.</p> <note> <p>Before you can update the alternate contact information for an Amazon Web Services account that is managed by Organizations, you must first enable integration between Amazon Web Services Account Management and Organizations. For more information, see <a href="https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-trusted-access.html">Enable trusted access for Amazon Web Services Account Management</a>.</p> </note>

        Args:
            alternate_contact_type: <p>Specifies which of the alternate contacts to delete. </p>
            account_id: <p>Specifies the 12 digit account ID number of the Amazon Web Services account that you want to access or modify with this operation.</p> <p>If you do not specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation.</p> <p>To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated administrator</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>; it must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>

        Raises:
            capo_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            capo_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            capo_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation failed because it specified a resource that can't be found.</p>
            capo_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            capo_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            capo_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account.types.delete_alternate_contact_request.DeleteAlternateContactRequest]",
        ) -> OperationResponse[None]:
            import capo_account._operations.account.delete_alternate_contact

            output, http_response = (
                capo_account._operations.account.delete_alternate_contact.delete_alternate_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account.types.delete_alternate_contact_request.DeleteAlternateContactRequest = {
            "alternate_contact_type": alternate_contact_type
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_gov_cloud_account_information(
        self,
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        standard_account_id: Optional["capo_account.types.account_id.AccountId"] = None,
    ) -> "capo_account.types.get_gov_cloud_account_information_response.GetGovCloudAccountInformationResponse":
        """<p>Retrieves information about the GovCloud account linked to the specified standard account (if it exists) including the GovCloud account ID and state. To use this API, an IAM user or role must have the <code>account:GetGovCloudAccountInformation</code> IAM permission. </p>

        Args:
            standard_account_id: <p>Specifies the 12 digit account ID number of the Amazon Web Services account that you want to access or modify with this operation.</p> <p>If you do not specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation.</p> <p>To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated administrator</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>; it must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>

        Raises:
            capo_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            capo_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            capo_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation failed because it specified a resource that can't be found.</p>
            capo_account.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The operation failed because it specified a resource that is not currently available.</p>
            capo_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            capo_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            capo_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account.types.get_gov_cloud_account_information_request.GetGovCloudAccountInformationRequest]",
        ) -> OperationResponse[
            "capo_account.types.get_gov_cloud_account_information_response.GetGovCloudAccountInformationResponse"
        ]:
            import capo_account._operations.account.get_gov_cloud_account_information

            output, http_response = (
                capo_account._operations.account.get_gov_cloud_account_information.get_gov_cloud_account_information(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account.types.get_gov_cloud_account_information_request.GetGovCloudAccountInformationRequest = {}
        if standard_account_id is not None:
            input_["standard_account_id"] = standard_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_contact_information(
        self,
        contact_information: "capo_account.types.contact_information.ContactInformation",
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["capo_account.types.account_id.AccountId"] = None,
    ) -> None:
        """<p>Updates the primary contact information of an Amazon Web Services account.</p> <p>For complete details about how to use the primary contact operations, see <a href="https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-primary.html">Update the primary contact for your Amazon Web Services account</a>.</p>

        Args:
            contact_information: <p>Contains the details of the primary contact information associated with an Amazon Web Services account.</p>
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated administrator</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>. It must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>

        Raises:
            capo_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            capo_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            capo_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            capo_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            capo_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account.types.put_contact_information_request.PutContactInformationRequest]",
        ) -> OperationResponse[None]:
            import capo_account._operations.account.put_contact_information

            output, http_response = (
                capo_account._operations.account.put_contact_information.put_contact_information(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account.types.put_contact_information_request.PutContactInformationRequest = {
            "contact_information": contact_information
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_contact_information(
        self,
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["capo_account.types.account_id.AccountId"] = None,
    ) -> "capo_account.types.get_contact_information_response.GetContactInformationResponse":
        """<p>Retrieves the primary contact information of an Amazon Web Services account.</p> <p>For complete details about how to use the primary contact operations, see <a href="https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-primary.html">Update the primary contact for your Amazon Web Services account</a>.</p>

        Args:
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated admin</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>. It must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>

        Raises:
            capo_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            capo_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            capo_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation failed because it specified a resource that can't be found.</p>
            capo_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            capo_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            capo_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account.types.get_contact_information_request.GetContactInformationRequest]",
        ) -> OperationResponse[
            "capo_account.types.get_contact_information_response.GetContactInformationResponse"
        ]:
            import capo_account._operations.account.get_contact_information

            output, http_response = (
                capo_account._operations.account.get_contact_information.get_contact_information(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account.types.get_contact_information_request.GetContactInformationRequest = {}
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_phone_number_verification(
        self,
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["capo_account.types.account_id.AccountId"] = None,
    ) -> "capo_account.types.send_phone_number_verification_response.SendPhoneNumberVerificationResponse":
        """<p>Sends a one-time passcode to the phone number in the primary contact information of an Amazon Web Services account. Use <a>VerifyPhoneNumber</a> to submit the passcode and complete the verification.</p> <p>For complete details about how to use the primary contact operations, see <a href="https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-primary.html">Update the primary contact for your Amazon Web Services account</a>.</p>

        Args:
            account_id: <p>Specifies the 12 digit account ID number of the Amazon Web Services account that you want to access or modify with this operation.</p> <p>If you do not specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation.</p> <p>To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated administrator</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>; it must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>

        Raises:
            capo_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            capo_account.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict in the current status of the resource. For example, this happens if you try to enable a Region that is currently being disabled (in a status of DISABLING) or if you try to change an account’s root user email to an email address which is already in use.</p>
            capo_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            capo_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation failed because it specified a resource that can't be found.</p>
            capo_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            capo_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            capo_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account.types.send_phone_number_verification_request.SendPhoneNumberVerificationRequest]",
        ) -> OperationResponse[
            "capo_account.types.send_phone_number_verification_response.SendPhoneNumberVerificationResponse"
        ]:
            import capo_account._operations.account.send_phone_number_verification

            output, http_response = (
                capo_account._operations.account.send_phone_number_verification.send_phone_number_verification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account.types.send_phone_number_verification_request.SendPhoneNumberVerificationRequest = {}
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def verify_phone_number(
        self,
        otp: "capo_account.types.otp.Otp",
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["capo_account.types.account_id.AccountId"] = None,
    ) -> "capo_account.types.verify_phone_number_response.VerifyPhoneNumberResponse":
        """<p>Verifies the phone number in the primary contact information of an Amazon Web Services account by submitting the one-time passcode that <a>SendPhoneNumberVerification</a> sent to that phone number.</p> <p>For complete details about how to use the primary contact operations, see <a href="https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-primary.html">Update the primary contact for your Amazon Web Services account</a>.</p>

        Args:
            account_id: <p>Specifies the 12 digit account ID number of the Amazon Web Services account that you want to access or modify with this operation.</p> <p>If you do not specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation.</p> <p>To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated administrator</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>; it must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>
            otp: <p>The one-time passcode sent to the phone number in the primary contact information by the <code>SendPhoneNumberVerification</code> operation.</p>

        Raises:
            capo_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            capo_account.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict in the current status of the resource. For example, this happens if you try to enable a Region that is currently being disabled (in a status of DISABLING) or if you try to change an account’s root user email to an email address which is already in use.</p>
            capo_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            capo_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation failed because it specified a resource that can't be found.</p>
            capo_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            capo_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            capo_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account.types.verify_phone_number_request.VerifyPhoneNumberRequest]",
        ) -> OperationResponse[
            "capo_account.types.verify_phone_number_response.VerifyPhoneNumberResponse"
        ]:
            import capo_account._operations.account.verify_phone_number

            output, http_response = (
                capo_account._operations.account.verify_phone_number.verify_phone_number(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account.types.verify_phone_number_request.VerifyPhoneNumberRequest = {
            "otp": otp
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def accept_primary_email_update(
        self,
        account_id: "capo_account.types.account_id.AccountId",
        primary_email: "capo_account.types.primary_email_address.PrimaryEmailAddress",
        otp: "capo_account.types.otp.Otp",
        *,
        config_overrides: Optional[AccountClientConfig] = None,
    ) -> "capo_account.types.accept_primary_email_update_response.AcceptPrimaryEmailUpdateResponse":
        """<p>Accepts the request that originated from <a>StartPrimaryEmailUpdate</a> to update the primary email address (also known as the root user email address) for the specified account.</p>

        Args:
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated admin</a> account assigned.</p> <p>This operation can only be called from the management account or the delegated administrator account of an organization for a member account.</p> <note> <p>The management account can't specify its own <code>AccountId</code>.</p> </note>
            primary_email: <p>The new primary email address for use with the specified account. This must match the <code>PrimaryEmail</code> from the <code>StartPrimaryEmailUpdate</code> API call.</p>
            otp: <p>The OTP code sent to the <code>PrimaryEmail</code> specified on the <code>StartPrimaryEmailUpdate</code> API call.</p>

        Raises:
            capo_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            capo_account.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict in the current status of the resource. For example, this happens if you try to enable a Region that is currently being disabled (in a status of DISABLING) or if you try to change an account’s root user email to an email address which is already in use.</p>
            capo_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            capo_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation failed because it specified a resource that can't be found.</p>
            capo_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            capo_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            capo_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account.types.accept_primary_email_update_request.AcceptPrimaryEmailUpdateRequest]",
        ) -> OperationResponse[
            "capo_account.types.accept_primary_email_update_response.AcceptPrimaryEmailUpdateResponse"
        ]:
            import capo_account._operations.account.accept_primary_email_update

            output, http_response = (
                capo_account._operations.account.accept_primary_email_update.accept_primary_email_update(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account.types.accept_primary_email_update_request.AcceptPrimaryEmailUpdateRequest = {
            "account_id": account_id,
            "primary_email": primary_email,
            "otp": otp,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_primary_email(
        self,
        account_id: "capo_account.types.account_id.AccountId",
        *,
        config_overrides: Optional[AccountClientConfig] = None,
    ) -> "capo_account.types.get_primary_email_response.GetPrimaryEmailResponse":
        """<p>Retrieves the primary email address for the specified account.</p>

        Args:
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated admin</a> account assigned.</p> <p>This operation can only be called from the management account or the delegated administrator account of an organization for a member account.</p> <note> <p>The management account can't specify its own <code>AccountId</code>.</p> </note>

        Raises:
            capo_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            capo_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            capo_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation failed because it specified a resource that can't be found.</p>
            capo_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            capo_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            capo_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account.types.get_primary_email_request.GetPrimaryEmailRequest]",
        ) -> OperationResponse[
            "capo_account.types.get_primary_email_response.GetPrimaryEmailResponse"
        ]:
            import capo_account._operations.account.get_primary_email

            output, http_response = (
                capo_account._operations.account.get_primary_email.get_primary_email(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account.types.get_primary_email_request.GetPrimaryEmailRequest = {
            "account_id": account_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_primary_email_update_status(
        self,
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["capo_account.types.account_id.AccountId"] = None,
    ) -> "capo_account.types.get_primary_email_update_status_response.GetPrimaryEmailUpdateStatusResponse":
        """<p>Retrieves the status of the most recent primary email update for the specified account. For complete details about how to update the primary email address, see <a href="https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-root-user-email.html">Update the primary email address for your AWS account</a>.</p>

        Args:
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated admin</a> account assigned.</p> <p>This operation can only be called from the management account or the delegated administrator account of an organization for a member account.</p> <note> <p>The management account can't specify its own <code>AccountId</code>.</p> </note>

        Raises:
            capo_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            capo_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            capo_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation failed because it specified a resource that can't be found.</p>
            capo_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            capo_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            capo_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account.types.get_primary_email_update_status_request.GetPrimaryEmailUpdateStatusRequest]",
        ) -> OperationResponse[
            "capo_account.types.get_primary_email_update_status_response.GetPrimaryEmailUpdateStatusResponse"
        ]:
            import capo_account._operations.account.get_primary_email_update_status

            output, http_response = (
                capo_account._operations.account.get_primary_email_update_status.get_primary_email_update_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account.types.get_primary_email_update_status_request.GetPrimaryEmailUpdateStatusRequest = {}
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_primary_email_update(
        self,
        account_id: "capo_account.types.account_id.AccountId",
        primary_email: "capo_account.types.primary_email_address.PrimaryEmailAddress",
        *,
        config_overrides: Optional[AccountClientConfig] = None,
    ) -> "capo_account.types.start_primary_email_update_response.StartPrimaryEmailUpdateResponse":
        """<p>Starts the process to update the primary email address for the specified account.</p>

        Args:
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated admin</a> account assigned.</p> <p>This operation can only be called from the management account or the delegated administrator account of an organization for a member account.</p> <note> <p>The management account can't specify its own <code>AccountId</code>.</p> </note>
            primary_email: <p>The new primary email address (also known as the root user email address) to use in the specified account.</p>

        Raises:
            capo_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            capo_account.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict in the current status of the resource. For example, this happens if you try to enable a Region that is currently being disabled (in a status of DISABLING) or if you try to change an account’s root user email to an email address which is already in use.</p>
            capo_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            capo_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation failed because it specified a resource that can't be found.</p>
            capo_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            capo_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            capo_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account.types.start_primary_email_update_request.StartPrimaryEmailUpdateRequest]",
        ) -> OperationResponse[
            "capo_account.types.start_primary_email_update_response.StartPrimaryEmailUpdateResponse"
        ]:
            import capo_account._operations.account.start_primary_email_update

            output, http_response = (
                capo_account._operations.account.start_primary_email_update.start_primary_email_update(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account.types.start_primary_email_update_request.StartPrimaryEmailUpdateRequest = {
            "account_id": account_id,
            "primary_email": primary_email,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disable_region(
        self,
        region_name: "capo_account.types.region_name.RegionName",
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["capo_account.types.account_id.AccountId"] = None,
    ) -> None:
        """<p>Disables (opts-out) a particular Region for an account.</p> <note> <p>The act of disabling a Region will remove all IAM access to any resources that reside in that Region.</p> </note>

        Args:
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated admin</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>. It must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>
            region_name: <p>Specifies the Region-code for a given Region name (for example, <code>af-south-1</code>). When you disable a Region, Amazon Web Services performs actions to deactivate that Region in your account, such as destroying IAM resources in the Region. This process takes a few minutes for most accounts, but this can take several hours. You cannot enable the Region until the disabling process is fully completed.</p>

        Raises:
            capo_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            capo_account.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict in the current status of the resource. For example, this happens if you try to enable a Region that is currently being disabled (in a status of DISABLING) or if you try to change an account’s root user email to an email address which is already in use.</p>
            capo_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            capo_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            capo_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            capo_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account.types.disable_region_request.DisableRegionRequest]",
        ) -> OperationResponse[None]:
            import capo_account._operations.account.disable_region

            output, http_response = (
                capo_account._operations.account.disable_region.disable_region(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account.types.disable_region_request.DisableRegionRequest = {
            "region_name": region_name
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def enable_region(
        self,
        region_name: "capo_account.types.region_name.RegionName",
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["capo_account.types.account_id.AccountId"] = None,
    ) -> None:
        """<p>Enables (opts-in) a particular Region for an account.</p>

        Args:
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated admin</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>. It must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>
            region_name: <p>Specifies the Region-code for a given Region name (for example, <code>af-south-1</code>). When you enable a Region, Amazon Web Services performs actions to prepare your account in that Region, such as distributing your IAM resources to the Region. This process takes a few minutes for most accounts, but it can take several hours. You cannot use the Region until this process is complete. Furthermore, you cannot disable the Region until the enabling process is fully completed.</p>

        Raises:
            capo_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            capo_account.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict in the current status of the resource. For example, this happens if you try to enable a Region that is currently being disabled (in a status of DISABLING) or if you try to change an account’s root user email to an email address which is already in use.</p>
            capo_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            capo_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            capo_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            capo_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account.types.enable_region_request.EnableRegionRequest]",
        ) -> OperationResponse[None]:
            import capo_account._operations.account.enable_region

            output, http_response = (
                capo_account._operations.account.enable_region.enable_region(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account.types.enable_region_request.EnableRegionRequest = {
            "region_name": region_name
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_region_opt_status(
        self,
        region_name: "capo_account.types.region_name.RegionName",
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["capo_account.types.account_id.AccountId"] = None,
    ) -> "capo_account.types.get_region_opt_status_response.GetRegionOptStatusResponse":
        """<p>Retrieves the opt-in status of a particular Region.</p>

        Args:
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated admin</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>. It must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>
            region_name: <p>Specifies the Region-code for a given Region name (for example, <code>af-south-1</code>). This function will return the status of whatever Region you pass into this parameter. </p>

        Raises:
            capo_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            capo_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            capo_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            capo_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            capo_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account.types.get_region_opt_status_request.GetRegionOptStatusRequest]",
        ) -> OperationResponse[
            "capo_account.types.get_region_opt_status_response.GetRegionOptStatusResponse"
        ]:
            import capo_account._operations.account.get_region_opt_status

            output, http_response = (
                capo_account._operations.account.get_region_opt_status.get_region_opt_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account.types.get_region_opt_status_request.GetRegionOptStatusRequest = {
            "region_name": region_name
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_regions(
        self,
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["capo_account.types.account_id.AccountId"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        region_opt_status_contains: Optional[
            "capo_account.types.region_opt_status_list.RegionOptStatusList"
        ] = None,
    ) -> "capo_account.types.list_regions_response.ListRegionsResponse":
        """<p>Lists all the Regions for a given account and their respective opt-in statuses. Optionally, this list can be filtered by the <code>region-opt-status-contains</code> parameter. </p>

        Args:
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated admin</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>. It must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>
            max_results: <p>The total number of items to return in the command’s output. If the total number of items available is more than the value specified, a <code>NextToken</code> is provided in the command’s output. To resume pagination, provide the <code>NextToken</code> value in the <code>starting-token</code> argument of a subsequent command. Do not use the <code>NextToken</code> response element directly outside of the Amazon Web Services CLI. For usage examples, see <a href="http://docs.aws.amazon.com/cli/latest/userguide/pagination.html">Pagination</a> in the <i>Amazon Web Services Command Line Interface User Guide</i>. </p>
            next_token: <p>A token used to specify where to start paginating. This is the <code>NextToken</code> from a previously truncated response. For usage examples, see <a href="http://docs.aws.amazon.com/cli/latest/userguide/pagination.html">Pagination</a> in the <i>Amazon Web Services Command Line Interface User Guide</i>.</p>
            region_opt_status_contains: <p>A list of Region statuses (Enabling, Enabled, Disabling, Disabled, Enabled_by_default) to use to filter the list of Regions for a given account. For example, passing in a value of ENABLING will only return a list of Regions with a Region status of ENABLING.</p>

        Raises:
            capo_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            capo_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            capo_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            capo_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            capo_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account.types.list_regions_request.ListRegionsRequest]",
        ) -> OperationResponse[
            "capo_account.types.list_regions_response.ListRegionsResponse"
        ]:
            import capo_account._operations.account.list_regions

            output, http_response = (
                capo_account._operations.account.list_regions.list_regions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account.types.list_regions_request.ListRegionsRequest = {}
        if account_id is not None:
            input_["account_id"] = account_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if region_opt_status_contains is not None:
            input_["region_opt_status_contains"] = region_opt_status_contains

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_regions(
        self,
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["capo_account.types.account_id.AccountId"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        region_opt_status_contains: Optional[
            "capo_account.types.region_opt_status_list.RegionOptStatusList"
        ] = None,
    ) -> "Iterator[capo_account.types.region.Region]":
        _token = next_token
        while True:
            _response = self.list_regions(
                config_overrides=config_overrides,
                account_id=account_id,
                max_results=max_results,
                next_token=_token,
                region_opt_status_contains=region_opt_status_contains,
            )
            _page = _resolve_path(_response, ("regions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
