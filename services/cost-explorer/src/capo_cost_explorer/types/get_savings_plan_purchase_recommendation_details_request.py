"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetSavingsPlanPurchaseRecommendationDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.recommendation_detail_id


class GetSavingsPlanPurchaseRecommendationDetailsRequest(TypedDict, closed=True):
    recommendation_detail_id: (
        "capo_cost_explorer.types.recommendation_detail_id.RecommendationDetailId"
    )
    """<p>The ID that is associated with the Savings Plan recommendation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetSavingsPlanPurchaseRecommendationDetailsRequest,
) -> dict:
    out: dict = {}
    out["RecommendationDetailId"] = value["recommendation_detail_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetSavingsPlanPurchaseRecommendationDetailsRequest:
    out: GetSavingsPlanPurchaseRecommendationDetailsRequest = {}  # type: ignore[typeddict-item]
    if data.get("RecommendationDetailId") is not None:
        out["recommendation_detail_id"] = data["RecommendationDetailId"]
    else:
        out["recommendation_detail_id"] = ""
    return out
