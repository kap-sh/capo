"""Generated from Smithy shape ``com.amazonaws.qconnect#RecommendationTriggerList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.recommendation_trigger

RecommendationTriggerList: TypeAlias = list[
    "capo_qconnect.types.recommendation_trigger.RecommendationTrigger"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationTriggerList) -> list:
    import capo_qconnect.types.recommendation_trigger

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.recommendation_trigger.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommendationTriggerList:
    import capo_qconnect.types.recommendation_trigger

    out: RecommendationTriggerList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.recommendation_trigger.deserialize_json(item))
    return out


def redact_sensitive(value: RecommendationTriggerList) -> list[Any]:
    import capo_qconnect.types.recommendation_trigger

    return [
        capo_qconnect.types.recommendation_trigger.redact_sensitive(item)
        for item in value
    ]
