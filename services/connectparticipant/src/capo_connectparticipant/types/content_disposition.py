"""Generated from Smithy shape ``com.amazonaws.connectparticipant#ContentDisposition``."""

from typing import Literal, TypeAlias, cast

ContentDisposition: TypeAlias = Literal[
    "INLINE",
    "ATTACHMENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentDisposition) -> str:
    return value


def deserialize_json(data: str) -> ContentDisposition:
    return cast(ContentDisposition, data)
