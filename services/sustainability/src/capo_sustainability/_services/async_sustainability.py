"""Generated from Smithy shape ``com.amazonaws.sustainability#AwsSustainabilityApiService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_sustainability._auth._signers
import capo_sustainability._auth._sigv4
from capo_sustainability._auth._identity import Credentials
from capo_sustainability._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_sustainability._auth._zapros_handler import AuthMiddleware
from capo_sustainability._pagination import resolve_path as _resolve_path
from capo_sustainability._services._aws_config import aaws_config
from capo_sustainability._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_sustainability.types.dimension_entry
    import capo_sustainability.types.dimension_list
    import capo_sustainability.types.emissions_type_list
    import capo_sustainability.types.estimated_carbon_emissions
    import capo_sustainability.types.estimated_water_allocation
    import capo_sustainability.types.filter_expression
    import capo_sustainability.types.get_estimated_carbon_emissions_dimension_values_request
    import capo_sustainability.types.get_estimated_carbon_emissions_dimension_values_response
    import capo_sustainability.types.get_estimated_carbon_emissions_request
    import capo_sustainability.types.get_estimated_carbon_emissions_response
    import capo_sustainability.types.get_estimated_water_allocation_dimension_values_request
    import capo_sustainability.types.get_estimated_water_allocation_dimension_values_response
    import capo_sustainability.types.get_estimated_water_allocation_request
    import capo_sustainability.types.get_estimated_water_allocation_response
    import capo_sustainability.types.granularity_configuration
    import capo_sustainability.types.max_results
    import capo_sustainability.types.next_token
    import capo_sustainability.types.time_granularity
    import capo_sustainability.types.time_period
    import capo_sustainability.types.water_allocation_type_list


class AsyncSustainabilityClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncSustainabilityClient:
    """A client for the ``Sustainability`` service.

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
        self._config = AsyncSustainabilityClientConfig(
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
        self, config_overrides: Optional[AsyncSustainabilityClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSustainabilityClientConfig = config_overrides or {}
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

    async def get_estimated_carbon_emissions(
        self,
        time_period: "capo_sustainability.types.time_period.TimePeriod",
        *,
        config_overrides: Optional[AsyncSustainabilityClientConfig] = None,
        group_by: Optional[
            "capo_sustainability.types.dimension_list.DimensionList"
        ] = None,
        filter_by: Optional[
            "capo_sustainability.types.filter_expression.FilterExpression"
        ] = None,
        emissions_types: Optional[
            "capo_sustainability.types.emissions_type_list.EmissionsTypeList"
        ] = None,
        granularity: Optional[
            "capo_sustainability.types.time_granularity.TimeGranularity"
        ] = None,
        granularity_configuration: Optional[
            "capo_sustainability.types.granularity_configuration.GranularityConfiguration"
        ] = None,
        max_results: Optional[
            "capo_sustainability.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_sustainability.types.next_token.NextToken"] = None,
    ) -> "capo_sustainability.types.get_estimated_carbon_emissions_response.GetEstimatedCarbonEmissionsResponse":
        """<p>Returns estimated carbon emission values based on customer grouping and filtering parameters. We recommend using pagination to ensure that the operation returns quickly and successfully. </p>

        Args:
            time_period: <p> The date range for fetching estimated carbon emissions. The range must include the start date of a month for that month's data to be included in the response. </p>
            group_by: <p>The dimensions available for grouping estimated carbon emissions.</p>
            filter_by: <p> The criteria for filtering estimated carbon emissions. To determine which dimensions are available to be filtered by, you can first call <a>GetEstimatedCarbonEmissionsDimensionValues</a> </p>
            emissions_types: <p>The emission types to include in the results. If absent, returns <code>TOTAL_LBM_CARBON_EMISSIONS</code> and <code>TOTAL_MBM_CARBON_EMISSIONS</code> emissions types. </p>
            granularity: <p> The time granularity for the results. If absent, uses <code>MONTHLY</code> time granularity. The smallest supported granularity for carbon emissions is <code>MONTHLY</code>. </p> <p> If requesting partial time periods, data will be returned based on the smallest supported granularity. For example, requesting <code>2025-04-01T00:00:00Z</code> to <code>2026-04-01T00:00:00Z</code> with <code>YEARLY_CALENDAR</code> granularity will return the last 9 months for 2025 and the first 3 months of 2026. </p>
            granularity_configuration: <p>Configuration for fiscal year calculations when using <code>YEARLY_FISCAL</code> or <code>QUARTERLY_FISCAL</code> granularity. </p>
            max_results: <p>The maximum number of results to return in a single call. Default is 1000.</p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p>

        Raises:
            capo_sustainability.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sustainability.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sustainability.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sustainability.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sustainability.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetEstimatedCarbonEmissionsSuccess

            >>> await client.get_estimated_carbon_emissions(time_period={'Start': '2025-01-01T00:00:00.000Z', 'End': '2025-12-31T23:59:59.999Z'}, group_by=['SERVICE'], emissions_types=['TOTAL_LBM_CARBON_EMISSIONS', 'TOTAL_MBM_CARBON_EMISSIONS', 'TOTAL_SCOPE_1_CARBON_EMISSIONS', 'TOTAL_SCOPE_2_LBM_CARBON_EMISSIONS', 'TOTAL_SCOPE_2_MBM_CARBON_EMISSIONS', 'TOTAL_SCOPE_3_LBM_CARBON_EMISSIONS', 'TOTAL_SCOPE_3_MBM_CARBON_EMISSIONS'], granularity='MONTHLY')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sustainability.types.get_estimated_carbon_emissions_request.GetEstimatedCarbonEmissionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sustainability.types.get_estimated_carbon_emissions_response.GetEstimatedCarbonEmissionsResponse"
        ]:
            import capo_sustainability._operations.aws_sustainability_api_service.get_estimated_carbon_emissions

            (
                output,
                http_response,
            ) = await capo_sustainability._operations.aws_sustainability_api_service.get_estimated_carbon_emissions.async_get_estimated_carbon_emissions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sustainability.types.get_estimated_carbon_emissions_request.GetEstimatedCarbonEmissionsRequest = {
            "time_period": time_period
        }
        if group_by is not None:
            input_["group_by"] = group_by
        if filter_by is not None:
            input_["filter_by"] = filter_by
        if emissions_types is not None:
            input_["emissions_types"] = emissions_types
        if granularity is not None:
            input_["granularity"] = granularity
        if granularity_configuration is not None:
            input_["granularity_configuration"] = granularity_configuration
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

    async def iter_get_estimated_carbon_emissions(
        self,
        time_period: "capo_sustainability.types.time_period.TimePeriod",
        *,
        config_overrides: Optional[AsyncSustainabilityClientConfig] = None,
        group_by: Optional[
            "capo_sustainability.types.dimension_list.DimensionList"
        ] = None,
        filter_by: Optional[
            "capo_sustainability.types.filter_expression.FilterExpression"
        ] = None,
        emissions_types: Optional[
            "capo_sustainability.types.emissions_type_list.EmissionsTypeList"
        ] = None,
        granularity: Optional[
            "capo_sustainability.types.time_granularity.TimeGranularity"
        ] = None,
        granularity_configuration: Optional[
            "capo_sustainability.types.granularity_configuration.GranularityConfiguration"
        ] = None,
        max_results: Optional[
            "capo_sustainability.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_sustainability.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_sustainability.types.estimated_carbon_emissions.EstimatedCarbonEmissions]":
        _token = next_token
        while True:
            _response = await self.get_estimated_carbon_emissions(
                time_period,
                config_overrides=config_overrides,
                group_by=group_by,
                filter_by=filter_by,
                emissions_types=emissions_types,
                granularity=granularity,
                granularity_configuration=granularity_configuration,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_estimated_carbon_emissions_dimension_values(
        self,
        time_period: "capo_sustainability.types.time_period.TimePeriod",
        dimensions: "capo_sustainability.types.dimension_list.DimensionList",
        *,
        config_overrides: Optional[AsyncSustainabilityClientConfig] = None,
        max_results: Optional[
            "capo_sustainability.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_sustainability.types.next_token.NextToken"] = None,
    ) -> "capo_sustainability.types.get_estimated_carbon_emissions_dimension_values_response.GetEstimatedCarbonEmissionsDimensionValuesResponse":
        """<p>Returns the possible dimension values available for a customer's account. We recommend using pagination to ensure that the operation returns quickly and successfully. </p>

        Args:
            time_period: <p> The date range for fetching the dimension values. The range must include the start date of a month for that month's dimensions to be included in the response. </p>
            dimensions: <p>The dimensions available for grouping estimated carbon emissions.</p>
            max_results: <p>The maximum number of results to return in a single call. Default is 1000.</p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p>

        Raises:
            capo_sustainability.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sustainability.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sustainability.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sustainability.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sustainability.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetEstimatedCarbonEmissionsDimensionValuesSuccess

            >>> await client.get_estimated_carbon_emissions_dimension_values(time_period={'Start': '2025-01-01T00:00:00.000Z', 'End': '2025-12-31T23:59:59.999Z'}, dimensions=['REGION', 'SERVICE', 'USAGE_ACCOUNT_ID'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sustainability.types.get_estimated_carbon_emissions_dimension_values_request.GetEstimatedCarbonEmissionsDimensionValuesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sustainability.types.get_estimated_carbon_emissions_dimension_values_response.GetEstimatedCarbonEmissionsDimensionValuesResponse"
        ]:
            import capo_sustainability._operations.aws_sustainability_api_service.get_estimated_carbon_emissions_dimension_values

            (
                output,
                http_response,
            ) = await capo_sustainability._operations.aws_sustainability_api_service.get_estimated_carbon_emissions_dimension_values.async_get_estimated_carbon_emissions_dimension_values(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sustainability.types.get_estimated_carbon_emissions_dimension_values_request.GetEstimatedCarbonEmissionsDimensionValuesRequest = {
            "time_period": time_period,
            "dimensions": dimensions,
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

    async def iter_get_estimated_carbon_emissions_dimension_values(
        self,
        time_period: "capo_sustainability.types.time_period.TimePeriod",
        dimensions: "capo_sustainability.types.dimension_list.DimensionList",
        *,
        config_overrides: Optional[AsyncSustainabilityClientConfig] = None,
        max_results: Optional[
            "capo_sustainability.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_sustainability.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_sustainability.types.dimension_entry.DimensionEntry]":
        _token = next_token
        while True:
            _response = await self.get_estimated_carbon_emissions_dimension_values(
                time_period,
                dimensions,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_estimated_water_allocation(
        self,
        time_period: "capo_sustainability.types.time_period.TimePeriod",
        *,
        config_overrides: Optional[AsyncSustainabilityClientConfig] = None,
        group_by: Optional[
            "capo_sustainability.types.dimension_list.DimensionList"
        ] = None,
        filter_by: Optional[
            "capo_sustainability.types.filter_expression.FilterExpression"
        ] = None,
        allocation_types: Optional[
            "capo_sustainability.types.water_allocation_type_list.WaterAllocationTypeList"
        ] = None,
        granularity: Optional[
            "capo_sustainability.types.time_granularity.TimeGranularity"
        ] = None,
        max_results: Optional[
            "capo_sustainability.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_sustainability.types.next_token.NextToken"] = None,
    ) -> "capo_sustainability.types.get_estimated_water_allocation_response.GetEstimatedWaterAllocationResponse":
        """<p>Returns estimated water allocation values based on customer grouping and filtering parameters. We recommend using pagination to ensure that the operation returns quickly and successfully. </p>

        Args:
            time_period: <p> The date range for fetching estimated water allocation. The range must include the start date of a year for that year's data to be included in the response. </p>
            group_by: <p>The dimensions available for grouping estimated water allocation.</p>
            filter_by: <p> The criteria for filtering estimated water allocation. To determine which dimensions are available to be filtered by, you can first call <a>GetEstimatedWaterAllocationDimensionValues</a> </p>
            allocation_types: <p>The allocation types to include in the results. If absent, returns <code>TOTAL_WATER_WITHDRAWALS</code> allocation types. </p>
            granularity: <p>The time granularity for the results. Only <code>YEARLY_CALENDAR</code> time granularity is currently supported for water allocation. Defaults to <code>YEARLY_CALENDAR</code> if absent.</p> <p> If requesting partial time periods, data will be returned based on the smallest supported granularity. For example, requesting <code>2025-04-01T00:00:00Z</code> to <code>2026-04-01T00:00:00Z</code> with <code>YEARLY_CALENDAR</code> will return all the data for 2026 only. </p>
            max_results: <p>The maximum number of results to return in a single call. Default is 1000.</p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p>

        Raises:
            capo_sustainability.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sustainability.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sustainability.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sustainability.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sustainability.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetEstimatedWaterAllocationSuccess

            >>> await client.get_estimated_water_allocation(time_period={'Start': '2025-01-01T00:00:00.00Z', 'End': '2026-01-01T00:00:00.00Z'}, group_by=['SERVICE'], allocation_types=['TOTAL_WATER_WITHDRAWALS'], granularity='YEARLY_CALENDAR')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sustainability.types.get_estimated_water_allocation_request.GetEstimatedWaterAllocationRequest]",
        ) -> AsyncOperationResponse[
            "capo_sustainability.types.get_estimated_water_allocation_response.GetEstimatedWaterAllocationResponse"
        ]:
            import capo_sustainability._operations.aws_sustainability_api_service.get_estimated_water_allocation

            (
                output,
                http_response,
            ) = await capo_sustainability._operations.aws_sustainability_api_service.get_estimated_water_allocation.async_get_estimated_water_allocation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sustainability.types.get_estimated_water_allocation_request.GetEstimatedWaterAllocationRequest = {
            "time_period": time_period
        }
        if group_by is not None:
            input_["group_by"] = group_by
        if filter_by is not None:
            input_["filter_by"] = filter_by
        if allocation_types is not None:
            input_["allocation_types"] = allocation_types
        if granularity is not None:
            input_["granularity"] = granularity
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

    async def iter_get_estimated_water_allocation(
        self,
        time_period: "capo_sustainability.types.time_period.TimePeriod",
        *,
        config_overrides: Optional[AsyncSustainabilityClientConfig] = None,
        group_by: Optional[
            "capo_sustainability.types.dimension_list.DimensionList"
        ] = None,
        filter_by: Optional[
            "capo_sustainability.types.filter_expression.FilterExpression"
        ] = None,
        allocation_types: Optional[
            "capo_sustainability.types.water_allocation_type_list.WaterAllocationTypeList"
        ] = None,
        granularity: Optional[
            "capo_sustainability.types.time_granularity.TimeGranularity"
        ] = None,
        max_results: Optional[
            "capo_sustainability.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_sustainability.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_sustainability.types.estimated_water_allocation.EstimatedWaterAllocation]":
        _token = next_token
        while True:
            _response = await self.get_estimated_water_allocation(
                time_period,
                config_overrides=config_overrides,
                group_by=group_by,
                filter_by=filter_by,
                allocation_types=allocation_types,
                granularity=granularity,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_estimated_water_allocation_dimension_values(
        self,
        time_period: "capo_sustainability.types.time_period.TimePeriod",
        dimensions: "capo_sustainability.types.dimension_list.DimensionList",
        *,
        config_overrides: Optional[AsyncSustainabilityClientConfig] = None,
        max_results: Optional[
            "capo_sustainability.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_sustainability.types.next_token.NextToken"] = None,
    ) -> "capo_sustainability.types.get_estimated_water_allocation_dimension_values_response.GetEstimatedWaterAllocationDimensionValuesResponse":
        """<p>Returns the possible dimension values available for a customer's account. We recommend using pagination to ensure that the operation returns quickly and successfully. </p>

        Args:
            time_period: <p> The date range for fetching the dimension values. The range must include the start date of a year for that year's data to be included in the response. </p>
            dimensions: <p>The dimensions available for grouping estimated water allocation.</p>
            max_results: <p>The maximum number of results to return in a single call. Default is 1000.</p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p>

        Raises:
            capo_sustainability.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sustainability.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sustainability.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sustainability.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sustainability.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetEstimatedWaterAllocationDimensionValuesSuccess

            >>> await client.get_estimated_water_allocation_dimension_values(time_period={'Start': '2025-01-01T00:00:00.00Z', 'End': '2026-01-01T00:00:00.00Z'}, dimensions=['REGION', 'SERVICE', 'USAGE_ACCOUNT_ID'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sustainability.types.get_estimated_water_allocation_dimension_values_request.GetEstimatedWaterAllocationDimensionValuesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sustainability.types.get_estimated_water_allocation_dimension_values_response.GetEstimatedWaterAllocationDimensionValuesResponse"
        ]:
            import capo_sustainability._operations.aws_sustainability_api_service.get_estimated_water_allocation_dimension_values

            (
                output,
                http_response,
            ) = await capo_sustainability._operations.aws_sustainability_api_service.get_estimated_water_allocation_dimension_values.async_get_estimated_water_allocation_dimension_values(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sustainability.types.get_estimated_water_allocation_dimension_values_request.GetEstimatedWaterAllocationDimensionValuesRequest = {
            "time_period": time_period,
            "dimensions": dimensions,
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

    async def iter_get_estimated_water_allocation_dimension_values(
        self,
        time_period: "capo_sustainability.types.time_period.TimePeriod",
        dimensions: "capo_sustainability.types.dimension_list.DimensionList",
        *,
        config_overrides: Optional[AsyncSustainabilityClientConfig] = None,
        max_results: Optional[
            "capo_sustainability.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_sustainability.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_sustainability.types.dimension_entry.DimensionEntry]":
        _token = next_token
        while True:
            _response = await self.get_estimated_water_allocation_dimension_values(
                time_period,
                dimensions,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
