from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_account_access._auth._signers
import capo_account_access._auth._sigv4
from capo_account_access._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_account_access.types.application_arn
    import capo_account_access.types.application_summary
    import capo_account_access.types.create_application_request
    import capo_account_access.types.create_application_response
    import capo_account_access.types.create_entitlement_request
    import capo_account_access.types.create_entitlement_response
    import capo_account_access.types.delete_application_request
    import capo_account_access.types.delete_application_response
    import capo_account_access.types.delete_entitlement_request
    import capo_account_access.types.delete_entitlement_response
    import capo_account_access.types.entitlement
    import capo_account_access.types.entitlement_filter
    import capo_account_access.types.entitlements_list_member
    import capo_account_access.types.get_application_request
    import capo_account_access.types.get_application_response
    import capo_account_access.types.get_entitlement_request
    import capo_account_access.types.get_entitlement_response
    import capo_account_access.types.identity_source
    import capo_account_access.types.list_applications_request
    import capo_account_access.types.list_applications_response
    import capo_account_access.types.list_entitlements_request
    import capo_account_access.types.list_entitlements_response
    import capo_account_access.types.tags_map
    from capo_account_access._services.account_access import (
        AccountAccessClient,
        AccountAccessClientConfig,
    )
    from capo_account_access._services.async_account_access import (
        AsyncAccountAccessClient,
        AsyncAccountAccessClientConfig,
    )


class Application:
    def __init__(self, service: AccountAccessClient) -> None:
        self._service = service

    def create(
        self,
        identity_source: "capo_account_access.types.identity_source.IdentitySource",
        *,
        config_overrides: Optional[AccountAccessClientConfig] = None,
        tags: Optional["capo_account_access.types.tags_map.TagsMap"] = None,
    ) -> "capo_account_access.types.create_application_response.CreateApplicationResponse":
        """<p>Creates an account access manager instance and its Amazon Web Services account access application in the associated IAM Identity Center instance. This operation is idempotent; calling it multiple times with the same parameters returns the existing application.</p>

        Args:
            identity_source: <p>Specifies the identity source for the application. The identity source defines the IAM Identity Center instance that provides principals for entitlements.</p>
            tags: <p>Specifies the tags to assign to the application.</p>

        Raises:
            capo_account_access.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this operation.</p>
            capo_account_access.errors.already_created_exception.AlreadyCreatedException: <p>The resource you are trying to create already exists. To retrieve the existing resource, use the corresponding Get operation.</p>
            capo_account_access.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account_access.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse[
            "capo_account_access.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_account_access._operations.aws_account_access.create_application

            output, http_response = (
                capo_account_access._operations.aws_account_access.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account_access.types.create_application_request.CreateApplicationRequest = {
            "identity_source": identity_source
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        application_arn: "capo_account_access.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[AccountAccessClientConfig] = None,
    ) -> "capo_account_access.types.get_application_response.GetApplicationResponse":
        """<p>Retrieves details about an account access manager application, including its status, identity source, and tags.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application to retrieve.</p>

        Raises:
            capo_account_access.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this operation.</p>
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify that the resource identifier is correct and that the resource exists in the current Region.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account_access.types.get_application_request.GetApplicationRequest]",
        ) -> OperationResponse[
            "capo_account_access.types.get_application_response.GetApplicationResponse"
        ]:
            import capo_account_access._operations.aws_account_access.get_application

            output, http_response = (
                capo_account_access._operations.aws_account_access.get_application.get_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account_access.types.get_application_request.GetApplicationRequest = {
            "application_arn": application_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        application_arn: "capo_account_access.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[AccountAccessClientConfig] = None,
    ) -> "capo_account_access.types.delete_application_response.DeleteApplicationResponse":
        """<p>Deletes an account access manager application. This operation is idempotent; deleting an application that has already been deleted does not return an error.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application to delete.</p>

        Raises:
            capo_account_access.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this operation.</p>
            capo_account_access.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify that the resource identifier is correct and that the resource exists in the current Region.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account_access.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[
            "capo_account_access.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_account_access._operations.aws_account_access.delete_application

            output, http_response = (
                capo_account_access._operations.aws_account_access.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account_access.types.delete_application_request.DeleteApplicationRequest = {
            "application_arn": application_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[AccountAccessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> (
        "capo_account_access.types.list_applications_response.ListApplicationsResponse"
    ):
        """<p>Lists the account access manager applications in your account. Use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>Specifies the maximum number of results to return in a single call.</p>
            next_token: <p>Specifies the pagination token from a previous call to retrieve the next set of results.</p>

        Raises:
            capo_account_access.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this operation.</p>
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account_access.types.list_applications_request.ListApplicationsRequest]",
        ) -> OperationResponse[
            "capo_account_access.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_account_access._operations.aws_account_access.list_applications

            output, http_response = (
                capo_account_access._operations.aws_account_access.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account_access.types.list_applications_request.ListApplicationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_entitlement(
        self,
        application_arn: "capo_account_access.types.application_arn.ApplicationArn",
        entitlement: "capo_account_access.types.entitlement.Entitlement",
        *,
        config_overrides: Optional[AccountAccessClientConfig] = None,
    ) -> "capo_account_access.types.create_entitlement_response.CreateEntitlementResponse":
        """<p>Creates an entitlement (assignment) in account access manager. An entitlement (assignment) grants a principal (IAM Identity Center user or group) permission to assume a specified IAM role in an Amazon Web Services account. This operation is idempotent.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application to create the entitlement for.</p>
            entitlement: <p>Specifies the entitlement configuration, including the principal and the IAM role to grant access to.</p>

        Raises:
            capo_account_access.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this operation.</p>
            capo_account_access.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify that the resource identifier is correct and that the resource exists in the current Region.</p>
            capo_account_access.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota for your account.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account_access.types.create_entitlement_request.CreateEntitlementRequest]",
        ) -> OperationResponse[
            "capo_account_access.types.create_entitlement_response.CreateEntitlementResponse"
        ]:
            import capo_account_access._operations.aws_account_access.create_entitlement

            output, http_response = (
                capo_account_access._operations.aws_account_access.create_entitlement.create_entitlement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account_access.types.create_entitlement_request.CreateEntitlementRequest = {
            "application_arn": application_arn,
            "entitlement": entitlement,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_entitlement(
        self,
        application_arn: "capo_account_access.types.application_arn.ApplicationArn",
        entitlement_id: str,
        *,
        config_overrides: Optional[AccountAccessClientConfig] = None,
    ) -> "capo_account_access.types.delete_entitlement_response.DeleteEntitlementResponse":
        """<p>Deletes an entitlement from an account access manager application. This operation is idempotent; deleting an entitlement that has already been deleted does not return an error.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application that the entitlement belongs to.</p>
            entitlement_id: <p>Specifies the unique identifier of the entitlement to delete.</p>

        Raises:
            capo_account_access.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this operation.</p>
            capo_account_access.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify that the resource identifier is correct and that the resource exists in the current Region.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account_access.types.delete_entitlement_request.DeleteEntitlementRequest]",
        ) -> OperationResponse[
            "capo_account_access.types.delete_entitlement_response.DeleteEntitlementResponse"
        ]:
            import capo_account_access._operations.aws_account_access.delete_entitlement

            output, http_response = (
                capo_account_access._operations.aws_account_access.delete_entitlement.delete_entitlement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account_access.types.delete_entitlement_request.DeleteEntitlementRequest = {
            "application_arn": application_arn,
            "entitlement_id": entitlement_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_entitlement(
        self,
        application_arn: "capo_account_access.types.application_arn.ApplicationArn",
        entitlement_id: str,
        *,
        config_overrides: Optional[AccountAccessClientConfig] = None,
    ) -> "capo_account_access.types.get_entitlement_response.GetEntitlementResponse":
        """<p>Retrieves details about a specific entitlement for an account access manager application, including the principal, IAM role, and target account.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application that the entitlement belongs to.</p>
            entitlement_id: <p>Specifies the unique identifier of the entitlement to retrieve.</p>

        Raises:
            capo_account_access.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this operation.</p>
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify that the resource identifier is correct and that the resource exists in the current Region.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account_access.types.get_entitlement_request.GetEntitlementRequest]",
        ) -> OperationResponse[
            "capo_account_access.types.get_entitlement_response.GetEntitlementResponse"
        ]:
            import capo_account_access._operations.aws_account_access.get_entitlement

            output, http_response = (
                capo_account_access._operations.aws_account_access.get_entitlement.get_entitlement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account_access.types.get_entitlement_request.GetEntitlementRequest = {
            "application_arn": application_arn,
            "entitlement_id": entitlement_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_entitlements(
        self,
        application_arn: "capo_account_access.types.application_arn.ApplicationArn",
        filter: "capo_account_access.types.entitlement_filter.EntitlementFilter",
        *,
        config_overrides: Optional[AccountAccessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> (
        "capo_account_access.types.list_entitlements_response.ListEntitlementsResponse"
    ):
        """<p>Lists the entitlements for a specified account access manager application. You can filter results by principal, IAM role, or account. Use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application to list entitlements for.</p>
            filter: <p>Specifies filter criteria to narrow the entitlements returned. You can filter by principal, IAM role, or account.</p>
            next_token: <p>Specifies the pagination token from a previous call to retrieve the next set of results.</p>
            max_results: <p>Specifies the maximum number of results to return in a single call.</p>

        Raises:
            capo_account_access.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this operation.</p>
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify that the resource identifier is correct and that the resource exists in the current Region.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account_access.types.list_entitlements_request.ListEntitlementsRequest]",
        ) -> OperationResponse[
            "capo_account_access.types.list_entitlements_response.ListEntitlementsResponse"
        ]:
            import capo_account_access._operations.aws_account_access.list_entitlements

            output, http_response = (
                capo_account_access._operations.aws_account_access.list_entitlements.list_entitlements(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account_access.types.list_entitlements_request.ListEntitlementsRequest = {
            "application_arn": application_arn,
            "filter": filter,
        }
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


class AsyncApplication:
    def __init__(self, service: AsyncAccountAccessClient) -> None:
        self._service = service

    async def create(
        self,
        identity_source: "capo_account_access.types.identity_source.IdentitySource",
        *,
        config_overrides: Optional[AsyncAccountAccessClientConfig] = None,
        tags: Optional["capo_account_access.types.tags_map.TagsMap"] = None,
    ) -> "capo_account_access.types.create_application_response.CreateApplicationResponse":
        """<p>Creates an account access manager instance and its Amazon Web Services account access application in the associated IAM Identity Center instance. This operation is idempotent; calling it multiple times with the same parameters returns the existing application.</p>

        Args:
            identity_source: <p>Specifies the identity source for the application. The identity source defines the IAM Identity Center instance that provides principals for entitlements.</p>
            tags: <p>Specifies the tags to assign to the application.</p>

        Raises:
            capo_account_access.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this operation.</p>
            capo_account_access.errors.already_created_exception.AlreadyCreatedException: <p>The resource you are trying to create already exists. To retrieve the existing resource, use the corresponding Get operation.</p>
            capo_account_access.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_account_access.types.create_application_request.CreateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_account_access.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_account_access._operations.aws_account_access.create_application

            (
                output,
                http_response,
            ) = await capo_account_access._operations.aws_account_access.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account_access.types.create_application_request.CreateApplicationRequest = {
            "identity_source": identity_source
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        application_arn: "capo_account_access.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[AsyncAccountAccessClientConfig] = None,
    ) -> "capo_account_access.types.get_application_response.GetApplicationResponse":
        """<p>Retrieves details about an account access manager application, including its status, identity source, and tags.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application to retrieve.</p>

        Raises:
            capo_account_access.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this operation.</p>
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify that the resource identifier is correct and that the resource exists in the current Region.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_account_access.types.get_application_request.GetApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_account_access.types.get_application_response.GetApplicationResponse"
        ]:
            import capo_account_access._operations.aws_account_access.get_application

            (
                output,
                http_response,
            ) = await capo_account_access._operations.aws_account_access.get_application.async_get_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account_access.types.get_application_request.GetApplicationRequest = {
            "application_arn": application_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        application_arn: "capo_account_access.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[AsyncAccountAccessClientConfig] = None,
    ) -> "capo_account_access.types.delete_application_response.DeleteApplicationResponse":
        """<p>Deletes an account access manager application. This operation is idempotent; deleting an application that has already been deleted does not return an error.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application to delete.</p>

        Raises:
            capo_account_access.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this operation.</p>
            capo_account_access.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify that the resource identifier is correct and that the resource exists in the current Region.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_account_access.types.delete_application_request.DeleteApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_account_access.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_account_access._operations.aws_account_access.delete_application

            (
                output,
                http_response,
            ) = await capo_account_access._operations.aws_account_access.delete_application.async_delete_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account_access.types.delete_application_request.DeleteApplicationRequest = {
            "application_arn": application_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncAccountAccessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> (
        "capo_account_access.types.list_applications_response.ListApplicationsResponse"
    ):
        """<p>Lists the account access manager applications in your account. Use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>Specifies the maximum number of results to return in a single call.</p>
            next_token: <p>Specifies the pagination token from a previous call to retrieve the next set of results.</p>

        Raises:
            capo_account_access.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this operation.</p>
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_account_access.types.list_applications_request.ListApplicationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_account_access.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_account_access._operations.aws_account_access.list_applications

            (
                output,
                http_response,
            ) = await capo_account_access._operations.aws_account_access.list_applications.async_list_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account_access.types.list_applications_request.ListApplicationsRequest = {}
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

    async def create_entitlement(
        self,
        application_arn: "capo_account_access.types.application_arn.ApplicationArn",
        entitlement: "capo_account_access.types.entitlement.Entitlement",
        *,
        config_overrides: Optional[AsyncAccountAccessClientConfig] = None,
    ) -> "capo_account_access.types.create_entitlement_response.CreateEntitlementResponse":
        """<p>Creates an entitlement (assignment) in account access manager. An entitlement (assignment) grants a principal (IAM Identity Center user or group) permission to assume a specified IAM role in an Amazon Web Services account. This operation is idempotent.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application to create the entitlement for.</p>
            entitlement: <p>Specifies the entitlement configuration, including the principal and the IAM role to grant access to.</p>

        Raises:
            capo_account_access.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this operation.</p>
            capo_account_access.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify that the resource identifier is correct and that the resource exists in the current Region.</p>
            capo_account_access.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota for your account.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_account_access.types.create_entitlement_request.CreateEntitlementRequest]",
        ) -> AsyncOperationResponse[
            "capo_account_access.types.create_entitlement_response.CreateEntitlementResponse"
        ]:
            import capo_account_access._operations.aws_account_access.create_entitlement

            (
                output,
                http_response,
            ) = await capo_account_access._operations.aws_account_access.create_entitlement.async_create_entitlement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account_access.types.create_entitlement_request.CreateEntitlementRequest = {
            "application_arn": application_arn,
            "entitlement": entitlement,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_entitlement(
        self,
        application_arn: "capo_account_access.types.application_arn.ApplicationArn",
        entitlement_id: str,
        *,
        config_overrides: Optional[AsyncAccountAccessClientConfig] = None,
    ) -> "capo_account_access.types.delete_entitlement_response.DeleteEntitlementResponse":
        """<p>Deletes an entitlement from an account access manager application. This operation is idempotent; deleting an entitlement that has already been deleted does not return an error.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application that the entitlement belongs to.</p>
            entitlement_id: <p>Specifies the unique identifier of the entitlement to delete.</p>

        Raises:
            capo_account_access.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this operation.</p>
            capo_account_access.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify that the resource identifier is correct and that the resource exists in the current Region.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_account_access.types.delete_entitlement_request.DeleteEntitlementRequest]",
        ) -> AsyncOperationResponse[
            "capo_account_access.types.delete_entitlement_response.DeleteEntitlementResponse"
        ]:
            import capo_account_access._operations.aws_account_access.delete_entitlement

            (
                output,
                http_response,
            ) = await capo_account_access._operations.aws_account_access.delete_entitlement.async_delete_entitlement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account_access.types.delete_entitlement_request.DeleteEntitlementRequest = {
            "application_arn": application_arn,
            "entitlement_id": entitlement_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_entitlement(
        self,
        application_arn: "capo_account_access.types.application_arn.ApplicationArn",
        entitlement_id: str,
        *,
        config_overrides: Optional[AsyncAccountAccessClientConfig] = None,
    ) -> "capo_account_access.types.get_entitlement_response.GetEntitlementResponse":
        """<p>Retrieves details about a specific entitlement for an account access manager application, including the principal, IAM role, and target account.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application that the entitlement belongs to.</p>
            entitlement_id: <p>Specifies the unique identifier of the entitlement to retrieve.</p>

        Raises:
            capo_account_access.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this operation.</p>
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify that the resource identifier is correct and that the resource exists in the current Region.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_account_access.types.get_entitlement_request.GetEntitlementRequest]",
        ) -> AsyncOperationResponse[
            "capo_account_access.types.get_entitlement_response.GetEntitlementResponse"
        ]:
            import capo_account_access._operations.aws_account_access.get_entitlement

            (
                output,
                http_response,
            ) = await capo_account_access._operations.aws_account_access.get_entitlement.async_get_entitlement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account_access.types.get_entitlement_request.GetEntitlementRequest = {
            "application_arn": application_arn,
            "entitlement_id": entitlement_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_entitlements(
        self,
        application_arn: "capo_account_access.types.application_arn.ApplicationArn",
        filter: "capo_account_access.types.entitlement_filter.EntitlementFilter",
        *,
        config_overrides: Optional[AsyncAccountAccessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> (
        "capo_account_access.types.list_entitlements_response.ListEntitlementsResponse"
    ):
        """<p>Lists the entitlements for a specified account access manager application. You can filter results by principal, IAM role, or account. Use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application to list entitlements for.</p>
            filter: <p>Specifies filter criteria to narrow the entitlements returned. You can filter by principal, IAM role, or account.</p>
            next_token: <p>Specifies the pagination token from a previous call to retrieve the next set of results.</p>
            max_results: <p>Specifies the maximum number of results to return in a single call.</p>

        Raises:
            capo_account_access.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this operation.</p>
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify that the resource identifier is correct and that the resource exists in the current Region.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_account_access.types.list_entitlements_request.ListEntitlementsRequest]",
        ) -> AsyncOperationResponse[
            "capo_account_access.types.list_entitlements_response.ListEntitlementsResponse"
        ]:
            import capo_account_access._operations.aws_account_access.list_entitlements

            (
                output,
                http_response,
            ) = await capo_account_access._operations.aws_account_access.list_entitlements.async_list_entitlements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_account_access.types.list_entitlements_request.ListEntitlementsRequest = {
            "application_arn": application_arn,
            "filter": filter,
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
