"""Generated from Smithy shape ``com.amazonaws.qconnect#ProfileRecommendations``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.profile_recommendation

ProfileRecommendations: TypeAlias = list[
    "capo_qconnect.types.profile_recommendation.ProfileRecommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileRecommendations) -> list:
    import capo_qconnect.types.profile_recommendation

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.profile_recommendation.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProfileRecommendations:
    import capo_qconnect.types.profile_recommendation

    out: ProfileRecommendations = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.profile_recommendation.deserialize_json(item))
    return out


def redact_sensitive(value: ProfileRecommendations) -> list[Any]:
    import capo_qconnect.types.profile_recommendation

    return [
        capo_qconnect.types.profile_recommendation.redact_sensitive(item)
        for item in value
    ]
