"""Generated from Smithy shape ``com.amazonaws.workspaces#ModificationStateEnum``."""

from typing import Literal, TypeAlias, cast

ModificationStateEnum: TypeAlias = Literal[
    "UPDATE_INITIATED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModificationStateEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModificationStateEnum:
    return cast(ModificationStateEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ModificationStateEnum) -> str:
    return value


def deserialize_cbor(data: str) -> ModificationStateEnum:
    return cast(ModificationStateEnum, data)
