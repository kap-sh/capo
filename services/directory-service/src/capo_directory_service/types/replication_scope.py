"""Generated from Smithy shape ``com.amazonaws.directoryservice#ReplicationScope``."""

from typing import Literal, TypeAlias, cast

ReplicationScope: TypeAlias = Literal["Domain",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplicationScope:
    return cast(ReplicationScope, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReplicationScope) -> str:
    return value


def deserialize_cbor(data: str) -> ReplicationScope:
    return cast(ReplicationScope, data)
