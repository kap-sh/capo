"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Priority``."""

from typing import Literal, TypeAlias, cast

"""<p>The priority of a recommendation.</p>"""
Priority: TypeAlias = Literal[
    "HIGH",
    "MEDIUM",
    "LOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: Priority) -> str:
    return value


def deserialize_json(data: str) -> Priority:
    return cast(Priority, data)
