"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeFeaturedResultsSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.featured_document_missing_list
    import capo_kendra.types.featured_document_with_metadata_list
    import capo_kendra.types.featured_results_set_description
    import capo_kendra.types.featured_results_set_id
    import capo_kendra.types.featured_results_set_name
    import capo_kendra.types.featured_results_set_status
    import capo_kendra.types.long
    import capo_kendra.types.query_text_list


class DescribeFeaturedResultsSetResponse(TypedDict, closed=True):
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
    """<p>The list of queries for featuring results. For more information on the list of queries, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_FeaturedResultsSet.html">FeaturedResultsSet</a>.</p>"""
    featured_documents_with_metadata: NotRequired[
        "capo_kendra.types.featured_document_with_metadata_list.FeaturedDocumentWithMetadataList"
    ]
    """<p>The list of document IDs for the documents you want to feature with their metadata information. For more information on the list of featured documents, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_FeaturedResultsSet.html">FeaturedResultsSet</a>.</p>"""
    featured_documents_missing: NotRequired[
        "capo_kendra.types.featured_document_missing_list.FeaturedDocumentMissingList"
    ]
    """<p>The list of document IDs that don't exist but you have specified as featured documents. Amazon Kendra cannot feature these documents if they don't exist in the index. You can check the status of a document and its ID or check for documents with status errors using the <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_BatchGetDocumentStatus.html">BatchGetDocumentStatus</a> API.</p>"""
    last_updated_timestamp: NotRequired["capo_kendra.types.long.Long"]
    """<p>The timestamp when the set of featured results was last updated.</p>"""
    creation_timestamp: NotRequired["capo_kendra.types.long.Long"]
    """<p>The Unix timestamp when the set of the featured results was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFeaturedResultsSetResponse) -> dict:
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
    if "featured_documents_with_metadata" in value:
        import capo_kendra.types.featured_document_with_metadata_list

        out["FeaturedDocumentsWithMetadata"] = (
            capo_kendra.types.featured_document_with_metadata_list.serialize_aws_json_1_1(
                value["featured_documents_with_metadata"]
            )
        )
    if "featured_documents_missing" in value:
        import capo_kendra.types.featured_document_missing_list

        out["FeaturedDocumentsMissing"] = (
            capo_kendra.types.featured_document_missing_list.serialize_aws_json_1_1(
                value["featured_documents_missing"]
            )
        )
    if "last_updated_timestamp" in value:
        out["LastUpdatedTimestamp"] = value["last_updated_timestamp"]
    if "creation_timestamp" in value:
        out["CreationTimestamp"] = value["creation_timestamp"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFeaturedResultsSetResponse:
    out: DescribeFeaturedResultsSetResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("FeaturedDocumentsWithMetadata") is not None:
        import capo_kendra.types.featured_document_with_metadata_list

        out["featured_documents_with_metadata"] = (
            capo_kendra.types.featured_document_with_metadata_list.deserialize_aws_json_1_1(
                data["FeaturedDocumentsWithMetadata"]
            )
        )
    if data.get("FeaturedDocumentsMissing") is not None:
        import capo_kendra.types.featured_document_missing_list

        out["featured_documents_missing"] = (
            capo_kendra.types.featured_document_missing_list.deserialize_aws_json_1_1(
                data["FeaturedDocumentsMissing"]
            )
        )
    if data.get("LastUpdatedTimestamp") is not None:
        out["last_updated_timestamp"] = data["LastUpdatedTimestamp"]
    if data.get("CreationTimestamp") is not None:
        out["creation_timestamp"] = data["CreationTimestamp"]
    return out
