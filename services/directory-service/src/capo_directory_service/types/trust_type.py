"""Generated from Smithy shape ``com.amazonaws.directoryservice#TrustType``."""

from typing import Literal, TypeAlias, cast

TrustType: TypeAlias = Literal[
    "Forest",
    "External",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrustType:
    return cast(TrustType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TrustType) -> str:
    return value


def deserialize_cbor(data: str) -> TrustType:
    return cast(TrustType, data)
