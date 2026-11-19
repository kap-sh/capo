"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleDimensionValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.idle_dimension_value

IdleDimensionValues: TypeAlias = list[
    "capo_compute_optimizer.types.idle_dimension_value.IdleDimensionValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleDimensionValues) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> IdleDimensionValues:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdleDimensionValues) -> list:
    return list(value)


def deserialize_cbor(data: list) -> IdleDimensionValues:
    return [item for item in data if item is not None]
