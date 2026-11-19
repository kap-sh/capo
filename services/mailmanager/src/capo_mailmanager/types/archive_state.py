"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveState``."""

from typing import Literal, TypeAlias, cast

ArchiveState: TypeAlias = Literal[
    "ACTIVE",
    "PENDING_DELETION",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ArchiveState:
    return cast(ArchiveState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ArchiveState) -> str:
    return value


def deserialize_cbor(data: str) -> ArchiveState:
    return cast(ArchiveState, data)
