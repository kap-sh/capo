"""Generated from Smithy shape ``com.amazonaws.kendra#QueryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.facet_result_list
    import capo_kendra.types.featured_results_item_list
    import capo_kendra.types.integer
    import capo_kendra.types.query_id
    import capo_kendra.types.query_result_item_list
    import capo_kendra.types.spell_corrected_query_list
    import capo_kendra.types.warning_list


class QueryResult(TypedDict, closed=True):
    query_id: NotRequired["capo_kendra.types.query_id.QueryId"]
    """<p>The identifier for the search. You also use <code>QueryId</code> to identify the search when using the <a href="https://docs.aws.amazon.com/kendra/latest/APIReference/API_SubmitFeedback.html">SubmitFeedback</a> API.</p>"""
    result_items: NotRequired[
        "capo_kendra.types.query_result_item_list.QueryResultItemList"
    ]
    """<p>The results of the search.</p>"""
    facet_results: NotRequired["capo_kendra.types.facet_result_list.FacetResultList"]
    """<p>Contains the facet results. A <code>FacetResult</code> contains the counts for each field/attribute key that was specified in the <code>Facets</code> input parameter.</p>"""
    total_number_of_results: NotRequired["capo_kendra.types.integer.Integer"]
    """<p>The total number of items found by the search. However, you can only retrieve up to 100 items. For example, if the search found 192 items, you can only retrieve the first 100 of the items.</p>"""
    warnings: NotRequired["capo_kendra.types.warning_list.WarningList"]
    """<p>A list of warning codes and their messages on problems with your query.</p> <p>Amazon Kendra currently only supports one type of warning, which is a warning on invalid syntax used in the query. For examples of invalid query syntax, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/searching-example.html#searching-index-query-syntax">Searching with advanced query syntax</a>.</p>"""
    spell_corrected_queries: NotRequired[
        "capo_kendra.types.spell_corrected_query_list.SpellCorrectedQueryList"
    ]
    """<p>A list of information related to suggested spell corrections for a query.</p>"""
    featured_results_items: NotRequired[
        "capo_kendra.types.featured_results_item_list.FeaturedResultsItemList"
    ]
    """<p>The list of featured result items. Featured results are displayed at the top of the search results page, placed above all other results for certain queries. If there's an exact match of a query, then certain documents are featured in the search results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryResult) -> dict:
    out: dict = {}
    if "query_id" in value:
        out["QueryId"] = value["query_id"]
    if "result_items" in value:
        import capo_kendra.types.query_result_item_list

        out["ResultItems"] = (
            capo_kendra.types.query_result_item_list.serialize_aws_json_1_1(
                value["result_items"]
            )
        )
    if "facet_results" in value:
        import capo_kendra.types.facet_result_list

        out["FacetResults"] = (
            capo_kendra.types.facet_result_list.serialize_aws_json_1_1(
                value["facet_results"]
            )
        )
    if "total_number_of_results" in value:
        out["TotalNumberOfResults"] = value["total_number_of_results"]
    if "warnings" in value:
        import capo_kendra.types.warning_list

        out["Warnings"] = capo_kendra.types.warning_list.serialize_aws_json_1_1(
            value["warnings"]
        )
    if "spell_corrected_queries" in value:
        import capo_kendra.types.spell_corrected_query_list

        out["SpellCorrectedQueries"] = (
            capo_kendra.types.spell_corrected_query_list.serialize_aws_json_1_1(
                value["spell_corrected_queries"]
            )
        )
    if "featured_results_items" in value:
        import capo_kendra.types.featured_results_item_list

        out["FeaturedResultsItems"] = (
            capo_kendra.types.featured_results_item_list.serialize_aws_json_1_1(
                value["featured_results_items"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryResult:
    out: QueryResult = {}  # type: ignore[typeddict-item]
    if data.get("QueryId") is not None:
        out["query_id"] = data["QueryId"]
    if data.get("ResultItems") is not None:
        import capo_kendra.types.query_result_item_list

        out["result_items"] = (
            capo_kendra.types.query_result_item_list.deserialize_aws_json_1_1(
                data["ResultItems"]
            )
        )
    if data.get("FacetResults") is not None:
        import capo_kendra.types.facet_result_list

        out["facet_results"] = (
            capo_kendra.types.facet_result_list.deserialize_aws_json_1_1(
                data["FacetResults"]
            )
        )
    if data.get("TotalNumberOfResults") is not None:
        out["total_number_of_results"] = data["TotalNumberOfResults"]
    if data.get("Warnings") is not None:
        import capo_kendra.types.warning_list

        out["warnings"] = capo_kendra.types.warning_list.deserialize_aws_json_1_1(
            data["Warnings"]
        )
    if data.get("SpellCorrectedQueries") is not None:
        import capo_kendra.types.spell_corrected_query_list

        out["spell_corrected_queries"] = (
            capo_kendra.types.spell_corrected_query_list.deserialize_aws_json_1_1(
                data["SpellCorrectedQueries"]
            )
        )
    if data.get("FeaturedResultsItems") is not None:
        import capo_kendra.types.featured_results_item_list

        out["featured_results_items"] = (
            capo_kendra.types.featured_results_item_list.deserialize_aws_json_1_1(
                data["FeaturedResultsItems"]
            )
        )
    return out
