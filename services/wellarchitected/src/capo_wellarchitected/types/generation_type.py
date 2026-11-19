"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GenerationType``."""

from typing import Literal, TypeAlias, cast

"""<p>How a recommendation generation was started.</p>"""
GenerationType: TypeAlias = Literal[
    "ONDEMAND",
    "SCHEDULED",
    "BASIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: GenerationType) -> str:
    return value


def deserialize_json(data: str) -> GenerationType:
    return cast(GenerationType, data)
