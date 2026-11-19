"""Generated from Smithy shape ``com.amazonaws.datasync#PreserveDeletedFiles``."""

from typing import Literal, TypeAlias, cast

PreserveDeletedFiles: TypeAlias = Literal[
    "PRESERVE",
    "REMOVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreserveDeletedFiles) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreserveDeletedFiles:
    return cast(PreserveDeletedFiles, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PreserveDeletedFiles) -> str:
    return value


def deserialize_cbor(data: str) -> PreserveDeletedFiles:
    return cast(PreserveDeletedFiles, data)
