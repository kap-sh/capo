"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RecommendationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a recommendation.</p>"""
RecommendationStatus: TypeAlias = Literal[
    "ACTIVE",
    "SUPPRESSED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommendationStatus:
    return cast(RecommendationStatus, data)
