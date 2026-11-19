"""Generated from Smithy shape ``com.amazonaws.snowball#StorageUnit``."""

from typing import Literal, TypeAlias, cast

StorageUnit: TypeAlias = Literal["TB",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageUnit:
    return cast(StorageUnit, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StorageUnit) -> str:
    return value


def deserialize_cbor(data: str) -> StorageUnit:
    return cast(StorageUnit, data)
