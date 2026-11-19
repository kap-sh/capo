"""Generated from Smithy shape ``com.amazonaws.acmpca#KeyStorageSecurityStandard``."""

from typing import Literal, TypeAlias, cast

KeyStorageSecurityStandard: TypeAlias = Literal[
    "FIPS_140_2_LEVEL_2_OR_HIGHER",
    "FIPS_140_2_LEVEL_3_OR_HIGHER",
    "CCPC_LEVEL_1_OR_HIGHER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyStorageSecurityStandard) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyStorageSecurityStandard:
    return cast(KeyStorageSecurityStandard, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: KeyStorageSecurityStandard) -> str:
    return value


def deserialize_cbor(data: str) -> KeyStorageSecurityStandard:
    return cast(KeyStorageSecurityStandard, data)
