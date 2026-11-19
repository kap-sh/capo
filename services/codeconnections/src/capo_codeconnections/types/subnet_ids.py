"""Generated from Smithy shape ``com.amazonaws.codeconnections#SubnetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeconnections.types.subnet_id

SubnetIds: TypeAlias = list["capo_codeconnections.types.subnet_id.SubnetId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SubnetIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SubnetIds:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SubnetIds) -> list:
    return list(value)


def deserialize_cbor(data: list) -> SubnetIds:
    return [item for item in data if item is not None]
