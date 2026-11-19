"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RecommendationItemType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of a recommendation item.</p>"""
RecommendationItemType: TypeAlias = Literal[
    "AWS_RESOURCE",
    "RECOMMENDATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationItemType) -> str:
    return value


def deserialize_json(data: str) -> RecommendationItemType:
    return cast(RecommendationItemType, data)
