"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#BatchUpdateRecommendationResourceExclusionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.recommendation_resource_exclusion_list


class BatchUpdateRecommendationResourceExclusionRequest(TypedDict, closed=True):
    recommendation_resource_exclusions: "capo_trustedadvisor.types.recommendation_resource_exclusion_list.RecommendationResourceExclusionList"
    """<p>A list of recommendation resource ARNs and exclusion status to update</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateRecommendationResourceExclusionRequest) -> dict:
    out: dict = {}
    import capo_trustedadvisor.types.recommendation_resource_exclusion_list

    out["recommendationResourceExclusions"] = (
        capo_trustedadvisor.types.recommendation_resource_exclusion_list.serialize_json(
            value["recommendation_resource_exclusions"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateRecommendationResourceExclusionRequest:
    out: BatchUpdateRecommendationResourceExclusionRequest = {}  # type: ignore[typeddict-item]
    if data.get("recommendationResourceExclusions") is not None:
        import capo_trustedadvisor.types.recommendation_resource_exclusion_list

        out["recommendation_resource_exclusions"] = (
            capo_trustedadvisor.types.recommendation_resource_exclusion_list.deserialize_json(
                data["recommendationResourceExclusions"]
            )
        )
    else:
        out["recommendation_resource_exclusions"] = []
    return out
