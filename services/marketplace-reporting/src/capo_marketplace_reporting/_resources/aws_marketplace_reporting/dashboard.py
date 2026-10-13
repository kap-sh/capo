from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_marketplace_reporting._auth._signers
import capo_marketplace_reporting._auth._sigv4
from capo_marketplace_reporting._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_marketplace_reporting.types.dashboard_identifier
    import capo_marketplace_reporting.types.embedding_domains
    import capo_marketplace_reporting.types.get_buyer_dashboard_input
    import capo_marketplace_reporting.types.get_buyer_dashboard_output
    from capo_marketplace_reporting._services.async_marketplace_reporting import (
        AsyncMarketplaceReportingClient,
        AsyncMarketplaceReportingClientConfig,
    )
    from capo_marketplace_reporting._services.marketplace_reporting import (
        MarketplaceReportingClient,
        MarketplaceReportingClientConfig,
    )


class Dashboard:
    def __init__(self, service: MarketplaceReportingClient) -> None:
        self._service = service

    def get_buyer_dashboard(
        self,
        dashboard_identifier: "capo_marketplace_reporting.types.dashboard_identifier.DashboardIdentifier",
        embedding_domains: "capo_marketplace_reporting.types.embedding_domains.EmbeddingDomains",
        *,
        config_overrides: Optional[MarketplaceReportingClientConfig] = None,
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

            >>> client.get_buyer_dashboard(dashboard_identifier='arn:aws:aws-marketplace::123456789012:AWSMarketplace/ReportingData/Agreement_V1/Dashboard/AgreementSummary_V1', embedding_domains=['https://*.amazon.com'])
            Getting a cost-analysis dashboard
            The following example shows how to obtain a dashboard for cost analysis

            >>> client.get_buyer_dashboard(dashboard_identifier='arn:aws:aws-marketplace::123456789012:AWSMarketplace/ReportingData/BillingEvent_V1/Dashboard/CostAnalysis_V1', embedding_domains=['https://*.amazon.com'])
        """

        def _handler(
            req: "OperationRequest[capo_marketplace_reporting.types.get_buyer_dashboard_input.GetBuyerDashboardInput]",
        ) -> OperationResponse[
            "capo_marketplace_reporting.types.get_buyer_dashboard_output.GetBuyerDashboardOutput"
        ]:
            import capo_marketplace_reporting._operations.aws_marketplace_reporting.get_buyer_dashboard

            output, http_response = (
                capo_marketplace_reporting._operations.aws_marketplace_reporting.get_buyer_dashboard.get_buyer_dashboard(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetBuyerDashboard")
        )
        input_: capo_marketplace_reporting.types.get_buyer_dashboard_input.GetBuyerDashboardInput = {
            "dashboard_identifier": dashboard_identifier,
            "embedding_domains": embedding_domains,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDashboard:
    def __init__(self, service: AsyncMarketplaceReportingClient) -> None:
        self._service = service

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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetBuyerDashboard")
        )
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
