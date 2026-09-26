"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#AuthRequestService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_iam_toolbox._auth._signers
import capo_iam_toolbox._auth._sigv4
from capo_iam_toolbox._auth._identity import Credentials
from capo_iam_toolbox._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_iam_toolbox._auth._zapros_handler import AuthMiddleware
from capo_iam_toolbox._pagination import resolve_path as _resolve_path
from capo_iam_toolbox._services._aws_config import aaws_config
from capo_iam_toolbox._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_iam_toolbox.types.evaluation
    import capo_iam_toolbox.types.get_request_authorization_details_input
    import capo_iam_toolbox.types.get_request_authorization_details_output


class AsyncIAMToolboxClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncIAMToolboxClient:
    """A client for the ``IAMToolbox`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = AsyncIAMToolboxClientConfig(
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
        self, config_overrides: Optional[AsyncIAMToolboxClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncIAMToolboxClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def get_request_authorization_details(
        self,
        authorization_id: str,
        *,
        config_overrides: Optional[AsyncIAMToolboxClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "capo_iam_toolbox.types.get_request_authorization_details_output.GetRequestAuthorizationDetailsOutput":
        """<p>Retrieves the authorization details for a specific access denied request. The details include the request context, the evaluations performed, and the policies that were evaluated.</p> <p>Use this operation to understand why a request was denied. Supported services include an authorization ID in the access denied error message. Pass that ID to this operation to retrieve the details.</p> <p>Authorization details are available for at least 24 hours after the denial.</p> <p>To use this operation, you must have the <code>iam:GetRequestAuthorizationDetails</code> permission.</p>

        Args:
            authorization_id: <p>The authorization ID received in the access denied error message. This ID identifies the specific request to retrieve details for.</p>
            next_token: <p>The pagination token from a previous call, used to retrieve the next page of evaluations. Omit this value on the first call.</p>

        Raises:
            capo_iam_toolbox.errors.access_denied_exception.AccessDeniedException: <p>The caller does not have sufficient access to perform this action.</p>
            capo_iam_toolbox.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request. Try again.</p>
            capo_iam_toolbox.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested authorization details do not exist in this region or have expired. Verify that the authorization ID from the access denied error message is correct and the call is made in the region where the denial occurred. Ensure that the calling principal belongs to the same account or organization as the original denied request.</p>
            capo_iam_toolbox.errors.validation_exception.ValidationException: <p>The request is malformed or is missing one or more required parameters. Check the request parameters and try again.</p>
            capo_iam_toolbox.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iam_toolbox.types.get_request_authorization_details_input.GetRequestAuthorizationDetailsInput]",
        ) -> AsyncOperationResponse[
            "capo_iam_toolbox.types.get_request_authorization_details_output.GetRequestAuthorizationDetailsOutput"
        ]:
            import capo_iam_toolbox._operations.auth_request_service.get_request_authorization_details

            (
                output,
                http_response,
            ) = await capo_iam_toolbox._operations.auth_request_service.get_request_authorization_details.async_get_request_authorization_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iam_toolbox.types.get_request_authorization_details_input.GetRequestAuthorizationDetailsInput = {
            "authorization_id": authorization_id
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_request_authorization_details(
        self,
        authorization_id: str,
        *,
        config_overrides: Optional[AsyncIAMToolboxClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_iam_toolbox.types.evaluation.Evaluation]":
        _token = next_token
        while True:
            _response = await self.get_request_authorization_details(
                authorization_id,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("evaluations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
