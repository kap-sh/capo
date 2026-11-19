"""Generated from Smithy shape ``com.amazonaws.workspaces#ModificationResourceEnum``."""

from typing import Literal, TypeAlias, cast

ModificationResourceEnum: TypeAlias = Literal[
    "ROOT_VOLUME",
    "USER_VOLUME",
    "COMPUTE_TYPE",
    "PROTOCOL",
    "NESTED_VIRTUALIZATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModificationResourceEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModificationResourceEnum:
    return cast(ModificationResourceEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ModificationResourceEnum) -> str:
    return value


def deserialize_cbor(data: str) -> ModificationResourceEnum:
    return cast(ModificationResourceEnum, data)
