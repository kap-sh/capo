"""Generated from Smithy shape ``com.amazonaws.workspaces#DedicatedTenancySupportEnum``."""

from typing import Literal, TypeAlias, cast

DedicatedTenancySupportEnum: TypeAlias = Literal["ENABLED",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DedicatedTenancySupportEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DedicatedTenancySupportEnum:
    return cast(DedicatedTenancySupportEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DedicatedTenancySupportEnum) -> str:
    return value


def deserialize_cbor(data: str) -> DedicatedTenancySupportEnum:
    return cast(DedicatedTenancySupportEnum, data)
