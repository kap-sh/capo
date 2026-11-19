"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EBSUtilizationMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.ebs_utilization_metric

EBSUtilizationMetrics: TypeAlias = list[
    "capo_compute_optimizer.types.ebs_utilization_metric.EBSUtilizationMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EBSUtilizationMetrics) -> list:
    import capo_compute_optimizer.types.ebs_utilization_metric

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.ebs_utilization_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EBSUtilizationMetrics:
    import capo_compute_optimizer.types.ebs_utilization_metric

    out: EBSUtilizationMetrics = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.ebs_utilization_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EBSUtilizationMetrics) -> list:
    import capo_compute_optimizer.types.ebs_utilization_metric

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.ebs_utilization_metric.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> EBSUtilizationMetrics:
    import capo_compute_optimizer.types.ebs_utilization_metric

    out: EBSUtilizationMetrics = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.ebs_utilization_metric.deserialize_cbor(item)
        )
    return out
