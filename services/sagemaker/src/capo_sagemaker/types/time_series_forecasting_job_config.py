"""Generated from Smithy shape ``com.amazonaws.sagemaker#TimeSeriesForecastingJobConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_job_completion_criteria
    import capo_sagemaker.types.candidate_generation_config
    import capo_sagemaker.types.forecast_frequency
    import capo_sagemaker.types.forecast_horizon
    import capo_sagemaker.types.forecast_quantiles
    import capo_sagemaker.types.holiday_config
    import capo_sagemaker.types.s3_uri
    import capo_sagemaker.types.time_series_config
    import capo_sagemaker.types.time_series_transformations


class TimeSeriesForecastingJobConfig(TypedDict, closed=True):
    feature_specification_s3_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>A URL to the Amazon S3 data source containing additional selected features that complement the target, itemID, timestamp, and grouped columns set in <code>TimeSeriesConfig</code>. When not provided, the AutoML job V2 includes all the columns from the original dataset that are not already declared in <code>TimeSeriesConfig</code>. If provided, the AutoML job V2 only considers these additional columns as a complement to the ones declared in <code>TimeSeriesConfig</code>.</p> <p>You can input <code>FeatureAttributeNames</code> (optional) in JSON format as shown below: </p> <p> <code>{ "FeatureAttributeNames":["col1", "col2", ...] }</code>.</p> <p>You can also specify the data type of the feature (optional) in the format shown below:</p> <p> <code>{ "FeatureDataTypes":{"col1":"numeric", "col2":"categorical" ... } }</code> </p> <p>Autopilot supports the following data types: <code>numeric</code>, <code>categorical</code>, <code>text</code>, and <code>datetime</code>.</p> <note> <p>These column keys must not include any column set in <code>TimeSeriesConfig</code>.</p> </note>"""
    completion_criteria: NotRequired[
        "capo_sagemaker.types.auto_ml_job_completion_criteria.AutoMLJobCompletionCriteria"
    ]
    forecast_frequency: NotRequired[
        "capo_sagemaker.types.forecast_frequency.ForecastFrequency"
    ]
    """<p>The frequency of predictions in a forecast.</p> <p>Valid intervals are an integer followed by Y (Year), M (Month), W (Week), D (Day), H (Hour), and min (Minute). For example, <code>1D</code> indicates every day and <code>15min</code> indicates every 15 minutes. The value of a frequency must not overlap with the next larger frequency. For example, you must use a frequency of <code>1H</code> instead of <code>60min</code>.</p> <p>The valid values for each frequency are the following:</p> <ul> <li> <p>Minute - 1-59</p> </li> <li> <p>Hour - 1-23</p> </li> <li> <p>Day - 1-6</p> </li> <li> <p>Week - 1-4</p> </li> <li> <p>Month - 1-11</p> </li> <li> <p>Year - 1</p> </li> </ul>"""
    forecast_horizon: NotRequired[
        "capo_sagemaker.types.forecast_horizon.ForecastHorizon"
    ]
    """<p>The number of time-steps that the model predicts. The forecast horizon is also called the prediction length. The maximum forecast horizon is the lesser of 500 time-steps or 1/4 of the time-steps in the dataset.</p>"""
    forecast_quantiles: NotRequired[
        "capo_sagemaker.types.forecast_quantiles.ForecastQuantiles"
    ]
    """<p>The quantiles used to train the model for forecasts at a specified quantile. You can specify quantiles from <code>0.01</code> (p1) to <code>0.99</code> (p99), by increments of 0.01 or higher. Up to five forecast quantiles can be specified. When <code>ForecastQuantiles</code> is not provided, the AutoML job uses the quantiles p10, p50, and p90 as default.</p>"""
    transformations: NotRequired[
        "capo_sagemaker.types.time_series_transformations.TimeSeriesTransformations"
    ]
    """<p>The transformations modifying specific attributes of the time-series, such as filling strategies for missing values.</p>"""
    time_series_config: NotRequired[
        "capo_sagemaker.types.time_series_config.TimeSeriesConfig"
    ]
    """<p>The collection of components that defines the time-series.</p>"""
    holiday_config: NotRequired["capo_sagemaker.types.holiday_config.HolidayConfig"]
    """<p>The collection of holiday featurization attributes used to incorporate national holiday information into your forecasting model.</p>"""
    candidate_generation_config: NotRequired[
        "capo_sagemaker.types.candidate_generation_config.CandidateGenerationConfig"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeSeriesForecastingJobConfig) -> dict:
    out: dict = {}
    if "feature_specification_s3_uri" in value:
        out["FeatureSpecificationS3Uri"] = value["feature_specification_s3_uri"]
    if "completion_criteria" in value:
        import capo_sagemaker.types.auto_ml_job_completion_criteria

        out["CompletionCriteria"] = (
            capo_sagemaker.types.auto_ml_job_completion_criteria.serialize_aws_json_1_1(
                value["completion_criteria"]
            )
        )
    if "forecast_frequency" in value:
        out["ForecastFrequency"] = value["forecast_frequency"]
    if "forecast_horizon" in value:
        out["ForecastHorizon"] = value["forecast_horizon"]
    if "forecast_quantiles" in value:
        import capo_sagemaker.types.forecast_quantiles

        out["ForecastQuantiles"] = (
            capo_sagemaker.types.forecast_quantiles.serialize_aws_json_1_1(
                value["forecast_quantiles"]
            )
        )
    if "transformations" in value:
        import capo_sagemaker.types.time_series_transformations

        out["Transformations"] = (
            capo_sagemaker.types.time_series_transformations.serialize_aws_json_1_1(
                value["transformations"]
            )
        )
    if "time_series_config" in value:
        import capo_sagemaker.types.time_series_config

        out["TimeSeriesConfig"] = (
            capo_sagemaker.types.time_series_config.serialize_aws_json_1_1(
                value["time_series_config"]
            )
        )
    if "holiday_config" in value:
        import capo_sagemaker.types.holiday_config

        out["HolidayConfig"] = (
            capo_sagemaker.types.holiday_config.serialize_aws_json_1_1(
                value["holiday_config"]
            )
        )
    if "candidate_generation_config" in value:
        import capo_sagemaker.types.candidate_generation_config

        out["CandidateGenerationConfig"] = (
            capo_sagemaker.types.candidate_generation_config.serialize_aws_json_1_1(
                value["candidate_generation_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeSeriesForecastingJobConfig:
    out: TimeSeriesForecastingJobConfig = {}  # type: ignore[typeddict-item]
    if data.get("FeatureSpecificationS3Uri") is not None:
        out["feature_specification_s3_uri"] = data["FeatureSpecificationS3Uri"]
    if data.get("CompletionCriteria") is not None:
        import capo_sagemaker.types.auto_ml_job_completion_criteria

        out["completion_criteria"] = (
            capo_sagemaker.types.auto_ml_job_completion_criteria.deserialize_aws_json_1_1(
                data["CompletionCriteria"]
            )
        )
    if data.get("ForecastFrequency") is not None:
        out["forecast_frequency"] = data["ForecastFrequency"]
    if data.get("ForecastHorizon") is not None:
        out["forecast_horizon"] = data["ForecastHorizon"]
    if data.get("ForecastQuantiles") is not None:
        import capo_sagemaker.types.forecast_quantiles

        out["forecast_quantiles"] = (
            capo_sagemaker.types.forecast_quantiles.deserialize_aws_json_1_1(
                data["ForecastQuantiles"]
            )
        )
    if data.get("Transformations") is not None:
        import capo_sagemaker.types.time_series_transformations

        out["transformations"] = (
            capo_sagemaker.types.time_series_transformations.deserialize_aws_json_1_1(
                data["Transformations"]
            )
        )
    if data.get("TimeSeriesConfig") is not None:
        import capo_sagemaker.types.time_series_config

        out["time_series_config"] = (
            capo_sagemaker.types.time_series_config.deserialize_aws_json_1_1(
                data["TimeSeriesConfig"]
            )
        )
    if data.get("HolidayConfig") is not None:
        import capo_sagemaker.types.holiday_config

        out["holiday_config"] = (
            capo_sagemaker.types.holiday_config.deserialize_aws_json_1_1(
                data["HolidayConfig"]
            )
        )
    if data.get("CandidateGenerationConfig") is not None:
        import capo_sagemaker.types.candidate_generation_config

        out["candidate_generation_config"] = (
            capo_sagemaker.types.candidate_generation_config.deserialize_aws_json_1_1(
                data["CandidateGenerationConfig"]
            )
        )
    return out
