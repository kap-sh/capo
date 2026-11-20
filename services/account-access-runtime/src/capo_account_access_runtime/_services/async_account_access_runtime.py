"""Generated from Smithy shape ``com.amazonaws.accountaccessruntime#AWSAccountAccessRuntime``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Literal, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_account_access_runtime._auth._signers
import capo_account_access_runtime._auth._sigv4
from capo_account_access_runtime._auth._providers import (
    BearerTokenProvider,
    StaticBearerTokenProvider,
)
from capo_account_access_runtime._auth._zapros_handler import AuthMiddleware
from capo_account_access_runtime._services._aws_config import aaws_config
from capo_account_access_runtime._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    RateLimiter,
    RetryQuota,
    aexecute_pipeline,
    alog_operation,
    arate_limit,
    aretry,
)

if TYPE_CHECKING:
    import capo_account_access_runtime.types.access_type
    import capo_account_access_runtime.types.get_role_credentials_request
    import capo_account_access_runtime.types.get_role_credentials_response
    import capo_account_access_runtime.types.list_roles_request
    import capo_account_access_runtime.types.list_roles_response
    import capo_account_access_runtime.types.session_name
    import capo_account_access_runtime.types.tenant_id
    import capo_account_access_runtime.types.token


class AsyncAccountAccessRuntimeClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    retry_mode: Literal["standard", "adaptive"] | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    bearer_provider: BearerTokenProvider | None
    anonymous: bool | None


class AsyncAccountAccessRuntimeClient:
    """A client for the ``AccountAccessRuntime`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        retry_mode: ``"standard"`` (the default) or ``"adaptive"``, which also slows the whole client down when the service throttles it.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        bearer: Bearer token for authentication.
        bearer_provider: Provider that resolves bearer tokens. Takes precedence over ``bearer``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        retry_mode: Literal["standard", "adaptive"] | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        bearer: str | None = None,
        bearer_provider: BearerTokenProvider | None = None,
        anonymous: bool | None = None,
    ):
        client = AsyncClient(http_handler)
        self._client = client.wrap_with_middleware(lambda next: AuthMiddleware(next))
        # One retry quota for all of this client's operations.
        self._retry_quota = RetryQuota()
        # One send-rate limiter too, used when retry_mode is adaptive.
        self._rate_limiter = RateLimiter()
        if bearer is not None and bearer_provider is not None:
            warnings.warn(
                "Both bearer and bearer_provider given; provider takes precedence"
            )
        if bearer_provider is None and bearer is not None:
            bearer_provider = StaticBearerTokenProvider(bearer)
        self._config = AsyncAccountAccessRuntimeClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "retry_mode": retry_mode,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "bearer_provider": bearer_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self,
        config_overrides: Optional[AsyncAccountAccessRuntimeClientConfig] = None,
        operation_logging: OperationLogging | None = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncAccountAccessRuntimeClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
        ]
        if operation_logging is not None:
            interceptors_.append(alog_operation(operation_logging))
        interceptors_.append(aretry())
        interceptors_.append(arate_limit())
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_quota=self._retry_quota,
            rate_limiter=self._rate_limiter,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            retry_mode=overrides.get("retry_mode", self._config.get("retry_mode")),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            bearer_provider=overrides.get(
                "bearer_provider", self._config.get("bearer_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def get_role_credentials(
        self,
        tenant_id: "capo_account_access_runtime.types.tenant_id.TenantId",
        role_arn: str,
        access_type: "capo_account_access_runtime.types.access_type.AccessType",
        *,
        config_overrides: Optional[AsyncAccountAccessRuntimeClientConfig] = None,
        session_name: Optional[
            "capo_account_access_runtime.types.session_name.SessionName"
        ] = None,
        session_duration: Optional[int] = None,
    ) -> "capo_account_access_runtime.types.get_role_credentials_response.GetRoleCredentialsResponse":
        """<p>Returns temporary Amazon Web Services credentials for a role that you are entitled to assume within a tenant. You can use these credentials for programmatic access with the CLI or an Amazon Web Services SDK. If you aren't entitled to the role, the request fails with an <code>AccessDeniedException</code> error.</p>

        Args:
            tenant_id: <p>The identifier of the tenant that the request applies to. A tenant ID begins with <code>aa-</code> and is 3 to 24 characters long. It can contain lowercase letters, numbers, and hyphens.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the role to retrieve credentials for. You must be entitled to assume this role.</p>
            access_type: <p>The type of access to request for the role. Specify <code>PROGRAMMATIC_ACCESS</code> to receive access key credentials for use with the CLI or an Amazon Web Services SDK.</p>
            session_name: <p>An optional name for the role session. The name can be 2 to 64 characters and can contain alphanumeric characters and the following symbols: plus (+), equal (=), comma (,), period (.), at (@), and hyphen (-). The session name appears in CloudTrail logs for the assumed role session.</p>
            session_duration: <p>The duration, in seconds, that the returned credentials remain valid. If you don't specify a value, the service uses the default session duration. The maximum value can't exceed the maximum session duration configured for the role.</p>

        Raises:
            capo_account_access_runtime.errors.access_denied_exception.AccessDeniedException: <p>You are authenticated but not authorized to perform the requested action, such as assuming a role that you aren't entitled to. This error returns an HTTP 403 status code.</p>
            capo_account_access_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request. If the problem persists, contact Amazon Web Services Support. This error returns an HTTP 500 status code.</p>
            capo_account_access_runtime.errors.throttling_exception.ThrottlingException: <p>The request rate exceeded the allowed limit. Reduce your request rate, and then retry the request. This error returns an HTTP 429 status code.</p>
            capo_account_access_runtime.errors.unauthorized_exception.UnauthorizedException: <p>The bearer token is missing, invalid, or expired. Obtain a new token, and then retry the request. This error returns an HTTP 401 status code.</p>
            capo_account_access_runtime.errors.validation_exception.ValidationException: <p>The request is missing a required parameter, or a parameter value doesn't satisfy its constraints, such as its length or pattern. Correct the input, and then retry the request. This error returns an HTTP 400 status code.</p>
            capo_account_access_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_account_access_runtime.types.get_role_credentials_request.GetRoleCredentialsRequest]",
        ) -> AsyncOperationResponse[
            "capo_account_access_runtime.types.get_role_credentials_response.GetRoleCredentialsResponse"
        ]:
            import capo_account_access_runtime._operations.aws_account_access_runtime.get_role_credentials

            (
                output,
                http_response,
            ) = await capo_account_access_runtime._operations.aws_account_access_runtime.get_role_credentials.async_get_role_credentials(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_account_access_runtime.types.get_role_credentials_response.GetRoleCredentialsResponse",
        ) -> dict[str, Any]:
            import capo_account_access_runtime.types.get_role_credentials_response

            return capo_account_access_runtime.types.get_role_credentials_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("GetRoleCredentials", redact_output=_redact_output),
        )
        input_: capo_account_access_runtime.types.get_role_credentials_request.GetRoleCredentialsRequest = {
            "tenant_id": tenant_id,
            "role_arn": role_arn,
            "access_type": access_type,
        }
        if session_name is not None:
            input_["session_name"] = session_name
        if session_duration is not None:
            input_["session_duration"] = session_duration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_roles(
        self,
        tenant_id: "capo_account_access_runtime.types.tenant_id.TenantId",
        *,
        config_overrides: Optional[AsyncAccountAccessRuntimeClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_account_access_runtime.types.token.Token"] = None,
    ) -> "capo_account_access_runtime.types.list_roles_response.ListRolesResponse":
        """<p>Returns the roles that you are entitled to access within a tenant. The results are paginated. Use a returned role with <code>GetRoleCredentials</code> to obtain temporary credentials.</p>

        Args:
            tenant_id: <p>The identifier of the tenant whose roles you want to list. A tenant ID begins with <code>aa-</code> and is 3 to 24 characters long. It can contain lowercase letters, numbers, and hyphens.</p>
            max_results: <p>The maximum number of roles to return in a single response. If more roles are available than the specified value, the response includes a <code>nextToken</code> value that you can use to retrieve the next page of results. If you don't specify a value, the service uses a default page size.</p>
            next_token: <p>The pagination token from a previous <code>ListRoles</code> response. Use it to retrieve the next page of results. Omit this parameter on the first call.</p>

        Raises:
            capo_account_access_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request. If the problem persists, contact Amazon Web Services Support. This error returns an HTTP 500 status code.</p>
            capo_account_access_runtime.errors.throttling_exception.ThrottlingException: <p>The request rate exceeded the allowed limit. Reduce your request rate, and then retry the request. This error returns an HTTP 429 status code.</p>
            capo_account_access_runtime.errors.unauthorized_exception.UnauthorizedException: <p>The bearer token is missing, invalid, or expired. Obtain a new token, and then retry the request. This error returns an HTTP 401 status code.</p>
            capo_account_access_runtime.errors.validation_exception.ValidationException: <p>The request is missing a required parameter, or a parameter value doesn't satisfy its constraints, such as its length or pattern. Correct the input, and then retry the request. This error returns an HTTP 400 status code.</p>
            capo_account_access_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_account_access_runtime.types.list_roles_request.ListRolesRequest]",
        ) -> AsyncOperationResponse[
            "capo_account_access_runtime.types.list_roles_response.ListRolesResponse"
        ]:
            import capo_account_access_runtime._operations.aws_account_access_runtime.list_roles

            (
                output,
                http_response,
            ) = await capo_account_access_runtime._operations.aws_account_access_runtime.list_roles.async_list_roles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListRoles")
        )
        input_: capo_account_access_runtime.types.list_roles_request.ListRolesRequest = {
            "tenant_id": tenant_id
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
