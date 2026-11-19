"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RecommendationType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of a recommendation.</p>"""
RecommendationType: TypeAlias = Literal[
    "RESOURCE",
    "ARCHITECTURE",
    "APPLICATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationType) -> str:
    return value


def deserialize_json(data: str) -> RecommendationType:
    return cast(RecommendationType, data)
