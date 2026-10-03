from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_account._auth._signers
import capo_account._auth._sigv4
from capo_account._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_account.types.account_id
    import capo_account.types.alternate_contact_type
    import capo_account.types.delete_alternate_contact_request
    import capo_account.types.email_address
    import capo_account.types.get_alternate_contact_request
    import capo_account.types.get_alternate_contact_response
    import capo_account.types.name
    import capo_account.types.phone_number
    import capo_account.types.put_alternate_contact_request
    import capo_account.types.title
    from capo_account._services.account import AccountClient, AccountClientConfig
    from capo_account._services.async_account import (
        AsyncAccountClient,
        AsyncAccountClientConfig,
    )


class AlternateContactResource:
    def __init__(self, service: AccountClient) -> None:
        self._service = service

    def put(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def read(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def delete(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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


class AsyncAlternateContactResource:
    def __init__(self, service: AsyncAccountClient) -> None:
        self._service = service

    async def put(
        self,
        name: "capo_account.types.name.Name",
        title: "capo_account.types.title.Title",
        email_address: "capo_account.types.email_address.EmailAddress",
        phone_number: "capo_account.types.phone_number.PhoneNumber",
        alternate_contact_type: "capo_account.types.alternate_contact_type.AlternateContactType",
        *,
        config_overrides: Optional[AsyncAccountClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_account.types.put_alternate_contact_request.PutAlternateContactRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_account._operations.account.put_alternate_contact

            (
                output,
                http_response,
            ) = await capo_account._operations.account.put_alternate_contact.async_put_alternate_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account.types.put_alternate_contact_request.PutAlternateContactRequest = {
            "name": name,
            "title": title,
            "email_address": email_address,
            "phone_number": phone_number,
            "alternate_contact_type": alternate_contact_type,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        alternate_contact_type: "capo_account.types.alternate_contact_type.AlternateContactType",
        *,
        config_overrides: Optional[AsyncAccountClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_account.types.get_alternate_contact_request.GetAlternateContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_account.types.get_alternate_contact_response.GetAlternateContactResponse"
        ]:
            import capo_account._operations.account.get_alternate_contact

            (
                output,
                http_response,
            ) = await capo_account._operations.account.get_alternate_contact.async_get_alternate_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account.types.get_alternate_contact_request.GetAlternateContactRequest = {
            "alternate_contact_type": alternate_contact_type
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        alternate_contact_type: "capo_account.types.alternate_contact_type.AlternateContactType",
        *,
        config_overrides: Optional[AsyncAccountClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_account.types.delete_alternate_contact_request.DeleteAlternateContactRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_account._operations.account.delete_alternate_contact

            (
                output,
                http_response,
            ) = await capo_account._operations.account.delete_alternate_contact.async_delete_alternate_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account.types.delete_alternate_contact_request.DeleteAlternateContactRequest = {
            "alternate_contact_type": alternate_contact_type
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
