"""Generated from Smithy shape ``com.amazonaws.wellarchitected#FeedbackCategory``."""

from typing import Literal, TypeAlias, cast

"""<p>A category that classifies the specific nature of recommendation feedback. Used to provide structured feedback that the recommendation engine can act upon in subsequent generation cycles.</p>"""
FeedbackCategory: TypeAlias = Literal[
    "OTHER",
    "RECOMMENDATION_NOT_RELEVANT",
    "RESOURCE_NOT_IMPORTANT",
    "RESOURCE_TYPE_NOT_IMPORTANT",
    "RECOMMENDATION_INCORRECT",
]


# --- restJson1 ser/de ---
def serialize_json(value: FeedbackCategory) -> str:
    return value


def deserialize_json(data: str) -> FeedbackCategory:
    return cast(FeedbackCategory, data)
