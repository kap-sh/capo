"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationResourceExclusion``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.recommendation_resource_arn


class RecommendationResourceExclusion(TypedDict, closed=True):
    arn: "capo_trustedadvisor.types.recommendation_resource_arn.RecommendationResourceArn"
    """<p>The ARN of the Recommendation Resource</p>"""
    is_excluded: "bool"
    """<p>The exclusion status</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationResourceExclusion) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["isExcluded"] = value["is_excluded"]
    return out


def deserialize_json(data: dict) -> RecommendationResourceExclusion:
    out: RecommendationResourceExclusion = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("isExcluded") is not None:
        out["is_excluded"] = data["isExcluded"]
    else:
        out["is_excluded"] = False
    return out
