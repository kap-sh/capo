"""Generated from Smithy shape ``com.amazonaws.guardduty#Recommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.recommendation

Recommendations: TypeAlias = list["capo_guardduty.types.recommendation.Recommendation"]


# --- restJson1 ser/de ---
def serialize_json(value: Recommendations) -> list:
    import capo_guardduty.types.recommendation

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.recommendation.serialize_json(item))
    return out


def deserialize_json(data: list) -> Recommendations:
    import capo_guardduty.types.recommendation

    out: Recommendations = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.recommendation.deserialize_json(item))
    return out
