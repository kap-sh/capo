"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#EventType``."""

from typing import Literal, TypeAlias, cast

"""Event type enumeration"""
EventType: TypeAlias = Literal[
    "SnapshotAndDeleteUnattachedEbsVolume",
    "UpgradeEbsVolumeType",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EventType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EventType:
    return cast(EventType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventType) -> str:
    return value


def deserialize_cbor(data: str) -> EventType:
    return cast(EventType, data)
