"""Generated from Smithy shape ``com.amazonaws.kendra#CreateFeaturedResultsSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.client_token_name
    import capo_kendra.types.featured_document_list
    import capo_kendra.types.featured_results_set_description
    import capo_kendra.types.featured_results_set_name
    import capo_kendra.types.featured_results_set_status
    import capo_kendra.types.index_id
    import capo_kendra.types.query_text_list
    import capo_kendra.types.tag_list


class CreateFeaturedResultsSetRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index that you want to use for featuring results.</p>"""
    featured_results_set_name: (
        "capo_kendra.types.featured_results_set_name.FeaturedResultsSetName"
    )
    """<p>A name for the set of featured results.</p>"""
    description: NotRequired[
        "capo_kendra.types.featured_results_set_description.FeaturedResultsSetDescription"
    ]
    """<p>A description for the set of featured results.</p>"""
    client_token: NotRequired["capo_kendra.types.client_token_name.ClientTokenName"]
    """<p>A token that you provide to identify the request to create a set of featured results. Multiple calls to the <code>CreateFeaturedResultsSet</code> API with the same client token will create only one featured results set.</p>"""
    status: NotRequired[
        "capo_kendra.types.featured_results_set_status.FeaturedResultsSetStatus"
    ]
    """<p>The current status of the set of featured results. When the value is <code>ACTIVE</code>, featured results are ready for use. You can still configure your settings before setting the status to <code>ACTIVE</code>. You can set the status to <code>ACTIVE</code> or <code>INACTIVE</code> using the <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateFeaturedResultsSet.html">UpdateFeaturedResultsSet</a> API. The queries you specify for featured results must be unique per featured results set for each index, whether the status is <code>ACTIVE</code> or <code>INACTIVE</code>.</p>"""
    query_texts: NotRequired["capo_kendra.types.query_text_list.QueryTextList"]
    """<p>A list of queries for featuring results. For more information on the list of queries, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_FeaturedResultsSet.html">FeaturedResultsSet</a>.</p>"""
    featured_documents: NotRequired[
        "capo_kendra.types.featured_document_list.FeaturedDocumentList"
    ]
    """<p>A list of document IDs for the documents you want to feature at the top of the search results page. For more information on the list of documents, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_FeaturedResultsSet.html">FeaturedResultsSet</a>.</p>"""
    tags: NotRequired["capo_kendra.types.tag_list.TagList"]
    """<p>A list of key-value pairs that identify or categorize the featured results set. You can also use tags to help control access to the featured results set. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols:_ . : / = + - @.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFeaturedResultsSetRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["FeaturedResultsSetName"] = value["featured_results_set_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
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
    if "tags" in value:
        import capo_kendra.types.tag_list

        out["Tags"] = capo_kendra.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFeaturedResultsSetRequest:
    out: CreateFeaturedResultsSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("CreateFeaturedResultsSetRequest.index_id required")
    if data.get("FeaturedResultsSetName") is not None:
        out["featured_results_set_name"] = data["FeaturedResultsSetName"]
    else:
        raise DeserializationError(
            "CreateFeaturedResultsSetRequest.featured_results_set_name required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
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
    if data.get("Tags") is not None:
        import capo_kendra.types.tag_list

        out["tags"] = capo_kendra.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
