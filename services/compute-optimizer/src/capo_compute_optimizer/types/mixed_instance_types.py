"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#MixedInstanceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.mixed_instance_type

MixedInstanceTypes: TypeAlias = list[
    "capo_compute_optimizer.types.mixed_instance_type.MixedInstanceType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MixedInstanceTypes) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> MixedInstanceTypes:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MixedInstanceTypes) -> list:
    return list(value)


def deserialize_cbor(data: list) -> MixedInstanceTypes:
    return [item for item in data if item is not None]
