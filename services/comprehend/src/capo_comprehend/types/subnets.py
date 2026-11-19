"""Generated from Smithy shape ``com.amazonaws.comprehend#Subnets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.subnet_id

Subnets: TypeAlias = list["capo_comprehend.types.subnet_id.SubnetId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Subnets) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Subnets:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Subnets) -> list:
    return list(value)


def deserialize_cbor(data: list) -> Subnets:
    return [item for item in data if item is not None]
