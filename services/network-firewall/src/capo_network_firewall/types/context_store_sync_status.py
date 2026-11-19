"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ContextStoreSyncStatus``."""

from typing import Literal, TypeAlias, cast

ContextStoreSyncStatus: TypeAlias = Literal[
    "SYNCING",
    "PARTIALLY_RESOLVED",
    "FULLY_RESOLVED",
    "SYNC_FAILED",
    "UNRESOLVED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContextStoreSyncStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ContextStoreSyncStatus:
    return cast(ContextStoreSyncStatus, data)
