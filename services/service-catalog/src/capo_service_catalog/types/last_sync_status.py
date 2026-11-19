"""Generated from Smithy shape ``com.amazonaws.servicecatalog#LastSyncStatus``."""

from typing import Literal, TypeAlias, cast

LastSyncStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastSyncStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LastSyncStatus:
    return cast(LastSyncStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LastSyncStatus) -> str:
    return value


def deserialize_cbor(data: str) -> LastSyncStatus:
    return cast(LastSyncStatus, data)
