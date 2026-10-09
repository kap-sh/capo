"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#AmazonConnectContactLens``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_connect_contact_lens._auth._signers
import capo_connect_contact_lens._auth._sigv4
from capo_connect_contact_lens._auth._identity import Credentials
from capo_connect_contact_lens._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_connect_contact_lens._auth._zapros_handler import AuthMiddleware
from capo_connect_contact_lens._pagination import resolve_path as _resolve_path
from capo_connect_contact_lens._services._aws_config import aaws_config
from capo_connect_contact_lens._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_connect_contact_lens.types.contact_id
    import capo_connect_contact_lens.types.instance_id
    import capo_connect_contact_lens.types.list_realtime_contact_analysis_segments_request
    import capo_connect_contact_lens.types.list_realtime_contact_analysis_segments_response
    import capo_connect_contact_lens.types.max_results
    import capo_connect_contact_lens.types.next_token


class AsyncConnectContactLensClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncConnectContactLensClient:
    """A client for the ``ConnectContactLens`` service.

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
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
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
        self._config = AsyncConnectContactLensClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncConnectContactLensClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncConnectContactLensClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def list_realtime_contact_analysis_segments(
        self,
        *,
        config_overrides: Optional[AsyncConnectContactLensClientConfig] = None,
        instance_id: Optional[
            "capo_connect_contact_lens.types.instance_id.InstanceId"
        ] = None,
        contact_id: Optional[
            "capo_connect_contact_lens.types.contact_id.ContactId"
        ] = None,
        max_results: Optional[
            "capo_connect_contact_lens.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_connect_contact_lens.types.next_token.NextToken"
        ] = None,
    ) -> "capo_connect_contact_lens.types.list_realtime_contact_analysis_segments_response.ListRealtimeContactAnalysisSegmentsResponse":
        """<p>Provides a list of analysis segments for a real-time analysis session for voice.</p> <note> <p>Voice data is retained for 24 hours. You must invoke this API during that time.</p> </note>

        Args:
            instance_id: <p>The identifier of the Amazon Connect instance.</p>
            contact_id: <p>The identifier of the contact.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connect_contact_lens.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connect_contact_lens.errors.internal_service_exception.InternalServiceException: <p>Request processing failed due to an error or failure with the service.</p>
            capo_connect_contact_lens.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid.</p>
            capo_connect_contact_lens.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_connect_contact_lens.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_connect_contact_lens.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connect_contact_lens.types.list_realtime_contact_analysis_segments_request.ListRealtimeContactAnalysisSegmentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_connect_contact_lens.types.list_realtime_contact_analysis_segments_response.ListRealtimeContactAnalysisSegmentsResponse"
        ]:
            import capo_connect_contact_lens._operations.amazon_connect_contact_lens.list_realtime_contact_analysis_segments

            (
                output,
                http_response,
            ) = await capo_connect_contact_lens._operations.amazon_connect_contact_lens.list_realtime_contact_analysis_segments.async_list_realtime_contact_analysis_segments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connect_contact_lens.types.list_realtime_contact_analysis_segments_request.ListRealtimeContactAnalysisSegmentsRequest = {}
        if instance_id is not None:
            input_["instance_id"] = instance_id
        if contact_id is not None:
            input_["contact_id"] = contact_id
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

    async def iter_list_realtime_contact_analysis_segments(
        self,
        *,
        config_overrides: Optional[AsyncConnectContactLensClientConfig] = None,
        instance_id: Optional[
            "capo_connect_contact_lens.types.instance_id.InstanceId"
        ] = None,
        contact_id: Optional[
            "capo_connect_contact_lens.types.contact_id.ContactId"
        ] = None,
        max_results: Optional[
            "capo_connect_contact_lens.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_connect_contact_lens.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_connect_contact_lens.types.list_realtime_contact_analysis_segments_response.ListRealtimeContactAnalysisSegmentsResponse]":
        _token = next_token
        while True:
            _response = await self.list_realtime_contact_analysis_segments(
                config_overrides=config_overrides,
                instance_id=instance_id,
                contact_id=contact_id,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
