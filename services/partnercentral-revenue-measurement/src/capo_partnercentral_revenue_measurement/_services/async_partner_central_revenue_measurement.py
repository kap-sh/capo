"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#PartnerCentralRevenueMeasurement``."""

import datetime
import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_partnercentral_revenue_measurement._auth._signers
import capo_partnercentral_revenue_measurement._auth._sigv4
from capo_partnercentral_revenue_measurement._auth._identity import Credentials
from capo_partnercentral_revenue_measurement._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_partnercentral_revenue_measurement._auth._zapros_handler import AuthMiddleware
from capo_partnercentral_revenue_measurement._pagination import (
    resolve_path as _resolve_path,
)
from capo_partnercentral_revenue_measurement._resources.partner_central_revenue_measurement.catalog import (
    AsyncCatalog,
)
from capo_partnercentral_revenue_measurement._services._aws_config import aaws_config
from capo_partnercentral_revenue_measurement._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.allocation_effective_date_string
    import capo_partnercentral_revenue_measurement.types.allocation_status
    import capo_partnercentral_revenue_measurement.types.attribution_sort_by
    import capo_partnercentral_revenue_measurement.types.attribution_summary
    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.client_token
    import capo_partnercentral_revenue_measurement.types.create_marketplace_revenue_share_allocation_input
    import capo_partnercentral_revenue_measurement.types.create_marketplace_revenue_share_allocation_output
    import capo_partnercentral_revenue_measurement.types.create_marketplace_revenue_share_input
    import capo_partnercentral_revenue_measurement.types.create_marketplace_revenue_share_output
    import capo_partnercentral_revenue_measurement.types.create_revenue_attribution_input
    import capo_partnercentral_revenue_measurement.types.create_revenue_attribution_output
    import capo_partnercentral_revenue_measurement.types.customer_aws_account_id_filter_list
    import capo_partnercentral_revenue_measurement.types.entity_identifier_filter_list
    import capo_partnercentral_revenue_measurement.types.entity_type_filter_list
    import capo_partnercentral_revenue_measurement.types.get_marketplace_revenue_share_allocation_input
    import capo_partnercentral_revenue_measurement.types.get_marketplace_revenue_share_allocation_output
    import capo_partnercentral_revenue_measurement.types.get_marketplace_revenue_share_input
    import capo_partnercentral_revenue_measurement.types.get_marketplace_revenue_share_output
    import capo_partnercentral_revenue_measurement.types.get_revenue_attribution_allocation_input
    import capo_partnercentral_revenue_measurement.types.get_revenue_attribution_allocation_output
    import capo_partnercentral_revenue_measurement.types.get_revenue_attribution_allocations_task_input
    import capo_partnercentral_revenue_measurement.types.get_revenue_attribution_allocations_task_output
    import capo_partnercentral_revenue_measurement.types.get_revenue_attribution_input
    import capo_partnercentral_revenue_measurement.types.get_revenue_attribution_output
    import capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_share_allocations_input
    import capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_share_allocations_output
    import capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_input
    import capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_output
    import capo_partnercentral_revenue_measurement.types.list_revenue_attribution_allocations_input
    import capo_partnercentral_revenue_measurement.types.list_revenue_attribution_allocations_output
    import capo_partnercentral_revenue_measurement.types.list_revenue_attributions_input
    import capo_partnercentral_revenue_measurement.types.list_revenue_attributions_output
    import capo_partnercentral_revenue_measurement.types.list_tags_for_resource_input
    import capo_partnercentral_revenue_measurement.types.list_tags_for_resource_output
    import capo_partnercentral_revenue_measurement.types.marketplace_product_id
    import capo_partnercentral_revenue_measurement.types.marketplace_product_id_list
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_id
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_sort_field
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_summary
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_sort_by
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_summary
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_tag_list
    import capo_partnercentral_revenue_measurement.types.next_token
    import capo_partnercentral_revenue_measurement.types.product_code_list
    import capo_partnercentral_revenue_measurement.types.resource_arn
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_id
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_sort_field
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_summary
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier_list
    import capo_partnercentral_revenue_measurement.types.revenue_share_allocation_change_list
    import capo_partnercentral_revenue_measurement.types.revenue_share_percent
    import capo_partnercentral_revenue_measurement.types.revision_token
    import capo_partnercentral_revenue_measurement.types.sort_order
    import capo_partnercentral_revenue_measurement.types.start_revenue_attribution_allocations_task_input
    import capo_partnercentral_revenue_measurement.types.start_revenue_attribution_allocations_task_output
    import capo_partnercentral_revenue_measurement.types.tag_key_list
    import capo_partnercentral_revenue_measurement.types.tag_list
    import capo_partnercentral_revenue_measurement.types.tag_resource_input
    import capo_partnercentral_revenue_measurement.types.tenancy_model
    import capo_partnercentral_revenue_measurement.types.untag_resource_input
    import capo_partnercentral_revenue_measurement.types.update_marketplace_revenue_share_allocation_input
    import capo_partnercentral_revenue_measurement.types.update_marketplace_revenue_share_allocation_output
    import capo_partnercentral_revenue_measurement.types.update_revenue_attribution_input
    import capo_partnercentral_revenue_measurement.types.update_revenue_attribution_output


class AsyncPartnerCentralRevenueMeasurementClientConfig(
    TypedDict, total=False, closed=True
):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncPartnerCentralRevenueMeasurementClient:
    """A client for the ``PartnerCentralRevenueMeasurement`` service.

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
        self._config = AsyncPartnerCentralRevenueMeasurementClientConfig(
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

        # resources
        self.catalog = AsyncCatalog(self)

    def operation_options(
        self,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPartnerCentralRevenueMeasurementClientConfig = (
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_partnercentral_revenue_measurement.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
    ) -> "capo_partnercentral_revenue_measurement.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Returns the tags associated with the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to list tags for.</p>

        Raises:
            capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_revenue_measurement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_revenue_measurement.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_revenue_measurement.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_revenue_measurement.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
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
        resource_arn: "capo_partnercentral_revenue_measurement.types.resource_arn.ResourceARN",
        tags: "capo_partnercentral_revenue_measurement.types.tag_list.TagList",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
    ) -> None:
        """<p>Adds or overwrites one or more tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>The tags to add to the resource.</p>

        Raises:
            capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_revenue_measurement.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_revenue_measurement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_revenue_measurement.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.tag_resource

            (
                output,
                http_response,
            ) = await capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_revenue_measurement.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_partnercentral_revenue_measurement.types.resource_arn.ResourceARN",
        tag_keys: "capo_partnercentral_revenue_measurement.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
    ) -> None:
        """<p>Removes one or more tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>The tag keys to remove from the resource.</p>

        Raises:
            capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_revenue_measurement.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_revenue_measurement.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_revenue_measurement.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.untag_resource

            (
                output,
                http_response,
            ) = await capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_revenue_measurement.types.untag_resource_input.UntagResourceInput = {
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

    async def create_marketplace_revenue_share(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        product_id: "capo_partnercentral_revenue_measurement.types.marketplace_product_id.MarketplaceProductId",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
        client_token: Optional[
            "capo_partnercentral_revenue_measurement.types.client_token.ClientToken"
        ] = None,
        tags: Optional[
            "capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_tag_list.MarketplaceRevenueShareTagList"
        ] = None,
    ) -> "capo_partnercentral_revenue_measurement.types.create_marketplace_revenue_share_output.CreateMarketplaceRevenueShareOutput":
        """<p>Creates a new marketplace revenue share resource in the specified catalog.</p>

        Args:
            catalog: <p>The catalog in which to create the marketplace revenue share.</p>
            client_token: <p>A unique token to ensure idempotency of the create request.</p>
            product_id: <p>The AWS Marketplace product identifier for this revenue share.</p>
            tags: <p>Tags to associate with the marketplace revenue share upon creation.</p>

        Raises:
            capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_revenue_measurement.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_revenue_measurement.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_revenue_measurement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for CreateMarketplaceRevenueShare

            >>> await client.create_marketplace_revenue_share(catalog='AWS', product_id='prod-abc123def4567')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_revenue_measurement.types.create_marketplace_revenue_share_input.CreateMarketplaceRevenueShareInput]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_revenue_measurement.types.create_marketplace_revenue_share_output.CreateMarketplaceRevenueShareOutput"
        ]:
            import capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.create_marketplace_revenue_share

            (
                output,
                http_response,
            ) = await capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.create_marketplace_revenue_share.async_create_marketplace_revenue_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_revenue_measurement.types.create_marketplace_revenue_share_input.CreateMarketplaceRevenueShareInput = {
            "catalog": catalog,
            "product_id": product_id,
        }
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

    async def get_marketplace_revenue_share(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        product_id: "capo_partnercentral_revenue_measurement.types.marketplace_product_id.MarketplaceProductId",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
        revision: Optional[int] = None,
    ) -> "capo_partnercentral_revenue_measurement.types.get_marketplace_revenue_share_output.GetMarketplaceRevenueShareOutput":
        """<p>Retrieves the details of a specific marketplace revenue share.</p>

        Args:
            catalog: <p>The catalog that the marketplace revenue share belongs to.</p>
            product_id: <p>The AWS Marketplace product identifier of the revenue share to retrieve.</p>
            revision: <p>The revision of the marketplace revenue share to retrieve. Omit to return the latest revision.</p>

        Raises:
            capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_revenue_measurement.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_revenue_measurement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for GetMarketplaceRevenueShare

            >>> await client.get_marketplace_revenue_share(catalog='AWS', product_id='prod-abc123def4567')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_revenue_measurement.types.get_marketplace_revenue_share_input.GetMarketplaceRevenueShareInput]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_revenue_measurement.types.get_marketplace_revenue_share_output.GetMarketplaceRevenueShareOutput"
        ]:
            import capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.get_marketplace_revenue_share

            (
                output,
                http_response,
            ) = await capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.get_marketplace_revenue_share.async_get_marketplace_revenue_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_revenue_measurement.types.get_marketplace_revenue_share_input.GetMarketplaceRevenueShareInput = {
            "catalog": catalog,
            "product_id": product_id,
        }
        if revision is not None:
            input_["revision"] = revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_marketplace_revenue_shares(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
        product_ids: Optional[
            "capo_partnercentral_revenue_measurement.types.marketplace_product_id_list.MarketplaceProductIdList"
        ] = None,
        product_codes: Optional[
            "capo_partnercentral_revenue_measurement.types.product_code_list.ProductCodeList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_partnercentral_revenue_measurement.types.next_token.NextToken"
        ] = None,
        sort_by: Optional[
            "capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_sort_by.MarketplaceRevenueShareSortBy"
        ] = None,
        sort_order: Optional[
            "capo_partnercentral_revenue_measurement.types.sort_order.SortOrder"
        ] = None,
        created_after: Optional[datetime.datetime] = None,
        created_before: Optional[datetime.datetime] = None,
    ) -> "capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_output.ListMarketplaceRevenueSharesOutput":
        """<p>Returns a paginated list of marketplace revenue shares with optional filters.</p>

        Args:
            catalog: <p>The catalog to list marketplace revenue shares from.</p>
            product_ids: <p>Filter results to only include shares with these product identifiers.</p>
            product_codes: <p>Filter results to only include shares with these product codes.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>Token for pagination. Use the value returned in the previous response to retrieve the next page.</p>
            sort_by: <p>The field to sort marketplace revenue shares by.</p>
            sort_order: <p>The direction to sort results.</p>
            created_after: <p>Filter results to only include marketplace revenue shares created after this timestamp.</p>
            created_before: <p>Filter results to only include marketplace revenue shares created before this timestamp.</p>

        Raises:
            capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_revenue_measurement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for ListMarketplaceRevenueShares

            >>> await client.list_marketplace_revenue_shares(catalog='AWS', max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_input.ListMarketplaceRevenueSharesInput]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_output.ListMarketplaceRevenueSharesOutput"
        ]:
            import capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.list_marketplace_revenue_shares

            (
                output,
                http_response,
            ) = await capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.list_marketplace_revenue_shares.async_list_marketplace_revenue_shares(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_shares_input.ListMarketplaceRevenueSharesInput = {
            "catalog": catalog
        }
        if product_ids is not None:
            input_["product_ids"] = product_ids
        if product_codes is not None:
            input_["product_codes"] = product_codes
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if created_after is not None:
            input_["created_after"] = created_after
        if created_before is not None:
            input_["created_before"] = created_before

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_marketplace_revenue_shares(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
        product_ids: Optional[
            "capo_partnercentral_revenue_measurement.types.marketplace_product_id_list.MarketplaceProductIdList"
        ] = None,
        product_codes: Optional[
            "capo_partnercentral_revenue_measurement.types.product_code_list.ProductCodeList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_partnercentral_revenue_measurement.types.next_token.NextToken"
        ] = None,
        sort_by: Optional[
            "capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_sort_by.MarketplaceRevenueShareSortBy"
        ] = None,
        sort_order: Optional[
            "capo_partnercentral_revenue_measurement.types.sort_order.SortOrder"
        ] = None,
        created_after: Optional[datetime.datetime] = None,
        created_before: Optional[datetime.datetime] = None,
    ) -> "AsyncIterator[capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_summary.MarketplaceRevenueShareSummary]":
        _token = next_token
        while True:
            _response = await self.list_marketplace_revenue_shares(
                catalog,
                config_overrides=config_overrides,
                product_ids=product_ids,
                product_codes=product_codes,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                sort_order=sort_order,
                created_after=created_after,
                created_before=created_before,
            )
            _page = _resolve_path(_response, ("marketplace_revenue_share_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_marketplace_revenue_share_allocation(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        product_id: "capo_partnercentral_revenue_measurement.types.marketplace_product_id.MarketplaceProductId",
        effective_from: "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString",
        revenue_share_percent: "capo_partnercentral_revenue_measurement.types.revenue_share_percent.RevenueSharePercent",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
        client_token: Optional[
            "capo_partnercentral_revenue_measurement.types.client_token.ClientToken"
        ] = None,
        effective_until: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
        ] = None,
    ) -> "capo_partnercentral_revenue_measurement.types.create_marketplace_revenue_share_allocation_output.CreateMarketplaceRevenueShareAllocationOutput":
        """<p>Creates a new marketplace revenue share allocation for the specified product.</p>

        Args:
            catalog: <p>The catalog in which to create the allocation.</p>
            product_id: <p>The AWS Marketplace product identifier for the parent revenue share.</p>
            client_token: <p>A unique token to ensure idempotency of the create request.</p>
            effective_from: <p>The effective start date for the allocation. Must be the first day of a month.</p>
            effective_until: <p>The effective end date for the allocation. Must be the last day of a month (YYYY-MM-DD). Omit for open-ended allocations.</p>
            revenue_share_percent: <p>The revenue share percentage for this allocation.</p>

        Raises:
            capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_revenue_measurement.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_revenue_measurement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for CreateMarketplaceRevenueShareAllocation

            >>> await client.create_marketplace_revenue_share_allocation(catalog='AWS', product_id='prod-abc123def4567', effective_from='2026-07-01', revenue_share_percent='15.50')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_revenue_measurement.types.create_marketplace_revenue_share_allocation_input.CreateMarketplaceRevenueShareAllocationInput]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_revenue_measurement.types.create_marketplace_revenue_share_allocation_output.CreateMarketplaceRevenueShareAllocationOutput"
        ]:
            import capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.create_marketplace_revenue_share_allocation

            (
                output,
                http_response,
            ) = await capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.create_marketplace_revenue_share_allocation.async_create_marketplace_revenue_share_allocation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_revenue_measurement.types.create_marketplace_revenue_share_allocation_input.CreateMarketplaceRevenueShareAllocationInput = {
            "catalog": catalog,
            "product_id": product_id,
            "effective_from": effective_from,
            "revenue_share_percent": revenue_share_percent,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if effective_until is not None:
            input_["effective_until"] = effective_until

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_marketplace_revenue_share_allocation(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        product_id: "capo_partnercentral_revenue_measurement.types.marketplace_product_id.MarketplaceProductId",
        marketplace_revenue_share_allocation_id: "capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_id.MarketplaceRevenueShareAllocationId",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
        marketplace_revenue_share_revision: Optional[
            "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
        ] = None,
    ) -> "capo_partnercentral_revenue_measurement.types.get_marketplace_revenue_share_allocation_output.GetMarketplaceRevenueShareAllocationOutput":
        """<p>Retrieves the details of a specific marketplace revenue share allocation.</p>

        Args:
            catalog: <p>The catalog that the allocation belongs to.</p>
            product_id: <p>The AWS Marketplace product identifier of the parent revenue share.</p>
            marketplace_revenue_share_allocation_id: <p>The unique identifier of the allocation to retrieve.</p>
            marketplace_revenue_share_revision: <p>The revision of the parent marketplace revenue share at which to retrieve the allocation. Omit to return the latest.</p>

        Raises:
            capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_revenue_measurement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for GetMarketplaceRevenueShareAllocation

            >>> await client.get_marketplace_revenue_share_allocation(catalog='AWS', product_id='prod-abc123def4567', marketplace_revenue_share_allocation_id='mrsa-abc123def4567')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_revenue_measurement.types.get_marketplace_revenue_share_allocation_input.GetMarketplaceRevenueShareAllocationInput]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_revenue_measurement.types.get_marketplace_revenue_share_allocation_output.GetMarketplaceRevenueShareAllocationOutput"
        ]:
            import capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.get_marketplace_revenue_share_allocation

            (
                output,
                http_response,
            ) = await capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.get_marketplace_revenue_share_allocation.async_get_marketplace_revenue_share_allocation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_revenue_measurement.types.get_marketplace_revenue_share_allocation_input.GetMarketplaceRevenueShareAllocationInput = {
            "catalog": catalog,
            "product_id": product_id,
            "marketplace_revenue_share_allocation_id": marketplace_revenue_share_allocation_id,
        }
        if marketplace_revenue_share_revision is not None:
            input_["marketplace_revenue_share_revision"] = (
                marketplace_revenue_share_revision
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_marketplace_revenue_share_allocations(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        product_id: "capo_partnercentral_revenue_measurement.types.marketplace_product_id.MarketplaceProductId",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
        status: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_status.AllocationStatus"
        ] = None,
        after_effective_from: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
        ] = None,
        before_effective_from: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
        ] = None,
        sort_by: Optional[
            "capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_sort_field.MarketplaceRevenueShareAllocationSortField"
        ] = None,
        sort_order: Optional[
            "capo_partnercentral_revenue_measurement.types.sort_order.SortOrder"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_partnercentral_revenue_measurement.types.next_token.NextToken"
        ] = None,
        marketplace_revenue_share_revision: Optional[
            "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
        ] = None,
    ) -> "capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_share_allocations_output.ListMarketplaceRevenueShareAllocationsOutput":
        """<p>Returns a paginated list of allocations under a marketplace revenue share, with optional filtering by status and effective date range. Supports historical reads at a specific share revision.</p>

        Args:
            catalog: <p>The catalog containing the allocations.</p>
            product_id: <p>The AWS Marketplace product identifier for the parent revenue share.</p>
            status: <p>Filter by allocation status.</p>
            after_effective_from: <p>Inclusive lower bound for EffectiveFrom date filter.</p>
            before_effective_from: <p>Exclusive upper bound for EffectiveFrom date filter (half-open range).</p>
            sort_by: <p>The field to sort marketplace revenue share allocations by.</p>
            sort_order: <p>The direction to sort results. Defaults to DESCENDING.</p>
            max_results: <p>Maximum number of results per page.</p>
            next_token: <p>Pagination token from a previous response.</p>
            marketplace_revenue_share_revision: <p>Optional share revision for historical list. Returns allocations as they existed at this revision.</p>

        Raises:
            capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_revenue_measurement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for ListMarketplaceRevenueShareAllocations

            >>> await client.list_marketplace_revenue_share_allocations(catalog='AWS', product_id='prod-abc123def4567')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_share_allocations_input.ListMarketplaceRevenueShareAllocationsInput]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_share_allocations_output.ListMarketplaceRevenueShareAllocationsOutput"
        ]:
            import capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.list_marketplace_revenue_share_allocations

            (
                output,
                http_response,
            ) = await capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.list_marketplace_revenue_share_allocations.async_list_marketplace_revenue_share_allocations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_revenue_measurement.types.list_marketplace_revenue_share_allocations_input.ListMarketplaceRevenueShareAllocationsInput = {
            "catalog": catalog,
            "product_id": product_id,
        }
        if status is not None:
            input_["status"] = status
        if after_effective_from is not None:
            input_["after_effective_from"] = after_effective_from
        if before_effective_from is not None:
            input_["before_effective_from"] = before_effective_from
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if marketplace_revenue_share_revision is not None:
            input_["marketplace_revenue_share_revision"] = (
                marketplace_revenue_share_revision
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_marketplace_revenue_share_allocations(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        product_id: "capo_partnercentral_revenue_measurement.types.marketplace_product_id.MarketplaceProductId",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
        status: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_status.AllocationStatus"
        ] = None,
        after_effective_from: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
        ] = None,
        before_effective_from: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
        ] = None,
        sort_by: Optional[
            "capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_sort_field.MarketplaceRevenueShareAllocationSortField"
        ] = None,
        sort_order: Optional[
            "capo_partnercentral_revenue_measurement.types.sort_order.SortOrder"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_partnercentral_revenue_measurement.types.next_token.NextToken"
        ] = None,
        marketplace_revenue_share_revision: Optional[
            "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_summary.MarketplaceRevenueShareAllocationSummary]":
        _token = next_token
        while True:
            _response = await self.list_marketplace_revenue_share_allocations(
                catalog,
                product_id,
                config_overrides=config_overrides,
                status=status,
                after_effective_from=after_effective_from,
                before_effective_from=before_effective_from,
                sort_by=sort_by,
                sort_order=sort_order,
                max_results=max_results,
                next_token=_token,
                marketplace_revenue_share_revision=marketplace_revenue_share_revision,
            )
            _page = _resolve_path(
                _response, ("marketplace_revenue_share_allocation_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_marketplace_revenue_share_allocation(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        product_id: "capo_partnercentral_revenue_measurement.types.marketplace_product_id.MarketplaceProductId",
        marketplace_revenue_share_allocation_id: "capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_id.MarketplaceRevenueShareAllocationId",
        marketplace_revenue_share_revision: "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
        client_token: Optional[
            "capo_partnercentral_revenue_measurement.types.client_token.ClientToken"
        ] = None,
        effective_from: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
        ] = None,
        effective_until: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
        ] = None,
        revenue_share_percent: Optional[
            "capo_partnercentral_revenue_measurement.types.revenue_share_percent.RevenueSharePercent"
        ] = None,
        status: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_status.AllocationStatus"
        ] = None,
    ) -> "capo_partnercentral_revenue_measurement.types.update_marketplace_revenue_share_allocation_output.UpdateMarketplaceRevenueShareAllocationOutput":
        """<p>Updates an existing marketplace revenue share allocation. Supports modifying effective dates, revenue share percentage, and status with time-based mutability rules.</p>

        Args:
            catalog: <p>The catalog containing the allocation.</p>
            product_id: <p>The AWS Marketplace product identifier for the parent revenue share.</p>
            marketplace_revenue_share_allocation_id: <p>The identifier of the allocation to update.</p>
            marketplace_revenue_share_revision: <p>The current revision of the parent share. Must match for optimistic concurrency control.</p>
            client_token: <p>A unique token to ensure idempotency of the update request.</p>
            effective_from: <p>The new effective start date. Must be the first day of a month. Only modifiable on future-dated allocations.</p>
            effective_until: <p>The new effective end date. Must be the last day of a month and on or after today.</p>
            revenue_share_percent: <p>The new revenue share percentage. Only modifiable on future-dated allocations.</p>
            status: <p>The new status. Set to INACTIVE for soft-delete. Only modifiable on future-dated allocations.</p>

        Raises:
            capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_revenue_measurement.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_revenue_measurement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for UpdateMarketplaceRevenueShareAllocation

            >>> await client.update_marketplace_revenue_share_allocation(catalog='AWS', product_id='prod-abc123def4567', marketplace_revenue_share_allocation_id='mrsa-abc123def4567', marketplace_revenue_share_revision='1', revenue_share_percent='20.00')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_revenue_measurement.types.update_marketplace_revenue_share_allocation_input.UpdateMarketplaceRevenueShareAllocationInput]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_revenue_measurement.types.update_marketplace_revenue_share_allocation_output.UpdateMarketplaceRevenueShareAllocationOutput"
        ]:
            import capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.update_marketplace_revenue_share_allocation

            (
                output,
                http_response,
            ) = await capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.update_marketplace_revenue_share_allocation.async_update_marketplace_revenue_share_allocation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_revenue_measurement.types.update_marketplace_revenue_share_allocation_input.UpdateMarketplaceRevenueShareAllocationInput = {
            "catalog": catalog,
            "product_id": product_id,
            "marketplace_revenue_share_allocation_id": marketplace_revenue_share_allocation_id,
            "marketplace_revenue_share_revision": marketplace_revenue_share_revision,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if effective_from is not None:
            input_["effective_from"] = effective_from
        if effective_until is not None:
            input_["effective_until"] = effective_until
        if revenue_share_percent is not None:
            input_["revenue_share_percent"] = revenue_share_percent
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_revenue_attribution(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        name: str,
        tenancy_model: "capo_partnercentral_revenue_measurement.types.tenancy_model.TenancyModel",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
        client_token: Optional[
            "capo_partnercentral_revenue_measurement.types.client_token.ClientToken"
        ] = None,
        description: Optional[str] = None,
        product_identifier: Optional[str] = None,
        tags: Optional[
            "capo_partnercentral_revenue_measurement.types.tag_list.TagList"
        ] = None,
    ) -> "capo_partnercentral_revenue_measurement.types.create_revenue_attribution_output.CreateRevenueAttributionOutput":
        """<p>Creates a new revenue attribution record in the specified catalog.</p>

        Args:
            catalog: <p>The catalog in which to create the revenue attribution.</p>
            client_token: <p>A unique token to ensure idempotency of the create request.</p>
            name: <p>The name of the revenue attribution. Must be unique within the catalog and the partner's account.</p>
            description: <p>A description of the revenue attribution.</p>
            tenancy_model: <p>The tenancy model for this revenue attribution.</p>
            product_identifier: <p>The unique product identifier in AWS Marketplace. Accepts a product entity ID (e.g., prod-abc123def4567) or a product ARN.</p>
            tags: <p>Tags to associate with the revenue attribution upon creation.</p>

        Raises:
            capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_revenue_measurement.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_revenue_measurement.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_revenue_measurement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for CreateRevenueAttribution

            >>> await client.create_revenue_attribution(catalog='AWS', name='My Revenue Attribution', tenancy_model='MULTI_TENANT')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_revenue_measurement.types.create_revenue_attribution_input.CreateRevenueAttributionInput]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_revenue_measurement.types.create_revenue_attribution_output.CreateRevenueAttributionOutput"
        ]:
            import capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.create_revenue_attribution

            (
                output,
                http_response,
            ) = await capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.create_revenue_attribution.async_create_revenue_attribution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_revenue_measurement.types.create_revenue_attribution_input.CreateRevenueAttributionInput = {
            "catalog": catalog,
            "name": name,
            "tenancy_model": tenancy_model,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if product_identifier is not None:
            input_["product_identifier"] = product_identifier
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_revenue_attribution(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        identifier: "capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier.RevenueAttributionIdentifier",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
        revision: Optional[
            "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
        ] = None,
    ) -> "capo_partnercentral_revenue_measurement.types.get_revenue_attribution_output.GetRevenueAttributionOutput":
        """<p>Retrieves the details of a specific revenue attribution.</p>

        Args:
            catalog: <p>The catalog that the revenue attribution belongs to.</p>
            identifier: <p>The unique identifier of the revenue attribution to retrieve. Accepts a direct ID or ARN.</p>
            revision: <p>The revision of the attribution to retrieve. Omit to return the latest revision.</p>

        Raises:
            capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_revenue_measurement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for GetRevenueAttribution

            >>> await client.get_revenue_attribution(catalog='AWS', identifier='ra-0a1b2c3d4e5f6')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_revenue_measurement.types.get_revenue_attribution_input.GetRevenueAttributionInput]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_revenue_measurement.types.get_revenue_attribution_output.GetRevenueAttributionOutput"
        ]:
            import capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.get_revenue_attribution

            (
                output,
                http_response,
            ) = await capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.get_revenue_attribution.async_get_revenue_attribution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_revenue_measurement.types.get_revenue_attribution_input.GetRevenueAttributionInput = {
            "catalog": catalog,
            "identifier": identifier,
        }
        if revision is not None:
            input_["revision"] = revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_revenue_attribution(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        identifier: "capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier.RevenueAttributionIdentifier",
        revision: "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
        client_token: Optional[
            "capo_partnercentral_revenue_measurement.types.client_token.ClientToken"
        ] = None,
        description: Optional[str] = None,
    ) -> "capo_partnercentral_revenue_measurement.types.update_revenue_attribution_output.UpdateRevenueAttributionOutput":
        """<p>Updates an existing revenue attribution record.</p>

        Args:
            catalog: <p>The catalog that the revenue attribution belongs to.</p>
            identifier: <p>The unique identifier of the revenue attribution to update. Accepts a direct ID or ARN.</p>
            client_token: <p>A unique token to ensure idempotency of the update request.</p>
            description: <p>The updated description of the revenue attribution.</p>
            revision: <p>The current revision of the revenue attribution. Must match the server's current value.</p>

        Raises:
            capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_revenue_measurement.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_revenue_measurement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for UpdateRevenueAttribution

            >>> await client.update_revenue_attribution(catalog='AWS', identifier='ra-0a1b2c3d4e5f6', revision='1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_revenue_measurement.types.update_revenue_attribution_input.UpdateRevenueAttributionInput]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_revenue_measurement.types.update_revenue_attribution_output.UpdateRevenueAttributionOutput"
        ]:
            import capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.update_revenue_attribution

            (
                output,
                http_response,
            ) = await capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.update_revenue_attribution.async_update_revenue_attribution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_revenue_measurement.types.update_revenue_attribution_input.UpdateRevenueAttributionInput = {
            "catalog": catalog,
            "identifier": identifier,
            "revision": revision,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_revenue_attributions(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
        identifiers: Optional[
            "capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier_list.RevenueAttributionIdentifierList"
        ] = None,
        created_after: Optional[datetime.datetime] = None,
        created_before: Optional[datetime.datetime] = None,
        sort_by: Optional[
            "capo_partnercentral_revenue_measurement.types.attribution_sort_by.AttributionSortBy"
        ] = None,
        sort_order: Optional[
            "capo_partnercentral_revenue_measurement.types.sort_order.SortOrder"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_partnercentral_revenue_measurement.types.next_token.NextToken"
        ] = None,
    ) -> "capo_partnercentral_revenue_measurement.types.list_revenue_attributions_output.ListRevenueAttributionsOutput":
        """<p>Returns a paginated list of revenue attributions with optional filters.</p>

        Args:
            catalog: <p>The catalog to list revenue attributions from.</p>
            identifiers: <p>Filter results to only include revenue attributions with the specified identifiers.</p>
            created_after: <p>Filter results to only include revenue attributions created after this timestamp.</p>
            created_before: <p>Filter results to only include revenue attributions created before this timestamp.</p>
            sort_by: <p>The field to sort revenue attributions by.</p>
            sort_order: <p>The direction to sort results.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>Token for pagination. Use the value returned in the previous response to retrieve the next page.</p>

        Raises:
            capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_revenue_measurement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for ListRevenueAttributions

            >>> await client.list_revenue_attributions(catalog='AWS')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_revenue_measurement.types.list_revenue_attributions_input.ListRevenueAttributionsInput]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_revenue_measurement.types.list_revenue_attributions_output.ListRevenueAttributionsOutput"
        ]:
            import capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.list_revenue_attributions

            (
                output,
                http_response,
            ) = await capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.list_revenue_attributions.async_list_revenue_attributions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_revenue_measurement.types.list_revenue_attributions_input.ListRevenueAttributionsInput = {
            "catalog": catalog
        }
        if identifiers is not None:
            input_["identifiers"] = identifiers
        if created_after is not None:
            input_["created_after"] = created_after
        if created_before is not None:
            input_["created_before"] = created_before
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    async def iter_list_revenue_attributions(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
        identifiers: Optional[
            "capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier_list.RevenueAttributionIdentifierList"
        ] = None,
        created_after: Optional[datetime.datetime] = None,
        created_before: Optional[datetime.datetime] = None,
        sort_by: Optional[
            "capo_partnercentral_revenue_measurement.types.attribution_sort_by.AttributionSortBy"
        ] = None,
        sort_order: Optional[
            "capo_partnercentral_revenue_measurement.types.sort_order.SortOrder"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_partnercentral_revenue_measurement.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_revenue_measurement.types.attribution_summary.AttributionSummary]":
        _token = next_token
        while True:
            _response = await self.list_revenue_attributions(
                catalog,
                config_overrides=config_overrides,
                identifiers=identifiers,
                created_after=created_after,
                created_before=created_before,
                sort_by=sort_by,
                sort_order=sort_order,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("revenue_attribution_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_revenue_attribution_allocation(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        revenue_attribution_identifier: "capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier.RevenueAttributionIdentifier",
        revenue_attribution_allocation_id: "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_id.RevenueAttributionAllocationId",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
        revenue_attribution_revision: Optional[
            "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
        ] = None,
    ) -> "capo_partnercentral_revenue_measurement.types.get_revenue_attribution_allocation_output.GetRevenueAttributionAllocationOutput":
        """<p>Retrieves a single allocation by its RevenueAttributionAllocationId. Supports optional point-in-time version queries.</p>

        Args:
            catalog: <p>The catalog that contains the resource.</p>
            revenue_attribution_identifier: <p>The revenue attribution identifier.</p>
            revenue_attribution_allocation_id: <p>The allocation identifier.</p>
            revenue_attribution_revision: <p>Point-in-time revision number to query.</p>

        Raises:
            capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_revenue_measurement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for GetRevenueAttributionAllocation

            >>> await client.get_revenue_attribution_allocation(catalog='AWS', revenue_attribution_identifier='ra-0a1b2c3d4e5f6', revenue_attribution_allocation_id='alloc-abc123def4567')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_revenue_measurement.types.get_revenue_attribution_allocation_input.GetRevenueAttributionAllocationInput]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_revenue_measurement.types.get_revenue_attribution_allocation_output.GetRevenueAttributionAllocationOutput"
        ]:
            import capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.get_revenue_attribution_allocation

            (
                output,
                http_response,
            ) = await capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.get_revenue_attribution_allocation.async_get_revenue_attribution_allocation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_revenue_measurement.types.get_revenue_attribution_allocation_input.GetRevenueAttributionAllocationInput = {
            "catalog": catalog,
            "revenue_attribution_identifier": revenue_attribution_identifier,
            "revenue_attribution_allocation_id": revenue_attribution_allocation_id,
        }
        if revenue_attribution_revision is not None:
            input_["revenue_attribution_revision"] = revenue_attribution_revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_revenue_attribution_allocations_task(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        revenue_attribution_identifier: "capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier.RevenueAttributionIdentifier",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
    ) -> "capo_partnercentral_revenue_measurement.types.get_revenue_attribution_allocations_task_output.GetRevenueAttributionAllocationsTaskOutput":
        """<p>Retrieves the current status of a previously submitted allocations task. When COMPLETE, includes the latest revision. When FAILED, includes error details.</p>

        Args:
            catalog: <p>The catalog that contains the resource.</p>
            revenue_attribution_identifier: <p>The revenue attribution identifier.</p>

        Raises:
            capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_revenue_measurement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for GetRevenueAttributionAllocationsTask

            >>> await client.get_revenue_attribution_allocations_task(catalog='AWS', revenue_attribution_identifier='ra-0a1b2c3d4e5f6')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_revenue_measurement.types.get_revenue_attribution_allocations_task_input.GetRevenueAttributionAllocationsTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_revenue_measurement.types.get_revenue_attribution_allocations_task_output.GetRevenueAttributionAllocationsTaskOutput"
        ]:
            import capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.get_revenue_attribution_allocations_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.get_revenue_attribution_allocations_task.async_get_revenue_attribution_allocations_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_revenue_measurement.types.get_revenue_attribution_allocations_task_input.GetRevenueAttributionAllocationsTaskInput = {
            "catalog": catalog,
            "revenue_attribution_identifier": revenue_attribution_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_revenue_attribution_allocations(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        revenue_attribution_identifier: "capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier.RevenueAttributionIdentifier",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
        entity_type_filters: Optional[
            "capo_partnercentral_revenue_measurement.types.entity_type_filter_list.EntityTypeFilterList"
        ] = None,
        entity_identifier_filters: Optional[
            "capo_partnercentral_revenue_measurement.types.entity_identifier_filter_list.EntityIdentifierFilterList"
        ] = None,
        customer_aws_account_id_filters: Optional[
            "capo_partnercentral_revenue_measurement.types.customer_aws_account_id_filter_list.CustomerAwsAccountIdFilterList"
        ] = None,
        status_filter: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_status.AllocationStatus"
        ] = None,
        after_effective_from: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
        ] = None,
        before_effective_from: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
        ] = None,
        after_effective_until: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
        ] = None,
        before_effective_until: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
        ] = None,
        sort_by: Optional[
            "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_sort_field.RevenueAttributionAllocationSortField"
        ] = None,
        sort_order: Optional[
            "capo_partnercentral_revenue_measurement.types.sort_order.SortOrder"
        ] = None,
        revenue_attribution_revision: Optional[
            "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_partnercentral_revenue_measurement.types.next_token.NextToken"
        ] = None,
    ) -> "capo_partnercentral_revenue_measurement.types.list_revenue_attribution_allocations_output.ListRevenueAttributionAllocationsOutput":
        """<p>Returns a paginated list of committed allocations with support for filtering by entity, customer, status, or date range.</p>

        Args:
            catalog: <p>The catalog that contains the resource.</p>
            revenue_attribution_identifier: <p>The revenue attribution identifier to query.</p>
            entity_type_filters: <p>Filter by deal entity types.</p>
            entity_identifier_filters: <p>Filter by deal entity identifiers.</p>
            customer_aws_account_id_filters: <p>Filter by customer AWS account IDs for associated deal entities.</p>
            status_filter: <p>Filter by allocation status.</p>
            after_effective_from: <p>Inclusive lower bound for EffectiveFrom date filter.</p>
            before_effective_from: <p>Exclusive upper bound for EffectiveFrom date filter (half-open range).</p>
            after_effective_until: <p>Inclusive lower bound for EffectiveUntil date filter.</p>
            before_effective_until: <p>Exclusive upper bound for EffectiveUntil date filter (half-open range).</p>
            sort_by: <p>Field to sort by.</p>
            sort_order: <p>Sort direction. Defaults to ASCENDING.</p>
            revenue_attribution_revision: <p>Point-in-time revision number to query.</p>
            max_results: <p>Maximum results per page.</p>
            next_token: <p>Pagination token from previous response.</p>

        Raises:
            capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_revenue_measurement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for ListRevenueAttributionAllocations

            >>> await client.list_revenue_attribution_allocations(catalog='AWS', revenue_attribution_identifier='ra-0a1b2c3d4e5f6')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_revenue_measurement.types.list_revenue_attribution_allocations_input.ListRevenueAttributionAllocationsInput]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_revenue_measurement.types.list_revenue_attribution_allocations_output.ListRevenueAttributionAllocationsOutput"
        ]:
            import capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.list_revenue_attribution_allocations

            (
                output,
                http_response,
            ) = await capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.list_revenue_attribution_allocations.async_list_revenue_attribution_allocations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_revenue_measurement.types.list_revenue_attribution_allocations_input.ListRevenueAttributionAllocationsInput = {
            "catalog": catalog,
            "revenue_attribution_identifier": revenue_attribution_identifier,
        }
        if entity_type_filters is not None:
            input_["entity_type_filters"] = entity_type_filters
        if entity_identifier_filters is not None:
            input_["entity_identifier_filters"] = entity_identifier_filters
        if customer_aws_account_id_filters is not None:
            input_["customer_aws_account_id_filters"] = customer_aws_account_id_filters
        if status_filter is not None:
            input_["status_filter"] = status_filter
        if after_effective_from is not None:
            input_["after_effective_from"] = after_effective_from
        if before_effective_from is not None:
            input_["before_effective_from"] = before_effective_from
        if after_effective_until is not None:
            input_["after_effective_until"] = after_effective_until
        if before_effective_until is not None:
            input_["before_effective_until"] = before_effective_until
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if revenue_attribution_revision is not None:
            input_["revenue_attribution_revision"] = revenue_attribution_revision
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

    async def iter_list_revenue_attribution_allocations(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        revenue_attribution_identifier: "capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier.RevenueAttributionIdentifier",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
        entity_type_filters: Optional[
            "capo_partnercentral_revenue_measurement.types.entity_type_filter_list.EntityTypeFilterList"
        ] = None,
        entity_identifier_filters: Optional[
            "capo_partnercentral_revenue_measurement.types.entity_identifier_filter_list.EntityIdentifierFilterList"
        ] = None,
        customer_aws_account_id_filters: Optional[
            "capo_partnercentral_revenue_measurement.types.customer_aws_account_id_filter_list.CustomerAwsAccountIdFilterList"
        ] = None,
        status_filter: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_status.AllocationStatus"
        ] = None,
        after_effective_from: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
        ] = None,
        before_effective_from: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
        ] = None,
        after_effective_until: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
        ] = None,
        before_effective_until: Optional[
            "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
        ] = None,
        sort_by: Optional[
            "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_sort_field.RevenueAttributionAllocationSortField"
        ] = None,
        sort_order: Optional[
            "capo_partnercentral_revenue_measurement.types.sort_order.SortOrder"
        ] = None,
        revenue_attribution_revision: Optional[
            "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_partnercentral_revenue_measurement.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_summary.RevenueAttributionAllocationSummary]":
        _token = next_token
        while True:
            _response = await self.list_revenue_attribution_allocations(
                catalog,
                revenue_attribution_identifier,
                config_overrides=config_overrides,
                entity_type_filters=entity_type_filters,
                entity_identifier_filters=entity_identifier_filters,
                customer_aws_account_id_filters=customer_aws_account_id_filters,
                status_filter=status_filter,
                after_effective_from=after_effective_from,
                before_effective_from=before_effective_from,
                after_effective_until=after_effective_until,
                before_effective_until=before_effective_until,
                sort_by=sort_by,
                sort_order=sort_order,
                revenue_attribution_revision=revenue_attribution_revision,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(
                _response, ("revenue_attribution_allocation_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_revenue_attribution_allocations_task(
        self,
        catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName",
        revenue_attribution_identifier: "capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier.RevenueAttributionIdentifier",
        revenue_attribution_revision: "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken",
        revenue_share_allocations: "capo_partnercentral_revenue_measurement.types.revenue_share_allocation_change_list.RevenueShareAllocationChangeList",
        *,
        config_overrides: Optional[
            AsyncPartnerCentralRevenueMeasurementClientConfig
        ] = None,
        client_token: Optional[
            "capo_partnercentral_revenue_measurement.types.client_token.ClientToken"
        ] = None,
        description: Optional[str] = None,
    ) -> "capo_partnercentral_revenue_measurement.types.start_revenue_attribution_allocations_task_output.StartRevenueAttributionAllocationsTaskOutput":
        """<p>Submits a batch of up to 250 allocation changes (CREATE and/or UPDATE) for asynchronous processing. Returns a TaskId for tracking.</p>

        Args:
            catalog: <p>The catalog context for this operation.</p>
            revenue_attribution_identifier: <p>The revenue attribution identifier.</p>
            revenue_attribution_revision: <p>Current revision of the revenue attribution for optimistic locking.</p>
            revenue_share_allocations: <p>The list of allocation changes to process in this batch.</p>
            client_token: <p>Idempotency token for deduplication and retry.</p>
            description: <p>Human-readable description of the batch.</p>

        Raises:
            capo_partnercentral_revenue_measurement.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_revenue_measurement.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_revenue_measurement.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_revenue_measurement.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Retry your request.</p>
            capo_partnercentral_revenue_measurement.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_revenue_measurement.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for StartRevenueAttributionAllocationsTask

            >>> await client.start_revenue_attribution_allocations_task(catalog='AWS', revenue_attribution_identifier='ra-0a1b2c3d4e5f6', revenue_attribution_revision='1', revenue_share_allocations=[{'Action': 'CREATE', 'EntityType': 'OFFER', 'EntityIdentifier': 'offer-abc123', 'CustomerAwsAccountId': '123456789012', 'RevenueSharePercent': '15.50', 'EffectiveFrom': '2026-07-01', 'EffectiveUntil': '2026-07-31'}], client_token='unique-token-123')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_revenue_measurement.types.start_revenue_attribution_allocations_task_input.StartRevenueAttributionAllocationsTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_revenue_measurement.types.start_revenue_attribution_allocations_task_output.StartRevenueAttributionAllocationsTaskOutput"
        ]:
            import capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.start_revenue_attribution_allocations_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_revenue_measurement._operations.partner_central_revenue_measurement.start_revenue_attribution_allocations_task.async_start_revenue_attribution_allocations_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_revenue_measurement.types.start_revenue_attribution_allocations_task_input.StartRevenueAttributionAllocationsTaskInput = {
            "catalog": catalog,
            "revenue_attribution_identifier": revenue_attribution_identifier,
            "revenue_attribution_revision": revenue_attribution_revision,
            "revenue_share_allocations": revenue_share_allocations,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description

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
