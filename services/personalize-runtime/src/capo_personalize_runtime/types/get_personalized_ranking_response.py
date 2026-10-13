"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#GetPersonalizedRankingResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize_runtime.types.item_list
    import capo_personalize_runtime.types.recommendation_id


class GetPersonalizedRankingResponse(TypedDict, closed=True):
    personalized_ranking: NotRequired[
        "capo_personalize_runtime.types.item_list.ItemList"
    ]
    """<p>A list of items in order of most likely interest to the user. The maximum is 500.</p>"""
    recommendation_id: NotRequired[
        "capo_personalize_runtime.types.recommendation_id.RecommendationID"
    ]
    """<p>The ID of the recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPersonalizedRankingResponse) -> dict:
    out: dict = {}
    if "personalized_ranking" in value:
        import capo_personalize_runtime.types.item_list

        out["personalizedRanking"] = (
            capo_personalize_runtime.types.item_list.serialize_json(
                value["personalized_ranking"]
            )
        )
    if "recommendation_id" in value:
        out["recommendationId"] = value["recommendation_id"]
    return out


def deserialize_json(data: dict) -> GetPersonalizedRankingResponse:
    out: GetPersonalizedRankingResponse = {}  # type: ignore[typeddict-item]
    if data.get("personalizedRanking") is not None:
        import capo_personalize_runtime.types.item_list

        out["personalized_ranking"] = (
            capo_personalize_runtime.types.item_list.deserialize_json(
                data["personalizedRanking"]
            )
        )
    if data.get("recommendationId") is not None:
        out["recommendation_id"] = data["recommendationId"]
    return out


def redact_sensitive(value: GetPersonalizedRankingResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "personalized_ranking" in value:
        import capo_personalize_runtime.types.item_list

        out["personalized_ranking"] = (
            capo_personalize_runtime.types.item_list.redact_sensitive(
                value["personalized_ranking"]
            )
        )
    return out
