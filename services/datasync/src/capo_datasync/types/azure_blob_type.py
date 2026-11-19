"""Generated from Smithy shape ``com.amazonaws.datasync#AzureBlobType``."""

from typing import Literal, TypeAlias, cast

AzureBlobType: TypeAlias = Literal["BLOCK",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AzureBlobType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AzureBlobType:
    return cast(AzureBlobType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AzureBlobType) -> str:
    return value


def deserialize_cbor(data: str) -> AzureBlobType:
    return cast(AzureBlobType, data)
