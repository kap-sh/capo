"""Generated from Smithy shape ``com.amazonaws.codeconnections#SyncConfigurationType``."""

from typing import Literal, TypeAlias, cast

SyncConfigurationType: TypeAlias = Literal["CFN_STACK_SYNC",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncConfigurationType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SyncConfigurationType:
    return cast(SyncConfigurationType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SyncConfigurationType) -> str:
    return value


def deserialize_cbor(data: str) -> SyncConfigurationType:
    return cast(SyncConfigurationType, data)
