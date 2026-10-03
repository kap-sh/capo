"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLJobObjective``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_metric_enum


class AutoMLJobObjective(TypedDict, closed=True):
    metric_name: NotRequired[
        "capo_sagemaker.types.auto_ml_metric_enum.AutoMLMetricEnum"
    ]
    """<p>The name of the objective metric used to measure the predictive quality of a machine learning system. During training, the model's parameters are updated iteratively to optimize its performance based on the feedback provided by the objective metric when evaluating the model on the validation dataset.</p> <p>The list of available metrics supported by Autopilot and the default metric applied when you do not specify a metric name explicitly depend on the problem type.</p> <ul> <li> <p>For tabular problem types:</p> <ul> <li> <p>List of available metrics: </p> <ul> <li> <p> Regression: <code>MAE</code>, <code>MSE</code>, <code>R2</code>, <code>RMSE</code> </p> </li> <li> <p> Binary classification: <code>Accuracy</code>, <code>AUC</code>, <code>BalancedAccuracy</code>, <code>F1</code>, <code>Precision</code>, <code>Recall</code> </p> </li> <li> <p> Multiclass classification: <code>Accuracy</code>, <code>BalancedAccuracy</code>, <code>F1macro</code>, <code>PrecisionMacro</code>, <code>RecallMacro</code> </p> </li> </ul> <p>For a description of each metric, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-metrics-validation.html#autopilot-metrics">Autopilot metrics for classification and regression</a>.</p> </li> <li> <p>Default objective metrics:</p> <ul> <li> <p>Regression: <code>MSE</code>.</p> </li> <li> <p>Binary classification: <code>F1</code>.</p> </li> <li> <p>Multiclass classification: <code>Accuracy</code>.</p> </li> </ul> </li> </ul> </li> <li> <p>For image or text classification problem types:</p> <ul> <li> <p>List of available metrics: <code>Accuracy</code> </p> <p>For a description of each metric, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/text-classification-data-format-and-metric.html">Autopilot metrics for text and image classification</a>.</p> </li> <li> <p>Default objective metrics: <code>Accuracy</code> </p> </li> </ul> </li> <li> <p>For time-series forecasting problem types:</p> <ul> <li> <p>List of available metrics: <code>RMSE</code>, <code>wQL</code>, <code>Average wQL</code>, <code>MASE</code>, <code>MAPE</code>, <code>WAPE</code> </p> <p>For a description of each metric, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/timeseries-objective-metric.html">Autopilot metrics for time-series forecasting</a>.</p> </li> <li> <p>Default objective metrics: <code>AverageWeightedQuantileLoss</code> </p> </li> </ul> </li> <li> <p>For text generation problem types (LLMs fine-tuning): Fine-tuning language models in Autopilot does not require setting the <code>AutoMLJobObjective</code> field. Autopilot fine-tunes LLMs without requiring multiple candidates to be trained and evaluated. Instead, using your dataset, Autopilot directly fine-tunes your target model to enhance a default objective metric, the cross-entropy loss. After fine-tuning a language model, you can evaluate the quality of its generated text using different metrics. For a list of the available metrics, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-llms-finetuning-metrics.html">Metrics for fine-tuning LLMs in Autopilot</a>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLJobObjective) -> dict:
    out: dict = {}
    if "metric_name" in value:
        import capo_sagemaker.types.auto_ml_metric_enum

        out["MetricName"] = (
            capo_sagemaker.types.auto_ml_metric_enum.serialize_aws_json_1_1(
                value["metric_name"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLJobObjective:
    out: AutoMLJobObjective = {}  # type: ignore[typeddict-item]
    if data.get("MetricName") is not None:
        import capo_sagemaker.types.auto_ml_metric_enum

        out["metric_name"] = (
            capo_sagemaker.types.auto_ml_metric_enum.deserialize_aws_json_1_1(
                data["MetricName"]
            )
        )
    return out
