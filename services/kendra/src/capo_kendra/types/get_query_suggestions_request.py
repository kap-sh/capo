"""Generated from Smithy shape ``com.amazonaws.kendra#GetQuerySuggestionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.attribute_suggestions_get_config
    import capo_kendra.types.index_id
    import capo_kendra.types.integer
    import capo_kendra.types.suggestion_query_text
    import capo_kendra.types.suggestion_types


class GetQuerySuggestionsRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index you want to get query suggestions from.</p>"""
    query_text: "capo_kendra.types.suggestion_query_text.SuggestionQueryText"
    """<p>The text of a user's query to generate query suggestions.</p> <p>A query is suggested if the query prefix matches what a user starts to type as their query.</p> <p>Amazon Kendra does not show any suggestions if a user types fewer than two characters or more than 60 characters. A query must also have at least one search result and contain at least one word of more than four characters.</p>"""
    max_suggestions_count: NotRequired["capo_kendra.types.integer.Integer"]
    """<p>The maximum number of query suggestions you want to show to your users.</p>"""
    suggestion_types: NotRequired["capo_kendra.types.suggestion_types.SuggestionTypes"]
    """<p>The suggestions type to base query suggestions on. The suggestion types are query history or document fields/attributes. You can set one type or the other.</p> <p>If you set query history as your suggestions type, Amazon Kendra suggests queries relevant to your users based on popular queries in the query history.</p> <p>If you set document fields/attributes as your suggestions type, Amazon Kendra suggests queries relevant to your users based on the contents of document fields.</p>"""
    attribute_suggestions_config: NotRequired[
        "capo_kendra.types.attribute_suggestions_get_config.AttributeSuggestionsGetConfig"
    ]
    """<p>Configuration information for the document fields/attributes that you want to base query suggestions on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQuerySuggestionsRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["QueryText"] = value["query_text"]
    if "max_suggestions_count" in value:
        out["MaxSuggestionsCount"] = value["max_suggestions_count"]
    if "suggestion_types" in value:
        import capo_kendra.types.suggestion_types

        out["SuggestionTypes"] = (
            capo_kendra.types.suggestion_types.serialize_aws_json_1_1(
                value["suggestion_types"]
            )
        )
    if "attribute_suggestions_config" in value:
        import capo_kendra.types.attribute_suggestions_get_config

        out["AttributeSuggestionsConfig"] = (
            capo_kendra.types.attribute_suggestions_get_config.serialize_aws_json_1_1(
                value["attribute_suggestions_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQuerySuggestionsRequest:
    out: GetQuerySuggestionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        out["index_id"] = ""
    if data.get("QueryText") is not None:
        out["query_text"] = data["QueryText"]
    else:
        out["query_text"] = ""
    if data.get("MaxSuggestionsCount") is not None:
        out["max_suggestions_count"] = data["MaxSuggestionsCount"]
    if data.get("SuggestionTypes") is not None:
        import capo_kendra.types.suggestion_types

        out["suggestion_types"] = (
            capo_kendra.types.suggestion_types.deserialize_aws_json_1_1(
                data["SuggestionTypes"]
            )
        )
    if data.get("AttributeSuggestionsConfig") is not None:
        import capo_kendra.types.attribute_suggestions_get_config

        out["attribute_suggestions_config"] = (
            capo_kendra.types.attribute_suggestions_get_config.deserialize_aws_json_1_1(
                data["AttributeSuggestionsConfig"]
            )
        )
    return out
