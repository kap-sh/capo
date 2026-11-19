"""Generated from Smithy shape ``com.amazonaws.acmpca#CrlType``."""

from typing import Literal, TypeAlias, cast

CrlType: TypeAlias = Literal[
    "COMPLETE",
    "PARTITIONED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrlType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CrlType:
    return cast(CrlType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CrlType) -> str:
    return value


def deserialize_cbor(data: str) -> CrlType:
    return cast(CrlType, data)
