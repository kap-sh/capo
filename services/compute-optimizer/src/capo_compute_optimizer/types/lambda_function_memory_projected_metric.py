"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionMemoryProjectedMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.lambda_function_memory_metric_name
    import capo_compute_optimizer.types.lambda_function_memory_metric_statistic
    import capo_compute_optimizer.types.metric_value


class LambdaFunctionMemoryProjectedMetric(TypedDict, closed=True):
    name: NotRequired[
        "capo_compute_optimizer.types.lambda_function_memory_metric_name.LambdaFunctionMemoryMetricName"
    ]
    """<p>The name of the projected utilization metric.</p>"""
    statistic: NotRequired[
        "capo_compute_optimizer.types.lambda_function_memory_metric_statistic.LambdaFunctionMemoryMetricStatistic"
    ]
    """<p>The statistic of the projected utilization metric.</p>"""
    value: "capo_compute_optimizer.types.metric_value.MetricValue"
    """<p>The values of the projected utilization metrics.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionMemoryProjectedMetric) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.lambda_function_memory_metric_name

        out["name"] = (
            capo_compute_optimizer.types.lambda_function_memory_metric_name.serialize_aws_json_1_0(
                value["name"]
            )
        )
    if "statistic" in value:
        import capo_compute_optimizer.types.lambda_function_memory_metric_statistic

        out["statistic"] = (
            capo_compute_optimizer.types.lambda_function_memory_metric_statistic.serialize_aws_json_1_0(
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


def deserialize_aws_json_1_0(data: dict) -> LambdaFunctionMemoryProjectedMetric:
    out: LambdaFunctionMemoryProjectedMetric = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.lambda_function_memory_metric_name

        out["name"] = (
            capo_compute_optimizer.types.lambda_function_memory_metric_name.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    if data.get("statistic") is not None:
        import capo_compute_optimizer.types.lambda_function_memory_metric_statistic

        out["statistic"] = (
            capo_compute_optimizer.types.lambda_function_memory_metric_statistic.deserialize_aws_json_1_0(
                data["statistic"]
            )
        )
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LambdaFunctionMemoryProjectedMetric) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.lambda_function_memory_metric_name

        out["name"] = (
            capo_compute_optimizer.types.lambda_function_memory_metric_name.serialize_cbor(
                value["name"]
            )
        )
    if "statistic" in value:
        import capo_compute_optimizer.types.lambda_function_memory_metric_statistic

        out["statistic"] = (
            capo_compute_optimizer.types.lambda_function_memory_metric_statistic.serialize_cbor(
                value["statistic"]
            )
        )
    out["value"] = value.get("value", 0)
    return out


def deserialize_cbor(data: dict) -> LambdaFunctionMemoryProjectedMetric:
    out: LambdaFunctionMemoryProjectedMetric = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.lambda_function_memory_metric_name

        out["name"] = (
            capo_compute_optimizer.types.lambda_function_memory_metric_name.deserialize_cbor(
                data["name"]
            )
        )
    if data.get("statistic") is not None:
        import capo_compute_optimizer.types.lambda_function_memory_metric_statistic

        out["statistic"] = (
            capo_compute_optimizer.types.lambda_function_memory_metric_statistic.deserialize_cbor(
                data["statistic"]
            )
        )
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0
    return out
