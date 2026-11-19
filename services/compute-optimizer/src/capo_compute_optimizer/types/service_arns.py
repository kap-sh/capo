"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ServiceArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.service_arn

ServiceArns: TypeAlias = list["capo_compute_optimizer.types.service_arn.ServiceArn"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceArns) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ServiceArns:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceArns) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ServiceArns:
    return [item for item in data if item is not None]
