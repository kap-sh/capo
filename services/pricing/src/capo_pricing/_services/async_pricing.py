"""Generated from Smithy shape ``com.amazonaws.pricing#AWSPriceListService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_pricing._auth._signers
import capo_pricing._auth._sigv4
from capo_pricing._auth._identity import Credentials
from capo_pricing._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_pricing._auth._zapros_handler import AuthMiddleware
from capo_pricing._pagination import resolve_path as _resolve_path
from capo_pricing._services._aws_config import aaws_config
from capo_pricing._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_pricing.types.attribute_value
    import capo_pricing.types.currency_code
    import capo_pricing.types.describe_services_max_results
    import capo_pricing.types.describe_services_request
    import capo_pricing.types.describe_services_response
    import capo_pricing.types.effective_date
    import capo_pricing.types.file_format
    import capo_pricing.types.filters
    import capo_pricing.types.format_version
    import capo_pricing.types.get_attribute_values_max_results
    import capo_pricing.types.get_attribute_values_request
    import capo_pricing.types.get_attribute_values_response
    import capo_pricing.types.get_price_list_file_url_request
    import capo_pricing.types.get_price_list_file_url_response
    import capo_pricing.types.get_products_max_results
    import capo_pricing.types.get_products_request
    import capo_pricing.types.get_products_response
    import capo_pricing.types.list_price_lists_request
    import capo_pricing.types.list_price_lists_response
    import capo_pricing.types.max_results
    import capo_pricing.types.price_list
    import capo_pricing.types.price_list_arn
    import capo_pricing.types.region_code
    import capo_pricing.types.service
    import capo_pricing.types.service_code
    import capo_pricing.types.string
    import capo_pricing.types.synthesized_json_price_list_json_item


class AsyncPricingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncPricingClient:
    """A client for the ``Pricing`` service.

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
        self._config = AsyncPricingClientConfig(
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
        self, config_overrides: Optional[AsyncPricingClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPricingClientConfig = config_overrides or {}
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

    async def describe_services(
        self,
        *,
        config_overrides: Optional[AsyncPricingClientConfig] = None,
        service_code: Optional["capo_pricing.types.string.String"] = None,
        format_version: Optional[
            "capo_pricing.types.format_version.FormatVersion"
        ] = None,
        next_token: Optional["capo_pricing.types.string.String"] = None,
        max_results: Optional[
            "capo_pricing.types.describe_services_max_results.DescribeServicesMaxResults"
        ] = None,
    ) -> "capo_pricing.types.describe_services_response.DescribeServicesResponse":
        """<p>Returns the metadata for one service or a list of the metadata for all services. Use this without a service code to get the service codes for all services. Use it with a service code, such as <code>AmazonEC2</code>, to get information specific to that service, such as the attribute names available for that service. For example, some of the attribute names available for EC2 are <code>volumeType</code>, <code>maxIopsVolume</code>, <code>operation</code>, <code>locationType</code>, and <code>instanceCapacity10xlarge</code>.</p>

        Args:
            service_code: <p>The code for the service whose information you want to retrieve, such as <code>AmazonEC2</code>. You can use the <code>ServiceCode</code> to filter the results in a <code>GetProducts</code> call. To retrieve a list of all services, leave this blank.</p>
            format_version: <p>The format version that you want the response to be in.</p> <p>Valid values are: <code>aws_v1</code> </p>
            next_token: <p>The pagination token that indicates the next set of results that you want to retrieve.</p>
            max_results: <p>The maximum number of results that you want returned in the response.</p>

        Raises:
            capo_pricing.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request wasn't signed correctly.</p>
            capo_pricing.errors.expired_next_token_exception.ExpiredNextTokenException: <p>The pagination token expired. Try again without a pagination token.</p>
            capo_pricing.errors.internal_error_exception.InternalErrorException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_pricing.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_pricing.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters had an invalid value.</p>
            capo_pricing.errors.not_found_exception.NotFoundException: <p>The requested resource can't be found.</p>
            capo_pricing.errors.throttling_exception.ThrottlingException: <p>You've made too many requests exceeding service quotas. </p>
            capo_pricing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve a list of services and service codes
            Retrieves the service for the given Service Code.

            >>> await client.describe_services(service_code='AmazonEC2', format_version='aws_v1', max_results=1)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pricing.types.describe_services_request.DescribeServicesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pricing.types.describe_services_response.DescribeServicesResponse"
        ]:
            import capo_pricing._operations.aws_price_list_service.describe_services

            (
                output,
                http_response,
            ) = await capo_pricing._operations.aws_price_list_service.describe_services.async_describe_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pricing.types.describe_services_request.DescribeServicesRequest = {}
        if service_code is not None:
            input_["service_code"] = service_code
        if format_version is not None:
            input_["format_version"] = format_version
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

    async def iter_describe_services(
        self,
        *,
        config_overrides: Optional[AsyncPricingClientConfig] = None,
        service_code: Optional["capo_pricing.types.string.String"] = None,
        format_version: Optional[
            "capo_pricing.types.format_version.FormatVersion"
        ] = None,
        next_token: Optional["capo_pricing.types.string.String"] = None,
        max_results: Optional[
            "capo_pricing.types.describe_services_max_results.DescribeServicesMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_pricing.types.service.Service]":
        _token = next_token
        while True:
            _response = await self.describe_services(
                config_overrides=config_overrides,
                service_code=service_code,
                format_version=format_version,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("services",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_attribute_values(
        self,
        service_code: "capo_pricing.types.string.String",
        attribute_name: "capo_pricing.types.string.String",
        *,
        config_overrides: Optional[AsyncPricingClientConfig] = None,
        next_token: Optional["capo_pricing.types.string.String"] = None,
        max_results: Optional[
            "capo_pricing.types.get_attribute_values_max_results.GetAttributeValuesMaxResults"
        ] = None,
    ) -> "capo_pricing.types.get_attribute_values_response.GetAttributeValuesResponse":
        """<p>Returns a list of attribute values. Attributes are similar to the details in a Price List API offer file. For a list of available attributes, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/reading-an-offer.html#pps-defs">Offer File Definitions</a> in the <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html">Billing and Cost Management User Guide</a>.</p>

        Args:
            service_code: <p>The service code for the service whose attributes you want to retrieve. For example, if you want the retrieve an EC2 attribute, use <code>AmazonEC2</code>.</p>
            attribute_name: <p>The name of the attribute that you want to retrieve the values for, such as <code>volumeType</code>.</p>
            next_token: <p>The pagination token that indicates the next set of results that you want to retrieve.</p>
            max_results: <p>The maximum number of results to return in response.</p>

        Raises:
            capo_pricing.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request wasn't signed correctly.</p>
            capo_pricing.errors.expired_next_token_exception.ExpiredNextTokenException: <p>The pagination token expired. Try again without a pagination token.</p>
            capo_pricing.errors.internal_error_exception.InternalErrorException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_pricing.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_pricing.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters had an invalid value.</p>
            capo_pricing.errors.not_found_exception.NotFoundException: <p>The requested resource can't be found.</p>
            capo_pricing.errors.throttling_exception.ThrottlingException: <p>You've made too many requests exceeding service quotas. </p>
            capo_pricing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve a list of attribute values
            This operation returns a list of values available for the given attribute.

            >>> await client.get_attribute_values(service_code='AmazonEC2', attribute_name='volumeType', max_results=2)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pricing.types.get_attribute_values_request.GetAttributeValuesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pricing.types.get_attribute_values_response.GetAttributeValuesResponse"
        ]:
            import capo_pricing._operations.aws_price_list_service.get_attribute_values

            (
                output,
                http_response,
            ) = await capo_pricing._operations.aws_price_list_service.get_attribute_values.async_get_attribute_values(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pricing.types.get_attribute_values_request.GetAttributeValuesRequest = {
            "service_code": service_code,
            "attribute_name": attribute_name,
        }
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

    async def iter_get_attribute_values(
        self,
        service_code: "capo_pricing.types.string.String",
        attribute_name: "capo_pricing.types.string.String",
        *,
        config_overrides: Optional[AsyncPricingClientConfig] = None,
        next_token: Optional["capo_pricing.types.string.String"] = None,
        max_results: Optional[
            "capo_pricing.types.get_attribute_values_max_results.GetAttributeValuesMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_pricing.types.attribute_value.AttributeValue]":
        _token = next_token
        while True:
            _response = await self.get_attribute_values(
                service_code,
                attribute_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("attribute_values",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_price_list_file_url(
        self,
        price_list_arn: "capo_pricing.types.price_list_arn.PriceListArn",
        file_format: "capo_pricing.types.file_format.FileFormat",
        *,
        config_overrides: Optional[AsyncPricingClientConfig] = None,
    ) -> "capo_pricing.types.get_price_list_file_url_response.GetPriceListFileUrlResponse":
        """<p> <i> <b>This feature is in preview release and is subject to change. Your use of Amazon Web Services Price List API is subject to the Beta Service Participation terms of the <a href="https://aws.amazon.com/service-terms/">Amazon Web Services Service Terms</a> (Section 1.10).</b> </i> </p> <p>This returns the URL that you can retrieve your Price List file from. This URL is based on the <code>PriceListArn</code> and <code>FileFormat</code> that you retrieve from the <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists.html">ListPriceLists</a> response. </p>

        Args:
            price_list_arn: <p>The unique identifier that maps to where your Price List files are located. <code>PriceListArn</code> can be obtained from the <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists.html">ListPriceLists</a> response. </p>
            file_format: <p>The format that you want to retrieve your Price List files in. The <code>FileFormat</code> can be obtained from the <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists.html">ListPriceLists</a> response. </p>

        Raises:
            capo_pricing.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request wasn't signed correctly.</p>
            capo_pricing.errors.internal_error_exception.InternalErrorException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_pricing.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters had an invalid value.</p>
            capo_pricing.errors.not_found_exception.NotFoundException: <p>The requested resource can't be found.</p>
            capo_pricing.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_pricing.errors.throttling_exception.ThrottlingException: <p>You've made too many requests exceeding service quotas. </p>
            capo_pricing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pricing.types.get_price_list_file_url_request.GetPriceListFileUrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_pricing.types.get_price_list_file_url_response.GetPriceListFileUrlResponse"
        ]:
            import capo_pricing._operations.aws_price_list_service.get_price_list_file_url

            (
                output,
                http_response,
            ) = await capo_pricing._operations.aws_price_list_service.get_price_list_file_url.async_get_price_list_file_url(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pricing.types.get_price_list_file_url_request.GetPriceListFileUrlRequest = {
            "price_list_arn": price_list_arn,
            "file_format": file_format,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_products(
        self,
        service_code: "capo_pricing.types.string.String",
        *,
        config_overrides: Optional[AsyncPricingClientConfig] = None,
        filters: Optional["capo_pricing.types.filters.Filters"] = None,
        format_version: Optional[
            "capo_pricing.types.format_version.FormatVersion"
        ] = None,
        next_token: Optional["capo_pricing.types.string.String"] = None,
        max_results: Optional[
            "capo_pricing.types.get_products_max_results.GetProductsMaxResults"
        ] = None,
    ) -> "capo_pricing.types.get_products_response.GetProductsResponse":
        """<p>Returns a list of all products that match the filter criteria.</p>

        Args:
            service_code: <p>The code for the service whose products you want to retrieve. </p>
            filters: <p>The list of filters that limit the returned products. only products that match all filters are returned.</p>
            format_version: <p>The format version that you want the response to be in.</p> <p>Valid values are: <code>aws_v1</code> </p>
            next_token: <p>The pagination token that indicates the next set of results that you want to retrieve.</p>
            max_results: <p>The maximum number of results to return in the response.</p>

        Raises:
            capo_pricing.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request wasn't signed correctly.</p>
            capo_pricing.errors.expired_next_token_exception.ExpiredNextTokenException: <p>The pagination token expired. Try again without a pagination token.</p>
            capo_pricing.errors.internal_error_exception.InternalErrorException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_pricing.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_pricing.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters had an invalid value.</p>
            capo_pricing.errors.not_found_exception.NotFoundException: <p>The requested resource can't be found.</p>
            capo_pricing.errors.throttling_exception.ThrottlingException: <p>You've made too many requests exceeding service quotas. </p>
            capo_pricing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pricing.types.get_products_request.GetProductsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pricing.types.get_products_response.GetProductsResponse"
        ]:
            import capo_pricing._operations.aws_price_list_service.get_products

            (
                output,
                http_response,
            ) = await capo_pricing._operations.aws_price_list_service.get_products.async_get_products(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pricing.types.get_products_request.GetProductsRequest = {
            "service_code": service_code
        }
        if filters is not None:
            input_["filters"] = filters
        if format_version is not None:
            input_["format_version"] = format_version
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

    async def iter_get_products(
        self,
        service_code: "capo_pricing.types.string.String",
        *,
        config_overrides: Optional[AsyncPricingClientConfig] = None,
        filters: Optional["capo_pricing.types.filters.Filters"] = None,
        format_version: Optional[
            "capo_pricing.types.format_version.FormatVersion"
        ] = None,
        next_token: Optional["capo_pricing.types.string.String"] = None,
        max_results: Optional[
            "capo_pricing.types.get_products_max_results.GetProductsMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_pricing.types.synthesized_json_price_list_json_item.SynthesizedJsonPriceListJsonItem]":
        _token = next_token
        while True:
            _response = await self.get_products(
                service_code,
                config_overrides=config_overrides,
                filters=filters,
                format_version=format_version,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("price_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_price_lists(
        self,
        service_code: "capo_pricing.types.service_code.ServiceCode",
        effective_date: "capo_pricing.types.effective_date.EffectiveDate",
        currency_code: "capo_pricing.types.currency_code.CurrencyCode",
        *,
        config_overrides: Optional[AsyncPricingClientConfig] = None,
        region_code: Optional["capo_pricing.types.region_code.RegionCode"] = None,
        next_token: Optional["capo_pricing.types.string.String"] = None,
        max_results: Optional["capo_pricing.types.max_results.MaxResults"] = None,
    ) -> "capo_pricing.types.list_price_lists_response.ListPriceListsResponse":
        """<p> <i> <b>This feature is in preview release and is subject to change. Your use of Amazon Web Services Price List API is subject to the Beta Service Participation terms of the <a href="https://aws.amazon.com/service-terms/">Amazon Web Services Service Terms</a> (Section 1.10).</b> </i> </p> <p>This returns a list of Price List references that the requester if authorized to view, given a <code>ServiceCode</code>, <code>CurrencyCode</code>, and an <code>EffectiveDate</code>. Use without a <code>RegionCode</code> filter to list Price List references from all available Amazon Web Services Regions. Use with a <code>RegionCode</code> filter to get the Price List reference that's specific to a specific Amazon Web Services Region. You can use the <code>PriceListArn</code> from the response to get your preferred Price List files through the <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetPriceListFileUrl.html">GetPriceListFileUrl</a> API.</p>

        Args:
            service_code: <p>The service code or the Savings Plans service code for the attributes that you want to retrieve. For example, to get the list of applicable Amazon EC2 price lists, use <code>AmazonEC2</code>. For a full list of service codes containing On-Demand and Reserved Instance (RI) pricing, use the <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_DescribeServices.html#awscostmanagement-pricing_DescribeServices-request-FormatVersion">DescribeServices</a> API.</p> <p>To retrieve the Reserved Instance and Compute Savings Plans price lists, use <code>ComputeSavingsPlans</code>. </p> <p>To retrieve Machine Learning Savings Plans price lists, use <code>MachineLearningSavingsPlans</code>. </p>
            effective_date: <p>The date that the Price List file prices are effective from. </p>
            region_code: <p>This is used to filter the Price List by Amazon Web Services Region. For example, to get the price list only for the <code>US East (N. Virginia)</code> Region, use <code>us-east-1</code>. If nothing is specified, you retrieve price lists for all applicable Regions. The available <code>RegionCode</code> list can be retrieved from <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetAttributeValues.html">GetAttributeValues</a> API.</p>
            currency_code: <p>The three alphabetical character ISO-4217 currency code that the Price List files are denominated in. </p>
            next_token: <p>The pagination token that indicates the next set of results that you want to retrieve. </p>
            max_results: <p>The maximum number of results to return in the response. </p>

        Raises:
            capo_pricing.errors.access_denied_exception.AccessDeniedException: <p>General authentication failure. The request wasn't signed correctly.</p>
            capo_pricing.errors.expired_next_token_exception.ExpiredNextTokenException: <p>The pagination token expired. Try again without a pagination token.</p>
            capo_pricing.errors.internal_error_exception.InternalErrorException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_pricing.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_pricing.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters had an invalid value.</p>
            capo_pricing.errors.not_found_exception.NotFoundException: <p>The requested resource can't be found.</p>
            capo_pricing.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_pricing.errors.throttling_exception.ThrottlingException: <p>You've made too many requests exceeding service quotas. </p>
            capo_pricing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pricing.types.list_price_lists_request.ListPriceListsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pricing.types.list_price_lists_response.ListPriceListsResponse"
        ]:
            import capo_pricing._operations.aws_price_list_service.list_price_lists

            (
                output,
                http_response,
            ) = await capo_pricing._operations.aws_price_list_service.list_price_lists.async_list_price_lists(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pricing.types.list_price_lists_request.ListPriceListsRequest = {
            "service_code": service_code,
            "effective_date": effective_date,
            "currency_code": currency_code,
        }
        if region_code is not None:
            input_["region_code"] = region_code
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

    async def iter_list_price_lists(
        self,
        service_code: "capo_pricing.types.service_code.ServiceCode",
        effective_date: "capo_pricing.types.effective_date.EffectiveDate",
        currency_code: "capo_pricing.types.currency_code.CurrencyCode",
        *,
        config_overrides: Optional[AsyncPricingClientConfig] = None,
        region_code: Optional["capo_pricing.types.region_code.RegionCode"] = None,
        next_token: Optional["capo_pricing.types.string.String"] = None,
        max_results: Optional["capo_pricing.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_pricing.types.price_list.PriceList]":
        _token = next_token
        while True:
            _response = await self.list_price_lists(
                service_code,
                effective_date,
                currency_code,
                config_overrides=config_overrides,
                region_code=region_code,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("price_lists",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
