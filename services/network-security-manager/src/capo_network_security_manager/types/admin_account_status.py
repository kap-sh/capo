"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AdminAccountStatus``."""

from typing import Literal, TypeAlias, cast

AdminAccountStatus: TypeAlias = Literal[
    "ONBOARDED",
    "OFFBOARDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AdminAccountStatus) -> str:
    return value


def deserialize_json(data: str) -> AdminAccountStatus:
    return cast(AdminAccountStatus, data)
