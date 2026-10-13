"""Generated from Smithy shape ``com.amazonaws.pi#RecommendationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.recommendation

RecommendationList: TypeAlias = list["capo_pi.types.recommendation.Recommendation"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationList) -> list:
    import capo_pi.types.recommendation

    out: list = []
    for item in value:
        out.append(capo_pi.types.recommendation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RecommendationList:
    import capo_pi.types.recommendation

    out: RecommendationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.recommendation.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: RecommendationList) -> list[Any]:
    import capo_pi.types.recommendation

    return [capo_pi.types.recommendation.redact_sensitive(item) for item in value]
