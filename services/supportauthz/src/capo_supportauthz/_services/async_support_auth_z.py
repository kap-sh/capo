"""Generated from Smithy shape ``com.amazonaws.supportauthz#SupportAuthZ``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_supportauthz._auth._signers
import capo_supportauthz._auth._sigv4
from capo_supportauthz._auth._identity import Credentials
from capo_supportauthz._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_supportauthz._auth._zapros_handler import AuthMiddleware
from capo_supportauthz._pagination import resolve_path as _resolve_path
from capo_supportauthz._services._aws_config import aaws_config
from capo_supportauthz._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_supportauthz.types.action
    import capo_supportauthz.types.action_summary
    import capo_supportauthz.types.arn
    import capo_supportauthz.types.client_token
    import capo_supportauthz.types.create_support_permit_input
    import capo_supportauthz.types.create_support_permit_output
    import capo_supportauthz.types.delete_support_permit_input
    import capo_supportauthz.types.delete_support_permit_output
    import capo_supportauthz.types.description
    import capo_supportauthz.types.get_action_input
    import capo_supportauthz.types.get_action_output
    import capo_supportauthz.types.get_support_permit_input
    import capo_supportauthz.types.get_support_permit_output
    import capo_supportauthz.types.list_actions_input
    import capo_supportauthz.types.list_actions_output
    import capo_supportauthz.types.list_support_permit_requests_input
    import capo_supportauthz.types.list_support_permit_requests_output
    import capo_supportauthz.types.list_support_permits_input
    import capo_supportauthz.types.list_support_permits_output
    import capo_supportauthz.types.list_tags_for_resource_input
    import capo_supportauthz.types.list_tags_for_resource_output
    import capo_supportauthz.types.max_results
    import capo_supportauthz.types.name
    import capo_supportauthz.types.next_token
    import capo_supportauthz.types.permit
    import capo_supportauthz.types.reject_support_permit_request_input
    import capo_supportauthz.types.reject_support_permit_request_output
    import capo_supportauthz.types.request_arn
    import capo_supportauthz.types.service
    import capo_supportauthz.types.signing_key_info
    import capo_supportauthz.types.support_case_display_id
    import capo_supportauthz.types.support_permit_identifier
    import capo_supportauthz.types.support_permit_request
    import capo_supportauthz.types.support_permit_statuses
    import capo_supportauthz.types.support_permit_summary
    import capo_supportauthz.types.tag_key_list
    import capo_supportauthz.types.tag_resource_input
    import capo_supportauthz.types.tag_resource_output
    import capo_supportauthz.types.tags
    import capo_supportauthz.types.untag_resource_input
    import capo_supportauthz.types.untag_resource_output


class AsyncSupportAuthZClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncSupportAuthZClient:
    """A client for the ``SupportAuthZ`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
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
        self._config = AsyncSupportAuthZClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncSupportAuthZClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSupportAuthZClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def create_support_permit(
        self,
        permit: "capo_supportauthz.types.permit.Permit",
        name: "capo_supportauthz.types.name.Name",
        signing_key_info: "capo_supportauthz.types.signing_key_info.SigningKeyInfo",
        *,
        config_overrides: Optional[AsyncSupportAuthZClientConfig] = None,
        description: Optional["capo_supportauthz.types.description.Description"] = None,
        support_case_display_id: Optional[
            "capo_supportauthz.types.support_case_display_id.SupportCaseDisplayId"
        ] = None,
        client_token: Optional[
            "capo_supportauthz.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_supportauthz.types.tags.Tags"] = None,
    ) -> (
        "capo_supportauthz.types.create_support_permit_output.CreateSupportPermitOutput"
    ):
        """<p>Creates a support permit that authorizes an AWS support operator to perform specified actions on specified resources. The permit is cryptographically signed using a customer-managed AWS KMS key (ECC_NIST_P384, SIGN_VERIFY) to ensure non-repudiation.</p>

        Args:
            permit: <p>The permit definition specifying the actions, resources, and time-window conditions that the support operator is authorized to use.</p>
            name: <p>A customer-chosen name for the support permit. Must be between 1 and 256 alphanumeric characters.</p>
            description: <p>A human-readable description of why this permit is being created. Maximum length of 1024 characters.</p>
            signing_key_info: <p>The signing key information used to sign the permit. Must reference an AWS KMS key with key usage SIGN_VERIFY and key spec ECC_NIST_P384.</p>
            support_case_display_id: <p>The display identifier of the AWS Support case associated with this permit.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service returns the existing permit without creating a duplicate.</p>
            tags: <p>The tags to associate with the support permit on creation.</p>

        Raises:
            capo_supportauthz.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this operation.</p>
            capo_supportauthz.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_supportauthz.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try again later.</p>
            capo_supportauthz.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota for your account.</p>
            capo_supportauthz.errors.throttling_exception.ThrottlingException: <p>The request rate exceeded the allowed limit. Try again later.</p>
            capo_supportauthz.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_supportauthz.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supportauthz.types.create_support_permit_input.CreateSupportPermitInput]",
        ) -> AsyncOperationResponse[
            "capo_supportauthz.types.create_support_permit_output.CreateSupportPermitOutput"
        ]:
            import capo_supportauthz._operations.support_auth_z.create_support_permit

            (
                output,
                http_response,
            ) = await capo_supportauthz._operations.support_auth_z.create_support_permit.async_create_support_permit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supportauthz.types.create_support_permit_input.CreateSupportPermitInput = {
            "permit": permit,
            "name": name,
            "signing_key_info": signing_key_info,
        }
        if description is not None:
            input_["description"] = description
        if support_case_display_id is not None:
            input_["support_case_display_id"] = support_case_display_id
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_support_permit(
        self,
        support_permit_identifier: "capo_supportauthz.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncSupportAuthZClientConfig] = None,
    ) -> (
        "capo_supportauthz.types.delete_support_permit_output.DeleteSupportPermitOutput"
    ):
        """<p>Deletes a support permit, revoking the authorization previously granted to the AWS support operator.</p>

        Args:
            support_permit_identifier: <p>The Amazon Resource Name (ARN) or name of the support permit to delete.</p>

        Raises:
            capo_supportauthz.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this operation.</p>
            capo_supportauthz.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try again later.</p>
            capo_supportauthz.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_supportauthz.errors.throttling_exception.ThrottlingException: <p>The request rate exceeded the allowed limit. Try again later.</p>
            capo_supportauthz.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_supportauthz.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supportauthz.types.delete_support_permit_input.DeleteSupportPermitInput]",
        ) -> AsyncOperationResponse[
            "capo_supportauthz.types.delete_support_permit_output.DeleteSupportPermitOutput"
        ]:
            import capo_supportauthz._operations.support_auth_z.delete_support_permit

            (
                output,
                http_response,
            ) = await capo_supportauthz._operations.support_auth_z.delete_support_permit.async_delete_support_permit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supportauthz.types.delete_support_permit_input.DeleteSupportPermitInput = {
            "support_permit_identifier": support_permit_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_action(
        self,
        action: "capo_supportauthz.types.action.Action",
        *,
        config_overrides: Optional[AsyncSupportAuthZClientConfig] = None,
    ) -> "capo_supportauthz.types.get_action_output.GetActionOutput":
        """<p>Retrieves the description of a specific support action.</p>

        Args:
            action: <p>The name of the support action to retrieve.</p>

        Raises:
            capo_supportauthz.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this operation.</p>
            capo_supportauthz.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try again later.</p>
            capo_supportauthz.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_supportauthz.errors.throttling_exception.ThrottlingException: <p>The request rate exceeded the allowed limit. Try again later.</p>
            capo_supportauthz.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_supportauthz.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supportauthz.types.get_action_input.GetActionInput]",
        ) -> AsyncOperationResponse[
            "capo_supportauthz.types.get_action_output.GetActionOutput"
        ]:
            import capo_supportauthz._operations.support_auth_z.get_action

            (
                output,
                http_response,
            ) = await capo_supportauthz._operations.support_auth_z.get_action.async_get_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supportauthz.types.get_action_input.GetActionInput = {
            "action": action
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_support_permit(
        self,
        support_permit_identifier: "capo_supportauthz.types.support_permit_identifier.SupportPermitIdentifier",
        *,
        config_overrides: Optional[AsyncSupportAuthZClientConfig] = None,
    ) -> "capo_supportauthz.types.get_support_permit_output.GetSupportPermitOutput":
        """<p>Retrieves the details of a support permit by its ARN or name.</p>

        Args:
            support_permit_identifier: <p>The ARN or name of the support permit to retrieve.</p>

        Raises:
            capo_supportauthz.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this operation.</p>
            capo_supportauthz.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try again later.</p>
            capo_supportauthz.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_supportauthz.errors.throttling_exception.ThrottlingException: <p>The request rate exceeded the allowed limit. Try again later.</p>
            capo_supportauthz.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_supportauthz.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supportauthz.types.get_support_permit_input.GetSupportPermitInput]",
        ) -> AsyncOperationResponse[
            "capo_supportauthz.types.get_support_permit_output.GetSupportPermitOutput"
        ]:
            import capo_supportauthz._operations.support_auth_z.get_support_permit

            (
                output,
                http_response,
            ) = await capo_supportauthz._operations.support_auth_z.get_support_permit.async_get_support_permit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supportauthz.types.get_support_permit_input.GetSupportPermitInput = {
            "support_permit_identifier": support_permit_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_actions(
        self,
        service: "capo_supportauthz.types.service.Service",
        *,
        config_overrides: Optional[AsyncSupportAuthZClientConfig] = None,
        next_token: Optional["capo_supportauthz.types.next_token.NextToken"] = None,
        max_results: Optional["capo_supportauthz.types.max_results.MaxResults"] = None,
    ) -> "capo_supportauthz.types.list_actions_output.ListActionsOutput":
        """<p>Lists available support actions for a specified AWS service. Use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call. Valid range is 1 to 100.</p>
            service: <p>The name of the AWS service for which to list available support actions.</p>

        Raises:
            capo_supportauthz.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this operation.</p>
            capo_supportauthz.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try again later.</p>
            capo_supportauthz.errors.throttling_exception.ThrottlingException: <p>The request rate exceeded the allowed limit. Try again later.</p>
            capo_supportauthz.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_supportauthz.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supportauthz.types.list_actions_input.ListActionsInput]",
        ) -> AsyncOperationResponse[
            "capo_supportauthz.types.list_actions_output.ListActionsOutput"
        ]:
            import capo_supportauthz._operations.support_auth_z.list_actions

            (
                output,
                http_response,
            ) = await capo_supportauthz._operations.support_auth_z.list_actions.async_list_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supportauthz.types.list_actions_input.ListActionsInput = {
            "service": service
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

    async def iter_list_actions(
        self,
        service: "capo_supportauthz.types.service.Service",
        *,
        config_overrides: Optional[AsyncSupportAuthZClientConfig] = None,
        next_token: Optional["capo_supportauthz.types.next_token.NextToken"] = None,
        max_results: Optional["capo_supportauthz.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_supportauthz.types.action_summary.ActionSummary]":
        _token = next_token
        while True:
            _response = await self.list_actions(
                service,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("action_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_support_permit_requests(
        self,
        *,
        config_overrides: Optional[AsyncSupportAuthZClientConfig] = None,
        next_token: Optional["capo_supportauthz.types.next_token.NextToken"] = None,
        max_results: Optional["capo_supportauthz.types.max_results.MaxResults"] = None,
        support_case_display_id: Optional[
            "capo_supportauthz.types.support_case_display_id.SupportCaseDisplayId"
        ] = None,
    ) -> "capo_supportauthz.types.list_support_permit_requests_output.ListSupportPermitRequestsOutput":
        """<p>Lists permit requests from AWS support operators. Use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call. Valid range is 1 to 100.</p>
            support_case_display_id: <p>Filters the results by support case display identifier.</p>

        Raises:
            capo_supportauthz.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this operation.</p>
            capo_supportauthz.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try again later.</p>
            capo_supportauthz.errors.throttling_exception.ThrottlingException: <p>The request rate exceeded the allowed limit. Try again later.</p>
            capo_supportauthz.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_supportauthz.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supportauthz.types.list_support_permit_requests_input.ListSupportPermitRequestsInput]",
        ) -> AsyncOperationResponse[
            "capo_supportauthz.types.list_support_permit_requests_output.ListSupportPermitRequestsOutput"
        ]:
            import capo_supportauthz._operations.support_auth_z.list_support_permit_requests

            (
                output,
                http_response,
            ) = await capo_supportauthz._operations.support_auth_z.list_support_permit_requests.async_list_support_permit_requests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supportauthz.types.list_support_permit_requests_input.ListSupportPermitRequestsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if support_case_display_id is not None:
            input_["support_case_display_id"] = support_case_display_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_support_permit_requests(
        self,
        *,
        config_overrides: Optional[AsyncSupportAuthZClientConfig] = None,
        next_token: Optional["capo_supportauthz.types.next_token.NextToken"] = None,
        max_results: Optional["capo_supportauthz.types.max_results.MaxResults"] = None,
        support_case_display_id: Optional[
            "capo_supportauthz.types.support_case_display_id.SupportCaseDisplayId"
        ] = None,
    ) -> "AsyncIterator[capo_supportauthz.types.support_permit_request.SupportPermitRequest]":
        _token = next_token
        while True:
            _response = await self.list_support_permit_requests(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                support_case_display_id=support_case_display_id,
            )
            _page = _resolve_path(_response, ("support_permit_requests",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_support_permits(
        self,
        *,
        config_overrides: Optional[AsyncSupportAuthZClientConfig] = None,
        next_token: Optional["capo_supportauthz.types.next_token.NextToken"] = None,
        max_results: Optional["capo_supportauthz.types.max_results.MaxResults"] = None,
        support_permit_statuses: Optional[
            "capo_supportauthz.types.support_permit_statuses.SupportPermitStatuses"
        ] = None,
    ) -> "capo_supportauthz.types.list_support_permits_output.ListSupportPermitsOutput":
        """<p>Lists all support permits in the caller's account. Use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call. Valid range is 1 to 100.</p>
            support_permit_statuses: <p>Filters the results by support permit status. Valid values: ACTIVE, INACTIVE, DELETING.</p>

        Raises:
            capo_supportauthz.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this operation.</p>
            capo_supportauthz.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try again later.</p>
            capo_supportauthz.errors.throttling_exception.ThrottlingException: <p>The request rate exceeded the allowed limit. Try again later.</p>
            capo_supportauthz.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_supportauthz.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supportauthz.types.list_support_permits_input.ListSupportPermitsInput]",
        ) -> AsyncOperationResponse[
            "capo_supportauthz.types.list_support_permits_output.ListSupportPermitsOutput"
        ]:
            import capo_supportauthz._operations.support_auth_z.list_support_permits

            (
                output,
                http_response,
            ) = await capo_supportauthz._operations.support_auth_z.list_support_permits.async_list_support_permits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supportauthz.types.list_support_permits_input.ListSupportPermitsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if support_permit_statuses is not None:
            input_["support_permit_statuses"] = support_permit_statuses

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_support_permits(
        self,
        *,
        config_overrides: Optional[AsyncSupportAuthZClientConfig] = None,
        next_token: Optional["capo_supportauthz.types.next_token.NextToken"] = None,
        max_results: Optional["capo_supportauthz.types.max_results.MaxResults"] = None,
        support_permit_statuses: Optional[
            "capo_supportauthz.types.support_permit_statuses.SupportPermitStatuses"
        ] = None,
    ) -> "AsyncIterator[capo_supportauthz.types.support_permit_summary.SupportPermitSummary]":
        _token = next_token
        while True:
            _response = await self.list_support_permits(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                support_permit_statuses=support_permit_statuses,
            )
            _page = _resolve_path(_response, ("support_permits",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_supportauthz.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncSupportAuthZClientConfig] = None,
    ) -> "capo_supportauthz.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the tags associated with a support permit resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to list tags for.</p>

        Raises:
            capo_supportauthz.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this operation.</p>
            capo_supportauthz.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try again later.</p>
            capo_supportauthz.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_supportauthz.errors.throttling_exception.ThrottlingException: <p>The request rate exceeded the allowed limit. Try again later.</p>
            capo_supportauthz.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_supportauthz.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supportauthz.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_supportauthz.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_supportauthz._operations.support_auth_z.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_supportauthz._operations.support_auth_z.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supportauthz.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reject_support_permit_request(
        self,
        request_arn: "capo_supportauthz.types.request_arn.RequestArn",
        *,
        config_overrides: Optional[AsyncSupportAuthZClientConfig] = None,
    ) -> "capo_supportauthz.types.reject_support_permit_request_output.RejectSupportPermitRequestOutput":
        """<p>Rejects a permit request from an AWS support operator. The operator cannot proceed with the requested action.</p>

        Args:
            request_arn: <p>The ARN of the permit request to reject.</p>

        Raises:
            capo_supportauthz.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this operation.</p>
            capo_supportauthz.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_supportauthz.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try again later.</p>
            capo_supportauthz.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_supportauthz.errors.throttling_exception.ThrottlingException: <p>The request rate exceeded the allowed limit. Try again later.</p>
            capo_supportauthz.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_supportauthz.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supportauthz.types.reject_support_permit_request_input.RejectSupportPermitRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_supportauthz.types.reject_support_permit_request_output.RejectSupportPermitRequestOutput"
        ]:
            import capo_supportauthz._operations.support_auth_z.reject_support_permit_request

            (
                output,
                http_response,
            ) = await capo_supportauthz._operations.support_auth_z.reject_support_permit_request.async_reject_support_permit_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supportauthz.types.reject_support_permit_request_input.RejectSupportPermitRequestInput = {
            "request_arn": request_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_supportauthz.types.arn.Arn",
        tags: "capo_supportauthz.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncSupportAuthZClientConfig] = None,
    ) -> "capo_supportauthz.types.tag_resource_output.TagResourceOutput":
        """<p>Adds or overwrites one or more tags for a support permit resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to tag.</p>
            tags: <p>The tags to add to the resource. Maximum of 50 tags.</p>

        Raises:
            capo_supportauthz.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this operation.</p>
            capo_supportauthz.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try again later.</p>
            capo_supportauthz.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_supportauthz.errors.throttling_exception.ThrottlingException: <p>The request rate exceeded the allowed limit. Try again later.</p>
            capo_supportauthz.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_supportauthz.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supportauthz.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_supportauthz.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_supportauthz._operations.support_auth_z.tag_resource

            (
                output,
                http_response,
            ) = await capo_supportauthz._operations.support_auth_z.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supportauthz.types.tag_resource_input.TagResourceInput = {
            "resource_arn": resource_arn,
            "tags": tags,
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
        resource_arn: "capo_supportauthz.types.arn.Arn",
        tag_keys: "capo_supportauthz.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncSupportAuthZClientConfig] = None,
    ) -> "capo_supportauthz.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes one or more tags from a support permit resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to untag.</p>
            tag_keys: <p>The tag keys to remove from the resource.</p>

        Raises:
            capo_supportauthz.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this operation.</p>
            capo_supportauthz.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Try again later.</p>
            capo_supportauthz.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_supportauthz.errors.throttling_exception.ThrottlingException: <p>The request rate exceeded the allowed limit. Try again later.</p>
            capo_supportauthz.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_supportauthz.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supportauthz.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_supportauthz.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_supportauthz._operations.support_auth_z.untag_resource

            (
                output,
                http_response,
            ) = await capo_supportauthz._operations.support_auth_z.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supportauthz.types.untag_resource_input.UntagResourceInput = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
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
