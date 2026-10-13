"""Generated from Smithy shape ``com.amazonaws.qconnect#RecommendationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.recommendation_data

RecommendationList: TypeAlias = list[
    "capo_qconnect.types.recommendation_data.RecommendationData"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationList) -> list:
    import capo_qconnect.types.recommendation_data

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.recommendation_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommendationList:
    import capo_qconnect.types.recommendation_data

    out: RecommendationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.recommendation_data.deserialize_json(item))
    return out


def redact_sensitive(value: RecommendationList) -> list[Any]:
    import capo_qconnect.types.recommendation_data

    return [
        capo_qconnect.types.recommendation_data.redact_sensitive(item) for item in value
    ]
