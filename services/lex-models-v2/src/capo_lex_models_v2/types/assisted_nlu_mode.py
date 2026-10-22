"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AssistedNluMode``."""

from typing import Literal, TypeAlias, cast

"""<p>Defines the operational mode for Assisted Natural Language Understanding. This enum determines how the enhanced NLU capabilities integrate with standard intent recognition.</p>"""
AssistedNluMode: TypeAlias = Literal[
    "Primary",
    "Fallback",
    "DialogManager",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssistedNluMode) -> str:
    return value


def deserialize_json(data: str) -> AssistedNluMode:
    return cast(AssistedNluMode, data)
