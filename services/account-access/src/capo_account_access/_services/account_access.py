"""Generated from Smithy shape ``com.amazonaws.accountaccess#AWSAccountAccess``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_account_access._auth._signers
import capo_account_access._auth._sigv4
from capo_account_access._auth._identity import Credentials
from capo_account_access._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_account_access._auth._zapros_handler import AuthMiddleware
from capo_account_access._pagination import resolve_path as _resolve_path
from capo_account_access._resources.aws_account_access.application import Application
from capo_account_access._services._aws_config import aws_config
from capo_account_access._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
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
    import capo_account_access.types.list_tags_for_resource_request
    import capo_account_access.types.list_tags_for_resource_response
    import capo_account_access.types.tag_keys
    import capo_account_access.types.tag_resource_request
    import capo_account_access.types.tag_resource_response
    import capo_account_access.types.tags_map
    import capo_account_access.types.untag_resource_request
    import capo_account_access.types.untag_resource_response


class AccountAccessClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AccountAccessClient:
    """A client for the ``AccountAccess`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
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
        self._config = AccountAccessClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.application = Application(self)

    def operation_options(
        self, config_overrides: Optional[AccountAccessClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: AccountAccessClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: "capo_account_access.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[AccountAccessClientConfig] = None,
    ) -> "capo_account_access.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags associated with an account access manager resource.</p>

        Args:
            resource_arn: <p>Specifies the ARN of the resource to list tags for.</p>

        Raises:
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify that the resource identifier is correct and that the resource exists in the current Region.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account_access.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_account_access.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_account_access._operations.aws_account_access.list_tags_for_resource

            output, http_response = (
                capo_account_access._operations.aws_account_access.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account_access.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_account_access.types.application_arn.ApplicationArn",
        tags: "capo_account_access.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AccountAccessClientConfig] = None,
    ) -> "capo_account_access.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to an account access manager resource.</p>

        Args:
            resource_arn: <p>Specifies the ARN of the resource to add tags to.</p>
            tags: <p>Specifies the tags to add to the resource.</p>

        Raises:
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify that the resource identifier is correct and that the resource exists in the current Region.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account_access.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_account_access.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_account_access._operations.aws_account_access.tag_resource

            output, http_response = (
                capo_account_access._operations.aws_account_access.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account_access.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_account_access.types.application_arn.ApplicationArn",
        tag_keys: "capo_account_access.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AccountAccessClientConfig] = None,
    ) -> "capo_account_access.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from an account access manager resource.</p>

        Args:
            resource_arn: <p>Specifies the ARN of the resource to remove tags from.</p>
            tag_keys: <p>Specifies the tag keys to remove from the resource.</p>

        Raises:
            capo_account_access.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try your request again later.</p>
            capo_account_access.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify that the resource identifier is correct and that the resource exists in the current Region.</p>
            capo_account_access.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Try your request again later.</p>
            capo_account_access.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.</p>
            capo_account_access.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_account_access.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_account_access.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_account_access._operations.aws_account_access.untag_resource

            output, http_response = (
                capo_account_access._operations.aws_account_access.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_account_access.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_application(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def get_application(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def delete_application(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def list_applications(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def iter_list_applications(
        self,
        *,
        config_overrides: Optional[AccountAccessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_account_access.types.application_summary.ApplicationSummary]":
        _token = next_token
        while True:
            _response = self.list_applications(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("applications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def iter_list_entitlements(
        self,
        application_arn: "capo_account_access.types.application_arn.ApplicationArn",
        filter: "capo_account_access.types.entitlement_filter.EntitlementFilter",
        *,
        config_overrides: Optional[AccountAccessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_account_access.types.entitlements_list_member.EntitlementsListMember]":
        _token = next_token
        while True:
            _response = self.list_entitlements(
                application_arn,
                filter,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("entitlements",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
