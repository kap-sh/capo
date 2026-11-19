"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InstanceArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.instance_arn

InstanceArns: TypeAlias = list["capo_compute_optimizer.types.instance_arn.InstanceArn"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceArns) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> InstanceArns:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceArns) -> list:
    return list(value)


def deserialize_cbor(data: list) -> InstanceArns:
    return [item for item in data if item is not None]
