"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InferredWorkloadTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.inferred_workload_type

InferredWorkloadTypes: TypeAlias = list[
    "capo_compute_optimizer.types.inferred_workload_type.InferredWorkloadType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InferredWorkloadTypes) -> list:
    import capo_compute_optimizer.types.inferred_workload_type

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.inferred_workload_type.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InferredWorkloadTypes:
    import capo_compute_optimizer.types.inferred_workload_type

    out: InferredWorkloadTypes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.inferred_workload_type.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InferredWorkloadTypes) -> list:
    import capo_compute_optimizer.types.inferred_workload_type

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.inferred_workload_type.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> InferredWorkloadTypes:
    import capo_compute_optimizer.types.inferred_workload_type

    out: InferredWorkloadTypes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.inferred_workload_type.deserialize_cbor(item)
        )
    return out
