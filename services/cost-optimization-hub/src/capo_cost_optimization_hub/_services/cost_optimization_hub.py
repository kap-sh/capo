"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#CostOptimizationHubService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_cost_optimization_hub._auth._signers
import capo_cost_optimization_hub._auth._sigv4
from capo_cost_optimization_hub._auth._identity import Credentials
from capo_cost_optimization_hub._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_cost_optimization_hub._auth._zapros_handler import AuthMiddleware
from capo_cost_optimization_hub._pagination import resolve_path as _resolve_path
from capo_cost_optimization_hub._services._aws_config import aws_config
from capo_cost_optimization_hub._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.account_enrollment_status
    import capo_cost_optimization_hub.types.account_id
    import capo_cost_optimization_hub.types.efficiency_metrics_by_group
    import capo_cost_optimization_hub.types.enrollment_status
    import capo_cost_optimization_hub.types.filter
    import capo_cost_optimization_hub.types.get_preferences_request
    import capo_cost_optimization_hub.types.get_preferences_response
    import capo_cost_optimization_hub.types.get_recommendation_request
    import capo_cost_optimization_hub.types.get_recommendation_response
    import capo_cost_optimization_hub.types.granularity_type
    import capo_cost_optimization_hub.types.list_efficiency_metrics_request
    import capo_cost_optimization_hub.types.list_efficiency_metrics_response
    import capo_cost_optimization_hub.types.list_enrollment_statuses_request
    import capo_cost_optimization_hub.types.list_enrollment_statuses_response
    import capo_cost_optimization_hub.types.list_recommendation_summaries_request
    import capo_cost_optimization_hub.types.list_recommendation_summaries_response
    import capo_cost_optimization_hub.types.list_recommendations_request
    import capo_cost_optimization_hub.types.list_recommendations_response
    import capo_cost_optimization_hub.types.max_results
    import capo_cost_optimization_hub.types.member_account_discount_visibility
    import capo_cost_optimization_hub.types.order_by
    import capo_cost_optimization_hub.types.preferred_commitment
    import capo_cost_optimization_hub.types.recommendation
    import capo_cost_optimization_hub.types.recommendation_summary
    import capo_cost_optimization_hub.types.savings_estimation_mode
    import capo_cost_optimization_hub.types.summary_metrics_list
    import capo_cost_optimization_hub.types.time_period
    import capo_cost_optimization_hub.types.update_enrollment_status_request
    import capo_cost_optimization_hub.types.update_enrollment_status_response
    import capo_cost_optimization_hub.types.update_preferences_request
    import capo_cost_optimization_hub.types.update_preferences_response


class CostOptimizationHubClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class CostOptimizationHubClient:
    """A client for the ``CostOptimizationHub`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
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
                Client(http_handler)
            )
        self._config = CostOptimizationHubClientConfig(
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
        self, config_overrides: Optional[CostOptimizationHubClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CostOptimizationHubClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def get_preferences(
        self, *, config_overrides: Optional[CostOptimizationHubClientConfig] = None
    ) -> "capo_cost_optimization_hub.types.get_preferences_response.GetPreferencesResponse":
        """<p>Returns a set of preferences for an account in order to add account-specific preferences into the service. These preferences impact how the savings associated with recommendations are presented—estimated savings after discounts or estimated savings before discounts, for example.</p>

        Raises:
            capo_cost_optimization_hub.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to use this operation with the given parameters.</p>
            capo_cost_optimization_hub.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_cost_optimization_hub.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cost_optimization_hub.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_cost_optimization_hub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_optimization_hub.types.get_preferences_request.GetPreferencesRequest]",
        ) -> OperationResponse[
            "capo_cost_optimization_hub.types.get_preferences_response.GetPreferencesResponse"
        ]:
            import capo_cost_optimization_hub._operations.cost_optimization_hub_service.get_preferences

            output, http_response = (
                capo_cost_optimization_hub._operations.cost_optimization_hub_service.get_preferences.get_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_optimization_hub.types.get_preferences_request.GetPreferencesRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_recommendation(
        self,
        recommendation_id: str,
        *,
        config_overrides: Optional[CostOptimizationHubClientConfig] = None,
    ) -> "capo_cost_optimization_hub.types.get_recommendation_response.GetRecommendationResponse":
        """<p>Returns both the current and recommended resource configuration and the estimated cost impact for a recommendation.</p> <p>The <code>recommendationId</code> is only valid for up to a maximum of 24 hours as recommendations are refreshed daily. To retrieve the <code>recommendationId</code>, use the <code>ListRecommendations</code> API.</p>

        Args:
            recommendation_id: <p>The ID for the recommendation.</p>

        Raises:
            capo_cost_optimization_hub.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to use this operation with the given parameters.</p>
            capo_cost_optimization_hub.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_cost_optimization_hub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Resource Name (ARN) in the request doesn't exist.</p>
            capo_cost_optimization_hub.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cost_optimization_hub.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_cost_optimization_hub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_optimization_hub.types.get_recommendation_request.GetRecommendationRequest]",
        ) -> OperationResponse[
            "capo_cost_optimization_hub.types.get_recommendation_response.GetRecommendationResponse"
        ]:
            import capo_cost_optimization_hub._operations.cost_optimization_hub_service.get_recommendation

            output, http_response = (
                capo_cost_optimization_hub._operations.cost_optimization_hub_service.get_recommendation.get_recommendation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_optimization_hub.types.get_recommendation_request.GetRecommendationRequest = {
            "recommendation_id": recommendation_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_efficiency_metrics(
        self,
        granularity: "capo_cost_optimization_hub.types.granularity_type.GranularityType",
        time_period: "capo_cost_optimization_hub.types.time_period.TimePeriod",
        *,
        config_overrides: Optional[CostOptimizationHubClientConfig] = None,
        group_by: Optional[str] = None,
        max_results: Optional[
            "capo_cost_optimization_hub.types.max_results.MaxResults"
        ] = None,
        order_by: Optional["capo_cost_optimization_hub.types.order_by.OrderBy"] = None,
        next_token: Optional[str] = None,
    ) -> "capo_cost_optimization_hub.types.list_efficiency_metrics_response.ListEfficiencyMetricsResponse":
        """<p>Returns cost efficiency metrics aggregated over time and optionally grouped by a specified dimension. The metrics provide insights into your cost optimization progress by tracking estimated savings, spending, and measures how effectively you're optimizing your Cloud resources.</p> <p>The operation supports both daily and monthly time granularities and allows grouping results by account ID, Amazon Web Services Region. Results are returned as time-series data, enabling you to analyze trends in your cost optimization performance over the specified time period.</p>

        Args:
            group_by: <p>The dimension by which to group the cost efficiency metrics. Valid values include account ID, Amazon Web Services Region. When no grouping is specified, metrics are aggregated across all resources in the specified time period.</p>
            granularity: <p>The time granularity for the cost efficiency metrics. Specify <code>Daily</code> for metrics aggregated by day, or <code>Monthly</code> for metrics aggregated by month.</p>
            time_period: <p>The time period for which to retrieve the cost efficiency metrics. The start date is inclusive and the end date is exclusive. Dates can be specified in either YYYY-MM-DD format or YYYY-MM format depending on the desired granularity.</p>
            max_results: <p>The maximum number of groups to return in the response. Valid values range from 0 to 1000. Use in conjunction with <code>nextToken</code> to paginate through results when the total number of groups exceeds this limit.</p>
            order_by: <p>The ordering specification for the results. Defines which dimension to sort by and whether to sort in ascending or descending order.</p>
            next_token: <p>The token to retrieve the next page of results. This value is returned in the response when the number of groups exceeds the specified <code>maxResults</code> value.</p>

        Raises:
            capo_cost_optimization_hub.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to use this operation with the given parameters.</p>
            capo_cost_optimization_hub.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_cost_optimization_hub.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cost_optimization_hub.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_cost_optimization_hub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_optimization_hub.types.list_efficiency_metrics_request.ListEfficiencyMetricsRequest]",
        ) -> OperationResponse[
            "capo_cost_optimization_hub.types.list_efficiency_metrics_response.ListEfficiencyMetricsResponse"
        ]:
            import capo_cost_optimization_hub._operations.cost_optimization_hub_service.list_efficiency_metrics

            output, http_response = (
                capo_cost_optimization_hub._operations.cost_optimization_hub_service.list_efficiency_metrics.list_efficiency_metrics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_optimization_hub.types.list_efficiency_metrics_request.ListEfficiencyMetricsRequest = {
            "granularity": granularity,
            "time_period": time_period,
        }
        if group_by is not None:
            input_["group_by"] = group_by
        if max_results is not None:
            input_["max_results"] = max_results
        if order_by is not None:
            input_["order_by"] = order_by
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_efficiency_metrics(
        self,
        granularity: "capo_cost_optimization_hub.types.granularity_type.GranularityType",
        time_period: "capo_cost_optimization_hub.types.time_period.TimePeriod",
        *,
        config_overrides: Optional[CostOptimizationHubClientConfig] = None,
        group_by: Optional[str] = None,
        max_results: Optional[
            "capo_cost_optimization_hub.types.max_results.MaxResults"
        ] = None,
        order_by: Optional["capo_cost_optimization_hub.types.order_by.OrderBy"] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_cost_optimization_hub.types.efficiency_metrics_by_group.EfficiencyMetricsByGroup]":
        _token = next_token
        while True:
            _response = self.list_efficiency_metrics(
                granularity,
                time_period,
                config_overrides=config_overrides,
                group_by=group_by,
                max_results=max_results,
                order_by=order_by,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("efficiency_metrics_by_group",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_enrollment_statuses(
        self,
        *,
        config_overrides: Optional[CostOptimizationHubClientConfig] = None,
        include_organization_info: Optional[bool] = None,
        account_id: Optional[
            "capo_cost_optimization_hub.types.account_id.AccountId"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_cost_optimization_hub.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_cost_optimization_hub.types.list_enrollment_statuses_response.ListEnrollmentStatusesResponse":
        """<p>Retrieves the enrollment status for an account. It can also return the list of accounts that are enrolled under the organization.</p>

        Args:
            include_organization_info: <p>Indicates whether to return the enrollment status for the organization.</p>
            account_id: <p>The account ID of a member account in the organization.</p>
            next_token: <p>The token to retrieve the next set of results.</p>
            max_results: <p>The maximum number of objects that are returned for the request.</p>

        Raises:
            capo_cost_optimization_hub.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to use this operation with the given parameters.</p>
            capo_cost_optimization_hub.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_cost_optimization_hub.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cost_optimization_hub.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_cost_optimization_hub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_optimization_hub.types.list_enrollment_statuses_request.ListEnrollmentStatusesRequest]",
        ) -> OperationResponse[
            "capo_cost_optimization_hub.types.list_enrollment_statuses_response.ListEnrollmentStatusesResponse"
        ]:
            import capo_cost_optimization_hub._operations.cost_optimization_hub_service.list_enrollment_statuses

            output, http_response = (
                capo_cost_optimization_hub._operations.cost_optimization_hub_service.list_enrollment_statuses.list_enrollment_statuses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_optimization_hub.types.list_enrollment_statuses_request.ListEnrollmentStatusesRequest = {}
        if include_organization_info is not None:
            input_["include_organization_info"] = include_organization_info
        if account_id is not None:
            input_["account_id"] = account_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_enrollment_statuses(
        self,
        *,
        config_overrides: Optional[CostOptimizationHubClientConfig] = None,
        include_organization_info: Optional[bool] = None,
        account_id: Optional[
            "capo_cost_optimization_hub.types.account_id.AccountId"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_cost_optimization_hub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_cost_optimization_hub.types.account_enrollment_status.AccountEnrollmentStatus]":
        _token = next_token
        while True:
            _response = self.list_enrollment_statuses(
                config_overrides=config_overrides,
                include_organization_info=include_organization_info,
                account_id=account_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_recommendations(
        self,
        *,
        config_overrides: Optional[CostOptimizationHubClientConfig] = None,
        filter: Optional["capo_cost_optimization_hub.types.filter.Filter"] = None,
        order_by: Optional["capo_cost_optimization_hub.types.order_by.OrderBy"] = None,
        include_all_recommendations: Optional[bool] = None,
        max_results: Optional[
            "capo_cost_optimization_hub.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_cost_optimization_hub.types.list_recommendations_response.ListRecommendationsResponse":
        """<p>Returns a list of recommendations.</p>

        Args:
            filter: <p>The constraints that you want all returned recommendations to match.</p>
            order_by: <p>The ordering of recommendations by a dimension.</p>
            include_all_recommendations: <p>List of all recommendations for a resource, or a single recommendation if de-duped by <code>resourceId</code>.</p>
            max_results: <p>The maximum number of recommendations that are returned for the request.</p>
            next_token: <p>The token to retrieve the next set of results.</p>

        Raises:
            capo_cost_optimization_hub.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to use this operation with the given parameters.</p>
            capo_cost_optimization_hub.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_cost_optimization_hub.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cost_optimization_hub.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_cost_optimization_hub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_optimization_hub.types.list_recommendations_request.ListRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_cost_optimization_hub.types.list_recommendations_response.ListRecommendationsResponse"
        ]:
            import capo_cost_optimization_hub._operations.cost_optimization_hub_service.list_recommendations

            output, http_response = (
                capo_cost_optimization_hub._operations.cost_optimization_hub_service.list_recommendations.list_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_optimization_hub.types.list_recommendations_request.ListRecommendationsRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if order_by is not None:
            input_["order_by"] = order_by
        if include_all_recommendations is not None:
            input_["include_all_recommendations"] = include_all_recommendations
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_recommendations(
        self,
        *,
        config_overrides: Optional[CostOptimizationHubClientConfig] = None,
        filter: Optional["capo_cost_optimization_hub.types.filter.Filter"] = None,
        order_by: Optional["capo_cost_optimization_hub.types.order_by.OrderBy"] = None,
        include_all_recommendations: Optional[bool] = None,
        max_results: Optional[
            "capo_cost_optimization_hub.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_cost_optimization_hub.types.recommendation.Recommendation]":
        _token = next_token
        while True:
            _response = self.list_recommendations(
                config_overrides=config_overrides,
                filter=filter,
                order_by=order_by,
                include_all_recommendations=include_all_recommendations,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_recommendation_summaries(
        self,
        group_by: str,
        *,
        config_overrides: Optional[CostOptimizationHubClientConfig] = None,
        filter: Optional["capo_cost_optimization_hub.types.filter.Filter"] = None,
        max_results: Optional[
            "capo_cost_optimization_hub.types.max_results.MaxResults"
        ] = None,
        metrics: Optional[
            "capo_cost_optimization_hub.types.summary_metrics_list.SummaryMetricsList"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_cost_optimization_hub.types.list_recommendation_summaries_response.ListRecommendationSummariesResponse":
        """<p>Returns a concise representation of savings estimates for resources. Also returns de-duped savings across different types of recommendations.</p> <note> <p>The following filters are not supported for this API: <code>recommendationIds</code>, <code>resourceArns</code>, and <code>resourceIds</code>.</p> </note>

        Args:
            group_by: <p>The grouping of recommendations by a dimension.</p>
            max_results: <p>The maximum number of recommendations to be returned for the request.</p>
            metrics: <p>Additional metrics to be returned for the request. The only valid value is <code>savingsPercentage</code>.</p>
            next_token: <p>The token to retrieve the next set of results.</p>

        Raises:
            capo_cost_optimization_hub.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to use this operation with the given parameters.</p>
            capo_cost_optimization_hub.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_cost_optimization_hub.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cost_optimization_hub.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_cost_optimization_hub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_optimization_hub.types.list_recommendation_summaries_request.ListRecommendationSummariesRequest]",
        ) -> OperationResponse[
            "capo_cost_optimization_hub.types.list_recommendation_summaries_response.ListRecommendationSummariesResponse"
        ]:
            import capo_cost_optimization_hub._operations.cost_optimization_hub_service.list_recommendation_summaries

            output, http_response = (
                capo_cost_optimization_hub._operations.cost_optimization_hub_service.list_recommendation_summaries.list_recommendation_summaries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_optimization_hub.types.list_recommendation_summaries_request.ListRecommendationSummariesRequest = {
            "group_by": group_by
        }
        if filter is not None:
            input_["filter"] = filter
        if max_results is not None:
            input_["max_results"] = max_results
        if metrics is not None:
            input_["metrics"] = metrics
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_recommendation_summaries(
        self,
        group_by: str,
        *,
        config_overrides: Optional[CostOptimizationHubClientConfig] = None,
        filter: Optional["capo_cost_optimization_hub.types.filter.Filter"] = None,
        max_results: Optional[
            "capo_cost_optimization_hub.types.max_results.MaxResults"
        ] = None,
        metrics: Optional[
            "capo_cost_optimization_hub.types.summary_metrics_list.SummaryMetricsList"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_cost_optimization_hub.types.recommendation_summary.RecommendationSummary]":
        _token = next_token
        while True:
            _response = self.list_recommendation_summaries(
                group_by,
                config_overrides=config_overrides,
                filter=filter,
                max_results=max_results,
                metrics=metrics,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_enrollment_status(
        self,
        status: "capo_cost_optimization_hub.types.enrollment_status.EnrollmentStatus",
        *,
        config_overrides: Optional[CostOptimizationHubClientConfig] = None,
        include_member_accounts: Optional[bool] = None,
    ) -> "capo_cost_optimization_hub.types.update_enrollment_status_response.UpdateEnrollmentStatusResponse":
        """<p>Updates the enrollment (opt in and opt out) status of an account to the Cost Optimization Hub service.</p> <p>If the account is a management account of an organization, this action can also be used to enroll member accounts of the organization.</p> <p>You must have the appropriate permissions to opt in to Cost Optimization Hub and to view its recommendations. When you opt in, Cost Optimization Hub automatically creates a service-linked role in your account to access its data.</p>

        Args:
            status: <p>Sets the account status.</p>
            include_member_accounts: <p>Indicates whether to enroll member accounts of the organization if the account is the management account or delegated administrator.</p>

        Raises:
            capo_cost_optimization_hub.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to use this operation with the given parameters.</p>
            capo_cost_optimization_hub.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_cost_optimization_hub.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cost_optimization_hub.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_cost_optimization_hub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_optimization_hub.types.update_enrollment_status_request.UpdateEnrollmentStatusRequest]",
        ) -> OperationResponse[
            "capo_cost_optimization_hub.types.update_enrollment_status_response.UpdateEnrollmentStatusResponse"
        ]:
            import capo_cost_optimization_hub._operations.cost_optimization_hub_service.update_enrollment_status

            output, http_response = (
                capo_cost_optimization_hub._operations.cost_optimization_hub_service.update_enrollment_status.update_enrollment_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_optimization_hub.types.update_enrollment_status_request.UpdateEnrollmentStatusRequest = {
            "status": status
        }
        if include_member_accounts is not None:
            input_["include_member_accounts"] = include_member_accounts

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_preferences(
        self,
        *,
        config_overrides: Optional[CostOptimizationHubClientConfig] = None,
        savings_estimation_mode: Optional[
            "capo_cost_optimization_hub.types.savings_estimation_mode.SavingsEstimationMode"
        ] = None,
        member_account_discount_visibility: Optional[
            "capo_cost_optimization_hub.types.member_account_discount_visibility.MemberAccountDiscountVisibility"
        ] = None,
        preferred_commitment: Optional[
            "capo_cost_optimization_hub.types.preferred_commitment.PreferredCommitment"
        ] = None,
    ) -> "capo_cost_optimization_hub.types.update_preferences_response.UpdatePreferencesResponse":
        """<p>Updates a set of preferences for an account in order to add account-specific preferences into the service. These preferences impact how the savings associated with recommendations are presented.</p>

        Args:
            savings_estimation_mode: <p>Sets the "savings estimation mode" preference.</p>
            member_account_discount_visibility: <p>Sets the "member account discount visibility" preference.</p>
            preferred_commitment: <p>Sets the preferences for how Reserved Instances and Savings Plans cost-saving opportunities are prioritized in terms of payment option and term length.</p>

        Raises:
            capo_cost_optimization_hub.errors.access_denied_exception.AccessDeniedException: <p>You are not authorized to use this operation with the given parameters.</p>
            capo_cost_optimization_hub.errors.internal_server_exception.InternalServerException: <p>An error on the server occurred during the processing of your request. Try again later.</p>
            capo_cost_optimization_hub.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cost_optimization_hub.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_cost_optimization_hub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_optimization_hub.types.update_preferences_request.UpdatePreferencesRequest]",
        ) -> OperationResponse[
            "capo_cost_optimization_hub.types.update_preferences_response.UpdatePreferencesResponse"
        ]:
            import capo_cost_optimization_hub._operations.cost_optimization_hub_service.update_preferences

            output, http_response = (
                capo_cost_optimization_hub._operations.cost_optimization_hub_service.update_preferences.update_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_optimization_hub.types.update_preferences_request.UpdatePreferencesRequest = {}
        if savings_estimation_mode is not None:
            input_["savings_estimation_mode"] = savings_estimation_mode
        if member_account_discount_visibility is not None:
            input_["member_account_discount_visibility"] = (
                member_account_discount_visibility
            )
        if preferred_commitment is not None:
            input_["preferred_commitment"] = preferred_commitment

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
