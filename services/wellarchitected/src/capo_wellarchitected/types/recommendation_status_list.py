"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RecommendationStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.recommendation_status

RecommendationStatusList: TypeAlias = list[
    "capo_wellarchitected.types.recommendation_status.RecommendationStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationStatusList) -> list:
    import capo_wellarchitected.types.recommendation_status

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.recommendation_status.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RecommendationStatusList:
    import capo_wellarchitected.types.recommendation_status

    out: RecommendationStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wellarchitected.types.recommendation_status.deserialize_json(item)
        )
    return out
