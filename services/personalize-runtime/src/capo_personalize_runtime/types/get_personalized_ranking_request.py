"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#GetPersonalizedRankingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_personalize_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize_runtime.types.arn
    import capo_personalize_runtime.types.context
    import capo_personalize_runtime.types.filter_values
    import capo_personalize_runtime.types.input_list
    import capo_personalize_runtime.types.metadata_columns
    import capo_personalize_runtime.types.user_id


class GetPersonalizedRankingRequest(TypedDict, closed=True):
    campaign_arn: "capo_personalize_runtime.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the campaign to use for generating the personalized ranking.</p>"""
    input_list: "capo_personalize_runtime.types.input_list.InputList"
    """<p>A list of items (by <code>itemId</code>) to rank. If an item was not included in the training dataset, the item is appended to the end of the reranked list. If you are including metadata in recommendations, the maximum is 50. Otherwise, the maximum is 500.</p>"""
    user_id: "capo_personalize_runtime.types.user_id.UserID"
    """<p>The user for which you want the campaign to provide a personalized ranking.</p>"""
    context: NotRequired["capo_personalize_runtime.types.context.Context"]
    """<p>The contextual metadata to use when getting recommendations. Contextual metadata includes any interaction information that might be relevant when getting a user's recommendations, such as the user's current location or device type.</p>"""
    filter_arn: NotRequired["capo_personalize_runtime.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of a filter you created to include items or exclude items from recommendations for a given user. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/filter.html">Filtering Recommendations</a>.</p>"""
    filter_values: NotRequired[
        "capo_personalize_runtime.types.filter_values.FilterValues"
    ]
    """<p>The values to use when filtering recommendations. For each placeholder parameter in your filter expression, provide the parameter name (in matching case) as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma. </p> <p>For filter expressions that use an <code>INCLUDE</code> element to include items, you must provide values for all parameters that are defined in the expression. For filters with expressions that use an <code>EXCLUDE</code> element to exclude items, you can omit the <code>filter-values</code>.In this case, Amazon Personalize doesn't use that portion of the expression to filter recommendations.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/filter.html">Filtering Recommendations</a>.</p>"""
    metadata_columns: NotRequired[
        "capo_personalize_runtime.types.metadata_columns.MetadataColumns"
    ]
    """<p>If you enabled metadata in recommendations when you created or updated the campaign, specify metadata columns from your Items dataset to include in the personalized ranking. The map key is <code>ITEMS</code> and the value is a list of column names from your Items dataset. The maximum number of columns you can provide is 10.</p> <p> For information about enabling metadata for a campaign, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-return-metadata">Enabling metadata in recommendations for a campaign</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPersonalizedRankingRequest) -> dict:
    out: dict = {}
    out["campaignArn"] = value["campaign_arn"]
    import capo_personalize_runtime.types.input_list

    out["inputList"] = capo_personalize_runtime.types.input_list.serialize_json(
        value["input_list"]
    )
    out["userId"] = value["user_id"]
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
    if "metadata_columns" in value:
        import capo_personalize_runtime.types.metadata_columns

        out["metadataColumns"] = (
            capo_personalize_runtime.types.metadata_columns.serialize_json(
                value["metadata_columns"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPersonalizedRankingRequest:
    out: GetPersonalizedRankingRequest = {}  # type: ignore[typeddict-item]
    if data.get("campaignArn") is not None:
        out["campaign_arn"] = data["campaignArn"]
    else:
        raise DeserializationError(
            "GetPersonalizedRankingRequest.campaign_arn required"
        )
    if data.get("inputList") is not None:
        import capo_personalize_runtime.types.input_list

        out["input_list"] = capo_personalize_runtime.types.input_list.deserialize_json(
            data["inputList"]
        )
    else:
        raise DeserializationError("GetPersonalizedRankingRequest.input_list required")
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("GetPersonalizedRankingRequest.user_id required")
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
    if data.get("metadataColumns") is not None:
        import capo_personalize_runtime.types.metadata_columns

        out["metadata_columns"] = (
            capo_personalize_runtime.types.metadata_columns.deserialize_json(
                data["metadataColumns"]
            )
        )
    return out
