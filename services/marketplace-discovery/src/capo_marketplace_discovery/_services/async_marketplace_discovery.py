"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#AWSMarketplaceDiscovery``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_marketplace_discovery._auth._signers
import capo_marketplace_discovery._auth._sigv4
from capo_marketplace_discovery._auth._identity import Credentials
from capo_marketplace_discovery._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_marketplace_discovery._auth._zapros_handler import AuthMiddleware
from capo_marketplace_discovery._pagination import resolve_path as _resolve_path
from capo_marketplace_discovery._services._aws_config import aaws_config
from capo_marketplace_discovery._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.facet_type_list
    import capo_marketplace_discovery.types.fulfillment_option
    import capo_marketplace_discovery.types.get_listing_input
    import capo_marketplace_discovery.types.get_listing_output
    import capo_marketplace_discovery.types.get_offer_input
    import capo_marketplace_discovery.types.get_offer_output
    import capo_marketplace_discovery.types.get_offer_set_input
    import capo_marketplace_discovery.types.get_offer_set_output
    import capo_marketplace_discovery.types.get_offer_terms_input
    import capo_marketplace_discovery.types.get_offer_terms_output
    import capo_marketplace_discovery.types.get_product_input
    import capo_marketplace_discovery.types.get_product_output
    import capo_marketplace_discovery.types.list_fulfillment_options_input
    import capo_marketplace_discovery.types.list_fulfillment_options_output
    import capo_marketplace_discovery.types.list_purchase_options_input
    import capo_marketplace_discovery.types.list_purchase_options_output
    import capo_marketplace_discovery.types.listing_facet_list
    import capo_marketplace_discovery.types.listing_id
    import capo_marketplace_discovery.types.listing_summary
    import capo_marketplace_discovery.types.locale
    import capo_marketplace_discovery.types.max_results
    import capo_marketplace_discovery.types.next_token
    import capo_marketplace_discovery.types.offer_id
    import capo_marketplace_discovery.types.offer_set_id
    import capo_marketplace_discovery.types.offer_term
    import capo_marketplace_discovery.types.product_id
    import capo_marketplace_discovery.types.purchase_option_filter_list
    import capo_marketplace_discovery.types.purchase_option_summary
    import capo_marketplace_discovery.types.search_facet_type
    import capo_marketplace_discovery.types.search_facets_input
    import capo_marketplace_discovery.types.search_facets_output
    import capo_marketplace_discovery.types.search_filter_list
    import capo_marketplace_discovery.types.search_listings_input
    import capo_marketplace_discovery.types.search_listings_output
    import capo_marketplace_discovery.types.search_listings_sort_by
    import capo_marketplace_discovery.types.search_listings_sort_order
    import capo_marketplace_discovery.types.search_text


class AsyncMarketplaceDiscoveryClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncMarketplaceDiscoveryClient:
    """A client for the ``MarketplaceDiscovery`` service.

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
        self._config = AsyncMarketplaceDiscoveryClientConfig(
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
        self, config_overrides: Optional[AsyncMarketplaceDiscoveryClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMarketplaceDiscoveryClientConfig = config_overrides or {}
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

    async def get_listing(
        self,
        listing_id: "capo_marketplace_discovery.types.listing_id.ListingId",
        *,
        config_overrides: Optional[AsyncMarketplaceDiscoveryClientConfig] = None,
        locale: Optional["capo_marketplace_discovery.types.locale.Locale"] = None,
    ) -> "capo_marketplace_discovery.types.get_listing_output.GetListingOutput":
        """<p>Provides details about a listing, such as descriptions, badges, categories, pricing model summaries, reviews, and associated products and offers.</p>

        Args:
            locale: <p>A BCP 47 language tag or comma-separated priority list specifying the preferred locale for response content. See <code>Locale</code> for supported values, constraints, fallback behavior, and the default locale. If omitted, the service returns content in the default locale.</p>
            listing_id: <p>The unique identifier of the listing to retrieve.</p>

        Raises:
            capo_marketplace_discovery.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_marketplace_discovery.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of the request.</p>
            capo_marketplace_discovery.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_marketplace_discovery.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_discovery.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_marketplace_discovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetListing for SaaS listing

            >>> await client.get_listing(locale='en-US', listing_id='prodview-sampleSaasId')
            GetListing for AMI listing with video

            >>> await client.get_listing(locale='en-US', listing_id='prodview-sampleAmiId')
            GetListing for multi-product listing

            >>> await client.get_listing(locale='en-US', listing_id='prodview-sampleMultiProductId')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_discovery.types.get_listing_input.GetListingInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_discovery.types.get_listing_output.GetListingOutput"
        ]:
            import capo_marketplace_discovery._operations.aws_marketplace_discovery.get_listing

            (
                output,
                http_response,
            ) = await capo_marketplace_discovery._operations.aws_marketplace_discovery.get_listing.async_get_listing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_discovery.types.get_listing_input.GetListingInput = {
            "listing_id": listing_id
        }
        if locale is not None:
            input_["locale"] = locale

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_offer(
        self,
        offer_id: "capo_marketplace_discovery.types.offer_id.OfferId",
        *,
        config_overrides: Optional[AsyncMarketplaceDiscoveryClientConfig] = None,
        locale: Optional["capo_marketplace_discovery.types.locale.Locale"] = None,
    ) -> "capo_marketplace_discovery.types.get_offer_output.GetOfferOutput":
        """<p>Provides details about an offer, such as the pricing model, seller of record, availability dates, badges, and associated products.</p>

        Args:
            locale: <p>A BCP 47 language tag or comma-separated priority list specifying the preferred locale for response content. See <code>Locale</code> for supported values, constraints, fallback behavior, and the default locale. If omitted, the service returns content in the default locale.</p>
            offer_id: <p>The unique identifier of the offer to retrieve.</p>

        Raises:
            capo_marketplace_discovery.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_marketplace_discovery.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of the request.</p>
            capo_marketplace_discovery.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_marketplace_discovery.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_discovery.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_marketplace_discovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetOffer for Contract Pricing offer

            >>> await client.get_offer(locale='en-US', offer_id='offer-sampleContractId')
            Invoke GetOffer for Usage Pricing offer

            >>> await client.get_offer(locale='en-US', offer_id='offer-sampleUsageId')
            Invoke GetOffer for BYOL Pricing offer

            >>> await client.get_offer(locale='en-US', offer_id='offer-sampleByolId')
            Invoke GetOffer for FREE Pricing offer

            >>> await client.get_offer(locale='en-US', offer_id='offer-sampleFreeId')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_discovery.types.get_offer_input.GetOfferInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_discovery.types.get_offer_output.GetOfferOutput"
        ]:
            import capo_marketplace_discovery._operations.aws_marketplace_discovery.get_offer

            (
                output,
                http_response,
            ) = await capo_marketplace_discovery._operations.aws_marketplace_discovery.get_offer.async_get_offer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_discovery.types.get_offer_input.GetOfferInput = {
            "offer_id": offer_id
        }
        if locale is not None:
            input_["locale"] = locale

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_offer_set(
        self,
        offer_set_id: "capo_marketplace_discovery.types.offer_set_id.OfferSetId",
        *,
        config_overrides: Optional[AsyncMarketplaceDiscoveryClientConfig] = None,
        locale: Optional["capo_marketplace_discovery.types.locale.Locale"] = None,
    ) -> "capo_marketplace_discovery.types.get_offer_set_output.GetOfferSetOutput":
        """<p>Provides details about an offer set, which is a bundle of offers across multiple products. Includes the seller, availability dates, buyer notes, and associated product-offer pairs.</p>

        Args:
            locale: <p>A BCP 47 language tag or comma-separated priority list specifying the preferred locale for response content. See <code>Locale</code> for supported values, constraints, fallback behavior, and the default locale. If omitted, the service returns content in the default locale.</p>
            offer_set_id: <p>The unique identifier of the offer set to retrieve.</p>

        Raises:
            capo_marketplace_discovery.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_marketplace_discovery.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of the request.</p>
            capo_marketplace_discovery.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_marketplace_discovery.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_discovery.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_marketplace_discovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get offer set with multiple products

            >>> await client.get_offer_set(locale='en-US', offer_set_id='offerset-sampleId')
            Get offer set with only required fields

            >>> await client.get_offer_set(offer_set_id='offerset-sampleMinimalId')
            Get offer set that never expires from a first-party seller

            >>> await client.get_offer_set(locale='en-US', offer_set_id='offerset-samplePerpetualId')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_discovery.types.get_offer_set_input.GetOfferSetInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_discovery.types.get_offer_set_output.GetOfferSetOutput"
        ]:
            import capo_marketplace_discovery._operations.aws_marketplace_discovery.get_offer_set

            (
                output,
                http_response,
            ) = await capo_marketplace_discovery._operations.aws_marketplace_discovery.get_offer_set.async_get_offer_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_discovery.types.get_offer_set_input.GetOfferSetInput = {
            "offer_set_id": offer_set_id
        }
        if locale is not None:
            input_["locale"] = locale

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_offer_terms(
        self,
        offer_id: "capo_marketplace_discovery.types.offer_id.OfferId",
        *,
        config_overrides: Optional[AsyncMarketplaceDiscoveryClientConfig] = None,
        locale: Optional["capo_marketplace_discovery.types.locale.Locale"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> "capo_marketplace_discovery.types.get_offer_terms_output.GetOfferTermsOutput":
        """<p>Returns the terms attached to an offer, such as pricing terms (usage-based, contract, BYOL, free trial), legal terms, payment schedules, validity terms, support terms, and renewal terms.</p>

        Args:
            locale: <p>A BCP 47 language tag or comma-separated priority list specifying the preferred locale for response content. See <code>Locale</code> for supported values, constraints, fallback behavior, and the default locale. If omitted, the service returns content in the default locale.</p>
            offer_id: <p>The unique identifier of the offer whose terms to retrieve.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to get more results.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>

        Raises:
            capo_marketplace_discovery.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_marketplace_discovery.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of the request.</p>
            capo_marketplace_discovery.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_marketplace_discovery.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_discovery.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_marketplace_discovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetOfferTerms for Usage-based ML Model offer

            >>> await client.get_offer_terms(locale='en-US', offer_id='offer-sampleUsageBasedId')
            GetOfferTerms for BYOL offer

            >>> await client.get_offer_terms(locale='en-US', offer_id='offer-sampleByolId')
            GetOfferTerms for configurable upfront pricing

            >>> await client.get_offer_terms(locale='en-US', offer_id='offer-sampleConfigUpfrontId')
            GetOfferTerms for free trial offer

            >>> await client.get_offer_terms(locale='en-US', offer_id='offer-sampleFreeTrialId')
            GetOfferTerms for recurring payment

            >>> await client.get_offer_terms(locale='en-US', offer_id='offer-sampleRecurringId')
            GetOfferTerms for variable payment

            >>> await client.get_offer_terms(locale='en-US', offer_id='offer-sampleVariableId')
            GetOfferTerms for renewal term

            >>> await client.get_offer_terms(locale='en-US', offer_id='offer-sampleRenewalId')
            GetOfferTerms for renewal term with fixed percentage

            >>> await client.get_offer_terms(locale='en-US', offer_id='offer-sampleRenewalFixedId')
            GetOfferTerms for renewal term with identical pricing (no price increase)

            >>> await client.get_offer_terms(locale='en-US', offer_id='offer-sampleRenewalNoPriceIncreaseId')
            GetOfferTerms for support term

            >>> await client.get_offer_terms(locale='en-US', offer_id='offer-sampleSupportId')
            GetOfferTerms for validity term with dates

            >>> await client.get_offer_terms(locale='en-US', offer_id='offer-sampleValidityId')
            GetOfferTerms for net payment term

            >>> await client.get_offer_terms(locale='en-US', offer_id='offer-sampleNetPaymentId')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_discovery.types.get_offer_terms_input.GetOfferTermsInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_discovery.types.get_offer_terms_output.GetOfferTermsOutput"
        ]:
            import capo_marketplace_discovery._operations.aws_marketplace_discovery.get_offer_terms

            (
                output,
                http_response,
            ) = await capo_marketplace_discovery._operations.aws_marketplace_discovery.get_offer_terms.async_get_offer_terms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_discovery.types.get_offer_terms_input.GetOfferTermsInput = {
            "offer_id": offer_id
        }
        if locale is not None:
            input_["locale"] = locale
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

    async def iter_get_offer_terms(
        self,
        offer_id: "capo_marketplace_discovery.types.offer_id.OfferId",
        *,
        config_overrides: Optional[AsyncMarketplaceDiscoveryClientConfig] = None,
        locale: Optional["capo_marketplace_discovery.types.locale.Locale"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_marketplace_discovery.types.offer_term.OfferTerm]":
        _token = next_token
        while True:
            _response = await self.get_offer_terms(
                offer_id,
                config_overrides=config_overrides,
                locale=locale,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("offer_terms",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_product(
        self,
        product_id: "capo_marketplace_discovery.types.product_id.ProductId",
        *,
        config_overrides: Optional[AsyncMarketplaceDiscoveryClientConfig] = None,
        locale: Optional["capo_marketplace_discovery.types.locale.Locale"] = None,
    ) -> "capo_marketplace_discovery.types.get_product_output.GetProductOutput":
        """<p>Provides details about a product, such as descriptions, highlights, categories, fulfillment option summaries, promotional media, and seller engagement options.</p>

        Args:
            locale: <p>A BCP 47 language tag or comma-separated priority list specifying the preferred locale for response content. See <code>Locale</code> for supported values, constraints, fallback behavior, and the default locale. If omitted, the service returns content in the default locale.</p>
            product_id: <p>The unique identifier of the product to retrieve.</p>

        Raises:
            capo_marketplace_discovery.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_marketplace_discovery.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of the request.</p>
            capo_marketplace_discovery.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_marketplace_discovery.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_discovery.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_marketplace_discovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetProduct for SaaS product with DEPLOYED status

            >>> await client.get_product(locale='en-US', product_id='prod-sampleSaasId')
            GetProduct for AMI product with NOT_DEPLOYED status

            >>> await client.get_product(locale='en-US', product_id='prod-sampleAmiId')
            GetProduct for professional services with NOT_APPLICABLE status

            >>> await client.get_product(locale='en-US', product_id='prod-sampleProServId')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_discovery.types.get_product_input.GetProductInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_discovery.types.get_product_output.GetProductOutput"
        ]:
            import capo_marketplace_discovery._operations.aws_marketplace_discovery.get_product

            (
                output,
                http_response,
            ) = await capo_marketplace_discovery._operations.aws_marketplace_discovery.get_product.async_get_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_discovery.types.get_product_input.GetProductInput = {
            "product_id": product_id
        }
        if locale is not None:
            input_["locale"] = locale

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_fulfillment_options(
        self,
        product_id: "capo_marketplace_discovery.types.product_id.ProductId",
        *,
        config_overrides: Optional[AsyncMarketplaceDiscoveryClientConfig] = None,
        locale: Optional["capo_marketplace_discovery.types.locale.Locale"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> "capo_marketplace_discovery.types.list_fulfillment_options_output.ListFulfillmentOptionsOutput":
        """<p>Returns the fulfillment options available for a product, including deployment details such as version information, operating systems, usage instructions, and release notes.</p>

        Args:
            locale: <p>A BCP 47 language tag or comma-separated priority list specifying the preferred locale for response content. See <code>Locale</code> for supported values, constraints, fallback behavior, and the default locale. If omitted, the service returns content in the default locale.</p>
            product_id: <p>The unique identifier of the product for which to list fulfillment options.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to get more results.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>

        Raises:
            capo_marketplace_discovery.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_marketplace_discovery.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of the request.</p>
            capo_marketplace_discovery.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_marketplace_discovery.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_discovery.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_marketplace_discovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List AMI Fulfillment Options

            >>> await client.list_fulfillment_options(locale='en-US', product_id='prod-sampleAmiId')
            List API Fulfillment Options

            >>> await client.list_fulfillment_options(locale='en-US', product_id='prod-sampleApiId')
            List API Fulfillment Options with Dynamic Endpoint

            >>> await client.list_fulfillment_options(locale='en-US', product_id='prod-sampleApiDynamicId')
            List CloudFormation Template Fulfillment Options

            >>> await client.list_fulfillment_options(locale='en-US', product_id='prod-sampleCftId')
            List Container Fulfillment Options

            >>> await client.list_fulfillment_options(locale='en-US', product_id='prod-sampleContainerId')
            List Helm Fulfillment Options

            >>> await client.list_fulfillment_options(locale='en-US', product_id='prod-sampleHelmId')
            List EKS Add-On Fulfillment Options

            >>> await client.list_fulfillment_options(locale='en-US', product_id='prod-sampleEksId')
            List EC2 Image Builder Component Fulfillment Options

            >>> await client.list_fulfillment_options(locale='en-US', product_id='prod-sampleImageBuilderId')
            List Data Exchange Fulfillment Options

            >>> await client.list_fulfillment_options(locale='en-US', product_id='prod-sampleDataExchangeId')
            List Professional Services Fulfillment Options

            >>> await client.list_fulfillment_options(locale='en-US', product_id='prod-sampleProServId')
            List SaaS Fulfillment Options

            >>> await client.list_fulfillment_options(locale='en-US', product_id='prod-sampleSaasId')
            List SageMaker Algorithm Fulfillment Options

            >>> await client.list_fulfillment_options(locale='en-US', product_id='prod-sampleSmAlgoId')
            List SageMaker Model Fulfillment Options

            >>> await client.list_fulfillment_options(locale='en-US', product_id='prod-sampleSmModelId')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_discovery.types.list_fulfillment_options_input.ListFulfillmentOptionsInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_discovery.types.list_fulfillment_options_output.ListFulfillmentOptionsOutput"
        ]:
            import capo_marketplace_discovery._operations.aws_marketplace_discovery.list_fulfillment_options

            (
                output,
                http_response,
            ) = await capo_marketplace_discovery._operations.aws_marketplace_discovery.list_fulfillment_options.async_list_fulfillment_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_discovery.types.list_fulfillment_options_input.ListFulfillmentOptionsInput = {
            "product_id": product_id
        }
        if locale is not None:
            input_["locale"] = locale
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

    async def iter_list_fulfillment_options(
        self,
        product_id: "capo_marketplace_discovery.types.product_id.ProductId",
        *,
        config_overrides: Optional[AsyncMarketplaceDiscoveryClientConfig] = None,
        locale: Optional["capo_marketplace_discovery.types.locale.Locale"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_marketplace_discovery.types.fulfillment_option.FulfillmentOption]":
        _token = next_token
        while True:
            _response = await self.list_fulfillment_options(
                product_id,
                config_overrides=config_overrides,
                locale=locale,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("fulfillment_options",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_purchase_options(
        self,
        *,
        config_overrides: Optional[AsyncMarketplaceDiscoveryClientConfig] = None,
        locale: Optional["capo_marketplace_discovery.types.locale.Locale"] = None,
        filters: Optional[
            "capo_marketplace_discovery.types.purchase_option_filter_list.PurchaseOptionFilterList"
        ] = None,
        max_results: Optional[
            "capo_marketplace_discovery.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> "capo_marketplace_discovery.types.list_purchase_options_output.ListPurchaseOptionsOutput":
        """<p>Returns the purchase options (offers and offer sets) available to the buyer. You can filter results by product, seller, purchase option type, visibility scope, and availability status.</p> <note> <p>You must include at least one of the following filters in the request: a <code>PRODUCT_ID</code> filter to specify the product for which to retrieve purchase options, or a <code>VISIBILITY_SCOPE</code> filter to retrieve purchase options by visibility.</p> </note>

        Args:
            locale: <p>A BCP 47 language tag or comma-separated priority list specifying the preferred locale for response content. See <code>Locale</code> for supported values, constraints, fallback behavior, and the default locale. If omitted, the service returns content in the default locale.</p>
            filters: <p>Filters to narrow the results. Multiple filters are combined with AND logic. Multiple values within the same filter are combined with OR logic.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to get more results.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>

        Raises:
            capo_marketplace_discovery.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_marketplace_discovery.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of the request.</p>
            capo_marketplace_discovery.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_marketplace_discovery.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_discovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Filter by Product ID

            >>> await client.list_purchase_options(locale='en-US', filters=[{'filterType': 'PRODUCT_ID', 'filterValues': ['prod-sampleOfferId']}])
            Filter by Seller with Private Offerset

            >>> await client.list_purchase_options(locale='en-US', filters=[{'filterType': 'SELLER_OF_RECORD_PROFILE_ID', 'filterValues': ['seller-sampleResellerId']}, {'filterType': 'PURCHASE_OPTION_TYPE', 'filterValues': ['OFFERSET']}, {'filterType': 'VISIBILITY_SCOPE', 'filterValues': ['PRIVATE']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_discovery.types.list_purchase_options_input.ListPurchaseOptionsInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_discovery.types.list_purchase_options_output.ListPurchaseOptionsOutput"
        ]:
            import capo_marketplace_discovery._operations.aws_marketplace_discovery.list_purchase_options

            (
                output,
                http_response,
            ) = await capo_marketplace_discovery._operations.aws_marketplace_discovery.list_purchase_options.async_list_purchase_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_discovery.types.list_purchase_options_input.ListPurchaseOptionsInput = {}
        if locale is not None:
            input_["locale"] = locale
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_purchase_options(
        self,
        *,
        config_overrides: Optional[AsyncMarketplaceDiscoveryClientConfig] = None,
        locale: Optional["capo_marketplace_discovery.types.locale.Locale"] = None,
        filters: Optional[
            "capo_marketplace_discovery.types.purchase_option_filter_list.PurchaseOptionFilterList"
        ] = None,
        max_results: Optional[
            "capo_marketplace_discovery.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_marketplace_discovery.types.purchase_option_summary.PurchaseOptionSummary]":
        _token = next_token
        while True:
            _response = await self.list_purchase_options(
                config_overrides=config_overrides,
                locale=locale,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("purchase_options",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def search_facets(
        self,
        *,
        config_overrides: Optional[AsyncMarketplaceDiscoveryClientConfig] = None,
        locale: Optional["capo_marketplace_discovery.types.locale.Locale"] = None,
        search_text: Optional[
            "capo_marketplace_discovery.types.search_text.SearchText"
        ] = None,
        filters: Optional[
            "capo_marketplace_discovery.types.search_filter_list.SearchFilterList"
        ] = None,
        facet_types: Optional[
            "capo_marketplace_discovery.types.facet_type_list.FacetTypeList"
        ] = None,
        next_token: Optional[
            "capo_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> "capo_marketplace_discovery.types.search_facets_output.SearchFacetsOutput":
        """<p>Returns available facet values for filtering listings, such as categories, pricing models, fulfillment option types, publishers, and customer ratings. Each facet value includes a count of matching listings.</p>

        Args:
            locale: <p>A BCP 47 language tag or comma-separated priority list specifying the preferred locale for response content. See <code>Locale</code> for supported values, constraints, fallback behavior, and the default locale. If omitted, the service returns content in the default locale.</p>
            search_text: <p>The search query text to filter listings before retrieving facets.</p>
            filters: <p>Filters to apply before retrieving facets. Multiple filters are combined with AND logic. Multiple values within the same filter are combined with OR logic.</p>
            facet_types: <p>A list of specific facet types to retrieve. If empty or null, all available facets are returned.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>

        Raises:
            capo_marketplace_discovery.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_marketplace_discovery.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of the request.</p>
            capo_marketplace_discovery.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_marketplace_discovery.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_discovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get facets for machine learning category
            Retrieve available facet values for listings in the machine learning category

            >>> await client.search_facets(locale='en-US', search_text='analytics', filters=[{'filterType': 'CATEGORY', 'filterValues': ['machine-learning']}], facet_types=['FULFILLMENT_OPTION_TYPE', 'PRICING_MODEL'])
            Get facets with term and rating range filters
            Retrieve facets for security listings with ratings between 3.0 and 5.0 stars

            >>> await client.search_facets(locale='en-US', filters=[{'filterType': 'CATEGORY', 'filterValues': ['security']}, {'filterType': 'MIN_AVERAGE_CUSTOMER_RATING', 'filterValues': ['3.0']}, {'filterType': 'MAX_AVERAGE_CUSTOMER_RATING', 'filterValues': ['5.0']}], facet_types=['PRICING_MODEL', 'AVERAGE_CUSTOMER_RATING'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_discovery.types.search_facets_input.SearchFacetsInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_discovery.types.search_facets_output.SearchFacetsOutput"
        ]:
            import capo_marketplace_discovery._operations.aws_marketplace_discovery.search_facets

            (
                output,
                http_response,
            ) = await capo_marketplace_discovery._operations.aws_marketplace_discovery.search_facets.async_search_facets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_discovery.types.search_facets_input.SearchFacetsInput = {}
        if locale is not None:
            input_["locale"] = locale
        if search_text is not None:
            input_["search_text"] = search_text
        if filters is not None:
            input_["filters"] = filters
        if facet_types is not None:
            input_["facet_types"] = facet_types
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_search_facets(
        self,
        *,
        config_overrides: Optional[AsyncMarketplaceDiscoveryClientConfig] = None,
        locale: Optional["capo_marketplace_discovery.types.locale.Locale"] = None,
        search_text: Optional[
            "capo_marketplace_discovery.types.search_text.SearchText"
        ] = None,
        filters: Optional[
            "capo_marketplace_discovery.types.search_filter_list.SearchFilterList"
        ] = None,
        facet_types: Optional[
            "capo_marketplace_discovery.types.facet_type_list.FacetTypeList"
        ] = None,
        next_token: Optional[
            "capo_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[tuple[capo_marketplace_discovery.types.search_facet_type.SearchFacetType, capo_marketplace_discovery.types.listing_facet_list.ListingFacetList]]":
        _token = next_token
        while True:
            _response = await self.search_facets(
                config_overrides=config_overrides,
                locale=locale,
                search_text=search_text,
                filters=filters,
                facet_types=facet_types,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("listing_facets",))
            for _k, _v in (_page or {}).items():
                yield (_k, _v)
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def search_listings(
        self,
        *,
        config_overrides: Optional[AsyncMarketplaceDiscoveryClientConfig] = None,
        locale: Optional["capo_marketplace_discovery.types.locale.Locale"] = None,
        search_text: Optional[
            "capo_marketplace_discovery.types.search_text.SearchText"
        ] = None,
        filters: Optional[
            "capo_marketplace_discovery.types.search_filter_list.SearchFilterList"
        ] = None,
        max_results: Optional[
            "capo_marketplace_discovery.types.max_results.MaxResults"
        ] = None,
        sort_by: Optional[
            "capo_marketplace_discovery.types.search_listings_sort_by.SearchListingsSortBy"
        ] = None,
        sort_order: Optional[
            "capo_marketplace_discovery.types.search_listings_sort_order.SearchListingsSortOrder"
        ] = None,
        next_token: Optional[
            "capo_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> "capo_marketplace_discovery.types.search_listings_output.SearchListingsOutput":
        """<p>Returns a list of product listings based on search criteria and filters. You can search by keyword, filter by category, pricing model, fulfillment type, and other attributes, and sort results by relevance or customer rating.</p>

        Args:
            locale: <p>A BCP 47 language tag or comma-separated priority list specifying the preferred locale for response content. See <code>Locale</code> for supported values, constraints, fallback behavior, and the default locale. If omitted, the service returns content in the default locale.</p>
            search_text: <p>The search query text to find relevant listings.</p>
            filters: <p>Filters to narrow search results. Multiple filters are combined with AND logic. Multiple values within the same filter are combined with OR logic.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to get more results.</p>
            sort_by: <p>The field to sort results by. Valid values are <code>RELEVANCE</code> and <code>AVERAGE_CUSTOMER_RATING</code>.</p>
            sort_order: <p>The sort direction. Valid values are <code>DESCENDING</code> and <code>ASCENDING</code>.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>

        Raises:
            capo_marketplace_discovery.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_marketplace_discovery.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of the request.</p>
            capo_marketplace_discovery.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_marketplace_discovery.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_marketplace_discovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Search for machine learning listings
            Search for SaaS listings in the machine learning category with sorting by relevance

            >>> await client.search_listings(locale='en-US', search_text='computer vision', filters=[{'filterType': 'CATEGORY', 'filterValues': ['machine-learning']}, {'filterType': 'FULFILLMENT_OPTION_TYPE', 'filterValues': ['SAAS']}], max_results=25, sort_by='RELEVANCE', sort_order='DESCENDING')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_discovery.types.search_listings_input.SearchListingsInput]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_discovery.types.search_listings_output.SearchListingsOutput"
        ]:
            import capo_marketplace_discovery._operations.aws_marketplace_discovery.search_listings

            (
                output,
                http_response,
            ) = await capo_marketplace_discovery._operations.aws_marketplace_discovery.search_listings.async_search_listings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_discovery.types.search_listings_input.SearchListingsInput = {}
        if locale is not None:
            input_["locale"] = locale
        if search_text is not None:
            input_["search_text"] = search_text
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_search_listings(
        self,
        *,
        config_overrides: Optional[AsyncMarketplaceDiscoveryClientConfig] = None,
        locale: Optional["capo_marketplace_discovery.types.locale.Locale"] = None,
        search_text: Optional[
            "capo_marketplace_discovery.types.search_text.SearchText"
        ] = None,
        filters: Optional[
            "capo_marketplace_discovery.types.search_filter_list.SearchFilterList"
        ] = None,
        max_results: Optional[
            "capo_marketplace_discovery.types.max_results.MaxResults"
        ] = None,
        sort_by: Optional[
            "capo_marketplace_discovery.types.search_listings_sort_by.SearchListingsSortBy"
        ] = None,
        sort_order: Optional[
            "capo_marketplace_discovery.types.search_listings_sort_order.SearchListingsSortOrder"
        ] = None,
        next_token: Optional[
            "capo_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> (
        "AsyncIterator[capo_marketplace_discovery.types.listing_summary.ListingSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.search_listings(
                config_overrides=config_overrides,
                locale=locale,
                search_text=search_text,
                filters=filters,
                max_results=max_results,
                sort_by=sort_by,
                sort_order=sort_order,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("listing_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
