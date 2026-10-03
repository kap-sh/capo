"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#PredictedItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize_runtime.types.item_id
    import capo_personalize_runtime.types.metadata
    import capo_personalize_runtime.types.name
    import capo_personalize_runtime.types.reason_list
    import capo_personalize_runtime.types.score


class PredictedItem(TypedDict, closed=True):
    item_id: NotRequired["capo_personalize_runtime.types.item_id.ItemID"]
    """<p>The recommended item ID.</p>"""
    score: NotRequired["capo_personalize_runtime.types.score.Score"]
    """<p>A numeric representation of the model's certainty that the item will be the next user selection. For more information on scoring logic, see <a>how-scores-work</a>.</p>"""
    promotion_name: NotRequired["capo_personalize_runtime.types.name.Name"]
    """<p>The name of the promotion that included the predicted item.</p>"""
    metadata: NotRequired["capo_personalize_runtime.types.metadata.Metadata"]
    """<p>Metadata about the item from your Items dataset.</p>"""
    reason: NotRequired["capo_personalize_runtime.types.reason_list.ReasonList"]
    """<p>If you use User-Personalization-v2, a list of reasons for why the item was included in recommendations. Possible reasons include the following:</p> <ul> <li> <p>Promoted item - Indicates the item was included as part of a promotion that you applied in your recommendation request.</p> </li> <li> <p>Exploration - Indicates the item was included with exploration. With exploration, recommendations include items with less interactions data or relevance for the user. For more information about exploration, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/use-case-recipe-features.html#about-exploration">Exploration</a>.</p> </li> <li> <p> Popular item - Indicates the item was included as a placeholder popular item. If you use a filter, depending on how many recommendations the filter removes, Amazon Personalize might add placeholder items to meet the <code>numResults</code> for your recommendation request. These items are popular items, based on interactions data, that satisfy your filter criteria. They don't have a relevance score for the user. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: PredictedItem) -> dict:
    out: dict = {}
    if "item_id" in value:
        out["itemId"] = value["item_id"]
    if "score" in value:
        out["score"] = (
            "NaN"
            if value["score"] != value["score"]
            else "Infinity"
            if value["score"] == float("inf")
            else "-Infinity"
            if value["score"] == float("-inf")
            else value["score"]
        )
    if "promotion_name" in value:
        out["promotionName"] = value["promotion_name"]
    if "metadata" in value:
        import capo_personalize_runtime.types.metadata

        out["metadata"] = capo_personalize_runtime.types.metadata.serialize_json(
            value["metadata"]
        )
    if "reason" in value:
        import capo_personalize_runtime.types.reason_list

        out["reason"] = capo_personalize_runtime.types.reason_list.serialize_json(
            value["reason"]
        )
    return out


def deserialize_json(data: dict) -> PredictedItem:
    out: PredictedItem = {}  # type: ignore[typeddict-item]
    if data.get("itemId") is not None:
        out["item_id"] = data["itemId"]
    if data.get("score") is not None:
        out["score"] = float(data["score"])
    if data.get("promotionName") is not None:
        out["promotion_name"] = data["promotionName"]
    if data.get("metadata") is not None:
        import capo_personalize_runtime.types.metadata

        out["metadata"] = capo_personalize_runtime.types.metadata.deserialize_json(
            data["metadata"]
        )
    if data.get("reason") is not None:
        import capo_personalize_runtime.types.reason_list

        out["reason"] = capo_personalize_runtime.types.reason_list.deserialize_json(
            data["reason"]
        )
    return out
