"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetDocumentContentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.data_source_id
    import capo_qbusiness.types.document_id
    import capo_qbusiness.types.index_id
    import capo_qbusiness.types.output_format


class GetDocumentContentRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of the Amazon Q Business application containing the document. This ensures the request is scoped to the correct application environment and its associated security policies.</p>"""
    index_id: "capo_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the index where documents are indexed.</p>"""
    data_source_id: NotRequired["capo_qbusiness.types.data_source_id.DataSourceId"]
    """<p>The identifier of the data source from which the document was ingested. This field is not present if the document is ingested by directly calling the BatchPutDocument API. If the document is from a file-upload data source, the datasource will be "uploaded-docs-file-stat-datasourceid".</p>"""
    document_id: "capo_qbusiness.types.document_id.DocumentId"
    """<p>The unique identifier of the document that is indexed via BatchPutDocument API or file-upload or connector sync. It is also found in chat or chatSync response.</p>"""
    output_format: NotRequired["capo_qbusiness.types.output_format.OutputFormat"]
    """<p>Document outputFormat. Defaults to RAW if not selected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDocumentContentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDocumentContentRequest:
    out: GetDocumentContentRequest = {}  # type: ignore[typeddict-item]
    return out
