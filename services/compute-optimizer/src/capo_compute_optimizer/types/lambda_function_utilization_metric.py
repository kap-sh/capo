"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionUtilizationMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.lambda_function_metric_name
    import capo_compute_optimizer.types.lambda_function_metric_statistic
    import capo_compute_optimizer.types.metric_value


class LambdaFunctionUtilizationMetric(TypedDict, closed=True):
    name: NotRequired[
        "capo_compute_optimizer.types.lambda_function_metric_name.LambdaFunctionMetricName"
    ]
    """<p>The name of the utilization metric.</p> <p>The following utilization metrics are available:</p> <ul> <li> <p> <code>Duration</code> - The amount of time that your function code spends processing an event.</p> </li> <li> <p> <code>Memory</code> - The amount of memory used per invocation.</p> </li> </ul>"""
    statistic: NotRequired[
        "capo_compute_optimizer.types.lambda_function_metric_statistic.LambdaFunctionMetricStatistic"
    ]
    """<p>The statistic of the utilization metric.</p> <p>The Compute Optimizer API, Command Line Interface (CLI), and SDKs return utilization metrics using only the <code>Maximum</code> statistic, which is the highest value observed during the specified period.</p> <p>The Compute Optimizer console displays graphs for some utilization metrics using the <code>Average</code> statistic, which is the value of <code>Sum</code> / <code>SampleCount</code> during the specified period. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendations.html">Viewing resource recommendations</a> in the <i>Compute Optimizer User Guide</i>. You can also get averaged utilization metric data for your resources using Amazon CloudWatch. For more information, see the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html">Amazon CloudWatch User Guide</a>.</p>"""
    value: "capo_compute_optimizer.types.metric_value.MetricValue"
    """<p>The value of the utilization metric.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionUtilizationMetric) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.lambda_function_metric_name

        out["name"] = (
            capo_compute_optimizer.types.lambda_function_metric_name.serialize_aws_json_1_0(
                value["name"]
            )
        )
    if "statistic" in value:
        import capo_compute_optimizer.types.lambda_function_metric_statistic

        out["statistic"] = (
            capo_compute_optimizer.types.lambda_function_metric_statistic.serialize_aws_json_1_0(
                value["statistic"]
            )
        )
    out["value"] = (
        "NaN"
        if value.get("value", 0) != value.get("value", 0)
        else "Infinity"
        if value.get("value", 0) == float("inf")
        else "-Infinity"
        if value.get("value", 0) == float("-inf")
        else value.get("value", 0)
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaFunctionUtilizationMetric:
    out: LambdaFunctionUtilizationMetric = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.lambda_function_metric_name

        out["name"] = (
            capo_compute_optimizer.types.lambda_function_metric_name.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    if data.get("statistic") is not None:
        import capo_compute_optimizer.types.lambda_function_metric_statistic

        out["statistic"] = (
            capo_compute_optimizer.types.lambda_function_metric_statistic.deserialize_aws_json_1_0(
                data["statistic"]
            )
        )
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0
    return out
