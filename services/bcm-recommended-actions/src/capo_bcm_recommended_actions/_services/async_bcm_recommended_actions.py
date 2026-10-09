"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#AWSBillingAndCostManagementRecommendedActions``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_bcm_recommended_actions._auth._signers
import capo_bcm_recommended_actions._auth._sigv4
from capo_bcm_recommended_actions._auth._identity import Credentials
from capo_bcm_recommended_actions._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_bcm_recommended_actions._auth._zapros_handler import AuthMiddleware
from capo_bcm_recommended_actions._pagination import resolve_path as _resolve_path
from capo_bcm_recommended_actions._services._aws_config import aaws_config
from capo_bcm_recommended_actions._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_bcm_recommended_actions.types.list_recommended_actions_request
    import capo_bcm_recommended_actions.types.list_recommended_actions_response
    import capo_bcm_recommended_actions.types.max_results
    import capo_bcm_recommended_actions.types.next_token
    import capo_bcm_recommended_actions.types.recommended_action
    import capo_bcm_recommended_actions.types.request_filter


class AsyncBCMRecommendedActionsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncBCMRecommendedActionsClient:
    """A client for the ``BCMRecommendedActions`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
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
        self._config = AsyncBCMRecommendedActionsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncBCMRecommendedActionsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBCMRecommendedActionsClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def list_recommended_actions(
        self,
        *,
        config_overrides: Optional[AsyncBCMRecommendedActionsClientConfig] = None,
        filter: Optional[
            "capo_bcm_recommended_actions.types.request_filter.RequestFilter"
        ] = None,
        max_results: Optional[
            "capo_bcm_recommended_actions.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bcm_recommended_actions.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bcm_recommended_actions.types.list_recommended_actions_response.ListRecommendedActionsResponse":
        """<p>Returns a list of recommended actions that match the filter criteria.</p>

        Args:
            filter: <p>The criteria that you want all returned recommended actions to match.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>The pagination token that indicates the next set of results that you want to retrieve.</p>

        Raises:
            capo_bcm_recommended_actions.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_bcm_recommended_actions.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_bcm_recommended_actions.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_bcm_recommended_actions.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_bcm_recommended_actions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_recommended_actions.types.list_recommended_actions_request.ListRecommendedActionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_recommended_actions.types.list_recommended_actions_response.ListRecommendedActionsResponse"
        ]:
            import capo_bcm_recommended_actions._operations.aws_billing_and_cost_management_recommended_actions.list_recommended_actions

            (
                output,
                http_response,
            ) = await capo_bcm_recommended_actions._operations.aws_billing_and_cost_management_recommended_actions.list_recommended_actions.async_list_recommended_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_recommended_actions.types.list_recommended_actions_request.ListRecommendedActionsRequest = {}
        if filter is not None:
            input_["filter"] = filter
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

    async def iter_list_recommended_actions(
        self,
        *,
        config_overrides: Optional[AsyncBCMRecommendedActionsClientConfig] = None,
        filter: Optional[
            "capo_bcm_recommended_actions.types.request_filter.RequestFilter"
        ] = None,
        max_results: Optional[
            "capo_bcm_recommended_actions.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bcm_recommended_actions.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_bcm_recommended_actions.types.recommended_action.RecommendedAction]":
        _token = next_token
        while True:
            _response = await self.list_recommended_actions(
                config_overrides=config_overrides,
                filter=filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("recommended_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
