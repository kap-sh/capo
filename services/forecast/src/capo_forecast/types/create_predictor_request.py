"""Generated from Smithy shape ``com.amazonaws.forecast#CreatePredictorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.auto_ml_override_strategy
    import capo_forecast.types.boolean
    import capo_forecast.types.encryption_config
    import capo_forecast.types.evaluation_parameters
    import capo_forecast.types.featurization_config
    import capo_forecast.types.forecast_types
    import capo_forecast.types.hyper_parameter_tuning_job_config
    import capo_forecast.types.input_data_config
    import capo_forecast.types.integer
    import capo_forecast.types.name
    import capo_forecast.types.optimization_metric
    import capo_forecast.types.tags
    import capo_forecast.types.training_parameters


class CreatePredictorRequest(TypedDict, closed=True):
    predictor_name: "capo_forecast.types.name.Name"
    """<p>A name for the predictor.</p>"""
    algorithm_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the algorithm to use for model training. Required if <code>PerformAutoML</code> is not set to <code>true</code>.</p> <p class="title"> <b>Supported algorithms:</b> </p> <ul> <li> <p> <code>arn:aws:forecast:::algorithm/ARIMA</code> </p> </li> <li> <p> <code>arn:aws:forecast:::algorithm/CNN-QR</code> </p> </li> <li> <p> <code>arn:aws:forecast:::algorithm/Deep_AR_Plus</code> </p> </li> <li> <p> <code>arn:aws:forecast:::algorithm/ETS</code> </p> </li> <li> <p> <code>arn:aws:forecast:::algorithm/NPTS</code> </p> </li> <li> <p> <code>arn:aws:forecast:::algorithm/Prophet</code> </p> </li> </ul>"""
    forecast_horizon: "capo_forecast.types.integer.Integer"
    """<p>Specifies the number of time-steps that the model is trained to predict. The forecast horizon is also called the prediction length.</p> <p>For example, if you configure a dataset for daily data collection (using the <code>DataFrequency</code> parameter of the <a>CreateDataset</a> operation) and set the forecast horizon to 10, the model returns predictions for 10 days.</p> <p>The maximum forecast horizon is the lesser of 500 time-steps or 1/3 of the TARGET_TIME_SERIES dataset length.</p>"""
    forecast_types: NotRequired["capo_forecast.types.forecast_types.ForecastTypes"]
    """<p>Specifies the forecast types used to train a predictor. You can specify up to five forecast types. Forecast types can be quantiles from 0.01 to 0.99, by increments of 0.01 or higher. You can also specify the mean forecast with <code>mean</code>. </p> <p>The default value is <code>["0.10", "0.50", "0.9"]</code>.</p>"""
    perform_auto_ml: NotRequired["capo_forecast.types.boolean.Boolean"]
    """<p>Whether to perform AutoML. When Amazon Forecast performs AutoML, it evaluates the algorithms it provides and chooses the best algorithm and configuration for your training dataset.</p> <p>The default value is <code>false</code>. In this case, you are required to specify an algorithm.</p> <p>Set <code>PerformAutoML</code> to <code>true</code> to have Amazon Forecast perform AutoML. This is a good option if you aren't sure which algorithm is suitable for your training data. In this case, <code>PerformHPO</code> must be false.</p>"""
    auto_ml_override_strategy: NotRequired[
        "capo_forecast.types.auto_ml_override_strategy.AutoMLOverrideStrategy"
    ]
    """<note> <p> The <code>LatencyOptimized</code> AutoML override strategy is only available in private beta. Contact Amazon Web Services Support or your account manager to learn more about access privileges. </p> </note> <p>Used to overide the default AutoML strategy, which is to optimize predictor accuracy. To apply an AutoML strategy that minimizes training time, use <code>LatencyOptimized</code>.</p> <p>This parameter is only valid for predictors trained using AutoML.</p>"""
    perform_hpo: NotRequired["capo_forecast.types.boolean.Boolean"]
    """<p>Whether to perform hyperparameter optimization (HPO). HPO finds optimal hyperparameter values for your training data. The process of performing HPO is known as running a hyperparameter tuning job.</p> <p>The default value is <code>false</code>. In this case, Amazon Forecast uses default hyperparameter values from the chosen algorithm.</p> <p>To override the default values, set <code>PerformHPO</code> to <code>true</code> and, optionally, supply the <a>HyperParameterTuningJobConfig</a> object. The tuning job specifies a metric to optimize, which hyperparameters participate in tuning, and the valid range for each tunable hyperparameter. In this case, you are required to specify an algorithm and <code>PerformAutoML</code> must be false.</p> <p>The following algorithms support HPO:</p> <ul> <li> <p>DeepAR+</p> </li> <li> <p>CNN-QR</p> </li> </ul>"""
    training_parameters: NotRequired[
        "capo_forecast.types.training_parameters.TrainingParameters"
    ]
    """<p>The hyperparameters to override for model training. The hyperparameters that you can override are listed in the individual algorithms. For the list of supported algorithms, see <a>aws-forecast-choosing-recipes</a>.</p>"""
    evaluation_parameters: NotRequired[
        "capo_forecast.types.evaluation_parameters.EvaluationParameters"
    ]
    """<p>Used to override the default evaluation parameters of the specified algorithm. Amazon Forecast evaluates a predictor by splitting a dataset into training data and testing data. The evaluation parameters define how to perform the split and the number of iterations.</p>"""
    hpo_config: NotRequired[
        "capo_forecast.types.hyper_parameter_tuning_job_config.HyperParameterTuningJobConfig"
    ]
    """<p>Provides hyperparameter override values for the algorithm. If you don't provide this parameter, Amazon Forecast uses default values. The individual algorithms specify which hyperparameters support hyperparameter optimization (HPO). For more information, see <a>aws-forecast-choosing-recipes</a>.</p> <p>If you included the <code>HPOConfig</code> object, you must set <code>PerformHPO</code> to true.</p>"""
    input_data_config: "capo_forecast.types.input_data_config.InputDataConfig"
    """<p>Describes the dataset group that contains the data to use to train the predictor.</p>"""
    featurization_config: "capo_forecast.types.featurization_config.FeaturizationConfig"
    """<p>The featurization configuration.</p>"""
    encryption_config: NotRequired[
        "capo_forecast.types.encryption_config.EncryptionConfig"
    ]
    """<p>An Key Management Service (KMS) key and the Identity and Access Management (IAM) role that Amazon Forecast can assume to access the key.</p>"""
    tags: NotRequired["capo_forecast.types.tags.Tags"]
    """<p>The optional metadata that you apply to the predictor to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for keys as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit.</p> </li> </ul>"""
    optimization_metric: NotRequired[
        "capo_forecast.types.optimization_metric.OptimizationMetric"
    ]
    """<p>The accuracy metric used to optimize the predictor.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePredictorRequest) -> dict:
    out: dict = {}
    out["PredictorName"] = value["predictor_name"]
    if "algorithm_arn" in value:
        out["AlgorithmArn"] = value["algorithm_arn"]
    out["ForecastHorizon"] = value["forecast_horizon"]
    if "forecast_types" in value:
        import capo_forecast.types.forecast_types

        out["ForecastTypes"] = (
            capo_forecast.types.forecast_types.serialize_aws_json_1_1(
                value["forecast_types"]
            )
        )
    if "perform_auto_ml" in value:
        out["PerformAutoML"] = value["perform_auto_ml"]
    if "auto_ml_override_strategy" in value:
        import capo_forecast.types.auto_ml_override_strategy

        out["AutoMLOverrideStrategy"] = (
            capo_forecast.types.auto_ml_override_strategy.serialize_aws_json_1_1(
                value["auto_ml_override_strategy"]
            )
        )
    if "perform_hpo" in value:
        out["PerformHPO"] = value["perform_hpo"]
    if "training_parameters" in value:
        import capo_forecast.types.training_parameters

        out["TrainingParameters"] = (
            capo_forecast.types.training_parameters.serialize_aws_json_1_1(
                value["training_parameters"]
            )
        )
    if "evaluation_parameters" in value:
        import capo_forecast.types.evaluation_parameters

        out["EvaluationParameters"] = (
            capo_forecast.types.evaluation_parameters.serialize_aws_json_1_1(
                value["evaluation_parameters"]
            )
        )
    if "hpo_config" in value:
        import capo_forecast.types.hyper_parameter_tuning_job_config

        out["HPOConfig"] = (
            capo_forecast.types.hyper_parameter_tuning_job_config.serialize_aws_json_1_1(
                value["hpo_config"]
            )
        )
    import capo_forecast.types.input_data_config

    out["InputDataConfig"] = (
        capo_forecast.types.input_data_config.serialize_aws_json_1_1(
            value["input_data_config"]
        )
    )
    import capo_forecast.types.featurization_config

    out["FeaturizationConfig"] = (
        capo_forecast.types.featurization_config.serialize_aws_json_1_1(
            value["featurization_config"]
        )
    )
    if "encryption_config" in value:
        import capo_forecast.types.encryption_config

        out["EncryptionConfig"] = (
            capo_forecast.types.encryption_config.serialize_aws_json_1_1(
                value["encryption_config"]
            )
        )
    if "tags" in value:
        import capo_forecast.types.tags

        out["Tags"] = capo_forecast.types.tags.serialize_aws_json_1_1(value["tags"])
    if "optimization_metric" in value:
        import capo_forecast.types.optimization_metric

        out["OptimizationMetric"] = (
            capo_forecast.types.optimization_metric.serialize_aws_json_1_1(
                value["optimization_metric"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePredictorRequest:
    out: CreatePredictorRequest = {}  # type: ignore[typeddict-item]
    if data.get("PredictorName") is not None:
        out["predictor_name"] = data["PredictorName"]
    else:
        raise DeserializationError("CreatePredictorRequest.predictor_name required")
    if data.get("AlgorithmArn") is not None:
        out["algorithm_arn"] = data["AlgorithmArn"]
    if data.get("ForecastHorizon") is not None:
        out["forecast_horizon"] = data["ForecastHorizon"]
    else:
        raise DeserializationError("CreatePredictorRequest.forecast_horizon required")
    if data.get("ForecastTypes") is not None:
        import capo_forecast.types.forecast_types

        out["forecast_types"] = (
            capo_forecast.types.forecast_types.deserialize_aws_json_1_1(
                data["ForecastTypes"]
            )
        )
    if data.get("PerformAutoML") is not None:
        out["perform_auto_ml"] = data["PerformAutoML"]
    if data.get("AutoMLOverrideStrategy") is not None:
        import capo_forecast.types.auto_ml_override_strategy

        out["auto_ml_override_strategy"] = (
            capo_forecast.types.auto_ml_override_strategy.deserialize_aws_json_1_1(
                data["AutoMLOverrideStrategy"]
            )
        )
    if data.get("PerformHPO") is not None:
        out["perform_hpo"] = data["PerformHPO"]
    if data.get("TrainingParameters") is not None:
        import capo_forecast.types.training_parameters

        out["training_parameters"] = (
            capo_forecast.types.training_parameters.deserialize_aws_json_1_1(
                data["TrainingParameters"]
            )
        )
    if data.get("EvaluationParameters") is not None:
        import capo_forecast.types.evaluation_parameters

        out["evaluation_parameters"] = (
            capo_forecast.types.evaluation_parameters.deserialize_aws_json_1_1(
                data["EvaluationParameters"]
            )
        )
    if data.get("HPOConfig") is not None:
        import capo_forecast.types.hyper_parameter_tuning_job_config

        out["hpo_config"] = (
            capo_forecast.types.hyper_parameter_tuning_job_config.deserialize_aws_json_1_1(
                data["HPOConfig"]
            )
        )
    if data.get("InputDataConfig") is not None:
        import capo_forecast.types.input_data_config

        out["input_data_config"] = (
            capo_forecast.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError("CreatePredictorRequest.input_data_config required")
    if data.get("FeaturizationConfig") is not None:
        import capo_forecast.types.featurization_config

        out["featurization_config"] = (
            capo_forecast.types.featurization_config.deserialize_aws_json_1_1(
                data["FeaturizationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePredictorRequest.featurization_config required"
        )
    if data.get("EncryptionConfig") is not None:
        import capo_forecast.types.encryption_config

        out["encryption_config"] = (
            capo_forecast.types.encryption_config.deserialize_aws_json_1_1(
                data["EncryptionConfig"]
            )
        )
    if data.get("Tags") is not None:
        import capo_forecast.types.tags

        out["tags"] = capo_forecast.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("OptimizationMetric") is not None:
        import capo_forecast.types.optimization_metric

        out["optimization_metric"] = (
            capo_forecast.types.optimization_metric.deserialize_aws_json_1_1(
                data["OptimizationMetric"]
            )
        )
    return out
