"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateType``."""

from typing import Literal, TypeAlias, cast

UpdateType: TypeAlias = Literal[
    "OS",
    "NETWORK",
    "SIZE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateType:
    return cast(UpdateType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateType) -> str:
    return value


def deserialize_cbor(data: str) -> UpdateType:
    return cast(UpdateType, data)
