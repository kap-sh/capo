"""Generated from Smithy shape ``com.amazonaws.inspector2#OnDemandScanStatusReason``."""

from typing import Literal, TypeAlias, cast

OnDemandScanStatusReason: TypeAlias = Literal[
    "ACCESS_DENIED",
    "INTERNAL_ERROR",
    "STORAGE_LIMIT_EXCEEDED",
    "EXTRACTION_COLLECTION_TIME_LIMIT_EXCEEDED",
    "UNSUPPORTED_OS",
    "RESOURCE_TERMINATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OnDemandScanStatusReason) -> str:
    return value


def deserialize_json(data: str) -> OnDemandScanStatusReason:
    return cast(OnDemandScanStatusReason, data)
