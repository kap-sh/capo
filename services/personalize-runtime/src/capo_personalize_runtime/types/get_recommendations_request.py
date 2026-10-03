"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#GetRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize_runtime.types.arn
    import capo_personalize_runtime.types.context
    import capo_personalize_runtime.types.filter_values
    import capo_personalize_runtime.types.item_id
    import capo_personalize_runtime.types.metadata_columns
    import capo_personalize_runtime.types.num_results
    import capo_personalize_runtime.types.promotion_list
    import capo_personalize_runtime.types.user_id


class GetRecommendationsRequest(TypedDict, closed=True):
    campaign_arn: NotRequired["capo_personalize_runtime.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the campaign to use for getting recommendations.</p>"""
    item_id: NotRequired["capo_personalize_runtime.types.item_id.ItemID"]
    """<p>The item ID to provide recommendations for.</p> <p>Required for <code>RELATED_ITEMS</code> recipe type.</p>"""
    user_id: NotRequired["capo_personalize_runtime.types.user_id.UserID"]
    """<p>The user ID to provide recommendations for.</p> <p>Required for <code>USER_PERSONALIZATION</code> recipe type.</p>"""
    num_results: "capo_personalize_runtime.types.num_results.NumResults"
    """<p>The number of results to return. The default is 25. If you are including metadata in recommendations, the maximum is 50. Otherwise, the maximum is 500.</p>"""
    context: NotRequired["capo_personalize_runtime.types.context.Context"]
    """<p>The contextual metadata to use when getting recommendations. Contextual metadata includes any interaction information that might be relevant when getting a user's recommendations, such as the user's current location or device type.</p>"""
    filter_arn: NotRequired["capo_personalize_runtime.types.arn.Arn"]
    """<p>The ARN of the filter to apply to the returned recommendations. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/filter.html">Filtering Recommendations</a>.</p> <p>When using this parameter, be sure the filter resource is <code>ACTIVE</code>.</p>"""
    filter_values: NotRequired[
        "capo_personalize_runtime.types.filter_values.FilterValues"
    ]
    """<p>The values to use when filtering recommendations. For each placeholder parameter in your filter expression, provide the parameter name (in matching case) as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma. </p> <p>For filter expressions that use an <code>INCLUDE</code> element to include items, you must provide values for all parameters that are defined in the expression. For filters with expressions that use an <code>EXCLUDE</code> element to exclude items, you can omit the <code>filter-values</code>.In this case, Amazon Personalize doesn't use that portion of the expression to filter recommendations.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/filter.html">Filtering recommendations and user segments</a>.</p>"""
    recommender_arn: NotRequired["capo_personalize_runtime.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the recommender to use to get recommendations. Provide a recommender ARN if you created a Domain dataset group with a recommender for a domain use case.</p>"""
    promotions: NotRequired[
        "capo_personalize_runtime.types.promotion_list.PromotionList"
    ]
    """<p>The promotions to apply to the recommendation request. A promotion defines additional business rules that apply to a configurable subset of recommended items.</p>"""
    metadata_columns: NotRequired[
        "capo_personalize_runtime.types.metadata_columns.MetadataColumns"
    ]
    """<p>If you enabled metadata in recommendations when you created or updated the campaign or recommender, specify the metadata columns from your Items dataset to include in item recommendations. The map key is <code>ITEMS</code> and the value is a list of column names from your Items dataset. The maximum number of columns you can provide is 10.</p> <p> For information about enabling metadata for a campaign, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-return-metadata">Enabling metadata in recommendations for a campaign</a>. For information about enabling metadata for a recommender, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/creating-recommenders.html#create-recommender-return-metadata">Enabling metadata in recommendations for a recommender</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationsRequest) -> dict:
    out: dict = {}
    if "campaign_arn" in value:
        out["campaignArn"] = value["campaign_arn"]
    if "item_id" in value:
        out["itemId"] = value["item_id"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    out["numResults"] = value.get("num_results", 0)
    if "context" in value:
        import capo_personalize_runtime.types.context

        out["context"] = capo_personalize_runtime.types.context.serialize_json(
            value["context"]
        )
    if "filter_arn" in value:
        out["filterArn"] = value["filter_arn"]
    if "filter_values" in value:
        import capo_personalize_runtime.types.filter_values

        out["filterValues"] = (
            capo_personalize_runtime.types.filter_values.serialize_json(
                value["filter_values"]
            )
        )
    if "recommender_arn" in value:
        out["recommenderArn"] = value["recommender_arn"]
    if "promotions" in value:
        import capo_personalize_runtime.types.promotion_list

        out["promotions"] = (
            capo_personalize_runtime.types.promotion_list.serialize_json(
                value["promotions"]
            )
        )
    if "metadata_columns" in value:
        import capo_personalize_runtime.types.metadata_columns

        out["metadataColumns"] = (
            capo_personalize_runtime.types.metadata_columns.serialize_json(
                value["metadata_columns"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetRecommendationsRequest:
    out: GetRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("campaignArn") is not None:
        out["campaign_arn"] = data["campaignArn"]
    if data.get("itemId") is not None:
        out["item_id"] = data["itemId"]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    if data.get("numResults") is not None:
        out["num_results"] = data["numResults"]
    else:
        out["num_results"] = 0
    if data.get("context") is not None:
        import capo_personalize_runtime.types.context

        out["context"] = capo_personalize_runtime.types.context.deserialize_json(
            data["context"]
        )
    if data.get("filterArn") is not None:
        out["filter_arn"] = data["filterArn"]
    if data.get("filterValues") is not None:
        import capo_personalize_runtime.types.filter_values

        out["filter_values"] = (
            capo_personalize_runtime.types.filter_values.deserialize_json(
                data["filterValues"]
            )
        )
    if data.get("recommenderArn") is not None:
        out["recommender_arn"] = data["recommenderArn"]
    if data.get("promotions") is not None:
        import capo_personalize_runtime.types.promotion_list

        out["promotions"] = (
            capo_personalize_runtime.types.promotion_list.deserialize_json(
                data["promotions"]
            )
        )
    if data.get("metadataColumns") is not None:
        import capo_personalize_runtime.types.metadata_columns

        out["metadata_columns"] = (
            capo_personalize_runtime.types.metadata_columns.deserialize_json(
                data["metadataColumns"]
            )
        )
    return out
