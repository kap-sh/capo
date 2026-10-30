"""Generated from Smithy shape ``com.amazonaws.continuum#PatchFormat``."""

from typing import Literal, TypeAlias, cast

"""How a patch is encoded, which determines the command that applies it."""
PatchFormat: TypeAlias = Literal[
    "GIT_MAILBOX_PATCH",
    "GIT_BINARY_DIFF",
    "GIT_DIFF",
]


# --- restJson1 ser/de ---
def serialize_json(value: PatchFormat) -> str:
    return value


def deserialize_json(data: str) -> PatchFormat:
    return cast(PatchFormat, data)
