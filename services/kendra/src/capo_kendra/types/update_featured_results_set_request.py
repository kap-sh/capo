"""Generated from Smithy shape ``com.amazonaws.kendra#UpdateFeaturedResultsSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.featured_document_list
    import capo_kendra.types.featured_results_set_description
    import capo_kendra.types.featured_results_set_id
    import capo_kendra.types.featured_results_set_name
    import capo_kendra.types.featured_results_set_status
    import capo_kendra.types.index_id
    import capo_kendra.types.query_text_list


class UpdateFeaturedResultsSetRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index used for featuring results.</p>"""
    featured_results_set_id: (
        "capo_kendra.types.featured_results_set_id.FeaturedResultsSetId"
    )
    """<p>The identifier of the set of featured results that you want to update.</p>"""
    featured_results_set_name: NotRequired[
        "capo_kendra.types.featured_results_set_name.FeaturedResultsSetName"
    ]
    """<p>A new name for the set of featured results.</p>"""
    description: NotRequired[
        "capo_kendra.types.featured_results_set_description.FeaturedResultsSetDescription"
    ]
    """<p>A new description for the set of featured results.</p>"""
    status: NotRequired[
        "capo_kendra.types.featured_results_set_status.FeaturedResultsSetStatus"
    ]
    """<p>You can set the status to <code>ACTIVE</code> or <code>INACTIVE</code>. When the value is <code>ACTIVE</code>, featured results are ready for use. You can still configure your settings before setting the status to <code>ACTIVE</code>. The queries you specify for featured results must be unique per featured results set for each index, whether the status is <code>ACTIVE</code> or <code>INACTIVE</code>.</p>"""
    query_texts: NotRequired["capo_kendra.types.query_text_list.QueryTextList"]
    """<p>A list of queries for featuring results. For more information on the list of queries, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_FeaturedResultsSet.html">FeaturedResultsSet</a>.</p>"""
    featured_documents: NotRequired[
        "capo_kendra.types.featured_document_list.FeaturedDocumentList"
    ]
    """<p>A list of document IDs for the documents you want to feature at the top of the search results page. For more information on the list of featured documents, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_FeaturedResultsSet.html">FeaturedResultsSet</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFeaturedResultsSetRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFeaturedResultsSetRequest:
    out: UpdateFeaturedResultsSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("UpdateFeaturedResultsSetRequest.index_id required")
    if data.get("FeaturedResultsSetId") is not None:
        out["featured_results_set_id"] = data["FeaturedResultsSetId"]
    else:
        raise DeserializationError(
            "UpdateFeaturedResultsSetRequest.featured_results_set_id required"
        )
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
    return out
