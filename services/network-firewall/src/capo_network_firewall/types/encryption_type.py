"""Generated from Smithy shape ``com.amazonaws.networkfirewall#EncryptionType``."""

from typing import Literal, TypeAlias, cast

EncryptionType: TypeAlias = Literal[
    "CUSTOMER_KMS",
    "AWS_OWNED_KMS_KEY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EncryptionType:
    return cast(EncryptionType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EncryptionType) -> str:
    return value


def deserialize_cbor(data: str) -> EncryptionType:
    return cast(EncryptionType, data)
