"""Generated from Smithy shape ``com.amazonaws.devopsagent#ChatArchiveStatus``."""

from typing import Literal, TypeAlias, cast

ChatArchiveStatus: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChatArchiveStatus) -> str:
    return value


def deserialize_json(data: str) -> ChatArchiveStatus:
    return cast(ChatArchiveStatus, data)
