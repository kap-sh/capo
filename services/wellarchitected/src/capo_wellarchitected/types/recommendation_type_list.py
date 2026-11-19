"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RecommendationTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.recommendation_type

RecommendationTypeList: TypeAlias = list[
    "capo_wellarchitected.types.recommendation_type.RecommendationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationTypeList) -> list:
    import capo_wellarchitected.types.recommendation_type

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.recommendation_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommendationTypeList:
    import capo_wellarchitected.types.recommendation_type

    out: RecommendationTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wellarchitected.types.recommendation_type.deserialize_json(item)
        )
    return out
