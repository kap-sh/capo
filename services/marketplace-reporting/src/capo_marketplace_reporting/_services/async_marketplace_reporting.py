"""Generated from Smithy shape ``com.amazonaws.marketplacereporting#AWSMarketplaceReporting``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_marketplace_reporting._auth._signers
import capo_marketplace_reporting._auth._sigv4
from capo_marketplace_reporting._auth._identity import Credentials
from capo_marketplace_reporting._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_marketplace_reporting._auth._zapros_handler import AuthMiddleware
from capo_marketplace_reporting._resources.aws_marketplace_reporting.dashboard import (
    AsyncDashboard,
)
from capo_marketplace_reporting._services._aws_config import aaws_config
from capo_marketplace_reporting._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_marketplace_reporting.types.dashboard_identifier
    import capo_marketplace_reporting.types.embedding_domains
    import capo_marketplace_reporting.types.get_buyer_dashboard_input
    import capo_marketplace_reporting.types.get_buyer_dashboard_output


class AsyncMarketplaceReportingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncMarketplaceReportingClient:
    """A client for the ``MarketplaceReporting`` service.

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
        self._config = AsyncMarketplaceReportingClientConfig(
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

        # resources
        self.dashboard = AsyncDashboard(self)

    def operation_options(
        self, config_overrides: Optional[AsyncMarketplaceReportingClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMarketplaceReportingClientConfig = config_overrides or {}
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

    async def get_buyer_dashboard(
        self,
        dashboard_identifier: "capo_marketplace_reporting.types.dashboard_identifier.DashboardIdentifier",
        embedding_domains: "capo_marketplace_reporting.types.embedding_domains.EmbeddingDomains",
        *,
        config_overrides: Optional[AsyncMarketplaceReportingClientConfig] = None,
    ) -> "capo_marketplace_reporting.types.get_buyer_dashboard_output.GetBuyerDashboardOutput":
        """<p>Generates an embedding URL for an Amazon QuickSight dashboard for an anonymous user.</p> <note> <p>This API is available only to Amazon Web Services Organization management accounts or delegated administrators registered for the procurement insights (<code>procurement-insights.marketplace.amazonaws.com</code>) feature.</p> </note> <p>The following rules apply to a generated URL:</p> <ul> <li> <p>It contains a temporary bearer token, valid for 5 minutes after it is generated. Once redeemed within that period, it cannot be re-used again.</p> </li> <li> <p>It has a session lifetime of one hour. The 5-minute validity period runs separately from the session lifetime.</p> </li> </ul>

        Args:
            dashboard_identifier: <p>The ARN of the requested dashboard.</p>
            embedding_domains: <p>Fully qualified domains that you add to the allow list for access to the generated URL that is then embedded. You can list up to two domains or subdomains in each API call. To include all subdomains under a specific domain, use <code>*</code>. For example, <code>https://*.amazon.com</code> includes all subdomains under <code>https://aws.amazon.com</code>.</p>

        Raises:
            capo_marketplace_reporting.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_marketplace_reporting.errors.bad_request_exception.BadRequestException: <p>The request is malformed, or it contains an error such as an invalid parameter. Ensure the request has all required parameters.</p>
            capo_marketplace_reporting.errors.internal_server_exception.InternalServerException: <p>The operation failed due to a server error.</p>
            capo_marketplace_reporting.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_marketplace_reporting.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Getting an agreements dashboard
            The following example shows how to obtain a dashboard for active agreements

            >>> await client.get_buyer_dashboard(dashboard_identifier='arn:aws:aws-marketplace::123456789012:AWSMarketplace/ReportingData/Agreement_V1/Dashboard/AgreementSummary_V1', embedding_domains=['https://*.amazon.com'])
            Getting a cost-analysis dashboard
            The following example shows how to obtain a dashboard for cost analysis

            >>> await client.get_buyer_dashboard(dashboard_identifier='arn:aws:aws-marketplace::123456789012:AWSMarketplace/ReportingData/BillingEvent_V1/Dashboard/CostAnalysis_V1', embedding_domains=['https://*.amazon.com'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_reporting.types.get_buyer_dashboard_input.GetBuyerDashboardInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_reporting.types.get_buyer_dashboard_output.GetBuyerDashboardOutput"
        ]:
            import capo_marketplace_reporting._operations.aws_marketplace_reporting.get_buyer_dashboard

            (
                output,
                http_response,
            ) = await capo_marketplace_reporting._operations.aws_marketplace_reporting.get_buyer_dashboard.async_get_buyer_dashboard(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_reporting.types.get_buyer_dashboard_input.GetBuyerDashboardInput = {
            "dashboard_identifier": dashboard_identifier,
            "embedding_domains": embedding_domains,
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
