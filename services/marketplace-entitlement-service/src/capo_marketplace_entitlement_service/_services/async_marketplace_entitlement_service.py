"""Generated from Smithy shape ``com.amazonaws.marketplaceentitlementservice#AWSMPEntitlementService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_marketplace_entitlement_service._auth._signers
import capo_marketplace_entitlement_service._auth._sigv4
from capo_marketplace_entitlement_service._auth._identity import Credentials
from capo_marketplace_entitlement_service._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_marketplace_entitlement_service._auth._zapros_handler import AuthMiddleware
from capo_marketplace_entitlement_service._pagination import (
    resolve_path as _resolve_path,
)
from capo_marketplace_entitlement_service._services._aws_config import aaws_config
from capo_marketplace_entitlement_service._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_marketplace_entitlement_service.types.get_entitlement_filters
    import capo_marketplace_entitlement_service.types.get_entitlements_request
    import capo_marketplace_entitlement_service.types.get_entitlements_result
    import capo_marketplace_entitlement_service.types.non_empty_string
    import capo_marketplace_entitlement_service.types.page_size_integer
    import capo_marketplace_entitlement_service.types.product_code


class AsyncMarketplaceEntitlementServiceClientConfig(
    TypedDict, total=False, closed=True
):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncMarketplaceEntitlementServiceClient:
    """A client for the ``MarketplaceEntitlementService`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
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
        use_dual_stack: bool | None = None,
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
        self._config = AsyncMarketplaceEntitlementServiceClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self,
        config_overrides: Optional[
            AsyncMarketplaceEntitlementServiceClientConfig
        ] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMarketplaceEntitlementServiceClientConfig = (
            config_overrides or {}
        )
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
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

    async def get_entitlements(
        self,
        product_code: "capo_marketplace_entitlement_service.types.product_code.ProductCode",
        *,
        config_overrides: Optional[
            AsyncMarketplaceEntitlementServiceClientConfig
        ] = None,
        filter: Optional[
            "capo_marketplace_entitlement_service.types.get_entitlement_filters.GetEntitlementFilters"
        ] = None,
        next_token: Optional[
            "capo_marketplace_entitlement_service.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional[
            "capo_marketplace_entitlement_service.types.page_size_integer.PageSizeInteger"
        ] = None,
    ) -> "capo_marketplace_entitlement_service.types.get_entitlements_result.GetEntitlementsResult":
        """<p>GetEntitlements retrieves entitlement values for a given product. The results can be filtered based on customer identifier, AWS account ID, license ARN, or product dimensions.</p>

        Args:
            product_code: <p>Product code is used to uniquely identify a product in AWS Marketplace. The product code will be provided by AWS Marketplace when the product listing is created.</p>
            filter: <p>Filter is used to return entitlements for a specific customer or for a specific dimension. Filters are described as keys mapped to a lists of values. Filtered requests are <i>unioned</i> for each value in the value list, and then <i>intersected</i> for each filter key.</p> <p> <code>CustomerIdentifier</code> and <code>CustomerAWSAccountId</code> are mutually exclusive parameters. You must use one or the other, but not both in the same request. </p> <note> <p>If you're migrating an existing integration, use <a href="https://docs.aws.amazon.com/marketplace/latest/userguide/data-feed-account.html">Account Feeds</a> to map <code>CustomerIdentifier</code> to <code>CustomerAWSAccountId</code>, and <a href="https://docs.aws.amazon.com/marketplace/latest/userguide/data-feed-agreements.html">Agreements Feeds</a> to map <code>CustomerAWSAccountId</code> and <code>LicenseArn</code>.</p> </note>
            next_token: <p>For paginated calls to GetEntitlements, pass the NextToken from the previous GetEntitlementsResult.</p>
            max_results: <p>The maximum number of items to retrieve from the GetEntitlements operation. For pagination, use the NextToken field in subsequent calls to GetEntitlements.</p>

        Raises:
            capo_marketplace_entitlement_service.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal error has occurred. Retry your request. If the problem persists, post a message with details on the AWS forums.</p>
            capo_marketplace_entitlement_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters in your request was invalid.</p>
            capo_marketplace_entitlement_service.errors.throttling_exception.ThrottlingException: <p>The calls to the GetEntitlements API are throttled.</p>
            capo_marketplace_entitlement_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_entitlement_service.types.get_entitlements_request.GetEntitlementsRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_entitlement_service.types.get_entitlements_result.GetEntitlementsResult"
        ]:
            import capo_marketplace_entitlement_service._operations.awsmp_entitlement_service.get_entitlements

            (
                output,
                http_response,
            ) = await capo_marketplace_entitlement_service._operations.awsmp_entitlement_service.get_entitlements.async_get_entitlements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_entitlement_service.types.get_entitlements_request.GetEntitlementsRequest = {
            "product_code": product_code
        }
        if filter is not None:
            input_["filter"] = filter
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

    async def iter_get_entitlements(
        self,
        product_code: "capo_marketplace_entitlement_service.types.product_code.ProductCode",
        *,
        config_overrides: Optional[
            AsyncMarketplaceEntitlementServiceClientConfig
        ] = None,
        filter: Optional[
            "capo_marketplace_entitlement_service.types.get_entitlement_filters.GetEntitlementFilters"
        ] = None,
        next_token: Optional[
            "capo_marketplace_entitlement_service.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional[
            "capo_marketplace_entitlement_service.types.page_size_integer.PageSizeInteger"
        ] = None,
    ) -> "AsyncIterator[capo_marketplace_entitlement_service.types.get_entitlements_result.GetEntitlementsResult]":
        _token = next_token
        while True:
            _response = await self.get_entitlements(
                product_code,
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
