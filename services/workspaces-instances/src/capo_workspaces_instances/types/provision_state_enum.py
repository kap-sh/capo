"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ProvisionStateEnum``."""

from typing import Literal, TypeAlias, cast

ProvisionStateEnum: TypeAlias = Literal[
    "ALLOCATING",
    "ALLOCATED",
    "DEALLOCATING",
    "DEALLOCATED",
    "ERROR_ALLOCATING",
    "ERROR_DEALLOCATING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProvisionStateEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProvisionStateEnum:
    return cast(ProvisionStateEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisionStateEnum) -> str:
    return value


def deserialize_cbor(data: str) -> ProvisionStateEnum:
    return cast(ProvisionStateEnum, data)
