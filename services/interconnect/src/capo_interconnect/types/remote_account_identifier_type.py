"""Generated from Smithy shape ``com.amazonaws.interconnect#RemoteAccountIdentifierType``."""

from typing import Literal, TypeAlias, cast

RemoteAccountIdentifierType: TypeAlias = Literal[
    "account",
    "email",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RemoteAccountIdentifierType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RemoteAccountIdentifierType:
    return cast(RemoteAccountIdentifierType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RemoteAccountIdentifierType) -> str:
    return value


def deserialize_cbor(data: str) -> RemoteAccountIdentifierType:
    return cast(RemoteAccountIdentifierType, data)
