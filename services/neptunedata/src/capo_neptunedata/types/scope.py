"""Generated from Smithy shape ``com.amazonaws.neptunedata#Scope``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the scope of the storage rebuild operation.</p>"""
Scope: TypeAlias = Literal[
    "ALL",
    "QUADS",
    "DICTIONARIES",
]


# --- restJson1 ser/de ---
def serialize_json(value: Scope) -> str:
    return value


def deserialize_json(data: str) -> Scope:
    return cast(Scope, data)
