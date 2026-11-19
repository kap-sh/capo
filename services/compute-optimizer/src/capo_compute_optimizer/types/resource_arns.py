"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ResourceArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.resource_arn

ResourceArns: TypeAlias = list["capo_compute_optimizer.types.resource_arn.ResourceArn"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceArns) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ResourceArns:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceArns) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ResourceArns:
    return [item for item in data if item is not None]
