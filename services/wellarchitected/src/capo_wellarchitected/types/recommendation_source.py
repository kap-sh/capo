"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RecommendationSource``."""

from typing import Literal, TypeAlias, cast

"""<p>The origin system that produced a recommendation.</p>"""
RecommendationSource: TypeAlias = Literal[
    "TRUSTED_ADVISOR",
    "COST_EXPLORER",
    "CLOUDWATCH",
    "WELL_ARCHITECTED_TOOL",
    "WELL_ARCHITECTED_AGENT",
    "CUSTOMER_IAC",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationSource) -> str:
    return value


def deserialize_json(data: str) -> RecommendationSource:
    return cast(RecommendationSource, data)
