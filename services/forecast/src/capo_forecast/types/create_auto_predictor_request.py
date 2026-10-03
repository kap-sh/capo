"""Generated from Smithy shape ``com.amazonaws.forecast#CreateAutoPredictorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.boolean
    import capo_forecast.types.data_config
    import capo_forecast.types.encryption_config
    import capo_forecast.types.forecast_dimensions
    import capo_forecast.types.forecast_types
    import capo_forecast.types.frequency
    import capo_forecast.types.integer
    import capo_forecast.types.monitor_config
    import capo_forecast.types.name
    import capo_forecast.types.optimization_metric
    import capo_forecast.types.tags
    import capo_forecast.types.time_alignment_boundary


class CreateAutoPredictorRequest(TypedDict, closed=True):
    predictor_name: "capo_forecast.types.name.Name"
    """<p>A unique name for the predictor</p>"""
    forecast_horizon: NotRequired["capo_forecast.types.integer.Integer"]
    """<p>The number of time-steps that the model predicts. The forecast horizon is also called the prediction length.</p> <p>The maximum forecast horizon is the lesser of 500 time-steps or 1/4 of the TARGET_TIME_SERIES dataset length. If you are retraining an existing AutoPredictor, then the maximum forecast horizon is the lesser of 500 time-steps or 1/3 of the TARGET_TIME_SERIES dataset length.</p> <p>If you are upgrading to an AutoPredictor or retraining an existing AutoPredictor, you cannot update the forecast horizon parameter. You can meet this requirement by providing longer time-series in the dataset.</p>"""
    forecast_types: NotRequired["capo_forecast.types.forecast_types.ForecastTypes"]
    """<p>The forecast types used to train a predictor. You can specify up to five forecast types. Forecast types can be quantiles from 0.01 to 0.99, by increments of 0.01 or higher. You can also specify the mean forecast with <code>mean</code>.</p>"""
    forecast_dimensions: NotRequired[
        "capo_forecast.types.forecast_dimensions.ForecastDimensions"
    ]
    """<p>An array of dimension (field) names that specify how to group the generated forecast.</p> <p>For example, if you are generating forecasts for item sales across all your stores, and your dataset contains a <code>store_id</code> field, you would specify <code>store_id</code> as a dimension to group sales forecasts for each store.</p>"""
    forecast_frequency: NotRequired["capo_forecast.types.frequency.Frequency"]
    """<p>The frequency of predictions in a forecast.</p> <p>Valid intervals are an integer followed by Y (Year), M (Month), W (Week), D (Day), H (Hour), and min (Minute). For example, "1D" indicates every day and "15min" indicates every 15 minutes. You cannot specify a value that would overlap with the next larger frequency. That means, for example, you cannot specify a frequency of 60 minutes, because that is equivalent to 1 hour. The valid values for each frequency are the following:</p> <ul> <li> <p>Minute - 1-59</p> </li> <li> <p>Hour - 1-23</p> </li> <li> <p>Day - 1-6</p> </li> <li> <p>Week - 1-4</p> </li> <li> <p>Month - 1-11</p> </li> <li> <p>Year - 1</p> </li> </ul> <p>Thus, if you want every other week forecasts, specify "2W". Or, if you want quarterly forecasts, you specify "3M".</p> <p>The frequency must be greater than or equal to the TARGET_TIME_SERIES dataset frequency.</p> <p>When a RELATED_TIME_SERIES dataset is provided, the frequency must be equal to the RELATED_TIME_SERIES dataset frequency.</p>"""
    data_config: NotRequired["capo_forecast.types.data_config.DataConfig"]
    """<p>The data configuration for your dataset group and any additional datasets.</p>"""
    encryption_config: NotRequired[
        "capo_forecast.types.encryption_config.EncryptionConfig"
    ]
    reference_predictor_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The ARN of the predictor to retrain or upgrade. This parameter is only used when retraining or upgrading a predictor. When creating a new predictor, do not specify a value for this parameter.</p> <p>When upgrading or retraining a predictor, only specify values for the <code>ReferencePredictorArn</code> and <code>PredictorName</code>. The value for <code>PredictorName</code> must be a unique predictor name.</p>"""
    optimization_metric: NotRequired[
        "capo_forecast.types.optimization_metric.OptimizationMetric"
    ]
    """<p>The accuracy metric used to optimize the predictor.</p>"""
    explain_predictor: NotRequired["capo_forecast.types.boolean.Boolean"]
    """<p>Create an Explainability resource for the predictor.</p>"""
    tags: NotRequired["capo_forecast.types.tags.Tags"]
    """<p>Optional metadata to help you categorize and organize your predictors. Each tag consists of a key and an optional value, both of which you define. Tag keys and values are case sensitive.</p> <p>The following restrictions apply to tags:</p> <ul> <li> <p>For each resource, each tag key must be unique and each tag key must have one value.</p> </li> <li> <p>Maximum number of tags per resource: 50.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8.</p> </li> <li> <p>Accepted characters: all letters and numbers, spaces representable in UTF-8, and + - = . _ : / @. If your tagging schema is used across other services and resources, the character restrictions of those services also apply. </p> </li> <li> <p>Key prefixes cannot include any upper or lowercase combination of <code>aws:</code> or <code>AWS:</code>. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit. You cannot edit or delete tag keys with this prefix.</p> </li> </ul>"""
    monitor_config: NotRequired["capo_forecast.types.monitor_config.MonitorConfig"]
    """<p>The configuration details for predictor monitoring. Provide a name for the monitor resource to enable predictor monitoring.</p> <p>Predictor monitoring allows you to see how your predictor's performance changes over time. For more information, see <a href="https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring.html">Predictor Monitoring</a>.</p>"""
    time_alignment_boundary: NotRequired[
        "capo_forecast.types.time_alignment_boundary.TimeAlignmentBoundary"
    ]
    """<p>The time boundary Forecast uses to align and aggregate any data that doesn't align with your forecast frequency. Provide the unit of time and the time boundary as a key value pair. For more information on specifying a time boundary, see <a href="https://docs.aws.amazon.com/forecast/latest/dg/data-aggregation.html#specifying-time-boundary">Specifying a Time Boundary</a>. If you don't provide a time boundary, Forecast uses a set of <a href="https://docs.aws.amazon.com/forecast/latest/dg/data-aggregation.html#default-time-boundaries">Default Time Boundaries</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAutoPredictorRequest) -> dict:
    out: dict = {}
    out["PredictorName"] = value["predictor_name"]
    if "forecast_horizon" in value:
        out["ForecastHorizon"] = value["forecast_horizon"]
    if "forecast_types" in value:
        import capo_forecast.types.forecast_types

        out["ForecastTypes"] = (
            capo_forecast.types.forecast_types.serialize_aws_json_1_1(
                value["forecast_types"]
            )
        )
    if "forecast_dimensions" in value:
        import capo_forecast.types.forecast_dimensions

        out["ForecastDimensions"] = (
            capo_forecast.types.forecast_dimensions.serialize_aws_json_1_1(
                value["forecast_dimensions"]
            )
        )
    if "forecast_frequency" in value:
        out["ForecastFrequency"] = value["forecast_frequency"]
    if "data_config" in value:
        import capo_forecast.types.data_config

        out["DataConfig"] = capo_forecast.types.data_config.serialize_aws_json_1_1(
            value["data_config"]
        )
    if "encryption_config" in value:
        import capo_forecast.types.encryption_config

        out["EncryptionConfig"] = (
            capo_forecast.types.encryption_config.serialize_aws_json_1_1(
                value["encryption_config"]
            )
        )
    if "reference_predictor_arn" in value:
        out["ReferencePredictorArn"] = value["reference_predictor_arn"]
    if "optimization_metric" in value:
        import capo_forecast.types.optimization_metric

        out["OptimizationMetric"] = (
            capo_forecast.types.optimization_metric.serialize_aws_json_1_1(
                value["optimization_metric"]
            )
        )
    if "explain_predictor" in value:
        out["ExplainPredictor"] = value["explain_predictor"]
    if "tags" in value:
        import capo_forecast.types.tags

        out["Tags"] = capo_forecast.types.tags.serialize_aws_json_1_1(value["tags"])
    if "monitor_config" in value:
        import capo_forecast.types.monitor_config

        out["MonitorConfig"] = (
            capo_forecast.types.monitor_config.serialize_aws_json_1_1(
                value["monitor_config"]
            )
        )
    if "time_alignment_boundary" in value:
        import capo_forecast.types.time_alignment_boundary

        out["TimeAlignmentBoundary"] = (
            capo_forecast.types.time_alignment_boundary.serialize_aws_json_1_1(
                value["time_alignment_boundary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAutoPredictorRequest:
    out: CreateAutoPredictorRequest = {}  # type: ignore[typeddict-item]
    if data.get("PredictorName") is not None:
        out["predictor_name"] = data["PredictorName"]
    else:
        raise DeserializationError("CreateAutoPredictorRequest.predictor_name required")
    if data.get("ForecastHorizon") is not None:
        out["forecast_horizon"] = data["ForecastHorizon"]
    if data.get("ForecastTypes") is not None:
        import capo_forecast.types.forecast_types

        out["forecast_types"] = (
            capo_forecast.types.forecast_types.deserialize_aws_json_1_1(
                data["ForecastTypes"]
            )
        )
    if data.get("ForecastDimensions") is not None:
        import capo_forecast.types.forecast_dimensions

        out["forecast_dimensions"] = (
            capo_forecast.types.forecast_dimensions.deserialize_aws_json_1_1(
                data["ForecastDimensions"]
            )
        )
    if data.get("ForecastFrequency") is not None:
        out["forecast_frequency"] = data["ForecastFrequency"]
    if data.get("DataConfig") is not None:
        import capo_forecast.types.data_config

        out["data_config"] = capo_forecast.types.data_config.deserialize_aws_json_1_1(
            data["DataConfig"]
        )
    if data.get("EncryptionConfig") is not None:
        import capo_forecast.types.encryption_config

        out["encryption_config"] = (
            capo_forecast.types.encryption_config.deserialize_aws_json_1_1(
                data["EncryptionConfig"]
            )
        )
    if data.get("ReferencePredictorArn") is not None:
        out["reference_predictor_arn"] = data["ReferencePredictorArn"]
    if data.get("OptimizationMetric") is not None:
        import capo_forecast.types.optimization_metric

        out["optimization_metric"] = (
            capo_forecast.types.optimization_metric.deserialize_aws_json_1_1(
                data["OptimizationMetric"]
            )
        )
    if data.get("ExplainPredictor") is not None:
        out["explain_predictor"] = data["ExplainPredictor"]
    if data.get("Tags") is not None:
        import capo_forecast.types.tags

        out["tags"] = capo_forecast.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("MonitorConfig") is not None:
        import capo_forecast.types.monitor_config

        out["monitor_config"] = (
            capo_forecast.types.monitor_config.deserialize_aws_json_1_1(
                data["MonitorConfig"]
            )
        )
    if data.get("TimeAlignmentBoundary") is not None:
        import capo_forecast.types.time_alignment_boundary

        out["time_alignment_boundary"] = (
            capo_forecast.types.time_alignment_boundary.deserialize_aws_json_1_1(
                data["TimeAlignmentBoundary"]
            )
        )
    return out
