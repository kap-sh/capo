"""Generated from Smithy shape ``com.amazonaws.guardduty#Disposition``."""

from typing import Literal, TypeAlias, cast

Disposition: TypeAlias = Literal[
    "Isolated",
    "Blocked",
    "Deleted",
    "Access Revoked",
    "Logged",
]


# --- restJson1 ser/de ---
def serialize_json(value: Disposition) -> str:
    return value


def deserialize_json(data: str) -> Disposition:
    return cast(Disposition, data)
