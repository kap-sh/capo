"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#BatchUpdateRecommendationResourceExclusionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.update_recommendation_resource_exclusion_error_list


class BatchUpdateRecommendationResourceExclusionResponse(TypedDict, closed=True):
    batch_update_recommendation_resource_exclusion_errors: "capo_trustedadvisor.types.update_recommendation_resource_exclusion_error_list.UpdateRecommendationResourceExclusionErrorList"
    """<p>A list of recommendation resource ARNs whose exclusion status failed to update, if any</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateRecommendationResourceExclusionResponse) -> dict:
    out: dict = {}
    import capo_trustedadvisor.types.update_recommendation_resource_exclusion_error_list

    out["batchUpdateRecommendationResourceExclusionErrors"] = (
        capo_trustedadvisor.types.update_recommendation_resource_exclusion_error_list.serialize_json(
            value["batch_update_recommendation_resource_exclusion_errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateRecommendationResourceExclusionResponse:
    out: BatchUpdateRecommendationResourceExclusionResponse = {}  # type: ignore[typeddict-item]
    if data.get("batchUpdateRecommendationResourceExclusionErrors") is not None:
        import capo_trustedadvisor.types.update_recommendation_resource_exclusion_error_list

        out["batch_update_recommendation_resource_exclusion_errors"] = (
            capo_trustedadvisor.types.update_recommendation_resource_exclusion_error_list.deserialize_json(
                data["batchUpdateRecommendationResourceExclusionErrors"]
            )
        )
    else:
        out["batch_update_recommendation_resource_exclusion_errors"] = []
    return out
