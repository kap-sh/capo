"""Generated from Smithy shape ``com.amazonaws.agentregistry#BatchGetDiscoverableRegistryRecordErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchGetDiscoverableRegistryRecordErrorCode: TypeAlias = Literal[
    "RESOURCE_NOT_FOUND",
    "ACCESS_DENIED",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetDiscoverableRegistryRecordErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetDiscoverableRegistryRecordErrorCode:
    return cast(BatchGetDiscoverableRegistryRecordErrorCode, data)
