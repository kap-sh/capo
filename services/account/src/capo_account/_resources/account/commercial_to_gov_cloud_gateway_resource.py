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
    import capo_account.types.get_gov_cloud_account_information_request
    import capo_account.types.get_gov_cloud_account_information_response
    from capo_account._services.account import AccountClient, AccountClientConfig
    from capo_account._services.async_account import (
        AsyncAccountClient,
        AsyncAccountClientConfig,
    )


class CommercialToGovCloudGatewayResource:
    def __init__(self, service: AccountClient) -> None:
        self._service = service

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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


class AsyncCommercialToGovCloudGatewayResource:
    def __init__(self, service: AsyncAccountClient) -> None:
        self._service = service

    async def get_gov_cloud_account_information(
        self,
        *,
        config_overrides: Optional[AsyncAccountClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_account.types.get_gov_cloud_account_information_request.GetGovCloudAccountInformationRequest]",
        ) -> AsyncOperationResponse[
            "capo_account.types.get_gov_cloud_account_information_response.GetGovCloudAccountInformationResponse"
        ]:
            import capo_account._operations.account.get_gov_cloud_account_information

            (
                output,
                http_response,
            ) = await capo_account._operations.account.get_gov_cloud_account_information.async_get_gov_cloud_account_information(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account.types.get_gov_cloud_account_information_request.GetGovCloudAccountInformationRequest = {}
        if standard_account_id is not None:
            input_["standard_account_id"] = standard_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
