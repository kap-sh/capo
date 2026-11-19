"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleUtilizationMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.idle_utilization_metric

IdleUtilizationMetrics: TypeAlias = list[
    "capo_compute_optimizer.types.idle_utilization_metric.IdleUtilizationMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleUtilizationMetrics) -> list:
    import capo_compute_optimizer.types.idle_utilization_metric

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.idle_utilization_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> IdleUtilizationMetrics:
    import capo_compute_optimizer.types.idle_utilization_metric

    out: IdleUtilizationMetrics = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.idle_utilization_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdleUtilizationMetrics) -> list:
    import capo_compute_optimizer.types.idle_utilization_metric

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.idle_utilization_metric.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> IdleUtilizationMetrics:
    import capo_compute_optimizer.types.idle_utilization_metric

    out: IdleUtilizationMetrics = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.idle_utilization_metric.deserialize_cbor(item)
        )
    return out
