"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GenerationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a recommendation generation process.</p>"""
GenerationStatus: TypeAlias = Literal[
    "QUEUED",
    "IN_PROGRESS",
    "COMPLETED",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: GenerationStatus) -> str:
    return value


def deserialize_json(data: str) -> GenerationStatus:
    return cast(GenerationStatus, data)
