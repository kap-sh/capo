"""Generated from Smithy shape ``com.amazonaws.directoryservice#TrustDirection``."""

from typing import Literal, TypeAlias, cast

TrustDirection: TypeAlias = Literal[
    "One-Way: Outgoing",
    "One-Way: Incoming",
    "Two-Way",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustDirection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrustDirection:
    return cast(TrustDirection, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TrustDirection) -> str:
    return value


def deserialize_cbor(data: str) -> TrustDirection:
    return cast(TrustDirection, data)
