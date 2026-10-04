"""Generated from Smithy shape ``com.amazonaws.guardduty#ManagedBy``."""

from typing import Literal, TypeAlias, cast

ManagedBy: TypeAlias = Literal["GUARDDUTY_POLICY",]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedBy) -> str:
    return value


def deserialize_json(data: str) -> ManagedBy:
    return cast(ManagedBy, data)
