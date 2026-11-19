"""Generated from Smithy shape ``com.amazonaws.guardduty#RecommendationCategory``."""

from typing import Literal, TypeAlias, cast

RecommendationCategory: TypeAlias = Literal[
    "ENABLE_PROTECTION",
    "FURTHER_INVESTIGATION",
    "SUPPRESSION_RULE",
    "HARDENING",
    "MONITORING",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationCategory) -> str:
    return value


def deserialize_json(data: str) -> RecommendationCategory:
    return cast(RecommendationCategory, data)
