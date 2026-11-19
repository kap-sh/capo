"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RecommendationState``."""

from typing import Literal, TypeAlias, cast

"""<p>The state of a recommendation.</p>"""
RecommendationState: TypeAlias = Literal[
    "OPEN",
    "CLOSED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationState) -> str:
    return value


def deserialize_json(data: str) -> RecommendationState:
    return cast(RecommendationState, data)
