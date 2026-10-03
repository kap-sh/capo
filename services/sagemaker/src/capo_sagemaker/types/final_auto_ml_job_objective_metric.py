"""Generated from Smithy shape ``com.amazonaws.sagemaker#FinalAutoMLJobObjectiveMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_job_objective_type
    import capo_sagemaker.types.auto_ml_metric_enum
    import capo_sagemaker.types.metric_value


class FinalAutoMLJobObjectiveMetric(TypedDict, closed=True):
    type: NotRequired[
        "capo_sagemaker.types.auto_ml_job_objective_type.AutoMLJobObjectiveType"
    ]
    """<p>The type of metric with the best result.</p>"""
    metric_name: NotRequired[
        "capo_sagemaker.types.auto_ml_metric_enum.AutoMLMetricEnum"
    ]
    """<p>The name of the metric with the best result. For a description of the possible objective metrics, see <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobObjective.html">AutoMLJobObjective$MetricName</a>.</p>"""
    value: NotRequired["capo_sagemaker.types.metric_value.MetricValue"]
    """<p>The value of the metric with the best result.</p>"""
    standard_metric_name: NotRequired[
        "capo_sagemaker.types.auto_ml_metric_enum.AutoMLMetricEnum"
    ]
    """<p>The name of the standard metric. For a description of the standard metrics, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-metrics-validation.html#autopilot-metrics">Autopilot candidate metrics</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FinalAutoMLJobObjectiveMetric) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_sagemaker.types.auto_ml_job_objective_type

        out["Type"] = (
            capo_sagemaker.types.auto_ml_job_objective_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "metric_name" in value:
        import capo_sagemaker.types.auto_ml_metric_enum

        out["MetricName"] = (
            capo_sagemaker.types.auto_ml_metric_enum.serialize_aws_json_1_1(
                value["metric_name"]
            )
        )
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
    if "standard_metric_name" in value:
        import capo_sagemaker.types.auto_ml_metric_enum

        out["StandardMetricName"] = (
            capo_sagemaker.types.auto_ml_metric_enum.serialize_aws_json_1_1(
                value["standard_metric_name"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FinalAutoMLJobObjectiveMetric:
    out: FinalAutoMLJobObjectiveMetric = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_sagemaker.types.auto_ml_job_objective_type

        out["type"] = (
            capo_sagemaker.types.auto_ml_job_objective_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("MetricName") is not None:
        import capo_sagemaker.types.auto_ml_metric_enum

        out["metric_name"] = (
            capo_sagemaker.types.auto_ml_metric_enum.deserialize_aws_json_1_1(
                data["MetricName"]
            )
        )
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    if data.get("StandardMetricName") is not None:
        import capo_sagemaker.types.auto_ml_metric_enum

        out["standard_metric_name"] = (
            capo_sagemaker.types.auto_ml_metric_enum.deserialize_aws_json_1_1(
                data["StandardMetricName"]
            )
        )
    return out
