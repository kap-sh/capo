"""Generated from Smithy shape ``com.amazonaws.sagemaker#FinalHyperParameterTuningJobObjectiveMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.hyper_parameter_tuning_job_objective_type
    import capo_sagemaker.types.metric_name
    import capo_sagemaker.types.metric_value


class FinalHyperParameterTuningJobObjectiveMetric(TypedDict, closed=True):
    type: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_objective_type.HyperParameterTuningJobObjectiveType"
    ]
    """<p>Select if you want to minimize or maximize the objective metric during hyperparameter tuning. </p>"""
    metric_name: NotRequired["capo_sagemaker.types.metric_name.MetricName"]
    """<p>The name of the objective metric. For SageMaker built-in algorithms, metrics are defined per algorithm. See the <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost-tuning.html">metrics for XGBoost</a> as an example. You can also use a custom algorithm for training and define your own metrics. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html">Define metrics and environment variables</a>.</p>"""
    value: NotRequired["capo_sagemaker.types.metric_value.MetricValue"]
    """<p>The value of the objective metric.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FinalHyperParameterTuningJobObjectiveMetric) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_sagemaker.types.hyper_parameter_tuning_job_objective_type

        out["Type"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_objective_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "value" in value:
        out["Value"] = (
            "NaN"
            if value["value"] != value["value"]
            else "Infinity"
            if value["value"] == float("inf")
            else "-Infinity"
            if value["value"] == float("-inf")
            else value["value"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FinalHyperParameterTuningJobObjectiveMetric:
    out: FinalHyperParameterTuningJobObjectiveMetric = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_sagemaker.types.hyper_parameter_tuning_job_objective_type

        out["type"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_objective_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    return out
