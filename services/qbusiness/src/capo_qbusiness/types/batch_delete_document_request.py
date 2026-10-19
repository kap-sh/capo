"""Generated from Smithy shape ``com.amazonaws.qbusiness#BatchDeleteDocumentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.delete_documents
    import capo_qbusiness.types.execution_id
    import capo_qbusiness.types.index_id


class BatchDeleteDocumentRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application.</p>"""
    index_id: "capo_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the Amazon Q Business index that contains the documents to delete.</p>"""
    documents: "capo_qbusiness.types.delete_documents.DeleteDocuments"
    """<p>Documents deleted from the Amazon Q Business index.</p>"""
    data_source_sync_id: NotRequired["capo_qbusiness.types.execution_id.ExecutionId"]
    """<p>The identifier of the data source sync during which the documents were deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDocumentRequest) -> dict:
    out: dict = {}
    import capo_qbusiness.types.delete_documents

    out["documents"] = capo_qbusiness.types.delete_documents.serialize_json(
        value["documents"]
    )
    if "data_source_sync_id" in value:
        out["dataSourceSyncId"] = value["data_source_sync_id"]
    return out


def deserialize_json(data: dict) -> BatchDeleteDocumentRequest:
    out: BatchDeleteDocumentRequest = {}  # type: ignore[typeddict-item]
    if data.get("documents") is not None:
        import capo_qbusiness.types.delete_documents

        out["documents"] = capo_qbusiness.types.delete_documents.deserialize_json(
            data["documents"]
        )
    else:
        out["documents"] = []
    if data.get("dataSourceSyncId") is not None:
        out["data_source_sync_id"] = data["dataSourceSyncId"]
    return out
