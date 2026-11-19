"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of a profile.</p>"""
ProfileType: TypeAlias = Literal[
    "STANDARD",
    "BASIC",
    "ORGANIZATIONAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileType) -> str:
    return value


def deserialize_json(data: str) -> ProfileType:
    return cast(ProfileType, data)
