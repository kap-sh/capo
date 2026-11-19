"""Generated from Smithy shape ``com.amazonaws.directoryservice#SubnetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.subnet_id

SubnetIds: TypeAlias = list["capo_directory_service.types.subnet_id.SubnetId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SubnetIds:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SubnetIds) -> list:
    return list(value)


def deserialize_cbor(data: list) -> SubnetIds:
    return [item for item in data if item is not None]
