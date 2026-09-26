"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#WAFConflictResolutionOptions``."""

from typing import Literal, TypeAlias, cast

WAFConflictResolutionOptions: TypeAlias = Literal["MERGE_WHERE_APPLICABLE",]


# --- restJson1 ser/de ---
def serialize_json(value: WAFConflictResolutionOptions) -> str:
    return value


def deserialize_json(data: str) -> WAFConflictResolutionOptions:
    return cast(WAFConflictResolutionOptions, data)
