"""Generated from Smithy shape ``com.amazonaws.forecastquery#AmazonForecastRuntime``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_forecastquery._auth._signers
import capo_forecastquery._auth._sigv4
from capo_forecastquery._auth._identity import Credentials
from capo_forecastquery._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_forecastquery._auth._zapros_handler import AuthMiddleware
from capo_forecastquery._services._aws_config import aws_config
from capo_forecastquery._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_forecastquery.types.arn
    import capo_forecastquery.types.date_time
    import capo_forecastquery.types.filters
    import capo_forecastquery.types.long_arn
    import capo_forecastquery.types.next_token
    import capo_forecastquery.types.query_forecast_request
    import capo_forecastquery.types.query_forecast_response
    import capo_forecastquery.types.query_what_if_forecast_request
    import capo_forecastquery.types.query_what_if_forecast_response


class forecastqueryClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class forecastqueryClient:
    """A client for the ``forecastquery`` service.

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
        self._config = forecastqueryClientConfig(
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
        self, config_overrides: Optional[forecastqueryClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: forecastqueryClientConfig = config_overrides or {}
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

    def query_forecast(
        self,
        forecast_arn: "capo_forecastquery.types.arn.Arn",
        filters: "capo_forecastquery.types.filters.Filters",
        *,
        config_overrides: Optional[forecastqueryClientConfig] = None,
        start_date: Optional["capo_forecastquery.types.date_time.DateTime"] = None,
        end_date: Optional["capo_forecastquery.types.date_time.DateTime"] = None,
        next_token: Optional["capo_forecastquery.types.next_token.NextToken"] = None,
    ) -> "capo_forecastquery.types.query_forecast_response.QueryForecastResponse":
        """<p>Retrieves a forecast for a single item, filtered by the supplied criteria.</p> <p>The criteria is a key-value pair. The key is either <code>item_id</code> (or the equivalent non-timestamp, non-target field) from the <code>TARGET_TIME_SERIES</code> dataset, or one of the forecast dimensions specified as part of the <code>FeaturizationConfig</code> object.</p> <p>By default, <code>QueryForecast</code> returns the complete date range for the filtered forecast. You can request a specific date range.</p> <p>To get the full forecast, use the <a href="https://docs.aws.amazon.com/en_us/forecast/latest/dg/API_CreateForecastExportJob.html">CreateForecastExportJob</a> operation.</p> <note> <p>The forecasts generated by Amazon Forecast are in the same timezone as the dataset that was used to create the predictor.</p> </note>

        Args:
            forecast_arn: <p>The Amazon Resource Name (ARN) of the forecast to query.</p>
            start_date: <p>The start date for the forecast. Specify the date using this format: yyyy-MM-dd'T'HH:mm:ss (ISO 8601 format). For example, 2015-01-01T08:00:00.</p>
            end_date: <p>The end date for the forecast. Specify the date using this format: yyyy-MM-dd'T'HH:mm:ss (ISO 8601 format). For example, 2015-01-01T20:00:00. </p>
            filters: <p>The filtering criteria to apply when retrieving the forecast. For example, to get the forecast for <code>client_21</code> in the electricity usage dataset, specify the following:</p> <p> <code>{"item_id" : "client_21"}</code> </p> <p>To get the full forecast, use the <a href="https://docs.aws.amazon.com/en_us/forecast/latest/dg/API_CreateForecastExportJob.html">CreateForecastExportJob</a> operation.</p>
            next_token: <p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>

        Raises:
            capo_forecastquery.errors.invalid_input_exception.InvalidInputException: <p>The value is invalid or is too long.</p>
            capo_forecastquery.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid. Tokens expire after 24 hours.</p>
            capo_forecastquery.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_forecastquery.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecastquery.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find that resource. Check the information that you've provided and try again.</p>
            capo_forecastquery.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_forecastquery.types.query_forecast_request.QueryForecastRequest]",
        ) -> OperationResponse[
            "capo_forecastquery.types.query_forecast_response.QueryForecastResponse"
        ]:
            import capo_forecastquery._operations.amazon_forecast_runtime.query_forecast

            output, http_response = (
                capo_forecastquery._operations.amazon_forecast_runtime.query_forecast.query_forecast(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecastquery.types.query_forecast_request.QueryForecastRequest = {
            "forecast_arn": forecast_arn,
            "filters": filters,
        }
        if start_date is not None:
            input_["start_date"] = start_date
        if end_date is not None:
            input_["end_date"] = end_date
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def query_what_if_forecast(
        self,
        what_if_forecast_arn: "capo_forecastquery.types.long_arn.LongArn",
        filters: "capo_forecastquery.types.filters.Filters",
        *,
        config_overrides: Optional[forecastqueryClientConfig] = None,
        start_date: Optional["capo_forecastquery.types.date_time.DateTime"] = None,
        end_date: Optional["capo_forecastquery.types.date_time.DateTime"] = None,
        next_token: Optional["capo_forecastquery.types.next_token.NextToken"] = None,
    ) -> "capo_forecastquery.types.query_what_if_forecast_response.QueryWhatIfForecastResponse":
        """<p>Retrieves a what-if forecast.</p>

        Args:
            what_if_forecast_arn: <p>The Amazon Resource Name (ARN) of the what-if forecast to query.</p>
            start_date: <p>The start date for the what-if forecast. Specify the date using this format: yyyy-MM-dd'T'HH:mm:ss (ISO 8601 format). For example, 2015-01-01T08:00:00.</p>
            end_date: <p>The end date for the what-if forecast. Specify the date using this format: yyyy-MM-dd'T'HH:mm:ss (ISO 8601 format). For example, 2015-01-01T20:00:00. </p>
            filters: <p>The filtering criteria to apply when retrieving the forecast. For example, to get the forecast for <code>client_21</code> in the electricity usage dataset, specify the following:</p> <p> <code>{"item_id" : "client_21"}</code> </p> <p>To get the full what-if forecast, use the <a href="https://docs.aws.amazon.com/en_us/forecast/latest/dg/API_CreateWhatIfForecastExport.html">CreateForecastExportJob</a> operation.</p>
            next_token: <p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>

        Raises:
            capo_forecastquery.errors.invalid_input_exception.InvalidInputException: <p>The value is invalid or is too long.</p>
            capo_forecastquery.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid. Tokens expire after 24 hours.</p>
            capo_forecastquery.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of requests per second has been exceeded.</p>
            capo_forecastquery.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecastquery.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find that resource. Check the information that you've provided and try again.</p>
            capo_forecastquery.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_forecastquery.types.query_what_if_forecast_request.QueryWhatIfForecastRequest]",
        ) -> OperationResponse[
            "capo_forecastquery.types.query_what_if_forecast_response.QueryWhatIfForecastResponse"
        ]:
            import capo_forecastquery._operations.amazon_forecast_runtime.query_what_if_forecast

            output, http_response = (
                capo_forecastquery._operations.amazon_forecast_runtime.query_what_if_forecast.query_what_if_forecast(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecastquery.types.query_what_if_forecast_request.QueryWhatIfForecastRequest = {
            "what_if_forecast_arn": what_if_forecast_arn,
            "filters": filters,
        }
        if start_date is not None:
            input_["start_date"] = start_date
        if end_date is not None:
            input_["end_date"] = end_date
        if next_token is not None:
            input_["next_token"] = next_token

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
