"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#FunctionArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.function_arn

FunctionArns: TypeAlias = list["capo_compute_optimizer.types.function_arn.FunctionArn"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FunctionArns) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> FunctionArns:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FunctionArns) -> list:
    return list(value)


def deserialize_cbor(data: list) -> FunctionArns:
    return [item for item in data if item is not None]
