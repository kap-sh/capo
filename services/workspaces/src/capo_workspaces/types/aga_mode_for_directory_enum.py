"""Generated from Smithy shape ``com.amazonaws.workspaces#AGAModeForDirectoryEnum``."""

from typing import Literal, TypeAlias, cast

AGAModeForDirectoryEnum: TypeAlias = Literal[
    "ENABLED_AUTO",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AGAModeForDirectoryEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AGAModeForDirectoryEnum:
    return cast(AGAModeForDirectoryEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AGAModeForDirectoryEnum) -> str:
    return value


def deserialize_cbor(data: str) -> AGAModeForDirectoryEnum:
    return cast(AGAModeForDirectoryEnum, data)
