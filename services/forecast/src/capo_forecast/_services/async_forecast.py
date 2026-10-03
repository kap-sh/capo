"""Generated from Smithy shape ``com.amazonaws.forecast#AmazonForecast``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_forecast._auth._signers
import capo_forecast._auth._sigv4
from capo_forecast._auth._identity import Credentials
from capo_forecast._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_forecast._auth._zapros_handler import AuthMiddleware
from capo_forecast._pagination import resolve_path as _resolve_path
from capo_forecast._services._aws_config import aaws_config
from capo_forecast._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.arn_list
    import capo_forecast.types.auto_ml_override_strategy
    import capo_forecast.types.boolean
    import capo_forecast.types.create_auto_predictor_request
    import capo_forecast.types.create_auto_predictor_response
    import capo_forecast.types.create_dataset_group_request
    import capo_forecast.types.create_dataset_group_response
    import capo_forecast.types.create_dataset_import_job_request
    import capo_forecast.types.create_dataset_import_job_response
    import capo_forecast.types.create_dataset_request
    import capo_forecast.types.create_dataset_response
    import capo_forecast.types.create_explainability_export_request
    import capo_forecast.types.create_explainability_export_response
    import capo_forecast.types.create_explainability_request
    import capo_forecast.types.create_explainability_response
    import capo_forecast.types.create_forecast_export_job_request
    import capo_forecast.types.create_forecast_export_job_response
    import capo_forecast.types.create_forecast_request
    import capo_forecast.types.create_forecast_response
    import capo_forecast.types.create_monitor_request
    import capo_forecast.types.create_monitor_response
    import capo_forecast.types.create_predictor_backtest_export_job_request
    import capo_forecast.types.create_predictor_backtest_export_job_response
    import capo_forecast.types.create_predictor_request
    import capo_forecast.types.create_predictor_response
    import capo_forecast.types.create_what_if_analysis_request
    import capo_forecast.types.create_what_if_analysis_response
    import capo_forecast.types.create_what_if_forecast_export_request
    import capo_forecast.types.create_what_if_forecast_export_response
    import capo_forecast.types.create_what_if_forecast_request
    import capo_forecast.types.create_what_if_forecast_response
    import capo_forecast.types.data_config
    import capo_forecast.types.data_destination
    import capo_forecast.types.data_source
    import capo_forecast.types.dataset_group_summary
    import capo_forecast.types.dataset_import_job_summary
    import capo_forecast.types.dataset_summary
    import capo_forecast.types.dataset_type
    import capo_forecast.types.delete_dataset_group_request
    import capo_forecast.types.delete_dataset_import_job_request
    import capo_forecast.types.delete_dataset_request
    import capo_forecast.types.delete_explainability_export_request
    import capo_forecast.types.delete_explainability_request
    import capo_forecast.types.delete_forecast_export_job_request
    import capo_forecast.types.delete_forecast_request
    import capo_forecast.types.delete_monitor_request
    import capo_forecast.types.delete_predictor_backtest_export_job_request
    import capo_forecast.types.delete_predictor_request
    import capo_forecast.types.delete_resource_tree_request
    import capo_forecast.types.delete_what_if_analysis_request
    import capo_forecast.types.delete_what_if_forecast_export_request
    import capo_forecast.types.delete_what_if_forecast_request
    import capo_forecast.types.describe_auto_predictor_request
    import capo_forecast.types.describe_auto_predictor_response
    import capo_forecast.types.describe_dataset_group_request
    import capo_forecast.types.describe_dataset_group_response
    import capo_forecast.types.describe_dataset_import_job_request
    import capo_forecast.types.describe_dataset_import_job_response
    import capo_forecast.types.describe_dataset_request
    import capo_forecast.types.describe_dataset_response
    import capo_forecast.types.describe_explainability_export_request
    import capo_forecast.types.describe_explainability_export_response
    import capo_forecast.types.describe_explainability_request
    import capo_forecast.types.describe_explainability_response
    import capo_forecast.types.describe_forecast_export_job_request
    import capo_forecast.types.describe_forecast_export_job_response
    import capo_forecast.types.describe_forecast_request
    import capo_forecast.types.describe_forecast_response
    import capo_forecast.types.describe_monitor_request
    import capo_forecast.types.describe_monitor_response
    import capo_forecast.types.describe_predictor_backtest_export_job_request
    import capo_forecast.types.describe_predictor_backtest_export_job_response
    import capo_forecast.types.describe_predictor_request
    import capo_forecast.types.describe_predictor_response
    import capo_forecast.types.describe_what_if_analysis_request
    import capo_forecast.types.describe_what_if_analysis_response
    import capo_forecast.types.describe_what_if_forecast_export_request
    import capo_forecast.types.describe_what_if_forecast_export_response
    import capo_forecast.types.describe_what_if_forecast_request
    import capo_forecast.types.describe_what_if_forecast_response
    import capo_forecast.types.domain
    import capo_forecast.types.encryption_config
    import capo_forecast.types.evaluation_parameters
    import capo_forecast.types.explainability_config
    import capo_forecast.types.explainability_export_summary
    import capo_forecast.types.explainability_summary
    import capo_forecast.types.featurization_config
    import capo_forecast.types.filters
    import capo_forecast.types.forecast_dimensions
    import capo_forecast.types.forecast_export_job_summary
    import capo_forecast.types.forecast_summary
    import capo_forecast.types.forecast_types
    import capo_forecast.types.format
    import capo_forecast.types.frequency
    import capo_forecast.types.geolocation_format
    import capo_forecast.types.get_accuracy_metrics_request
    import capo_forecast.types.get_accuracy_metrics_response
    import capo_forecast.types.hyper_parameter_tuning_job_config
    import capo_forecast.types.import_mode
    import capo_forecast.types.input_data_config
    import capo_forecast.types.integer
    import capo_forecast.types.list_dataset_groups_request
    import capo_forecast.types.list_dataset_groups_response
    import capo_forecast.types.list_dataset_import_jobs_request
    import capo_forecast.types.list_dataset_import_jobs_response
    import capo_forecast.types.list_datasets_request
    import capo_forecast.types.list_datasets_response
    import capo_forecast.types.list_explainabilities_request
    import capo_forecast.types.list_explainabilities_response
    import capo_forecast.types.list_explainability_exports_request
    import capo_forecast.types.list_explainability_exports_response
    import capo_forecast.types.list_forecast_export_jobs_request
    import capo_forecast.types.list_forecast_export_jobs_response
    import capo_forecast.types.list_forecasts_request
    import capo_forecast.types.list_forecasts_response
    import capo_forecast.types.list_monitor_evaluations_request
    import capo_forecast.types.list_monitor_evaluations_response
    import capo_forecast.types.list_monitors_request
    import capo_forecast.types.list_monitors_response
    import capo_forecast.types.list_predictor_backtest_export_jobs_request
    import capo_forecast.types.list_predictor_backtest_export_jobs_response
    import capo_forecast.types.list_predictors_request
    import capo_forecast.types.list_predictors_response
    import capo_forecast.types.list_tags_for_resource_request
    import capo_forecast.types.list_tags_for_resource_response
    import capo_forecast.types.list_what_if_analyses_request
    import capo_forecast.types.list_what_if_analyses_response
    import capo_forecast.types.list_what_if_forecast_exports_request
    import capo_forecast.types.list_what_if_forecast_exports_response
    import capo_forecast.types.list_what_if_forecasts_request
    import capo_forecast.types.list_what_if_forecasts_response
    import capo_forecast.types.local_date_time
    import capo_forecast.types.long_arn
    import capo_forecast.types.max_results
    import capo_forecast.types.monitor_config
    import capo_forecast.types.monitor_summary
    import capo_forecast.types.name
    import capo_forecast.types.next_token
    import capo_forecast.types.optimization_metric
    import capo_forecast.types.predictor_backtest_export_job_summary
    import capo_forecast.types.predictor_monitor_evaluation
    import capo_forecast.types.predictor_summary
    import capo_forecast.types.resume_resource_request
    import capo_forecast.types.schema
    import capo_forecast.types.stop_resource_request
    import capo_forecast.types.tag_keys
    import capo_forecast.types.tag_resource_request
    import capo_forecast.types.tag_resource_response
    import capo_forecast.types.tags
    import capo_forecast.types.time_alignment_boundary
    import capo_forecast.types.time_series_replacements_data_source
    import capo_forecast.types.time_series_selector
    import capo_forecast.types.time_series_transformations
    import capo_forecast.types.time_zone
    import capo_forecast.types.timestamp_format
    import capo_forecast.types.training_parameters
    import capo_forecast.types.untag_resource_request
    import capo_forecast.types.untag_resource_response
    import capo_forecast.types.update_dataset_group_request
    import capo_forecast.types.update_dataset_group_response
    import capo_forecast.types.use_geolocation_for_time_zone
    import capo_forecast.types.what_if_analysis_summary
    import capo_forecast.types.what_if_forecast_arn_list_for_export
    import capo_forecast.types.what_if_forecast_export_summary
    import capo_forecast.types.what_if_forecast_summary


class AsyncforecastClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncforecastClient:
    """A client for the ``forecast`` service.

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
        self._config = AsyncforecastClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncforecastClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncforecastClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def create_auto_predictor(
        self,
        predictor_name: "capo_forecast.types.name.Name",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        forecast_horizon: Optional["capo_forecast.types.integer.Integer"] = None,
        forecast_types: Optional[
            "capo_forecast.types.forecast_types.ForecastTypes"
        ] = None,
        forecast_dimensions: Optional[
            "capo_forecast.types.forecast_dimensions.ForecastDimensions"
        ] = None,
        forecast_frequency: Optional["capo_forecast.types.frequency.Frequency"] = None,
        data_config: Optional["capo_forecast.types.data_config.DataConfig"] = None,
        encryption_config: Optional[
            "capo_forecast.types.encryption_config.EncryptionConfig"
        ] = None,
        reference_predictor_arn: Optional["capo_forecast.types.arn.Arn"] = None,
        optimization_metric: Optional[
            "capo_forecast.types.optimization_metric.OptimizationMetric"
        ] = None,
        explain_predictor: Optional["capo_forecast.types.boolean.Boolean"] = None,
        tags: Optional["capo_forecast.types.tags.Tags"] = None,
        monitor_config: Optional[
            "capo_forecast.types.monitor_config.MonitorConfig"
        ] = None,
        time_alignment_boundary: Optional[
            "capo_forecast.types.time_alignment_boundary.TimeAlignmentBoundary"
        ] = None,
    ) -> (
        "capo_forecast.types.create_auto_predictor_response.CreateAutoPredictorResponse"
    ):
        """<p>Creates an Amazon Forecast predictor.</p> <p>Amazon Forecast creates predictors with AutoPredictor, which involves applying the optimal combination of algorithms to each time series in your datasets. You can use <a>CreateAutoPredictor</a> to create new predictors or upgrade/retrain existing predictors.</p> <p> <b>Creating new predictors</b> </p> <p>The following parameters are required when creating a new predictor:</p> <ul> <li> <p> <code>PredictorName</code> - A unique name for the predictor.</p> </li> <li> <p> <code>DatasetGroupArn</code> - The ARN of the dataset group used to train the predictor.</p> </li> <li> <p> <code>ForecastFrequency</code> - The granularity of your forecasts (hourly, daily, weekly, etc).</p> </li> <li> <p> <code>ForecastHorizon</code> - The number of time-steps that the model predicts. The forecast horizon is also called the prediction length.</p> </li> </ul> <p>When creating a new predictor, do not specify a value for <code>ReferencePredictorArn</code>.</p> <p> <b>Upgrading and retraining predictors</b> </p> <p>The following parameters are required when retraining or upgrading a predictor:</p> <ul> <li> <p> <code>PredictorName</code> - A unique name for the predictor.</p> </li> <li> <p> <code>ReferencePredictorArn</code> - The ARN of the predictor to retrain or upgrade.</p> </li> </ul> <p>When upgrading or retraining a predictor, only specify values for the <code>ReferencePredictorArn</code> and <code>PredictorName</code>. </p>

        Args:
            predictor_name: <p>A unique name for the predictor</p>
            forecast_horizon: <p>The number of time-steps that the model predicts. The forecast horizon is also called the prediction length.</p> <p>The maximum forecast horizon is the lesser of 500 time-steps or 1/4 of the TARGET_TIME_SERIES dataset length. If you are retraining an existing AutoPredictor, then the maximum forecast horizon is the lesser of 500 time-steps or 1/3 of the TARGET_TIME_SERIES dataset length.</p> <p>If you are upgrading to an AutoPredictor or retraining an existing AutoPredictor, you cannot update the forecast horizon parameter. You can meet this requirement by providing longer time-series in the dataset.</p>
            forecast_types: <p>The forecast types used to train a predictor. You can specify up to five forecast types. Forecast types can be quantiles from 0.01 to 0.99, by increments of 0.01 or higher. You can also specify the mean forecast with <code>mean</code>.</p>
            forecast_dimensions: <p>An array of dimension (field) names that specify how to group the generated forecast.</p> <p>For example, if you are generating forecasts for item sales across all your stores, and your dataset contains a <code>store_id</code> field, you would specify <code>store_id</code> as a dimension to group sales forecasts for each store.</p>
            forecast_frequency: <p>The frequency of predictions in a forecast.</p> <p>Valid intervals are an integer followed by Y (Year), M (Month), W (Week), D (Day), H (Hour), and min (Minute). For example, "1D" indicates every day and "15min" indicates every 15 minutes. You cannot specify a value that would overlap with the next larger frequency. That means, for example, you cannot specify a frequency of 60 minutes, because that is equivalent to 1 hour. The valid values for each frequency are the following:</p> <ul> <li> <p>Minute - 1-59</p> </li> <li> <p>Hour - 1-23</p> </li> <li> <p>Day - 1-6</p> </li> <li> <p>Week - 1-4</p> </li> <li> <p>Month - 1-11</p> </li> <li> <p>Year - 1</p> </li> </ul> <p>Thus, if you want every other week forecasts, specify "2W". Or, if you want quarterly forecasts, you specify "3M".</p> <p>The frequency must be greater than or equal to the TARGET_TIME_SERIES dataset frequency.</p> <p>When a RELATED_TIME_SERIES dataset is provided, the frequency must be equal to the RELATED_TIME_SERIES dataset frequency.</p>
            data_config: <p>The data configuration for your dataset group and any additional datasets.</p>
            reference_predictor_arn: <p>The ARN of the predictor to retrain or upgrade. This parameter is only used when retraining or upgrading a predictor. When creating a new predictor, do not specify a value for this parameter.</p> <p>When upgrading or retraining a predictor, only specify values for the <code>ReferencePredictorArn</code> and <code>PredictorName</code>. The value for <code>PredictorName</code> must be a unique predictor name.</p>
            optimization_metric: <p>The accuracy metric used to optimize the predictor.</p>
            explain_predictor: <p>Create an Explainability resource for the predictor.</p>
            tags: <p>Optional metadata to help you categorize and organize your predictors. Each tag consists of a key and an optional value, both of which you define. Tag keys and values are case sensitive.</p> <p>The following restrictions apply to tags:</p> <ul> <li> <p>For each resource, each tag key must be unique and each tag key must have one value.</p> </li> <li> <p>Maximum number of tags per resource: 50.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8.</p> </li> <li> <p>Accepted characters: all letters and numbers, spaces representable in UTF-8, and + - = . _ : / @. If your tagging schema is used across other services and resources, the character restrictions of those services also apply. </p> </li> <li> <p>Key prefixes cannot include any upper or lowercase combination of <code>aws:</code> or <code>AWS:</code>. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit. You cannot edit or delete tag keys with this prefix.</p> </li> </ul>
            monitor_config: <p>The configuration details for predictor monitoring. Provide a name for the monitor resource to enable predictor monitoring.</p> <p>Predictor monitoring allows you to see how your predictor's performance changes over time. For more information, see <a href="https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring.html">Predictor Monitoring</a>.</p>
            time_alignment_boundary: <p>The time boundary Forecast uses to align and aggregate any data that doesn't align with your forecast frequency. Provide the unit of time and the time boundary as a key value pair. For more information on specifying a time boundary, see <a href="https://docs.aws.amazon.com/forecast/latest/dg/data-aggregation.html#specifying-time-boundary">Specifying a Time Boundary</a>. If you don't provide a time boundary, Forecast uses a set of <a href="https://docs.aws.amazon.com/forecast/latest/dg/data-aggregation.html#default-time-boundaries">Default Time Boundaries</a>.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of resources per account has been exceeded.</p>
            capo_forecast.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>There is already a resource with this name. Try again with a different name.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.create_auto_predictor_request.CreateAutoPredictorRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.create_auto_predictor_response.CreateAutoPredictorResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.create_auto_predictor

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.create_auto_predictor.async_create_auto_predictor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.create_auto_predictor_request.CreateAutoPredictorRequest = {
            "predictor_name": predictor_name
        }
        if forecast_horizon is not None:
            input_["forecast_horizon"] = forecast_horizon
        if forecast_types is not None:
            input_["forecast_types"] = forecast_types
        if forecast_dimensions is not None:
            input_["forecast_dimensions"] = forecast_dimensions
        if forecast_frequency is not None:
            input_["forecast_frequency"] = forecast_frequency
        if data_config is not None:
            input_["data_config"] = data_config
        if encryption_config is not None:
            input_["encryption_config"] = encryption_config
        if reference_predictor_arn is not None:
            input_["reference_predictor_arn"] = reference_predictor_arn
        if optimization_metric is not None:
            input_["optimization_metric"] = optimization_metric
        if explain_predictor is not None:
            input_["explain_predictor"] = explain_predictor
        if tags is not None:
            input_["tags"] = tags
        if monitor_config is not None:
            input_["monitor_config"] = monitor_config
        if time_alignment_boundary is not None:
            input_["time_alignment_boundary"] = time_alignment_boundary

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_dataset(
        self,
        dataset_name: "capo_forecast.types.name.Name",
        domain: "capo_forecast.types.domain.Domain",
        dataset_type: "capo_forecast.types.dataset_type.DatasetType",
        schema: "capo_forecast.types.schema.Schema",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        data_frequency: Optional["capo_forecast.types.frequency.Frequency"] = None,
        encryption_config: Optional[
            "capo_forecast.types.encryption_config.EncryptionConfig"
        ] = None,
        tags: Optional["capo_forecast.types.tags.Tags"] = None,
    ) -> "capo_forecast.types.create_dataset_response.CreateDatasetResponse":
        """<p>Creates an Amazon Forecast dataset. The information about the dataset that you provide helps Forecast understand how to consume the data for model training. This includes the following:</p> <ul> <li> <p> <i> <code>DataFrequency</code> </i> - How frequently your historical time-series data is collected.</p> </li> <li> <p> <i> <code>Domain</code> </i> and <i> <code>DatasetType</code> </i> - Each dataset has an associated dataset domain and a type within the domain. Amazon Forecast provides a list of predefined domains and types within each domain. For each unique dataset domain and type within the domain, Amazon Forecast requires your data to include a minimum set of predefined fields.</p> </li> <li> <p> <i> <code>Schema</code> </i> - A schema specifies the fields in the dataset, including the field name and data type.</p> </li> </ul> <p>After creating a dataset, you import your training data into it and add the dataset to a dataset group. You use the dataset group to create a predictor. For more information, see <a href="https://docs.aws.amazon.com/forecast/latest/dg/howitworks-datasets-groups.html">Importing datasets</a>.</p> <p>To get a list of all your datasets, use the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_ListDatasets.html">ListDatasets</a> operation.</p> <p>For example Forecast datasets, see the <a href="https://github.com/aws-samples/amazon-forecast-samples">Amazon Forecast Sample GitHub repository</a>.</p> <note> <p>The <code>Status</code> of a dataset must be <code>ACTIVE</code> before you can import training data. Use the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDataset.html">DescribeDataset</a> operation to get the status.</p> </note>

        Args:
            dataset_name: <p>A name for the dataset.</p>
            domain: <p>The domain associated with the dataset. When you add a dataset to a dataset group, this value and the value specified for the <code>Domain</code> parameter of the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html">CreateDatasetGroup</a> operation must match.</p> <p>The <code>Domain</code> and <code>DatasetType</code> that you choose determine the fields that must be present in the training data that you import to the dataset. For example, if you choose the <code>RETAIL</code> domain and <code>TARGET_TIME_SERIES</code> as the <code>DatasetType</code>, Amazon Forecast requires <code>item_id</code>, <code>timestamp</code>, and <code>demand</code> fields to be present in your data. For more information, see <a href="https://docs.aws.amazon.com/forecast/latest/dg/howitworks-datasets-groups.html">Importing datasets</a>.</p>
            dataset_type: <p>The dataset type. Valid values depend on the chosen <code>Domain</code>.</p>
            data_frequency: <p>The frequency of data collection. This parameter is required for RELATED_TIME_SERIES datasets.</p> <p>Valid intervals are an integer followed by Y (Year), M (Month), W (Week), D (Day), H (Hour), and min (Minute). For example, "1D" indicates every day and "15min" indicates every 15 minutes. You cannot specify a value that would overlap with the next larger frequency. That means, for example, you cannot specify a frequency of 60 minutes, because that is equivalent to 1 hour. The valid values for each frequency are the following:</p> <ul> <li> <p>Minute - 1-59</p> </li> <li> <p>Hour - 1-23</p> </li> <li> <p>Day - 1-6</p> </li> <li> <p>Week - 1-4</p> </li> <li> <p>Month - 1-11</p> </li> <li> <p>Year - 1</p> </li> </ul> <p>Thus, if you want every other week forecasts, specify "2W". Or, if you want quarterly forecasts, you specify "3M".</p>
            schema: <p>The schema for the dataset. The schema attributes and their order must match the fields in your data. The dataset <code>Domain</code> and <code>DatasetType</code> that you choose determine the minimum required fields in your training data. For information about the required fields for a specific dataset domain and type, see <a href="https://docs.aws.amazon.com/forecast/latest/dg/howitworks-domains-ds-types.html">Dataset Domains and Dataset Types</a>.</p>
            encryption_config: <p>An Key Management Service (KMS) key and the Identity and Access Management (IAM) role that Amazon Forecast can assume to access the key.</p>
            tags: <p>The optional metadata that you apply to the dataset to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for keys as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit.</p> </li> </ul>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of resources per account has been exceeded.</p>
            capo_forecast.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>There is already a resource with this name. Try again with a different name.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.create_dataset_request.CreateDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.create_dataset_response.CreateDatasetResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.create_dataset

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.create_dataset.async_create_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.create_dataset_request.CreateDatasetRequest = {
            "dataset_name": dataset_name,
            "domain": domain,
            "dataset_type": dataset_type,
            "schema": schema,
        }
        if data_frequency is not None:
            input_["data_frequency"] = data_frequency
        if encryption_config is not None:
            input_["encryption_config"] = encryption_config
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_dataset_group(
        self,
        dataset_group_name: "capo_forecast.types.name.Name",
        domain: "capo_forecast.types.domain.Domain",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        dataset_arns: Optional["capo_forecast.types.arn_list.ArnList"] = None,
        tags: Optional["capo_forecast.types.tags.Tags"] = None,
    ) -> "capo_forecast.types.create_dataset_group_response.CreateDatasetGroupResponse":
        """<p>Creates a dataset group, which holds a collection of related datasets. You can add datasets to the dataset group when you create the dataset group, or later by using the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_UpdateDatasetGroup.html">UpdateDatasetGroup</a> operation.</p> <p>After creating a dataset group and adding datasets, you use the dataset group when you create a predictor. For more information, see <a href="https://docs.aws.amazon.com/forecast/latest/dg/howitworks-datasets-groups.html">Dataset groups</a>.</p> <p>To get a list of all your datasets groups, use the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_ListDatasetGroups.html">ListDatasetGroups</a> operation.</p> <note> <p>The <code>Status</code> of a dataset group must be <code>ACTIVE</code> before you can use the dataset group to create a predictor. To get the status, use the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetGroup.html">DescribeDatasetGroup</a> operation.</p> </note>

        Args:
            dataset_group_name: <p>A name for the dataset group.</p>
            domain: <p>The domain associated with the dataset group. When you add a dataset to a dataset group, this value and the value specified for the <code>Domain</code> parameter of the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html">CreateDataset</a> operation must match.</p> <p>The <code>Domain</code> and <code>DatasetType</code> that you choose determine the fields that must be present in training data that you import to a dataset. For example, if you choose the <code>RETAIL</code> domain and <code>TARGET_TIME_SERIES</code> as the <code>DatasetType</code>, Amazon Forecast requires that <code>item_id</code>, <code>timestamp</code>, and <code>demand</code> fields are present in your data. For more information, see <a href="https://docs.aws.amazon.com/forecast/latest/dg/howitworks-datasets-groups.html">Dataset groups</a>.</p>
            dataset_arns: <p>An array of Amazon Resource Names (ARNs) of the datasets that you want to include in the dataset group.</p>
            tags: <p>The optional metadata that you apply to the dataset group to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for keys as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit.</p> </li> </ul>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of resources per account has been exceeded.</p>
            capo_forecast.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>There is already a resource with this name. Try again with a different name.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.create_dataset_group_request.CreateDatasetGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.create_dataset_group_response.CreateDatasetGroupResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.create_dataset_group

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.create_dataset_group.async_create_dataset_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.create_dataset_group_request.CreateDatasetGroupRequest = {
            "dataset_group_name": dataset_group_name,
            "domain": domain,
        }
        if dataset_arns is not None:
            input_["dataset_arns"] = dataset_arns
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_dataset_import_job(
        self,
        dataset_import_job_name: "capo_forecast.types.name.Name",
        dataset_arn: "capo_forecast.types.arn.Arn",
        data_source: "capo_forecast.types.data_source.DataSource",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        timestamp_format: Optional[
            "capo_forecast.types.timestamp_format.TimestampFormat"
        ] = None,
        time_zone: Optional["capo_forecast.types.time_zone.TimeZone"] = None,
        use_geolocation_for_time_zone: Optional[
            "capo_forecast.types.use_geolocation_for_time_zone.UseGeolocationForTimeZone"
        ] = None,
        geolocation_format: Optional[
            "capo_forecast.types.geolocation_format.GeolocationFormat"
        ] = None,
        tags: Optional["capo_forecast.types.tags.Tags"] = None,
        format: Optional["capo_forecast.types.format.Format"] = None,
        import_mode: Optional["capo_forecast.types.import_mode.ImportMode"] = None,
    ) -> "capo_forecast.types.create_dataset_import_job_response.CreateDatasetImportJobResponse":
        """<p>Imports your training data to an Amazon Forecast dataset. You provide the location of your training data in an Amazon Simple Storage Service (Amazon S3) bucket and the Amazon Resource Name (ARN) of the dataset that you want to import the data to.</p> <p>You must specify a <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_DataSource.html">DataSource</a> object that includes an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the data, as Amazon Forecast makes a copy of your data and processes it in an internal Amazon Web Services system. For more information, see <a href="https://docs.aws.amazon.com/forecast/latest/dg/aws-forecast-iam-roles.html">Set up permissions</a>.</p> <p>The training data must be in CSV or Parquet format. The delimiter must be a comma (,).</p> <p>You can specify the path to a specific file, the S3 bucket, or to a folder in the S3 bucket. For the latter two cases, Amazon Forecast imports all files up to the limit of 10,000 files.</p> <p>Because dataset imports are not aggregated, your most recent dataset import is the one that is used when training a predictor or generating a forecast. Make sure that your most recent dataset import contains all of the data you want to model off of, and not just the new data collected since the previous import.</p> <p>To get a list of all your dataset import jobs, filtered by specified criteria, use the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_ListDatasetImportJobs.html">ListDatasetImportJobs</a> operation.</p>

        Args:
            dataset_import_job_name: <p>The name for the dataset import job. We recommend including the current timestamp in the name, for example, <code>20190721DatasetImport</code>. This can help you avoid getting a <code>ResourceAlreadyExistsException</code> exception.</p>
            dataset_arn: <p>The Amazon Resource Name (ARN) of the Amazon Forecast dataset that you want to import data to.</p>
            data_source: <p>The location of the training data to import and an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the data. The training data must be stored in an Amazon S3 bucket.</p> <p>If encryption is used, <code>DataSource</code> must include an Key Management Service (KMS) key and the IAM role must allow Amazon Forecast permission to access the key. The KMS key and IAM role must match those specified in the <code>EncryptionConfig</code> parameter of the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html">CreateDataset</a> operation.</p>
            timestamp_format: <p>The format of timestamps in the dataset. The format that you specify depends on the <code>DataFrequency</code> specified when the dataset was created. The following formats are supported</p> <ul> <li> <p>"yyyy-MM-dd"</p> <p>For the following data frequencies: Y, M, W, and D</p> </li> <li> <p>"yyyy-MM-dd HH:mm:ss"</p> <p>For the following data frequencies: H, 30min, 15min, and 1min; and optionally, for: Y, M, W, and D</p> </li> </ul> <p>If the format isn't specified, Amazon Forecast expects the format to be "yyyy-MM-dd HH:mm:ss".</p>
            time_zone: <p>A single time zone for every item in your dataset. This option is ideal for datasets with all timestamps within a single time zone, or if all timestamps are normalized to a single time zone. </p> <p>Refer to the <a href="http://joda-time.sourceforge.net/timezones.html">Joda-Time API</a> for a complete list of valid time zone names.</p>
            use_geolocation_for_time_zone: <p>Automatically derive time zone information from the geolocation attribute. This option is ideal for datasets that contain timestamps in multiple time zones and those timestamps are expressed in local time.</p>
            geolocation_format: <p>The format of the geolocation attribute. The geolocation attribute can be formatted in one of two ways:</p> <ul> <li> <p> <code>LAT_LONG</code> - the latitude and longitude in decimal format (Example: 47.61_-122.33).</p> </li> <li> <p> <code>CC_POSTALCODE</code> (US Only) - the country code (US), followed by the 5-digit ZIP code (Example: US_98121).</p> </li> </ul>
            tags: <p>The optional metadata that you apply to the dataset import job to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for keys as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit.</p> </li> </ul>
            format: <p>The format of the imported data, CSV or PARQUET. The default value is CSV.</p>
            import_mode: <p>Specifies whether the dataset import job is a <code>FULL</code> or <code>INCREMENTAL</code> import. A <code>FULL</code> dataset import replaces all of the existing data with the newly imported data. An <code>INCREMENTAL</code> import appends the imported data to the existing data.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of resources per account has been exceeded.</p>
            capo_forecast.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>There is already a resource with this name. Try again with a different name.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.create_dataset_import_job_request.CreateDatasetImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.create_dataset_import_job_response.CreateDatasetImportJobResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.create_dataset_import_job

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.create_dataset_import_job.async_create_dataset_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.create_dataset_import_job_request.CreateDatasetImportJobRequest = {
            "dataset_import_job_name": dataset_import_job_name,
            "dataset_arn": dataset_arn,
            "data_source": data_source,
        }
        if timestamp_format is not None:
            input_["timestamp_format"] = timestamp_format
        if time_zone is not None:
            input_["time_zone"] = time_zone
        if use_geolocation_for_time_zone is not None:
            input_["use_geolocation_for_time_zone"] = use_geolocation_for_time_zone
        if geolocation_format is not None:
            input_["geolocation_format"] = geolocation_format
        if tags is not None:
            input_["tags"] = tags
        if format is not None:
            input_["format"] = format
        if import_mode is not None:
            input_["import_mode"] = import_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_explainability(
        self,
        explainability_name: "capo_forecast.types.name.Name",
        resource_arn: "capo_forecast.types.arn.Arn",
        explainability_config: "capo_forecast.types.explainability_config.ExplainabilityConfig",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        data_source: Optional["capo_forecast.types.data_source.DataSource"] = None,
        schema: Optional["capo_forecast.types.schema.Schema"] = None,
        enable_visualization: Optional["capo_forecast.types.boolean.Boolean"] = None,
        start_date_time: Optional[
            "capo_forecast.types.local_date_time.LocalDateTime"
        ] = None,
        end_date_time: Optional[
            "capo_forecast.types.local_date_time.LocalDateTime"
        ] = None,
        tags: Optional["capo_forecast.types.tags.Tags"] = None,
    ) -> "capo_forecast.types.create_explainability_response.CreateExplainabilityResponse":
        """<note> <p>Explainability is only available for Forecasts and Predictors generated from an AutoPredictor (<a>CreateAutoPredictor</a>)</p> </note> <p>Creates an Amazon Forecast Explainability.</p> <p>Explainability helps you better understand how the attributes in your datasets impact forecast. Amazon Forecast uses a metric called Impact scores to quantify the relative impact of each attribute and determine whether they increase or decrease forecast values.</p> <p>To enable Forecast Explainability, your predictor must include at least one of the following: related time series, item metadata, or additional datasets like Holidays and the Weather Index.</p> <p>CreateExplainability accepts either a Predictor ARN or Forecast ARN. To receive aggregated Impact scores for all time series and time points in your datasets, provide a Predictor ARN. To receive Impact scores for specific time series and time points, provide a Forecast ARN.</p> <p> <b>CreateExplainability with a Predictor ARN</b> </p> <note> <p>You can only have one Explainability resource per predictor. If you already enabled <code>ExplainPredictor</code> in <a>CreateAutoPredictor</a>, that predictor already has an Explainability resource.</p> </note> <p>The following parameters are required when providing a Predictor ARN:</p> <ul> <li> <p> <code>ExplainabilityName</code> - A unique name for the Explainability.</p> </li> <li> <p> <code>ResourceArn</code> - The Arn of the predictor.</p> </li> <li> <p> <code>TimePointGranularity</code> - Must be set to “ALL”.</p> </li> <li> <p> <code>TimeSeriesGranularity</code> - Must be set to “ALL”.</p> </li> </ul> <p>Do not specify a value for the following parameters:</p> <ul> <li> <p> <code>DataSource</code> - Only valid when TimeSeriesGranularity is “SPECIFIC”.</p> </li> <li> <p> <code>Schema</code> - Only valid when TimeSeriesGranularity is “SPECIFIC”.</p> </li> <li> <p> <code>StartDateTime</code> - Only valid when TimePointGranularity is “SPECIFIC”.</p> </li> <li> <p> <code>EndDateTime</code> - Only valid when TimePointGranularity is “SPECIFIC”.</p> </li> </ul> <p> <b>CreateExplainability with a Forecast ARN</b> </p> <note> <p>You can specify a maximum of 50 time series and 500 time points.</p> </note> <p>The following parameters are required when providing a Predictor ARN:</p> <ul> <li> <p> <code>ExplainabilityName</code> - A unique name for the Explainability.</p> </li> <li> <p> <code>ResourceArn</code> - The Arn of the forecast.</p> </li> <li> <p> <code>TimePointGranularity</code> - Either “ALL” or “SPECIFIC”.</p> </li> <li> <p> <code>TimeSeriesGranularity</code> - Either “ALL” or “SPECIFIC”.</p> </li> </ul> <p>If you set TimeSeriesGranularity to “SPECIFIC”, you must also provide the following:</p> <ul> <li> <p> <code>DataSource</code> - The S3 location of the CSV file specifying your time series.</p> </li> <li> <p> <code>Schema</code> - The Schema defines the attributes and attribute types listed in the Data Source.</p> </li> </ul> <p>If you set TimePointGranularity to “SPECIFIC”, you must also provide the following:</p> <ul> <li> <p> <code>StartDateTime</code> - The first timestamp in the range of time points.</p> </li> <li> <p> <code>EndDateTime</code> - The last timestamp in the range of time points.</p> </li> </ul>

        Args:
            explainability_name: <p>A unique name for the Explainability.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the Predictor or Forecast used to create the Explainability.</p>
            explainability_config: <p>The configuration settings that define the granularity of time series and time points for the Explainability.</p>
            enable_visualization: <p>Create an Explainability visualization that is viewable within the Amazon Web Services console.</p>
            start_date_time: <p>If <code>TimePointGranularity</code> is set to <code>SPECIFIC</code>, define the first point for the Explainability.</p> <p>Use the following timestamp format: yyyy-MM-ddTHH:mm:ss (example: 2015-01-01T20:00:00)</p>
            end_date_time: <p>If <code>TimePointGranularity</code> is set to <code>SPECIFIC</code>, define the last time point for the Explainability.</p> <p>Use the following timestamp format: yyyy-MM-ddTHH:mm:ss (example: 2015-01-01T20:00:00)</p>
            tags: <p>Optional metadata to help you categorize and organize your resources. Each tag consists of a key and an optional value, both of which you define. Tag keys and values are case sensitive.</p> <p>The following restrictions apply to tags:</p> <ul> <li> <p>For each resource, each tag key must be unique and each tag key must have one value.</p> </li> <li> <p>Maximum number of tags per resource: 50.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8.</p> </li> <li> <p>Accepted characters: all letters and numbers, spaces representable in UTF-8, and + - = . _ : / @. If your tagging schema is used across other services and resources, the character restrictions of those services also apply. </p> </li> <li> <p>Key prefixes cannot include any upper or lowercase combination of <code>aws:</code> or <code>AWS:</code>. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit. You cannot edit or delete tag keys with this prefix.</p> </li> </ul>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of resources per account has been exceeded.</p>
            capo_forecast.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>There is already a resource with this name. Try again with a different name.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.create_explainability_request.CreateExplainabilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.create_explainability_response.CreateExplainabilityResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.create_explainability

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.create_explainability.async_create_explainability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.create_explainability_request.CreateExplainabilityRequest = {
            "explainability_name": explainability_name,
            "resource_arn": resource_arn,
            "explainability_config": explainability_config,
        }
        if data_source is not None:
            input_["data_source"] = data_source
        if schema is not None:
            input_["schema"] = schema
        if enable_visualization is not None:
            input_["enable_visualization"] = enable_visualization
        if start_date_time is not None:
            input_["start_date_time"] = start_date_time
        if end_date_time is not None:
            input_["end_date_time"] = end_date_time
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_explainability_export(
        self,
        explainability_export_name: "capo_forecast.types.name.Name",
        explainability_arn: "capo_forecast.types.arn.Arn",
        destination: "capo_forecast.types.data_destination.DataDestination",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        tags: Optional["capo_forecast.types.tags.Tags"] = None,
        format: Optional["capo_forecast.types.format.Format"] = None,
    ) -> "capo_forecast.types.create_explainability_export_response.CreateExplainabilityExportResponse":
        """<p>Exports an Explainability resource created by the <a>CreateExplainability</a> operation. Exported files are exported to an Amazon Simple Storage Service (Amazon S3) bucket.</p> <p>You must specify a <a>DataDestination</a> object that includes an Amazon S3 bucket and an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the Amazon S3 bucket. For more information, see <a>aws-forecast-iam-roles</a>.</p> <note> <p>The <code>Status</code> of the export job must be <code>ACTIVE</code> before you can access the export in your Amazon S3 bucket. To get the status, use the <a>DescribeExplainabilityExport</a> operation.</p> </note>

        Args:
            explainability_export_name: <p>A unique name for the Explainability export.</p>
            explainability_arn: <p>The Amazon Resource Name (ARN) of the Explainability to export.</p>
            tags: <p>Optional metadata to help you categorize and organize your resources. Each tag consists of a key and an optional value, both of which you define. Tag keys and values are case sensitive.</p> <p>The following restrictions apply to tags:</p> <ul> <li> <p>For each resource, each tag key must be unique and each tag key must have one value.</p> </li> <li> <p>Maximum number of tags per resource: 50.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8.</p> </li> <li> <p>Accepted characters: all letters and numbers, spaces representable in UTF-8, and + - = . _ : / @. If your tagging schema is used across other services and resources, the character restrictions of those services also apply. </p> </li> <li> <p>Key prefixes cannot include any upper or lowercase combination of <code>aws:</code> or <code>AWS:</code>. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit. You cannot edit or delete tag keys with this prefix.</p> </li> </ul>
            format: <p>The format of the exported data, CSV or PARQUET.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of resources per account has been exceeded.</p>
            capo_forecast.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>There is already a resource with this name. Try again with a different name.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.create_explainability_export_request.CreateExplainabilityExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.create_explainability_export_response.CreateExplainabilityExportResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.create_explainability_export

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.create_explainability_export.async_create_explainability_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.create_explainability_export_request.CreateExplainabilityExportRequest = {
            "explainability_export_name": explainability_export_name,
            "explainability_arn": explainability_arn,
            "destination": destination,
        }
        if tags is not None:
            input_["tags"] = tags
        if format is not None:
            input_["format"] = format

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_forecast(
        self,
        forecast_name: "capo_forecast.types.name.Name",
        predictor_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        forecast_types: Optional[
            "capo_forecast.types.forecast_types.ForecastTypes"
        ] = None,
        tags: Optional["capo_forecast.types.tags.Tags"] = None,
        time_series_selector: Optional[
            "capo_forecast.types.time_series_selector.TimeSeriesSelector"
        ] = None,
    ) -> "capo_forecast.types.create_forecast_response.CreateForecastResponse":
        """<p>Creates a forecast for each item in the <code>TARGET_TIME_SERIES</code> dataset that was used to train the predictor. This is known as inference. To retrieve the forecast for a single item at low latency, use the operation. To export the complete forecast into your Amazon Simple Storage Service (Amazon S3) bucket, use the <a>CreateForecastExportJob</a> operation.</p> <p>The range of the forecast is determined by the <code>ForecastHorizon</code> value, which you specify in the <a>CreatePredictor</a> request. When you query a forecast, you can request a specific date range within the forecast.</p> <p>To get a list of all your forecasts, use the <a>ListForecasts</a> operation.</p> <note> <p>The forecasts generated by Amazon Forecast are in the same time zone as the dataset that was used to create the predictor.</p> </note> <p>For more information, see <a>howitworks-forecast</a>.</p> <note> <p>The <code>Status</code> of the forecast must be <code>ACTIVE</code> before you can query or export the forecast. Use the <a>DescribeForecast</a> operation to get the status.</p> </note> <p>By default, a forecast includes predictions for every item (<code>item_id</code>) in the dataset group that was used to train the predictor. However, you can use the <code>TimeSeriesSelector</code> object to generate a forecast on a subset of time series. Forecast creation is skipped for any time series that you specify that are not in the input dataset. The forecast export file will not contain these time series or their forecasted values.</p>

        Args:
            forecast_name: <p>A name for the forecast.</p>
            predictor_arn: <p>The Amazon Resource Name (ARN) of the predictor to use to generate the forecast.</p>
            forecast_types: <p>The quantiles at which probabilistic forecasts are generated. <b>You can currently specify up to 5 quantiles per forecast</b>. Accepted values include <code>0.01 to 0.99</code> (increments of .01 only) and <code>mean</code>. The mean forecast is different from the median (0.50) when the distribution is not symmetric (for example, Beta and Negative Binomial). </p> <p>The default quantiles are the quantiles you specified during predictor creation. If you didn't specify quantiles, the default values are <code>["0.1", "0.5", "0.9"]</code>. </p>
            tags: <p>The optional metadata that you apply to the forecast to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for keys as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit.</p> </li> </ul>
            time_series_selector: <p>Defines the set of time series that are used to create the forecasts in a <code>TimeSeriesIdentifiers</code> object.</p> <p>The <code>TimeSeriesIdentifiers</code> object needs the following information:</p> <ul> <li> <p> <code>DataSource</code> </p> </li> <li> <p> <code>Format</code> </p> </li> <li> <p> <code>Schema</code> </p> </li> </ul>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of resources per account has been exceeded.</p>
            capo_forecast.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>There is already a resource with this name. Try again with a different name.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.create_forecast_request.CreateForecastRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.create_forecast_response.CreateForecastResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.create_forecast

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.create_forecast.async_create_forecast(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.create_forecast_request.CreateForecastRequest = {
            "forecast_name": forecast_name,
            "predictor_arn": predictor_arn,
        }
        if forecast_types is not None:
            input_["forecast_types"] = forecast_types
        if tags is not None:
            input_["tags"] = tags
        if time_series_selector is not None:
            input_["time_series_selector"] = time_series_selector

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_forecast_export_job(
        self,
        forecast_export_job_name: "capo_forecast.types.name.Name",
        forecast_arn: "capo_forecast.types.arn.Arn",
        destination: "capo_forecast.types.data_destination.DataDestination",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        tags: Optional["capo_forecast.types.tags.Tags"] = None,
        format: Optional["capo_forecast.types.format.Format"] = None,
    ) -> "capo_forecast.types.create_forecast_export_job_response.CreateForecastExportJobResponse":
        """<p>Exports a forecast created by the <a>CreateForecast</a> operation to your Amazon Simple Storage Service (Amazon S3) bucket. The forecast file name will match the following conventions:</p> <p><ForecastExportJobName>_<ExportTimestamp>_<PartNumber></p> <p>where the <ExportTimestamp> component is in Java SimpleDateFormat (yyyy-MM-ddTHH-mm-ssZ).</p> <p>You must specify a <a>DataDestination</a> object that includes an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the Amazon S3 bucket. For more information, see <a>aws-forecast-iam-roles</a>.</p> <p>For more information, see <a>howitworks-forecast</a>.</p> <p>To get a list of all your forecast export jobs, use the <a>ListForecastExportJobs</a> operation.</p> <note> <p>The <code>Status</code> of the forecast export job must be <code>ACTIVE</code> before you can access the forecast in your Amazon S3 bucket. To get the status, use the <a>DescribeForecastExportJob</a> operation.</p> </note>

        Args:
            forecast_export_job_name: <p>The name for the forecast export job.</p>
            forecast_arn: <p>The Amazon Resource Name (ARN) of the forecast that you want to export.</p>
            destination: <p>The location where you want to save the forecast and an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the location. The forecast must be exported to an Amazon S3 bucket.</p> <p>If encryption is used, <code>Destination</code> must include an Key Management Service (KMS) key. The IAM role must allow Amazon Forecast permission to access the key.</p>
            tags: <p>The optional metadata that you apply to the forecast export job to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for keys as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit.</p> </li> </ul>
            format: <p>The format of the exported data, CSV or PARQUET. The default value is CSV.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of resources per account has been exceeded.</p>
            capo_forecast.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>There is already a resource with this name. Try again with a different name.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.create_forecast_export_job_request.CreateForecastExportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.create_forecast_export_job_response.CreateForecastExportJobResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.create_forecast_export_job

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.create_forecast_export_job.async_create_forecast_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.create_forecast_export_job_request.CreateForecastExportJobRequest = {
            "forecast_export_job_name": forecast_export_job_name,
            "forecast_arn": forecast_arn,
            "destination": destination,
        }
        if tags is not None:
            input_["tags"] = tags
        if format is not None:
            input_["format"] = format

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_monitor(
        self,
        monitor_name: "capo_forecast.types.name.Name",
        resource_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        tags: Optional["capo_forecast.types.tags.Tags"] = None,
    ) -> "capo_forecast.types.create_monitor_response.CreateMonitorResponse":
        """<p>Creates a predictor monitor resource for an existing auto predictor. Predictor monitoring allows you to see how your predictor's performance changes over time. For more information, see <a href="https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring.html">Predictor Monitoring</a>. </p>

        Args:
            monitor_name: <p>The name of the monitor resource.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the predictor to monitor.</p>
            tags: <p>A list of <a href="https://docs.aws.amazon.com/forecast/latest/dg/tagging-forecast-resources.html">tags</a> to apply to the monitor resource.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of resources per account has been exceeded.</p>
            capo_forecast.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>There is already a resource with this name. Try again with a different name.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.create_monitor_request.CreateMonitorRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.create_monitor_response.CreateMonitorResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.create_monitor

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.create_monitor.async_create_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.create_monitor_request.CreateMonitorRequest = {
            "monitor_name": monitor_name,
            "resource_arn": resource_arn,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_predictor(
        self,
        predictor_name: "capo_forecast.types.name.Name",
        forecast_horizon: "capo_forecast.types.integer.Integer",
        input_data_config: "capo_forecast.types.input_data_config.InputDataConfig",
        featurization_config: "capo_forecast.types.featurization_config.FeaturizationConfig",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        algorithm_arn: Optional["capo_forecast.types.arn.Arn"] = None,
        forecast_types: Optional[
            "capo_forecast.types.forecast_types.ForecastTypes"
        ] = None,
        perform_auto_ml: Optional["capo_forecast.types.boolean.Boolean"] = None,
        auto_ml_override_strategy: Optional[
            "capo_forecast.types.auto_ml_override_strategy.AutoMLOverrideStrategy"
        ] = None,
        perform_hpo: Optional["capo_forecast.types.boolean.Boolean"] = None,
        training_parameters: Optional[
            "capo_forecast.types.training_parameters.TrainingParameters"
        ] = None,
        evaluation_parameters: Optional[
            "capo_forecast.types.evaluation_parameters.EvaluationParameters"
        ] = None,
        hpo_config: Optional[
            "capo_forecast.types.hyper_parameter_tuning_job_config.HyperParameterTuningJobConfig"
        ] = None,
        encryption_config: Optional[
            "capo_forecast.types.encryption_config.EncryptionConfig"
        ] = None,
        tags: Optional["capo_forecast.types.tags.Tags"] = None,
        optimization_metric: Optional[
            "capo_forecast.types.optimization_metric.OptimizationMetric"
        ] = None,
    ) -> "capo_forecast.types.create_predictor_response.CreatePredictorResponse":
        """<note> <p> This operation creates a legacy predictor that does not include all the predictor functionalities provided by Amazon Forecast. To create a predictor that is compatible with all aspects of Forecast, use <a>CreateAutoPredictor</a>.</p> </note> <p>Creates an Amazon Forecast predictor.</p> <p>In the request, provide a dataset group and either specify an algorithm or let Amazon Forecast choose an algorithm for you using AutoML. If you specify an algorithm, you also can override algorithm-specific hyperparameters.</p> <p>Amazon Forecast uses the algorithm to train a predictor using the latest version of the datasets in the specified dataset group. You can then generate a forecast using the <a>CreateForecast</a> operation.</p> <p> To see the evaluation metrics, use the <a>GetAccuracyMetrics</a> operation. </p> <p>You can specify a featurization configuration to fill and aggregate the data fields in the <code>TARGET_TIME_SERIES</code> dataset to improve model training. For more information, see <a>FeaturizationConfig</a>.</p> <p>For RELATED_TIME_SERIES datasets, <code>CreatePredictor</code> verifies that the <code>DataFrequency</code> specified when the dataset was created matches the <code>ForecastFrequency</code>. TARGET_TIME_SERIES datasets don't have this restriction. Amazon Forecast also verifies the delimiter and timestamp format. For more information, see <a>howitworks-datasets-groups</a>.</p> <p>By default, predictors are trained and evaluated at the 0.1 (P10), 0.5 (P50), and 0.9 (P90) quantiles. You can choose custom forecast types to train and evaluate your predictor by setting the <code>ForecastTypes</code>. </p> <p> <b>AutoML</b> </p> <p>If you want Amazon Forecast to evaluate each algorithm and choose the one that minimizes the <code>objective function</code>, set <code>PerformAutoML</code> to <code>true</code>. The <code>objective function</code> is defined as the mean of the weighted losses over the forecast types. By default, these are the p10, p50, and p90 quantile losses. For more information, see <a>EvaluationResult</a>.</p> <p>When AutoML is enabled, the following properties are disallowed:</p> <ul> <li> <p> <code>AlgorithmArn</code> </p> </li> <li> <p> <code>HPOConfig</code> </p> </li> <li> <p> <code>PerformHPO</code> </p> </li> <li> <p> <code>TrainingParameters</code> </p> </li> </ul> <p>To get a list of all of your predictors, use the <a>ListPredictors</a> operation.</p> <note> <p>Before you can use the predictor to create a forecast, the <code>Status</code> of the predictor must be <code>ACTIVE</code>, signifying that training has completed. To get the status, use the <a>DescribePredictor</a> operation.</p> </note>

        Args:
            predictor_name: <p>A name for the predictor.</p>
            algorithm_arn: <p>The Amazon Resource Name (ARN) of the algorithm to use for model training. Required if <code>PerformAutoML</code> is not set to <code>true</code>.</p> <p class="title"> <b>Supported algorithms:</b> </p> <ul> <li> <p> <code>arn:aws:forecast:::algorithm/ARIMA</code> </p> </li> <li> <p> <code>arn:aws:forecast:::algorithm/CNN-QR</code> </p> </li> <li> <p> <code>arn:aws:forecast:::algorithm/Deep_AR_Plus</code> </p> </li> <li> <p> <code>arn:aws:forecast:::algorithm/ETS</code> </p> </li> <li> <p> <code>arn:aws:forecast:::algorithm/NPTS</code> </p> </li> <li> <p> <code>arn:aws:forecast:::algorithm/Prophet</code> </p> </li> </ul>
            forecast_horizon: <p>Specifies the number of time-steps that the model is trained to predict. The forecast horizon is also called the prediction length.</p> <p>For example, if you configure a dataset for daily data collection (using the <code>DataFrequency</code> parameter of the <a>CreateDataset</a> operation) and set the forecast horizon to 10, the model returns predictions for 10 days.</p> <p>The maximum forecast horizon is the lesser of 500 time-steps or 1/3 of the TARGET_TIME_SERIES dataset length.</p>
            forecast_types: <p>Specifies the forecast types used to train a predictor. You can specify up to five forecast types. Forecast types can be quantiles from 0.01 to 0.99, by increments of 0.01 or higher. You can also specify the mean forecast with <code>mean</code>. </p> <p>The default value is <code>["0.10", "0.50", "0.9"]</code>.</p>
            perform_auto_ml: <p>Whether to perform AutoML. When Amazon Forecast performs AutoML, it evaluates the algorithms it provides and chooses the best algorithm and configuration for your training dataset.</p> <p>The default value is <code>false</code>. In this case, you are required to specify an algorithm.</p> <p>Set <code>PerformAutoML</code> to <code>true</code> to have Amazon Forecast perform AutoML. This is a good option if you aren't sure which algorithm is suitable for your training data. In this case, <code>PerformHPO</code> must be false.</p>
            auto_ml_override_strategy: <note> <p> The <code>LatencyOptimized</code> AutoML override strategy is only available in private beta. Contact Amazon Web Services Support or your account manager to learn more about access privileges. </p> </note> <p>Used to overide the default AutoML strategy, which is to optimize predictor accuracy. To apply an AutoML strategy that minimizes training time, use <code>LatencyOptimized</code>.</p> <p>This parameter is only valid for predictors trained using AutoML.</p>
            perform_hpo: <p>Whether to perform hyperparameter optimization (HPO). HPO finds optimal hyperparameter values for your training data. The process of performing HPO is known as running a hyperparameter tuning job.</p> <p>The default value is <code>false</code>. In this case, Amazon Forecast uses default hyperparameter values from the chosen algorithm.</p> <p>To override the default values, set <code>PerformHPO</code> to <code>true</code> and, optionally, supply the <a>HyperParameterTuningJobConfig</a> object. The tuning job specifies a metric to optimize, which hyperparameters participate in tuning, and the valid range for each tunable hyperparameter. In this case, you are required to specify an algorithm and <code>PerformAutoML</code> must be false.</p> <p>The following algorithms support HPO:</p> <ul> <li> <p>DeepAR+</p> </li> <li> <p>CNN-QR</p> </li> </ul>
            training_parameters: <p>The hyperparameters to override for model training. The hyperparameters that you can override are listed in the individual algorithms. For the list of supported algorithms, see <a>aws-forecast-choosing-recipes</a>.</p>
            evaluation_parameters: <p>Used to override the default evaluation parameters of the specified algorithm. Amazon Forecast evaluates a predictor by splitting a dataset into training data and testing data. The evaluation parameters define how to perform the split and the number of iterations.</p>
            hpo_config: <p>Provides hyperparameter override values for the algorithm. If you don't provide this parameter, Amazon Forecast uses default values. The individual algorithms specify which hyperparameters support hyperparameter optimization (HPO). For more information, see <a>aws-forecast-choosing-recipes</a>.</p> <p>If you included the <code>HPOConfig</code> object, you must set <code>PerformHPO</code> to true.</p>
            input_data_config: <p>Describes the dataset group that contains the data to use to train the predictor.</p>
            featurization_config: <p>The featurization configuration.</p>
            encryption_config: <p>An Key Management Service (KMS) key and the Identity and Access Management (IAM) role that Amazon Forecast can assume to access the key.</p>
            tags: <p>The optional metadata that you apply to the predictor to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for keys as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit.</p> </li> </ul>
            optimization_metric: <p>The accuracy metric used to optimize the predictor.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of resources per account has been exceeded.</p>
            capo_forecast.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>There is already a resource with this name. Try again with a different name.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.create_predictor_request.CreatePredictorRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.create_predictor_response.CreatePredictorResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.create_predictor

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.create_predictor.async_create_predictor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.create_predictor_request.CreatePredictorRequest = {
            "predictor_name": predictor_name,
            "forecast_horizon": forecast_horizon,
            "input_data_config": input_data_config,
            "featurization_config": featurization_config,
        }
        if algorithm_arn is not None:
            input_["algorithm_arn"] = algorithm_arn
        if forecast_types is not None:
            input_["forecast_types"] = forecast_types
        if perform_auto_ml is not None:
            input_["perform_auto_ml"] = perform_auto_ml
        if auto_ml_override_strategy is not None:
            input_["auto_ml_override_strategy"] = auto_ml_override_strategy
        if perform_hpo is not None:
            input_["perform_hpo"] = perform_hpo
        if training_parameters is not None:
            input_["training_parameters"] = training_parameters
        if evaluation_parameters is not None:
            input_["evaluation_parameters"] = evaluation_parameters
        if hpo_config is not None:
            input_["hpo_config"] = hpo_config
        if encryption_config is not None:
            input_["encryption_config"] = encryption_config
        if tags is not None:
            input_["tags"] = tags
        if optimization_metric is not None:
            input_["optimization_metric"] = optimization_metric

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_predictor_backtest_export_job(
        self,
        predictor_backtest_export_job_name: "capo_forecast.types.name.Name",
        predictor_arn: "capo_forecast.types.arn.Arn",
        destination: "capo_forecast.types.data_destination.DataDestination",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        tags: Optional["capo_forecast.types.tags.Tags"] = None,
        format: Optional["capo_forecast.types.format.Format"] = None,
    ) -> "capo_forecast.types.create_predictor_backtest_export_job_response.CreatePredictorBacktestExportJobResponse":
        """<p>Exports backtest forecasts and accuracy metrics generated by the <a>CreateAutoPredictor</a> or <a>CreatePredictor</a> operations. Two folders containing CSV or Parquet files are exported to your specified S3 bucket.</p> <p> The export file names will match the following conventions:</p> <p> <code><ExportJobName>_<ExportTimestamp>_<PartNumber>.csv</code> </p> <p>The <ExportTimestamp> component is in Java SimpleDate format (yyyy-MM-ddTHH-mm-ssZ).</p> <p>You must specify a <a>DataDestination</a> object that includes an Amazon S3 bucket and an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the Amazon S3 bucket. For more information, see <a>aws-forecast-iam-roles</a>.</p> <note> <p>The <code>Status</code> of the export job must be <code>ACTIVE</code> before you can access the export in your Amazon S3 bucket. To get the status, use the <a>DescribePredictorBacktestExportJob</a> operation.</p> </note>

        Args:
            predictor_backtest_export_job_name: <p>The name for the backtest export job.</p>
            predictor_arn: <p>The Amazon Resource Name (ARN) of the predictor that you want to export.</p>
            tags: <p>Optional metadata to help you categorize and organize your backtests. Each tag consists of a key and an optional value, both of which you define. Tag keys and values are case sensitive.</p> <p>The following restrictions apply to tags:</p> <ul> <li> <p>For each resource, each tag key must be unique and each tag key must have one value.</p> </li> <li> <p>Maximum number of tags per resource: 50.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8.</p> </li> <li> <p>Accepted characters: all letters and numbers, spaces representable in UTF-8, and + - = . _ : / @. If your tagging schema is used across other services and resources, the character restrictions of those services also apply. </p> </li> <li> <p>Key prefixes cannot include any upper or lowercase combination of <code>aws:</code> or <code>AWS:</code>. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit. You cannot edit or delete tag keys with this prefix.</p> </li> </ul>
            format: <p>The format of the exported data, CSV or PARQUET. The default value is CSV.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of resources per account has been exceeded.</p>
            capo_forecast.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>There is already a resource with this name. Try again with a different name.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.create_predictor_backtest_export_job_request.CreatePredictorBacktestExportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.create_predictor_backtest_export_job_response.CreatePredictorBacktestExportJobResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.create_predictor_backtest_export_job

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.create_predictor_backtest_export_job.async_create_predictor_backtest_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.create_predictor_backtest_export_job_request.CreatePredictorBacktestExportJobRequest = {
            "predictor_backtest_export_job_name": predictor_backtest_export_job_name,
            "predictor_arn": predictor_arn,
            "destination": destination,
        }
        if tags is not None:
            input_["tags"] = tags
        if format is not None:
            input_["format"] = format

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_what_if_analysis(
        self,
        what_if_analysis_name: "capo_forecast.types.name.Name",
        forecast_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        time_series_selector: Optional[
            "capo_forecast.types.time_series_selector.TimeSeriesSelector"
        ] = None,
        tags: Optional["capo_forecast.types.tags.Tags"] = None,
    ) -> "capo_forecast.types.create_what_if_analysis_response.CreateWhatIfAnalysisResponse":
        """<p>What-if analysis is a scenario modeling technique where you make a hypothetical change to a time series and compare the forecasts generated by these changes against the baseline, unchanged time series. It is important to remember that the purpose of a what-if analysis is to understand how a forecast can change given different modifications to the baseline time series.</p> <p>For example, imagine you are a clothing retailer who is considering an end of season sale to clear space for new styles. After creating a baseline forecast, you can use a what-if analysis to investigate how different sales tactics might affect your goals.</p> <p>You could create a scenario where everything is given a 25% markdown, and another where everything is given a fixed dollar markdown. You could create a scenario where the sale lasts for one week and another where the sale lasts for one month. With a what-if analysis, you can compare many different scenarios against each other.</p> <p>Note that a what-if analysis is meant to display what the forecasting model has learned and how it will behave in the scenarios that you are evaluating. Do not blindly use the results of the what-if analysis to make business decisions. For instance, forecasts might not be accurate for novel scenarios where there is no reference available to determine whether a forecast is good.</p> <p>The <a>TimeSeriesSelector</a> object defines the items that you want in the what-if analysis.</p>

        Args:
            what_if_analysis_name: <p>The name of the what-if analysis. Each name must be unique.</p>
            forecast_arn: <p>The Amazon Resource Name (ARN) of the baseline forecast.</p>
            time_series_selector: <p>Defines the set of time series that are used in the what-if analysis with a <code>TimeSeriesIdentifiers</code> object. What-if analyses are performed only for the time series in this object.</p> <p>The <code>TimeSeriesIdentifiers</code> object needs the following information:</p> <ul> <li> <p> <code>DataSource</code> </p> </li> <li> <p> <code>Format</code> </p> </li> <li> <p> <code>Schema</code> </p> </li> </ul>
            tags: <p>A list of <a href="https://docs.aws.amazon.com/forecast/latest/dg/tagging-forecast-resources.html">tags</a> to apply to the what if forecast.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of resources per account has been exceeded.</p>
            capo_forecast.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>There is already a resource with this name. Try again with a different name.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.create_what_if_analysis_request.CreateWhatIfAnalysisRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.create_what_if_analysis_response.CreateWhatIfAnalysisResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.create_what_if_analysis

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.create_what_if_analysis.async_create_what_if_analysis(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.create_what_if_analysis_request.CreateWhatIfAnalysisRequest = {
            "what_if_analysis_name": what_if_analysis_name,
            "forecast_arn": forecast_arn,
        }
        if time_series_selector is not None:
            input_["time_series_selector"] = time_series_selector
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_what_if_forecast(
        self,
        what_if_forecast_name: "capo_forecast.types.name.Name",
        what_if_analysis_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        time_series_transformations: Optional[
            "capo_forecast.types.time_series_transformations.TimeSeriesTransformations"
        ] = None,
        time_series_replacements_data_source: Optional[
            "capo_forecast.types.time_series_replacements_data_source.TimeSeriesReplacementsDataSource"
        ] = None,
        tags: Optional["capo_forecast.types.tags.Tags"] = None,
    ) -> "capo_forecast.types.create_what_if_forecast_response.CreateWhatIfForecastResponse":
        """<p>A what-if forecast is a forecast that is created from a modified version of the baseline forecast. Each what-if forecast incorporates either a replacement dataset or a set of transformations to the original dataset. </p>

        Args:
            what_if_forecast_name: <p>The name of the what-if forecast. Names must be unique within each what-if analysis.</p>
            what_if_analysis_arn: <p>The Amazon Resource Name (ARN) of the what-if analysis.</p>
            time_series_transformations: <p>The transformations that are applied to the baseline time series. Each transformation contains an action and a set of conditions. An action is applied only when all conditions are met. If no conditions are provided, the action is applied to all items.</p>
            time_series_replacements_data_source: <p>The replacement time series dataset, which contains the rows that you want to change in the related time series dataset. A replacement time series does not need to contain all rows that are in the baseline related time series. Include only the rows (measure-dimension combinations) that you want to include in the what-if forecast.</p> <p>This dataset is merged with the original time series to create a transformed dataset that is used for the what-if analysis.</p> <p>This dataset should contain the items to modify (such as item_id or workforce_type), any relevant dimensions, the timestamp column, and at least one of the related time series columns. This file should not contain duplicate timestamps for the same time series.</p> <p>Timestamps and item_ids not included in this dataset are not included in the what-if analysis. </p>
            tags: <p>A list of <a href="https://docs.aws.amazon.com/forecast/latest/dg/tagging-forecast-resources.html">tags</a> to apply to the what if forecast.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of resources per account has been exceeded.</p>
            capo_forecast.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>There is already a resource with this name. Try again with a different name.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.create_what_if_forecast_request.CreateWhatIfForecastRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.create_what_if_forecast_response.CreateWhatIfForecastResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.create_what_if_forecast

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.create_what_if_forecast.async_create_what_if_forecast(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.create_what_if_forecast_request.CreateWhatIfForecastRequest = {
            "what_if_forecast_name": what_if_forecast_name,
            "what_if_analysis_arn": what_if_analysis_arn,
        }
        if time_series_transformations is not None:
            input_["time_series_transformations"] = time_series_transformations
        if time_series_replacements_data_source is not None:
            input_["time_series_replacements_data_source"] = (
                time_series_replacements_data_source
            )
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_what_if_forecast_export(
        self,
        what_if_forecast_export_name: "capo_forecast.types.name.Name",
        what_if_forecast_arns: "capo_forecast.types.what_if_forecast_arn_list_for_export.WhatIfForecastArnListForExport",
        destination: "capo_forecast.types.data_destination.DataDestination",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        tags: Optional["capo_forecast.types.tags.Tags"] = None,
        format: Optional["capo_forecast.types.format.Format"] = None,
    ) -> "capo_forecast.types.create_what_if_forecast_export_response.CreateWhatIfForecastExportResponse":
        """<p>Exports a forecast created by the <a>CreateWhatIfForecast</a> operation to your Amazon Simple Storage Service (Amazon S3) bucket. The forecast file name will match the following conventions:</p> <p> <code>≈<ForecastExportJobName>_<ExportTimestamp>_<PartNumber></code> </p> <p>The <ExportTimestamp> component is in Java SimpleDateFormat (yyyy-MM-ddTHH-mm-ssZ).</p> <p>You must specify a <a>DataDestination</a> object that includes an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the Amazon S3 bucket. For more information, see <a>aws-forecast-iam-roles</a>.</p> <p>For more information, see <a>howitworks-forecast</a>.</p> <p>To get a list of all your what-if forecast export jobs, use the <a>ListWhatIfForecastExports</a> operation.</p> <note> <p>The <code>Status</code> of the forecast export job must be <code>ACTIVE</code> before you can access the forecast in your Amazon S3 bucket. To get the status, use the <a>DescribeWhatIfForecastExport</a> operation.</p> </note>

        Args:
            what_if_forecast_export_name: <p>The name of the what-if forecast to export.</p>
            what_if_forecast_arns: <p>The list of what-if forecast Amazon Resource Names (ARNs) to export.</p>
            destination: <p>The location where you want to save the forecast and an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the location. The forecast must be exported to an Amazon S3 bucket.</p> <p>If encryption is used, <code>Destination</code> must include an Key Management Service (KMS) key. The IAM role must allow Amazon Forecast permission to access the key.</p>
            tags: <p>A list of <a href="https://docs.aws.amazon.com/forecast/latest/dg/tagging-forecast-resources.html">tags</a> to apply to the what if forecast.</p>
            format: <p>The format of the exported data, CSV or PARQUET.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of resources per account has been exceeded.</p>
            capo_forecast.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>There is already a resource with this name. Try again with a different name.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.create_what_if_forecast_export_request.CreateWhatIfForecastExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.create_what_if_forecast_export_response.CreateWhatIfForecastExportResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.create_what_if_forecast_export

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.create_what_if_forecast_export.async_create_what_if_forecast_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.create_what_if_forecast_export_request.CreateWhatIfForecastExportRequest = {
            "what_if_forecast_export_name": what_if_forecast_export_name,
            "what_if_forecast_arns": what_if_forecast_arns,
            "destination": destination,
        }
        if tags is not None:
            input_["tags"] = tags
        if format is not None:
            input_["format"] = format

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_dataset(
        self,
        dataset_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> None:
        """<p>Deletes an Amazon Forecast dataset that was created using the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html">CreateDataset</a> operation. You can only delete datasets that have a status of <code>ACTIVE</code> or <code>CREATE_FAILED</code>. To get the status use the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDataset.html">DescribeDataset</a> operation.</p> <note> <p>Forecast does not automatically update any dataset groups that contain the deleted dataset. In order to update the dataset group, use the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_UpdateDatasetGroup.html">UpdateDatasetGroup</a> operation, omitting the deleted dataset's ARN.</p> </note>

        Args:
            dataset_arn: <p>The Amazon Resource Name (ARN) of the dataset to delete.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.delete_dataset_request.DeleteDatasetRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_forecast._operations.amazon_forecast.delete_dataset

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.delete_dataset.async_delete_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.delete_dataset_request.DeleteDatasetRequest = {
            "dataset_arn": dataset_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_dataset_group(
        self,
        dataset_group_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> None:
        """<p>Deletes a dataset group created using the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html">CreateDatasetGroup</a> operation. You can only delete dataset groups that have a status of <code>ACTIVE</code>, <code>CREATE_FAILED</code>, or <code>UPDATE_FAILED</code>. To get the status, use the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetGroup.html">DescribeDatasetGroup</a> operation.</p> <p>This operation deletes only the dataset group, not the datasets in the group.</p>

        Args:
            dataset_group_arn: <p>The Amazon Resource Name (ARN) of the dataset group to delete.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.delete_dataset_group_request.DeleteDatasetGroupRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_forecast._operations.amazon_forecast.delete_dataset_group

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.delete_dataset_group.async_delete_dataset_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.delete_dataset_group_request.DeleteDatasetGroupRequest = {
            "dataset_group_arn": dataset_group_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_dataset_import_job(
        self,
        dataset_import_job_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> None:
        """<p>Deletes a dataset import job created using the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html">CreateDatasetImportJob</a> operation. You can delete only dataset import jobs that have a status of <code>ACTIVE</code> or <code>CREATE_FAILED</code>. To get the status, use the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetImportJob.html">DescribeDatasetImportJob</a> operation.</p>

        Args:
            dataset_import_job_arn: <p>The Amazon Resource Name (ARN) of the dataset import job to delete.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.delete_dataset_import_job_request.DeleteDatasetImportJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_forecast._operations.amazon_forecast.delete_dataset_import_job

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.delete_dataset_import_job.async_delete_dataset_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.delete_dataset_import_job_request.DeleteDatasetImportJobRequest = {
            "dataset_import_job_arn": dataset_import_job_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_explainability(
        self,
        explainability_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> None:
        """<p>Deletes an Explainability resource.</p> <p>You can delete only predictor that have a status of <code>ACTIVE</code> or <code>CREATE_FAILED</code>. To get the status, use the <a>DescribeExplainability</a> operation.</p>

        Args:
            explainability_arn: <p>The Amazon Resource Name (ARN) of the Explainability resource to delete.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.delete_explainability_request.DeleteExplainabilityRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_forecast._operations.amazon_forecast.delete_explainability

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.delete_explainability.async_delete_explainability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.delete_explainability_request.DeleteExplainabilityRequest = {
            "explainability_arn": explainability_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_explainability_export(
        self,
        explainability_export_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> None:
        """<p>Deletes an Explainability export.</p>

        Args:
            explainability_export_arn: <p>The Amazon Resource Name (ARN) of the Explainability export to delete. </p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.delete_explainability_export_request.DeleteExplainabilityExportRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_forecast._operations.amazon_forecast.delete_explainability_export

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.delete_explainability_export.async_delete_explainability_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.delete_explainability_export_request.DeleteExplainabilityExportRequest = {
            "explainability_export_arn": explainability_export_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_forecast(
        self,
        forecast_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> None:
        """<p>Deletes a forecast created using the <a>CreateForecast</a> operation. You can delete only forecasts that have a status of <code>ACTIVE</code> or <code>CREATE_FAILED</code>. To get the status, use the <a>DescribeForecast</a> operation.</p> <p>You can't delete a forecast while it is being exported. After a forecast is deleted, you can no longer query the forecast.</p>

        Args:
            forecast_arn: <p>The Amazon Resource Name (ARN) of the forecast to delete.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.delete_forecast_request.DeleteForecastRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_forecast._operations.amazon_forecast.delete_forecast

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.delete_forecast.async_delete_forecast(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.delete_forecast_request.DeleteForecastRequest = {
            "forecast_arn": forecast_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_forecast_export_job(
        self,
        forecast_export_job_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> None:
        """<p>Deletes a forecast export job created using the <a>CreateForecastExportJob</a> operation. You can delete only export jobs that have a status of <code>ACTIVE</code> or <code>CREATE_FAILED</code>. To get the status, use the <a>DescribeForecastExportJob</a> operation.</p>

        Args:
            forecast_export_job_arn: <p>The Amazon Resource Name (ARN) of the forecast export job to delete.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.delete_forecast_export_job_request.DeleteForecastExportJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_forecast._operations.amazon_forecast.delete_forecast_export_job

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.delete_forecast_export_job.async_delete_forecast_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.delete_forecast_export_job_request.DeleteForecastExportJobRequest = {
            "forecast_export_job_arn": forecast_export_job_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_monitor(
        self,
        monitor_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> None:
        """<p>Deletes a monitor resource. You can only delete a monitor resource with a status of <code>ACTIVE</code>, <code>ACTIVE_STOPPED</code>, <code>CREATE_FAILED</code>, or <code>CREATE_STOPPED</code>.</p>

        Args:
            monitor_arn: <p>The Amazon Resource Name (ARN) of the monitor resource to delete.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.delete_monitor_request.DeleteMonitorRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_forecast._operations.amazon_forecast.delete_monitor

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.delete_monitor.async_delete_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.delete_monitor_request.DeleteMonitorRequest = {
            "monitor_arn": monitor_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_predictor(
        self,
        predictor_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> None:
        """<p>Deletes a predictor created using the <a>DescribePredictor</a> or <a>CreatePredictor</a> operations. You can delete only predictor that have a status of <code>ACTIVE</code> or <code>CREATE_FAILED</code>. To get the status, use the <a>DescribePredictor</a> operation.</p>

        Args:
            predictor_arn: <p>The Amazon Resource Name (ARN) of the predictor to delete.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.delete_predictor_request.DeletePredictorRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_forecast._operations.amazon_forecast.delete_predictor

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.delete_predictor.async_delete_predictor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.delete_predictor_request.DeletePredictorRequest = {
            "predictor_arn": predictor_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_predictor_backtest_export_job(
        self,
        predictor_backtest_export_job_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> None:
        """<p>Deletes a predictor backtest export job.</p>

        Args:
            predictor_backtest_export_job_arn: <p>The Amazon Resource Name (ARN) of the predictor backtest export job to delete.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.delete_predictor_backtest_export_job_request.DeletePredictorBacktestExportJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_forecast._operations.amazon_forecast.delete_predictor_backtest_export_job

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.delete_predictor_backtest_export_job.async_delete_predictor_backtest_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.delete_predictor_backtest_export_job_request.DeletePredictorBacktestExportJobRequest = {
            "predictor_backtest_export_job_arn": predictor_backtest_export_job_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_tree(
        self,
        resource_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> None:
        """<p>Deletes an entire resource tree. This operation will delete the parent resource and its child resources.</p> <p>Child resources are resources that were created from another resource. For example, when a forecast is generated from a predictor, the forecast is the child resource and the predictor is the parent resource.</p> <p>Amazon Forecast resources possess the following parent-child resource hierarchies:</p> <ul> <li> <p> <b>Dataset</b>: dataset import jobs</p> </li> <li> <p> <b>Dataset Group</b>: predictors, predictor backtest export jobs, forecasts, forecast export jobs</p> </li> <li> <p> <b>Predictor</b>: predictor backtest export jobs, forecasts, forecast export jobs</p> </li> <li> <p> <b>Forecast</b>: forecast export jobs</p> </li> </ul> <note> <p> <code>DeleteResourceTree</code> will only delete Amazon Forecast resources, and will not delete datasets or exported files stored in Amazon S3. </p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the parent resource to delete. All child resources of the parent resource will also be deleted.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.delete_resource_tree_request.DeleteResourceTreeRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_forecast._operations.amazon_forecast.delete_resource_tree

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.delete_resource_tree.async_delete_resource_tree(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.delete_resource_tree_request.DeleteResourceTreeRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_what_if_analysis(
        self,
        what_if_analysis_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> None:
        """<p>Deletes a what-if analysis created using the <a>CreateWhatIfAnalysis</a> operation. You can delete only what-if analyses that have a status of <code>ACTIVE</code> or <code>CREATE_FAILED</code>. To get the status, use the <a>DescribeWhatIfAnalysis</a> operation. </p> <p>You can't delete a what-if analysis while any of its forecasts are being exported.</p>

        Args:
            what_if_analysis_arn: <p>The Amazon Resource Name (ARN) of the what-if analysis that you want to delete.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.delete_what_if_analysis_request.DeleteWhatIfAnalysisRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_forecast._operations.amazon_forecast.delete_what_if_analysis

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.delete_what_if_analysis.async_delete_what_if_analysis(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.delete_what_if_analysis_request.DeleteWhatIfAnalysisRequest = {
            "what_if_analysis_arn": what_if_analysis_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_what_if_forecast(
        self,
        what_if_forecast_arn: "capo_forecast.types.long_arn.LongArn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> None:
        """<p>Deletes a what-if forecast created using the <a>CreateWhatIfForecast</a> operation. You can delete only what-if forecasts that have a status of <code>ACTIVE</code> or <code>CREATE_FAILED</code>. To get the status, use the <a>DescribeWhatIfForecast</a> operation. </p> <p>You can't delete a what-if forecast while it is being exported. After a what-if forecast is deleted, you can no longer query the what-if analysis.</p>

        Args:
            what_if_forecast_arn: <p>The Amazon Resource Name (ARN) of the what-if forecast that you want to delete.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.delete_what_if_forecast_request.DeleteWhatIfForecastRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_forecast._operations.amazon_forecast.delete_what_if_forecast

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.delete_what_if_forecast.async_delete_what_if_forecast(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.delete_what_if_forecast_request.DeleteWhatIfForecastRequest = {
            "what_if_forecast_arn": what_if_forecast_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_what_if_forecast_export(
        self,
        what_if_forecast_export_arn: "capo_forecast.types.long_arn.LongArn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> None:
        """<p>Deletes a what-if forecast export created using the <a>CreateWhatIfForecastExport</a> operation. You can delete only what-if forecast exports that have a status of <code>ACTIVE</code> or <code>CREATE_FAILED</code>. To get the status, use the <a>DescribeWhatIfForecastExport</a> operation. </p>

        Args:
            what_if_forecast_export_arn: <p>The Amazon Resource Name (ARN) of the what-if forecast export that you want to delete.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.delete_what_if_forecast_export_request.DeleteWhatIfForecastExportRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_forecast._operations.amazon_forecast.delete_what_if_forecast_export

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.delete_what_if_forecast_export.async_delete_what_if_forecast_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.delete_what_if_forecast_export_request.DeleteWhatIfForecastExportRequest = {
            "what_if_forecast_export_arn": what_if_forecast_export_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_auto_predictor(
        self,
        predictor_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.describe_auto_predictor_response.DescribeAutoPredictorResponse":
        """<p>Describes a predictor created using the CreateAutoPredictor operation.</p>

        Args:
            predictor_arn: <p>The Amazon Resource Name (ARN) of the predictor.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.describe_auto_predictor_request.DescribeAutoPredictorRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.describe_auto_predictor_response.DescribeAutoPredictorResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.describe_auto_predictor

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.describe_auto_predictor.async_describe_auto_predictor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.describe_auto_predictor_request.DescribeAutoPredictorRequest = {
            "predictor_arn": predictor_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_dataset(
        self,
        dataset_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.describe_dataset_response.DescribeDatasetResponse":
        """<p>Describes an Amazon Forecast dataset created using the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html">CreateDataset</a> operation.</p> <p>In addition to listing the parameters specified in the <code>CreateDataset</code> request, this operation includes the following dataset properties:</p> <ul> <li> <p> <code>CreationTime</code> </p> </li> <li> <p> <code>LastModificationTime</code> </p> </li> <li> <p> <code>Status</code> </p> </li> </ul>

        Args:
            dataset_arn: <p>The Amazon Resource Name (ARN) of the dataset.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.describe_dataset_request.DescribeDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.describe_dataset_response.DescribeDatasetResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.describe_dataset

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.describe_dataset.async_describe_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.describe_dataset_request.DescribeDatasetRequest = {
            "dataset_arn": dataset_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_dataset_group(
        self,
        dataset_group_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.describe_dataset_group_response.DescribeDatasetGroupResponse":
        """<p>Describes a dataset group created using the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html">CreateDatasetGroup</a> operation.</p> <p>In addition to listing the parameters provided in the <code>CreateDatasetGroup</code> request, this operation includes the following properties:</p> <ul> <li> <p> <code>DatasetArns</code> - The datasets belonging to the group.</p> </li> <li> <p> <code>CreationTime</code> </p> </li> <li> <p> <code>LastModificationTime</code> </p> </li> <li> <p> <code>Status</code> </p> </li> </ul>

        Args:
            dataset_group_arn: <p>The Amazon Resource Name (ARN) of the dataset group.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.describe_dataset_group_request.DescribeDatasetGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.describe_dataset_group_response.DescribeDatasetGroupResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.describe_dataset_group

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.describe_dataset_group.async_describe_dataset_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.describe_dataset_group_request.DescribeDatasetGroupRequest = {
            "dataset_group_arn": dataset_group_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_dataset_import_job(
        self,
        dataset_import_job_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.describe_dataset_import_job_response.DescribeDatasetImportJobResponse":
        """<p>Describes a dataset import job created using the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html">CreateDatasetImportJob</a> operation.</p> <p>In addition to listing the parameters provided in the <code>CreateDatasetImportJob</code> request, this operation includes the following properties:</p> <ul> <li> <p> <code>CreationTime</code> </p> </li> <li> <p> <code>LastModificationTime</code> </p> </li> <li> <p> <code>DataSize</code> </p> </li> <li> <p> <code>FieldStatistics</code> </p> </li> <li> <p> <code>Status</code> </p> </li> <li> <p> <code>Message</code> - If an error occurred, information about the error.</p> </li> </ul>

        Args:
            dataset_import_job_arn: <p>The Amazon Resource Name (ARN) of the dataset import job.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.describe_dataset_import_job_request.DescribeDatasetImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.describe_dataset_import_job_response.DescribeDatasetImportJobResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.describe_dataset_import_job

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.describe_dataset_import_job.async_describe_dataset_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.describe_dataset_import_job_request.DescribeDatasetImportJobRequest = {
            "dataset_import_job_arn": dataset_import_job_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_explainability(
        self,
        explainability_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.describe_explainability_response.DescribeExplainabilityResponse":
        """<p>Describes an Explainability resource created using the <a>CreateExplainability</a> operation.</p>

        Args:
            explainability_arn: <p>The Amazon Resource Name (ARN) of the Explaianability to describe.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.describe_explainability_request.DescribeExplainabilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.describe_explainability_response.DescribeExplainabilityResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.describe_explainability

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.describe_explainability.async_describe_explainability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.describe_explainability_request.DescribeExplainabilityRequest = {
            "explainability_arn": explainability_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_explainability_export(
        self,
        explainability_export_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.describe_explainability_export_response.DescribeExplainabilityExportResponse":
        """<p>Describes an Explainability export created using the <a>CreateExplainabilityExport</a> operation.</p>

        Args:
            explainability_export_arn: <p>The Amazon Resource Name (ARN) of the Explainability export.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.describe_explainability_export_request.DescribeExplainabilityExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.describe_explainability_export_response.DescribeExplainabilityExportResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.describe_explainability_export

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.describe_explainability_export.async_describe_explainability_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.describe_explainability_export_request.DescribeExplainabilityExportRequest = {
            "explainability_export_arn": explainability_export_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_forecast(
        self,
        forecast_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.describe_forecast_response.DescribeForecastResponse":
        """<p>Describes a forecast created using the <a>CreateForecast</a> operation.</p> <p>In addition to listing the properties provided in the <code>CreateForecast</code> request, this operation lists the following properties:</p> <ul> <li> <p> <code>DatasetGroupArn</code> - The dataset group that provided the training data.</p> </li> <li> <p> <code>CreationTime</code> </p> </li> <li> <p> <code>LastModificationTime</code> </p> </li> <li> <p> <code>Status</code> </p> </li> <li> <p> <code>Message</code> - If an error occurred, information about the error.</p> </li> </ul>

        Args:
            forecast_arn: <p>The Amazon Resource Name (ARN) of the forecast.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.describe_forecast_request.DescribeForecastRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.describe_forecast_response.DescribeForecastResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.describe_forecast

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.describe_forecast.async_describe_forecast(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.describe_forecast_request.DescribeForecastRequest = {
            "forecast_arn": forecast_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_forecast_export_job(
        self,
        forecast_export_job_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.describe_forecast_export_job_response.DescribeForecastExportJobResponse":
        """<p>Describes a forecast export job created using the <a>CreateForecastExportJob</a> operation.</p> <p>In addition to listing the properties provided by the user in the <code>CreateForecastExportJob</code> request, this operation lists the following properties:</p> <ul> <li> <p> <code>CreationTime</code> </p> </li> <li> <p> <code>LastModificationTime</code> </p> </li> <li> <p> <code>Status</code> </p> </li> <li> <p> <code>Message</code> - If an error occurred, information about the error.</p> </li> </ul>

        Args:
            forecast_export_job_arn: <p>The Amazon Resource Name (ARN) of the forecast export job.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.describe_forecast_export_job_request.DescribeForecastExportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.describe_forecast_export_job_response.DescribeForecastExportJobResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.describe_forecast_export_job

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.describe_forecast_export_job.async_describe_forecast_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.describe_forecast_export_job_request.DescribeForecastExportJobRequest = {
            "forecast_export_job_arn": forecast_export_job_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_monitor(
        self,
        monitor_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.describe_monitor_response.DescribeMonitorResponse":
        """<p>Describes a monitor resource. In addition to listing the properties provided in the <a>CreateMonitor</a> request, this operation lists the following properties:</p> <ul> <li> <p> <code>Baseline</code> </p> </li> <li> <p> <code>CreationTime</code> </p> </li> <li> <p> <code>LastEvaluationTime</code> </p> </li> <li> <p> <code>LastEvaluationState</code> </p> </li> <li> <p> <code>LastModificationTime</code> </p> </li> <li> <p> <code>Message</code> </p> </li> <li> <p> <code>Status</code> </p> </li> </ul>

        Args:
            monitor_arn: <p>The Amazon Resource Name (ARN) of the monitor resource to describe.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.describe_monitor_request.DescribeMonitorRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.describe_monitor_response.DescribeMonitorResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.describe_monitor

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.describe_monitor.async_describe_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.describe_monitor_request.DescribeMonitorRequest = {
            "monitor_arn": monitor_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_predictor(
        self,
        predictor_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.describe_predictor_response.DescribePredictorResponse":
        """<note> <p> This operation is only valid for legacy predictors created with CreatePredictor. If you are not using a legacy predictor, use <a>DescribeAutoPredictor</a>.</p> </note> <p>Describes a predictor created using the <a>CreatePredictor</a> operation.</p> <p>In addition to listing the properties provided in the <code>CreatePredictor</code> request, this operation lists the following properties:</p> <ul> <li> <p> <code>DatasetImportJobArns</code> - The dataset import jobs used to import training data.</p> </li> <li> <p> <code>AutoMLAlgorithmArns</code> - If AutoML is performed, the algorithms that were evaluated.</p> </li> <li> <p> <code>CreationTime</code> </p> </li> <li> <p> <code>LastModificationTime</code> </p> </li> <li> <p> <code>Status</code> </p> </li> <li> <p> <code>Message</code> - If an error occurred, information about the error.</p> </li> </ul>

        Args:
            predictor_arn: <p>The Amazon Resource Name (ARN) of the predictor that you want information about.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.describe_predictor_request.DescribePredictorRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.describe_predictor_response.DescribePredictorResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.describe_predictor

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.describe_predictor.async_describe_predictor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.describe_predictor_request.DescribePredictorRequest = {
            "predictor_arn": predictor_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_predictor_backtest_export_job(
        self,
        predictor_backtest_export_job_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.describe_predictor_backtest_export_job_response.DescribePredictorBacktestExportJobResponse":
        """<p>Describes a predictor backtest export job created using the <a>CreatePredictorBacktestExportJob</a> operation.</p> <p>In addition to listing the properties provided by the user in the <code>CreatePredictorBacktestExportJob</code> request, this operation lists the following properties:</p> <ul> <li> <p> <code>CreationTime</code> </p> </li> <li> <p> <code>LastModificationTime</code> </p> </li> <li> <p> <code>Status</code> </p> </li> <li> <p> <code>Message</code> (if an error occurred)</p> </li> </ul>

        Args:
            predictor_backtest_export_job_arn: <p>The Amazon Resource Name (ARN) of the predictor backtest export job.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.describe_predictor_backtest_export_job_request.DescribePredictorBacktestExportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.describe_predictor_backtest_export_job_response.DescribePredictorBacktestExportJobResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.describe_predictor_backtest_export_job

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.describe_predictor_backtest_export_job.async_describe_predictor_backtest_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.describe_predictor_backtest_export_job_request.DescribePredictorBacktestExportJobRequest = {
            "predictor_backtest_export_job_arn": predictor_backtest_export_job_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_what_if_analysis(
        self,
        what_if_analysis_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.describe_what_if_analysis_response.DescribeWhatIfAnalysisResponse":
        """<p>Describes the what-if analysis created using the <a>CreateWhatIfAnalysis</a> operation.</p> <p>In addition to listing the properties provided in the <code>CreateWhatIfAnalysis</code> request, this operation lists the following properties:</p> <ul> <li> <p> <code>CreationTime</code> </p> </li> <li> <p> <code>LastModificationTime</code> </p> </li> <li> <p> <code>Message</code> - If an error occurred, information about the error.</p> </li> <li> <p> <code>Status</code> </p> </li> </ul>

        Args:
            what_if_analysis_arn: <p>The Amazon Resource Name (ARN) of the what-if analysis that you are interested in.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.describe_what_if_analysis_request.DescribeWhatIfAnalysisRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.describe_what_if_analysis_response.DescribeWhatIfAnalysisResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.describe_what_if_analysis

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.describe_what_if_analysis.async_describe_what_if_analysis(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.describe_what_if_analysis_request.DescribeWhatIfAnalysisRequest = {
            "what_if_analysis_arn": what_if_analysis_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_what_if_forecast(
        self,
        what_if_forecast_arn: "capo_forecast.types.long_arn.LongArn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.describe_what_if_forecast_response.DescribeWhatIfForecastResponse":
        """<p>Describes the what-if forecast created using the <a>CreateWhatIfForecast</a> operation.</p> <p>In addition to listing the properties provided in the <code>CreateWhatIfForecast</code> request, this operation lists the following properties:</p> <ul> <li> <p> <code>CreationTime</code> </p> </li> <li> <p> <code>LastModificationTime</code> </p> </li> <li> <p> <code>Message</code> - If an error occurred, information about the error.</p> </li> <li> <p> <code>Status</code> </p> </li> </ul>

        Args:
            what_if_forecast_arn: <p>The Amazon Resource Name (ARN) of the what-if forecast that you are interested in.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.describe_what_if_forecast_request.DescribeWhatIfForecastRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.describe_what_if_forecast_response.DescribeWhatIfForecastResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.describe_what_if_forecast

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.describe_what_if_forecast.async_describe_what_if_forecast(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.describe_what_if_forecast_request.DescribeWhatIfForecastRequest = {
            "what_if_forecast_arn": what_if_forecast_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_what_if_forecast_export(
        self,
        what_if_forecast_export_arn: "capo_forecast.types.long_arn.LongArn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.describe_what_if_forecast_export_response.DescribeWhatIfForecastExportResponse":
        """<p>Describes the what-if forecast export created using the <a>CreateWhatIfForecastExport</a> operation.</p> <p>In addition to listing the properties provided in the <code>CreateWhatIfForecastExport</code> request, this operation lists the following properties:</p> <ul> <li> <p> <code>CreationTime</code> </p> </li> <li> <p> <code>LastModificationTime</code> </p> </li> <li> <p> <code>Message</code> - If an error occurred, information about the error.</p> </li> <li> <p> <code>Status</code> </p> </li> </ul>

        Args:
            what_if_forecast_export_arn: <p>The Amazon Resource Name (ARN) of the what-if forecast export that you are interested in.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.describe_what_if_forecast_export_request.DescribeWhatIfForecastExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.describe_what_if_forecast_export_response.DescribeWhatIfForecastExportResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.describe_what_if_forecast_export

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.describe_what_if_forecast_export.async_describe_what_if_forecast_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.describe_what_if_forecast_export_request.DescribeWhatIfForecastExportRequest = {
            "what_if_forecast_export_arn": what_if_forecast_export_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_accuracy_metrics(
        self,
        predictor_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.get_accuracy_metrics_response.GetAccuracyMetricsResponse":
        """<p>Provides metrics on the accuracy of the models that were trained by the <a>CreatePredictor</a> operation. Use metrics to see how well the model performed and to decide whether to use the predictor to generate a forecast. For more information, see <a href="https://docs.aws.amazon.com/forecast/latest/dg/metrics.html">Predictor Metrics</a>.</p> <p>This operation generates metrics for each backtest window that was evaluated. The number of backtest windows (<code>NumberOfBacktestWindows</code>) is specified using the <a>EvaluationParameters</a> object, which is optionally included in the <code>CreatePredictor</code> request. If <code>NumberOfBacktestWindows</code> isn't specified, the number defaults to one.</p> <p>The parameters of the <code>filling</code> method determine which items contribute to the metrics. If you want all items to contribute, specify <code>zero</code>. If you want only those items that have complete data in the range being evaluated to contribute, specify <code>nan</code>. For more information, see <a>FeaturizationMethod</a>.</p> <note> <p>Before you can get accuracy metrics, the <code>Status</code> of the predictor must be <code>ACTIVE</code>, signifying that training has completed. To get the status, use the <a>DescribePredictor</a> operation.</p> </note>

        Args:
            predictor_arn: <p>The Amazon Resource Name (ARN) of the predictor to get metrics for.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.get_accuracy_metrics_request.GetAccuracyMetricsRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.get_accuracy_metrics_response.GetAccuracyMetricsResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.get_accuracy_metrics

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.get_accuracy_metrics.async_get_accuracy_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.get_accuracy_metrics_request.GetAccuracyMetricsRequest = {
            "predictor_arn": predictor_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_dataset_groups(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
    ) -> "capo_forecast.types.list_dataset_groups_response.ListDatasetGroupsResponse":
        """<p>Returns a list of dataset groups created using the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html">CreateDatasetGroup</a> operation. For each dataset group, this operation returns a summary of its properties, including its Amazon Resource Name (ARN). You can retrieve the complete set of properties by using the dataset group ARN with the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetGroup.html">DescribeDatasetGroup</a> operation.</p>

        Args:
            next_token: <p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>
            max_results: <p>The number of items to return in the response.</p>

        Raises:
            capo_forecast.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid. Tokens expire after 24 hours.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.list_dataset_groups_request.ListDatasetGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.list_dataset_groups_response.ListDatasetGroupsResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.list_dataset_groups

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.list_dataset_groups.async_list_dataset_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.list_dataset_groups_request.ListDatasetGroupsRequest = {}
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

    async def iter_list_dataset_groups(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_forecast.types.dataset_group_summary.DatasetGroupSummary]":
        _token = next_token
        while True:
            _response = await self.list_dataset_groups(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("dataset_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_dataset_import_jobs(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "capo_forecast.types.list_dataset_import_jobs_response.ListDatasetImportJobsResponse":
        """<p>Returns a list of dataset import jobs created using the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html">CreateDatasetImportJob</a> operation. For each import job, this operation returns a summary of its properties, including its Amazon Resource Name (ARN). You can retrieve the complete set of properties by using the ARN with the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetImportJob.html">DescribeDatasetImportJob</a> operation. You can filter the list by providing an array of <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_Filter.html">Filter</a> objects.</p>

        Args:
            next_token: <p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>
            max_results: <p>The number of items to return in the response.</p>
            filters: <p>An array of filters. For each filter, you provide a condition and a match statement. The condition is either <code>IS</code> or <code>IS_NOT</code>, which specifies whether to include or exclude the datasets that match the statement from the list, respectively. The match statement consists of a key and a value.</p> <p> <b>Filter properties</b> </p> <ul> <li> <p> <code>Condition</code> - The condition to apply. Valid values are <code>IS</code> and <code>IS_NOT</code>. To include the datasets that match the statement, specify <code>IS</code>. To exclude matching datasets, specify <code>IS_NOT</code>.</p> </li> <li> <p> <code>Key</code> - The name of the parameter to filter on. Valid values are <code>DatasetArn</code> and <code>Status</code>.</p> </li> <li> <p> <code>Value</code> - The value to match.</p> </li> </ul> <p>For example, to list all dataset import jobs whose status is ACTIVE, you specify the following filter:</p> <p> <code>"Filters": [ { "Condition": "IS", "Key": "Status", "Value": "ACTIVE" } ]</code> </p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid. Tokens expire after 24 hours.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.list_dataset_import_jobs_request.ListDatasetImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.list_dataset_import_jobs_response.ListDatasetImportJobsResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.list_dataset_import_jobs

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.list_dataset_import_jobs.async_list_dataset_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.list_dataset_import_jobs_request.ListDatasetImportJobsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_dataset_import_jobs(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_forecast.types.dataset_import_job_summary.DatasetImportJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_dataset_import_jobs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(_response, ("dataset_import_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_datasets(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
    ) -> "capo_forecast.types.list_datasets_response.ListDatasetsResponse":
        """<p>Returns a list of datasets created using the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html">CreateDataset</a> operation. For each dataset, a summary of its properties, including its Amazon Resource Name (ARN), is returned. To retrieve the complete set of properties, use the ARN with the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDataset.html">DescribeDataset</a> operation.</p>

        Args:
            next_token: <p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>
            max_results: <p>The number of items to return in the response.</p>

        Raises:
            capo_forecast.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid. Tokens expire after 24 hours.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.list_datasets_request.ListDatasetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.list_datasets_response.ListDatasetsResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.list_datasets

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.list_datasets.async_list_datasets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.list_datasets_request.ListDatasetsRequest = {}
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

    async def iter_list_datasets(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_forecast.types.dataset_summary.DatasetSummary]":
        _token = next_token
        while True:
            _response = await self.list_datasets(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("datasets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_explainabilities(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "capo_forecast.types.list_explainabilities_response.ListExplainabilitiesResponse":
        """<p>Returns a list of Explainability resources created using the <a>CreateExplainability</a> operation. This operation returns a summary for each Explainability. You can filter the list using an array of <a>Filter</a> objects.</p> <p>To retrieve the complete set of properties for a particular Explainability resource, use the ARN with the <a>DescribeExplainability</a> operation.</p>

        Args:
            next_token: <p>If the result of the previous request was truncated, the response includes a NextToken. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>
            max_results: <p>The number of items returned in the response.</p>
            filters: <p>An array of filters. For each filter, provide a condition and a match statement. The condition is either <code>IS</code> or <code>IS_NOT</code>, which specifies whether to include or exclude the resources that match the statement from the list. The match statement consists of a key and a value.</p> <p> <b>Filter properties</b> </p> <ul> <li> <p> <code>Condition</code> - The condition to apply. Valid values are <code>IS</code> and <code>IS_NOT</code>.</p> </li> <li> <p> <code>Key</code> - The name of the parameter to filter on. Valid values are <code>ResourceArn</code> and <code>Status</code>.</p> </li> <li> <p> <code>Value</code> - The value to match.</p> </li> </ul>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid. Tokens expire after 24 hours.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.list_explainabilities_request.ListExplainabilitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.list_explainabilities_response.ListExplainabilitiesResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.list_explainabilities

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.list_explainabilities.async_list_explainabilities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.list_explainabilities_request.ListExplainabilitiesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_explainabilities(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_forecast.types.explainability_summary.ExplainabilitySummary]":
        _token = next_token
        while True:
            _response = await self.list_explainabilities(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(_response, ("explainabilities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_explainability_exports(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "capo_forecast.types.list_explainability_exports_response.ListExplainabilityExportsResponse":
        """<p>Returns a list of Explainability exports created using the <a>CreateExplainabilityExport</a> operation. This operation returns a summary for each Explainability export. You can filter the list using an array of <a>Filter</a> objects.</p> <p>To retrieve the complete set of properties for a particular Explainability export, use the ARN with the <a>DescribeExplainability</a> operation.</p>

        Args:
            next_token: <p>If the result of the previous request was truncated, the response includes a NextToken. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>
            max_results: <p>The number of items to return in the response.</p>
            filters: <p>An array of filters. For each filter, provide a condition and a match statement. The condition is either <code>IS</code> or <code>IS_NOT</code>, which specifies whether to include or exclude resources that match the statement from the list. The match statement consists of a key and a value.</p> <p> <b>Filter properties</b> </p> <ul> <li> <p> <code>Condition</code> - The condition to apply. Valid values are <code>IS</code> and <code>IS_NOT</code>.</p> </li> <li> <p> <code>Key</code> - The name of the parameter to filter on. Valid values are <code>ResourceArn</code> and <code>Status</code>.</p> </li> <li> <p> <code>Value</code> - The value to match.</p> </li> </ul>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid. Tokens expire after 24 hours.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.list_explainability_exports_request.ListExplainabilityExportsRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.list_explainability_exports_response.ListExplainabilityExportsResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.list_explainability_exports

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.list_explainability_exports.async_list_explainability_exports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.list_explainability_exports_request.ListExplainabilityExportsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_explainability_exports(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_forecast.types.explainability_export_summary.ExplainabilityExportSummary]":
        _token = next_token
        while True:
            _response = await self.list_explainability_exports(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(_response, ("explainability_exports",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_forecast_export_jobs(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "capo_forecast.types.list_forecast_export_jobs_response.ListForecastExportJobsResponse":
        """<p>Returns a list of forecast export jobs created using the <a>CreateForecastExportJob</a> operation. For each forecast export job, this operation returns a summary of its properties, including its Amazon Resource Name (ARN). To retrieve the complete set of properties, use the ARN with the <a>DescribeForecastExportJob</a> operation. You can filter the list using an array of <a>Filter</a> objects.</p>

        Args:
            next_token: <p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>
            max_results: <p>The number of items to return in the response.</p>
            filters: <p>An array of filters. For each filter, you provide a condition and a match statement. The condition is either <code>IS</code> or <code>IS_NOT</code>, which specifies whether to include or exclude the forecast export jobs that match the statement from the list, respectively. The match statement consists of a key and a value.</p> <p> <b>Filter properties</b> </p> <ul> <li> <p> <code>Condition</code> - The condition to apply. Valid values are <code>IS</code> and <code>IS_NOT</code>. To include the forecast export jobs that match the statement, specify <code>IS</code>. To exclude matching forecast export jobs, specify <code>IS_NOT</code>.</p> </li> <li> <p> <code>Key</code> - The name of the parameter to filter on. Valid values are <code>ForecastArn</code> and <code>Status</code>.</p> </li> <li> <p> <code>Value</code> - The value to match.</p> </li> </ul> <p>For example, to list all jobs that export a forecast named <i>electricityforecast</i>, specify the following filter:</p> <p> <code>"Filters": [ { "Condition": "IS", "Key": "ForecastArn", "Value": "arn:aws:forecast:us-west-2:<acct-id>:forecast/electricityforecast" } ]</code> </p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid. Tokens expire after 24 hours.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.list_forecast_export_jobs_request.ListForecastExportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.list_forecast_export_jobs_response.ListForecastExportJobsResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.list_forecast_export_jobs

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.list_forecast_export_jobs.async_list_forecast_export_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.list_forecast_export_jobs_request.ListForecastExportJobsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_forecast_export_jobs(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_forecast.types.forecast_export_job_summary.ForecastExportJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_forecast_export_jobs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(_response, ("forecast_export_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_forecasts(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "capo_forecast.types.list_forecasts_response.ListForecastsResponse":
        """<p>Returns a list of forecasts created using the <a>CreateForecast</a> operation. For each forecast, this operation returns a summary of its properties, including its Amazon Resource Name (ARN). To retrieve the complete set of properties, specify the ARN with the <a>DescribeForecast</a> operation. You can filter the list using an array of <a>Filter</a> objects.</p>

        Args:
            next_token: <p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>
            max_results: <p>The number of items to return in the response.</p>
            filters: <p>An array of filters. For each filter, you provide a condition and a match statement. The condition is either <code>IS</code> or <code>IS_NOT</code>, which specifies whether to include or exclude the forecasts that match the statement from the list, respectively. The match statement consists of a key and a value.</p> <p> <b>Filter properties</b> </p> <ul> <li> <p> <code>Condition</code> - The condition to apply. Valid values are <code>IS</code> and <code>IS_NOT</code>. To include the forecasts that match the statement, specify <code>IS</code>. To exclude matching forecasts, specify <code>IS_NOT</code>.</p> </li> <li> <p> <code>Key</code> - The name of the parameter to filter on. Valid values are <code>DatasetGroupArn</code>, <code>PredictorArn</code>, and <code>Status</code>.</p> </li> <li> <p> <code>Value</code> - The value to match.</p> </li> </ul> <p>For example, to list all forecasts whose status is not ACTIVE, you would specify:</p> <p> <code>"Filters": [ { "Condition": "IS_NOT", "Key": "Status", "Value": "ACTIVE" } ]</code> </p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid. Tokens expire after 24 hours.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.list_forecasts_request.ListForecastsRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.list_forecasts_response.ListForecastsResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.list_forecasts

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.list_forecasts.async_list_forecasts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.list_forecasts_request.ListForecastsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_forecasts(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_forecast.types.forecast_summary.ForecastSummary]":
        _token = next_token
        while True:
            _response = await self.list_forecasts(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(_response, ("forecasts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_monitor_evaluations(
        self,
        monitor_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "capo_forecast.types.list_monitor_evaluations_response.ListMonitorEvaluationsResponse":
        """<p>Returns a list of the monitoring evaluation results and predictor events collected by the monitor resource during different windows of time.</p> <p>For information about monitoring see <a>predictor-monitoring</a>. For more information about retrieving monitoring results see <a href="https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring-results.html">Viewing Monitoring Results</a>.</p>

        Args:
            next_token: <p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>
            max_results: <p>The maximum number of monitoring results to return.</p>
            monitor_arn: <p>The Amazon Resource Name (ARN) of the monitor resource to get results from.</p>
            filters: <p>An array of filters. For each filter, provide a condition and a match statement. The condition is either <code>IS</code> or <code>IS_NOT</code>, which specifies whether to include or exclude the resources that match the statement from the list. The match statement consists of a key and a value.</p> <p> <b>Filter properties</b> </p> <ul> <li> <p> <code>Condition</code> - The condition to apply. Valid values are <code>IS</code> and <code>IS_NOT</code>.</p> </li> <li> <p> <code>Key</code> - The name of the parameter to filter on. The only valid value is <code>EvaluationState</code>.</p> </li> <li> <p> <code>Value</code> - The value to match. Valid values are only <code>SUCCESS</code> or <code>FAILURE</code>.</p> </li> </ul> <p>For example, to list only successful monitor evaluations, you would specify:</p> <p> <code>"Filters": [ { "Condition": "IS", "Key": "EvaluationState", "Value": "SUCCESS" } ]</code> </p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid. Tokens expire after 24 hours.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.list_monitor_evaluations_request.ListMonitorEvaluationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.list_monitor_evaluations_response.ListMonitorEvaluationsResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.list_monitor_evaluations

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.list_monitor_evaluations.async_list_monitor_evaluations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.list_monitor_evaluations_request.ListMonitorEvaluationsRequest = {
            "monitor_arn": monitor_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_monitor_evaluations(
        self,
        monitor_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_forecast.types.predictor_monitor_evaluation.PredictorMonitorEvaluation]":
        _token = next_token
        while True:
            _response = await self.list_monitor_evaluations(
                monitor_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(_response, ("predictor_monitor_evaluations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_monitors(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "capo_forecast.types.list_monitors_response.ListMonitorsResponse":
        """<p>Returns a list of monitors created with the <a>CreateMonitor</a> operation and <a>CreateAutoPredictor</a> operation. For each monitor resource, this operation returns of a summary of its properties, including its Amazon Resource Name (ARN). You can retrieve a complete set of properties of a monitor resource by specify the monitor's ARN in the <a>DescribeMonitor</a> operation.</p>

        Args:
            next_token: <p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>
            max_results: <p>The maximum number of monitors to include in the response.</p>
            filters: <p>An array of filters. For each filter, provide a condition and a match statement. The condition is either <code>IS</code> or <code>IS_NOT</code>, which specifies whether to include or exclude the resources that match the statement from the list. The match statement consists of a key and a value.</p> <p> <b>Filter properties</b> </p> <ul> <li> <p> <code>Condition</code> - The condition to apply. Valid values are <code>IS</code> and <code>IS_NOT</code>.</p> </li> <li> <p> <code>Key</code> - The name of the parameter to filter on. The only valid value is <code>Status</code>.</p> </li> <li> <p> <code>Value</code> - The value to match.</p> </li> </ul> <p>For example, to list all monitors who's status is ACTIVE, you would specify:</p> <p> <code>"Filters": [ { "Condition": "IS", "Key": "Status", "Value": "ACTIVE" } ]</code> </p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid. Tokens expire after 24 hours.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.list_monitors_request.ListMonitorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.list_monitors_response.ListMonitorsResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.list_monitors

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.list_monitors.async_list_monitors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.list_monitors_request.ListMonitorsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_monitors(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_forecast.types.monitor_summary.MonitorSummary]":
        _token = next_token
        while True:
            _response = await self.list_monitors(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(_response, ("monitors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_predictor_backtest_export_jobs(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "capo_forecast.types.list_predictor_backtest_export_jobs_response.ListPredictorBacktestExportJobsResponse":
        """<p>Returns a list of predictor backtest export jobs created using the <a>CreatePredictorBacktestExportJob</a> operation. This operation returns a summary for each backtest export job. You can filter the list using an array of <a>Filter</a> objects.</p> <p>To retrieve the complete set of properties for a particular backtest export job, use the ARN with the <a>DescribePredictorBacktestExportJob</a> operation.</p>

        Args:
            next_token: <p>If the result of the previous request was truncated, the response includes a NextToken. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>
            max_results: <p>The number of items to return in the response.</p>
            filters: <p>An array of filters. For each filter, provide a condition and a match statement. The condition is either <code>IS</code> or <code>IS_NOT</code>, which specifies whether to include or exclude the predictor backtest export jobs that match the statement from the list. The match statement consists of a key and a value.</p> <p> <b>Filter properties</b> </p> <ul> <li> <p> <code>Condition</code> - The condition to apply. Valid values are <code>IS</code> and <code>IS_NOT</code>. To include the predictor backtest export jobs that match the statement, specify <code>IS</code>. To exclude matching predictor backtest export jobs, specify <code>IS_NOT</code>.</p> </li> <li> <p> <code>Key</code> - The name of the parameter to filter on. Valid values are <code>PredictorArn</code> and <code>Status</code>.</p> </li> <li> <p> <code>Value</code> - The value to match.</p> </li> </ul>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid. Tokens expire after 24 hours.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.list_predictor_backtest_export_jobs_request.ListPredictorBacktestExportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.list_predictor_backtest_export_jobs_response.ListPredictorBacktestExportJobsResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.list_predictor_backtest_export_jobs

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.list_predictor_backtest_export_jobs.async_list_predictor_backtest_export_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.list_predictor_backtest_export_jobs_request.ListPredictorBacktestExportJobsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_predictor_backtest_export_jobs(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_forecast.types.predictor_backtest_export_job_summary.PredictorBacktestExportJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_predictor_backtest_export_jobs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(_response, ("predictor_backtest_export_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_predictors(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "capo_forecast.types.list_predictors_response.ListPredictorsResponse":
        """<p>Returns a list of predictors created using the <a>CreateAutoPredictor</a> or <a>CreatePredictor</a> operations. For each predictor, this operation returns a summary of its properties, including its Amazon Resource Name (ARN). </p> <p>You can retrieve the complete set of properties by using the ARN with the <a>DescribeAutoPredictor</a> and <a>DescribePredictor</a> operations. You can filter the list using an array of <a>Filter</a> objects.</p>

        Args:
            next_token: <p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>
            max_results: <p>The number of items to return in the response.</p>
            filters: <p>An array of filters. For each filter, you provide a condition and a match statement. The condition is either <code>IS</code> or <code>IS_NOT</code>, which specifies whether to include or exclude the predictors that match the statement from the list, respectively. The match statement consists of a key and a value.</p> <p> <b>Filter properties</b> </p> <ul> <li> <p> <code>Condition</code> - The condition to apply. Valid values are <code>IS</code> and <code>IS_NOT</code>. To include the predictors that match the statement, specify <code>IS</code>. To exclude matching predictors, specify <code>IS_NOT</code>.</p> </li> <li> <p> <code>Key</code> - The name of the parameter to filter on. Valid values are <code>DatasetGroupArn</code> and <code>Status</code>.</p> </li> <li> <p> <code>Value</code> - The value to match.</p> </li> </ul> <p>For example, to list all predictors whose status is ACTIVE, you would specify:</p> <p> <code>"Filters": [ { "Condition": "IS", "Key": "Status", "Value": "ACTIVE" } ]</code> </p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid. Tokens expire after 24 hours.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.list_predictors_request.ListPredictorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.list_predictors_response.ListPredictorsResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.list_predictors

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.list_predictors.async_list_predictors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.list_predictors_request.ListPredictorsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_predictors(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_forecast.types.predictor_summary.PredictorSummary]":
        _token = next_token
        while True:
            _response = await self.list_predictors(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(_response, ("predictors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for an Amazon Forecast resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. </p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_what_if_analyses(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> (
        "capo_forecast.types.list_what_if_analyses_response.ListWhatIfAnalysesResponse"
    ):
        """<p>Returns a list of what-if analyses created using the <a>CreateWhatIfAnalysis</a> operation. For each what-if analysis, this operation returns a summary of its properties, including its Amazon Resource Name (ARN). You can retrieve the complete set of properties by using the what-if analysis ARN with the <a>DescribeWhatIfAnalysis</a> operation.</p>

        Args:
            next_token: <p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>
            max_results: <p>The number of items to return in the response.</p>
            filters: <p>An array of filters. For each filter, you provide a condition and a match statement. The condition is either <code>IS</code> or <code>IS_NOT</code>, which specifies whether to include or exclude the what-if analysis jobs that match the statement from the list, respectively. The match statement consists of a key and a value.</p> <p> <b>Filter properties</b> </p> <ul> <li> <p> <code>Condition</code> - The condition to apply. Valid values are <code>IS</code> and <code>IS_NOT</code>. To include the what-if analysis jobs that match the statement, specify <code>IS</code>. To exclude matching what-if analysis jobs, specify <code>IS_NOT</code>.</p> </li> <li> <p> <code>Key</code> - The name of the parameter to filter on. Valid values are <code>WhatIfAnalysisArn</code> and <code>Status</code>.</p> </li> <li> <p> <code>Value</code> - The value to match.</p> </li> </ul> <p>For example, to list all jobs that export a forecast named <i>electricityWhatIf</i>, specify the following filter:</p> <p> <code>"Filters": [ { "Condition": "IS", "Key": "WhatIfAnalysisArn", "Value": "arn:aws:forecast:us-west-2:<acct-id>:forecast/electricityWhatIf" } ]</code> </p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid. Tokens expire after 24 hours.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.list_what_if_analyses_request.ListWhatIfAnalysesRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.list_what_if_analyses_response.ListWhatIfAnalysesResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.list_what_if_analyses

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.list_what_if_analyses.async_list_what_if_analyses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.list_what_if_analyses_request.ListWhatIfAnalysesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_what_if_analyses(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_forecast.types.what_if_analysis_summary.WhatIfAnalysisSummary]":
        _token = next_token
        while True:
            _response = await self.list_what_if_analyses(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(_response, ("what_if_analyses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_what_if_forecast_exports(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "capo_forecast.types.list_what_if_forecast_exports_response.ListWhatIfForecastExportsResponse":
        """<p>Returns a list of what-if forecast exports created using the <a>CreateWhatIfForecastExport</a> operation. For each what-if forecast export, this operation returns a summary of its properties, including its Amazon Resource Name (ARN). You can retrieve the complete set of properties by using the what-if forecast export ARN with the <a>DescribeWhatIfForecastExport</a> operation.</p>

        Args:
            next_token: <p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>
            max_results: <p>The number of items to return in the response.</p>
            filters: <p>An array of filters. For each filter, you provide a condition and a match statement. The condition is either <code>IS</code> or <code>IS_NOT</code>, which specifies whether to include or exclude the what-if forecast export jobs that match the statement from the list, respectively. The match statement consists of a key and a value.</p> <p> <b>Filter properties</b> </p> <ul> <li> <p> <code>Condition</code> - The condition to apply. Valid values are <code>IS</code> and <code>IS_NOT</code>. To include the forecast export jobs that match the statement, specify <code>IS</code>. To exclude matching forecast export jobs, specify <code>IS_NOT</code>.</p> </li> <li> <p> <code>Key</code> - The name of the parameter to filter on. Valid values are <code>WhatIfForecastExportArn</code> and <code>Status</code>.</p> </li> <li> <p> <code>Value</code> - The value to match.</p> </li> </ul> <p>For example, to list all jobs that export a forecast named <i>electricityWIFExport</i>, specify the following filter:</p> <p> <code>"Filters": [ { "Condition": "IS", "Key": "WhatIfForecastExportArn", "Value": "arn:aws:forecast:us-west-2:<acct-id>:forecast/electricityWIFExport" } ]</code> </p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid. Tokens expire after 24 hours.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.list_what_if_forecast_exports_request.ListWhatIfForecastExportsRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.list_what_if_forecast_exports_response.ListWhatIfForecastExportsResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.list_what_if_forecast_exports

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.list_what_if_forecast_exports.async_list_what_if_forecast_exports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.list_what_if_forecast_exports_request.ListWhatIfForecastExportsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_what_if_forecast_exports(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_forecast.types.what_if_forecast_export_summary.WhatIfForecastExportSummary]":
        _token = next_token
        while True:
            _response = await self.list_what_if_forecast_exports(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(_response, ("what_if_forecast_exports",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_what_if_forecasts(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "capo_forecast.types.list_what_if_forecasts_response.ListWhatIfForecastsResponse":
        """<p>Returns a list of what-if forecasts created using the <a>CreateWhatIfForecast</a> operation. For each what-if forecast, this operation returns a summary of its properties, including its Amazon Resource Name (ARN). You can retrieve the complete set of properties by using the what-if forecast ARN with the <a>DescribeWhatIfForecast</a> operation.</p>

        Args:
            next_token: <p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>
            max_results: <p>The number of items to return in the response.</p>
            filters: <p>An array of filters. For each filter, you provide a condition and a match statement. The condition is either <code>IS</code> or <code>IS_NOT</code>, which specifies whether to include or exclude the what-if forecast export jobs that match the statement from the list, respectively. The match statement consists of a key and a value.</p> <p> <b>Filter properties</b> </p> <ul> <li> <p> <code>Condition</code> - The condition to apply. Valid values are <code>IS</code> and <code>IS_NOT</code>. To include the forecast export jobs that match the statement, specify <code>IS</code>. To exclude matching forecast export jobs, specify <code>IS_NOT</code>.</p> </li> <li> <p> <code>Key</code> - The name of the parameter to filter on. Valid values are <code>WhatIfForecastArn</code> and <code>Status</code>.</p> </li> <li> <p> <code>Value</code> - The value to match.</p> </li> </ul> <p>For example, to list all jobs that export a forecast named <i>electricityWhatIfForecast</i>, specify the following filter:</p> <p> <code>"Filters": [ { "Condition": "IS", "Key": "WhatIfForecastArn", "Value": "arn:aws:forecast:us-west-2:<acct-id>:forecast/electricityWhatIfForecast" } ]</code> </p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token is not valid. Tokens expire after 24 hours.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.list_what_if_forecasts_request.ListWhatIfForecastsRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.list_what_if_forecasts_response.ListWhatIfForecastsResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.list_what_if_forecasts

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.list_what_if_forecasts.async_list_what_if_forecasts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.list_what_if_forecasts_request.ListWhatIfForecastsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_what_if_forecasts(
        self,
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
        next_token: Optional["capo_forecast.types.next_token.NextToken"] = None,
        max_results: Optional["capo_forecast.types.max_results.MaxResults"] = None,
        filters: Optional["capo_forecast.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_forecast.types.what_if_forecast_summary.WhatIfForecastSummary]":
        _token = next_token
        while True:
            _response = await self.list_what_if_forecasts(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(_response, ("what_if_forecasts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def resume_resource(
        self,
        resource_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> None:
        """<p>Resumes a stopped monitor resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the monitor resource to resume.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of resources per account has been exceeded.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.resume_resource_request.ResumeResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_forecast._operations.amazon_forecast.resume_resource

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.resume_resource.async_resume_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.resume_resource_request.ResumeResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_resource(
        self,
        resource_arn: "capo_forecast.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> None:
        """<p>Stops a resource.</p> <p>The resource undergoes the following states: <code>CREATE_STOPPING</code> and <code>CREATE_STOPPED</code>. You cannot resume a resource once it has been stopped.</p> <p>This operation can be applied to the following resources (and their corresponding child resources):</p> <ul> <li> <p>Dataset Import Job</p> </li> <li> <p>Predictor Job</p> </li> <li> <p>Forecast Job</p> </li> <li> <p>Forecast Export Job</p> </li> <li> <p>Predictor Backtest Export Job</p> </li> <li> <p>Explainability Job</p> </li> <li> <p>Explainability Export Job</p> </li> </ul>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource to stop. The supported ARNs are <code>DatasetImportJobArn</code>, <code>PredictorArn</code>, <code>PredictorBacktestExportJobArn</code>, <code>ForecastArn</code>, <code>ForecastExportJobArn</code>, <code>ExplainabilityArn</code>, and <code>ExplainabilityExportArn</code>. </p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of resources per account has been exceeded.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.stop_resource_request.StopResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_forecast._operations.amazon_forecast.stop_resource

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.stop_resource.async_stop_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.stop_resource_request.StopResourceRequest = {
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
        resource_arn: "capo_forecast.types.arn.Arn",
        tags: "capo_forecast.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.tag_resource_response.TagResourceResponse":
        """<p>Associates the specified tags to a resource with the specified <code>resourceArn</code>. If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are also deleted.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. </p>
            tags: <p>The tags to add to the resource. A tag is an array of key-value pairs.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for keys as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit.</p> </li> </ul>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.limit_exceeded_exception.LimitExceededException: <p>The limit on the number of resources per account has been exceeded.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.tag_resource

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_forecast.types.arn.Arn",
        tag_keys: "capo_forecast.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes the specified tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. </p>
            tag_keys: <p>The keys of the tags to be removed.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.untag_resource

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_dataset_group(
        self,
        dataset_group_arn: "capo_forecast.types.arn.Arn",
        dataset_arns: "capo_forecast.types.arn_list.ArnList",
        *,
        config_overrides: Optional[AsyncforecastClientConfig] = None,
    ) -> "capo_forecast.types.update_dataset_group_response.UpdateDatasetGroupResponse":
        """<p>Replaces the datasets in a dataset group with the specified datasets.</p> <note> <p>The <code>Status</code> of the dataset group must be <code>ACTIVE</code> before you can use the dataset group to create a predictor. Use the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetGroup.html">DescribeDatasetGroup</a> operation to get the status.</p> </note>

        Args:
            dataset_group_arn: <p>The ARN of the dataset group.</p>
            dataset_arns: <p>An array of the Amazon Resource Names (ARNs) of the datasets to add to the dataset group.</p>

        Raises:
            capo_forecast.errors.invalid_input_exception.InvalidInputException: <p>We can't process the request because it includes an invalid value or a value that exceeds the valid range.</p>
            capo_forecast.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_forecast.errors.resource_not_found_exception.ResourceNotFoundException: <p>We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.</p>
            capo_forecast.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_forecast.types.update_dataset_group_request.UpdateDatasetGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_forecast.types.update_dataset_group_response.UpdateDatasetGroupResponse"
        ]:
            import capo_forecast._operations.amazon_forecast.update_dataset_group

            (
                output,
                http_response,
            ) = await capo_forecast._operations.amazon_forecast.update_dataset_group.async_update_dataset_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_forecast.types.update_dataset_group_request.UpdateDatasetGroupRequest = {
            "dataset_group_arn": dataset_group_arn,
            "dataset_arns": dataset_arns,
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
