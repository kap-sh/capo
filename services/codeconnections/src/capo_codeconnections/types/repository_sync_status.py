"""Generated from Smithy shape ``com.amazonaws.codeconnections#RepositorySyncStatus``."""

from typing import Literal, TypeAlias, cast

RepositorySyncStatus: TypeAlias = Literal[
    "FAILED",
    "INITIATED",
    "IN_PROGRESS",
    "SUCCEEDED",
    "QUEUED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositorySyncStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RepositorySyncStatus:
    return cast(RepositorySyncStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RepositorySyncStatus) -> str:
    return value


def deserialize_cbor(data: str) -> RepositorySyncStatus:
    return cast(RepositorySyncStatus, data)
