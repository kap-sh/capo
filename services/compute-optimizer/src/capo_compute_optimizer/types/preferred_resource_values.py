"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#PreferredResourceValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.preferred_resource_value

PreferredResourceValues: TypeAlias = list[
    "capo_compute_optimizer.types.preferred_resource_value.PreferredResourceValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreferredResourceValues) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> PreferredResourceValues:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PreferredResourceValues) -> list:
    return list(value)


def deserialize_cbor(data: list) -> PreferredResourceValues:
    return [item for item in data if item is not None]
