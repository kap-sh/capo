"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#FilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.filter_value

FilterValues: TypeAlias = list["capo_compute_optimizer.types.filter_value.FilterValue"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> FilterValues:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FilterValues) -> list:
    return list(value)


def deserialize_cbor(data: list) -> FilterValues:
    return [item for item in data if item is not None]
