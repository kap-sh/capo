"""Generated from Smithy shape ``com.amazonaws.kendra#FeaturedResultsSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.featured_document_list
    import capo_kendra.types.featured_results_set_description
    import capo_kendra.types.featured_results_set_id
    import capo_kendra.types.featured_results_set_name
    import capo_kendra.types.featured_results_set_status
    import capo_kendra.types.long
    import capo_kendra.types.query_text_list


class FeaturedResultsSet(TypedDict, closed=True):
    featured_results_set_id: NotRequired[
        "capo_kendra.types.featured_results_set_id.FeaturedResultsSetId"
    ]
    """<p>The identifier of the set of featured results.</p>"""
    featured_results_set_name: NotRequired[
        "capo_kendra.types.featured_results_set_name.FeaturedResultsSetName"
    ]
    """<p>The name for the set of featured results.</p>"""
    description: NotRequired[
        "capo_kendra.types.featured_results_set_description.FeaturedResultsSetDescription"
    ]
    """<p>The description for the set of featured results.</p>"""
    status: NotRequired[
        "capo_kendra.types.featured_results_set_status.FeaturedResultsSetStatus"
    ]
    """<p>The current status of the set of featured results. When the value is <code>ACTIVE</code>, featured results are ready for use. You can still configure your settings before setting the status to <code>ACTIVE</code>. You can set the status to <code>ACTIVE</code> or <code>INACTIVE</code> using the <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateFeaturedResultsSet.html">UpdateFeaturedResultsSet</a> API. The queries you specify for featured results must be unique per featured results set for each index, whether the status is <code>ACTIVE</code> or <code>INACTIVE</code>.</p>"""
    query_texts: NotRequired["capo_kendra.types.query_text_list.QueryTextList"]
    """<p>The list of queries for featuring results.</p> <p>Specific queries are mapped to specific documents for featuring in the results. If a query contains an exact match, then one or more specific documents are featured in the results. The exact match applies to the full query. For example, if you only specify 'Kendra', queries such as 'How does kendra semantically rank results?' will not render the featured results. Featured results are designed for specific queries, rather than queries that are too broad in scope.</p>"""
    featured_documents: NotRequired[
        "capo_kendra.types.featured_document_list.FeaturedDocumentList"
    ]
    """<p>The list of document IDs for the documents you want to feature at the top of the search results page. You can use the <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_Query.html">Query</a> API to search for specific documents with their document IDs included in the result items, or you can use the console.</p> <p>You can add up to four featured documents. You can request to increase this limit by contacting <a href="http://aws.amazon.com/contact-us/">Support</a>.</p> <p>Specific queries are mapped to specific documents for featuring in the results. If a query contains an exact match, then one or more specific documents are featured in the results. The exact match applies to the full query. For example, if you only specify 'Kendra', queries such as 'How does kendra semantically rank results?' will not render the featured results. Featured results are designed for specific queries, rather than queries that are too broad in scope.</p>"""
    last_updated_timestamp: NotRequired["capo_kendra.types.long.Long"]
    """<p>The Unix timestamp when the set of featured results was last updated.</p>"""
    creation_timestamp: NotRequired["capo_kendra.types.long.Long"]
    """<p>The Unix timestamp when the set of featured results was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturedResultsSet) -> dict:
    out: dict = {}
    if "featured_results_set_id" in value:
        out["FeaturedResultsSetId"] = value["featured_results_set_id"]
    if "featured_results_set_name" in value:
        out["FeaturedResultsSetName"] = value["featured_results_set_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_kendra.types.featured_results_set_status

        out["Status"] = (
            capo_kendra.types.featured_results_set_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "query_texts" in value:
        import capo_kendra.types.query_text_list

        out["QueryTexts"] = capo_kendra.types.query_text_list.serialize_aws_json_1_1(
            value["query_texts"]
        )
    if "featured_documents" in value:
        import capo_kendra.types.featured_document_list

        out["FeaturedDocuments"] = (
            capo_kendra.types.featured_document_list.serialize_aws_json_1_1(
                value["featured_documents"]
            )
        )
    if "last_updated_timestamp" in value:
        out["LastUpdatedTimestamp"] = value["last_updated_timestamp"]
    if "creation_timestamp" in value:
        out["CreationTimestamp"] = value["creation_timestamp"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FeaturedResultsSet:
    out: FeaturedResultsSet = {}  # type: ignore[typeddict-item]
    if data.get("FeaturedResultsSetId") is not None:
        out["featured_results_set_id"] = data["FeaturedResultsSetId"]
    if data.get("FeaturedResultsSetName") is not None:
        out["featured_results_set_name"] = data["FeaturedResultsSetName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        import capo_kendra.types.featured_results_set_status

        out["status"] = (
            capo_kendra.types.featured_results_set_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("QueryTexts") is not None:
        import capo_kendra.types.query_text_list

        out["query_texts"] = capo_kendra.types.query_text_list.deserialize_aws_json_1_1(
            data["QueryTexts"]
        )
    if data.get("FeaturedDocuments") is not None:
        import capo_kendra.types.featured_document_list

        out["featured_documents"] = (
            capo_kendra.types.featured_document_list.deserialize_aws_json_1_1(
                data["FeaturedDocuments"]
            )
        )
    if data.get("LastUpdatedTimestamp") is not None:
        out["last_updated_timestamp"] = data["LastUpdatedTimestamp"]
    if data.get("CreationTimestamp") is not None:
        out["creation_timestamp"] = data["CreationTimestamp"]
    return out
