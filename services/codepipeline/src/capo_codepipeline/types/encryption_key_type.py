"""Generated from Smithy shape ``com.amazonaws.codepipeline#EncryptionKeyType``."""

from typing import Literal, TypeAlias, cast

EncryptionKeyType: TypeAlias = Literal["KMS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionKeyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EncryptionKeyType:
    return cast(EncryptionKeyType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EncryptionKeyType) -> str:
    return value


def deserialize_cbor(data: str) -> EncryptionKeyType:
    return cast(EncryptionKeyType, data)
