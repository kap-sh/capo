"""Generated from Smithy shape ``com.amazonaws.sso#SWBPortalService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_sso._auth._signers
import capo_sso._auth._sigv4
from capo_sso._auth._identity import Credentials
from capo_sso._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_sso._auth._zapros_handler import AuthMiddleware
from capo_sso._pagination import resolve_path as _resolve_path
from capo_sso._services._aws_config import aws_config
from capo_sso._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_sso.types.access_token_type
    import capo_sso.types.account_id_type
    import capo_sso.types.account_info
    import capo_sso.types.get_role_credentials_request
    import capo_sso.types.get_role_credentials_response
    import capo_sso.types.list_account_roles_request
    import capo_sso.types.list_account_roles_response
    import capo_sso.types.list_accounts_request
    import capo_sso.types.list_accounts_response
    import capo_sso.types.logout_request
    import capo_sso.types.max_result_type
    import capo_sso.types.next_token_type
    import capo_sso.types.role_info
    import capo_sso.types.role_name_type


class SSOClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class SSOClient:
    """A client for the ``SSO`` service.

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
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = SSOClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[SSOClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SSOClientConfig = config_overrides or {}
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
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def get_role_credentials(
        self,
        role_name: "capo_sso.types.role_name_type.RoleNameType",
        account_id: "capo_sso.types.account_id_type.AccountIdType",
        access_token: "capo_sso.types.access_token_type.AccessTokenType",
        *,
        config_overrides: Optional[SSOClientConfig] = None,
    ) -> "capo_sso.types.get_role_credentials_response.GetRoleCredentialsResponse":
        """<p>Returns the STS short-term credentials for a given role name that is assigned to the user.</p>

        Args:
            role_name: <p>The friendly name of the role that is assigned to the user.</p>
            account_id: <p>The identifier for the AWS account that is assigned to the user.</p>
            access_token: <p>The token issued by the <code>CreateToken</code> API call. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html">CreateToken</a> in the <i>IAM Identity Center OIDC API Reference Guide</i>.</p>

        Raises:
            capo_sso.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that a problem occurred with the input to the request. For example, a required parameter might be missing or out of range.</p>
            capo_sso.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_sso.errors.too_many_requests_exception.TooManyRequestsException: <p>Indicates that the request is being made too frequently and is more than what the server can handle.</p>
            capo_sso.errors.unauthorized_exception.UnauthorizedException: <p>Indicates that the request is not authorized. This can happen due to an invalid access token in the request.</p>
            capo_sso.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sso.types.get_role_credentials_request.GetRoleCredentialsRequest]",
        ) -> OperationResponse[
            "capo_sso.types.get_role_credentials_response.GetRoleCredentialsResponse"
        ]:
            import capo_sso._operations.swb_portal_service.get_role_credentials

            output, http_response = (
                capo_sso._operations.swb_portal_service.get_role_credentials.get_role_credentials(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sso.types.get_role_credentials_request.GetRoleCredentialsRequest = {
            "role_name": role_name,
            "account_id": account_id,
            "access_token": access_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_account_roles(
        self,
        access_token: "capo_sso.types.access_token_type.AccessTokenType",
        account_id: "capo_sso.types.account_id_type.AccountIdType",
        *,
        config_overrides: Optional[SSOClientConfig] = None,
        next_token: Optional["capo_sso.types.next_token_type.NextTokenType"] = None,
        max_results: Optional["capo_sso.types.max_result_type.MaxResultType"] = None,
    ) -> "capo_sso.types.list_account_roles_response.ListAccountRolesResponse":
        """<p>Lists all roles that are assigned to the user for a given AWS account.</p>

        Args:
            next_token: <p>The page token from the previous response output when you request subsequent pages.</p>
            max_results: <p>The number of items that clients can request per page.</p>
            access_token: <p>The token issued by the <code>CreateToken</code> API call. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html">CreateToken</a> in the <i>IAM Identity Center OIDC API Reference Guide</i>.</p>
            account_id: <p>The identifier for the AWS account that is assigned to the user.</p>

        Raises:
            capo_sso.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that a problem occurred with the input to the request. For example, a required parameter might be missing or out of range.</p>
            capo_sso.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_sso.errors.too_many_requests_exception.TooManyRequestsException: <p>Indicates that the request is being made too frequently and is more than what the server can handle.</p>
            capo_sso.errors.unauthorized_exception.UnauthorizedException: <p>Indicates that the request is not authorized. This can happen due to an invalid access token in the request.</p>
            capo_sso.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sso.types.list_account_roles_request.ListAccountRolesRequest]",
        ) -> OperationResponse[
            "capo_sso.types.list_account_roles_response.ListAccountRolesResponse"
        ]:
            import capo_sso._operations.swb_portal_service.list_account_roles

            output, http_response = (
                capo_sso._operations.swb_portal_service.list_account_roles.list_account_roles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sso.types.list_account_roles_request.ListAccountRolesRequest = {
            "access_token": access_token,
            "account_id": account_id,
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

    def iter_list_account_roles(
        self,
        access_token: "capo_sso.types.access_token_type.AccessTokenType",
        account_id: "capo_sso.types.account_id_type.AccountIdType",
        *,
        config_overrides: Optional[SSOClientConfig] = None,
        next_token: Optional["capo_sso.types.next_token_type.NextTokenType"] = None,
        max_results: Optional["capo_sso.types.max_result_type.MaxResultType"] = None,
    ) -> "Iterator[capo_sso.types.role_info.RoleInfo]":
        _token = next_token
        while True:
            _response = self.list_account_roles(
                access_token,
                account_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("role_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_accounts(
        self,
        access_token: "capo_sso.types.access_token_type.AccessTokenType",
        *,
        config_overrides: Optional[SSOClientConfig] = None,
        next_token: Optional["capo_sso.types.next_token_type.NextTokenType"] = None,
        max_results: Optional["capo_sso.types.max_result_type.MaxResultType"] = None,
    ) -> "capo_sso.types.list_accounts_response.ListAccountsResponse":
        """<p>Lists all AWS accounts assigned to the user. These AWS accounts are assigned by the administrator of the account. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/useraccess.html#assignusers">Assign User Access</a> in the <i>IAM Identity Center User Guide</i>. This operation returns a paginated response.</p>

        Args:
            next_token: <p>(Optional) When requesting subsequent pages, this is the page token from the previous response output.</p>
            max_results: <p>This is the number of items clients can request per page.</p>
            access_token: <p>The token issued by the <code>CreateToken</code> API call. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html">CreateToken</a> in the <i>IAM Identity Center OIDC API Reference Guide</i>.</p>

        Raises:
            capo_sso.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that a problem occurred with the input to the request. For example, a required parameter might be missing or out of range.</p>
            capo_sso.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_sso.errors.too_many_requests_exception.TooManyRequestsException: <p>Indicates that the request is being made too frequently and is more than what the server can handle.</p>
            capo_sso.errors.unauthorized_exception.UnauthorizedException: <p>Indicates that the request is not authorized. This can happen due to an invalid access token in the request.</p>
            capo_sso.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sso.types.list_accounts_request.ListAccountsRequest]",
        ) -> OperationResponse[
            "capo_sso.types.list_accounts_response.ListAccountsResponse"
        ]:
            import capo_sso._operations.swb_portal_service.list_accounts

            output, http_response = (
                capo_sso._operations.swb_portal_service.list_accounts.list_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sso.types.list_accounts_request.ListAccountsRequest = {
            "access_token": access_token
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

    def iter_list_accounts(
        self,
        access_token: "capo_sso.types.access_token_type.AccessTokenType",
        *,
        config_overrides: Optional[SSOClientConfig] = None,
        next_token: Optional["capo_sso.types.next_token_type.NextTokenType"] = None,
        max_results: Optional["capo_sso.types.max_result_type.MaxResultType"] = None,
    ) -> "Iterator[capo_sso.types.account_info.AccountInfo]":
        _token = next_token
        while True:
            _response = self.list_accounts(
                access_token,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("account_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def logout(
        self,
        access_token: "capo_sso.types.access_token_type.AccessTokenType",
        *,
        config_overrides: Optional[SSOClientConfig] = None,
    ) -> None:
        """<p>Removes the locally stored SSO tokens from the client-side cache and sends an API call to the IAM Identity Center service to invalidate the corresponding server-side IAM Identity Center sign in session.</p> <note> <p>If a user uses IAM Identity Center to access the AWS CLI, the user’s IAM Identity Center sign in session is used to obtain an IAM session, as specified in the corresponding IAM Identity Center permission set. More specifically, IAM Identity Center assumes an IAM role in the target account on behalf of the user, and the corresponding temporary AWS credentials are returned to the client.</p> <p>After user logout, any existing IAM role sessions that were created by using IAM Identity Center permission sets continue based on the duration configured in the permission set. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/authconcept.html">User authentications</a> in the <i>IAM Identity Center User Guide</i>.</p> </note>

        Args:
            access_token: <p>The token issued by the <code>CreateToken</code> API call. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html">CreateToken</a> in the <i>IAM Identity Center OIDC API Reference Guide</i>.</p>

        Raises:
            capo_sso.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that a problem occurred with the input to the request. For example, a required parameter might be missing or out of range.</p>
            capo_sso.errors.too_many_requests_exception.TooManyRequestsException: <p>Indicates that the request is being made too frequently and is more than what the server can handle.</p>
            capo_sso.errors.unauthorized_exception.UnauthorizedException: <p>Indicates that the request is not authorized. This can happen due to an invalid access token in the request.</p>
            capo_sso.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sso.types.logout_request.LogoutRequest]",
        ) -> OperationResponse[None]:
            import capo_sso._operations.swb_portal_service.logout

            output, http_response = (
                capo_sso._operations.swb_portal_service.logout.logout(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sso.types.logout_request.LogoutRequest = {
            "access_token": access_token
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
