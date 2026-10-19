"""Generated from Smithy shape ``com.amazonaws.costexplorer#ListSavingsPlansPurchaseRecommendationGenerationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generation_status
    import capo_cost_explorer.types.next_page_token
    import capo_cost_explorer.types.recommendation_id_list
    import capo_cost_explorer.types.recommendations_page_size


class ListSavingsPlansPurchaseRecommendationGenerationRequest(TypedDict, closed=True):
    generation_status: NotRequired[
        "capo_cost_explorer.types.generation_status.GenerationStatus"
    ]
    """<p>The status of the recommendation generation.</p>"""
    recommendation_ids: NotRequired[
        "capo_cost_explorer.types.recommendation_id_list.RecommendationIdList"
    ]
    """<p>The IDs for each specific recommendation.</p>"""
    page_size: NotRequired[
        "capo_cost_explorer.types.recommendations_page_size.RecommendationsPageSize"
    ]
    """<p>The number of recommendations that you want returned in a single response object.</p>"""
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListSavingsPlansPurchaseRecommendationGenerationRequest,
) -> dict:
    out: dict = {}
    if "generation_status" in value:
        import capo_cost_explorer.types.generation_status

        out["GenerationStatus"] = (
            capo_cost_explorer.types.generation_status.serialize_aws_json_1_1(
                value["generation_status"]
            )
        )
    if "recommendation_ids" in value:
        import capo_cost_explorer.types.recommendation_id_list

        out["RecommendationIds"] = (
            capo_cost_explorer.types.recommendation_id_list.serialize_aws_json_1_1(
                value["recommendation_ids"]
            )
        )
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListSavingsPlansPurchaseRecommendationGenerationRequest:
    out: ListSavingsPlansPurchaseRecommendationGenerationRequest = {}  # type: ignore[typeddict-item]
    if data.get("GenerationStatus") is not None:
        import capo_cost_explorer.types.generation_status

        out["generation_status"] = (
            capo_cost_explorer.types.generation_status.deserialize_aws_json_1_1(
                data["GenerationStatus"]
            )
        )
    if data.get("RecommendationIds") is not None:
        import capo_cost_explorer.types.recommendation_id_list

        out["recommendation_ids"] = (
            capo_cost_explorer.types.recommendation_id_list.deserialize_aws_json_1_1(
                data["RecommendationIds"]
            )
        )
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
