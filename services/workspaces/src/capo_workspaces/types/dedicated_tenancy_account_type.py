"""Generated from Smithy shape ``com.amazonaws.workspaces#DedicatedTenancyAccountType``."""

from typing import Literal, TypeAlias, cast

DedicatedTenancyAccountType: TypeAlias = Literal[
    "SOURCE_ACCOUNT",
    "TARGET_ACCOUNT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DedicatedTenancyAccountType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DedicatedTenancyAccountType:
    return cast(DedicatedTenancyAccountType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DedicatedTenancyAccountType) -> str:
    return value


def deserialize_cbor(data: str) -> DedicatedTenancyAccountType:
    return cast(DedicatedTenancyAccountType, data)
