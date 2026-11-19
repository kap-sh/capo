"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GenerationRecommendationTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.recommendation_type

GenerationRecommendationTypes: TypeAlias = list[
    "capo_wellarchitected.types.recommendation_type.RecommendationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: GenerationRecommendationTypes) -> list:
    import capo_wellarchitected.types.recommendation_type

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.recommendation_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> GenerationRecommendationTypes:
    import capo_wellarchitected.types.recommendation_type

    out: GenerationRecommendationTypes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wellarchitected.types.recommendation_type.deserialize_json(item)
        )
    return out
