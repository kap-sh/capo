"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionMemoryProjectedMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.lambda_function_memory_projected_metric

LambdaFunctionMemoryProjectedMetrics: TypeAlias = list[
    "capo_compute_optimizer.types.lambda_function_memory_projected_metric.LambdaFunctionMemoryProjectedMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionMemoryProjectedMetrics) -> list:
    import capo_compute_optimizer.types.lambda_function_memory_projected_metric

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.lambda_function_memory_projected_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LambdaFunctionMemoryProjectedMetrics:
    import capo_compute_optimizer.types.lambda_function_memory_projected_metric

    out: LambdaFunctionMemoryProjectedMetrics = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.lambda_function_memory_projected_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LambdaFunctionMemoryProjectedMetrics) -> list:
    import capo_compute_optimizer.types.lambda_function_memory_projected_metric

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.lambda_function_memory_projected_metric.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> LambdaFunctionMemoryProjectedMetrics:
    import capo_compute_optimizer.types.lambda_function_memory_projected_metric

    out: LambdaFunctionMemoryProjectedMetrics = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.lambda_function_memory_projected_metric.deserialize_cbor(
                item
            )
        )
    return out
