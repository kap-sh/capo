"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#BackupState``."""

from typing import Literal, TypeAlias, cast

BackupState: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "READY",
    "DELETED",
    "PENDING_DELETION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BackupState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BackupState:
    return cast(BackupState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BackupState) -> str:
    return value


def deserialize_cbor(data: str) -> BackupState:
    return cast(BackupState, data)
